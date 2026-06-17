#!/usr/bin/env python3
"""
政策文件规范化重命名脚本
功能：
  - 已COU化的文件: 添加 [✓] 前缀，格式: [✓] {标准号}-{规范名称}.md
  - 未COU化的文件: 添加 [○] 前缀，格式: [○] {原始名称}.md

用法:
  python3 .claude/policy_rename.py [--dry-run]
"""

import re
import yaml
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/root/obsidian_vault")
POLICY_DIR = VAULT_ROOT / "Archive（归档）/PolicyArchive（政策法规库）/MD Documents（MD文档）"
RAW_COU_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"


def build_cou_source_map():
    """构建source到COU-R文件的映射"""
    source_map = {}
    for f in RAW_COU_DIR.glob("*.md"):
        try:
            content = f.read_text(encoding='utf-8')
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm = yaml.safe_load(fm_match.group(1))
                if fm and fm.get('source'):
                    src = fm['source']
                    if src not in source_map:
                        source_map[src] = 0
                    source_map[src] += 1
        except:
            pass
    return source_map


def extract_standard_info(filename):
    """从文件名提取标准号信息"""
    # 匹配 GB/T, GB/T, GAT, GBT 等格式
    patterns = [
        r'(GB/?T?\s*\d+(?:\.\d+)*-\d+)',  # GB/T 22239-2019
        r'(GAT\s*\d+-\d+)',                 # GAT 1389-2017
        r'(GBZ\s*\d+-\d+)',                 # GBZ 20985
        r'(GBT\s*\d+-\d+)',                 # GBT 20272
    ]
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            std = match.group(1)
            # 标准化格式
            std = re.sub(r'\s+', '', std)
            std = std.upper()
            std = re.sub(r'GB/?T', 'GBT', std)
            std = re.sub(r'GAT', 'GAT', std)
            std = re.sub(r'GBZ', 'GBZ', std)
            return std
    return None


def normalize_cou_filename(filename, source):
    """为已COU文件生成规范化的文件名"""
    # 提取标准号
    std = extract_standard_info(filename)
    if not std:
        # 尝试从source提取
        std = extract_standard_info(source)
    if not std:
        std = "未知标准"

    # 提取描述性名称（去掉标准号和常见前缀）
    name = filename
    # 去掉开头的编号如 "06.", "1.", "2." 等
    name = re.sub(r'^\d+[\.、]\s*', '', name)
    # 去掉标准号
    name = re.sub(r'(GB/?T?\s*\d+(?:\.\d+)*-\d+)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'(GAT\s*\d+-\d+)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'(GBZ\s*\d+-\d+)', '', name, flags=re.IGNORECASE)
    # 去掉括号内容
    name = re.sub(r'[（(][^）)]*[）)]', '', name)
    name = name.strip()
    # 去掉多余空格和横线
    name = re.sub(r'[\s\-–]+', '-', name).strip('-')

    if name:
        return f"[✓] {std}-{name}"
    else:
        return f"[✓] {std}"


def normalize_non_cou_filename(filename):
    """为未COU文件生成规范化的文件名"""
    name = filename
    # 去掉开头的编号
    name = re.sub(r'^\d+[\.、]\s*', '', name)
    # 去掉括号内容
    name = re.sub(r'[（(][^）)]*[）)]', '', name)
    name = name.strip()
    # 标准化空格和横线
    name = re.sub(r'[\s\-–]+', '-', name).strip('-')
    return f"[○] {name}"


def is_cou_matched(filename, source_map):
    """判断文件是否已COU化"""
    for src in source_map:
        std_nums = re.findall(r'(\d{4,})', src)
        if src in filename or filename in src:
            return src, source_map[src]
        for num in std_nums:
            if num in filename and len(num) >= 4:
                return src, source_map[src]
    return None, 0


def rename_policy_files(dry_run=True):
    """批量重命名政策文件"""
    if not POLICY_DIR.exists():
        print(f"[!] 目录不存在: {POLICY_DIR}")
        return

    source_map = build_cou_source_map()
    files = list(POLICY_DIR.glob("*.md"))

    print(f"[*] 扫描目录: {POLICY_DIR}")
    print(f"[*] 找到 {len(files)} 个政策文件")
    print(f"[*] 模式: {'Dry Run' if dry_run else '正式重命名'}")
    print(f"[*] COU来源数: {len(source_map)}")

    coued_count = 0
    not_coued_count = 0
    skipped_count = 0
    error_count = 0

    for fpath in files:
        try:
            old_name = fpath.stem
            src, cou_count = is_cou_matched(old_name, source_map)

            if src:
                # 已COU化
                new_name = normalize_cou_filename(old_name, src)
                coued_count += 1
            else:
                # 未COU化
                new_name = normalize_non_cou_filename(old_name)
                not_coued_count += 1

            new_path = POLICY_DIR / f"{new_name}.md"

            # 检查是否需要重命名
            if new_name == old_name:
                skipped_count += 1
                continue

            # 检查目标是否已存在
            if new_path.exists() and new_path != fpath:
                # 添加序号避免冲突
                base_name = new_name
                counter = 1
                while new_path.exists():
                    new_name = f"{base_name}-{counter}"
                    new_path = POLICY_DIR / f"{new_name}.md"
                    counter += 1

            if dry_run:
                status = "[✓COU]" if src else "[○待]"
                print(f"  [DRY] {status} {old_name}.md -> {new_name}.md")
            else:
                fpath.rename(new_path)
                status = "[✓COU]" if src else "[○待]"
                print(f"  [OK]  {status} {old_name}.md -> {new_name}.md")

        except Exception as e:
            print(f"  [ERR] {fpath.name}: {e}")
            error_count += 1

    print()
    print(f"[*] 完成统计:")
    print(f"    已COU化: {coued_count}")
    print(f"    未COU化: {not_coued_count}")
    print(f"    跳过(无需重命名): {skipped_count}")
    print(f"    错误: {error_count}")

    if not dry_run:
        print(f"[*] 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    rename_policy_files(dry_run=dry_run)