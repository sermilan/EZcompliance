---
name: markdown-to-wechat-html
description: >-
  动态读取 Markdown 文章的语境与情感主题，自适应推导出一套独一无二的专属排版设计系统，并最终输出完全带有内联 CSS 样式的 HTML 文件，供直接全选复制到微信公众号编辑器中。
---

# 微信公众号排版自适应生成技能 (markdown-to-wechat-html)

## Overview
本技能用于指导 Agent 自动将 Markdown 格式的技术文章、行业分析或散文，无缝转化为带有精致内联 CSS 排版的 HTML 文件。
其核心在于**完全开放的审美推导机制**：Agent 会根据文章的语境、题材与情感调性，自主生成一套配色素雅且排版考究的专属视觉系统，并将该系统以内联属性形式注入 HTML 标签中，实现每一篇文章都量身定制的视觉质感。

## Dependencies
None.（纯指令型技能，无需调用外部物理计算依赖。）

## Quick Start

### 典型运行示例
**输入：**
1. 目标 Markdown 文本。
2. （可选）用户额外指定的主观调性词汇，如“复古暗绿”、“莫兰迪色系”、“赛博朋克霓虹风”。

**Agent 接收指令后的心智流程：**
1. **分析语境**：分析文章属于“AI 科技”方向，调性属于“理性、前沿、冷峻”。
2. **构建设计系统**：
   * 主色调：`#2563eb`（科技蓝）
   * 辅助色：`#10b981`（翡翠绿）
   * 背景色：`#f8fafc`（冷灰）
   * 圆角大小：`6px`
   * 行高：`1.8`，字间距：`0.05em`
3. **输出转换**：将文章内容包裹在 HTML 标签中，注入对应设计参数的内联 `style="..."`，输出 `.html` 文件。

---

## Workflow

当用户要求您使用此技能转换文章时，请严格按以下四步工作流执行：

### 1. 题材与情感剖析 (Aesthetic Profiling)
在转换前，首先通读 Markdown 全文，诊断其文风并生成专属的设计系统参数。
*   **文风类别诊断**：判断文章是科技严谨、宏观商业、热点元气、还是文艺治愈。
*   **推导专属配色组合**：
    *   **主色 (Primary)**：用于核心 H2 标题修饰、重点强调字、按钮、卡片顶部装饰等。建议采用高饱和度但不过于刺眼的颜色（如 `#4f46e5` 靛蓝、`#0891b2` 深青、`#b45309` 琥珀橘）。
    *   **辅助色 (Secondary)**：用于 H3 标题左侧竖条、卡片左侧粗边框、次级修饰。
    *   **背景色 (Background)**：用于强调卡片的背景（如 `#faf5ff` 淡紫、`#f0fdf4` 淡绿、`#f8fafc`  slate灰）。
*   **推导排版参数**：
    *   字号：正文字体强制使用公众号黄金尺寸 `16px`。
    *   行高 (`line-height`)：商业严谨文采用 `1.75`；生活、情感散文采用 `1.8 - 1.9` 保证留白。
    *   字间距 (`letter-spacing`)：设置为 `0.04em - 0.06em` 提升中文呼吸感。
    *   圆角 (`border-radius`)：根据情感选择。科技商务采用较小圆角 (`4px - 6px`)；生活治愈采用大圆角 (`8px - 12px`)。
    *   正文文字颜色：强制使用深 slate 灰（`#334155` 或 `#2c3e50`），**禁止使用纯黑色 (#000)**，以降低视觉疲劳。

### 2. 微信 HTML 元素样式映射规范
在转换 Markdown 为 HTML 时，必须为不同的 Markdown 元素动态渲染符合以下内联样式的属性：

#### 2.1 H1 (文章主标题 - 可选)
*   **样式**：字号 `24px`，加粗，文字颜色使用深暗色（如 `#1e1b4b`），对齐方式建议为两端对齐或居中，边距为 `margin-bottom: 25px`。

#### 2.2 H2 (主章节标题)
微信排版的灵魂。禁止出现无修饰的裸 h2。必须应用以下精致格式之一（结合生成的主色和辅助色）：
*   **格式 A (渐变背景条)**：`background: linear-gradient(to right, {主色10%透明度}, rgba(255,255,255,0)); border-left: 5px solid {主色}; padding: 10px 15px; border-radius: 4px; font-size: 19px; color: {主色暗色}; font-weight: bold; margin: 40px 0 20px;`
*   **格式 B (底部粗底线)**：`display: inline-block; border-bottom: 3px solid {主色}; padding-bottom: 6px; font-size: 19px; color: {主色暗色}; font-weight: bold; margin: 40px 0 20px;`

#### 2.3 H3 (子章节标题)
*   **样式**：字号 `17px`，加粗，`margin: 30px 0 15px;`，左侧添加一条辅助色细线：`border-left: 3px solid {辅助色}; padding-left: 10px; color: {辅助色暗色};`。

#### 2.4 Paragraph & List (正文与列表)
*   **样式**：正文字号 `16px`，两端对齐（`text-align: justify;`），文字颜色使用炭灰或深墨（如 `#334155`），行高和字间距使用步骤 1 确定的参数。列表 `ul`, `ol` 的列表项 `li` 需设置 `margin-bottom: 8px; font-size: 15px; color: #475569;`。

#### 2.5 Blockquote (金句与重点引言)
*   **样式**：使用卡片化包裹。`background-color: {背景色}; border-left: 4px solid {主色或辅助色}; padding: 15px 20px; border-radius: 0 {圆角} {圆角} 0; margin: 20px 0; color: #475569; font-style: italic; font-size: 15px; line-height: 1.7;`。

#### 2.6 Markdown 表格 (Table)
微信原生表格极易出现屏幕溢出。必须使用外层容器进行防溢出排版：
*   **外层包裹**：使用 `<div style="overflow-x: auto; margin: 25px 0; border: 1px solid #e2e8f0; border-radius: {圆角};">`。
*   **Table 样式**：`width: 100%; border-collapse: collapse; font-size: 14px; text-align: center; color: #334155;`。
*   **表头 (Th)**：`background-color: {主色}; color: #ffffff; padding: 12px 10px; font-weight: bold;`。
*   **表身 (Td)**：`padding: 12px 10px; border-bottom: 1px solid #f1f5f9;`，交替行可以加上浅背景色（`#f8fafc`）。

#### 2.7 图片 (Image)
*   **样式**：外层加上 `<div style="text-align: center; margin: 30px 0;">`，图片本身设置 `max-width: 100%; height: auto; border-radius: {圆角}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);`。图注使用 `<p style="font-size: 13px; color: #64748b; margin-top: 8px;">`。

### 3. 生成与输出
*   将所有处理后的 HTML 标签合并在标准 HTML5 基本文档结构中（包含完整的 `<html>`, `<head>`, `<body>` 标签，以及编码声明 `<meta charset="UTF-8">`）。
*   将排版后的全部内容渲染到一个 `.html` 文件中。

### 4. 健壮性自审 (Self-Correction)
输出前，Agent 必须在心智中做二次审核：
*   是否有非内联样式？（微信只支持 `style="..."` 属性，任何 `<style>` 标签或 class 类选择器在粘贴后都会失效，**必须全部转为内联属性**）。
*   标签是否完全闭合？（特别是复杂的 `<div>` 卡片嵌套和表格结构，如果有一个标签没有闭合，会导致公众号编辑器渲染完全瘫痪）。
*   图片是否保留了原始的有效链接？

---

## Rate Limiting
Not applicable.（纯文本逻辑重构，不涉及外部非 API 调用。）

---

## Common Mistakes

*   **千篇一律的配色**：忽视了题材和情感剖析，导致无论是严肃的财经分析还是温馨的情感杂记，都使用同一种靛蓝科技色调。务必在步骤 1 中为文章起草独一无二的 Palette。
*   **未闭合的标签**：大模型在生成大量的长 HTML 字符时，容易在尾部丢失几个闭合 `</div>` 标签。这会导致用户粘贴到微信后，正文后的所有版块（如留言区、赞赏码）全部缩进变形。必须运行严格的闭合审查。
*   **使用微信不支持的外部 CSS**：使用了类似于 `<style>.my-h2 { ... }</style>` 的外部样式表。微信编辑器会将其直接吞掉。必须坚决把所有样式内联化。
