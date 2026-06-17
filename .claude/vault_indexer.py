#!/usr/bin/env python3
"""
Obsidian Vault Backlink Indexer
扫描所有 .md 文件，提取 wikilinks、tags、outlinks，生成索引
"""

import re
import json
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

VAULT_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = VAULT_ROOT / "index（索引）"
INDEX_DIR.mkdir(exist_ok=True)

# ==================== 正则表达式 ====================

WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
# 匹配 [[link]] 和 [[link|display]] 和 [[link#heading]]

MDLINK_PATTERN = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
# 匹配 [text](url) 但排除图片

TAG_PATTERN = re.compile(r'(?:^|\s)#([a-zA-Z][a-zA-Z0-9_/-]*)')
# 匹配 #tag

FRONTMATTER_TAG_PATTERN = re.compile(r'^tags:\s*$', re.MULTILINE)
# 简单 frontmatter tags 检测

# ==================== 索引类 ====================

class VaultIndexer:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.files = {}           # path -> file_info
        self.backlinks = defaultdict(list)  # target -> list of source files
        self.outlinks = defaultdict(list)   # source -> list of targets
        self.tags = defaultdict(list)       # tag -> list of files

    def scan(self):
        """扫描 vault 中所有 .md 文件"""
        md_files = list(self.vault_root.rglob("*.md"))

        # 排除 index 目录自身
        md_files = [f for f in md_files if not str(f).startswith(str(INDEX_DIR))]

        for file_path in md_files:
            self._process_file(file_path)

    def _process_file(self, path: Path):
        """处理单个文件"""
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {path}: {e}")
            return

        rel_path = path.relative_to(self.vault_root)

        # 提取 wikilinks
        wikilinks = WIKILINK_PATTERN.findall(content)

        # 提取 markdown 外链
        mdlinks = MDLINK_PATTERN.findall(content)

        # 提取 tags
        frontmatter_tags = self._extract_frontmatter_tags(content)
        inline_tags = TAG_PATTERN.findall(content)
        all_tags = list(set(frontmatter_tags + inline_tags))

        # 提取标题（第一个 # 开头）
        title = self._extract_title(content)

        # 提取摘要（开头 200 字）
        summary = content[:200].strip().replace('\n', ' ')

        # 记录文件信息
        self.files[str(rel_path)] = {
            "title": title,
            "summary": summary,
            "tags": all_tags,
            "wikilinks": wikilinks,
            "external_links": [link for _, link in mdlinks],
            "word_count": len(content.split()),
            "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
        }

        # 建立反向链接
        for target in wikilinks:
            self.backlinks[target].append(str(rel_path))

        # 记录外链
        for title_text, url in mdlinks:
            self.outlinks[str(rel_path)].append({"type": "url", "url": url, "text": title_text})

        # 记录 tags
        for tag in all_tags:
            self.tags[tag].append(str(rel_path))

    def _extract_frontmatter_tags(self, content: str) -> list:
        """提取 frontmatter 中的 tags"""
        tags = []
        if content.startswith('---'):
            parts = content[3:].split('---', 1)
            if len(parts) >= 2:
                frontmatter = parts[0]
                # 找到 tags: 行之后的所有列表项
                in_tags = False
                for line in frontmatter.split('\n'):
                    if line.strip().startswith('tags:'):
                        in_tags = True
                        continue
                    elif in_tags and line.strip().startswith('- '):
                        tags.append(line.strip()[2:])
                    elif in_tags and line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                        # 遇到另一个顶级 key 就停止
                        break
                    elif in_tags and not line.strip():
                        continue
                    else:
                        in_tags = False
        return tags

    def _extract_title(self, content: str) -> str:
        """提取文档标题"""
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# ') and not line.startswith('## '):
                return line[2:].strip()
        return ""

    def generate_index(self):
        """生成索引文件"""

        # 1. backlinks index: 每个文件被哪些文件链接
        backlinks_index = {}
        for target, sources in self.backlinks.items():
            backlinks_index[target] = list(set(sources))

        # 2. outlinks index: 每个文件链接到哪些文件
        outlinks_index = {}
        for source, targets in self.outlinks.items():
            outlinks_index[source] = targets

        # 3. tags index
        tags_index = {tag: list(set(files)) for tag, files in self.tags.items()}

        # 4. manifest: 每个文件的简要信息
        manifest = {}
        for path, info in self.files.items():
            manifest[path] = {
                "title": info["title"],
                "summary": info["summary"][:150] + "..." if len(info["summary"]) > 150 else info["summary"],
                "tags": info["tags"],
                "word_count": info["word_count"],
                "wikilinks_count": len(info["wikilinks"]),
                "backlinks_count": len(backlinks_index.get(path, [])),
                "modified": info["modified"]
            }

        # 写入 JSON 文件
        with open(INDEX_DIR / "backlinks.json", "w", encoding="utf-8") as f:
            json.dump(backlinks_index, f, ensure_ascii=False, indent=2)

        with open(INDEX_DIR / "manifest.json", "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

        with open(INDEX_DIR / "tags.json", "w", encoding="utf-8") as f:
            json.dump(tags_index, f, ensure_ascii=False, indent=2)

        # 5. 计算每个文件的背链数（使用 wikilinks 指向的文件名匹配）
        for path, info in self.files.items():
            filename = Path(path).stem  # 文件名不含扩展名
            # 统计有多少文件的 wikilinks 指向这个文件
            info["backlinks_count"] = sum(
                1 for target, sources in backlinks_index.items()
                if target == filename or target == path or target == Path(path).name
                for _ in sources
            )

        # 重新排序热门页面
        hot = sorted(self.files.items(), key=lambda x: x[1].get('backlinks_count', 0), reverse=True)[:10]

        # 5. 生成可读的 index.md
        self._generate_index_readme(manifest, hot, tags_index)

        print(f"索引完成！")
        print(f"  - 文件数: {len(self.files)}")
        print(f"  - 有背链的文件: {len(backlinks_index)}")
        print(f"  - 标签数: {len(tags_index)}")
        print(f"  输出目录: {INDEX_DIR}")

    def _generate_index_readme(self, manifest, hot_pages, tags_index):
        """生成可读的索引概览"""

        lines = [
            "---",
            "title: Vault Index",
            f"date: {datetime.now().strftime('%Y-%m-%d')}",
            "tags: [index, vault]",
            "---",
            "",
            "# Obsidian Vault Index",
            "",
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            f"总计文件: {len(self.files)}",
            "",
            "---",
            "",
            "## 最近修改",
            ""
        ]

        # 按修改时间排序，取前 10
        recent = sorted(manifest.items(), key=lambda x: x[1]['modified'], reverse=True)[:10]
        for path, info in recent:
            lines.append(f"- [[{path}]] — {info['title'] or '无标题'} ({info['modified'][:10]})")

        lines.extend(["", "---", "", "## 标签云", ""])

        # 标签按频率排序
        sorted_tags = sorted(tags_index.items(), key=lambda x: len(x[1]), reverse=True)
        for tag, files in sorted_tags[:30]:
            lines.append(f"- #{tag} ({len(files)} 个文件)")

        lines.extend(["", "---", "", "## 热门页面（按背链数）", ""])

        # 按背链数排序（传入的 hot_pages 已排序）
        for path, info in hot_pages:
            bc = info.get('backlinks_count', 0)
            if bc > 0:
                lines.append(f"- [[{path}]] — {bc} 个背链")

        lines.extend(["", "---", "", "## 索引文件", "", "- `backlinks.json` — 反向链接索引", "- `manifest.json` — 所有文件元数据", "- `tags.json` — 标签索引", ""])

        with open(INDEX_DIR / "index.md", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


if __name__ == "__main__":
    indexer = VaultIndexer(VAULT_ROOT)
    indexer.scan()
    indexer.generate_index()
