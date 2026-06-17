#!/usr/bin/env python3
"""
极简标注脚本 - 只保留关系区，不添加正文双链
避免破坏原有内容
"""

import os
import re
import yaml
from pathlib import Path
import time

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
VOCAB_FILE = VAULT_DIR / ".claude/controlled_vocabulary_focused.yml"

def load_vocab():
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab = yaml.safe_load(f)

    term_map = {}
    for category, items in vocab.items():
        for item in items:
            canonical = item['canonical']
            for alias in item.get('aliases', []) + [canonical]:
                if len(alias) >= 2:
                    term_map[alias] = (canonical, category)

    return term_map, sorted(term_map.keys(), key=len, reverse=True)

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm, parts[2]
    except:
        return None, content

def find_concepts(body, term_map, sorted_terms):
    """在正文中查找概念（不修改，只统计）"""
    found = set()
    for term in sorted_terms:
        if term in body:
            canonical, cat = term_map[term]
            found.add((canonical, cat))
    return list(found)

def generate_relationship_section(found_items):
    sections = {'法律依据': [], '相关标准': [], '核心制度': [], '数据类型': [], '监管机构': []}

    for canonical, category in found_items:
        link = f'[[{canonical}]]'
        if category in ['laws', 'regulations']:
            sections['法律依据'].append(link)
        elif category == 'standards':
            sections['相关标准'].append(link)
        elif category == 'concepts':
            if any(k in canonical for k in ['制度', '保护', '审查', '评估', '等级']):
                sections['核心制度'].append(link)
            elif any(k in canonical for k in ['个人', '重要', '核心', '数据']):
                sections['数据类型'].append(link)
            else:
                sections['核心制度'].append(link)
        elif category == 'institutions':
            sections['监管机构'].append(link)

    lines = []
    for name, items in sections.items():
        if items:
            unique = list(dict.fromkeys(items))[:6]
            lines.append(f'- {name}：')
            for item in unique:
                lines.append(f'  {item}')
    return '\n'.join(lines) if lines else ''

def extract_std_num(filename):
    patterns = [
        (r'GB/\w\s*\d+[\-–]\d+', 'GB/T'),
        (r'GA/\w\s*\d+[\-–]\d+', 'GA/T'),
        (r'YD/?T\s*\d+[\-–]\d+', 'YD/T'),
        (r'GBT?\s*(\d+)[\-–](\d+)', 'GB/T'),
    ]
    for p, prefix in patterns:
        m = re.search(p, filename, re.I)
        if m:
            num = re.sub(r'\s+', '', m.group(0))
            if prefix and not num.startswith(prefix):
                num = num.replace('GB', prefix, 1).replace('GA', prefix, 1)
            return num
    return None

def process_file(filepath, term_map, sorted_terms):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()

        fm, body = parse_frontmatter(raw)
        filename = filepath.name

        # 删除旧关系区（不修改正文）
        body = re.sub(r'\n##\s*(相关文档|关联关系)[^\n]*\n.*?(?=\n---\n|\n##\s|\Z)', '', body, flags=re.DOTALL)

        # 查找概念
        found_items = find_concepts(body, term_map, sorted_terms)

        # 生成关系区
        rel_section = generate_relationship_section(found_items)
        new_body = body.rstrip() + '\n\n---\n\n## 关联关系\n' + rel_section

        # 更新frontmatter（不改变已有内容）
        if fm is None:
            fm = {}
        fm['title'] = fm.get('title', Path(filename).stem)
        std_num = extract_std_num(filename)
        if std_num and not fm.get('standard_number'):
            fm['standard_number'] = std_num
        if not fm.get('status'):
            fm['status'] = '现行有效'
        if not fm.get('level'):
            fm['level'] = 'document'
        if 'related' in fm and fm['related']:
            fm['related'] = [str(r).strip() for r in fm['related'] if r and str(r) != 'None']

        new_content = '---\n' + yaml.dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, len(found_items)
    except:
        return False, 0

def main():
    print("=" * 60)
    print("极简标注 v1 - 只保留关系区，不改正文")
    print("=" * 60)

    term_map, sorted_terms = load_vocab()
    print(f"词表: {len(term_map)} 个术语")

    files = list(POLICY_DIR.glob("*.md"))
    print(f"文件: {len(files)} 个")

    processed = 0
    total_concepts = 0
    errors = 0

    start = time.time()
    for i, fp in enumerate(files):
        ok, concepts = process_file(fp, term_map, sorted_terms)
        if ok:
            processed += 1
            total_concepts += concepts
        else:
            errors += 1

        if (i+1) % 100 == 0:
            print(f"进度: {i+1}/{len(files)} | 已处理: {processed} | 概念: {total_concepts} | 耗时: {time.time()-start:.1f}s")

    print(f"\n完成! 处理: {processed} | 总概念: {total_concepts} | 平均: {total_concepts/max(processed,1):.1f}/文件 | 耗时: {time.time()-start:.1f}s")

if __name__ == '__main__':
    main()