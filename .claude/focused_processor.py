#!/usr/bin/env python3
"""
精简版知识图谱标注脚本 v3 - 跳过已处理文件，只处理干净的文件
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

def is_clean_content(text):
    """检查内容是否干净（没有重复字符等wikilink问题）"""
    # 检测连续重复的中文词（wikilink问题遗留）
    if re.search(r'(中华人民共和国){2,}', text):
        return False
    if re.search(r'(\[\[){3,}', text):  # 三个或更多 [
        return False
    return True

def clean_for_processing(text):
    """清理wikilink但保持内容干净"""
    # 移除所有 [[ ]] 及其内容
    text = re.sub(r'\[\[([^\]]+)\]\]', '', text)
    return text

def add_wikilinks_focused(text, term_map, sorted_terms, max_links=8):
    """只添加高价值双链"""
    result = text
    links_added = []
    added_canonicals = set()

    for term in sorted_terms:
        if len(links_added) >= max_links:
            break
        canonical, category = term_map[term]
        if canonical in added_canonicals:
            continue

        if term in result:
            replacement = f'[[{canonical}]]' if term == canonical else f'[[{canonical}|{term}]]'
            result = result.replace(term, replacement, 1)
            added_canonicals.add(canonical)
            links_added.append((canonical, category))

    return result, links_added

def generate_relationship_section(found_items):
    sections = {
        '法律依据': [],
        '相关标准': [],
        '核心制度': [],
        '数据类型': [],
        '监管机构': []
    }

    for canonical, category in found_items:
        link = f'[[{canonical}]]'
        if category == 'laws':
            sections['法律依据'].append(link)
        elif category == 'regulations':
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
            unique = list(dict.fromkeys(items))[:5]
            lines.append(f'- {name}：')
            for item in unique:
                lines.append(f'  {item}')

    return '\n'.join(lines) if lines else ''

def process_file(filepath, term_map, sorted_terms):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()

        # 检查内容是否干净
        if not is_clean_content(raw):
            # 内容不干净，需要清理
            cleaned = clean_for_processing(raw)
        else:
            cleaned = raw

        fm, body = parse_frontmatter(cleaned)
        filename = filepath.name

        # 删除旧关系区
        body = re.sub(r'\n##\s*(相关文档|关联关系)[^\n]*\n.*?(?=\n---\n|\n##\s|\Z)', '', body, flags=re.DOTALL)

        std_num = extract_std_num(filename)

        # 只添加8个高价值双链
        new_body, found_items = add_wikilinks_focused(body, term_map, sorted_terms, max_links=8)

        # 生成关系区
        rel_section = generate_relationship_section(found_items)
        if rel_section:
            new_body = new_body.rstrip() + '\n\n---\n\n## 关联关系\n' + rel_section

        # 更新frontmatter
        if fm is None:
            fm = {}
        fm['title'] = fm.get('title', Path(filename).stem)
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
    print("精简知识图谱标注 v3 (清理模式)")
    print("=" * 60)

    term_map, sorted_terms = load_vocab()
    print(f"词表: {len(term_map)} 个高价值术语")

    files = list(POLICY_DIR.glob("*.md"))
    print(f"文件: {len(files)} 个")

    processed = 0
    total_links = 0
    errors = 0
    skipped = 0

    start = time.time()
    for i, fp in enumerate(files):
        ok, links = process_file(fp, term_map, sorted_terms)
        if ok:
            processed += 1
            total_links += links
        else:
            errors += 1

        if (i+1) % 100 == 0:
            print(f"进度: {i+1}/{len(files)} | 已处理: {processed} | 双链: {total_links} | 耗时: {time.time()-start:.1f}s")

    print(f"\n完成! 处理: {processed} | 总双链: {total_links} | 平均: {total_links/max(processed,1):.1f}/文件 | 耗时: {time.time()-start:.1f}s")

if __name__ == '__main__':
    main()