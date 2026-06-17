#!/usr/bin/env python3
"""
政策法规库OCR处理脚本
功能：对PDF/DOC/DOCX/TXT文件进行OCR处理，转换为Markdown
支持断点续传，自动跳过已处理文件
"""

import base64
import os
import requests
import json
import time
from pathlib import Path

API_URL = "https://47h248z8e3p5o132.aistudio-app.com/layout-parsing"
TOKEN = "f4c6d1aab7dfff9492786f0d76359300587dbbfb"

SOURCE_DIR = "/root/obsidian_vault/Archive（归档）/政策法规库/政策法规库原始文档/金融行业"
OUTPUT_DIR = "/root/obsidian_vault/Archive（归档）/政策法规库/政策法规库MD文档"
PROGRESS_FILE = "/root/obsidian_vault/Archive（归档）/政策法规库/.ocr_progress.json"
LOG_FILE = "/root/obsidian_vault/Archive（归档）/政策法规库/ocr_processing.log"

# 页数限制
DAILY_LIMIT = 20000
daily_used = 0

def get_file_type(filename):
    ext = Path(filename).suffix.lower()
    if ext == '.pdf':
        return 0
    elif ext in ['.docx', '.doc']:
        return 0  # API可能不支持，但按PDF方式处理
    else:
        return 1  # 图片或其他

def call_ocr_api(file_path, file_type=0):
    """调用OCR API with retry logic"""
    with open(file_path, "rb") as file:
        file_bytes = file.read()
        file_data = base64.b64encode(file_bytes).decode("ascii")

    headers = {
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    }

    required_payload = {
        "file": file_data,
        "fileType": file_type,
    }

    optional_payload = {
        "useDocOrientationClassify": False,
        "useDocUnwarping": False,
        "useChartRecognition": False,
    }

    payload = {**required_payload, **optional_payload}

    # Retry with exponential backoff
    for attempt in range(5):
        try:
            # Create fresh session each time
            session = requests.Session()
            response = session.post(API_URL, json=payload, headers=headers, timeout=60)
            session.close()

            if response.status_code == 200:
                return response.json()["result"]
            elif response.status_code == 429:
                print(f"  API限流，等待60秒...")
                time.sleep(60)
                continue
            elif response.status_code == 400:
                raise Exception(f"API返回错误: 400 - {response.text[:100]}")
            else:
                print(f"  API错误 {response.status_code}，重试...")
                time.sleep(30 * (attempt + 1))
                continue
        except requests.exceptions.ConnectionError as e:
            print(f"  连接错误，重试 ({attempt+1}/5)...")
            time.sleep(30 * (attempt + 1))
        except requests.exceptions.Timeout:
            print(f"  超时，重试 ({attempt+1}/5)...")
            time.sleep(30 * (attempt + 1))
        except Exception as e:
            print(f"  错误: {e}，重试 ({attempt+1}/5)...")
            time.sleep(30 * (attempt + 1))

    return None

def get_output_filename(source_file):
    """根据源文件名生成输出markdown文件名"""
    basename = Path(source_file).stem
    # 清理文件名中的非法字符
    basename = basename.replace('/', '-').replace('\\', '-').replace(':', '-')
    return basename + ".md"

def sanitize_path(path_str):
    """清理路径字符串"""
    return path_str.replace('/', '-').replace('\\', '-').replace(':', '-')

def process_file(source_file, file_type=0):
    """处理单个文件"""
    global daily_used

    result = call_ocr_api(source_file, file_type)

    if result is None:
        return False, "API限流"

    # 计算页数（基于layoutParsingResults数量）
    page_count = len(result.get("layoutParsingResults", []))

    output_filename = get_output_filename(source_file)
    output_path = Path(OUTPUT_DIR) / output_filename

    # 合并所有页面的markdown
    combined_md = []
    for i, res in enumerate(result.get("layoutParsingResults", [])):
        md_text = res.get("markdown", {}).get("text", "")
        combined_md.append(md_text)

        # 保存图片（如果有）- 失败不影响主流程
        images = res.get("markdown", {}).get("images", {})
        for img_path, img_url in images.items():
            try:
                img_base = sanitize_path(output_filename.replace(".md", ""))
                img_dir = Path(OUTPUT_DIR) / "images" / img_base
                img_dir.mkdir(parents=True, exist_ok=True)
                img_full_path = img_dir / Path(img_path).name
                img_response = requests.get(img_url, timeout=30)
                if img_response.status_code == 200:
                    with open(img_full_path, "wb") as f:
                        f.write(img_response.content)
            except Exception as e:
                print(f"  图片保存跳过: {e}")

    # 写入合并后的markdown
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(combined_md))

    daily_used += page_count
    return True, f"成功 ({page_count}页)"

def load_progress():
    """加载处理进度"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"processed": [], "failed": [], "daily_used": 0}

def save_progress(progress):
    """保存处理进度"""
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def get_all_files():
    """获取所有待处理文件"""
    files = []
    source_path = Path(SOURCE_DIR)
    for ext in ['*.pdf', '*.docx', '*.doc', '*.txt']:
        files.extend(source_path.rglob(ext))
    return sorted(files)

def main():
    global daily_used

    print("=" * 60)
    print("政策法规库OCR处理脚本")
    print("=" * 60)

    progress = load_progress()
    daily_used = progress.get("daily_used", 0)
    processed = set(progress.get("processed", []))
    failed = set(progress.get("failed", []))

    print(f"已处理: {len(processed)} 个文件")
    print(f"今日已使用页数: {daily_used}/{DAILY_LIMIT}")

    if daily_used >= DAILY_LIMIT:
        print("已达到每日页数限额，请明天再处理")
        return

    files = get_all_files()
    print(f"待处理文件总数: {len(files)}")

    # 过滤未处理的文件
    unprocessed = [f for f in files if str(f) not in processed and str(f) not in failed]
    print(f"本次待处理: {len(unprocessed)} 个文件")

    success_count = 0
    fail_count = 0
    skip_count = len(files) - len(unprocessed)

    for i, file_path in enumerate(unprocessed):
        rel_path = str(file_path)
        print(f"\n[{i+1}/{len(unprocessed)}] 处理: {rel_path}")

        if daily_used >= DAILY_LIMIT:
            print("已达每日限额，保存进度后退出")
            progress["daily_used"] = daily_used
            save_progress(progress)
            break

        try:
            # 确定文件类型
            file_type = 0  # PDF
            success = False
            msg = ""
            if file_path.suffix.lower() in ['.docx', '.doc']:
                # DOC/DOCX作为文档处理
                file_type = 0
                success, msg = process_file(file_path, file_type)
            elif file_path.suffix.lower() == '.txt':
                # TXT直接读取内容
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                output_filename = get_output_filename(file_path)
                output_path = Path(OUTPUT_DIR) / output_filename
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                success = True
                msg = "成功 (TXT直读)"
            else:
                success, msg = process_file(file_path, file_type)

            if success:
                print(f"  结果: {msg}")
                processed.add(rel_path)
                success_count += 1
            else:
                print(f"  结果: {msg} - 暂停处理")
                failed.add(rel_path)
                fail_count += 1
                break

        except Exception as e:
            print(f"  错误: {str(e)}")
            failed.add(rel_path)
            fail_count += 1

        # 每处理5个文件保存一次进度
        if (i + 1) % 5 == 0:
            progress["processed"] = list(processed)
            progress["failed"] = list(failed)
            progress["daily_used"] = daily_used
            save_progress(progress)
            print(f"  [进度已保存]")

    # 最终保存
    progress["processed"] = list(processed)
    progress["failed"] = list(failed)
    progress["daily_used"] = daily_used
    save_progress(progress)

    print("\n" + "=" * 60)
    print(f"处理完成！")
    print(f"  成功: {success_count}")
    print(f"  失败: {fail_count}")
    print(f"  跳过: {skip_count} (已处理)")
    print(f"  今日已用页数: {daily_used}/{DAILY_LIMIT}")
    print("=" * 60)

if __name__ == "__main__":
    main()
