#!/usr/bin/env python3
"""
COU 去重合并脚本
功能：
  1. 扫描 COU-R（原始） 目录下的所有原始 COU
  2. 按 fingerprint 字段聚类
  3. 生成合并后的 COU-M（合并） 页面
  4. 输出 SaaS 导入用 JSON

用法：
  python3 .claude/cou_dedup.py
"""

import re
import json
import yaml
import hashlib
from pathlib import Path
from collections import defaultdict

WORK_ROOT = Path("/root/ezcompliance")
RAW_COU_DIR = WORK_ROOT / "COU" / "COU-R（原始）"
MERGED_COU_DIR = WORK_ROOT / "COU" / "COU-M（合并）"
EXPORT_FILE = WORK_ROOT / "data" / "cou_merged_export.json"
SCENE_DIR = WORK_ROOT / "场景"

# 主体归一化映射
SUBJECT_NORMALIZE = {
    # 数据控制者类
    "个人信息处理者": "数据控制者",
    "数据处理者": "数据控制者",
    "数据控制者": "数据控制者",
    "个人信息主体": "数据主体",
    "自然人": "数据主体",
    "网络运营者": "网络运营者",
    "关键信息基础设施运营者": "网络运营者",
    "网络安全等级保护对象运营者": "网络运营者",
    "重要数据处理者": "数据控制者",
    "数据安全责任人": "数据控制者",
    "运营者": "网络运营者",       # CII条例中的"运营者"
    "网络运营者": "网络运营者",
    # 服务提供类
    "受托处理者": "服务提供者",
    "受托人": "服务提供者",
    "接收方": "服务提供者",
    "境外接收方": "服务提供者",
    "云服务商": "服务提供者",
    "供应方": "服务提供者",
    "服务供应商": "服务提供者",
    "网络产品和服务的提供者": "服务提供者",
}

def normalize_subject(subject):
    """将具体主体名归一化为核心角色"""
    if not subject:
        return "未知主体"
    subject = subject.strip()
    return SUBJECT_NORMALIZE.get(subject, subject)


def compute_norm_fingerprint(cou_data):
    """用归一化主体计算指纹，用于跨标准去重"""
    s = normalize_subject(cou_data.get("subject", ""))
    a = cou_data.get("action", "").strip()
    o = cou_data.get("object", "").strip()
    return f"{s}|{a}|{o}"

# 合并权重计算：加权平均
def calculate_merged_weight(raw_cous):
    """
    所有来源权重加权平均
    """
    if not raw_cous:
        return 0.0
    total_weight = sum(cou["final_weight"] for cou in raw_cous)
    return round(total_weight / len(raw_cous), 2)


def extract_frontmatter_cou(filepath):
    """从 COU 文件中提取 COU 数据（前matter或嵌入式yaml块）"""
    content = filepath.read_text(encoding="utf-8")

    # 优先提取 YAML frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        try:
            data = yaml.safe_load(fm_match.group(1))
            if data and isinstance(data, dict):
                return data
        except:
            pass

    # 回退：解析文件末尾的嵌入式 yaml 代码块
    yaml_blocks = re.findall(r"```yaml\s*(.*?)\s*```", content, re.DOTALL)
    for block in reversed(yaml_blocks):
        try:
            data = yaml.safe_load(block)
            if data and isinstance(data, dict) and "fingerprint" in data:
                return data
        except:
            continue

    # 再试：从 markdown 内容中直接提取关键字段
    result = {}
    fp = re.search(r"fingerprint:\s*(\S+)", content)
    if fp:
        result["fingerprint"] = fp.group(1).strip()

    cou_id = re.search(r"cou_id:\s*(\S+)", content)
    if cou_id:
        result["cou_id"] = cou_id.group(1).strip()

    subject = re.search(r"subject:\s*(.+?)(?:\n|$)", content)
    if subject:
        result["subject"] = subject.group(1).strip()

    action = re.search(r"action:\s*(.+?)(?:\n|$)", content)
    if action:
        result["action"] = action.group(1).strip()

    obj = re.search(r"object:\s*(.+?)(?:\n|$)", content)
    if obj:
        result["object"] = obj.group(1).strip()

    cond = re.search(r"condition:\s*(.+?)(?:\n|$)", content)
    if cond:
        result["condition"] = cond.group(1).strip()

    bw = re.search(r"base_weight:\s*([0-9.]+)", content)
    if bw:
        result["base_weight"] = float(bw.group(1))

    wf = re.search(r"weight_factor:\s*([0-9.]+)", content)
    if wf:
        result["weight_factor"] = float(wf.group(1))

    fw = re.search(r"final_weight:\s*([0-9.]+)", content)
    if fw:
        result["final_weight"] = float(fw.group(1))

    domains = re.findall(r"domains:\s*\[(.*?)\]", content)
    if domains:
        result["domains"] = [d.strip() for d in domains[0].split(",")]

    source_match = re.search(r"source:\s*(.+?)(?:\n|$)", content)
    if source_match:
        result["source"] = source_match.group(1).strip()

    chapter_match = re.search(r"chapter:\s*(.+?)(?:\n|$)", content)
    if chapter_match:
        result["chapter"] = chapter_match.group(1).strip()

    if result:
        result["_file"] = str(filepath.relative_to(WORK_ROOT))
        return result

    return None


def build_fingerprint_index():
    """构建归一化fingerprint -> [raw_cou_list] 的索引，递归扫描子文件夹"""
    fingerprint_map = defaultdict(list)

    if RAW_COU_DIR.exists():
        # 递归扫描所有子文件夹中的 COU-R-*.md 文件
        for fpath in RAW_COU_DIR.rglob("COU-R-*.md"):
            cou_data = extract_frontmatter_cou(fpath)
            if not cou_data:
                continue

            # 用原始fingerprint做key进行归一化聚类
            fp = cou_data.get("fingerprint", "")
            if fp:
                # 同时保留原始fingerprint用于显示
                cou_data["_original_fp"] = fp
                # 用归一化后的指纹做聚类key
                norm_fp = compute_norm_fingerprint(cou_data)
                # 路径相对于 COU-R（原始）根目录，包含标准子文件夹
                cou_data["_file"] = str(fpath.relative_to(RAW_COU_DIR))
                fingerprint_map[norm_fp].append(cou_data)

    return fingerprint_map


def generate_merged_cou_id(fingerprint, index):
    """为合并后的 COU 生成唯一 ID"""
    seq = index + 1
    # 用fingerprint的md5前6位作为类别码（避免中文文件名问题）
    fp_hash = hashlib.md5(fingerprint.encode('utf-8')).hexdigest()[:6].upper()
    return f"COU-M-{fp_hash}-{seq:03d}"


def create_merged_cou_page(merged_id, norm_fingerprint, raw_cous):
    """创建合并后的 COU 实体页"""
    sources = [cou["source"] for cou in raw_cous]
    max_weight = max(cou["final_weight"] for cou in raw_cous)
    avg_weight = calculate_merged_weight(raw_cous)

    # 归一化主体
    norm_subjects = list({normalize_subject(cou.get("subject", "")) for cou in raw_cous})
    # 原始主体
    orig_subjects = list({cou.get("subject", "") for cou in raw_cous})
    actions = list({cou.get("action", "") for cou in raw_cous})
    objects = list({cou.get("object", "") for cou in raw_cous})
    conditions = list({cou.get("condition", "") for cou in raw_cous if cou.get("condition")})

    # 去重后的来源列表
    unique_sources = list(dict.fromkeys(sources))

    # 判断是否跨标准合并
    unique_laws = set()
    for s in unique_sources:
        if "个人信息保护法" in s:
            unique_laws.add("PIPL")
        elif "数据安全法" in s:
            unique_laws.add("DSL")
        elif "GB/T 39204" in s or "39204" in s:
            unique_laws.add("GB/T 39204")
        elif "GBT 22239" in s or "22239" in s:
            unique_laws.add("GBT 22239")
        elif "网络安全法" in s:
            unique_laws.add("WL")
        else:
            unique_laws.add(s[:10])

    cross_std = len(unique_laws) > 1
    cross_std_note = f"（跨{len(unique_laws)}个标准合并）" if cross_std else ""

    content = f"""# {merged_id}

> **状态**: 已合并 (Merged) {cross_std_note}
> **来源数**: {len(raw_cous)} 个原始 COU
> **归一化指纹**: {norm_fingerprint}

## 来源原始 COU

"""
    for cou in raw_cous:
        fp_display = cou.get('_original_fp', '')[:30]
        # 包含标准子文件夹路径的 wikilink
        rel_path = cou.get('_file', '')
        content += f"- [[{rel_path}|{Path(rel_path).stem}]] — {cou.get('source', '')} {cou.get('chapter', '')} (fp: {fp_display}...)\n"

    domains_list = sorted({cou.get('domains', ['unknown'])[0] for cou in raw_cous if cou.get('domains')})

    content += f"""
## 共性解剖结构

| 要素 | 内容 |
|------|------|
| 归一化主体 | {' / '.join(norm_subjects)} |
| 原始主体 | {' / '.join(orig_subjects)} |
| 动作 | {' / '.join(actions)} |
| 客体 | {' / '.join(objects)} |
| 条件 | {' / '.join(conditions) if conditions else '无特定条件'} |

## 权重计算

| 指标 | 值 |
|------|---|
| 最高来源权重 | {max_weight} |
| 加权平均权重 | **{avg_weight}** |
| 来源数量 | {len(raw_cous)} |
| 涉及标准 | {', '.join(sorted(unique_laws))} |

## 元数据

```yaml
cou_id: {merged_id}
type: merged
fingerprint: {norm_fingerprint}
sources: {unique_sources}
raw_cou_count: {len(raw_cous)}
avg_weight: {avg_weight}
max_weight: {max_weight}
domains: [{', '.join(domains_list)}]
norm_subjects: {norm_subjects}
cross_standard: {cross_std}
```
"""

    out_path = MERGED_COU_DIR / f"{merged_id}.md"
    out_path.write_text(content, encoding="utf-8")
    return out_path


def export_for_saas(fingerprint_map):
    """导出 SaaS 格式的 JSON"""
    export_data = []

    for idx, (fp, raw_cous) in enumerate(fingerprint_map.items()):
        avg_weight = calculate_merged_weight(raw_cous)
        max_weight = max(cou["final_weight"] for cou in raw_cous)

        # 找最高权重来源作为主来源
        primary = max(raw_cous, key=lambda x: x["final_weight"])

        # 归一化主体
        norm_subject = normalize_subject(primary.get("subject", ""))

        # 与 generate_merged_cou_id 保持一致的ID生成逻辑
        seq = idx + 1
        fp_hash = hashlib.md5(fp.encode('utf-8')).hexdigest()[:6].upper()
        merged_id = f"COU-M-{fp_hash}-{seq:03d}"

        # 判断是否跨标准
        unique_laws = set()
        for s in {cou.get("source", "") for cou in raw_cous}:
            if "个人信息保护法" in s:
                unique_laws.add("PIPL")
            elif "数据安全法" in s:
                unique_laws.add("DSL")
            elif "GB/T 39204" in s or "39204" in s:
                unique_laws.add("GB/T 39204")
            elif "GBT 22239" in s or "22239" in s:
                unique_laws.add("GBT 22239")
            elif "网络安全法" in s:
                unique_laws.add("WL")
            else:
                unique_laws.add(s[:10])

        export_data.append({
            "cou_id": merged_id,
            "fingerprint": fp,
            "norm_subject": norm_subject,
            "subject": primary.get("subject", ""),
            "action": primary.get("action", ""),
            "object": primary.get("object", ""),
            "condition": primary.get("condition", ""),
            "avg_weight": avg_weight,
            "max_weight": max_weight,
            "source_count": len(raw_cous),
            "primary_source": primary.get("source", ""),
            "all_sources": list({cou.get("source", "") for cou in raw_cous}),
            "domains": list({cou.get("domains", [""])[0] for cou in raw_cous if cou.get("domains")}),
            "cross_standard": len(unique_laws) > 1,
            "standards": list(unique_laws),
        })

    EXPORT_FILE.write_text(
        json.dumps(export_data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"[*] SaaS export: {EXPORT_FILE} ({len(export_data)} merged COUs)")
    return export_data


def main():
    print("[*] COU 去重合并处理")
    print(f"[*] 扫描目录: {RAW_COU_DIR}")

    MERGED_COU_DIR.mkdir(parents=True, exist_ok=True)

    # 清理旧的合并文件
    for f in MERGED_COU_DIR.glob("*.md"):
        f.unlink()
    print(f"[*] 已清理旧合并文件")

    fingerprint_map = build_fingerprint_index()
    print(f"[*] 发现 {len(fingerprint_map)} 个唯一动作指纹")

    merged_count = 0
    for fp, raw_cous in fingerprint_map.items():
        idx = merged_count
        merged_id = generate_merged_cou_id(fp, idx)
        create_merged_cou_page(merged_id, fp, raw_cous)
        merged_count += 1

    print(f"[*] 生成 {merged_count} 个合并 COU 页面")

    export_for_saas(fingerprint_map)
    print("[*] 完成!")


if __name__ == "__main__":
    main()
