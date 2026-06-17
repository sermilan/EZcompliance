#!/usr/bin/env python3
"""
基于受控词表的智能双链标注脚本 v2.0
- 读取 controlled_vocabulary.yml 词表
- 对正文进行智能双链标注
- 生成关联关系区
- 保持原文不变，仅添加标注
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
VOCAB_FILE = VAULT_DIR / ".claude/controlled_vocabulary.yml"

# 加载受控词表
def load_vocabulary():
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 构建匹配模式：优先匹配长名称
def build_match_patterns(vocab):
    patterns = []
    for category, items in vocab.items():
        for item in items:
            canonical = item['canonical']
            aliases = item.get('aliases', [])
            # 先按长度排序，优先匹配长名称
            all_names = sorted([canonical] + aliases, key=len, reverse=True)
            for name in all_names:
                patterns.append({
                    'name': name,
                    'canonical': canonical,
                    'category': category
                })
    # 按长度降序排列，避免短词优先匹配
    patterns.sort(key=lambda x: len(x['name']), reverse=True)
    return patterns

# 解析frontmatter
def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm, content[len(parts[0]) + len(parts[1]) + 6:]
    except:
        return None, content

# 检查段落是否在代码块中
def is_in_code_block(lines, pos):
    """检查pos位置是否在代码块中"""
    in_block = False
    block_count = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            if in_block:
                block_count -= 1
                if block_count == 0:
                    in_block = False
            else:
                in_block = True
                block_count = 1
        if in_block and i == pos:
            return True
    return False

# 添加正文双链
def add_wikilinks(content, patterns, max_per_file=50):
    """在正文中添加双链，使用词表匹配"""
    lines = content.split('\n')
    new_lines = []
    link_count = 0
    added_links = set()  # 已添加的链接，避免重复

    for line in lines:
        # 跳过frontmatter区域（已在---之间）
        if line.strip() == '---':
            new_lines.append(line)
            continue

        # 跳过代码块
        if line.strip().startswith('```'):
            new_lines.append(line)
            continue

        # 跳过已有wikilink的行（如果整行都是链接列表）
        if line.strip().startswith('- [[') or line.strip().startswith('[['):
            new_lines.append(line)
            continue

        # 跳过标题行（# 开头）
        if re.match(r'^#{1,6}\s+', line):
            new_lines.append(line)
            continue

        # 在正文中查找概念
        modified_line = line
        for pattern in patterns:
            name = pattern['name']
            canonical = pattern['canonical']
            # 跳过太短的词
            if len(name) < 3:
                continue
            # 检查是否已添加过这个规范名
            if canonical in added_links:
                continue
            # 构造正则，确保匹配完整词
            escaped_name = re.escape(name)
            # 匹配独立词组
            regex = rf'(?<!\[\[)(?<!\w)({escaped_name})(?!\]\])'
            if re.search(regex, modified_line):
                # 替换为wikilink
                if name != canonical:
                    replacement = f'[[{canonical}|{name}]]'
                else:
                    replacement = f'[[{canonical}]]'
                modified_line = re.sub(regex, replacement, modified_line, count=1)
                added_links.add(canonical)
                link_count += 1
                if link_count >= max_per_file:
                    break

        new_lines.append(modified_line)
        if link_count >= max_per_file:
            break

    return '\n'.join(new_lines), link_count, list(added_links)

# 生成关联关系区
def generate_relationship_section(found_concepts, frontmatter):
    """根据找到的概念生成关联关系区"""
    sections = {
        '相关法规': [],
        '相关标准': [],
        '核心概念': [],
        '适用场景': [],
        '监管主体': []
    }

    # 从found_concepts中分类
    for concept in found_concepts:
        cat = concept['category']
        canonical = concept['canonical']
        link = f'[[{canonical}]]'

        if cat == 'laws':
            sections['相关法规'].append(link)
        elif cat == 'regulations':
            sections['相关法规'].append(link)
        elif cat == 'standards':
            sections['相关标准'].append(link)
        elif cat == 'concepts':
            sections['核心概念'].append(link)
        elif cat == 'scenarios':
            sections['适用场景'].append(link)
        elif cat == 'institutions':
            sections['监管主体'].append(link)

    # 构建关系区文本
    lines = ['\n\n---\n\n## 关联关系\n']
    for section_name, items in sections.items():
        if items:
            # 去重
            unique_items = list(dict.fromkeys(items))
            lines.append(f'\n- {section_name}：')
            for item in unique_items[:5]:  # 最多5个
                lines.append(f'  {item}')

    return '\n'.join(lines)

# 主处理函数
def process_file(filepath, patterns):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        # 分析正文中的概念
        found = []
        for pattern in patterns:
            name = pattern['name']
            if len(name) < 3:
                continue
            escaped_name = re.escape(name)
            if re.search(rf'(?<!\[\[)(?<!\w)({escaped_name})(?!\]\])', body):
                found.append(pattern)

        # 统计找到的概念
        canonical_found = {}
        for p in found:
            if p['canonical'] not in canonical_found:
                canonical_found[p['canonical']] = p

        # 生成关联关系区
        rel_section = generate_relationship_section(canonical_found.values(), frontmatter)

        # 检查是否已有关系区
        if '## 关联关系' in body:
            # 已有关联关系区，跳过
            return False, 'skipped', 0, []

        # 添加关系区
        new_content = body.rstrip() + rel_section

        # 构建新文件内容
        if frontmatter:
            fm_text = '---\n' + yaml.dump(frontmatter, allow_unicode=True, sort_keys=False) + '---\n\n'
            new_content = fm_text + new_content
        else:
            new_content = '---\ntitle: ""\ntype: ""\n---\n\n' + new_content

        # 保存
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, 'processed', len(canonical_found), list(canonical_found.keys())
    except Exception as e:
        return False, f'error: {str(e)}', 0, []

def main():
    print("=" * 60)
    print("基于受控词表的智能双链标注 v2.0")
    print("=" * 60)

    # 加载词表
    print(f"\n加载词表: {VOCAB_FILE}")
    vocab = load_vocabulary()
    patterns = build_match_patterns(vocab)

    # 统计词表
    total_terms = sum(len(items) for items in vocab.values())
    print(f"词表加载完成: {total_terms} 个术语")

    # 获取所有md文件
    md_files = list(POLICY_DIR.glob("*.md"))
    print(f"总文件数: {len(md_files)}")

    # 找出需要处理的文件（还没有关联关系区的）
    files_to_process = []
    for f in md_files:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                content = fp.read()
            frontmatter, body = parse_frontmatter(content)
            if '## 关联关系' not in body and body.strip():
                files_to_process.append(f)
        except:
            continue

    print(f"需要处理的文件数: {len(files_to_process)}")

    # 处理文件
    processed = 0
    skipped = 0
    errors = 0
    total_concepts = 0

    for i, filepath in enumerate(files_to_process):
        success, status, concept_count, concepts = process_file(filepath, patterns)
        if status == 'processed':
            processed += 1
            total_concepts += concept_count
        elif status == 'skipped':
            skipped += 1
        else:
            errors += 1

        if (i + 1) % 100 == 0:
            print(f"进度: {i+1}/{len(files_to_process)} - 已处理: {processed}, 跳过: {skipped}, 错误: {errors}")

    print(f"\n完成!")
    print(f"  已处理: {processed} 个文件")
    print(f"  新增概念: {total_concepts} 个")
    print(f"  跳过(已有关系区): {skipped}")
    print(f"  错误: {errors}")

if __name__ == '__main__':
    main()
