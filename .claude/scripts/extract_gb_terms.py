#!/usr/bin/env python3
"""
GB文件术语提取脚本
从 GB/T 标准 MD 文件中提取术语和定义，生成 terms.yml
"""

import os
import re
import yaml
from pathlib import Path

# 搜索 GB 文件的目录
SEARCH_DIRS = [
    "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）",
]

# 输出文件
OUTPUT_FILE = "/root/obsidian_vault/terms/cyber_terms.yml"


def find_gb_files(dirs):
    """查找所有 GB 文件"""
    gb_files = []
    for d in dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if re.match(r'.*GB[/T]?\s*[-]?\s*\d+.*\.md', f, re.IGNORECASE):
                    gb_files.append(os.path.join(d, f))
    return gb_files


def extract_terms_from_file(filepath):
    """从单个 GB 文件提取术语"""
    terms = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  读取失败: {filepath}, {e}")
        return terms, {}

    filename = os.path.basename(filepath)
    print(f"  处理: {filename}")

    # 格式: 编号单独一行，然后 ## 术语名 英文名，然后定义
    # 例如:
    # 3.1
    #
    # ## 网络安全 cybersecurity
    #
    # 定义内容...

    all_terms = []
    in_term_section = False

    # 分割文件内容
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 进入术语和定义章节
        if '术语和定义' in line:
            in_term_section = True
            i += 1
            continue

        # 退出缩略语章节（进入第4章）
        if in_term_section and re.match(r'^#+\s*4\s+缩略语', line):
            break

        if not in_term_section:
            i += 1
            continue

        # 匹配术语编号 (3.1 或 3.10 等)
        num_match = re.match(r'^(\d+\.\d+)\s*$', line)
        if num_match:
            term_num = num_match.group(1)
            # 跳过分隔的空行
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1

            if i >= len(lines):
                break

            # 读取术语名行
            term_line = lines[i].strip()
            # 去掉 ## 标题标记
            term_line = re.sub(r'^##?\s*', '', term_line)
            # 分离中文名和英文名
            # 格式: 网络安全 cybersecurity 或 网络安全-cybersecurity
            parts = re.split(r'\s+', term_line, 1)
            cn_name = parts[0] if parts else ''
            en_name = parts[1] if len(parts) > 1 else ''

            # 收集定义内容（直到下一个编号或分隔线）
            i += 1
            definitions = []
            while i < len(lines):
                current = lines[i]
                # 遇到下一个编号就停止
                if re.match(r'^\d+\.\d+\s*$', current.strip()):
                    break
                # 遇到分隔线或空章节标题也停止
                if re.match(r'^---', current) or re.match(r'^#+\s*\d', current):
                    break
                # 跳过注释引用行
                if current.strip().startswith('[') and current.strip().endswith(']'):
                    i += 1
                    continue
                # 跳过空白行
                if not current.strip():
                    i += 1
                    continue
                # 跳过只有单个字的行（可能是排版）
                stripped = current.strip()
                if len(stripped) <= 2 and not stripped[0].isdigit():
                    i += 1
                    continue
                definitions.append(current.strip())
                i += 1

            def_text = ' '.join(definitions).strip()
            def_text = re.sub(r'\s+', ' ', def_text)  # 合并空白

            if cn_name and def_text:
                all_terms.append({
                    'id': f"gb_{term_num.replace('.', '_')}_{len(all_terms)}",
                    'number': term_num,
                    'term': cn_name,
                    'en': en_name,
                    'definition': def_text[:500],
                    'source': filename
                })
            continue

        i += 1

    # 提取缩略语
    abbrevs = {}
    in_abbrev = False

    for line in content.split('\n'):
        if '缩略语' in line:
            in_abbrev = True
            continue
        if in_abbrev:
            # 匹配 AP: 无线访问接入点 (Wireless Access Point)
            match = re.match(r'\s*([A-Z][A-Z0-9\-]+):\s*(.+?)(?:\n|$)', line)
            if match:
                abbrev = match.group(1)
                rest = match.group(2).strip()
                # 去掉括号内容
                rest = re.sub(r'\(.+?\)', '', rest).strip()
                abbrevs[abbrev] = rest

    return all_terms, abbrevs


def main():
    print("=" * 60)
    print("GB 文件术语提取器")
    print("=" * 60)

    # 查找文件
    print("\n[1] 扫描 GB 文件...")
    gb_files = find_gb_files(SEARCH_DIRS)
    print(f"    找到 {len(gb_files)} 个 GB 文件")

    # 提取术语
    print("\n[2] 提取术语...")
    all_terms = []
    all_abbrevs = {}

    for f in gb_files:
        terms, abbrevs = extract_terms_from_file(f)
        all_terms.extend(terms)
        all_abbrevs.update(abbrevs)

    print(f"    提取 {len(all_terms)} 个术语")
    print(f"    提取 {len(all_abbrevs)} 个缩略语")

    # 去重
    seen = set()
    unique_terms = []
    for t in all_terms:
        key = (t['term'], t['source'])
        if key not in seen:
            seen.add(key)
            unique_terms.append(t)

    print(f"    去重后 {len(unique_terms)} 个术语")

    # 构建输出
    output = {
        'metadata': {
            'generated': '2026-04-29',
            'source': 'GBT standards',
            'term_count': len(unique_terms),
            'abbrev_count': len(all_abbrevs)
        },
        'abbreviations': all_abbrevs,
        'terms': unique_terms
    }

    # 确保输出目录存在
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # 写入文件
    print(f"\n[3] 写入 {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 网络安全术语表\n")
        f.write("# 由脚本自动从 GB/T 标准文件中提取\n\n")
        yaml.dump(output, f, allow_unicode=True, sort_keys=False)

    print(f"    完成! 共 {len(unique_terms)} 个术语")

    # 显示样例
    print("\n[4] 样例术语 (前5个):")
    for t in unique_terms[:5]:
        print(f"    - {t['term']}: {t['definition'][:60]}...")

    return unique_terms, all_abbrevs


if __name__ == '__main__':
    main()