#!/usr/bin/env python3
"""
Batch Word to Markdown Converter
批量将 Word 文件（.doc/.docx）转换为 Markdown，原文件保留
"""

import os
import sys
from pathlib import Path
from datetime import datetime

try:
    from markitdown import MarkItDown
except ImportError:
    print("Error: markitdown not installed. Run: pip install 'markitdown[all]'")
    sys.exit(1)

def batch_convert(input_dir: str, output_dir: str, extensions=(".doc", ".docx")):
    """
    批量转换 Word 文件为 Markdown

    Args:
        input_dir: 输入目录
        output_dir: 输出目录
        extensions: 要转换的文件扩展名
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    md = MarkItDown(enable_plugins=False)

    # 获取所有 Word 文件
    word_files = []
    for ext in extensions:
        word_files.extend(input_path.glob(f"*{ext}"))

    word_files = sorted(word_files)
    total = len(word_files)
    success = 0
    failed = []

    print(f"找到 {total} 个 Word 文件，开始转换...\n")

    for i, word_file in enumerate(word_files, 1):
        try:
            # 转换
            result = md.convert(str(word_file))
            content = result.text_content

            # 生成输出文件名
            stem = word_file.stem  # 去掉扩展名
            timestamp = datetime.now().strftime("%Y%m%d")
            out_file = output_path / f"{stem}.md"

            # 写入文件
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(content)

            success += 1
            print(f"[{i}/{total}] ✓ {word_file.name}")

        except Exception as e:
            failed.append((word_file.name, str(e)))
            print(f"[{i}/{total}] ✗ {word_file.name} - {e}")

    # 汇总
    print(f"\n{'='*50}")
    print(f"转换完成: {success}/{total} 成功")
    if failed:
        print(f"失败 {len(failed)} 个:")
        for name, err in failed:
            print(f"  - {name}: {err}")

    return success, failed

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 batch_word_converter.py <输入目录> <输出目录>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    batch_convert(input_dir, output_dir)
