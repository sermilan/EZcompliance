#!/usr/bin/env python3
"""
双链标注脚本
基于术语表自动为 Markdown 文件添加 [[wikilink]]
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

# 配置路径
TERMS_FILE = "/root/obsidian_vault/terms/cyber_terms.yml"
ALIASES_FILE = "/root/obsidian_vault/terms/law_aliases.yml"
STANDARDS_FILE = "/root/obsidian_vault/terms/standards_aliases.yml"
SEARCH_DIR = "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
OUTPUT_DIR = "/root/obsidian_vault/Wiki（维基）/Projects（项目）/policy-linker"

# 加载术语和别名
def load_terms():
    with open(TERMS_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data['terms']

def load_aliases():
    aliases = {}
    # 加载 law_aliases
    if os.path.exists(ALIASES_FILE):
        with open(ALIASES_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and 'aliases' in data:
                aliases.update(data['aliases'])

    # 加载 standards_aliases
    if os.path.exists(STANDARDS_FILE):
        with open(STANDARDS_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and 'aliases' in data:
                # 只取标准编号的别名
                for k, v in data['aliases'].items():
                    if 'GB' in k or 'GBT' in k:
                        aliases[k] = v
    return aliases

def load_stopwords():
    """加载停用词表"""
    stopwords_file = "/root/obsidian_vault/terms/stopwords.yml"
    if os.path.exists(stopwords_file):
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and 'stopwords' in data:
                return set(data['stopwords'])
    return set()

def build_term_index(terms):
    """构建术语索引，按长度降序排列（优先匹配长术语）"""
    term_list = []
    for t in terms:
        term_list.append({
            'term': t['term'],
            'en': t.get('en', ''),
            'source': t.get('source', ''),
            'id': t.get('id', '')
        })

    # 按长度降序排列
    term_list.sort(key=lambda x: len(x['term']), reverse=True)
    return term_list

def normalize_alias(text, aliases):
    """将别名归一化到标准词"""
    for alias, standard in aliases.items():
        # 精确匹配
        if text == alias:
            return standard
        # 包含匹配
        if alias in text:
            return text.replace(alias, standard)
    return text

def is_inside_existing_link(pos, link_ranges):
    """检查位置是否在已有链接范围内"""
    for start, end in link_ranges:
        if start <= pos < end:
            return True
    return False

def add_wikilinks(content, term_index, aliases, filename):
    """为内容添加 wikilink"""
    # 记录已有的wikilink位置
    existing_link_ranges = []
    for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
        existing_link_ranges.append(match.span())

    existing_links = set()
    for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
        existing_links.add(match.group(1))

    # 按长度降序排列术语（优先匹配长术语）
    term_list = sorted(term_index, key=lambda x: len(x['term']), reverse=True)

    # 统计添加的链接（用 set 去重）
    added_links = set()
    new_link_ranges = []  # 新增链接的位置

    # 加载停用词（避免重复加载）
    if not hasattr(add_wikilinks, '_stopwords'):
        add_wikilinks._stopwords = load_stopwords()
    stopwords = add_wikilinks._stopwords

    # 定义允许的边界字符
    VALID_BOUNDARY_CHARS = set(' \t\n\r(（【《<"，,。.;;:!?）】》>、')

    for term_info in term_list:
        term = term_info['term']
        en = term_info.get('en', '')

        # 跳过太短的术语（长度小于2）
        if len(term) < 2:
            continue

        # 跳过包含特殊字符的术语
        if re.search(r'[（）()【】\[\]《》<>]', term):
            continue

        # 跳过已经是链接的术语
        if term in existing_links:
            continue

        # 跳过停用词
        if term in stopwords:
            continue

        # 简单字符串匹配（更可靠的中文处理）
        search_start = 0
        while True:
            pos = content.find(term, search_start)
            if pos == -1:
                break

            # 检查是否在已有链接内
            if is_inside_existing_link(pos, existing_link_ranges + new_link_ranges):
                search_start = pos + 1
                continue

            # 检查前后字符（确保是独立术语，不是其他词的一部分）
            before = content[pos - 1] if pos > 0 else ' '
            after = content[pos + len(term)] if pos + len(term) < len(content) else ' '

            # 检查前后字符
            is_chinese = '\u4e00' <= term[0] <= '\u9fff'

            if is_chinese:
                # 中文术语：检查前后是否都是字母/中文（长词的一部分）
                before_is_part = before.isalnum() or ('\u4e00' <= before <= '\u9fff')
                after_is_part = after.isalnum() or ('\u4e00' <= after <= '\u9fff')
                # 如果前后都是某个词的一部分（不是边界），跳过
                if before_is_part and after_is_part:
                    search_start = pos + 1
                    continue
            else:
                # 英文术语：前后有任意一个是字母数字就跳过
                if before.isalnum() or after.isalnum():
                    search_start = pos + 1
                    continue

            # 替换为 wikilink
            link_text = f"[[{term}]]"
            content = content[:pos] + link_text + content[pos + len(term):]
            # 记录新链接位置
            new_link_ranges.append((pos, pos + len(link_text)))
            added_links.add(term)
            existing_links.add(term)
            # 调整已有链接范围
            existing_link_ranges = [(s, e) for s, e in existing_link_ranges if e <= pos]
            search_start = pos + len(link_text)

        # 也处理英文名（如果存在）
        if en and len(en) > 2:
            search_start = 0
            while True:
                pos = content.find(en, search_start)
                if pos == -1:
                    break

                if is_inside_existing_link(pos, existing_link_ranges + new_link_ranges):
                    search_start = pos + 1
                    continue

                before = content[pos - 1] if pos > 0 else ' '
                after = content[pos + len(en)] if pos + len(en) < len(content) else ' '

                if before.isalnum() or after.isalnum():
                    search_start = pos + 1
                    continue

                link_text = f"[[{term}]]"
                content = content[:pos] + link_text + content[pos + len(en):]
                new_link_ranges.append((pos, pos + len(link_text)))
                added_links.add(term)
                existing_links.add(term)
                existing_link_ranges = [(s, e) for s, e in existing_link_ranges if e <= pos]
                search_start = pos + len(link_text)

    return content, list(added_links)


def process_file(filepath, term_index, aliases, dry_run=True):
    """处理单个文件"""
    filename = os.path.basename(filepath)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"读取失败: {e}"

    # 检查是否是已处理的文件（避免重复处理）
    if '## 双链标注' in content or 'processed_by_policy_linker' in content:
        return None, "已处理过"

    # 添加 wikilinks
    new_content, added_links = add_wikilinks(content, term_index, aliases, filename)

    if not added_links:
        return None, "无新增链接"

    if dry_run:
        return {
            'file': filename,
            'added': added_links,
            'count': len(added_links)
        }, None

    # 写入文件（在开头添加标注）
    header = f"\n<!-- processed_by_policy_linker: {len(added_links)} links -->\n"

    # 找到 frontmatter 结束位置
    frontmatter_end = 0
    if new_content.startswith('---'):
        match = re.search(r'^---\s*\n', new_content[3:])
        if match:
            frontmatter_end = match.end() + 3

    new_content = new_content[:frontmatter_end] + header + new_content[frontmatter_end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return {
        'file': filename,
        'added': added_links,
        'count': len(added_links)
    }, None

def main():
    import argparse
    parser = argparse.ArgumentParser(description='双链标注脚本')
    parser.add_argument('--dry-run', action='store_true', help='仅显示将要添加的链接，不实际修改')
    parser.add_argument('--write', action='store_true', help='实际写入文件（默认仅dry-run）')
    parser.add_argument('--limit', type=int, default=0, help='限制处理文件数量')
    parser.add_argument('--min-links', type=int, default=0, help='最少添加链接数才显示')
    args = parser.parse_args()

    if args.write:
        args.dry_run = False

    print("=" * 60)
    print("双链标注脚本")
    print("=" * 60)

    # 加载术语
    print("\n[1] 加载术语表...")
    terms = load_terms()
    aliases = load_aliases()
    term_index = build_term_index(terms)
    print(f"    术语数: {len(term_index)}")
    print(f"    别名数: {len(aliases)}")

    # 获取文件列表
    print("\n[2] 扫描文件...")
    files = [f for f in os.listdir(SEARCH_DIR) if f.endswith('.md')]
    if args.limit > 0:
        files = files[:args.limit]
    print(f"    待处理: {len(files)} 个文件")

    # 处理文件
    print("\n[3] 处理文件...")
    results = []
    for i, fname in enumerate(files):
        if i % 100 == 0:
            print(f"    进度: {i}/{len(files)}")

        fpath = os.path.join(SEARCH_DIR, fname)
        result, error = process_file(fpath, term_index, aliases, dry_run=not args.write)

        if result and result['count'] >= args.min_links:
            results.append(result)

    print(f"    完成: {len(files)}/{len(files)}")

    # 排序输出
    results.sort(key=lambda x: x['count'], reverse=True)

    print(f"\n[4] 结果统计:")
    print(f"    有链接增加的文件: {len(results)}")
    total_links = sum(r['count'] for r in results)
    print(f"    新增链接总数: {total_links}")

    # 显示前20个
    print(f"\n[5] 新增链接最多的文件 (前20):")
    for r in results[:20]:
        print(f"    [{r['count']:3d}] {r['file']}")
        if r['count'] <= 5:
            for t in r['added']:
                print(f"         - {t}")

    # 显示样例
    if results:
        print(f"\n[6] 样例 (第一个文件的链接):")
        sample = results[0]
        print(f"    文件: {sample['file']}")
        print(f"    链接数: {sample['count']}")
        print(f"    术语: {', '.join(sample['added'][:10])}")

    return results

if __name__ == '__main__':
    main()