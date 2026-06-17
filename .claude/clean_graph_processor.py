#!/usr/bin/env python3
"""
知识图谱标注脚本 - 纯净版
原则：
1. 不修改正文内容（不添加wikilinks到正文）
2. 只生成结构化关系区
3. 每个文档列出最重要的关联（最多10个）
4. 关系分类清晰：法律依据/相关标准/核心概念/监管机构
"""

import os
import re
import yaml
from pathlib import Path
import time

VAULT_DIR = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_DIR / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
VOCAB_FILE = VAULT_DIR / ".claude/controlled_vocabulary_focused.yml"

# 受控词表 - 高价值概念
VOCABULARY = {
    'laws': [
        ('中华人民共和国网络安全法', ['网络安全法', '网安法']),
        ('中华人民共和国数据安全法', ['数据安全法']),
        ('中华人民共和国个人信息保护法', ['个人信息保护法', '个保法']),
        ('中华人民共和国密码法', ['密码法']),
        ('中华人民共和国国家安全法', ['国家安全法']),
        ('中华人民共和国保守国家秘密法', ['保密法', '保守国家秘密法']),
        ('中华人民共和国计算机信息系统安全保护条例', ['计算机信息系统安全保护条例']),
    ],
    'regulations': [
        ('关键信息基础设施安全保护条例', ['关基保护条例', '关基条例']),
        ('网络安全审查办法', ['安全审查办法']),
        ('数据出境安全评估办法', ['数据出境评估', '出境评估']),
        ('网络安全等级保护条例', ['等保条例']),
    ],
    'standards': [
        ('GB/T 22239-2019 信息安全技术 网络安全等级保护基本要求', ['等保2.0', '等级保护基本要求', 'GB/T 22239']),
        ('GB/T 22240-2020 信息安全技术 网络安全等级保护定级指南', ['等保定级指南', '定级指南', 'GB/T 22240']),
        ('GB/T 25070-2019 信息安全技术 网络安全等级保护安全设计技术要求', ['安全设计技术要求', 'GB/T 25070']),
        ('GB/T 28448-2019 信息安全技术 网络安全等级保护测评要求', ['等保测评要求', 'GB/T 28448']),
        ('GB/T 35273-2020 信息安全技术 个人信息安全规范', ['个人信息安全规范', '个保规范', 'GB/T 35273']),
        ('GB/T 17859-1999 计算机信息系统安全保护等级划分准则', ['等级划分准则', 'GB 17859']),
        ('GB/T 20984-2022 信息安全技术 信息安全风险评估方法', ['风险评估方法', 'GB/T 20984']),
        ('GB/T 25069-2010 信息安全技术 术语', ['信息安全术语', 'GB/T 25069']),
        ('GB/T 41391-2022 信息安全技术 移动互联网应用程序（App）收集个人信息基本要求', ['App收集个人信息基本要求', 'GB/T 41391']),
        ('GB/T 42574-2023 信息安全技术 个人信息安全影响评估指南', ['PIA指南', '个人信息安全影响评估', 'GB/T 42574']),
    ],
    'concepts': [
        ('数据分类分级保护制度', ['数据分类分级', '分类分级保护']),
        ('数据安全审查制度', ['数据安全审查', '安全审查']),
        ('数据出境安全评估', ['数据出境评估', '出境评估']),
        ('个人信息保护影响评估', ['PIA评估', '隐私影响评估']),
        ('网络安全等级保护制度', ['等级保护制度', '等保制度', '等级保护']),
        ('关键信息基础设施', ['关基', 'CII', '关键基础设施']),
        ('等级保护测评', ['等保测评', '安全测评']),
        ('个人信息', ['个人数据']),
        ('敏感个人信息', ['敏感数据', '个人敏感信息']),
        ('重要数据', []),
        ('核心数据', []),
        ('身份鉴别', ['身份认证']),
        ('访问控制', ['权限控制']),
        ('安全审计', ['日志审计']),
        ('数据加密', ['加密']),
        ('应急响应', ['应急预案', '应急处置']),
        ('安全监测', ['安全监控']),
        ('安全管理制度', ['管理制度']),
    ],
    'institutions': [
        ('国家网信部门', ['国家互联网信息办公室', '网信办', '国家网信办']),
        ('公安机关', ['公安部门', '公安网安']),
        ('工业和信息化主管部门', ['工业和信息化部', '工信部']),
        ('行业主管部门', ['行业监管部门']),
    ]
}

# 构建高效查找表
TERM_MAP = {}  # alias -> (canonical, category)
for category, terms in VOCABULARY.items():
    for canonical, aliases in terms:
        for alias in [canonical] + aliases:
            if len(alias) >= 2:
                TERM_MAP[alias] = (canonical, category)

SORTED_TERMS = sorted(TERM_MAP.keys(), key=len, reverse=True)

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

def find_concepts_in_text(body):
    """在正文中查找概念"""
    found = set()
    for term in SORTED_TERMS:
        if term in body:
            canonical, cat = TERM_MAP[term]
            found.add((canonical, cat))
    return list(found)

def generate_relationship_section(found_items):
    """生成结构化关系区"""
    sections = {
        '法律依据': [],
        '相关标准': [],
        '核心概念': [],
        '监管机构': []
    }

    for canonical, category in found_items:
        link = f'[[{canonical}]]'
        if category in ['laws', 'regulations']:
            sections['法律依据'].append(link)
        elif category == 'standards':
            sections['相关标准'].append(link)
        elif category == 'concepts':
            sections['核心概念'].append(link)
        elif category == 'institutions':
            sections['监管机构'].append(link)

    lines = ['\n\n---\n\n## 关联关系\n']
    for name, items in sections.items():
        if items:
            # 去重并限制数量
            unique = list(dict.fromkeys(items))[:6]
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
        body = re.sub(r'\n##\s*(相关文档|关联关系)[^\n]*\n.*?(?=\n---\n|\n##\s|\Z)', '', body, flags=re.DOTALL)

        # 分析正文中的概念
        found_items = find_concepts_in_text(body)

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

        # 清理related字段
        if 'related' in fm and fm['related']:
            fm['related'] = [str(r).strip() for r in fm['related'] if r and str(r) != 'None']

        new_content = '---\n' + yaml.dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, len(found_items)
    except Exception as e:
        return False, 0

def main():
    print("=" * 60)
    print("知识图谱标注 - 纯净版")
    print("原则：不修改正文，只生成结构化关系区")
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
            elapsed = time.time() - start
            print(f"进度: {i+1}/{len(files)} | 已处理: {processed} | 概念: {total_concepts} | 耗时: {elapsed:.1f}s")

    print(f"\n完成!")
    print(f"  处理: {processed} 文件")
    print(f"  总概念: {total_concepts}")
    print(f"  平均: {total_concepts/max(processed,1):.1f} 概念/文件")
    print(f"  耗时: {time.time()-start:.1f}s")

if __name__ == '__main__':
    main()