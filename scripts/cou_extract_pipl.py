#!/usr/bin/env python3
"""
PIPL/DSL COU 提取脚本
适用：《个人信息保护法》《数据安全法》等法律文本

结构特征：
- 按"第X条"划分条款
- 条款内用"（一）（二）"或"1. 2."划分子条款
- 动作词：应当、必须、不得、有权、可以

用法：
  python3 .claude/cou_extract_pipl.py [文件名片段]
"""

import re
import sys
from pathlib import Path

VAULT_ROOT = Path("/root/obsidian_vault")
OUTPUT_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"

# 法律层级基础权重
BASE_WEIGHT = 10  # L级 = 法律

# 主体映射（常见主体词）
SUBJECT_MAP = {
    "个人信息处理者": "个人信息处理者",
    "个人信息主体": "自然人（个人信息主体）",
    "受托人": "受托处理者",
    "接收方": "境外接收方",
    "关键信息基础设施运营者": "关键信息基础设施运营者",
    "国家": "国家（监管机构）",
    "部门": "履行个人信息保护职责的部门",
}

# 域映射
DOMAIN_MAP = {
    "第一章": ["总则", "基本规定"],
    "第二章": ["个人信息处理规则", "一般规定", "敏感信息", "国家机关"],
    "第三章": ["个人信息跨境", "数据出境"],
    "第四章": ["个人权利", "主体权利"],
    "第五章": ["处理者义务", "合规义务"],
    "第六章": ["监管职责", "部门职责"],
    "第七章": ["法律责任", "处罚"],
    "第八章": ["附则"],
    "第一节": ["一般规定"],
    "第二节": ["敏感个人信息"],
    "第三节": ["国家机关"],
    # DSL专有
    "数据安全": ["数据安全", "分类分级"],
    "重要数据": ["重要数据", "核心数据"],
    "数据出境": ["数据出境", "跨境传输"],
    # WL专有
    "网络安全": ["网络安全", "等级保护"],
}


def get_domain(chapter, section=""):
    """确定归属域"""
    if chapter in DOMAIN_MAP:
        return DOMAIN_MAP[chapter]
    if section in DOMAIN_MAP:
        return DOMAIN_MAP[section]
    return ["通用合规"]


def extract_action_verbs(text):
    """从文本中提取所有动作义务词及其位置"""
    patterns = [
        (r'应当、?(.*?)[。，]', '应当'),
        (r'必须、?(.*?)[。，]', '必须'),
        (r'不得(.*?)[。，]', '不得'),
        (r'有权(.*?)[。，]', '有权'),
        (r'可以(.*?)[。，]', '可以'),
        (r'应当(.*?)[，。；]', '应当'),
        (r'必须(.*?)[，。；]', '必须'),
        (r'不得(.*?)[，。；]', '不得'),
    ]
    results = []
    for pattern, verb in patterns:
        for m in re.finditer(pattern, text):
            obj = m.group(1).strip() if m.lastindex else ""
            if obj and len(obj) > 2:
                results.append((verb, obj, m.start()))
    return results


def split_sub_clauses(text):
    """拆分条款中的子条款"""
    # 优先按"（一）（二）"拆分
    subs = re.split(r'（[一二三四五六七八九十]+）', text)
    if len(subs) > 1:
        return [(f"（{chr(ord('一')+i)}）", subs[i+1] if i+1 < len(subs) else "")
                for i in range(len(subs)-1)]
    # 回退按数字拆分
    subs = re.split(r'\d+[、.]', text)
    return [(str(i+1), s.strip()) for i, s in enumerate(subs) if s.strip()]


def compute_fingerprint(subject, action, obj):
    """计算指纹"""
    return f"{subject}|{action}|{obj}"


def gen_cou_id(article_num, sub_clause="", law_code="PIPL"):
    """生成COU ID"""
    if sub_clause:
        return f"COU-R-{law_code}-{article_num}-{sub_clause}"
    return f"COU-R-{law_code}-{article_num}"


def create_cou_file(cou_id, article_num, sub_clause, subject, action, obj, domain, original_text, law_name="个人信息保护法", law_code="PIPL"):
    """创建单个COU文件"""
    fingerprint = compute_fingerprint(subject, action, obj)
    weight_factor = 1.5 if action in ['应当', '必须'] else (0.5 if action == '不得' else 1.0)
    final_weight = round(BASE_WEIGHT * weight_factor, 1)

    new_fpath = OUTPUT_DIR / f"{cou_id}.md"

    content = f"""---
title: "{cou_id}"
cou_id: "{cou_id}"
source: "{law_name}"
article: "{article_num}"
sub_clause: "{sub_clause}"
subject: "{subject}"
action: "{action}"
object: "{obj}"
condition: "无特定触发条件"
base_weight: {BASE_WEIGHT}
weight_factor: {weight_factor}
final_weight: {final_weight}
domains: {domain}
fingerprint: "{fingerprint}"
---

# {cou_id}

> **来源**: [[{law_name}]]
> **条款**: 第{article_num}条{sub_clause if sub_clause else ''}
> **层级**: R (原始COU · Raw)
> **基础权重**: {BASE_WEIGHT} (法律层级)

## 解剖结构

| 要素 | 内容 |
|------|------|
| 主体 | {subject} |
| 动作 | {action} |
| 客体 | {obj} |
| 条件 | 无特定触发条件 |
| 权重计算 | {BASE_WEIGHT} × {weight_factor} = **{final_weight}** |

## 原文

> {original_text.strip()}

## 元数据

```yaml
cou_id: {cou_id}
source: 个人信息保护法
article: "{article_num}"
sub_clause: "{sub_clause}"
subject: "{subject}"
action: "{action}"
object: "{obj}"
condition: "无特定触发条件"
base_weight: {BASE_WEIGHT}
weight_factor: {weight_factor}
final_weight: {final_weight}
domains: {domain}
fingerprint: "{fingerprint}"
```
"""

    new_fpath.write_text(content, encoding="utf-8")
    return cou_id, fingerprint, final_weight


def extract_from_file(filepath, law_name="个人信息保护法", law_code="PIPL"):
    """从法律文件中提取COU"""
    print(f"[*] 提取: {filepath.name}")

    content = filepath.read_text(encoding="utf-8")
    lines = content.split('\n')

    current_chapter = "第一章"
    current_section = ""
    cou_count = 0
    article_pattern = re.compile(r'^\*{0,2}第([一二三四五六七八九十百\d]+)条[　\s*\*]*(.*)$')

    for line in lines:
        line_stripped = line.strip()

        # 检测章节（支持 **第一章** 和 # 第一章 两种格式）
        if re.match(r'^#{1,2}\s*\*{0,2}第[一二三四五六七八]+章', line_stripped) or re.match(r'^\*{0,2}第[一二三四五六七八]+章\*{0,2}$', line_stripped):
            m = re.search(r'第([一二三四五六七八]+)章', line_stripped)
            if m:
                current_chapter = f"第{m.group(1)}章"
                current_section = ""  # 重置节
        elif re.match(r'^#{1,3}\s*\*{0,2}第[一二三四五六七八]+节', line_stripped) or re.match(r'^\*{0,2}第[一二三四五六七八]+节\*{0,2}$', line_stripped):
            m = re.search(r'第([一二三四五六七八]+)节', line_stripped)
            if m:
                current_section = f"第{m.group(1)}节"
        elif '## ' in line and '节' in line:
            m = re.search(r'第([一二三四五六七八]+)节', line)
            if m:
                current_section = f"第{m.group(1)}节"

        # 检测条款
        m = article_pattern.match(line)
        if m:
            article_num = m.group(1)
            article_text = m.group(2).strip()

            if not article_text:
                continue

            domain = get_domain(current_chapter, current_section)

            # 分析条款中的义务动作
            obligations = extract_action_verbs(article_text)

            if obligations:
                for verb, obj, pos in obligations:
                    subject = "数据处理者"  # 默认主体（通用）
                    cou_id = gen_cou_id(article_num, verb[0], law_code)
                    try:
                        result = create_cou_file(
                            cou_id, article_num, verb,
                            subject, verb, obj, domain, article_text,
                            law_name, law_code
                        )
                        print(f"  [COU] {result[0]} | {verb} | weight={result[2]}")
                        cou_count += 1
                    except Exception as e:
                        print(f"  [ERR] {cou_id}: {e}")
            else:
                # 无明确义务词，作为描述性条款跳过或提取"处理"动作
                if any(k in article_text for k in ['处理', '收集', '使用', '提供']):
                    subject = "数据处理者"
                    action = "处理"
                    obj = article_text[:40]
                    cou_id = gen_cou_id(article_num, "", law_code)
                    try:
                        result = create_cou_file(
                            cou_id, article_num, "",
                            subject, action, obj, domain, article_text,
                            law_name, law_code
                        )
                        print(f"  [COU] {result[0]} | {action} | weight={result[2]}")
                        cou_count += 1
                    except:
                        pass

    return cou_count


def main():
    # 支持的命令行参数: [法律名片段] [law_code]
    # laws字典: key -> (glob_pattern, law_name, law_code)
    laws = {
        "pipl": ("*个人信息保护法*2021*", "个人信息保护法", "PIPL"),
        "个人信息保护法": ("*个人信息保护法*2021*", "个人信息保护法", "PIPL"),
        "dsl": ("*数据安全法*", "数据安全法", "DSL"),
        "数据安全法": ("*数据安全法*", "数据安全法", "DSL"),
        "网络安全法": ("*网络安全法*", "网络安全法", "WL"),
        "wl": ("*网络安全法*", "网络安全法", "WL"),
        "cii": ("*关键信息基础设施安全保护条例*", "关键信息基础设施安全保护条例", "CII"),
        "关键信息基础设施安全保护条例": ("*关键信息基础设施安全保护条例*", "关键信息基础设施安全保护条例", "CII"),
    }

    search_key = sys.argv[1] if len(sys.argv) > 1 else "pipl"
    law_code = sys.argv[2] if len(sys.argv) > 2 else None

    if search_key in laws:
        glob_pattern, law_name, code = laws[search_key]
    else:
        glob_pattern = f"*{search_key}*"
        law_name = search_key
        if "数据安全法" in search_key:
            code = "DSL"
        elif "个人信息保护法" in search_key:
            code = "PIPL"
        elif "网络安全法" in search_key:
            code = "WL"
        else:
            code = law_code or "LAW"

    candidates = list(VAULT_ROOT.glob(
        f"Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）/{glob_pattern}.md"))

    if not candidates:
        print(f"[!] 未找到包含 '{search_key}' 的文件")
        return

    # 优先选择正式版本（带日期2022>日期2017>745>最新版>2.前缀>1.前缀>征求意见稿）
    filepath = candidates[0]
    # 按日期和优先级选择
    date_preferred = None
    for c in candidates:
        if "2022" in c.name and "数据出境安全评估办法" in c.name:
            if "征求意见稿" not in c.name:
                date_preferred = c
                break
    if date_preferred:
        filepath = date_preferred
    else:
        # 回退：选2022年的
        for c in candidates:
            if "2022" in c.name and "征求意见稿" not in c.name:
                filepath = c
                break
        else:
            # 再回退：选带日期的
            for c in candidates:
                if c.name[0].isdigit() and ("202" in c.name or "201" in c.name):
                    if "征求意见稿" not in c.name:
                        filepath = c
                        break

    if not filepath.exists():
        print(f"[!] 文件不存在: {filepath}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cou_count = extract_from_file(filepath, law_name, code)
    print(f"[*] 提取完成: {cou_count} 个COU")
    print(f"[*] 输出目录: {OUTPUT_DIR}")

    if not candidates:
        print(f"[!] 未找到包含 '{search_key}' 的文件")
        return

    filepath = candidates[0]
    if not filepath.exists():
        print(f"[!] 文件不存在: {filepath}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cou_count = extract_from_file(filepath, law_name, code)
    print(f"[*] 提取完成: {cou_count} 个COU")
    print(f"[*] 输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
