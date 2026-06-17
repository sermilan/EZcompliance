#!/usr/bin/env python3
"""
Dead Link Checker — scans vault for broken wikilinks.
Skips: code blocks, Notion（Notion 同步）/ (read-only), .md extension links that resolve.
"""

import os, re, sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent
os.chdir(VAULT_ROOT)

# Build target set (all .md files + image files in Images/)
md_targets = set()
image_targets = set()
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        fp = (Path(root) / f)
        rel = str(fp)
        if f.endswith('.md'):
            md_targets.add(str(fp.with_suffix('')))
            md_targets.add(fp.stem)
        if 'Images（图片）' in rel or 'Images' in rel:
            image_targets.add(rel)
            image_targets.add(str(fp.with_suffix('')))

def is_in_code(pos, text):
    """Check if position is inside a fenced code block or inline code span."""
    before = text[:pos]
    # Fenced code block
    if before.count('```') % 2 == 1:
        return True
    # Inline code: check if there's an unclosed backtick on the same line before this position
    line_start = before.rfind('\n')
    if line_start == -1:
        line_start = 0
    line_before = before[line_start:pos]
    # Count single backticks (not part of double/triple)
    # Simple: count ` occurrences and check oddness
    bt_count = line_before.count('`')
    return bt_count % 2 == 1

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[#|][^\]]+)?\]\]')

dead = defaultdict(list)
total_links = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if not f.endswith('.md'):
            continue
        fp = Path(root) / f
        rel = str(fp)
        # Skip Notion (read-only)
        if rel.startswith('Notion（Notion 同步）') or rel.startswith('./Notion（Notion 同步）'):
            continue
        try:
            with open(fp, 'r') as fh:
                text = fh.read()
        except:
            continue
        for m in WIKILINK_RE.finditer(text):
            total_links += 1
            link = m.group(1).strip()
            if '://' in link or link.startswith('http'):
                continue
            if is_in_code(m.start(), text):
                continue
            # Resolve
            if link in md_targets:
                continue
            if link.endswith('.md') and link[:-3] in md_targets:
                continue
            if link in image_targets:
                continue
            # Try stripping .png/.jpg (Obsidian resolves these)
            if link.endswith('.png') or link.endswith('.jpg') or link.endswith('.jpeg') or link.endswith('.webp'):
                bare = str(Path(link).with_suffix(''))
                if bare in image_targets:
                    continue
            dead[rel].append(link)

dead_count = sum(len(v) for v in dead.values())
print(f"Total wikilinks scanned: {total_links}")
print(f"Dead links found: {dead_count} in {len(dead)} files")
print()

# Group by category
cats = defaultdict(list)
for src, links in dead.items():
    top = src.split('/')[0] if '/' in src else '(root)'
    for l in links:
        cats[top].append((src, l))

for cat in sorted(cats):
    items = cats[cat]
    print(f"### {cat} ({len(items)} dead links) ###")
    for src, dst in items[:8]:
        print(f"  [{src}] -> [[{dst}]]")
    if len(items) > 8:
        print(f"  ... and {len(items)-8} more")
    print()

# Exit code: 0 if clean, 1 if dead links found
sys.exit(0 if dead_count == 0 else 1)
