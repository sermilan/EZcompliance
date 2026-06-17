#!/usr/bin/env python3
"""
精准知识图谱标注脚本 v1.0
规则：
1. 不修改正文，不加正文双链
2. 只生成"知识关系"区
3. 关系类型：上位依据/下位细化/相关法规/相关标准/核心制度/核心概念/适用对象/监管主体/适用场景/合规义务
4. 只标注高价值知识节点
5. 每个文件关系区不超过20个链接
"""

import os
import re
import yaml
from pathlib import Path
import time

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
VOCAB_FILE = VAULT_DIR / ".claude/precise_vocabulary.yml"

# 加载词表
def load_vocab():
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab = yaml.safe_load(f)

    term_map = {}
    for category, items in vocab.items():
        for item in items:
            canonical = item['canonical']
            for alias in [canonical] + item.get('aliases', []):
                if len(alias) >= 2:
                    term_map[alias] = (canonical, category)

    sorted_terms = sorted(term_map.keys(), key=len, reverse=True)
    return term_map, sorted_terms

TERM_MAP, SORTED_TERMS = load_vocab()

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

def find_concepts(body):
    """在正文中查找概念"""
    found = set()
    for term in SORTED_TERMS:
        if term in body:
            canonical, cat = TERM_MAP[term]
            found.add((canonical, cat))
    return list(found)

def classify_concept(canonical, category):
    """将概念分类到关系类型"""
    # 法规类
    if category in ['laws', 'regulations']:
        if any(k in canonical for k in ['条例', '办法', '规定', '决定', '细则']):
            return '下位细化'
        return '相关法规'

    # 标准类
    if category == 'standards':
        return '相关标准'

    # 制度类 - 必须是有明确法律/标准含义的
    if category == 'concepts':
        if any(k in canonical for k in ['制度', '测评', '评估', '审查']):
            return '核心制度'
        if any(k in canonical for k in ['个人', '数据']):
            return '合规义务'

    # 机构类
    if category == 'institutions':
        return '监管主体'

    return '核心概念'

def generate_relationship_section(found_items):
    """生成结构化关系区"""
    sections = {
        '上位依据': [],
        '下位细化': [],
        '相关法规': [],
        '相关标准': [],
        '核心制度': [],
        '核心概念': [],
        '适用对象': [],
        '监管主体': [],
        '适用场景': [],
        '合规义务': []
    }

    for canonical, category in found_items:
        link = f'[[{canonical}]]'
        rel_type = classify_concept(canonical, category)
        sections[rel_type].append(link)

    lines = ['\n\n---\n\n## 知识关系\n']
    for name, items in sections.items():
        if items:
            unique = list(dict.fromkeys(items))[:5]  # 每类最多5个
            lines.append(f'- {name}：')
            for item in unique:
                lines.append(f'  {item}')

    return '\n'.join(lines)

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

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()

        fm, body = parse_frontmatter(raw)
        filename = filepath.name

        # 删除旧关系区
        body = re.sub(r'\n##\s*(相关文档|关联关系|知识关系)[^\n]*\n.*?(?=\n---\n|\n##\s|\Z)', '', body, flags=re.DOTALL)

        # 分析正文中的概念
        found_items = find_concepts(body)

        # 生成关系区
        rel_section = generate_relationship_section(found_items)
        new_body = body.rstrip() + rel_section

        # 更新frontmatter
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
    print("精准知识图谱标注 v1.0")
    print("规则：不改正文，只生成知识关系区")
    print("=" * 60)

    print(f"词表: {len(TERM_MAP)} 个术语")

    files = list(POLICY_DIR.glob("*.md"))
    print(f"文件: {len(files)} 个")

    processed = 0
    total_concepts = 0
    errors = 0

    start = time.time()
    for i, fp in enumerate(files):
        ok, concepts = process_file(fp)
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