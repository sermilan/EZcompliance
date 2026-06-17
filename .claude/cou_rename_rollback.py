#!/usr/bin/env python3
"""
COU文件重命名回退脚本
功能：从frontmatter的title字段恢复原始文件名
"""

import re
import yaml
from pathlib import Path

VAULT_ROOT = Path("/root/obsidian_vault")
RAW_COU_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"


def extract_frontmatter_title(filepath):
    """提取COU文件的frontmatter title"""
    content = filepath.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            return fm.get('title', '')
        except:
            pass
    return ''


def rollback_rename(dry_run=True):
    """回退重命名"""
    files = list(RAW_COU_DIR.glob("*.md"))
    print(f"[*] 扫描目录: {RAW_COU_DIR}")
    print(f"[*] 找到 {len(files)} 个COU文件")
    print(f"[*] 模式: {'Dry Run' if dry_run else '正式回退'}")

    restored_count = 0
    skipped_count = 0
    error_count = 0

    for fpath in files:
        try:
            original_title = extract_frontmatter_title(fpath)
            if not original_title:
                skipped_count += 1
                continue

            original_name = f"{original_title}.md"
            if original_name == fpath.name:
                # 已是原名
                skipped_count += 1
                continue

            new_path = RAW_COU_DIR / original_name

            # 检查目标是否已存在
            if new_path.exists() and new_path != fpath:
                print(f"  [SKIP] {fpath.name} -> {original_name} (目标已存在)")
                error_count += 1
                continue

            if dry_run:
                print(f"  [DRY] {fpath.name} -> {original_name}")
            else:
                fpath.rename(new_path)
                print(f"  [OK] {fpath.name} -> {original_name}")

            restored_count += 1

        except Exception as e:
            print(f"  [ERR] {fpath.name}: {e}")
            error_count += 1

    print()
    print(f"[*] 完成: 回退 {restored_count}, 跳过 {skipped_count}, 错误 {error_count}")


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    rollback_rename(dry_run=dry_run)