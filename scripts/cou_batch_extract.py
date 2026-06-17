#!/usr/bin/env python3
"""
GBT 22239-2019 COU 批量提取脚本
从markdown文件中提取所有"应..."条款，生成COU-R原始文件

用法：
  python3 .claude/cou_batch_extract.py
"""

import re
import hashlib
from pathlib import Path

VAULT_ROOT = Path("/root/obsidian_vault")
SOURCE_FILE = VAULT_ROOT / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）/GBT 22239-2019 信息安全技术-网络安全等级保护基本要求.md"
DEFAULT_LAW_CODE = "22239"
CURRENT_LAW_CODE = "22239"  # 可在运行时覆盖
CURRENT_LAW_NAME = "GBT 22239-2019"  # 可在运行时覆盖
OUTPUT_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# 层级基础权重
LEVEL_WEIGHT = {
    "5": 10.4,  # 第五级 - 特别严重
    "4": 10.4,  # 第四级 - 严重
    "3": 9.6,   # 第三级 - 较严重
    "2": 8.0,   # 第二级 - 一般严重
    "1": 6.4,   # 第一级 - 轻微
}

# 动作词标准化
ACTION_WORDS = {
    "应": "执行",
    "应具备": "具备",
    "应能够": "能够",
    "应满足": "满足",
    "应采取": "采取",
    "应配备": "配备",
    "应设置": "设置",
    "应提供": "提供",
    "应进行": "进行",
    "应建立": "建立",
    "应制定": "制定",
    "应实现": "实现",
    "应支持": "支持",
    "应采用": "采用",
    "应确定": "确定",
    "应配置": "配置",
    "应记录": "记录",
    "应部署": "部署",
    "应定期": "定期执行",
    "应具备": "具备",
}

# 安全域映射
DOMAIN_MAP = {
    "安全物理环境": ["物理安全", "环境安全"],
    "安全通信网络": ["网络安全", "通信安全"],
    "安全区域边界": ["边界安全", "访问控制"],
    "安全计算环境": ["主机安全", "计算环境"],
    "安全管理中心": ["安全管理", "集中管控"],
    "安全管理制度": ["管理安全", "制度合规"],
    "安全管理机构": ["组织架构", "管理安全"],
    "安全管理人员": ["人员管理", "培训考核"],
    "安全建设管理": ["建设管理", "项目安全"],
    "安全运维管理": ["运维管理", "持续运营"],
    "安全管理制度": ["制度管理", "合规管理"],
}


def normalize_action(text):
    """标准化动作词"""
    for k, v in ACTION_WORDS.items():
        if k in text:
            return text.replace(k, v).strip()
    return text.strip()


def extract_clause_number(text):
    """提取条款编号"""
    m = re.search(r'^([a-zA-Z0-9（）\.]+)）', text.strip())
    if m:
        return m.group(1).strip()
    return ""


def extract_clause_text(text):
    """提取条款正文"""
    text = re.sub(r'^[a-zA-Z0-9（）\.]+）\s*', '', text.strip())
    return text


def extract_subject_and_object(text):
    """从条款文本中提取主体和客体"""
    # 常见的"应"后接动作+客体的模式
    subject = "网络安全等级保护对象运营者"  # 默认主体
    action = ""
    obj = ""

    # 去掉"应"字开头的
    text = re.sub(r'^应', '', text)

    # 常见动作模式
    action_patterns = [
        r'(配备|设置|部署|配置|提供|建立|制定|实现|支持|采用|确定|记录|进行|建立|满足|具备|采取|执行|定期)',
    ]

    for pattern in action_patterns:
        m = re.search(pattern, text)
        if m:
            action = m.group(1)
            obj = text[m.end():].strip('。，；；。')
            if len(obj) > 50:
                obj = obj[:50] + "..."
            break

    if not action:
        # 取前20个字符作为动作描述
        action = text[:20].strip('，。；、')

    return subject, action, obj


def compute_fingerprint(subject, action, obj):
    """计算COU指纹"""
    text = f"{subject}|{action}|{obj}"
    return text


def gen_cou_id(level, section, clause):
    """生成COU ID"""
    return f"COU-R-{CURRENT_LAW_CODE}-{level}-{section}-{clause}"


def create_cou_file(cou_id, level, section, clause, original_text, domain, law_name="GBT 22239-2019"):
    """创建单个COU文件"""
    subject, action, obj = extract_subject_and_object(original_text)
    fingerprint = compute_fingerprint(subject, action, obj)
    base_weight = LEVEL_WEIGHT.get(level, 8.0)
    weight_factor = 1.3 if "应" in original_text else 1.0
    final_weight = round(base_weight * weight_factor, 1)

    # 处理条款编号
    clause_clean = clause.replace('.', '-') if clause else section

    new_fname = f"{cou_id}.md"
    new_fpath = OUTPUT_DIR / new_fname

    content = f"""---
title: "{cou_id}"
cou_id: "{cou_id}"
source: "{law_name}"
chapter: "{level}-{section}"
clause: "{clause_clean}"
subject: "{subject}"
action: "{action}"
object: "{obj}"
condition: "定级为第{level}级时"
base_weight: {base_weight}
weight_factor: {weight_factor}
final_weight: {final_weight}
domains: {DOMAIN_MAP.get(domain, ['通用安全'])}
fingerprint: "{fingerprint}"
level: "{level}"
---

# {cou_id}

> **来源**: [[{law_name}]]
> **章节**: 第{level}级 - {domain} - {section}{f'({clause_clean})' if clause_clean else ''}
> **层级**: R (原始COU · Raw)
> **基础权重**: {base_weight}

## 解剖结构

| 要素 | 内容 |
|------|------|
| 主体 | {subject} |
| 动作 | {action} |
| 客体 | {obj} |
| 条件 | 定级为第{level}级时 |
| 权重计算 | {base_weight} × {weight_factor} = **{final_weight}** |

## 原文

> {original_text}

## 元数据

```yaml
cou_id: {cou_id}
source: "{law_name}"
chapter: "{level}-{section}"
clause: "{clause_clean}"
subject: "{subject}"
action: "{action}"
object: "{obj}"
condition: "定级为第{level}级时"
base_weight: {base_weight}
weight_factor: {weight_factor}
final_weight: {final_weight}
domains: {DOMAIN_MAP.get(domain, ['通用安全'])}
fingerprint: "{fingerprint}"
level: "{level}"
```
"""

    new_fpath.write_text(content, encoding="utf-8")
    return cou_id, fingerprint, final_weight


def main(override=None):
    if override is None:
        override = {}
    if override:
        globals().update(override)
    print(f"[*] COU 批量提取: {CURRENT_LAW_NAME}")
    print(f"[*] 源文件: {SOURCE_FILE}")

    content = SOURCE_FILE.read_text(encoding="utf-8")

    # 匹配章节标题行
    section_pattern = re.compile(r'^(#{1,4})\s*(\d+\.\d+(?:\.\d+)?)\s+(.+?)$', re.MULTILINE)

    current_level = "3"  # 默认第三级
    current_section = ""
    current_domain = ""

    cou_count = 0
    skip_sections = {"附录", "前言", "引言", "范围", "规范性引用", "术语", "缩略语", "等级保护概述", "目次"}

    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 检测章节级别
        if line.startswith('#### '):
            m = re.match(r'^#### (\d+\.\d+\.\d+)\s+(.+)$', line)
            if m:
                section_num = m.group(1)
                section_name = m.group(2)
                level = section_num.split('.')[0]
                current_section = section_num
                current_domain = section_name
                if level in ['6', '7', '8', '9', '10']:
                    current_level = str(int(level) - 5)
                else:
                    current_level = level

        elif line.startswith('### '):
            m = re.match(r'^### (\d+\.\d+)\s+(.+)$', line)
            if m:
                current_section = m.group(1)
                current_domain = m.group(2)
                level = current_section.split('.')[0]
                if level in ['6', '7', '8', '9', '10']:
                    current_level = str(int(level) - 5)  # 8 -> 3
                else:
                    current_level = level

        elif line.startswith('##### '):
            m = re.match(r'^##### (\d+\.\d+\.\d+)\s+(.+)$', line)
            if m:
                current_section = m.group(1)
                current_domain = m.group(2)
                current_level = current_section.split('.')[0]
                if current_level in ['6', '7', '8', '9', '10']:
                    current_level = str(int(current_level) - 5)

        # 检测"本项要求包括"
        elif "本项要求包括" in line or "包括：" in line or "包括：" in line:
            pass

        # 检测"a）...应..."条款
        elif re.match(r'^[a-zA-Z0-9（）\.]+）\s*', line):
            clause_text = extract_clause_text(line)
            if '应' in clause_text and len(clause_text) > 5:
                clause_num = extract_clause_number(line)
                try:
                    cou_id = gen_cou_id(current_level, current_section.replace('.', '-'), clause_num)
                    result = create_cou_file(cou_id, current_level, current_section, clause_num, clause_text, current_domain, CURRENT_LAW_NAME)
                    print(f"  [COU] {result[0]} | weight={result[2]} | {result[1][:40]}...")
                    cou_count += 1
                except Exception as e:
                    print(f"  [ERR] {line[:40]}... -> {e}")

        # 单条要求（无条款编号）
        elif line.startswith('应') and len(line) > 10:
            if '本项要求' not in line and '包括' not in line:
                try:
                    cou_id = gen_cou_id(current_level, current_section.replace('.', '-'), '0')
                    result = create_cou_file(cou_id, current_level, current_section, '', line, current_domain, CURRENT_LAW_NAME)
                    print(f"  [COU] {result[0]} | weight={result[2]} | {result[1][:40]}...")
                    cou_count += 1
                except Exception as e:
                    print(f"  [ERR] {line[:40]}... -> {e}")

        i += 1

    print(f"[*] 提取完成: {cou_count} 个COU")
    print(f"[*] 输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    import sys
    # 支持: python3 cou_batch_extract.py "GBT 28448-2018" 28448 "GBT 28448-2019"
    override = {}
    if len(sys.argv) > 1:
        search = sys.argv[1]
        law_code = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_LAW_CODE
        law_name = sys.argv[3] if len(sys.argv) > 3 else search
        candidates = list(VAULT_ROOT.glob(
            f"Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）/*{search}*.md"))
        if candidates:
            override['SOURCE_FILE'] = candidates[0]
            override['CURRENT_LAW_CODE'] = law_code
            override['CURRENT_LAW_NAME'] = law_name
            print(f"[*] 使用文件: {candidates[0].name}, code: {law_code}, name: {law_name}")
        else:
            print(f"[!] 未找到: {search}")
            sys.exit(1)
    main(override)
