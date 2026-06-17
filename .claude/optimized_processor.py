#!/usr/bin/env python3
"""
网络安全政策法规知识图谱标注脚本 v3.7 (修复相关字段)
"""

import os
import re
import yaml
from pathlib import Path
import time

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
VOCAB_FILE = VAULT_DIR / ".claude/controlled_vocabulary.yml"

def load_vocab_and_build_map():
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab = yaml.safe_load(f)

    term_map = {}
    for category, items in vocab.items():
        for item in items:
            canonical = item['canonical']
            for alias in item.get('aliases', []) + [canonical]:
                if len(alias) >= 3:
                    term_map[alias] = (canonical, category)

    sorted_terms = sorted(term_map.keys(), key=len, reverse=True)
    return term_map, sorted_terms

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

def extract_std_num(filename):
    patterns = [
        (r'GB/\w\s*\d+[\-–]\d+', 'GB/T'),
        (r'GA/\w\s*\d+[\-–]\d+', 'GA/T'),
        (r'YD/?T\s*\d+[\-–]\d+', 'YD/T'),
        (r'DB\d+/T\s*\d+[\-–]\d+', None),
        (r'SJ/?T\s*\d+[\-–]\d+', 'SJ/T'),
        (r'GBT?\s*(\d+)[\-–](\d+)', 'GB/T'),
        (r'GAT?\s*(\d+)[\-–](\d+)', 'GA/T'),
    ]
    for p, prefix in patterns:
        m = re.search(p, filename, re.I)
        if m:
            num = m.group(0)
            num = re.sub(r'\s+', '', num)
            if prefix and not num.startswith(prefix):
                num = num.replace('GB', prefix, 1).replace('GA', prefix, 1)
            return num
    return None

def clean_wikilinks(text):
    """清理wikilinks，处理别名格式"""
    # 处理 [[alias|display]] 格式 - 保留display
    def replace_wikilink(m):
        content = m.group(1)
        if '|' in content:
            parts = content.split('|')
            return parts[-1]
        return content

    # 替换wikilinks为纯文本
    text = re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, text)

    # 清理残留的括号
    text = re.sub(r'[\[\]]+', '', text)

    return text

def add_wikilinks_simple(text, term_map, sorted_terms, max_links=30):
    """简化版：直接替换"""
    result = text
    links_added = 0
    added = set()

    for term in sorted_terms:
        if links_added >= max_links:
            break
        if term in added:
            continue

        if term in result:
            result = result.replace(term, f'[[{term_map[term][0]}]]', 1)
            added.add(term)
            links_added += 1

    return result, links_added

def process_file(filepath, term_map, sorted_terms):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 清理wikilinks
        content = clean_wikilinks(content)

        fm, body = parse_frontmatter(content)
        filename = filepath.name

        # 删除已有关系区
        body = re.sub(r'\n##\s*(相关文档|关联关系)[^\n]*\n.*?(?=\n---\n|\n##\s|\Z)', '', body, flags=re.DOTALL)

        std_num = extract_std_num(filename)

        # 添加wikilinks
        new_body, body_links = add_wikilinks_simple(body, term_map, sorted_terms, max_links=30)

        # 查找概念
        found_canonicals = set()
        for term in sorted_terms:
            if term in body:
                found_canonicals.add(term_map[term][0])

        # 构建关系区
        sections = {'相关法规': [], '相关标准': [], '核心概念': [], '适用场景': [], '监管主体': []}
        for canonical in found_canonicals:
            for term, (canon, cat) in term_map.items():
                if canon == canonical:
                    link = f'[[{canonical}]]'
                    if cat in ['laws', 'regulations']:
                        sections['相关法规'].append(link)
                    elif cat == 'standards':
                        sections['相关标准'].append(link)
                    elif cat in ['concepts', 'subjects']:
                        sections['核心概念'].append(link)
                    elif cat == 'scenarios':
                        sections['适用场景'].append(link)
                    elif cat == 'institutions':
                        sections['监管主体'].append(link)
                    break

        rel_lines = []
        for name, items in sections.items():
            if items:
                unique = list(dict.fromkeys(items))
                rel_lines.append(f'\n- {name}：')
                for item in unique[:8]:
                    rel_lines.append(f'  {item}')

        rel_section = ''.join(rel_lines)
        new_body = new_body.rstrip() + '\n\n---\n\n## 关联关系\n' + rel_section

        # 更新frontmatter
        if fm is None:
            fm = {}
        fm['title'] = fm.get('title', Path(filename).stem)
        if std_num and not fm.get('standard_number'):
            fm['standard_number'] = std_num
        if not fm.get('status'):
            fm['status'] = '现行有效'
        if not fm.get('level') or fm.get('level') in ['待确认', '']:
            fm['level'] = 'document'

        # 清理related字段中的格式错误
        if 'related' in fm and fm['related']:
            cleaned_related = []
            for r in fm['related']:
                r = str(r).strip()
                r = re.sub(r"^'+\s*", '', r)
                r = re.sub(r"^\[+\s*", '', r)
                r = re.sub(r"\]+\s*$", '', r)
                if r and r != 'None':
                    cleaned_related.append(r)
            fm['related'] = cleaned_related

        new_content = '---\n' + yaml.dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, len(found_canonicals), body_links
    except Exception as e:
        return False, 0, 0

def main():
    print("=" * 60)
    print("知识图谱标注 v3.7 (修复相关字段)")
    print("=" * 60)

    term_map, sorted_terms = load_vocab_and_build_map()
    print(f"词表: {len(term_map)} 个术语")

    files = list(POLICY_DIR.glob("*.md"))
    print(f"文件: {len(files)} 个")

    total_concepts = 0
    total_links = 0
    processed = 0
    errors = 0

    start = time.time()
    for i, fp in enumerate(files):
        ok, concepts, links = process_file(fp, term_map, sorted_terms)
        if ok:
            processed += 1
            total_concepts += concepts
            total_links += links
        else:
            errors += 1

        if (i+1) % 100 == 0:
            elapsed = time.time() - start
            print(f"进度: {i+1}/{len(files)} | 已处理: {processed} | 正文双链: {total_links} | 概念: {total_concepts} | 耗时: {elapsed:.1f}s")

    print(f"\n完成! 处理: {processed} | 正文双链: {total_links} | 关系概念: {total_concepts} | 错误: {errors} | 总耗时: {time.time()-start:.1f}s")

if __name__ == '__main__':
    main()
