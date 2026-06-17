#!/usr/bin/env python3
"""
MarkItDown Converter Skill
将各种文件格式转换为 Markdown
支持: PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, 图片, 音频, EPUB, ZIP, YouTube
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

try:
    from markitdown import MarkItDown
except ImportError:
    print("Error: markitdown not installed. Run: pip install 'markitdown[all]'")
    sys.exit(1)

VAULT_ROOT = Path(__file__).resolve().parent.parent
WIKI_SUMMARY_DIR = VAULT_ROOT / "Wiki（维基）" / "Summary（摘要）"
WIKI_TRANSLATION_DIR = VAULT_ROOT / "Wiki（维基）" / "Translation（翻译）"

def convert_file(input_path: str, output_path: str = None, enable_plugins: bool = False) -> tuple[str, str]:
    """
    转换文件为 Markdown

    Args:
        input_path: 输入文件路径
        output_path: 输出文件路径（可选）
        enable_plugins: 是否启用插件

    Returns:
        (markdown_content, output_file_path)
    """
    md = MarkItDown(enable_plugins=enable_plugins)
    result = md.convert(input_path)
    content = result.text_content

    # 确定输出路径
    if output_path:
        out_path = Path(output_path)
    else:
        # 自动生成输出路径
        input_name = Path(input_path).stem
        timestamp = datetime.now().strftime("%Y%m%d")
        out_path = WIKI_SUMMARY_DIR / f"{input_name}_{timestamp}.md"

    # 确保输出目录存在
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # 写入文件
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    return content, str(out_path)

def get_supported_formats():
    """返回支持的格式列表"""
    return [
        ("文档", "PDF, DOCX, PPTX, XLSX, XLS, EPUB"),
        ("网页", "HTML"),
        ("数据", "CSV, JSON, XML"),
        ("媒体", "图片 (EXIF + OCR), 音频 (EXIF + 转录)"),
        ("其他", "ZIP 文件, YouTube URL"),
    ]

def main():
    parser = argparse.ArgumentParser(
        description="MarkItDown Converter - 将各种文件转换为 Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s document.pdf                    # 转换为 Markdown 并保存
  %(prog)s document.pdf -o output.md       # 指定输出文件
  %(prog)s document.pdf -p                 # 启用插件（LLM 图像描述等）
  %(prog)s --list-formats                  # 列出支持的格式
        """
    )
    parser.add_argument("input", nargs="?", help="输入文件路径或 URL")
    parser.add_argument("-o", "--output", help="输出 Markdown 文件路径")
    parser.add_argument("-p", "--plugins", action="store_true",
                        help="启用插件（用于图像描述等高级功能）")
    parser.add_argument("--list-formats", action="store_true",
                        help="列出所有支持的格式")

    args = parser.parse_args()

    if args.list_formats:
        print("MarkItDown 支持的文件格式:\n")
        for category, formats in get_supported_formats():
            print(f"  {category}: {formats}")
        return

    if not args.input:
        parser.print_help()
        return

    try:
        content, output_path = convert_file(
            args.input,
            args.output,
            args.plugins
        )
        print(f"✓ 转换成功: {output_path}")
        print(f"✓ 字数: {len(content)} 字符")
    except FileNotFoundError:
        print(f"Error: 文件不存在: {args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: 转换失败 - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
