#!/usr/bin/env python3
"""
网络安全政策法规知识图谱标注脚本 v3.0
分层处理：
1. 文档级标注：完善 YAML frontmatter
2. 段落级标注：正文关键概念双链
3. 关系级标注：关联关系区
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

def build_match_patterns(vocab):
    """构建匹配模式，优先匹配长名称"""
    patterns = []
    for category, items in vocab.items():
        for item in items:
            canonical = item['canonical']
            aliases = item.get('aliases', [])
            all_names = sorted([canonical] + aliases, key=len, reverse=True)
            for name in all_names:
                patterns.append({
                    'name': name,
                    'canonical': canonical,
                    'category': category
                })
    patterns.sort(key=lambda x: len(x['name']), reverse=True)
    return patterns

def parse_frontmatter(content):
    """解析frontmatter"""
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

def extract_standard_info(filename, content):
    """从文件名和内容提取标准信息"""
    # 从文件名提取标准号
    patterns = [
        r'(GB/\w\s*\d+[\-–]\d+)',
        r'(GA/\w\s*\d+[\-–]\d+)',
        r'(YD/?T\s*\d+[\-–]\d+)',
        r'(DB\d+/T\s*\d+[\-–]\d+)',
        r'(SJ/?T\s*\d+[\-–]\d+)',
        r'(T/CCIA\s*\d+[\-–]\d+)',
        r'(GBT?\s*\d+[\-–]\d+)',
        r'(GAT?\s*\d+[\-–]\d+)',
        r'(GBZ?\s*\d+[\-–]\d+)',
        r'(JR/T\s*\d+[\-–]\d+)',
    ]

    for p in patterns:
        m = re.search(p, filename, re.IGNORECASE)
        if m:
            std = m.group(1)
            # 规范化格式
            std = re.sub(r'GBT\s*', 'GB/T ', std)
            std = re.sub(r'GAT\s*', 'GA/T ', std)
            std = re.sub(r'GBZ\s*', 'GB/Z ', std)
            std = re.sub(r'YD/?T\s*', 'YD/T ', std)
            std = re.sub(r'DB(\d+)/?T\s*', r'DB\1/T ', std)
            std = re.sub(r'SJ/?T\s*', 'SJ/T ', std)
            return std

    # 从内容提取
    patterns_content = [
        r'GB\s*/\s*T\s*\d+[\-–]\d+',
        r'GA\s*/\s*T\s*\d+[\-–]\d+',
        r'YD\s*/\s*T\s*\d+[\-–]\d+',
        r'GB\s*\d+[\-–]\d+',
    ]
    for p in patterns_content:
        m = re.search(p, content[:2000])
        if m:
            return m.group(0).replace(' ', '')

    return None

def extract_date(content):
    """提取发布日期"""
    patterns = [
        r'(\d{4})年(\d{1,2})月(\d{1,2})日',
        r'(\d{4})[-年](\d{1,2})[-月]',
        r'(\d{4})年(\d{1,2})月',
    ]
    for p in patterns:
        m = re.search(p, content[:2000])
        if m:
            if len(m.groups()) == 3:
                return f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"
            elif len(m.groups()) == 2:
                return f"{m.group(1)}-{m.group(2).zfill(2)}"
    return None

def extract_issuer(content, filename):
    """提取发布机构"""
    # 常见机构
    issuers = [
        ('国家互联网信息办公室', ['国家互联网信息办公室', '网信办', '国家网信办']),
        ('工业和信息化部', ['工业和信息化部', '工信部']),
        ('公安部', ['公安部', '公安部门']),
        ('国家市场监督管理总局', ['国家市场监督管理总局', '市场监管总局']),
        ('国家标准化管理委员会', ['国家标准化管理委员会', '标准委']),
        ('中国信通院', ['中国信息通信研究院', '中国信通院', '信通院']),
        ('全国信息安全标准化技术委员会', ['全国信息安全标准化技术委员会', '信安标委', 'TC260']),
        ('国家保密局', ['国家保密局', '保密局']),
        ('国家密码管理局', ['国家密码管理局', '密码管理局']),
        ('国务院', ['国务院']),
        ('全国人大常委会', ['全国人大常委会', '人大常委会']),
    ]

    for issuer, keywords in issuers:
        for kw in keywords:
            if kw in content[:3000]:
                return issuer
    return None

def determine_type(filename, content):
    """判断文档类型"""
    name = filename.lower()
    if any(k in name for k in ['白皮书', 'whitepaper']):
        return 'whitepaper'
    if any(k in name for k in ['报告', 'research']):
        return 'report'
    if any(k in name for k in ['指南', 'guide', '指引']):
        return 'guide'
    if any(k in name for k in ['标准', 'standard', '规范']):
        return 'standard'
    if any(k in name for k in ['法律', 'law', '法规', 'regulation', '条例']):
        return 'law'
    if any(k in name for k in ['规划', 'plan', '方案', '计划']):
        return 'policy'
    if any(k in name for k in ['培训', '手册', 'manual']):
        return 'manual'
    return 'document'

def determine_level(filename, content):
    """判断标准级别"""
    name = filename
    if 'GB' in name.upper() and ('T' in name or '/T' in name.upper()):
        return '国家标准'
    if 'GA' in name.upper():
        return '行业标准'
    if 'YD' in name.upper():
        return '行业标准'
    if 'JR' in name.upper():
        return '行业标准'
    if 'DB' in name.upper():
        return '地方标准'
    if 'T/' in name:
        return '团体标准'
    if 'ISO' in name.upper():
        return '国际标准'
    if any(k in name for k in ['法律', '条例', '办法', '规定', '细则']):
        return '行政法规'
    return 'document'

def add_body_wikilinks(body, patterns, max_links=30):
    """在正文中添加双链"""
    lines = body.split('\n')
    new_lines = []
    link_count = 0
    added = set()
    in_code_block = False

    for line in lines:
        # 切换代码块状态
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        # 跳过代码块
        if in_code_block:
            new_lines.append(line)
            continue

        # 跳过frontmatter边界
        if line.strip() == '---':
            new_lines.append(line)
            continue

        # 跳过标题行
        if re.match(r'^#{1,6}\s+', line):
            new_lines.append(line)
            continue

        # 跳过已有wikilink的行
        if '[[' in line:
            new_lines.append(line)
            continue

        # 跳过列表行（关系区等）
        if re.match(r'^[-*]\s+', line.strip()) and len(line.strip()) < 100:
            new_lines.append(line)
            continue

        # 在正文中查找概念
        modified_line = line
        for pattern in patterns:
            if link_count >= max_links:
                break
            name = pattern['name']
            canonical = pattern['canonical']
            if len(name) < 3 or canonical in added:
                continue

            escaped = re.escape(name)
            regex = rf'(?<!\[\[)(?<!\w)({escaped})(?!\]\])'
            if re.search(regex, modified_line):
                if name != canonical:
                    replacement = f'[[{canonical}|{name}]]'
                else:
                    replacement = f'[[{canonical}]]'
                modified_line = re.sub(regex, replacement, modified_line, count=1)
                added.add(canonical)
                link_count += 1

        new_lines.append(modified_line)

    return '\n'.join(new_lines), link_count, added

def generate_relationship_section(found_concepts):
    """生成关联关系区"""
    sections = {
        '相关法规': [],
        '相关标准': [],
        '核心概念': [],
        '适用场景': [],
        '监管主体': []
    }

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

    lines = ['\n\n---\n\n## 关联关系\n']
    for section_name, items in sections.items():
        if items:
            unique = list(dict.fromkeys(items))
            lines.append(f'\n- {section_name}：')
            for item in unique[:8]:
                lines.append(f'  {item}')

    return '\n'.join(lines)

def process_file(filepath, patterns):
    """处理单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)
        filename = filepath.name

        # 提取信息
        standard_number = extract_standard_info(filename, content)
        publish_date = extract_date(content)
        issuer = extract_issuer(content, filename)
        doc_type = determine_type(filename, content)
        level = determine_level(filename, content)

        # 分析正文中的概念
        found = []
        for pattern in patterns:
            name = pattern['name']
            if len(name) < 3:
                continue
            escaped = re.escape(name)
            if re.search(rf'(?<!\[\[)(?<!\w)({escaped})(?!\]\])', body):
                found.append(pattern)

        # 去重
        canonical_found = {}
        for p in found:
            if p['canonical'] not in canonical_found:
                canonical_found[p['canonical']] = p

        # 更新frontmatter
        if frontmatter is None:
            frontmatter = {}

        frontmatter['title'] = frontmatter.get('title', Path(filename).stem)
        if doc_type:
            frontmatter['type'] = doc_type
        if not frontmatter.get('domain'):
            frontmatter['domain'] = []
        if issuer:
            frontmatter['issuer'] = issuer
        if publish_date:
            frontmatter['publish_date'] = publish_date
        if not frontmatter.get('status'):
            frontmatter['status'] = '现行有效'
        if not frontmatter.get('level') or frontmatter.get('level') in ['待确认', '']:
            frontmatter['level'] = level
        if standard_number:
            frontmatter['standard_number'] = standard_number
        if not frontmatter.get('tags'):
            frontmatter['tags'] = []
        if not frontmatter.get('aliases'):
            frontmatter['aliases'] = []
        if not frontmatter.get('related'):
            frontmatter['related'] = []

        # 添加正文双链
        new_body, body_links, added_concepts = add_body_wikilinks(body, patterns, max_links=30)

        # 生成或更新关联关系区
        rel_section = generate_relationship_section(canonical_found.values())

        # 检查是否已有关系区
        if '## 关联关系' in new_body:
            # 更新现有关系区
            parts = new_body.split('## 关联关系')
            new_body = parts[0] + rel_section.replace('\n\n---\n\n', '')
        else:
            new_body = new_body.rstrip() + rel_section

        # 构建新内容
        fm_text = '---\n' + yaml.dump(frontmatter, allow_unicode=True, sort_keys=False) + '---\n\n'
        new_content = fm_text + new_body

        # 保存
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, 'processed', len(canonical_found), body_links
    except Exception as e:
        return False, f'error: {str(e)}', 0, 0

def main():
    print("=" * 60)
    print("网络安全政策法规知识图谱标注 v3.0")
    print("=" * 60)

    vocab = load_vocabulary()
    patterns = build_match_patterns(vocab)
    print(f"词表加载: {len(patterns)} 个术语模式")

    md_files = list(POLICY_DIR.glob("*.md"))
    print(f"总文件数: {len(md_files)}")

    # 处理所有文件
    processed = 0
    errors = 0
    total_body_links = 0
    total_concepts = 0

    for i, filepath in enumerate(md_files):
        success, status, concepts, body_links = process_file(filepath, patterns)
        if status == 'processed':
            processed += 1
            total_concepts += concepts
            total_body_links += body_links
        else:
            errors += 1

        if (i + 1) % 100 == 0:
            print(f"进度: {i+1}/{len(md_files)} - 已处理: {processed}, 正文双链: {total_body_links}, 概念: {total_concepts}")

    print(f"\n完成!")
    print(f"  已处理: {processed} 个文件")
    print(f"  正文新增双链: {total_body_links} 个")
    print(f"  关系区概念: {total_concepts} 个")
    print(f"  错误: {errors}")

if __name__ == '__main__':
    main()
