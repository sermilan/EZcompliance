#!/usr/bin/env python3
"""
批量处理PolicyArchive中的markdown文件：
1. 替换PDF转换的processed字段为标准frontmatter
2. 添加relationship section
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"

# 标准号格式映射
STANDARD_PATTERNS = [
    (r'GBT\s*(\d+)[\-–](\d+)', r'GB/T \1—\2'),
    (r'GAT\s*(\d+)[\-–](\d+)', r'GA/T \1—\2'),
    (r'GBZ\s*(\d+)[\-–](\d+)', r'GB/Z \1—\2'),
    (r'YD/?T\s*(\d+)[\-–](\d+)', r'YD/T \1—\2'),
    (r'DB\d+/?T\s*(\d+)[\-–](\d+)', r'DB\1/T \2'),
    (r'SJ/?T\s*(\d+)[\-–](\d+)', r'SJ/T \1—\2'),
    (r'T/CCIA\s*(\d+)[\-–](\d+)', r'T/CCIA \1—\2'),
]

def normalize_standard_number(text):
    """标准化标准号格式"""
    for pattern, replacement in STANDARD_PATTERNS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def extract_standard_number_from_filename(filename):
    """从文件名提取标准号"""
    name = Path(filename).stem
    # 匹配常见标准号格式
    patterns = [
        r'(GB/\w\s*\d+[\-–]\d+)',
        r'(GA/\w\s*\d+[\-–]\d+)',
        r'(YD/\w\s*\d+[\-–]\d+)',
        r'(DB\d+/T\s*\d+[\-–]\d+)',
        r'(SJ/T\s*\d+[\-–]\d+)',
        r'(T/CCIA\s*\d+[\-–]\d+)',
        r'(GBT?\s*\d+[\-–]\d+)',
        r'(GAT?\s*\d+[\-–]\d+)',
        r'(GBZ?\s*\d+[\-–]\d+)',
    ]
    for p in patterns:
        m = re.search(p, name, re.IGNORECASE)
        if m:
            return normalize_standard_number(m.group(1))
    return None

def extract_date_from_content(content):
    """从内容提取发布日期"""
    # 匹配各种日期格式
    patterns = [
        r'(\d{4})年(\d{1,2})月(\d{1,2})日',
        r'(\d{4})[-年](\d{1,2})[-月]',
        r'(\d{4})年(\d{1,2})月',
    ]
    for p in patterns:
        m = re.search(p, content)
        if m:
            if len(m.groups()) == 3:
                return f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"
            elif len(m.groups()) == 2:
                return f"{m.group(1)}-{m.group(2).zfill(2)}"
    return None

def determine_doc_type(filename, content):
    """判断文档类型"""
    name = Path(filename).stem.lower()
    if any(k in name for k in ['白皮书', 'whitepaper']):
        return 'whitepaper'
    if any(k in name for k in ['报告', 'research', '研究报告']):
        return 'report'
    if any(k in name for k in ['指南', 'guide', '指引', '规范', '办法']):
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

def determine_domain(filename, content):
    """判断领域"""
    name = Path(filename).stem
    domains = []
    if any(k in name for k in ['数据安全', '数据治理', '数据管理']):
        domains.append('数据安全')
    if any(k in name for k in ['个人信息', '隐私', '个人信息和']):
        domains.append('个人信息保护')
    if any(k in name for k in ['网络安全', '网络空间安全']):
        domains.append('网络安全')
    if any(k in name for k in ['关键信息基础设施', 'CII', '关键基础设施']):
        domains.append('关键信息基础设施')
    if any(k in name for k in ['等级保护', '等保']):
        domains.append('等级保护')
    if any(k in name for k in ['密码', '商用密码', '密评']):
        domains.append('密码安全')
    if any(k in name for k in ['工业互联网', '工业控制']):
        domains.append('工业互联网安全')
    if any(k in name for k in ['车联网', '汽车数据']):
        domains.append('车联网')
    if any(k in name for k in ['公共数据', '政务数据']):
        domains.append('公共数据')
    if any(k in name for k in ['人工智能', '生成式AI', 'AIGC']):
        domains.append('人工智能安全')
    if any(k in name for k in ['云', '云计算']):
        domains.append('云计算安全')
    if len(domains) == 0:
        domains.append('数据安全')
    return domains

def has_frontmatter(content):
    """检查是否有frontmatter"""
    return content.strip().startswith('---')

def parse_frontmatter(content):
    """解析frontmatter"""
    if not has_frontmatter(content):
        return None, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm, content[len(parts[0]) + len(parts[1]) + 6:]
    except:
        return None, content

def needs_processing(frontmatter):
    """检查是否需要处理"""
    if frontmatter is None:
        return True
    return 'processed' in frontmatter or 'source' in frontmatter

def create_frontmatter(title, doc_type, domains, standard_number, publish_date, issuer, status, level, filename):
    """创建标准frontmatter"""
    fm = {
        'title': title,
        'type': doc_type,
        'domain': domains,
        'jurisdiction': '中国',
        'issuer': issuer or '待确认',
        'publish_date': publish_date or datetime.now().strftime('%Y-%m'),
        'status': status or '现行有效',
        'level': level or '待确认',
    }
    if standard_number:
        fm['standard_number'] = standard_number
    return fm

def add_relationship_section(content, related_links):
    """添加关系部分"""
    if not related_links:
        return content
    section = '\n\n## 相关文档\n\n'
    for link in related_links[:10]:  # 最多10个链接
        section += f'- {link}\n'
    return content.rstrip() + section

def find_related_docs(current_file, all_files):
    """查找相关文档"""
    current_name = Path(current_file).stem
    related = []

    keywords = []
    # 从文件名提取关键词
    for kw in ['数据安全', '个人信息', '网络安全', '等级保护', '关键信息', '车联网', '人工智能']:
        if kw in current_name:
            keywords.append(kw)

    for f in all_files:
        if f == current_file:
            continue
        fname = Path(f).stem
        for kw in keywords:
            if kw in fname and f not in related:
                related.append(f'[[{fname}]]')
                break

    return related[:5]  # 最多5个

def process_file(filepath, all_files):
    """处理单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        # 检查是否需要处理
        if frontmatter and 'processed' not in frontmatter and 'standard_number' in str(frontmatter):
            # 已经有完整frontmatter，跳过
            return False, 'skipped'

        # 提取文件信息
        filename = filepath.name
        title = frontmatter.get('title', Path(filename).stem) if frontmatter else Path(filename).stem
        title = re.sub(r'^\d+[\.、]', '', title)  # 去除序号

        doc_type = frontmatter.get('type', 'document') if frontmatter else determine_doc_type(filename, body)
        if doc_type == 'pdf':
            doc_type = determine_doc_type(filename, body)

        domains = frontmatter.get('domain', []) if frontmatter else determine_domain(filename, body)
        if isinstance(domains, str):
            domains = [domains]

        standard_number = frontmatter.get('standard_number') if frontmatter else None
        if not standard_number:
            standard_number = extract_standard_number_from_filename(filename)

        publish_date = frontmatter.get('publish_date') or frontmatter.get('published-date') if frontmatter else None
        if not publish_date:
            publish_date = extract_date_from_content(body)

        issuer = frontmatter.get('issuer') or frontmatter.get('publisher') if frontmatter else None

        status_map = {
            '现行': '现行有效',
            '有效': '现行有效',
            '现行有效': '现行有效',
            '征求意见': '征求意见稿',
            'draft': '征求意见稿',
            '试行': '试行',
            '作废': '已作废',
            '废止': '已作废',
        }
        status = frontmatter.get('status', '现行有效') if frontmatter else '现行有效'
        if status in status_map:
            status = status_map[status]

        level = frontmatter.get('level') if frontmatter else None

        # 创建新frontmatter
        new_fm = create_frontmatter(title, doc_type, domains, standard_number, publish_date, issuer, status, level, filename)
        new_fm['tags'] = frontmatter.get('tags', []) if frontmatter else []
        new_fm['aliases'] = frontmatter.get('aliases', []) if frontmatter else []
        new_fm['related'] = []

        # 查找相关文档
        related_links = find_related_docs(str(filepath), all_files)
        new_fm['related'] = related_links

        # 构建新内容
        new_content = '---\n' + yaml.dump(new_fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body.strip()

        # 添加关系section
        new_content = add_relationship_section(new_content, related_links)

        # 保存
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, 'processed'
    except Exception as e:
        return False, f'error: {str(e)}'

def main():
    """主函数"""
    print(f"处理目录: {POLICY_DIR}")

    # 获取所有md文件
    md_files = list(POLICY_DIR.glob("*.md"))
    print(f"总文件数: {len(md_files)}")

    # 找出需要处理的文件（有processed字段的）
    files_to_process = []
    for f in md_files:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                content = fp.read()
            frontmatter, _ = parse_frontmatter(content)
            if needs_processing(frontmatter):
                files_to_process.append(f)
        except:
            continue

    print(f"需要处理的文件数: {len(files_to_process)}")

    # 处理文件
    processed = 0
    skipped = 0
    errors = 0

    all_files = [str(f) for f in md_files]

    for i, filepath in enumerate(files_to_process):
        success, status = process_file(filepath, all_files)
        if status == 'processed':
            processed += 1
        elif status == 'skipped':
            skipped += 1
        else:
            errors += 1

        if (i + 1) % 50 == 0:
            print(f"进度: {i+1}/{len(files_to_process)} - 已处理: {processed}, 跳过: {skipped}, 错误: {errors}")

    print(f"\n完成! 已处理: {processed}, 跳过: {skipped}, 错误: {errors}")

if __name__ == '__main__':
    main()
