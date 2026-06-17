#!/usr/bin/env python3
"""
COU 格式迁移脚本
功能：
  1. 读取旧格式 COU-S-39204-*.md 文件（无 frontmatter，无 fingerprint）
  2. 提取 subject/action/object 计算 fingerprint
  3. 添加 frontmatter 和 fingerprint
  4. 输出迁移后的文件到 COU-R（原始） 目录

用法：
  python3 .claude/cou_migrate.py
"""

import re
import hashlib
import yaml
from pathlib import Path

VAULT_ROOT = Path("/root/obsidian_vault")
OLD_COU_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU"
NEW_COU_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"

NEW_COU_DIR.mkdir(parents=True, exist_ok=True)


def compute_fingerprint(subject, action, obj):
    """根据主体+动作+客体计算指纹"""
    text = f"{subject}|{action}|{obj}"
    # 用前8位md5或直接用语义
    return text


def normalize_action(action_str):
    """标准化动作词"""
    return action_str.replace("、", "-").strip()


def migrate_one_file(fpath):
    """迁移单个旧 COU 文件"""
    content = fpath.read_text(encoding="utf-8")

    # 提取 yaml 代码块中的元数据
    yaml_match = re.search(r"```yaml\s*(.*?)\s*```", content, re.DOTALL)
    if not yaml_match:
        print(f"  [SKIP] {fpath.name} - 无yaml块")
        return False

    try:
        meta = yaml.safe_load(yaml_match.group(1))
    except:
        print(f"  [SKIP] {fpath.name} - yaml解析失败")
        return False

    if not meta or "subject" not in meta:
        print(f"  [SKIP] {fpath.name} - 缺少subject字段")
        return False

    # 提取原文
    quote_match = re.search(r"## 原文\s*\n>\s*(.+?)(?:\n\n|\n##)", content, re.DOTALL)
    original_text = quote_match.group(1).strip() if quote_match else ""

    # 提取关联场景
    scene_links = re.findall(r"\[\[场景-[^\]]+\]\]", content)

    # 计算 fingerprint
    subject = meta.get("subject", "")
    action = normalize_action(meta.get("action", ""))
    obj = meta.get("object", "")
    fingerprint = compute_fingerprint(subject, action, obj)

    # 提取章节信息
    chapter_match = re.search(r"chapter:\s*(.+?)(?:\n|$)", yaml_match.group(1))
    clause_match = re.search(r"clause:\s*(.+?)(?:\n|$)", yaml_match.group(1))
    domains_match = re.search(r"domains:\s*\[(.*?)\]", yaml_match.group(1))
    source_match = re.search(r"source:\s*(.+?)(?:\n|$)", yaml_match.group(1))

    chapter = chapter_match.group(1).strip() if chapter_match else ""
    clause = clause_match.group(1).strip() if clause_match else ""
    domains_str = domains_match.group(1).strip() if domains_match else "分析识别"
    domains = [d.strip() for d in domains_str.split(",")] if domains_str else ["分析识别"]
    source = source_match.group(1).strip() if source_match else "GB/T 39204-2022"

    base_weight = meta.get("base_weight", 8)
    final_weight = meta.get("final_weight", 8.0)

    # 生成新文件名（带COU-R前缀）
    old_cou_id = meta.get("cou_id", fpath.stem)
    new_cou_id = old_cou_id.replace("COU-S-39204", "COU-R-S-39204")
    new_fname = f"{new_cou_id}.md"
    new_fpath = NEW_COU_DIR / new_fname

    # 构建新文件内容（带frontmatter）
    new_content = f"""---
title: "{new_cou_id}"
cou_id: "{new_cou_id}"
source: "{source}"
chapter: "{chapter}"
clause: "{clause}"
subject: "{subject}"
action: "{action}"
object: "{obj}"
condition: "{meta.get('condition', '无特定触发条件')}"
base_weight: {base_weight}
weight_factor: {round(final_weight / base_weight, 1) if base_weight else 1.0}
final_weight: {final_weight}
domains: {domains}
fingerprint: "{fingerprint}"
---

# {new_cou_id}

> **来源**: [[GB T 39204-2022 信息安全技术 关键信息基础设施安全保护要求]]
> **章节**: {chapter}{' '+clause if clause and clause not in ['a','b','c','d','e','f','g','h','i','j','k'] else ''}
> **层级**: R (原始COU · Raw)
> **基础权重**: {base_weight}

## 解剖结构

| 要素 | 内容 |
|------|------|
| 主体 | {subject} |
| 动作 | {action} |
| 客体 | {obj} |
| 条件 | {meta.get('condition', '无特定触发条件')} |
| 权重计算 | {base_weight} × {round(final_weight/base_weight,1) if base_weight else 1.0} = **{final_weight}** |

## 原文

> {original_text}

## 关联场景

{chr(10).join(f'- [[{s}]]' for s in scene_links) if scene_links else '- (无关联场景)'}

## 元数据

```yaml
cou_id: {new_cou_id}
source: {source}
chapter: {chapter}
clause: {clause}
subject: {subject}
action: {action}
object: {obj}
condition: "{meta.get('condition', '无特定触发条件')}"
base_weight: {base_weight}
weight_factor: {round(final_weight/base_weight, 1) if base_weight else 1.0}
final_weight: {final_weight}
domains: {domains}
fingerprint: "{fingerprint}"
```
"""

    new_fpath.write_text(new_content, encoding="utf-8")
    print(f"  [MIGRATED] {fpath.name} → {new_fname} (fp={fingerprint})")
    return True


def main():
    print("[*] COU 格式迁移脚本")
    print("[*] 源目录: " + str(OLD_COU_DIR))
    print("[*] 输出目录: " + str(NEW_COU_DIR))

    old_files = list(OLD_COU_DIR.glob("COU-S-39204-*.md"))
    print(f"[*] 找到 {len(old_files)} 个旧格式 COU 文件")

    success = 0
    for fpath in sorted(old_files):
        if migrate_one_file(fpath):
            success += 1

    print(f"[*] 迁移完成: {success}/{len(old_files)} 个文件")
    print(f"[*] 新文件输出至: {NEW_COU_DIR}")


if __name__ == "__main__":
    main()
