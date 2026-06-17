#!/usr/bin/env python3
"""
Backlink Suggester
读取一篇文章，分析其内容，从 vault 索引中找出可关联的已有页面，
生成背链建议列表。
"""

import json
import sys
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = VAULT_ROOT / "index（索引）"

# 加载索引
def load_indexes():
    with open(INDEX_DIR / "manifest.json", encoding="utf-8") as f:
        manifest = json.load(f)
    with open(INDEX_DIR / "backlinks.json", encoding="utf-8") as f:
        backlinks = json.load(f)
    with open(INDEX_DIR / "tags.json", encoding="utf-8") as f:
        tags = json.load(f)
    return manifest, backlinks, tags

# 加载文章内容
def read_article(file_path: str) -> str:
    path = VAULT_ROOT / file_path
    return path.read_text(encoding="utf-8")

# 提取引用文本块（用于背链描述）
def extract_quote(content: str, keyword: str, context_chars: int = 150) -> str:
    """找到包含关键词的句子作为引用"""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if keyword.lower() in line.lower() and len(line.strip()) > 20:
            return line.strip()[:context_chars]
    return content[:context_chars] + "..."

# 构建反向标签索引（tag -> 文件列表）
def build_tag_to_files(tags_index):
    tag_files = defaultdict(list)
    for tag, files in tags_index.items():
        for f in files:
            tag_files[tag].append(f)
    return tag_files

def main():
    if len(sys.argv) < 2:
        print("用法: python3 backlink_suggester.py <文章路径>")
        print("示例: python3 backlink_suggester.py 'Research Inbox/EpochX_论文翻译.md'")
        sys.exit(1)

    article_path = sys.argv[1]
    print(f"\n=== Backlink 分析 ===")
    print(f"文章: {article_path}\n")

    # 加载索引
    manifest, backlinks_index, tags_index = load_indexes()
    article_info = manifest.get(article_path)

    if not article_info:
        print(f"错误: 未在索引中找到 '{article_path}'")
        print(f"提示: 先运行 vault_indexer.py 更新索引")
        sys.exit(1)

    print(f"标题: {article_info['title']}")
    print(f"字数: {article_info['word_count']}")
    print(f"现有背链: {article_info['backlinks_count']}")
    print(f"现有标签: {article_info['tags']}\n")

    # 读取文章完整内容用于分析
    content = read_article(article_path)

    # 统计文章中出现的词频（排除停用词）
    stopwords = {'的', '是', '在', '和', '了', '有', '我', '你', '他', '她', '它', '们',
                 '这', '那', '个', '不', '与', '也', '都', '可以', '进行', '通过', '使用',
                 '一个', '进行', '已经', '能够', '需要', '可能', '如果', '因为', '所以',
                 '但是', '而且', '或者', '以及', '对于', '关于', '这个', '那个', '什么',
                 '如何', '怎么', '为什么', '哪些', '哪些', '哪', '还', '被', '把', '将'}

    # 简单分词（按中文/英文词边界）
    words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z][a-zA-Z0-9_-]*', content.lower())
    word_freq = defaultdict(int)
    for w in words:
        if w not in stopwords and len(w) > 1:
            word_freq[w] += 1

    # 取高频词作为概念
    top_concepts = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]
    print("--- 文章高频概念 ---")
    for word, freq in top_concepts:
        print(f"  {word}: {freq}")
    print()

    # 找相似标签的文件
    article_tags = set(article_info.get('tags', []))
    tag_files = build_tag_to_files(tags_index)

    suggestions = []

    # 1. 基于标签推荐
    if article_tags:
        print("--- 标签匹配推荐 ---")
        for tag in article_tags:
            related = tag_files.get(tag, [])
            for f in related:
                if f != article_path:
                    info = manifest.get(f, {})
                    suggestions.append({
                        "file": f,
                        "title": info.get('title', f),
                        "reason": f"标签匹配: #{tag}",
                        "match_type": "tag"
                    })
                    print(f"  [[{f}]] (#{tag})")

    # 2. 基于已有背链的来源文件（可能是相关主题）
    print("\n--- 已有链接来源推荐 ---")
    article_backlink_sources = []
    for target, sources in backlinks_index.items():
        if any(article_path in s or Path(article_path).stem in s for s in sources):
            article_backlink_sources.extend(sources)

    for f in set(article_backlink_sources):
        if f != article_path:
            info = manifest.get(f, {})
            suggestions.append({
                "file": f,
                "title": info.get('title', f),
                "reason": "已有 wikilink 关联",
                "match_type": "existing_link"
            })
            print(f"  [[{f}]]")

    # 3. 基于高频概念匹配标题
    print("\n--- 概念匹配推荐 ---")
    concept_keywords = [w for w, _ in top_concepts[:10]]

    for file_path, info in manifest.items():
        if file_path == article_path:
            continue

        title = info.get('title', '')
        file_tags = info.get('tags', [])

        # 标题中包含高频概念
        matched_concepts = [kw for kw in concept_keywords
                           if kw.lower() in title.lower() or
                              kw.lower() in info.get('summary', '').lower()]

        if matched_concepts:
            suggestions.append({
                "file": file_path,
                "title": title,
                "reason": f"概念匹配: {', '.join(matched_concepts[:3])}",
                "match_type": "concept",
                "concepts": matched_concepts
            })
            print(f"  [[{file_path}]] ({', '.join(matched_concepts[:3])})")

    # 去重
    seen = set()
    unique_suggestions = []
    for s in suggestions:
        if s['file'] not in seen:
            seen.add(s['file'])
            unique_suggestions.append(s)

    # 输出汇总
    print(f"\n=== 背链建议汇总 ===")
    print(f"共找到 {len(unique_suggestions)} 个推荐关联页面\n")

    # 生成 Obsidian 格式的输出
    output_lines = [
        f"# {article_info['title']} — 背链建议",
        "",
        f"来源: [[{article_path}]]",
        f"生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        f"## 推荐关联 ({len(unique_suggestions)} 条)",
        ""
    ]

    for i, s in enumerate(unique_suggestions[:15], 1):
        output_lines.append(f"### {i}. [[{s['file']}]]")
        output_lines.append(f"- **推荐理由**: {s['reason']}")
        output_lines.append(f"- **文件标题**: {s['title']}")
        output_lines.append("")

    output_lines.extend([
        "---",
        "",
        "## 可添加到源文件的 wikilink",
        "",
        "```",
        f"# 在 {article_path} 末尾添加以下背链:",
        ""
    ])

    for s in unique_suggestions[:15]:
        # 生成合适的 wikilink 格式
        display = s['title'] if s['title'] else Path(s['file']).stem
        output_lines.append(f"# [[{s['file']}|{display}]]  # {s['reason']}")

    output_lines.append("```")

    output = "\n".join(output_lines)
    print(output)

    # 保存结果
    safe_name = Path(article_path).stem.replace(' ', '_')
    output_file = INDEX_DIR / f"backlink_suggestions_{safe_name}.md"
    output_file.write_text(output, encoding='utf-8')
    print(f"\n已保存到: {output_file}")


if __name__ == "__main__":
    main()
