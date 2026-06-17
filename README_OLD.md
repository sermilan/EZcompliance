# 从业十余年收集的网络安全与合规文件，全部共享

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Project Status: Active](https://img.shields.io/badge/Project-Status-Active-green.svg)](https://www.repostatus.org/#active)

> 中国网络安全合规义务知识库 | Cybersecurity Compliance Obligation (COU) Knowledge Base for China

## 概述

网络、数据安全与合规领域，涵盖从业十来年的各种相关文件，全部开放共享。

原始文件大概有6个GB，做了处理后，大概文件数量1000+。

**前前后后花了两周的时间处理这些文件，主要做了三件事**

1. **全部做了OCR识别，因为里面有很大一部分是扫描pdf文件** 
2. **转为了AI更容易理解的Markdown文件**
3. **按照我定义的最小合规单元COU进行了一部分文件的转化**

**注：本打算补充[[双链]]以方便大家在Obsidian上作为知识管理，但一番操作后发现效果并不理想。有兴趣的可以自行再做尝试**

**处理细节**

1. **格式统一** — 将散落的 PDF、Word、HTML 等格式的原始政策文件转换为 Markdown，统一便于机器解析和全文检索
2. **COU 语义提取** — 借助 LLM 对每一条义务条款进行理解，按照五要素结构（主体/动作/客体/条件/权重）进行语义标注和结构化提取
3. **交叉去重** — 同一义务可能出现在多个标准中，通过指纹比对实现跨标准合并

最终呈现三个层次的资产：1015 份政策原文（514 份已完成 COU 标注）、5322 条原始 COU 提取物、3801 个去重合并后的唯一合规义务单元。这套知识体系可服务于合规审计、风险评估、安全建设对标等多种场景。


### 核心概念

**COU (Compliance Obligation Unit)** — 合规义务单元，是将政策文本中的义务条款解构为标准化结构：

| 字段 | 说明 | 示例 |
|------|------|------|
| Subject | 义务主体 | 网络安全等级保护对象运营者 |
| Action | 动作词 | 建立、记录、提供、应当 |
| Object | 客体/对象 | 网络安全事件应急预案 |
| Condition | 触发条件 | 定级为第5级时 |
| Weight | 合规权重 | 10.4 (= 8.0 × 1.3) |

### 目录结构

```
china-cybersecurity-cou/
├── README.md
├── LICENSE
│
├── policy-raw/                          # 原始政策文件 (1015个)
│   ├── [✓] GBT22239-2019-网络安全等级保护基本要求.md   # [✓]=已COU化
│   ├── [✓] 网络安全法.md                              # [✓]=已COU化
│   └── [○] 欧盟GDPR一般数据保护法案.md               # [○]=未COU化
│   └── ...
│
├── cou-r/                                # COU原始层 (5322个)
│   ├── COU-R-PIPL-六十九-应.md          # 法律类: COU-R-{法典}-{条款}-{动作}
│   └── COU-R-22239-3-8-1-4-d.md         # 标准类: COU-R-{标准号}-{级}-{章}-{条}-{款}
│   └── ...
│
├── cou-m/                                # COU合并层 (3801个)
│   ├── COU-M-00069D-1687.md             # 跨标准合并后的唯一COU
│   └── ...
│
├── cou-export.json                       # SaaS导入用JSON (完整3801条)
│
└── scripts/                              # 处理脚本
    ├── cou_batch_extract.py              # GB/T标准COU批量提取
    ├── cou_extract_pipl.py               # 法律法规COU提取
    ├── cou_dedup.py                       # COU去重合并
    └── policy_rename.py                  # 政策文件规范化重命名
```

## 数据统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 政策原文 | 1015 | `[✓]` 已COU化 514 / `[○]` 未COU化 500 |
| COU原始层 | 5322 | 来自177个来源的义务提取 |
| COU合并层 | 3801 | 去重合并后的唯一合规义务 |
| 覆盖标准 | 102 | GB/T、GAT、GBZ、网络安全法、PIPL、DSL等 |

### 覆盖的主要标准

**国家标准 (GB/T)**
- GBT 22239-2019 网络安全等级保护基本要求
- GBT 18336-2015 信息技术安全评估准则
- GBT 20272-2019 操作系统安全技术要求
- GBT 20984-2022 信息安全风险评估方法
- GBT 28448-2018 等级保护测评要求
- GBT 39725-2020 数据安全技术
- 以及其他90+项标准

**法律法规**
- 中华人民共和国网络安全法
- 中华人民共和国个人信息保护法
- 中华人民共和国数据安全法
- 关键信息基础设施安全保护条例
- 网络安全审查办法
- 以及其他20+项法规

## COU结构说明

### COU-R (Raw) 原始层

每个COU-R文件对应一条原始义务条款：

```yaml
---
cou_id: "COU-R-22239-3-8-1-4-d"
source: "GBT 22239-2019"
chapter: "3-8.1.4"
clause: "d"
subject: "网络安全等级保护对象运营者"
action: "提供"
object: "数据有效性检验功能，保证通过人机接口输入..."
condition: "定级为第3级时"
base_weight: 9.6
weight_factor: 1.3
final_weight: 12.5
domains: ['主机安全', '计算环境']
fingerprint: "网络安全等级保护对象运营者|提供|数据有效性检验功能..."
level: "3"
---
```

### COU-M (Merged) 合并层

按"主体|动作|客体"指纹去重合并，跨标准归一化：

```yaml
---
cou_id: "COU-M-00069D-1687"
type: merged
fingerprint: "网络运营者|提供|数据有效性检验功能，保证通过人机接口输入..."
sources: ['GBT 22239-2019', 'GBT 20272-2019']
raw_cou_count: 2
avg_weight: 11.45
max_weight: 12.5
domains: ['主机安全']
norm_subjects: ['网络运营者']
cross_standard: true
---
```

## 使用场景

### 1. 合规审计
```bash
# 查找所有"网络运营者"相关的"记录"义务
grep -r "网络运营者|记录|" cou-m/
```

### 2. 风险评估
```bash
# 导出高权重义务（weight > 15）到CSV
jq '.[] | select(.max_weight > 15)' cou-export.json
```

### 3. 标准映射
```bash
# 查看某标准涉及的COU数量
grep -l "GBT 22239" cou-r/*.md | wc -l
```

### 4. SaaS导入
```bash
# 导入到合规管理SaaS
curl -X POST /api/cou/import -d @cou-export.json
```

## 文件命名规范

### 政策原文
- `[✓] {标准号}-{描述名称}.md` — 已提取COU
- `[○] {原始名称}.md` — 尚未提取COU

### COU原始层
- 法律类: `COU-R-{LAW_CODE}-{ARTICLE}-{NORM_ACTION}.md`
  - 例: `COU-R-PIPL-六十九-YING.md`
- 标准类: `COU-R-{STD_CODE}-{LEVEL}-{SECTION}-{CLAUSE}-{SUB}.md`
  - 例: `COU-R-22239-3-8-1-4-d.md`

### COU合并层
- `COU-M-{FINGERPRINT_PREFIX}-{SEQ}.md`
- 例: `COU-M-00069D-1687.md`

## 贡献指南

### 提交新的COU提取

1. 政策原文放入 `policy-raw/`
2. 运行提取脚本:
   ```bash
   python3 scripts/cou_batch_extract.py --source "GBT XXXXX-YYYY"
   ```
3. 提交COU-R文件
4. 运行合并脚本:
   ```bash
   python3 scripts/cou_dedup.py
   ```

### 报告问题

- 政策原文错误 → 提交 Issue 到原始文件
- COU提取错误 → 提交 Issue 到对应COU-R文件
- 遗漏义务 → 提交 PR 添加缺失的COU

## 致谢

本知识库的构建参考了以下工作：

- [全国信息安全标准化技术委员会 (TC260)](https://www.tc260.org.cn/) — 标准文件
- [国家互联网信息办公室](http://www.cac.gov.cn/) — 政策法规
- OWASP 项目 — 安全评估框架
- NIST SP 800系列 — 风险管理指南

## 免责声明

- 本知识库仅供学习研究参考，不构成法律合规建议
- 政策原文版权归原发布机构所有
- 请以官方原文为准，本库不保证内容实时更新

## 许可证

本项目采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可证

- 政策原文：版权归原发布机构所有，CC BY-SA仅适用于COU标注和结构化数据
- COU提取物：采用 CC BY-SA 4.0

---

**Generated**: 2026-05-07
**Last Updated**: 2026-05-07
**Total COU**: 3,801 unique compliance obligations
