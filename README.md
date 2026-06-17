# 从业十余年收集的网络安全与合规文件，全部共享

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Project Status: Active](https://img.shields.io/badge/Project-Status-Active-green.svg)](https://www.repostatus.org/#active)

> 中国网络安全合规义务知识库 | Cybersecurity Compliance Obligation (COU) Knowledge Base for China

## 概述

网络、数据安全与合规领域，涵盖从业十来年的各种相关文件，全部开放共享。

原始文件大概有6个GB，做了处理后，大概文件数量1000+。

**主要做了三件事**

1. **全部做了OCR识别，因为里面有很大一部分是扫描pdf文件**
2. **转为了AI更容易理解的Markdown文件**
3. **按照我定义的最小合规单元COU进行了一部分文件的转化**

**注：本打算补充[[双链]]以方便大家在Obsidian上作为知识管理，但一番操作后发现效果并不理想。有兴趣的可以自行再做尝试**

**处理细节**

1. **格式统一** — 将散落的 PDF、Word、HTML 等格式的原始政策文件转换为 Markdown，统一便于机器解析和全文检索
2. **COU 语义提取** — 借助 LLM 对每一条义务条款进行理解，按照五要素结构（主体/动作/客体/条件/权重）进行语义标注和结构化提取
3. **交叉去重** — 同一义务可能出现在多个标准中，通过指纹比对实现跨标准合并

最终呈现三个层次的资产：1015 份政策原文（514 份已完成 COU 标注）、5572 条原始 COU 提取物、3942 个去重合并后的唯一合规义务单元。这套知识体系可服务于合规审计、风险评估、安全建设对标等多种场景。

---

### 核心概念

**COU (Compliance Obligation Unit)** — 合规义务单元，是将政策文本中的义务条款解构为标准化结构：

| 字段 | 说明 | 示例 |
|------|------|------|
| Subject | 义务主体 | 网络运营者 |
| Action | 动作词 | 建立、记录、提供、应当 |
| Object | 客体/对象 | 网络安全事件应急预案 |
| Condition | 触发条件 | 定级为第3级时 |
| Weight | 合规权重 | 8.0 (= 8.0 × 1.0) |

### 目录结构

```
EZcompliance/
├── README.md                             # 项目说明
├── LICENSE                               # CC BY-SA 4.0
├── COU化状态报告.md                       # COU化进度追踪
│
├── policy-raw/                           # 原始政策文件 (1016个, 31个分类文件夹)
│   ├── 法律法规/               (550)        # 网络安全法、PIPL、DSL 等
│   ├── GBT-其他/               (95)         # GB/T 标准合集
│   ├── 指南/                   (65)         # 各类指南/指引/规范
│   ├── GBT20984/               (42)         # 信息安全风险评估方法
│   ├── GAT系列/                (31)         # GA/T 行业标准
│   ├── 国际与行业框架/          (31)         # OWASP, PCI-DSS, ISO, NIST 等
│   ├── GAT2380-2026/           (1)          # 数据安全基本要求（报批稿）
│   └── ...
│
├── COU/
│   ├── COU-R（原始）/                     # COU原始层 — 按标准分文件夹
│   │   ├── README.md                     # COU-R 索引
│   │   ├── GAT2380-2026/      (250)      # GA/T 2380 数据安全基本要求
│   │   ├── GBT22239-2019/     (759)      # 等级保护基本要求
│   │   ├── GBT28448-2019/     (350)      # 等级保护测评要求
│   │   ├── 个人信息保护法/     (95)
│   │   ├── 数据安全法/        (34)
│   │   └── ... (102 个标准文件夹, 共 5572 条)
│   │
│   └── COU-M（合并）/                     # COU合并层 — 跨标准去重
│       └── COU-M-{HASH}-{SEQ}.md         # 3942 个唯一合规义务
│
├── 场景/                                 # 场景聚合文件
│   ├── 原始/                              # 按标准分文件夹
│   │   └── GAT2380-2026/     (24)         # 按数据环节 + 等级组织
│   └── 合并/                              # 跨标准场景合并（待生成）
│
├── data/                                 # 数据导出
│   ├── cou_merged_export.json            # SaaS 导入用 JSON (3942条)
│   └── GAT2380-2026_COU_export.json      # GA/T 2380 专项导出 (250条)
│
├── scripts/                              # 处理脚本
│   ├── cou_batch_extract.py              # GB/T 标准 COU 批量提取
│   ├── cou_extract_pipl.py               # 法律法规 COU 提取
│   ├── cou_dedup.py                      # COU 去重合并
│   └── policy_rename.py                  # 政策文件规范化重命名
│
└── cou_extract_gat2380.py                # GA/T 2380 专项提取脚本
```

### 最新更新 (2026-06-17)

- ✅ **GA/T 2380-2026 数据安全基本要求（报批稿）** COU 提取完成 (250条)
- ✅ 目录结构优化：COU-R 按"同一标准一个文件夹"重组为 102 个目录
- ✅ 分支统一为 `main`，旧 `master` 已删除
- ✅ COU-M 重新生成：3942 个去重合并单元 (含 184 个跨标准合并)

---

## 数据统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 政策原文 | 1015 | `[✓]` 已COU化 514 / `[○]` 未COU化 500 |
| COU原始层 | 5572 | 来自 102 个标准/法规 |
| COU合并层 | 3942 | 去重合并后的唯一合规义务 (含 184 个跨标准合并) |
| 场景聚合 | 24 | 按数据环节 + 等级组织 (GA/T 2380) |

### 覆盖的主要标准

**最新**

- **GA/T 2380-2026** 信息安全技术 网络安全等级保护数据安全基本要求（报批稿）

**国家标准 (GB/T)**

- GBT 22239-2019 网络安全等级保护基本要求
- GBT 28448-2019 等级保护测评要求
- GBT 18336-2015 信息技术安全评估准则
- GBT 20272-2019 操作系统安全技术要求
- GBT 20984-2022 信息安全风险评估方法
- 以及其他 90+ 项标准

**法律法规**

- 中华人民共和国网络安全法
- 中华人民共和国个人信息保护法
- 中华人民共和国数据安全法
- 关键信息基础设施安全保护条例
- 以及其他 15+ 项法规

---

## COU结构说明

### COU-R (Raw) 原始层

每条 COU-R 对应一条原始义务条款，按标准分文件夹组织：

```yaml
---
cou_id: "COU-R-2380-L3-6-5-1-a"
source: "GAT 2380-2026"
chapter: "6.5.1"
clause: "a"
level: "3"
subject: "网络运营者"
action: "对登录的程序或应用进行身份标识和鉴别"
object: "身份鉴别信息具有复杂度要求并定期更换"
condition: "定级为第3级时"
base_weight: 8.0
final_weight: 8.0
domains: ["计算环境安全", "数据存储安全"]
fingerprint: "网络运营者|对登录的程序或应用进行身份标识和鉴别|..."
---
```

**命名规范**

- 标准类: `COU-R-{标准号}-L{等级}-{章节}-{条款}.md`
  - 例: `COU-R-2380-L3-6-5-1-a.md`
- 法律类: `COU-R-{法典}-{条款}-{动作}.md`
  - 例: `COU-R-PIPL-六十九-应.md`

### COU-M (Merged) 合并层

按"主体|动作|客体"指纹去重合并，跨标准归一化：

```yaml
---
cou_id: "COU-M-00069D-1687"
type: merged
fingerprint: "网络运营者|提供|数据有效性检验功能..."
sources: ['GBT 22239-2019', 'GBT 20272-2019']
raw_cou_count: 2
avg_weight: 11.45
cross_standard: true
---
```

COU-M 文件中的 wikilink 包含标准子文件夹路径，可直接在 Obsidian 中解析：
```
[[GBT20272/COU-R-20272-4-4-5-3-h.md|COU-R-20272-4-4-5-3-h]]
```

---

## 使用场景

### 1. 合规审计
```bash
# 查找所有"网络运营者"相关的"记录"义务
grep -r "网络运营者|记录|" COU/COU-M（合并）/
```

### 2. 风险评估
```bash
# 导出高权重义务（weight > 10）到CSV
jq '.[] | select(.max_weight > 10)' data/cou_merged_export.json
```

### 3. 标准映射
```bash
# 查看某标准涉及的COU数量
ls COU/COU-R（原始）/GBT22239-2019/ | wc -l
```

### 4. SaaS导入
```bash
# 导入到合规管理SaaS
curl -X POST /api/cou/import -d @data/cou_merged_export.json
```

---

## 贡献指南

### 提交新的COU提取

1. 政策原文放入 `policy-raw/`
2. 运行提取脚本:
   ```bash
   python3 cou_extract_gat2380.py   # 或其他专用提取脚本
   ```
3. COU-R 文件自动归入 `COU/COU-R（原始）/{标准名}/`
4. 运行合并脚本:
   ```bash
   python3 scripts/cou_dedup.py
   ```

---

## 致谢

- [全国信息安全标准化技术委员会 (TC260)](https://www.tc260.org.cn/) — 标准文件
- [国家互联网信息办公室](http://www.cac.gov.cn/) — 政策法规
- 本知识库的构建参考了 OWASP、NIST SP 800 系列等工作

## 免责声明

- 本知识库仅供学习研究参考，不构成法律合规建议
- 政策原文版权归原发布机构所有
- 请以官方原文为准，本库不保证内容实时更新

## 许可证

本项目采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可证

- 政策原文：版权归原发布机构所有，CC BY-SA 仅适用于 COU 标注和结构化数据
- COU 提取物：采用 CC BY-SA 4.0

---

**Generated**: 2026-05-07 · **Last Updated**: 2026-06-17  
**Total**: 5,572 COU-R · 3,942 COU-M · 102 standards
