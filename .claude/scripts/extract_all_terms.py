#!/usr/bin/env python3
"""
全面术语提取脚本
从所有类型的政策文件中提取术语定义
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

SEARCH_DIR = "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
OUTPUT_DIR = "/root/obsidian_vault/terms"

# 定义文件类型和分类
FILE_TYPE_PATTERNS = [
    (r'GBT?[\s_-]?\d+.*\.md', '国家标准 GB/T'),
    (r'GB\s*\d+.*\.md', '国家标准 GB'),
    (r'YD[\s_-]?\d+.*\.md', '行业标准 YD'),
    (r'JR[\s_-]?\d+.*\.md', '金融行业标准 JR'),
    (r'SJ[\s_-]?\d+.*\.md', '电子行业标准 SJ'),
    (r'中华人民共和国.*\.md', '法律'),
    (r'.*条例.*\.md', '行政法规'),
    (r'.*办法.*\.md', '部门规章'),
    (r'.*规定.*\.md', '部门规章'),
    (r'.*指南.*\.md', '指南/规范'),
    (r'.*白皮书.*\.md', '白皮书'),
    (r'.*报告.*\.md', '研究报告'),
]


def classify_file(filename):
    """识别文件类型"""
    for pattern, ftype in FILE_TYPE_PATTERNS:
        if re.search(pattern, filename, re.IGNORECASE):
            return ftype
    return '其他'


def extract_terms_from_content(content, filename, file_type):
    """通用术语提取"""
    terms = []

    # 1. 提取"术语和定义"章节（GB标准格式）
    if '术语和定义' in content:
        terms.extend(extract_gb_terms(content, filename))

    # 2. 提取法律定义条款（"本法所称"、"是指"格式）
    if file_type in ['法律', '行政法规', '部门规章']:
        terms.extend(extract_law_definitions(content, filename))

    # 3. 提取"下列术语适用于本文件"格式
    terms.extend(extract_applicable_terms(content, filename))

    return terms


def extract_gb_terms(content, filename):
    """提取 GB 标准格式的术语"""
    terms = []
    in_term_section = False
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if '术语和定义' in line:
            in_term_section = True
            i += 1
            continue

        if in_term_section and re.match(r'^#+\s*[45]\s', line):
            break

        if not in_term_section:
            i += 1
            continue

        num_match = re.match(r'^(\d+\.\d+)\s*$', line)
        if num_match:
            term_num = num_match.group(1)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1

            if i >= len(lines):
                break

            term_line = lines[i].strip()
            term_line = re.sub(r'^##?\s*', '', term_line)
            parts = re.split(r'\s+', term_line, 1)
            cn_name = parts[0] if parts else ''
            en_name = parts[1] if len(parts) > 1 else ''

            i += 1
            definitions = []
            while i < len(lines):
                current = lines[i]
                if re.match(r'^\d+\.\d+\s*$', current.strip()):
                    break
                if re.match(r'^---', current) or re.match(r'^#+\s*\d', current):
                    break
                if current.strip().startswith('[') and current.strip().endswith(']'):
                    i += 1
                    continue
                if not current.strip():
                    i += 1
                    continue
                stripped = current.strip()
                if len(stripped) <= 2 and not stripped[0].isdigit():
                    i += 1
                    continue
                definitions.append(current.strip())
                i += 1

            def_text = ' '.join(definitions).strip()
            def_text = re.sub(r'\s+', ' ', def_text)

            if cn_name and def_text:
                terms.append({
                    'term': cn_name,
                    'en': en_name,
                    'definition': def_text[:500],
                    'source': filename,
                    'type': 'standard'
                })
            continue

        i += 1

    return terms


def extract_law_definitions(content, filename):
    """提取法律定义条款"""
    terms = []

    # 匹配模式1: "本法所称XXX，是指/为/指..."
    pattern1 = re.compile(r'[本法本条例本办法]所称([^，。,]+?)[，,是]?\s*(?:指|为|是|\b)([^。；;。\n]+?)(?:[。；;]|$)')

    # 匹配模式2: "XXX是指..." (开头的定义)
    pattern2 = re.compile(r'^([^，。,：:]{2,30})\s*(?:是|指|为)\s*([^。；;。\n]+?)(?:[。；;]|$)', re.MULTILINE)

    for match in pattern1.finditer(content):
        term_name = match.group(1).strip()
        definition = match.group(2).strip()
        if len(term_name) >= 2 and len(definition) >= 4:
            terms.append({
                'term': term_name,
                'definition': definition[:300],
                'source': filename,
                'type': 'law'
            })

    for match in pattern2.finditer(content):
        term_name = match.group(1).strip()
        definition = match.group(2).strip()
        if len(term_name) >= 2 and len(definition) >= 4 and not term_name.startswith('第'):
            terms.append({
                'term': term_name,
                'definition': definition[:300],
                'source': filename,
                'type': 'law'
            })

    return terms


def extract_applicable_terms(content, filename):
    """提取'下列术语适用于本文件'格式的定义"""
    terms = []

    # 匹配 "XXX：YYY" 或 "XXX——YYY" 格式的简短定义
    pattern = re.compile(r'^([^：:\n]{2,30})\s*[:：]\s*([^。\n]{4,100})', re.MULTILINE)

    in_applicable = False
    for line in content.split('\n'):
        if '下列术语' in line and '适用' in line:
            in_applicable = True
            continue
        if in_applicable and re.match(r'^#+\s*\d', line):
            break
        if in_applicable:
            match = pattern.match(line.strip())
            if match:
                term_name = match.group(1).strip()
                definition = match.group(2).strip()
                if len(term_name) >= 2:
                    terms.append({
                        'term': term_name,
                        'definition': definition,
                        'source': filename,
                        'type': 'applicable'
                    })

    return terms


def extract_abbreviations(content):
    """提取缩略语"""
    abbrevs = {}
    in_abbrev = False

    for line in content.split('\n'):
        if '缩略语' in line:
            in_abbrev = True
            continue
        if in_abbrev:
            if re.match(r'^##?\s*\d', line) or line.startswith('---'):
                break
            match = re.match(r'\s*([A-Z][A-Z0-9\-]+):\s*(.+?)(?:\n|$)', line)
            if match:
                abbrev = match.group(1)
                rest = match.group(2).strip()
                rest = re.sub(r'\(.+?\)', '', rest).strip()
                abbrevs[abbrev] = rest

    return abbrevs


def main():
    print("=" * 60)
    print("全面术语提取器")
    print("=" * 60)

    files = [f for f in os.listdir(SEARCH_DIR) if f.endswith('.md')]
    print(f"\n[1] 扫描文件... 共 {len(files)} 个")

    # 按类型统计
    type_stats = defaultdict(list)
    all_terms = []
    all_abbrevs = {}

    for i, fname in enumerate(files):
        if i % 100 == 0:
            print(f"  处理进度: {i}/{len(files)}")

        fpath = os.path.join(SEARCH_DIR, fname)
        ftype = classify_file(fname)
        type_stats[ftype].append(fname)

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        terms = extract_terms_from_content(content, fname, ftype)
        abbrevs = extract_abbreviations(content)

        all_terms.extend(terms)
        all_abbrevs.update(abbrevs)

    print(f"  处理完成: {len(files)}/{len(files)}")

    # 去重
    seen = set()
    unique_terms = []
    for t in all_terms:
        key = (t['term'], t.get('source', ''))
        if key not in seen and len(t['term']) >= 2:
            seen.add(key)
            unique_terms.append(t)

    # 按来源文件分组
    by_source = defaultdict(list)
    for t in unique_terms:
        by_source[t['source']].append(t)

    print(f"\n[2] 提取结果:")
    print(f"    术语总数: {len(unique_terms)}")
    print(f"    缩略语总数: {len(all_abbrevs)}")

    print(f"\n[3] 文件类型分布:")
    for ftype, flist in sorted(type_stats.items(), key=lambda x: -len(x[1])):
        print(f"    {ftype}: {len(flist)} 个文件")

    # 输出到多个文件
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 主术语表
    main_output = {
        'metadata': {
            'generated': '2026-04-29',
            'total_terms': len(unique_terms),
            'total_abbrevs': len(all_abbrevs),
            'file_count': len(files),
            'categories': {k: len(v) for k, v in type_stats.items()}
        },
        'abbreviations': all_abbrevs,
        'terms': unique_terms
    }

    with open(f"{OUTPUT_DIR}/all_terms.yml", 'w', encoding='utf-8') as f:
        f.write("# 政策标准术语总表\n")
        f.write("# 自动从 PolicyArchive 中提取\n\n")
        yaml.dump(main_output, f, allow_unicode=True, sort_keys=False)

    # 按类别拆分
    for ftype in ['法律', '行政法规', '国家标准 GB/T', '国家标准 GB']:
        ftype_terms = [t for t in unique_terms if
                       any(ftype.lower() in classify_file(t['source']).lower() for _ in [1])]
        ftype_terms = [t for t in unique_terms if classify_file(t['source']) == ftype]
        if ftype_terms:
            with open(f"{OUTPUT_DIR}/terms_{ftype.replace('/', '_').replace(' ', '_')}.yml", 'w', encoding='utf-8') as f:
                yaml.dump({'terms': ftype_terms}, f, allow_unicode=True, sort_keys=False)

    print(f"\n[4] 输出文件:")
    print(f"    {OUTPUT_DIR}/all_terms.yml")

    # 显示样例
    print(f"\n[5] 术语样例 (前10个):")
    for t in unique_terms[:10]:
        print(f"    [{t.get('type', '?')}] {t['term']}: {t['definition'][:50]}...")

    return unique_terms, all_abbrevs, type_stats


if __name__ == '__main__':
    main()