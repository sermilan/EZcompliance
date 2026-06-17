#!/usr/bin/env python3
"""
Batch PDF to Markdown converter using PaddleOCR-VL API
"""

import base64
import os
import requests
import json
import re
from pathlib import Path
from datetime import datetime

API_URL = "https://47h248z8e3p5o132.aistudio-app.com/layout-parsing"
TOKEN = "f4c6d1aab7dfff9492786f0d76359300587dbbfb"

SOURCE_DIR = "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）/新建文件夹"
TARGET_DIR = "/root/obsidian_vault/Wiki（维基）/Reference（参考）/PolicyArchive（政策法规库）/新建文件夹"
PROGRESS_FILE = "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）/.conversion_progress.json"

def ocr_convert(file_path, file_type=0):
    """Convert PDF to markdown using PaddleOCR-VL API"""
    with open(file_path, "rb") as f:
        file_data = base64.b64encode(f.read()).decode("ascii")

    payload = {
        "file": file_data,
        "fileType": file_type,
        "useDocOrientationClassify": False,
        "useDocUnwarping": False,
        "useChartRecognition": False
    }

    response = requests.post(API_URL, json=payload, headers={
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    }, timeout=120)

    if response.status_code == 429 or "rate limit" in response.text.lower():
        return {"status": "rate_limited", "text": "", "remaining": 0}

    result = response.json()["result"]
    markdown_text = result["layoutParsingResults"][0]["markdown"]["text"]
    return {"status": "success", "text": markdown_text}

def extract_date_from_filename(filename):
    """Try to extract date from filename like 'xxx2020.4.13.pdf' or 'xxx202401.pdf'"""
    patterns = [
        r'(\d{4})\.(\d{1,2})\.(\d{1,2})',  # 2020.4.13
        r'(\d{4})(\d{2})',                  # 202401
        r'(\d{4})-(\d{2})-(\d{2})',         # 2024-01-01
    ]
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            if len(match.groups()) == 3:
                return f"{match.group(1)}-{match.group(2).zfill(2)}-{match.group(3).zfill(2)}"
            elif len(match.groups()) == 2:
                return f"{match.group(1)}-{match.group(2)}-01"
    return datetime.now().strftime("%Y-%m-%d")

def sanitize_filename(name):
    """Remove special characters from filename"""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.replace(' ', '-')
    if len(name) > 50:
        name = name[:50]
    return name

def create_frontmatter(title, date, source_file):
    """Create YAML frontmatter for the markdown file"""
    return f'''---
title: "{title}"
date: {date}
source: "{source_file}"
converted: {datetime.now().strftime("%Y-%m-%d")}
---

'''

def load_progress():
    """Load conversion progress"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Handle old format with "processed" as int
            if isinstance(data.get("processed"), int):
                return {"processed": [], "failed": [], "api_calls": 0}
            return data
    return {"processed": [], "failed": [], "api_calls": 0}

def save_progress(progress):
    """Save conversion progress"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def get_target_md_path(pdf_path):
    """Get corresponding md file path for a PDF file"""
    filename = os.path.basename(pdf_path)
    md_name = sanitize_filename(os.path.splitext(filename)[0]) + ".md"
    return os.path.join(TARGET_DIR, md_name)

def main():
    # Create target directory
    os.makedirs(TARGET_DIR, exist_ok=True)

    # Load progress
    progress = load_progress()
    processed_set = set(progress["processed"])
    failed_set = set(progress["failed"])

    # Get all PDF files
    pdf_files = list(Path(SOURCE_DIR).glob("*.pdf"))
    total = len(pdf_files)

    print(f"Total PDF files found: {total}")
    print(f"Already processed: {len(processed_set)}")
    print(f"Previously failed: {len(failed_set)}")

    success_count = 0
    skip_count = 0
    fail_count = 0
    rate_limited = False

    for i, pdf_path in enumerate(pdf_files):
        pdf_str = str(pdf_path)
        target_md = get_target_md_path(pdf_str)

        # Check if already converted
        if os.path.exists(target_md):
            print(f"[{i+1}/{total}] SKIP (already exists): {os.path.basename(pdf_path)}")
            skip_count += 1
            continue

        if pdf_str in failed_set:
            print(f"[{i+1}/{total}] SKIP (previously failed): {os.path.basename(pdf_path)}")
            skip_count += 1
            continue

        print(f"[{i+1}/{total}] Converting: {os.path.basename(pdf_path)}")

        try:
            result = ocr_convert(pdf_str)

            if result["status"] == "rate_limited":
                print(f"[STOPPED] API rate limit reached at file {i+1}")
                rate_limited = True
                break

            # Extract title from filename
            title = os.path.splitext(os.path.basename(pdf_str))[0]
            date = extract_date_from_filename(os.path.basename(pdf_str))

            # Create markdown with frontmatter
            markdown_content = create_frontmatter(title, date, os.path.basename(pdf_str))
            markdown_content += result["text"]

            # Save markdown file
            with open(target_md, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            progress["processed"].append(pdf_str)
            progress["api_calls"] += 1
            success_count += 1
            print(f"  -> Saved: {os.path.basename(target_md)}")

        except Exception as e:
            progress["failed"].append(pdf_str)
            fail_count += 1
            print(f"  -> ERROR: {str(e)}")

        # Save progress after each file
        save_progress(progress)

    print("\n" + "="*50)
    print(f"Conversion Summary:")
    print(f"  Total PDF files: {total}")
    print(f"  Successfully converted: {success_count}")
    print(f"  Skipped (already exists): {skip_count}")
    print(f"  Failed: {fail_count}")
    if rate_limited:
        print(f"  Stopped: Rate limit reached")
    print(f"  API calls made: {progress['api_calls']}")
    print("="*50)

    return rate_limited, fail_count

if __name__ == "__main__":
    main()