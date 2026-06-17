#!/usr/bin/env python3
"""
COU文件规范化重命名脚本
功能：
  1. 读取COU-R文件的frontmatter信息
  2. 按规范生成新文件名
  3. 重命名文件并更新内部链接

命名规范：
  法律类: COU-R-{LAW_CODE}-{ARTICLE_NUM}-{NORM_ACTION}.md
  标准类: COU-R-{STD_CODE}-{LEVEL}-{SECTION}-{CLAUSE}-{SUB}.md

用法:
  python3 .claude/cou_rename.py [--dry-run]
"""

import re
import yaml
import shutil
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/root/obsidian_vault")
RAW_COU_DIR = VAULT_ROOT / "Wiki（维基）/Reference（参考）/COU/COU-R（原始）"

# 动作词标准化映射
ACTION_MAP = {
    '应当': 'YING',
    '必须': 'BIXU',
    '不得': 'BU',
    '有权': 'YOU',
    '可以': 'KE',
    '处理': 'CHULI',
    '收集': 'SHOUJI',
    '使用': 'SHIYONG',
    '存储': 'CUNCHU',
    '删除': 'SHANCHU',
    '提供': 'TIGONG',
    '传输': 'CHUANSHU',
    '公开': 'GONGKAI',
    '公告': 'GONGGAO',
}

# 法典映射
LAW_CODE_MAP = {
    '个人信息保护法': 'PIPL',
    '数据安全法': 'DSL',
    '网络安全法': 'WL',
    '密码法': 'MM',
    '保守国家秘密法': 'BAOMI',
    '国家安全法': 'GUOJA',
    '刑法': 'XING',
    '消费者权益保护法': 'XIAOF',
    '基本医疗卫生与健康促进法': 'YILIAO',
    '电信条例': 'DIANX',
    '关键信息基础设施安全保护条例': 'CII',
    '网络数据安全管理条例': 'WTSJ',
    '网络安全审查办法': 'WLSC',
    '汽车数据安全管理若干规定': 'QICHE',
    '儿童个人信息网络保护规定': 'ERTONG',
    '互联网信息服务管理办法': 'HLWXX',
    '生成式人工智能服务管理暂行办法': 'SHENGCH',
}

# 中文数字转换
CN_TO_ARABIC = {
    '零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
    '五': '5', '六': '6', '七': '7', '八': '8', '九': '9',
    '十': '10', '百': '100',
}


def cn_to_arabic(cn_str):
    """将中文数字转换为阿拉伯数字"""
    if not cn_str:
        return '0'
    result = 0
    temp = 0
    for char in cn_str:
        if char in CN_TO_ARABIC:
            val = int(CN_TO_ARABIC[char])
            if val >= 10:
                if temp > 0:
                    result += temp * val
                else:
                    result = val
                temp = 0
            else:
                temp = val
    result += temp
    return str(result) if result > 0 else '0'


def normalize_action(action):
    """标准化动作词"""
    if not action:
        return 'UNKNOWN'
    for k, v in ACTION_MAP.items():
        if k in action:
            return v
    # 取前4个字符
    return action[:4].upper()


def get_std_code(source):
    """从来源获取标准代码"""
    if not source:
        return 'UNKNOWN'
    # 检查是否是已知法典
    if source in LAW_CODE_MAP:
        return LAW_CODE_MAP[source]
    # 从标准名提取数字代码
    match = re.search(r'(\d{4,})', source)
    if match:
        return match.group(1)
    # 回退：取拼音首字母或前4字符
    return re.sub(r'[^\w]', '', source)[:4].upper()


def extract_frontmatter(filepath):
    """提取COU文件的frontmatter"""
    content = filepath.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        try:
            return yaml.safe_load(fm_match.group(1))
        except:
            pass
    return {}


def generate_new_filename(cou_data, old_name):
    """根据COU数据生成新文件名"""
    source = cou_data.get('source', '')
    article = cou_data.get('article', '')
    sub_clause = cou_data.get('sub_clause', '')
    action = cou_data.get('action', '')

    std_code = get_std_code(source)

    # 判断是法律类还是标准类
    if source in LAW_CODE_MAP or '法' in source or '条例' in source or '办法' in source:
        # 法律类: COU-R-{CODE}-{ART}-{ACT}
        art_num = cn_to_arabic(article) if not article.isdigit() else article
        art_num = art_num.zfill(3)  # 补零到3位
        norm_action = normalize_action(sub_clause or action)
        new_name = f"COU-R-{std_code}-{art_num}-{norm_action}"
    else:
        # 标准类: 保持原有结构，简化命名
        # 原有格式: COU-R-{CODE}-{LEVEL}-{SECTION}-{CLAUSE}-{SUB}[-{SUFFIX}]
        parts = old_name.replace('COU-R-', '').split('-')
        if len(parts) >= 3:
            # 保留层级、章节、条款信息
            level = parts[1]
            section = parts[2] if len(parts) > 2 else '0'
            clause = parts[3] if len(parts) > 3 else '0'
            sub = parts[4] if len(parts) > 4 else '0'
            # 保留原始后缀(a,b,c等)，避免多文件冲突
            if len(parts) > 5:
                suffix = parts[5]
                sub = f"{sub}-{suffix}"
            new_name = f"COU-R-{std_code}-{level}-{section}-{clause}-{sub}"
        else:
            new_name = old_name.replace('COU-R-', f'COU-R-{std_code}-')

    return new_name


def rename_cou_files(dry_run=True):
    """批量重命名COU文件"""
    if not RAW_COU_DIR.exists():
        print(f"[!] 目录不存在: {RAW_COU_DIR}")
        return

    files = list(RAW_COU_DIR.glob("*.md"))
    print(f"[*] 扫描目录: {RAW_COU_DIR}")
    print(f"[*] 找到 {len(files)} 个COU文件")
    print(f"[*] 模式: {'Dry Run (不实际重命名)' if dry_run else '正式重命名'}")

    renamed_count = 0
    skipped_count = 0
    error_count = 0

    for fpath in files:
        try:
            cou_data = extract_frontmatter(fpath)
            old_name = fpath.stem

            # 生成新文件名
            new_name = generate_new_filename(cou_data, old_name)

            if new_name == old_name:
                skipped_count += 1
                continue

            new_path = RAW_COU_DIR / f"{new_name}.md"

            # 检查新文件名是否已存在
            if new_path.exists() and new_path != fpath:
                # 避免冲突，添加序号
                counter = 1
                while new_path.exists():
                    new_name_counter = f"{new_name}-{counter}"
                    new_path = RAW_COU_DIR / f"{new_name_counter}.md"
                    counter += 1

            if dry_run:
                print(f"  [DRY] {old_name}.md -> {new_path.name}")
            else:
                # 重命名文件
                shutil.move(str(fpath), str(new_path))
                print(f"  [OK] {old_name}.md -> {new_path.name}")

            renamed_count += 1

        except Exception as e:
            print(f"  [ERR] {fpath.name}: {e}")
            error_count += 1

    print()
    print(f"[*] 完成: 重命名 {renamed_count}, 跳过 {skipped_count}, 错误 {error_count}")

    if not dry_run:
        print(f"[*] 备份目录: 无 (直接重命名)")
        # 更新修改时间
        print(f"[*] 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    rename_cou_files(dry_run=dry_run)