#!/usr/bin/env python3
"""
Policy Archive OCR Processor
Uses PaddleOCR-VL-1.5 API to convert documents to Markdown
Daily limit: 20000 pages

Memory optimization: process in batches with rest periods
"""

import base64
import gc
import os
import json
import time
import requests
from pathlib import Path
from datetime import datetime

API_URL = "https://47h248z8e3p5o132.aistudio-app.com/layout-parsing"
TOKEN = "f4c6d1aab7dfff9492786f0d76359300587dbbfb"

BASE_DIR = "/root/obsidian_vault/Archive（归档）/PolicyArchive（政策法规库）"
ORIGINAL_DIR = f"{BASE_DIR}/Original Documents（原始文档）"
OUTPUT_DIR = f"{BASE_DIR}/MD Documents（MD文档）"
PROCESS_LOG = f"{BASE_DIR}/.ocr_process_log.json"
DAILY_LIMIT = 20000

# Memory optimization settings
BATCH_SIZE = 3           # Process N files before rest
REST_SECONDS = 60        # Rest period between batches
MEMORY_WARNING = 800      # MB, warn if available memory below this

def check_memory():
    """Check available memory, return True if healthy"""
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                if line.startswith('MemAvailable:'):
                    available_kb = int(line.split()[1])
                    available_mb = available_kb // 1024
                    return available_mb >= MEMORY_WARNING
    except:
        pass
    return True

def gc_collect():
    """Force garbage collection"""
    gc.collect()
    print("    [GC: Memory cleaned]")

def memory_saver():
    """Extra aggressive memory cleanup"""
    import sys
    # Clear any cached module attributes
    modules_to_clear = ['json', 'base64']
    for mod in modules_to_clear:
        if mod in sys.modules:
            # Don't clear, just hint GC
            pass
    gc.collect()
    gc.collect()  # Double collect for thorough cleanup
    print("    [GC: Extra memory cleanup done]")

def load_process_log():
    """Load processing log for resume support"""
    if os.path.exists(PROCESS_LOG):
        with open(PROCESS_LOG, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'processed': [], 'total_pages': 0, 'date': str(datetime.now().date())}

def save_process_log(log):
    """Save processing log"""
    with open(PROCESS_LOG, 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

def load_file_list():
    """Load file list to process"""
    list_file = f"{BASE_DIR}/files_to_process.json"
    if os.path.exists(list_file):
        with open(list_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def get_file_type(ext):
    """Map file extension to API fileType parameter"""
    # PDF: 0, Image/DOCX: 1
    # Note: .doc files are NOT supported by the API
    if ext == '.pdf':
        return 0
    elif ext in ['.docx', '.pptx', '.xlsx', '.png', '.jpg', '.jpeg', '.tif', '.tiff']:
        return 1
    else:
        return -1  # Unsupported format

def process_file(filepath, relpath, ext, retry=3, timeout=180):
    """Process a single file and return markdown content"""
    for attempt in range(retry):
        try:
            with open(filepath, "rb") as file:
                file_bytes = file.read()
                file_data = base64.b64encode(file_bytes).decode("ascii")

            headers = {
                "Authorization": f"token {TOKEN}",
                "Content-Type": "application/json"
            }

            required_payload = {
                "file": file_data,
                "fileType": get_file_type(ext)
            }

            optional_payload = {
                "useDocOrientationClassify": False,
                "useDocUnwarping": False,
                "useChartRecognition": False,
            }

            payload = {**required_payload, **optional_payload}

            response = requests.post(API_URL, json=payload, headers=headers, timeout=timeout)

            if response.status_code == 503:
                # Queue full, wait and retry - but cap total wait time
                print(f"  Queue full (503), waiting 90s...")
                time.sleep(90)
                continue

            if response.status_code != 200:
                print(f"  API error: {response.status_code}, attempt {attempt+1}/{retry}")
                if attempt < retry - 1:
                    time.sleep(10 * (attempt + 1))
                continue

            result = response.json()["result"]
            pages = len(result["layoutParsingResults"])

            # Combine all pages into one markdown
            md_content = []
            for i, res in enumerate(result["layoutParsingResults"]):
                md_content.append(res["markdown"]["text"])

            return "\n\n---\n\n".join(md_content), pages

        except requests.exceptions.Timeout:
            print(f"  Timeout, attempt {attempt+1}/{retry}")
            if attempt < retry - 1:
                time.sleep(60)
        except requests.exceptions.ConnectionError as e:
            err_str = str(e)
            if 'Connection refused' in err_str or 'Connection reset' in err_str:
                print(f"  Connection error, waiting 90s...")
                time.sleep(90)
            else:
                print(f"  Connection error: {e}, attempt {attempt+1}/{retry}")
                if attempt < retry - 1:
                    time.sleep(30)
        except Exception as e:
            err_str = str(e)
            if 'SSL' in err_str or 'SSLError' in err_str:
                print(f"  SSL error, waiting 45s...")
                time.sleep(45)
            else:
                print(f"  Error: {e}, attempt {attempt+1}/{retry}")
                if attempt < retry - 1:
                    time.sleep(20)

    return None, 0

def sanitize_filename(filename):
    """Sanitize filename for cross-platform compatibility"""
    # Remove/replace problematic characters
    replacements = {
        '<': '＜',
        '>': '＞',
        ':': '：',
        '"': '"',
        '/': '／',
        '\\': '＼',
        '|': '｜',
        '?': '？',
        '*': '＊'
    }
    for old, new in replacements.items():
        filename = filename.replace(old, new)
    return filename

def main():
    print("=" * 60)
    print("Policy Archive OCR Processor")
    print("=" * 60)

    # Check daily limit reset
    today = str(datetime.now().date())
    log = load_process_log()

    # Initialize log if starting fresh
    if not log.get('processed'):
        log = {'processed': [], 'total_pages': 0, 'date': today}
        save_process_log(log)
        print(f"Initialized new log for {today}")

    if log.get('date') != today:
        print(f"New day detected, resetting counter (was {log.get('total_pages', 0)} pages)")
        log = {'processed': [], 'total_pages': 0, 'date': today}

    files = load_file_list()
    print(f"Total files to process: {len(files)}")
    print(f"Pages processed today: {log.get('total_pages', 0)} / {DAILY_LIMIT}")
    print()

    # Filter out already processed files
    processed_set = set(log.get('processed', []))

    # Also check if MD output already exists (for resume after crash)
    def md_exists(file_info):
        md_filename = sanitize_filename(os.path.splitext(file_info['name'])[0]) + '.md'
        output_path = os.path.join(OUTPUT_DIR, md_filename)
        if os.path.exists(output_path):
            return True
        # Also check for _N suffix versions
        for n in range(1, 100):
            if os.path.exists(os.path.join(OUTPUT_DIR, f"{os.path.splitext(md_filename)[0]}_{n}.md")):
                return True
        return False

    remaining_files = [f for f in files if f['relpath'] not in processed_set and not md_exists(f)]
    print(f"Remaining files: {len(remaining_files)} (after dedup)")

    if not remaining_files:
        print("All files already processed!")
        return

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success_count = 0
    error_count = 0
    skip_count = 0
    batch_count = 0

    for i, file_info in enumerate(remaining_files):
        relpath = file_info['relpath']
        filepath = file_info['path']
        ext = file_info['ext']

        # Check daily limit
        if log.get('total_pages', 0) >= DAILY_LIMIT:
            print(f"\n⚠️  Daily limit reached ({DAILY_LIMIT} pages)")
            print(f"Processed {success_count} files today")
            print(f"Run again tomorrow to continue, or manually process remaining files")
            save_process_log(log)
            break

        # Progress indicator
        if (i + 1) % 10 == 0 or log.get('total_pages', 0) % 1000 == 0:
            print(f"\n[{i+1}/{len(remaining_files)}] Processing: {relpath[:50]}...")
            print(f"    Pages today: {log.get('total_pages', 0)} / {DAILY_LIMIT}")

        # Memory check before processing
        if not check_memory():
            print(f"\n⚠️  Low memory detected, resting 90s...")
            memory_saver()
            time.sleep(90)

        # Skip if file doesn't exist
        if not os.path.exists(filepath):
            print(f"  ⚠️ File not found, skipping")
            skip_count += 1
            continue

        # Skip unsupported file types (.doc files are not supported)
        file_type = get_file_type(ext)
        if file_type == -1:
            print(f"  ⚠️ Unsupported format {ext}, skipping")
            skip_count += 1
            continue

        # Process file
        md_content, pages = process_file(filepath, relpath, ext)

        if md_content is None:
            error_count += 1
            continue

        # Save markdown file
        # Use original filename with .md extension
        md_filename = sanitize_filename(os.path.splitext(file_info['name'])[0]) + '.md'
        output_path = os.path.join(OUTPUT_DIR, md_filename)

        # Handle duplicate filenames
        counter = 1
        base_name = md_filename
        while os.path.exists(output_path):
            md_filename = f"{os.path.splitext(base_name)[0]}_{counter}.md"
            output_path = os.path.join(OUTPUT_DIR, md_filename)
            counter += 1

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            f.write(f"title: \"{os.path.splitext(file_info['name'])[0]}\"\n")
            f.write(f"source: \"{relpath}\"\n")
            f.write(f"type: \"{ext[1:]}\"\n")
            f.write(f"processed: \"{datetime.now().isoformat()}\"\n")
            f.write(f"---\n\n")
            f.write(md_content)

        # Clear md_content immediately to free memory
        del md_content

        # Update log
        log['processed'].append(relpath)
        log['total_pages'] = log.get('total_pages', 0) + pages
        success_count += 1
        batch_count += 1

        # Batch processing with rest and GC
        if batch_count >= BATCH_SIZE:
            print(f"    [Batch {batch_count} complete, resting {REST_SECONDS}s...]")
            memory_saver()
            time.sleep(REST_SECONDS)
            batch_count = 0

        # Save log after each file
        save_process_log(log)

    # Final save
    save_process_log(log)

    print()
    print("=" * 60)
    print("Processing complete!")
    print(f"  Success: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Total pages today: {log.get('total_pages', 0)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
