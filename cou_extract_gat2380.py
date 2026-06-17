#!/usr/bin/env python3
"""
GAT 2380-2026 COU 批量提取脚本 v2
修复: 命名冲突 / 切词 / YAML格式 / 冗余
"""
import re, json, hashlib
from pathlib import Path
from collections import defaultdict

WORK_DIR = Path("/root/ezcompliance")
SOURCE_FILE = WORK_DIR / "GAT 2380—2026《信息安全技术 网络安全等级保护数据安全基本要求》（报批稿）.md"
STANDARD_CODE = "2380"
STANDARD_NAME = "GAT 2380-2026"
OUTPUT_DIR = WORK_DIR / "COU-R" / "GAT2380-2026"

# 清空并重建
import shutil
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LEVEL_WEIGHT = {"4": 10.0, "3": 8.0, "2": 6.0, "1": 4.0}
ACTION_WEIGHT = {"应": 1.0, "宜": 0.7, "可": 0.4}
ACTION_EN = {"应": "SHALL", "宜": "SHOULD", "可": "MAY"}

DOMAIN_MAP = {
    "一般规定": ["通用安全", "数据安全总则"],
    "安全物理环境": ["物理安全", "环境安全"],
    "安全通信网络": ["通信网络安全", "数据传输安全"],
    "安全区域边界": ["边界安全", "网络隔离"],
    "安全计算环境": ["计算环境安全", "数据存储安全"],
    "安全数据处理": ["数据处理安全", "数据全生命周期"],
    "安全管理中心": ["集中管控", "安全监测"],
    "安全管理制度": ["制度管理", "合规管理"],
    "安全管理机构": ["组织架构", "安全治理"],
    "安全管理人员": ["人员管理", "安全培训"],
    "安全建设管理": ["建设管理", "供应链安全"],
    "安全运维管理": ["运维管理", "持续运营"],
}

DATA_PHASES_KW = {
    "收集": "数据收集", "存储": "数据存储", "使用": "数据使用",
    "加工": "数据加工", "传输": "数据传输", "提供": "数据提供",
    "公开": "数据公开", "销毁": "数据销毁", "删除": "数据删除",
    "共享": "数据共享", "交换": "数据交换", "导入": "数据导入",
    "导出": "数据导出", "备份": "数据备份", "恢复": "数据恢复",
    "脱敏": "数据脱敏", "溯源": "数据溯源", "标记": "数据标记",
    "识别": "数据识别",
}

DATA_CLASS_KW = {
    "核心数据": "核心数据", "重要数据": "重要数据", "敏感数据": "敏感数据",
    "一般数据": "一般数据", "敏感个人信息": "敏感个人信息",
    "个人信息": "个人信息", "鉴别数据": "鉴别数据", "业务数据": "业务数据",
    "审计数据": "审计数据", "配置数据": "配置数据", "溯源数据": "溯源数据",
    "生物特征": "生物特征信息",
}

# 动作词模式（动词短语）
ACTION_PATTERNS = [
    (r'^(采取|配备|设置|部署|配置|提供|建立|制定|实现|支持|采用|确定|记录|进行|满足|具备|执行|定期|保护|识别|规范|管理|检测|监测|控制|授权|加密|脱敏|备份|恢复|销毁|清除|标记|溯源|限制|审核|检查|评估|审批|培训|上报|报告|保证|确保|明确|设立|签署|开展|约束|编制|通知|定义|指定|集中)', 1),
    (r'^(对|在|应能|应能够)', 0),
]

def get_weight(level, action_word):
    base = LEVEL_WEIGHT.get(level, 6.0)
    factor = ACTION_WEIGHT.get(action_word, 1.0)
    return round(base * factor, 1)

def level_from_section(sec):
    m = {"4": "1", "5": "2", "6": "3", "7": "4", "8": "5"}
    return m.get(sec.split('.')[0], sec.split('.')[0])

def detect_phases(text):
    return list({v for k, v in DATA_PHASES_KW.items() if k in text}) or ["数据处理全流程"]

def detect_classes(text):
    return list({v for k, v in DATA_CLASS_KW.items() if k in text})

def extract_action_object(text):
    """从条款文本提取动作和客体。处理 '对XX进行YY' '在XX时YY' 等汉语句式。"""
    t = text
    for a in ['应', '宜', '可']:
        if t.startswith(a):
            t = t[1:].strip()
            break

    if not t or len(t) < 2:
        return text[:20], text[:50]

    action = ""
    obj = ""

    # 特殊处理: "对...进行/采取/..." 和 "在...前/时...提出/进行/..."
    m_dui = re.match(r'^(对|在)(.+?)(进行|采取|实现|开展|执行|保护|识别|控制|管理|检测|监测|规范|约束|限制|记录|提出|建立|制定|提供|设置|配置)(.+)', t)
    if m_dui:
        action = m_dui.group(1) + m_dui.group(2) + m_dui.group(3)
        obj = m_dui.group(4).strip('。，；；。、 \t\n')[:60]
        return action, obj

    # 标准动作词匹配
    for pat, grp in ACTION_PATTERNS:
        m = re.search(pat, t)
        if m:
            action = m.group(grp)
            rest = t[m.end(grp):].strip('。，；；。、 \t\n')

            # 在标点边界截断
            cut = len(rest)
            for sep in ['。', '；', '，', '、', '包括', '等，']:
                idx = rest.find(sep)
                if 10 < idx < cut:
                    cut = idx
            if cut > 80:
                cut = 80
            obj = rest[:cut].strip('。，；；。、 \t\n')
            if not obj:
                obj = rest[:50]
            break

    if not action:
        action = t[:25].strip()
        obj = t[25:75].strip('。，；；。、 \t\n') if len(t) > 25 else t[:50]

    if not obj:
        obj = t[:50]

    return action, obj

def compute_fingerprint(subject, action, obj):
    return f"{subject}|{action}|{obj}"

def gen_cou_filename(level, section, clause):
    """生成唯一文件名，section 用完整小节号"""
    sec_clean = section.replace('.', '-')
    clause_clean = clause.replace('.', '-') if clause else "X"
    return f"COU-R-{STANDARD_CODE}-L{level}-{sec_clean}-{clause_clean}"

def parse_document(filepath):
    content = filepath.read_text(encoding="utf-8")
    lines = content.split('\n')

    current_level = "1"
    current_section = ""       # 如 "6.5.1"
    current_full_section = ""  # 如 "6.5.1.1" 包含嵌套子节
    current_domain = ""
    current_clause_letter = ""
    results = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # H2: ## 6 第三级...
        if line.startswith('## ') and not line.startswith('###'):
            m = re.match(r'^## (\d+)\s+(.+)$', line)
            if m:
                current_section = m.group(1)
                current_full_section = m.group(1)
                current_domain = m.group(2)
                current_level = level_from_section(current_section)
                current_clause_letter = ""

        # H3: ### 6.5 安全计算环境
        elif line.startswith('### ') and not line.startswith('####'):
            m = re.match(r'^### (\d+\.\d+)\s+(.+)$', line)
            if m:
                current_section = m.group(1)
                current_full_section = m.group(1)
                current_domain = m.group(2)
                current_clause_letter = ""

        # H4: #### 6.5.1 身份鉴别
        elif line.startswith('#### '):
            m = re.match(r'^#### (\d+\.\d+\.\d+)\s+(.+)$', line)
            if m:
                current_section = m.group(1)
                current_full_section = m.group(1)
                current_domain = m.group(2)
                current_clause_letter = ""

        # 数字子节标题（纯文本）: 6.7.1 / 6.7.2 / 7.7.2 / 6.5.1.1 ...
        elif re.match(r'^\d+\.\d+\.\d+(?:\.\d+)?\s+', line) and not line.startswith('#'):
            m = re.match(r'^(\d+\.\d+\.\d+(?:\.\d+)?)\s+(.+)$', line)
            if m:
                current_full_section = m.group(1)
                # 检查是否包含"对于重要""对于一般""对于核心"等系统限定
                sub_domain = m.group(2)
                if any(kw in sub_domain for kw in ['对于一般', '对于重要', '对于核心', '集中管控', '除满足']):
                    # 这是一个嵌套子节，保持当前domain但更新section
                    pass
                current_clause_letter = ""

        # 条款 a）b）c）...
        elif re.match(r'^([a-zA-Z])[）\)]\s*', line):
            m = re.match(r'^([a-zA-Z])[）\)]\s*(.+)', line)
            if m:
                letter = m.group(1)
                clause_text = m.group(2).strip()
                for aw in ['应', '宜', '可']:
                    if clause_text.startswith(aw):
                        results.append({
                            'level': current_level,
                            'section': current_full_section,
                            'domain': current_domain,
                            'clause': letter,
                            'clause_text': clause_text,
                            'action_word': aw,
                            'full_text': f"{letter}）{clause_text}",
                        })
                        break

        # 独立条款（无字母编号）- 排除 "应急预案" "应急响应" 等非条款词
        elif re.match(r'^(应|宜|可)', line) and len(line) > 8:
            # 跳过非条款引导词
            if any(line.startswith(w) for w in ['应急预案', '应急响应', '应用', '应该']):
                i += 1
                continue
            for aw in ['应', '宜', '可']:
                if line.startswith(aw):
                    results.append({
                        'level': current_level,
                        'section': current_full_section,
                        'domain': current_domain,
                        'clause': '',
                        'clause_text': line,
                        'action_word': aw,
                        'full_text': line,
                    })
                    break

        # 处理 "XX要求包括：" 后面的内联编号条款（已被上面的正则捕获）
        # 处理多条款同行 (a）xxx；b）xxx)
        elif re.match(r'^[a-zA-Z][）\)]', line) and '；' in line:
            # 拆分行内多个条款
            parts = re.split(r'；\s*(?=[a-zA-Z][）\)])', line)
            for part in parts:
                part = part.strip()
                m2 = re.match(r'^([a-zA-Z])[）\)]\s*(.+)', part)
                if m2:
                    letter = m2.group(1)
                    clause_text = m2.group(2).strip()
                    for aw in ['应', '宜', '可']:
                        if aw in clause_text[:2]:
                            results.append({
                                'level': current_level,
                                'section': current_full_section,
                                'domain': current_domain,
                                'clause': letter,
                                'clause_text': clause_text,
                                'action_word': aw,
                                'full_text': part,
                            })
                            break

        i += 1

    return results

def create_cou(clause_data):
    level = clause_data['level']
    section = clause_data['section']
    domain = clause_data['domain']
    clause_text = clause_data['clause_text']
    action_word = clause_data['action_word']
    full_text = clause_data['full_text']
    clause_num = clause_data.get('clause', '')

    action, obj = extract_action_object(clause_text)
    fingerprint = compute_fingerprint("网络运营者", action, obj)
    final_weight = get_weight(level, action_word)
    domains = DOMAIN_MAP.get(domain, ['通用安全'])
    data_phases = detect_phases(clause_text)
    data_classes = detect_classes(clause_text)

    filename = gen_cou_filename(level, section, clause_num)
    cou_id = filename

    condition = f"定级为第{level}级时"
    if "重要数据处理系统" in clause_text or "重要数据" in clause_text:
        condition += "；涉及重要数据"
    if "核心数据" in clause_text:
        condition += "；涉及核心数据"

    # 用 YAML 兼容的列表格式
    domains_yaml = "[" + ", ".join(domains) + "]"
    phases_yaml = "[" + ", ".join(data_phases) + "]"
    classes_yaml = "[" + ", ".join(data_classes) + "]" if data_classes else "[]"

    content = f"""---
title: "{cou_id}"
cou_id: "{cou_id}"
source: "{STANDARD_NAME}"
standard_code: "{STANDARD_CODE}"
chapter: "{section}"
domain: "{domain}"
clause: "{clause_num}"
level: "{level}"
action_word: "{action_word}"
action_en: "{ACTION_EN.get(action_word, 'SHALL')}"
subject: "网络运营者"
action: "{action}"
object: "{obj}"
condition: "{condition}"
base_weight: {LEVEL_WEIGHT.get(level, 6.0)}
action_weight_factor: {ACTION_WEIGHT.get(action_word, 1.0)}
final_weight: {final_weight}
domains: {domains_yaml}
data_phases: {phases_yaml}
data_classes: {classes_yaml}
fingerprint: "{fingerprint}"
tags: ["{STANDARD_NAME}", "数据安全", "等级保护", "第{level}级"]
---

# {cou_id}

> **来源**: {STANDARD_NAME}《信息安全技术 网络安全等级保护数据安全基本要求》
> **章节**: 第{level}级 - {domain} - {section}{f' (条款{clause_num})' if clause_num else ''}
> **动作词**: {action_word} ({ACTION_EN.get(action_word, 'SHALL')}) | **权重**: {final_weight}

## 解剖结构

| 要素 | 内容 |
|------|------|
| 主体 | 网络运营者 |
| 动作 | {action} |
| 客体 | {obj} |
| 条件 | {condition} |
| 数据环节 | {", ".join(data_phases)} |
| 数据分类 | {", ".join(data_classes) if data_classes else '通用'} |
| 安全域 | {", ".join(domains)} |
| 权重 | {LEVEL_WEIGHT.get(level, 6.0)} × {ACTION_WEIGHT.get(action_word, 1.0)} = **{final_weight}** |

## 原文

> {full_text}
"""

    filepath = OUTPUT_DIR / f"{filename}.md"
    filepath.write_text(content, encoding="utf-8")
    return cou_id, fingerprint, final_weight

def main():
    print(f"[*] GAT 2380-2026 COU 提取 v2")
    print(f"[*] 源文件: {SOURCE_FILE}")

    clauses = parse_document(SOURCE_FILE)
    print(f"[*] 解析到 {len(clauses)} 条原始条款")

    # 过滤
    skip_kw = ['术语和定义', '规范性引用', '前言', '引言', '范围', '参考文献', '目次']
    filtered = [c for c in clauses if not any(kw in c.get('domain', '') or kw in c.get('section', '') for kw in skip_kw)]
    print(f"[*] 过滤后 {len(filtered)} 条有效条款")

    # 创建 COU
    all_cous = []
    id_counter = defaultdict(int)
    for i, clause in enumerate(filtered):
        try:
            cou_id, fingerprint, final_weight = create_cou(clause)
            id_counter[cou_id] += 1
            clause['cou_id'] = cou_id
            clause['_fingerprint'] = fingerprint
            clause['final_weight'] = final_weight
            all_cous.append(clause)
            if (i + 1) % 50 == 0:
                print(f"  ... {i+1}/{len(filtered)}")
        except Exception as e:
            print(f"  [ERR] {clause.get('clause_text', '')[:40]}... -> {e}")

    # 统计
    dupes = {k: v for k, v in id_counter.items() if v > 1}
    file_count = len(list(OUTPUT_DIR.glob("*.md")))

    print(f"\n[*] 生成 {len(all_cous)} 个 COU-R 条目 → {file_count} 个文件")
    if dupes:
        print(f"[!] {len(dupes)} 个 ID 仍有冲突（需进一步处理）:")
        for k, v in list(dupes.items())[:5]:
            print(f"    {k}: {v}次")

    # 统计
    by_level = defaultdict(lambda: {"应": 0, "宜": 0, "可": 0, "total": 0})
    for c in all_cous:
        by_level[c['level']][c['action_word']] += 1
        by_level[c['level']]['total'] += 1

    print(f"\n{'等级':<8} {'应':>5} {'宜':>5} {'合计':>6}")
    total = {"应": 0, "宜": 0, "total": 0}
    for lv in ['1', '2', '3', '4']:
        s = by_level[lv]
        print(f"第{lv}级{'':>3} {s['应']:>5} {s['宜']:>5} {s['total']:>6}")
        for k in total:
            total[k] += s[k]
    print(f"{'合计':<8} {total['应']:>5} {total['宜']:>5} {total['total']:>6}")

    # 重新导出 JSON
    export = []
    for c in all_cous:
        action, obj = extract_action_object(c['clause_text'])
        export.append({
            "cou_id": c['cou_id'],
            "source": STANDARD_NAME,
            "standard_code": STANDARD_CODE,
            "level": c['level'],
            "chapter": c['section'],
            "domain": c['domain'],
            "clause": c.get('clause', ''),
            "action_word": c['action_word'],
            "action_en": ACTION_EN.get(c['action_word'], 'SHALL'),
            "subject": "网络运营者",
            "action": action,
            "object": obj,
            "condition": f"定级为第{c['level']}级时",
            "final_weight": c['final_weight'],
            "fingerprint": c['_fingerprint'],
            "domains": DOMAIN_MAP.get(c['domain'], ['通用安全']),
            "data_phases": detect_phases(c['clause_text']),
            "data_classes": detect_classes(c['clause_text']),
            "full_text": c['full_text'],
        })

    json_path = WORK_DIR / "data" / "GAT2380-2026_COU_export.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[*] JSON 导出: {json_path} ({len(export)} 条)")

    print(f"\n[*] 完成! 输出: {OUTPUT_DIR}")
    return all_cous

if __name__ == "__main__":
    main()
