---
title: "ITSS运维能力成熟度模型"
source: "ITSS/ITSS运维能力成熟度模型.pdf"
type: "pdf"
processed: "2026-04-22T12:17:06.346188"
---

ITSS $ ^{\text{®}} $

ITSS.1—2015

# 信息技术服务 运行维护服务能力成熟度模型

# Information technology service—Maintenance service capability maturity model

2015-02-15 发布

2015-02-15 实施

中国电子工业标准化技术协会

信息技术服务分会

发布



---



---

## 目 次

前言 …… II  
引言 …… III  
1 范围 …… 1  
2 规范性引用文件 …… 1  
3 术语定义和缩略语 …… 1  
4 运维服务能力成熟度模型 …… 1  
5 基本级 …… 7  
6 拓展级 …… 12  
7 改进（协同）级 …… 24  
8 提升（量化）级 …… 41

---

## 前言

运维服务能力成熟度模型（以下简称：本模型）参照GB/T1.1-2009《标准化工作导则 第1部分：标准的结构和编写》的要求起草。

本模型由中国电子工业标准化技术协会信息技术服务分会提出并归口。

本模型是信息技术服务标准（Information Technology Service Standards，简称：ITSS）库组成部分。

本模型的某些内容可能涉及专利，本模型的发布机构不承担识别这些专利的责任。

本模型的起草单位：浪潮软件股份有限公司、中国电子技术标准化研究院、北京华胜天成科技股份有限公司、神州数码系统集成服务有限公司、北京华宇软件股份有限公司、北京信城通数码科技有限公司、上海宝信软件股份有限公司、四川久远银海软件股份有限公司、西安未来国际信息股份有限公司、大连华信计算机技术股份有限公司、北京荣之联科技股份有限公司、广州华南资讯科技有限公司、北京护航科技有限公司、万达信息股份有限公司、广州市金禧信息技术服务有限公司、成都信息化技术应用发展中心、大连软件行业协会、联通集成有限公司、广州赛宝认证中心有限公司。

本模型的主要起草人：张帆、周平、宋跃武、刘玲、金桥、宋晓东、白璐、李雪、牛娜、孙佩、刘宏、林平、熊健淞、潘纯峰、张宏伟、郭浩、顾俊、尹宏、但强、段笑雨、徐秀、黄艳春、王铮、张王军。

本模型的参与起草单位：湖北省软件行业协会、首都信息发展股份有限公司、中国软件评测中心、北京中科金财科技股份有限公司、山东省标准化研究院、山东省电子信息产品检验院、赛尔网络有限公司、北京合力金桥系统集成技术有限公司、中国华融资产管理股份有限公司、上海翰纬信息管理咨询有限公司、通号通信信息集团有限公司、北京信息化协会、北京斯福泰克科技股份有限公司、中科软科技股份有限公司、太极计算机股份有限公司、中国平煤神马集团平顶山信息通信技术开发公司、沈阳赛宝科技服务有限公司、广西软件管理中心、广西电子信息协会、海南省软件行业协会、福建省软件行业协会、厦门市信息消费产业与应用促进会、深圳市信息工程协会、广州南天电脑系统有限公司、广州越维信息科技有限公司、广州中软信息技术有限公司、广东卓维网络有限公司、广东地球村计算机系统股份有限公司、文思海辉技术有限公司、河南九洲计算机有限公司、天讯瑞达通信技术有限公司、重庆市赛晟信息技术服务有限公司、山西天地科技有限公司、重庆商社（集团）有限公司、重庆南华中天信息技术有限公司、重庆市中冉信息产业有限公司、陕西北佳信息技术有限公司、甘肃紫光智能交通与控制技术有限公司、深圳市雷迪信息技术有限公司、陕西通信信息技术有限公司、中科院沈阳自动化研究所、沈阳荣科科技股份有限公司、大连软件公共服务平台、辽宁省评测中心、吉林省联宇合达科技有限公司、东软集团股份有限公司、中科院沈阳自动化所、吉林省电子产品监督检验研究院。

使用帮助信息：任何单位和个人在使用本模型的过程中，若存在疑问，或有对本模型的改进建议和意见，请与中国电子工业标准化技术协会信息技术服务分会联系。

电话：010-68208771/2/3；电子邮件：itss@miit.gov.cn

通信地址：北京市海淀区万寿路27号电子大厦东配楼412房间（100846）

为了推动本模型的持续改进，使其内容更加贴近用户组织的实际需求，欢迎社会各方力量参加本模型的持续改进，本模型的更多信息欢迎访问中国电子工业标准化技术协会信息技术服务分会官方网站。

http://www.itss.cn

---

## 引 言

随着我国各行业、各领域信息化工作的深入开展，信息化发展由重建设向重应用转移，运行维护（以下简称运维）服务正逐步发展成为信息技术服务业的一个重要子行业，并保持持续快速增长态势。

按照工业和信息化部的总体部署，我国信息技术服务业未来一段时期内的发展目标是由大变强，发展重心从追求规模速度转向注重产业发展质量。在此背景下，运维服务能力成熟度模型应运而生，为运维服务行业发展的规范和引导提供了有益的指导。通过开展运维服务能力成熟度评估，有助于：

a）建立运维服务组织的能力水平评判标准；

b) 提供有效选择和评价运维服务供方的方法；

c）提供运维服务能力建设的最佳实践；

d) 支撑提升运维服务行业发展质量的评价方法。

---



---

# 信息技术服务运维服务能力成熟度模型

## 1 范围

信息技术运维服务能力成熟度模型包括基本级、拓展级、改进（协同）级和提升（量化）级四个等级，从低到高分别用四、三、二、一表示。

本模型规定了各级运维服务能力成熟度在管理、人员、过程、技术和资源方面应满足的要求。

本模型适用于运维服务供方建立、保持和改进运维服务能力，也适用于评价供方运维服务能力。

## 2 规范性引用文件

下列文件对于本文件的引用是必不可少的。凡是注日期的引用文件，仅注日期的版本适用于本文件。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 28827.1—2012 信息技术服务 运行维护 第1部分：通用要求

GB/T 28827.2—2012 信息技术服务 运行维护 第2部分：交付规范

GB/T 28827.3—2012 信息技术服务 运行维护 第3部分：应急响应规范

国家标准《信息技术服务质量评价指标体系》（报批稿）

## 3 术语定义和缩略语

### 3.1 术语和定义

GB/T 28827.1、GB/T 28827.2、GB/T 28827.3、GB/T 29264—2012、《信息技术服务质量评价指标体系》（报批稿）界定的以及下列术语和定义适用于本文件。

3.1.1

## 模型 model

系统、实体、现象或过程的物理、数学或逻辑表示。

#### 3.1.2 

## 成熟度 maturity

组织在实施、度量、控制和改善运行维护服务的过程中，各个发展阶段的服务能力程度。

### 3.2 缩略语

下列缩略语适用于本文件。

ITSS: 信息技术服务标准（Information Technology Service Standards）

KPI：关键绩效指标（Key Performance Indicator）

SLA：服务级别协议（Service-Level Agreement）

---

## 4 运维服务能力成熟度模型

### 4.1 运维服务能力成熟度模型框架

运维服务能力成熟度模型的建立参考了信息技术服务领域有关成熟度的各类模型，它是反映运维服务能力水平的框架。该模型按运维服务组织能力建设和管理定义了逐步进化的四个等级，自低向高分别为基本级、拓展级、改进（协同）级和提升（量化）级。如图1所示。

每个运维服务能力成熟度（以下简称：成熟度）等级由管理、人员、资源、技术和过程所组成。每个成熟度等级表明一个组织的运维服务能力达到的水平。

<div style="text-align: center;"><img src="imgs/img_in_image_box_311_466_896_795.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图1 运维服务能力成熟度模型框架</div>


运维服务能力水平的提升通过渐进的方式来实现，较高的成熟度等级涵盖了低等级的全部要求，成熟度等级不可跨级，即较高的成熟度等级必然以低成熟度等级为基础。

运维服务能力成熟度是基于ITSS的原理、颁布实施的GB/T 28827系列国家标准和电子行业标准（见附录A）提出的。基本级和拓展级以GB/T 28827.1为基础提出成熟度要求，改进（协同）级以GB/T 28827.1、GB/T 28827.2、GB/T 28827.3为基础提出成熟度要求，提升（量化）级以GB/T 28827.1、GB/T 28827.2、GB/T 28827.3及《信息技术服务质量评价指标体系》（报批稿）为基础提出成熟度要求。运维服务能力成熟度模型在实践中为组织的运维服务能力建设提供路线图和方法论。

### 4.2 运维服务能力成熟度模型构成

本模型中各成熟度等级由特征和关键指标构成，其结构如图2所示。每个成熟度等级规定了运维服务组织在能力管理、人员、过程、技术和资源方面的要求。

依据标准GB/T 28827.1、GB/T 28827.2、GB/T 28827.3和《信息技术服务质量评价指标体系》，并结合每个成熟度等级的特征和关键指标，对每个成熟度等级规定了具体要求。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_323_194_852_588.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图2 运维服务能力成熟度模型的构成</div>


### 4.3 成熟度等级

#### 4.3.1 基本级

##### 4.3.1.1 定义

基本级（四级），是指依据GB/T 28827.1实施了必要的运维服务能力管理，日常运维服务活动有序开展。

##### 4.3.1.2 特征

运维服务组织应具备以下特征：

a）管理层对实施运维服务能力管理有基本意识，依据GB/T 28827.1初步建立运维服务能力管理体系；

b）个人技术水平对运维服务能力的提升发挥关键作用；

c）基本建成框架性的运维服务管理过程，并得到实施；

d) 具备运维技术研发基本条件；

e）根据运维服务需求提供必要的资源，开始逐步积累和利用知识。

##### 4.3.1.3 关键指标

基本级暂无总的关键指标要求。针对具体的运维服务能力管理和组成运维服务能力的各要素有关键指标要求。

#### 4.3.2 拓展级

##### 4.3.2.1 定义

拓展级（三级），是指依据GB/T 28827.1实施了较为系统的运维服务能力管理，并形成了较为完善的人员、过程、技术和资源方面的管理制度，且得到有效实施。

##### 4.3.2.2 特征

运维服务组织应具备以下特征：

a）管理层对实施运维服务能力管理具有较高认识，并结合业务发展需要，策划和实施运维服务能力管理；

b) 依据 GB/T 28827.1 建立运维服务能力管理体系，并得到有效实施；

c）单个业务单元或运维服务团队的综合能力决定了整体运维服务能力水平；

d) 运维服务管理过程全面覆盖运维业务和相关部门，在过程的精细化、执行效果一致性方面可持续改进；

e) 运维技术与业务发展基本匹配，并确保技术研发的持续性；

---

f）为运维服务业务发展提供资源支持，在核心工具、知识库、服务台等之间的集成水平和整体协调性方面持续改进。

##### 4.3.2.3 关键指标

a）运维服务能力管理的投入，包括人、财、物等方面；

b) 运维服务目录的完备性；

c) 关键岗位的人员流动率；

d) 关键绩效指标（KPI）体系；

e) 核心工具应用情况；

f) 知识规模及其应用情况。

#### 4.3.3 改进（协同）级

##### 4.3.3.1 定义

改进（协同）级（二级），是指组织的运维服务能力发展战略和目标清晰，形成了完善的运维服务能力管理体系，并能综合 GB/T 28827.1、GB/T 28827.2、GB/T 28827.3 实现人员、过程、资源和技术能力要素的协同改进。

##### 4.3.3.2 特征

运维服务组织应具备以下特征：

a) 管理层对实施运维服务能力管理具有明确的方向和目标，运维服务业务的发展由运维交付、质量管理、人力资源管理、技术研发等部门协同推进，实现运维服务产品标准化，具备运维服务集成能力；

b) 依据GB/T 28827.1、GB/T 28827.2、GB/T 28827.3建立完善的运维服务能力管理体系，并在运维服务设计、研发和交付方面具备考核服务能力的指标体系和方法；

c）运维服务管理过程实现精细化，并能通过完备的制度保障交付过程的一致性和准确性；

d) 运维技术研发与业务发展协调一致并具备前瞻性，拥有业务发展所需的核心技术；

e）能够统一规划运维业务发展所需的资源，各类资源之间具有较强的关联度和协调性，共享水平高，资源的提供和使用初步实现量化管理。

##### 4.3.3.3 关键指标

a) 服务产品标准化程度；

b) 基于基线的管理；

c) 过程自动化水平;

d) 运维技术研发投入比；

e）知识库建设及应用水平。

#### 4.3.4 提升（量化）级

##### 4.3.4.1 定义

提升（量化）级（一级），是指基于信息技术服务业务综合发展的需要，实施基于量化提升的运维服务能力体系，并形成推动运维服务业务变革的机制。

##### 4.3.4.2 特征

运维服务组织应具备以下特征：

a) 管理层对实施运维服务能力体系建设具有明确的量化指标，并能合理有效使用各种指标数据进行决策；

b) 运维服务能力管理体系能够基于量化指标进行优化提升；

c）依据全面的运维服务管理过程量化指标体系进行过程再造，实现改进与变革；

d) 运维技术研发与组织战略协调一致，具有技术创新能力，建立技术促进业务发展的合理绩效指标，并根据数据积累提升技术研发能力水平；

e）根据运维服务质量的数据积累，优化改进运维服务能力。

---

##### 4.3.4.3 关键指标

a) 服务质量度量指标体系；

b) 投资回报率评价指标体系；

c) 自主可控水平；

d) 集成和组合服务能力水平。

### 4.4 应用

#### 4.4.1 概述

本模型适用于任何规模和业务领域的运维服务组织。外部的运维服务组织和需方内部的运维服务组织都可以参照本模型的要求建立、保持和改进运维服务能力。运维服务组织可以：

a）将本模型作为指南，确定自身运维服务能力建设和改进的目标和途径：

b) 基于自身的运维服务业务基础和管理要求，以某成熟度等级为目标，实施全方位的改进，以实现运维服务能力管理的提升；

c）结合自身的运维服务能力和管理需要，借鉴本模型的具体要求，在选定的区域、要素和环节上改进提高。

本模型是评价运维服务组织服务能力的依据和准则。模型可用于以下四种模式的评估：

a) 运维服务供方的自我评估；

b) 第三方评估机构的外部评估；

c) 咨询机构的诊断评估；

d) 运维服务需方对供方进行选择和评价。

#### 4.4.2 自我评估

运维服务供方的自我评估是指运维服务组织已建立并实施了运维服务能力管理体系，根据组织的管理要求，定期的或临时性对运维服务能力管理的符合性和有效性进行内部检查。自我评估旨在发现运维服务能力管理和实施中的问题或不足，识别改进点，并提出改进措施，从而促进本组织运维服务能力和服务质量的持续改进。

#### 4.4.3 第三方评估

第三方评估机构的外部评估是指被授权的运维服务能力评估机构，基于运维服务供方或需方的申请，依据本模型，按照评估程序对运维服务组织所进行的正式评估。外部评估旨在通过第三方的客观评价证实运维服务组织的服务能力管理已达到某成熟度等级，其评估结果即可为运维服务供方确定自身运维服务能力管理所达到的成熟度等级，亦可为需方选择运维服务供方提供参考信息，或有助于需方对运维供方的服务能力建立信任。

#### 4.4.4 诊断评估

咨询机构的诊断评估是指咨询团队参照约定的能力成熟度目标等级，通过检查、提问和现场访谈等方式，对运维服务组织的服务能力管理现状所进行的调研和差距分析。诊断评估旨在快速了解运维服务组织的运维服务能力管理基础，更有效地协助运维服务组织运用本模型建立或健全运维服务能力管理体系；其结果也便于运维服务组织具体了解自身的差距，设立运维服务能力改进目标和范围，并针对具体差距采取改进措施，推进运维服务能力的提升，以实现运维服务业务和管理目标。

#### 4.4.5 需方要求

运维服务需方可以将运维服务能力成熟度模型作为评价和选择供方的依据，并对供方的运维服务能力提出要求，也可以针对外包运维服务所关联的业务或系统的重要程度，确定对运维服务供方的综合要求。

### 4.5 成熟度等级要求和关键指标的描述

本模型的第 5 章至第 8 章分别按照下述方式规定了各个成熟度等级的要求和关键指标。

---

a）每个成熟度等级由五个方面的要求构成，分别是管理要求、人员要求、资源要求、技术要求和过程要求。

b) 每个方面的要求以表格形式描述，其中：

1) 表格第一列为引用标准的章节；

2）表格第二列为引用标准的条款要求；

3）表格第三列为对应成熟度等级的具体要求，主要用于描述在满足标准条款要求的情况，满足该成熟度等级的特征要求应开展的相关工作；

4）表格第四列为对应成熟度等级要求的关键指标，主要用于描述实现了成熟度等级具体要求所具备的显著特征，同时也提供了评价是否达到具体成熟度等级要求的方法。

---

## 5 基本级

### 5.1 管理要求

基本级的管理要求见表 1。

<div style="text-align: center;">表 1 基本级的管理要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准章条</td><td style='text-align: center; word-wrap: break-word;'>标准要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.2 策划</td><td style='text-align: center; word-wrap: break-word;'>a) 根据自身业务定位和能力，策划运行维护服务对象的服务内容与要求，并形成服务目录；b) 依据组织的业务发展需要来建立组织结构和管理制度，支持服务目录的实施或实现；c) 对人员、资源、技术和过程进行规划，建立相适应的指标体系和服务保障体系；d) 策划如何管理、审核并改进服务质量，建立内部审核评估机制。</td><td style='text-align: center; word-wrap: break-word;'>建立运维服务目录并形成文档，并在提供运维服务的过程中得到应用。建立运维服务相关的组织架构和管理制度，并在实际应用过程中形成书面文件。a) 建立运维服务能力管理计划；b) 运维服务能力管理计划的制定和实施应结合GB/T 28827.1规定的四要素要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务目录；b) 能力管理计划；c) 质量管理制度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.3 实施</td><td style='text-align: center; word-wrap: break-word;'>a) 制定满足整体策划的实施计划，并按计划实施；b) 建立与需方的沟通协调机制；c) 按照服务能力要求实施管理活动并记录，确保服务能力管理和服务过程实施可追溯，服务结果可计量或可评估；d) 提交满足质量要求的交付物。</td><td style='text-align: center; word-wrap: break-word;'>建立与运维服务相适应的质量管理方法或制度，并得到应用。a) 有运维服务能力管理计划的具体实施方案及实施记录，包括：具体的任务、责任人、日程安排以及预期要达到的目标或结果；b) 有与需方有关的沟通记录；c) 有运维服务能力管理计划的实施结果或交付物的记录或总结报告；d) 有运维项目验收管理制度、服务质量报告（包括服务满意度报告内容等）。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务能力管理实施记录；b) 与需方沟通的记录；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.4 检查</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审服务过程及相关管理体系，以确保服务能力的适宜性和有效性；b) 调查需方满意度，并对服务能力策划实施的结果进行统计分析；c) 检查各项指标达成情况。</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审运维服务过程及相关管理制度；b) 建立满意度管理文件，对需方满意度进行调查和评价。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务定期评审记录；b) 满意度评价报告。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.5 改进</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务能力管理改进机制；b) 对不符合策划要求的行为进行总结分析；c) 对未达成的指标进行调查分析；d) 根据分析结果确定改进措施，制定服务能力改进计划。</td><td style='text-align: center; word-wrap: break-word;'>建立运维服务能力管理改进机制，及时修正能力管理中的缺陷。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

### 5.2 人员要求

基本级的人员要求见表 2。

<div style="text-align: center;">表 2 基本级的人员要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="3">GB/T 28827.1-2012 6.2 人员管理</td><td rowspan="3">a) 人员储备 
供方应建立运行维护服务相关的人员储备计划和机制，确保有足够的人员以满足与需方约定的当前和未来的运维业务需求。 
b) 人员培训 
供方应建立运行维护服务相关的培训体系或机制，在制定培训时应识别培训要求，并提供及时和有效的培训。 
c) 绩效考核 
供方应建立运行维护服务相关的绩效考核体系或机制，并能够有效组织实施。</td><td style='text-align: center; word-wrap: break-word;'>a) 具备能应对业务需求的人员配置管理措施； 
b) 关键岗位有人员储备，并定义此类人员变更的应对方法。</td><td rowspan="3">a) 关键岗位人员变更应对方； 
b) 培训实施记录； 
c) 人员绩效考核记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>能够识别培训需求，并实施对运维人员的培训。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期对人员进行绩效考核。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.3 岗位结构</td><td style='text-align: center; word-wrap: break-word;'>a) 管理岗人员和职责为： 
1) 在运行维护服务中负责管理运行维护服务； 
2) 与需方建立顺畅的沟通渠道，准确地将需方的需求传递到运维团队； 
3) 规划、检查运行维护服务的各个过程，对运行维护服务的策划、实施、检查、改进的范围、过程、信息安全和成果负责。 
b) 技术支持岗人员和职责为： 
1) 在运行维护服务中负责技术支持的人员，包括网络、操作系统、数据库、中间件、应用开发、硬件、集成、信息安全等方面的专业技术人员； 
2) 对运行维护服务过程中的请求、事件和问题做出响应，保障信息安全并对处理结果负责。 
c) 操作岗人员和职责为： 
1) 在运行维护服务中负责日常操作实施的人员； 
2) 根据规范和手册，执行运行维护服务各过程，并对其执行结果负责。</td><td style='text-align: center; word-wrap: break-word;'>a) 明确运维服务业务相关的岗位结构； 
b) 明确各类运维服务的岗位职责和任职资格要求。</td><td style='text-align: center; word-wrap: break-word;'>岗位职责说明对于岗位结构的覆盖率。</td></tr></table>

---

<div style="text-align: center;">表 2 (续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.4 知识</td><td style='text-align: center; word-wrap: break-word;'>a) 基础知识信息技术相关基础知识。b) 专业知识从事运行维护服务所必备的知识，应具有较为系统的内容体系和知识范围。如网络技术人员应具备网络专业整体的内容体系和知识。c) 综合知识与运行维护服务相关的企业和行业知识。</td><td style='text-align: center; word-wrap: break-word;'>能够识别运维服务业务所需要的基础知识、专业知识和综合知识，并采取措施使运维服务主要人员能够具备这些知识。</td><td style='text-align: center; word-wrap: break-word;'>。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.5 技能</td><td style='text-align: center; word-wrap: break-word;'>a) 确定运行维护服务人员在运行维护服务中所必备的能力；b) 要求运行维护服务人员具备从事相关运行维护服务的资格；c) 特殊环境运行维护服务人员应具备相关资格。</td><td style='text-align: center; word-wrap: break-word;'>a) 能够识别运维服务业务所需的资格要求和能力要求；b) 保障主要人员具备相关能力；c) 确保满足特殊环境运维服务人员的资格要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务业务有关的运维资格要求和能力要求；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.6 经验</td><td style='text-align: center; word-wrap: break-word;'>a) 运行维护服务人员应具备所从事运行维护服务活动的经验；b) 供方应具备一定的从事运行维护服务活动的经验。</td><td style='text-align: center; word-wrap: break-word;'>保障主要运维人员具备从事运维服务活动的经验。</td><td style='text-align: center; word-wrap: break-word;'>从事运行维护服务的平均年限。</td></tr></table>

### 5.3 资源要求

基本级的资源要求见表 3。

<div style="text-align: center;">表 3 基本级的资源要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.2 运维工具</td><td style='text-align: center; word-wrap: break-word;'>a) 监控工具，对运行维护服务对象进行数据的采集和监控，评估可能导致运行维护服务对象故障的因素； b) 过程管理工具，按照商定的 SLA 管理运行维护服务的交付过程，过程管理工具宜包括日常运行维护管理、记录、测量、监督和评估等功能； c) 专用工具，根据服务要求配备的安全工具和用于特殊要求的工具。</td><td style='text-align: center; word-wrap: break-word;'>必要时，在提供运维服务过程中能有效使用必要的监控工具，监控工具可以是用户的、也可以是自有的或第三方提供的。 必要时，在提供运维服务过程中能有效使用过程管理工具来管理运维服务过程，至少满足事件管理需求，过程管理工具可以是用户的、也可以是自有的或第三方提供的。 无要求。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<div style="text-align: center;">表 3 (续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.3 服务台</td><td style='text-align: center; word-wrap: break-word;'>a) 设置专门的沟通渠道作为与需方的联络点，沟通渠道可以是热线电话、传真、网站、电子邮箱等；b) 设定专人负责服务请求的处理；c) 针对沟通渠道整合服务过程，建立管理制度，包括服务请求的接收、记录、跟踪和反馈等机制，以及日常工作的监督和考核。</td><td style='text-align: center; word-wrap: break-word;'>a) 设置与需方的沟通渠道，有专人负责处理服务请求；b) 建立服务台管理制度。</td><td style='text-align: center; word-wrap: break-word;'>服务台管理制度；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.4 备件库</td><td style='text-align: center; word-wrap: break-word;'>a) 备件响应方式和级别定义，能够满足 SLA 所约定的备件支持；b) 备件供应商管理：能够规范备件的采购过程，对供应商进行选择和评价；c) 备件出入库管理：能够对入库备件进行标识，规范备件的使用和核销，备件物品的帐务管理；d) 备件可用性管理：能够定期对备件状态进行检测，以确保其功能满足运行维护需求。</td><td style='text-align: center; word-wrap: break-word;'>无要求。</td><td style='text-align: center; word-wrap: break-word;'>无。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.5 知识库</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应针对常见问题的描述、分析和解决方法建立知识库；b) 确保整个组织内的知识是可用的、可共享的；c) 组织应选择一种合适的知识管理策略；d) 知识库应具备知识的添加、更新和查询功能；e) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织对常见问题的描述、分析和解决方法进行归纳总结；b) 建立知识积累和使用的相关制度。</td><td style='text-align: center; word-wrap: break-word;'>a) 知识库内容和条目；b) 知识库管理制度。</td></tr></table>

### 5.4 技术要求

基本级的技术要求见表 4。

---

<div style="text-align: center;">表 4 基本级的技术要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.2 技术研发</td><td style='text-align: center; word-wrap: break-word;'>a) 根据业务和市场分析，制定研发规划，包括新技术和前沿技术的应用、技术储备等；b) 配备与规划相适应的研发环境；c) 配备与规划相适应的研发队伍。</td><td style='text-align: center; word-wrap: break-word;'>制定运维技术研发规划，并实际执行。</td><td style='text-align: center; word-wrap: break-word;'>运维技术研发计划文件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.3 与发现问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 具有信息采集和监控的手段；b) 具有诊断和分析问题的方法。</td><td style='text-align: center; word-wrap: break-word;'>a) 能够进行信息采集和监控；b) 具备诊断和分析问题的手段。</td><td style='text-align: center; word-wrap: break-word;'>a) 信息采集/监控相关的文档和操作手册；b) 问题诊断方案。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.4 与解决问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 解决问题的技术指标或标准；b) 解决问题的方案或手册；c) 测试环境、测试标准和方法。</td><td style='text-align: center; word-wrap: break-word;'>具有对故障和问题的解决办法，可包含解决方案、操作手册。</td><td style='text-align: center; word-wrap: break-word;'>解决问题方案或手册的可用性和使用便捷性。</td></tr></table>

### 5.5 过程要求

基本级的过程要求见表 5。

<div style="text-align: center;">表 5 基本级的过程要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9.2 服务级别管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务目录；
b) 与需方签订 SLA；
c) 根据需方的考核评估要求，建立 SLA 考核自评估机制，包括 SLA 完成情况、达成率；
d) 在 SLA 评估后制定改进内容及改进措施。</td><td style='text-align: center; word-wrap: break-word;'>a) 定义服务级别管理过程，与需方签订服务级别协议；
b) 定义服务目录。</td><td style='text-align: center; word-wrap: break-word;'>SLA 文件的可用性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9.3 服务报告</td><td style='text-align: center; word-wrap: break-word;'>a) 与服务报告过程一致的活动，包括建立、审批、分发、归档等；
b) 服务报告计划，包括提交方式、时间、需方接收对象等；
c) 服务报告模板，包括格式、提纲等。</td><td style='text-align: center; word-wrap: break-word;'>根据需方或供方的管理要求，提供服务报告。</td><td style='text-align: center; word-wrap: break-word;'>服务报告。</td></tr></table>

---

<div style="text-align: center;">表5(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.4 事件管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与事件管理过程一致的活动，包括事件受理、分类和初步支持、调查和诊断、解决、进展监控与跟踪、关闭等；b) 事件分类、分级机制；c) 事件升级机制；d) 满意度调查机制；e) 事件解决评估机制，包括事件解决率、事件平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>a) 建立事件管理过程文件及相关模板；b) 定义事件的分类、分级机制；c) 定义针对事件的满意度调查机制。</td><td style='text-align: center; word-wrap: break-word;'>a) 事件管理流程；b) 事件管理过程记录文档。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.5 问题管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与问题管理过程一致的活动，包括问题建立、分类、调查和诊断、解决、关闭等；b) 问题分类管理机制，包括问题的影响范围、重要程度、紧急程度并确定优先级；c) 问题导入知识库机制；d) 问题解决评估机制，包括问题解决率、问题平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>a) 建立问题管理过程文件及相关模板；b) 定义问题的分类、分级机制；c) 按照问题管理过程执行，并留下相应记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 问题管理流程；b) 问题管理过程记录文档。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.6 配置管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与配置管理过程一致的活动，包括识别、记录、更新和审核等；b) 配置数据库管理机制；c) 配置项审核机制。</td><td style='text-align: center; word-wrap: break-word;'>a) 建立配置管理过程文件及相关模板；b) 按照配置管理过程执行，并留下相应记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 配置管理流程；b) 配置管理过程记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.7 变更管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与变更管理过程一致的活动，包括请求、评估、审批、实施、确认和回顾等；b) 建立变更类型和范围的管理机制；c) 对变更完成情况进行统计分析，包括未经批准变更数量及占比、不同类型的变更数量及占比、不成功的变更数量及占比、取消的变更数量及占比、变更关联的配置数。</td><td style='text-align: center; word-wrap: break-word;'>a) 建立变更管理过程文件及模板；b) 依据变更管理过程执行，并留下相应记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 变更管理流程；b) 变更管理过程记录。</td></tr></table>

---

<div style="text-align: center;">表5(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.8 发布管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与发布管理过程一致的活动，包括规划、设计、建设、配置和测试等；b) 建立发布类型和范围的管理机制；c) 制定完整的方案，包括发布计划、回退方案、发布记录等；d) 对发布完成情况进行统计分析，包括发布成功率、发布及时率、是否更新配置管理数据库等。</td><td style='text-align: center; word-wrap: break-word;'>a) 建立发布管理过程文件及模板；b) 依据发布管理过程执行，并留下相应记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 发布管理流程；b) 发布管理过程记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.9 信息安全管理</td><td style='text-align: center; word-wrap: break-word;'>a) 符合相关法律法规的规定，满足需方对运行维护服务过程的信息安全需求和供方本身信息安全需求；b) 建立与信息安全管理过程一致的活动，包括识别、评估、处置和改进等。</td><td style='text-align: center; word-wrap: break-word;'>在运维服务过程中考虑供需双方信息安全的要求，建立信息安全管理制度。</td><td style='text-align: center; word-wrap: break-word;'>信息安全管理相关制度。</td></tr></table>

## 6 拓展级

### 6.1 管理要求

拓展级的管理要求见表 6。

---

<div style="text-align: center;">表 6 拓展级的管理要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="4">GB/T 28827.1-2012 5.2 策划</td><td style='text-align: center; word-wrap: break-word;'>a) 根据自身业务定位和能力，策划运行维护服务对象的服务内容与要求，并形成服务目录；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 制定服务目录的管理流程，包括服务目录管理的相关角色和职责，明确服务目录管理流程与其他流程的关系，如 SLA 等； b) 服务目录应包括服务列表，列表层次结构需符合 GB/T 29264-2012 的要求； c) 服务目录应包括服务产品的详细描述内容，如服务名称、服务简介、服务目标，以及服务对象、服务内容、服务频度、服务时间、交付方式、交付成果等； d) 建立起服务目录与运维服务业务的关联关系。</td><td style='text-align: center; word-wrap: break-word;'>服务目录规范性、符合性、完整性和适宜性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 依据组织的业务发展需要来建立组织结构和管理制度，支持服务目录的实施或实现；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 运维服务团队相对独立，并建立运维管理制度； b) 服务目录有实施保障措施。</td><td style='text-align: center; word-wrap: break-word;'>服务团队的独立性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 对人员、资源、技术和过程进行规划，建立相适应的指标体系和服务保障体系；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 组织应对组织级运维服务能力管理进行策划，围绕人员、资源、技术和过程四要素进行考虑，形成组织级运维服务能力管理计划； b) 组织应建立与能力策划相适应的能力指标体系； c) 建立能力管理计划和能力指标体系的考核方法及考核准则。</td><td style='text-align: center; word-wrap: break-word;'>a) 能力管理计划的适宜性和完整性； b) 能力指标体系的适宜性和完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 策划如何管理、审核并改进服务质量，建立内部审核评估机制。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 建立内部审核评估机制； b) 策划内部审核评估，明确审核评估团队及审核周期； c) 内部审核评估计划应覆盖运维业务相关部门及项目层。</td><td style='text-align: center; word-wrap: break-word;'>a) 内部审核机制的规范性； b) 内部审核评估计划的覆盖范围。</td></tr></table>

---

<div style="text-align: center;">表 6（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="4">GB/T 28827.1-2012 5.3 实施</td><td style='text-align: center; word-wrap: break-word;'>a) 制定满足整体策划的实施计划，并按计划实施；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 实施计划/方案应覆盖四要素，包括具体的任务、责任人、日程安排以及预期的目标或结果； b) 管理实施记录以验证实施过程与实施计划的一致性。</td><td style='text-align: center; word-wrap: break-word;'>实施计划的合理性；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 建立与需方的沟通协调机制；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 识别与需方沟通的干系人； b) 建立与需方有效的沟通渠道，如定期访谈、邮件等； c) 建立组织级与需方的沟通制度。</td><td style='text-align: center; word-wrap: break-word;'>沟通协调机制的完整性、适宜性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 按照服务能力要求实施管理活动并记录，确保服务能力管理和服务过程实施可追溯，服务结果可计量或可评估；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： 按照服务能力管理实施计划进行实施，做好过程监督考核，重点关注运维服务能力管理计划落实的相关记录。</td><td style='text-align: center; word-wrap: break-word;'>实施记录的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 提交满足质量要求的交付物。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 能力管理过程中的交付物满足能力质量要求； b) 服务过程中的交付物满足服务质量要求。</td><td style='text-align: center; word-wrap: break-word;'>交付物的完整性和符合性。</td></tr><tr><td rowspan="3">GB/T 28827.1-2012 5.4 检查</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审服务过程及相关管理体系，以确保服务能力的适宜性和有效性；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 组织定期评审，并保存评审记录，如评审检查表、服务过程及管理体系评审记录、内审记录等； b) 依据评审结果形成评审报告； c) 评审应覆盖全部运维服务业务。</td><td style='text-align: center; word-wrap: break-word;'>a) 评审检查表对标准条款的覆盖范围； b) 评审报告的完整性； c) 评审发现的有效问题数。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 调查需方满意度，并对服务能力策划实施的结果进行统计分析；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 调查需方满意度，检查运维服务能力管理计划的实施效果； b) 制定客户满意度管理制度； c) 跟踪监督运维服务能力管理计划及实施计划执行情况，并保存跟踪监督记录及效果反馈； d) 满意度调查结果形成相关报告，内容应包括满意度指标、计算方法、分析结果等。</td><td style='text-align: center; word-wrap: break-word;'>满意度调查制度的完整性、适宜性和有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 检查各项指标达成情况。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： 检查能力指标体系中相关指标的落实情况，并保存记录。</td><td style='text-align: center; word-wrap: break-word;'>能力指标的达成情况。</td></tr></table>

---

<div style="text-align: center;">表6（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="4">GB/T 28827.1-2012 5.5 改进</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务能力管理改进机制;</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 建立运维服务能力管理改进机制； b) 运维服务能力管理改进机制至少包括改进流程、改进策略，以及对发现的问题和不符合项处理的相关制度； c) 运维服务能力管理计划的跟踪监督应与内审和管理评审相结合。</td><td style='text-align: center; word-wrap: break-word;'>改进机制的适宜性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 对不符合策划要求的行为进行总结分析；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 对不符合策划要求的行为进行总结分析； b) 对运维服务能力管理实施计划的执行有偏差的部分进行总结分析； c) 对不符合项进行总结分析； d) 有预防与纠正措施的记录。</td><td style='text-align: center; word-wrap: break-word;'>对不符合项总结分析的有效性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 对未达成的指标进行调查分析；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： 对未达成的指标进行调查分析，并形成报告或记录。</td><td style='text-align: center; word-wrap: break-word;'>对未达成指标分析的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 根据分析结果确定改进措施，制定服务能力改进计划。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求： a) 根据分析结果确定改进措施，制定服务能力改进计划； b) 服务能力改进计划至少有能力改进项、改进目标、改进进度、责任人等； c) 保存运维服务能力管理改进过程相关记录，如改进实施方案、改进进展报告等。</td><td style='text-align: center; word-wrap: break-word;'>a) 纳入改进计划的改进机会； b) 服务能力改进计划。</td></tr></table>

---

### 6.2 人员要求

拓展级的人员要求见表 7。

<div style="text-align: center;">表 7 拓展级的人员要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="5">GB/T 28827.1-2012 6.2 人员管理</td><td style='text-align: center; word-wrap: break-word;'>a) 人员储备</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 制定人员储备管理文件及相关计划、b) 制定工作交接规范，并保存人员变更记录；c) 人员储备机制及人员储备计划需满足当前运维业务要求；d) 具备足够的人员，并满足当前运维业务需求。</td><td rowspan="5">a) 人员储备机制的适宜性；b) 人员培训体系满足运维业务的有效性；c) 人员绩效考核机制的适宜性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 人员培训</td><td rowspan="2">除达到四级要求外，还应满足以下要求：a) 制定培训管理制度、保存培训记录，如培训需求、培训计划、培训课程体系及教材/课件、培训实施记录、培训效果评价；b) 培训体系或机制与运维业务相匹配；c) 识别各岗位、各级别培训要求，制定培训计划，培训内容包括管理、技术、操作及综合知识等；d) 建立培训绩效评价机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>供方应建立运行维护服务相关的培训体系或机制，在制定培训时应识别培训要求，并提供及时和有效的培训。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核</td><td rowspan="2">除达到四级要求外，还应满足以下要求：a) 制定绩效管理办法，建立考核体系，考核体系应与运维业务相匹配；b) 根据不同岗位制定具体的、差异化的考核指标。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>供方应建立运行维护服务相关的绩效考核体系或机制，并能够有效组织实施。</td></tr></table>

---

<div style="text-align: center;">表7（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">GB/T 28827 运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.3 岗位结构</td><td style='text-align: center; word-wrap: break-word;'>a) 管理岗人员和职责为: 1) 在运行维护服务中负责管理运行维护服务; 2) 与需方建立顺畅的沟通渠道, 准确地将需方的需求传递到运维团队; 3) 规划、检查运行维护服务的各个过程, 对运行维护服务的策划、实施、检查、改进的范围、过程、信息安全和成果负责。 b) 技术支持岗人员和职责为: 1) 在运行维护服务中负责技术支持, 包括网络、操作系统、数据库、中间件、应用开发、硬件、集成、信息安全等; 2) 对运行维护服务过程中的请求、事件和问题做出响应, 保障信息安全并对处理结果负责。 c) 操作岗人员和职责为: 1) 在运行维护服务中负责日常操作的实施; 2) 根据规范和手册, 执行运行维护服务各过程, 并对其执行结果负责。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外, 还应满足以下要求: a) 具备完整的岗位职责说明; b) 岗位设置和要求与业务和服务目录相匹配; c) 岗位职责得到有效的执行。</td><td style='text-align: center; word-wrap: break-word;'>a) 岗位职责说明的完整性; b) 岗位职责执行的有效性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.4 知识</td><td style='text-align: center; word-wrap: break-word;'>a) 基础知识与信息技术相关的基本知识。 b) 专业知识从事运行维护服务所必备的知识, 应具有较为系统的内容体系和知识范围, 如网络技术人员应具备网络专业整体的内容体系的知识。 c) 综合知识与运行维护服务相关的组织和行业知识。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外, 还应满足以下要求: a) 建立运维相关的知识体系或培训课程体系, 包括运维基础、针对运维对象的专业知识与行业知识; b) 知识体系应对不同类别和级别的岗位提出相应的知识要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 掌握相关知识的证明文件或专业认证证书; b) 符合要求的人员数量及比例。</td></tr></table>

---

<div style="text-align: center;">表7（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.5 技能</td><td style='text-align: center; word-wrap: break-word;'>a) 确定运行维护服务人员在运行维护服务中所必备的能力；b) 要求运行维护服务人员具备从事相关运行维护服务的资格；c) 特殊环境运行维护服务人员应具备相关资格。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 制定运维人员技能级别规范，保存从业资格证书；b) 人员技能与服务目录匹配；c) 建立人员技能评价体系，人员技能与岗位要求匹配，保存技能评价记录；。</td><td style='text-align: center; word-wrap: break-word;'>a) 运行维护服务人员技能评价体系的适宜性；b) 具备相关行业、专业资格人员的数量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.6 经验</td><td style='text-align: center; word-wrap: break-word;'>a) 运行维护服务人员应具备所从事运行维护服务活动的经验；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 建立人员履历、培训及其管理的相关制度；b) 人员经验与业务需求匹配，如项目人员分配，岗位职责等。</td><td style='text-align: center; word-wrap: break-word;'>运维人员主持或参与运行维护服务项目的项目数量、项目金额、项目规模以及在项目中的角色作用等。</td></tr></table>

### 6.3 资源要求

拓展级的资源要求见表 8。

<div style="text-align: center;">表 8 拓展级的资源要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.2 运维工具</td><td style='text-align: center; word-wrap: break-word;'>a) 监控工具，对运行维护服务对象进行数据的采集和监控，评估可能导致运行维护服务对象故障的因素；b) 过程管理工具，按照商定的 SLA 管理运行维护服务的交付过程，过程管理工具宜包括日常运行维护管理、记录、测量、监督和评估等功能；c) 专用工具，根据服务要求配备的安全工具和用于特殊要求的工具。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：使用运维工具对运维对象进行数据采集和监控，并重点关注以下方面：a) 自有运维工具有著作权登记证书或外购工具合同；b) 运维工具至少应具有对服务结果和过程进行分析的功能；c) 运维工具有操作手册，并对使用效果进行自评估，保存自评估报告；d) 工具应具备权限设置功能。</td><td style='text-align: center; word-wrap: break-word;'>a) 与工具功能匹配的使用手册；b) 工具使用日志记录等；c) 工具的使用效果自评估报告；d) 工具应具备权限设置功能。</td></tr></table>

---

<div style="text-align: center;">表8（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 7.3 服务台</td><td style='text-align: center; word-wrap: break-word;'>a) 设置专门的沟通渠道作为与需方的联络点，沟通渠道可以是热线电话、传真、网站、电子邮箱等；b) 设定专人负责服务请求的处理；</td><td rowspan="2">除达到四级要求外，还应满足以下要求：建立、使用和管理服务台，并重点关注以下方面：a) 制定服务台的职能说明、服务台管理制度、服务流程、操作手册，并保存用户评价记录；b) 建立服务请求的流程，包括服务请求的操作规程、跟踪和反馈方法；c) 建立用户评价记录产生的流程、主要内容、评价结果与考核的关系；d) 监督管理服务台的日常工作。</td><td rowspan="2">a) 日常工作记录的完整性；b) 用户评价记录的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 针对沟通渠道整合服务过程，建立管理制度，包括服务请求的接收、记录、跟踪和反馈等机制，以及日常工作的监督和考核。</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 7.4 备件库</td><td style='text-align: center; word-wrap: break-word;'>a) 备件响应方式和级别定义，能够满足SLA所约定的备件支持；b) 备件供应商管理：能够规范备件的采购过程，对供应商进行选择和评价；c) 备件出入库管理：能够对入库备件进行标识，规范备件的使用和核销，备件物品的帐务管理；</td><td rowspan="2">根据服务目录及服务级别协议，对于其中明确要求提供备品备件的，应建立备件库，并要求：a) 制定备件库管理规范，包括：备件响应方式和级别定义、备品备件的数量和类型、类别与编码、存放环境，以上内容均能够满足SLA所要求的备件支持；b) 制定备件采购计划或方案，包括采购人员职责、采购流程、库存策略、紧急采购预案等。制定供应商管理制度，至少每年对供应商进行一次评估；c) 制定出入库制度，包括送货、验收、入库、出库等的流程，并实施，具有备件库存管理的记录或报告；d) 制定备件的检测、报废制度，能定期对备件状态进行检测，以确保其功能满足运维需求。对涉及国家强制规定检定设备须送专业机构检测并获得检测报告。</td><td rowspan="2">a) 备件库信息完整性、准确性和真实性；b) 备件管理规范的适用性；c) 备件库出入库管理制度的适用性；d) 备件可用率。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 备件可用性管理：能够定期对备件状态进行检测，以确保其功能满足运行维护需求。</td></tr></table>

---

<div style="text-align: center;">表8（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 7.5 知识库</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应针对常见问题的描述、分析和解决方法建立知识库；b) 确保整个组织内的知识是可用的、可共享的；c) 组织应选择一种合适的知识管理策略；d) 知识库应具备知识的添加、更新和查询功能；</td><td rowspan="2">除达到四级要求外，还应满足以下要求：建立、管理和使用知识库，并重点关注以下方面：a) 知识库内容至少应包括针对已知错误和问题的描述、分析和解决方法；b) 知识库可共享给整个组织，并提供有效方式访问方式；c) 具有知识管理策略，包括知识来源、类别、共享范围、更新升级、传播方式等。d) 制定知识库使用手册，并保留知识维护记录（添加、更新等）；e) 制定知识管理和使用制度，对知识库进行生命周期管理，知识管理的角色应落实到具体人员。</td><td rowspan="2">a) 知识库的覆盖范围；b) 知识库的可用性和有效性；c) 入库管理和审批记录的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>e) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。</td></tr></table>

### 6.4 技术要求

拓展级的技术要求见表 9。

<div style="text-align: center;">表 9 拓展级的技术要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012
8.2 技术研发
c) 配备与规划相适应的研发队伍。</td><td style='text-align: center; word-wrap: break-word;'>a) 根据业务和市场分析，制定研发规划，包括新技术和前沿技术的应用、技术储备等；
b) 配备与规划相适应的研发环境；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：制定详细的运维服务技术研发规划并得到实施，重点关注以下方面：
a) 运维技术研发应与业务发展匹配；
b) 根据业务及市场分析，制定研发规划文件，规划文件应包括当前技术的发展动态分析、拟关注的重点方向、拟研发的技术与业务的关联程度等内容；
c) 研发规划得到实施，具备与规划相适应的研发组织结构和人员数量、研发经费投入、研发环境以及研发成果等。</td><td style='text-align: center; word-wrap: break-word;'>a) 研发投入经费；
b) 研发成果数量；
c) 技术研发规划文件内容的完整性。</td></tr></table>

---

<div style="text-align: center;">表9（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8.3 与发现问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 具有信息采集和监控的手段:</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求:拥有与发现问题相关的技术，并重点关注以下方面:a) 拥有核心的运维服务工具，为运维数据的信息采集、监控提供支撑，并配备信息采集和监控技术的说明文件；b) 对问题的诊断和分析有较完备的流程体系，例如能够借助知识库解决问题等;c) 有效利用诊断方案和分析手册。</td><td style='text-align: center; word-wrap: break-word;'>a) 信息采集手段的可用性和使用便捷性;b) 诊断方案或手册的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8.4 与解决问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 解决问题的技术指标或标准;b) 解决问题的方案或手册;</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求:拥有与解决问题相关的技术，并重点关注以下方面:a) 建立系统/设备处于正常状态的指标体系;b) 有测试环境、测试标准和方法;c) 有典型故障和问题的解决方案和操作手册，并得到有效利用。</td><td style='text-align: center; word-wrap: break-word;'>a) 解决问题的技术指标或标准的有效性;b) 测试环境与需方运行维护环境的匹配度;c) 测试标准和方法的有效性。</td></tr></table>

### 6.5 过程要求

拓展级的过程要求见表 10。

---

<div style="text-align: center;">表 10 拓展级的过程要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.2 服务级别管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务目录；b) 与需方签订 SLA；c) 根据需方的考核评估要求，建立 SLA 考核自评估机制，包括 SLA 完成情况、达成率；d) 在 SLA 评估后制定改进内容及改进措施。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：确保供方定义、签订和管理 SLA，满足需方对服务质量的要求，并重点关注以下方面：a) 建立 SLA 考核自评估机制，具有服务级别协议的执行绩效跟踪记录，如 SLA 完成情况、达成率、用户反馈等，在评估后制定改进内容及改进措施；b) 服务级别协议中应包含量化指标，如响应时间、解决问题的时间等。</td><td style='text-align: center; word-wrap: break-word;'>a) 签订 SLA 文件的规范性；b) SLA 考核评估机制的有效性和完整性；c) SLA 执行的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.3 服务报告</td><td style='text-align: center; word-wrap: break-word;'>a) 与服务报告过程一致的活动，包括建立、审批、分发、归档等；b) 服务报告计划，包括提交方式、时间、需方接收对象等；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 制定服务报告的管理规范，并对服务报告内容、产生频次、审核要求、传播和保存等做出说明；b) 服务报告内容应完备，至少包括运维服务相关的基本要素，如与 SLA 相对的服务绩效、满意度分析、工作量、重大事件后的性能分析、趋势分析、未达标的内容和事件，并针对不同运维服务内容提供服务报告模板；c) 及时跟进和解决服务报告中提出的问题；d) 服务报告计划需满足 SLA 的约定或供方的制度。服务报告计划可多种形式；e) 服务报告应进行有效的分类。</td><td style='text-align: center; word-wrap: break-word;'>a) 服务报告管理过程的规范性；b) 服务报告的完整性、及时性和准确性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.4 事件管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与事件管理过程一致的活动，包括事件受理、分类和初步支持、调查和诊断、解决、进展监控与跟踪、关闭等；b) 事件分类、分级机制；c) 事件升级机制；d) 满意度调查机制；</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 具备事件管理工具，制定事件记录模板，保存事件记录、事件回访记录和事件管理报告；b) 建立事件或故障分类分级机制，并保持与组织业务相适应。c) 建立事件升级机制；d) 建立事件评估机制，包括事件解决率、事件平均解决时间等。等</td><td style='text-align: center; word-wrap: break-word;'>a) 事件管理过程的完整性、有效性；b) 事件解决评估机制的有效性；c) 事件升级机制的有效性。</td></tr></table>

---

<div style="text-align: center;">表10(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.5 问题管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与问题管理过程一致的活动，包括问题建立、分类、调查和诊断、解决、关闭等；b) 问题分类管理机制，包括问题的影响范围、重要程度、紧急程度并确定优先级；c) 问题导入知识库机制；d) 问题解决评估机制，包括问题解决率、问题平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 建立与问题管理过程一致的活动，包括问题建立、分类、调查和诊断、关闭等；b) 建立有效的问题解决评估机制，包括问题解决率、问题平均解决时间等；c) 有支撑问题管理活动和结果的问题记录文档、问题管理报告等，并与知识库关联。</td><td style='text-align: center; word-wrap: break-word;'>a) 问题管理过程的完整性；b) 问题解决评估机制有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.6 配置管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与配置管理过程一致的活动，包括识别、记录、更新和审核等；b) 配置数据库管理机制；c) 配置项审核机制。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：a) 建立与业务相适应的配置管理数据库；b) 建立配置管理规范、配置管理数据库管理规范、配置管理记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 配置管理活动的完整性；b) 配置数据的准确、完整、有效、可用和可追溯；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.7 变更管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与变更管理过程一致的活动，包括请求、评估、审批、实施、确认和回顾等；b) 建立变更类型和范围的管理机制；c) 对变更完成情况进行统计分析，包括未经批准变更数量及占比、不同类型的变更数量及占比、不成功的变更数量及占比、取消的变更数量及占比、变更关联的配置数。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：供方通过管理、控制变更的过程，确保变更有序实施。供方应根据变更管理的过程要求，实现以下方面：a) 定义变更类型，建立变更范围管理机制，明确变更审批负责人或变更审批委员会；b) 制定变更管理规范，保存变更管理记录，包括变更申请单、审批记录、变更管理报告等；</td><td style='text-align: center; word-wrap: break-word;'>a) 变更管理过程的完整性；b) 变更记录的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.8 发布管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与发布管理过程一致的活动，包括规划、设计、建设、配置和测试等；b) 建立发布类型和范围的管理机制；c) 制定完整的方案，包括发布计划、回退方案、发布记录等；d) 对发布完成情况进行统计分析，包括发布成功率、发布及时率、是否更新配置管理数据库等。</td><td style='text-align: center; word-wrap: break-word;'>除达到四级要求外，还应满足以下要求：制定发布管理规范，保存发布过程记录，包括：发布计划、测试方案、回退方案、发布记录、发布评估报告等。</td><td style='text-align: center; word-wrap: break-word;'>a) 发布管理过程的完整性；b) 发布过程记录的完整性。</td></tr></table>

---

<div style="text-align: center;">表10（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 9.9 信息安全管理</td><td style='text-align: center; word-wrap: break-word;'>a) 符合相关法律法规的规定，满足需方对运行维护服务过程的信息安全需求和供方本身信息安全需求；</td><td rowspan="2">除达到四级要求外，还应满足以下要求：供方应建立运行维护服务过程中的信息安全管理过程，并重点关注以下方面：a) 建立信息安全管理过程，包括安全方针、策略等，并对信息安全风险进行识别、评估、处置和改进，形成相关记录；如信息安全控制措施及风险评估记录、实施记录等；b) 建立与组织业务相适应的信息安全事件处理流程。</td><td rowspan="2">a) 信息安全培训的有效性；b) 信息安全事件处理记录的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 建立与信息安全管理过程一致的活动，包括识别、评估、处置和改进等。</td></tr></table>

## 7 改进（协同）级

### 7.1 管理要求

改进（协同）级的管理要求见表 11。

---

<div style="text-align: center;">表 11 改进（协同）级的管理要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="4">5.2 策划</td><td style='text-align: center; word-wrap: break-word;'>a) 根据自身业务定位和能力，策划运行维护服务对象的服务内容与要求，并形成服务目录；</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 服务目录符合企业的运维服务业务定位和能力，与企业的组织结构、人员的岗位职责、经验等相匹配；b) 建立服务目录的更新制度和方法，在企业组织级和项目级设置服务目录管理的岗位职责，定期对服务目录与企业业务服务对象的符合度进行评估，并对服务目录进行更新。</td><td rowspan="4">a) 服务目录与实际业务的匹配度；b) 服务目录与组织架构及岗位设置的匹配度；c) 与业务匹配的服务产品化过程；d) 将应急处置纳入服务策划和组织设置中；e) 服务策划覆盖的全面性，如服务交付策划、能力管理策划、质量管理策划。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) _依据组织的业务发展需要来建立组织结构和管理制度，支持服务目录的实施或实现；</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 应定期根据组织的业务发展需要对组织架构和管理制度进行策划和完善，并根据策划结果对企业组织架构和管理制度进行优化；b) 策划活动应由组织的运维交付、质量管理、人力资源管理、技术研发等部门共同参与；c) 策划活动的结果要与服务目录相匹配，策划结果包括对组织级的服务目录进行修订；d) 策划过程和根据策划对企业组织架构和管理制度的优化过程要留下记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 对人员、资源、技术和过程进行规划，建立相适应的指标体系和服务保障体系；</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 依据标准制定完善的运维服务能力管理计划和管理制度；b) 建立完善的运维服务能力管理指标体系和管理制度，具有明确的量化指标，包括组织能力指标考评、服务项目管理考评、服务交付指标等方面；c) 建立服务保障体系，具有保障制度、岗位设置和匹配岗位的人员技术能力；d) 以上各种管理制度、指标体系、保障体系的建立应由企业的运维交付、质量管理、人力资源管理、技术研发等部门共同参与完成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 策划如何管理、审核并改进服务质量，建立内部审核评估机制。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 建立服务质量管理体系，包括服务质量管理要求、服务质量审核机制和服务改进机制；b) 有专职质量管理岗位、有明确的岗位职责和人员配备；c) 质量管理体系的建立与实施需由企业的运维交付、质量管理、人力资源管理、技术研发等部门共同参与；d) 根据业务发展定期对服务质量管理体系优化改进。</td></tr></table>

---

<div style="text-align: center;">表11(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 5.3 实施</td><td style='text-align: center; word-wrap: break-word;'>a) 制定满足整体策划的实施计划，并按计划实施；b) 建立与需方的沟通协调机制；c) 按照服务能力要求实施管理活动并记录，确保服务能力管理和服务过程实施可追溯，服务结果可计量或可评估；</td><td rowspan="2">除达到三级要求外，还应满足以下要求：a) 根据整体策划制定组织级和项目级的实施计划，有关键的时间点、人员分工和交付物要求；b) 建立与需方的沟通协调机制，在岗位职责中明确沟通职责，并保留沟通记录；c) 按照服务能力策划实施管理活动，确保服务能力管理和服务过程实施可追溯，服务结果可计量或可评估；d) 实施后进行总结评估和改进；e) 应对实施情况及指标完成情况进行总结分析和优化改善，应考虑运维工作涵盖的各个方面，包括但不限于管理、资源、人员、技术、过程、交付、应急等，注重运维能力管理的全面发展。</td><td rowspan="2">a) 服务实施计划与实际执行情况的偏差；b) 服务实施过程的可追溯性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 提交满足质量要求的交付物。</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 5.4 检查</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审服务过程及相关管理体系，以确保服务能力的适宜性和有效性；b) 调查需方满意度，并对服务能力策划实施的结果进行统计分析；</td><td rowspan="2">除达到三级要求外，还应满足以下要求：a) 有独立的部门或人员负责服务质量检查工作，并具备承担该工作的能力，掌握服务能力管理知识，掌握本企业服务质量管理体系；b) 按照制度或要求对实施过程的执行和实施结果进行监测、评审并记录，保留记录文档；c) 对检查结果进行分析评估，提供持续改进建议。各项检查结果作为服务改进、服务管理计划和体系改进的输入项，并得到运用；d) 对所有管理文档、分析报告和过程实施记录进行管理。</td><td rowspan="2">a) 运维能力检查对服务交付的支撑作用和正面效果；b) 检查的计划性、全面性和有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 检查各项指标达成情况。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.5 改进</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务能力管理改进机制；b) 对不符合策划要求的行为进行总结分析；c) 对未达成的指标进行调查分析；d) 根据分析结果确定改进措施，制定服务能力改进计划。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 对改进过程进行监控管理；宜保留所有管理文档、分析报告和过程实施记录；b) 运维服务能力管理改进结果应与服务目录、人员、工具、技术、过程的持续改进相匹配。</td><td style='text-align: center; word-wrap: break-word;'>服务改进活动的持续性。</td></tr></table>

---

<div style="text-align: center;">表11(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.2 交付策划</td><td style='text-align: center; word-wrap: break-word;'>根据需方需求和供方自身能力，双方协商签署服务级别协议；供方做好必要的交付准备，制定交付计划，确保服务正常提供。</td><td style='text-align: center; word-wrap: break-word;'>a) 与需方签署服务级别协议；b) 服务级别协议应包括服务目标、服务范围、服务级别量化指标、服务交付物、服务交付方式、服务资源配备等信息；c) 与需方签署的服务级别协议应准确体现需方需求；d) 建立有效的评估方法，以评估服务级别达成情况；e) 制定服务交付计划，包括实施计划、检查计划和改进计划；f) 建立并完善服务交付管理机制，包括人员管理、资源管理、技术管理、过程管理、客户沟通管理、质量管理、预算管理、风险控制管理、应急管理等；g) 明确和规范关键服务的交付记录；h) 交付前应配备服务交付相关资源，包括人员、工具软件、知识库、备件库、服务台、预算等；i) 识别服务交付风险和需方安全需求，制定安全管理机制和风险规避计划，建立风险清单，制定和实施风险应对计划。</td><td style='text-align: center; word-wrap: break-word;'>a) 量化后的SLA在实际项目中的覆盖率；b) SLA量化的完整性和合理性；c) SLA与服务交付计划的对应关系；d) 服务交付计划内容的完整性；e) 将应急响应要求纳入服务交付计划。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.3 交付实施</td><td style='text-align: center; word-wrap: break-word;'>供方按照交付策划向需方提供运行维护服务，完成服务级别协议规定内容。</td><td style='text-align: center; word-wrap: break-word;'>a) 按照交付策划要求，交付服务；b) 宜采用自动化工具，准确、及时对服务过程进行记录；c) 及时与需方沟通，准确向需方报告服务级别协议达成情况；d) 向需方报告服务交付情况；e) 处理用户投诉；f) 实施风险规避计划；g) 实施过程中统计运维人员、资源、过程、技术及SLA达成情况，对需要完善的方面及时改进。</td><td style='text-align: center; word-wrap: break-word;'>a) 服务交付计划与实际执行情况的偏差；b) 服务实施过程的可追溯性；c) 服务交付结果的量化分析及与需方的沟通机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.4 交付检查</td><td style='text-align: center; word-wrap: break-word;'>供需双方通过交付策划与交付实施的对比检查，确认完成情况，并对发现的问题提出改进建议。</td><td style='text-align: center; word-wrap: break-word;'>a) 依据交付策划的内容，检查服务交付实施情况；b) 评估服务级别协议达成情况；c) 宜采取独立方式审计交付计划的实施情况；d) 宜采取独立方式审计交付过程的合规性，且宜保证一定量的审计频率；f) 调查需方的满意度，并对需方满意度进行评估分析；h) 保证一定的满意度调查范围；i) 检查与评估风险规避计划的实施情况。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付检查与SLA及服务交付计划的相关性；b) 服务交付检查活动对于改善服务交付计划和实施过程的作用。</td></tr></table>

---

<div style="text-align: center;">表11(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">GB/T 28827 标准</td><td rowspan="2">标准条款要求</td><td colspan="3">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.5 交付改进</td><td style='text-align: center; word-wrap: break-word;'>供方通过对交付各过程的总结分析，提出建议并改进，以提高效率，提升需方满意度。</td><td style='text-align: center; word-wrap: break-word;'>a) 分析服务交付过程，提出和实施改善建议；b) 分析和改善未达成服务级别协议情况；c) 分析和改善用户投诉情况；d) 分析和改善用户不满意情况；e) 分析服务过程，改善服务交付，挖掘服务价值；f) 建立供方内部主动服务改进机制，跟踪服务改善情况；g) 依据风险评估情况，更新风险清单和风险规避计划。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付改进活动的有效性；b) 交付改进活动的持续性。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.2 例行操作</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供日常的预定服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 针对例行操作应有日常工作计划，至少包括：例行操作的交付目标、内容、范围、周期和人员安排；b) 应配套相关的指导手册，至少包括：任务清单、各项任务的操作步骤及说明、运行状态是否正常的判定标准、运行状态信息的记录要求、异常状况处置流程（角色定义、处置方法、流转过程、结束要求）、报告模版。以上文档内容需保持及时更新；c) 采用高效率、低误差的例行操作模式，必要时采用自动化巡检；d) 例行操作的数据及时归档，且便于查询。</td><td style='text-align: center; word-wrap: break-word;'>a) 例行操作的计划及配套手册；b) 例行操作活动的过程可追溯性。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.3 响应支持</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供服务请求或故障申报的即时服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 应公示多种受理响应支持的渠道。包括：电话、传真、邮件或网络方式；b) 与需方明确服务承诺，包括：工作时间、响应时间；c) 与需方就响应级别、报警升级条件等内容达成共识；d) 响应支持活动的记录过程至少应包括以下活动：分类、分发、处理、升级、转派、关闭。采用自动化平台提高效率，对记录增、改、删实行权限控制；e) 对响应支持进行优先级定义；f) 制定多途径、高效的沟通机制；g) 在需方同意的情况下，由供方负责人确认后结束响应支持。</td><td style='text-align: center; word-wrap: break-word;'>a) 响应支持活动的过程可追溯性；b) 响应支持活动的结果分析；c) 响应支持活动的异常处理及沟通机制。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.4 优化改善</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供服务请求或故障申报的即时服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 编写优化改善方案，方案中宜包含：目标、内容、步骤、人员、预算、进度、考核指标、风险预案和回退方案；b) 优化改善后应有观察期，应有评审和总结；c) 依靠数据积累，通过建立基线和优化改善后的比较，量化指标确保服务的效果。</td><td style='text-align: center; word-wrap: break-word;'>a) 优化改善活动的计划性；b) 优化改善活动的效果测量。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<div style="text-align: center;">表11(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">GB/T 28827 运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.5 调研评估</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供对运行维护服务对象的调查研究或分析评价，给出报告或建议等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 在调研评估开展前提供计划，包括目标、内容、步骤、人员、预算、进度、交付成果和沟通计划等；b) 评估报告中应包含现状、需求、过程和建议等内容；c) 调研评估后应跟踪落地效果偏差，并且有内部评审或需方评审；d) 必要时可依靠自动化平台，获取有效数据支撑。</td><td style='text-align: center; word-wrap: break-word;'>a) 调研评估活动的计划性；b) 调研评估活动的效果测量。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 7.2 现场交付</td><td style='text-align: center; word-wrap: break-word;'>供方通过现场支持的方式为需方提供服务，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付各阶段所要完成的工作和要求应在规定的时间内告知工程师和客户，并在必要时得到确认，包括任务清单、达成目标、时间周期、风险预估和管理要求；b) 应具备交付任务发布/接受、远程指导、交付成果上传、知识库查询、服务质量及时评价等提高交付效率的手段；c) 对交付过程进行量化的数据统计分析，如服务时间、SLA达成情况、风险发生概率和影响、满意度等。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付方式的多样性；b) 交付方式与服务级别协议要求的一致性；c) 交付记录的完整性。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.2 交付成果管理</td><td style='text-align: center; word-wrap: break-word;'>供方在提供运行维护服务交付的过程中，通过向需方提供无形的（如状态恢复、性能提升等）或有形的（如过程记录、服务报告、现场备件等）交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 主要成果可自动及时获取；b) 成果应有生命周期管理，对成果的访问编辑安全可控。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付成果的完整性；b) 交付成果对SLA要求的满足程度；c) 交付成果的全生命周期管理，包括交付成果的准备、审核、交付、存档、传播、复用及废弃等。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.3 例行操作成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供例行操作服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 成果应涵盖运维服务对象的健康状况；b) 成果应包括相关业务信息健康记录、风险管控建议、性能趋势预判、历史数据挖掘等。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付成果的完全周期管理，包括交付成果的准备、审核、交付、存档、传播、复用及废弃等。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.4 响应支持成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供响应支持服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 成果应涵盖运维服务对象的可用性、连续性状况；b) 成果应包括相关业务信息可用连续性记录、应急预案及执行报告、客户满意度情况等。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付成果的完全周期管理，包括交付成果的准备、审核、交付、存档、传播、复用及废弃等。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.5 优化改善成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供优化改善服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 成果应涵盖运维服务对象的性能、功能状况；b) 成果应包括相关业务信息性能记录、容量计划、功能升级方案及实施效果总结等。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付成果的完全周期管理，包括交付成果的准备、审核、交付、存档、传播、复用及废弃等。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.6 调研评估成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供调研评估服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 成果应涵盖信息技术和业务的发展趋势；b) 成果应包括相关业务趋势信息、信息技术和业务的框架建议、重大技术变革研究等。</td><td style='text-align: center; word-wrap: break-word;'>a) 交付成果的完全周期管理，包括交付成果的准备、审核、交付、存档、传播、复用及废弃等。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<div style="text-align: center;">表 11（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.1 应急响应组织</td><td style='text-align: center; word-wrap: break-word;'>运行维护服务的组织由相关利益方组成，包括服务需方、服务供方、分包方、供应商等。应在运行维护服务组织基础上建立应急响应组织。</td><td style='text-align: center; word-wrap: break-word;'>应在运行维护服务组织基础上建立应急响应组织，要求如下：a) 应急响应组织的人员应包含运行维护服务组织的人员；b) 应急响应组织由相关利益方组成，包括服务需方、服务供方、分包方、供应商等；c) 应规定运行维护服务及应急响应所有相关利益方的角色及职责；d) 应急响应服务的范围、要求等应与相关利益方达成一致，确定沟通流程和方式，并形成记录；e) 将应急响应组织统一纳入运维管理组织内。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急组织与应急响应服务的一致对应；b) 应急组织与运维管理组织的关联关系。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.2 应急响应制度</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应制度，明确应急响应的目标、原则、范围以及各项管理制度，并要求：a) 与相关利益方就应急响应制度达成一致；b) 定期对应急响应制度进行评审；c) 在组织战略、业务流程、需方要求等发生重大变化时对应急响应制度进行调整。</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应制度，要求：a) 明确应急响应的目标、原则、范围以及各项管理制度；b) 与相关利益方就应急响应制度达成一致。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急响应制度的完整性、合理性；b) 应急响应制度的传播和宣贯机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.3 风险评估和改进</td><td style='text-align: center; word-wrap: break-word;'>组织应按照确定的方法和流程对重要信息系统实施风险评估，确保组织了解其在运行维护过程中的关键活动、所需资源、限制条件及信息系统面临的各种风险要素。组织应了解当风险演变为应急事件时所产生的影响和后果，以及信息系统服务中断所带来的损失。组织应授权组织内或组织外的服务供方进行风险识别，并将授权通知到所有相关利益方。</td><td style='text-align: center; word-wrap: break-word;'>a) 按照确定的方法和流程对重要信息系统实施风险评估，并形成书面的风险识别及评估表；b) 组织应了解当风险演变为应急事件时所产生的影响和后果，以及信息系统务中断所带来的损失；c) 形成风险评估报告。</td><td style='text-align: center; word-wrap: break-word;'>a) 风险识别和分析过程的完整性和合理性；b) 风险评估报告。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.4 划分应急事件级别</td><td style='text-align: center; word-wrap: break-word;'>组织应根据信息系统的重要程度、信息系统服务时段、信息系统受损程度对可能发生的应急事件进行级别划分。组织应结合自身的业务要求，对应急事件级别对应的响应时间、处置完成时间等达成一致。组织应根据应急事件级别配置响应的保障措施，如人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>应急事件级别划分需考虑以下因素：a) 重要程度；b) 服务时段；c) 受损程度。</td><td style='text-align: center; word-wrap: break-word;'>应急事件划分的合理性。</td></tr></table>

---

<div style="text-align: center;">表 11（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">GB/T 28827 运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.5 预案制定</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应预案。服务需方应组织对应急响应预案进行评审，并与相关利益方达成一致。经过评审确认的应急响应预案，应由应急响应责任者负责发布。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应根据风险评估结果制定应急响应预案；b) 服务需方应组织人员对应急响应预案进行评审，评审通过后正式发布；c) 应急响应预案应进行版本控制。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急响应预案的制定方法和内容；b) 应急预案的评审过程；c) 应急预案的版本控制。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.6 培训和演练</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应培训计划，并组织相关人员参与。应急响应预案应作为培训的主要内容。为检验应急响应预案的有效性，同时使相关人员了解运行维护预案的目标和内容，熟悉应急响应的操作规程，组织应进行应急演练。</td><td style='text-align: center; word-wrap: break-word;'>a) 培训应至少每年举办一次；b) 针对应急响应预案，应：1) 预先制定演练计划、演练脚本；2) 演练的整个过程应有详细的记录，并形成报告。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应急响应的培训宣贯体系。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 6.1 日常监测与预警</td><td style='text-align: center; word-wrap: break-word;'>组织应结合运行维护服务级别协议和应急响应预案，开展日常监测与预警活动；组织应建立监测、预警的记录和报告制度，并按照约定的形式和时间间隔上报现场负责人。发现应急事件时，值班人员应及时向现场负责人提交报告，并确认对方收到报告。值班人员应采取必要措施，开展应急事件的先期处置，以提高应急响应效率，避免次生、衍生事件的发生。应该对应急事件保持持续性跟踪。</td><td style='text-align: center; word-wrap: break-word;'>组织应该对运行维护服务对象的运行情况进行监测与预警，以跟踪和判别以下对象的容量、可用性和连续性：a) 应用系统；b) 支撑应用系统运行的系统软件、工具软件；c) 网络及网络设备；d) 安全设备；e) 主机、存储、外设、终端等设备；f) 电力、空调、消防等基础环境。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>将运维服务对象纳入日常监测和预警。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 6.2 核实与评估</td><td style='text-align: center; word-wrap: break-word;'>现场负责人应对报告内容进行逐项核实。现场负责人应根据事件级别定义，初步确定应急事件所对应的事件级别。应将事件级别置于动态调整控制中。</td><td style='text-align: center; word-wrap: break-word;'>现场负责人应对报告内容进行逐项核实。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应急事件报告。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 6.3 应急响应预案启动</td><td style='text-align: center; word-wrap: break-word;'>组织应建立、审议应急响应预案启动的策略和程序，以控制预案启动的授权和实施。应记录应急响应预案启动的过程和结果。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应建立、审议应急响应预案启动的策略和程序；b) 应记录应急响应预案启动的过程和结果；c) 将应急事件置于统一的事件处理流程控制范围内。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>a) 应急预案的启动机制；b) 应急预案启动后的全过程跟踪和记录。</td></tr></table>

---

<div style="text-align: center;">表 11（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.1 应急调度</td><td style='text-align: center; word-wrap: break-word;'>组织应按照预案，开展统一的应急调度，包括人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>组织应该按照预案开展统一的应急调度，包括人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>应急调度过程中的沟通机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.2 排查与诊断</td><td style='text-align: center; word-wrap: break-word;'>组织应建立有效的排查与诊断的流程；处置过程中，现场负责人应及时与相关利益方进行沟通，并组织相关利益方对问题进行确认。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应明确故障排查和诊断流程；b) 处置应急事件的过程中，现场负责人应及时与相关利益方就排查、诊断结果进行沟通和问题确认。</td><td style='text-align: center; word-wrap: break-word;'>故障排查与诊断记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.3 处理与恢复</td><td style='text-align: center; word-wrap: break-word;'>应基于应急响应预案、配置管理数据库、知识库等进行故障处理和系统恢复。必要时可启用备品备件、灾备系统等。应该对过程及结果信息进行记录，并及时告知相关利益方。</td><td style='text-align: center; word-wrap: break-word;'>在处理和回复应急事件时，应在满足事件级别处置时间要求的前提下，尽快恢复服务。</td><td style='text-align: center; word-wrap: break-word;'>应急事件的处理与恢复记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.4 升级与信息通报</td><td style='text-align: center; word-wrap: break-word;'>组织应建立、审议应急事件升级的策略和程序，升级内容应包含预案调整、人员调整、资金调整以及设备调整。应该对事件升级的过程和结果信息进行整理与归档。现场负责人应向相关利益方通报事件升级信息。</td><td style='text-align: center; word-wrap: break-word;'>组织应建立、审议应急事件升级的策略和程序，以控制应急事件升级的授权和实施。</td><td style='text-align: center; word-wrap: break-word;'>事件升级信息记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.5 持续服务</td><td style='text-align: center; word-wrap: break-word;'>完成处理与恢复后，应组织运行维护人员提供持续性服务。组织应对持续性服务的效果进行评价。持续服务的评价结果，应作为应急事件关闭的输入。</td><td style='text-align: center; word-wrap: break-word;'>完成处理与恢复后，应组织运行维护人员提供持续性服务。</td><td style='text-align: center; word-wrap: break-word;'>持续服务相关记录。</td></tr></table>

---

<div style="text-align: center;">表 11（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.1 应急工作总结</td><td style='text-align: center; word-wrap: break-word;'>组织应定期对应急响应工作进行分析和回顾，总结经验教训，并采取适当的后续措施。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应定期对应急响应工作进行分析和回顾，总结经验教训，并采取适当的后续措施； b) 将总结报告作为改进应急响应工作及信息系统的重要依据。</td><td style='text-align: center; word-wrap: break-word;'>应急响应工作总结报告。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.2 应急工作审核</td><td style='text-align: center; word-wrap: break-word;'>应急响应责任者应定期组织对应急响应工作的评审，以确保应急响应过程和管理符合预定的标准和要求。审核的结果应该正式存档并通知给相关利益方。 评审应至少每年举行一次。</td><td style='text-align: center; word-wrap: break-word;'>a) 为保证应急响应的有效性和时效性，应定期组织人员对应急响应工作进行评审，评审应至少每年举行一次； b) 审核的结果应该正式存档并通知给相关利益方。</td><td style='text-align: center; word-wrap: break-word;'>应急响应的有效性和时效性评审记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.3 应急工作改进</td><td style='text-align: center; word-wrap: break-word;'>应急事件总结、应急工作审核的结果应该作为应急准备阶段各项工作的改进要素。组织应根据总结报告中给出的建议项和评审结果，完善信息系统，深化应急准备工作。</td><td style='text-align: center; word-wrap: break-word;'>根据应急事件总结、应急工作审核报告、客户方的要求、技术的革新和发展等因素，对应急工作进行持续完善和改进。</td><td style='text-align: center; word-wrap: break-word;'>应急工作改进记录。</td></tr></table>

### 7.2 人员要求

改进（协同）级的人员要求见表 12。

---

<div style="text-align: center;">表 12 改进（协同）级的人员要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="3">GB/T 28827.1-2012 6.2 人员管理</td><td style='text-align: center; word-wrap: break-word;'>a) 人员储备 
  供方应建立运行维护服务相关的人员储备计划 
  和机制，确保有足够的人员以满足与需方约定的 
  当前和未来的运维业务需求。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：
a) 基于运维四要素及交付管理和应急响应对关键岗位的要求，制定人力资源规划和人力资源储备机制；
b) 有人力资源年度计划，其中包括人员储备计划；
c) 有岗位需求评估和岗位设置方案，岗位包括管理、工具研发、技术支持、过程管理以及应急响应等相应的关键岗位；
d) 有人员招（选）聘管理的工作流程；
e) 当发生人员变更时，保存相应工作交接记录。当有突发的服务需求时，有对其作出及时调整的记录；
f) 对人力资源储备和人员招（选）聘管理的适宜性进行定期评估和改进。</td><td rowspan="3">a) 核心人员储备率；
b) 储备计划满足各过程和业务的程度；
c) 人员培训支撑各过程和业务发展的程度；
d) 人员绩效考核对提升服务质量的效果。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 人员培训 
  供方应建立运行维护服务相关的培训体系或机 
  制，在制定培训时应识别培训要求，并提供及时 和有效的培训。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：
a) 制定了年度培训计划，其包括对管理、工具、技术、过程以及交付和应急响应等岗位人员的培训安排；
b) 年度培训经费投入得到管理，包括预算，核算和成本控制；
c) 建立培训讲师库和培训教材库，培训教材覆盖了管理、工具、技术、过程以及交付和应急响应的内容；
d) 有对培训效果的总结分析和改进，分析至少包括培训目标实现率、培训覆盖率、培训有效率，改进制定了改进计划；
e) 形成了培训实施的记录；
f) 对培训管理、讲师库和培训教材库的可用性进行定期评估和改进。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核 
  供方应建立运行维护服务相关的绩效考核体系 或机制，并能够有效组织实施。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：
a) 有人员绩效考核管理的工作流程，建立人员绩效考核管理制度，人员考核覆盖：管理、工具、技术、过程以及交付和应急响应等岗位；
b) 绩效考核制度得到了实施，至少每年一次实施了绩效考核，包括制定考核方案、提交绩效报告、考核评价、考核结果应用；
c) 根据考核的结果及时调整相关岗位，形成相应记录；
d) 形成了绩效考核实施的记录；
e) 对人员绩效考核制度的可用性进行定期评估和改进。</td></tr></table>

---

<div style="text-align: center;">表 12（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.3 岗位结构</td><td style='text-align: center; word-wrap: break-word;'>a) 管理岗人员和职责为:1) 在运行维护服务中负责管理运行维护服务;2) 与需方建立顺畅的沟通渠道, 准确地将需方的需求传递到运维团队;3) 规划、检查运行维护服务的各个过程, 对运行维护服务的策划、实施、检查、改进的范围、过程、信息安全和成果负责。b) 技术支持岗人员和职责为:1) 在运行维护服务中负责技术支持的人员, 包括网络、操作系统、数据库、中间件、应用开发、硬件、集成、信息安全等方面的专业技术人员;2) 对运行维护服务过程中的请求、事件和问题做出响应, 保障信息安全并对处理结果负责。c) 操作岗人员和职责为:1) 在运行维护服务中负责日常操作实施的人员;2) 根据规范和手册, 执行运行维护服务各过程, 并对其执行结果负责。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外, 还应满足以下要求:a) 基于业务和管理需要进行岗位设计和优化;b) 岗位职责规定了岗位间的关联关系和协同要求, 岗位职责经批准后得到了有效实施;c) 对岗位结构和岗位职责的可用性进行定期评估和改进。</td><td style='text-align: center; word-wrap: break-word;'>a) 岗位结构与业务的匹配度;b) 基于协同和效率的岗位设计;c) 岗位结构的定期评估优化。</td></tr></table>

---

<div style="text-align: center;">表 12（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.4 知识</td><td rowspan="3">a) 基础知识：信息技术相关基础知识。b) 专业知识：从事运行维护服务所必备的知识，应具有较为系统的内容体系和知识范围。如网络技术人员应具备网络专业整体的内容体系和知识；c) 综合知识：与运行维护服务相关的企业和行业知识。d) 确定运行维护服务人员在运行维护服务中所必备的能力；b) 要求运行维护服务人员具备从事相关运行维护服务的资格；c) 特殊环境运行维护服务人员应具备相关资格。a) 运行维护服务人员应具备所从事运行维护服务活动的经验；b) 供方应具备一定的从事运行维护服务活动的经验。</td><td rowspan="3">除达到三级要求外，还应满足以下要求：a) 建立人员知识、技能与岗位职责的验证机制，形成相应的岗位胜任考核管理制度；b) 至少每年一次实施岗位考核，并形成记录；c) 并根据考核结果，调整人员培训计划、优化岗位设置；d) 基于管理、工具、技术、过程以及交付和应急响应对岗位的要求，建立人员资源库；e) 当有突发的服务需求时，有对其作出及时响应的记录；f) 对人员考核管理、人员资源库的可用性进行定期评估和改进。</td><td rowspan="3">a) 满足业务需求的职级体系；b) 专业化人员的成长路径；c) 人员专业技能分布与服务业务匹配程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.5 技能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.6 经验</td></tr></table>

### 7.3 资源要求

改进（协同）级的资源要求见表 13。

<div style="text-align: center;">表 13 改进（协同）级的资源要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T28827.1-2012 7.2 运维工具</td><td style='text-align: center; word-wrap: break-word;'>a) 监控工具，对运行维护服务对象进行数据的采集和监控，评估可能导致运行维护服务对象故障的因素； b) 过程管理工具，按照商定的SLA管理运行维护服务的交付过程，过程管理工具宜包括日常运行维护管理、记录、测量、监督和评估等功能； c) 专用工具，根据服务要求配备的安全工具和用于特殊要求的工具。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求： a) 设立了运维工具的应用管理流程； b) 知识库覆盖运维工具的应用指南； c) 工程师使用运维工具成为能力要求的一部分。设立了运维工具实施和使用培训课程； d) 监控工具能够实现与流程管理工具的集成； e) 制定了运维工具的评估和改进管理流程。定期评估运维工具的应用效果，提炼改进需求。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维工具对业务的覆盖比率； b) 运维工具对运维各项指标能够实现数据提取、分析功能的比率； c) 运维工具实现情况和技术研发成果的匹配度； d) 运维工具在服务交付和服务管理中的应用情况。</td></tr></table>

---

<div style="text-align: center;">表 13（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="3">GB/T 28827.1-20127.3 服务台</td><td style='text-align: center; word-wrap: break-word;'>a) 设置专门的沟通渠道作为与需方的联络点，沟通渠道可以是热线电话、传真、网站、电子邮箱等；b) 设定专人负责服务请求的处理；</td><td rowspan="2">除达到三级要求外，还应满足以下要求：a) 制定了服务台的管理规范；b) 服务台能够从知识库获得必要的支持，如：常见问题处理方法；c) 制定了服务台的知识、技能和经验要求，设立了服务台培训课程；d) 制定了服务台的绩效考核办法，并定期进行绩效考核；e) 服务台管理与服务交付流程、事件管理流程、服务级别管理流程等实现集成；f) 服务台的日常工作纳入过程管理工具支撑范围；g) 服务台的设立和运行得到定期评估和改进；h) 服务台应对服务交付发挥支撑作用，如：事件接受和处理、一线支持、服务交付的调度管理等。</td><td rowspan="2">a) 制定了服务台的管理规范，是服务交付管理流程的一部分。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 针对沟通渠道整合服务过程，建立管理制度，包括服务请求的接收、记录、跟踪和反馈等机制，以及日常工作的监督和考核。</td></tr><tr><td rowspan="2">a) 备件响应方式和级别定义，能够满足 SLA 所约定的备件支持；b) 备件供应商管理：能够规范备件的采购过程，对供应商进行选择和评价；c) 备件出入库管理：能够对入库备件进行标识，规范备件的使用和核销，备件物品的帐务管理；</td><td rowspan="3">除达到三级要求外，还应满足以下要求：a) 备件管理的相关经验应纳入知识库；b) 明确备件服务级别管理、采购管理、库存管理和可用性管理等相应的岗位职责；c) 对以上岗位进行定期的培训及绩效考核；d) 应采用自动化工具进行备件管理，备件管理和过程管理工具应实现集成；e) 对备件服务级别达成、供应商管理、出入库管理和备件可用性进行定期评估和改进。</td><td rowspan="3">a) 备件库对服务目录的覆盖程度；b) 备件相关的投诉率。</td></tr><tr><td rowspan="2">GB/T 28827.1-20127.4 备件库</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 备件可用性管理：能够定期对备件状态进行检测，以确保其功能满足运行维护需求。</td></tr></table>

---

<div style="text-align: center;">表 13（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.5 知识库</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应针对常见问题的描述、分析和解决方法建立知识库；b) 确保整个组织内的知识是可用的、可共享的；c) 组织应选择一种合适的知识管理策略；d) 知识库应具备知识的添加、更新和查询功能；e) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 应建立知识库管理流程。规定知识需求识别、搜集、知识加工整理、知识分享和获取等管理职责；b) 识别主要岗位和主要业务流程的知识技能需求，并能通过知识库系统进行相应支持；c) 知识库工具与服务台工具应实现集成；d) 定期评估知识库管理平台和知识库内容的适宜性，并进行改进。</td><td style='text-align: center; word-wrap: break-word;'>a) 知识库用于解决问题的有效性；b) 知识库与业务流程及岗位职责的匹配度。</td></tr></table>

### 7.4 技术要求

改进（协同）级的技术要求见表 14。

<div style="text-align: center;">表 14 改进（协同）级的技术要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 8.2 技术研发</td><td style='text-align: center; word-wrap: break-word;'>a) 根据业务和市场分析, 制定研发规划, 包括新技术和前沿技术的应用、技术储备等; b) 配备与规划相适应的研发环境;</td><td rowspan="2">除达到三级要求外, 还应满足以下要求: a) 应建立技术研发管理规范; b) 技术研发的经费投入得到管理, 包括预算, 核算和成本控制; c) 技术研发环境得到管理, 包括研发环境规范、研发环境和研发产出物的配置管理; d) 具有专业的技术研发队伍, 规定了技术研发岗位的知识、技能和经验要求; e) 将研发规划的实现情况纳入对研发岗位的绩效考核; f) 技术研发规划需依据市场目标和业务目标, 覆盖服务产品开发、改善服务管理工具、发现问题的技术和解决问题的技术等方面; g) 技术研发的成果具有重要的应用案例。</td><td rowspan="2">a) 技术研发规划目标达成情况; b) 技术研发费用使用情况; c) 技术研发成果在发现问题、解决问题、运维工具和服务交付中的应用情况。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 配备与规划相适应的研发队伍。</td></tr></table>

---

<div style="text-align: center;">表 14（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.3 与发现问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 具有信息采集和监控的手段;</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求:a) 明确针对发现问题技术的管理职责;b) 建立发现问题技术的应用流程，并应用于服务交付流程和应急响应流程;c) 建立发现问题技术的开发和改进流程，包括收集需求、技术开发、应用和改进。</td><td style='text-align: center; word-wrap: break-word;'>a) 发现问题技术在服务交付中的应用情况;b) 工程师对发现问题技术的掌握程度，以及与岗位技能要求的匹配度。</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 8.4 与解决问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 解决问题的技术指标或标准;b) 解决问题的方案或手册;</td><td rowspan="2">除达到三级要求外，还应满足以下要求:a) 明确解决问题技术的管理职责，并规定其能力要求和绩效考核要求;b) 建立解决问题技术的开发和改进流程;c) 与解决问题技术相关的信息，可通过知识库管理系统进行查询和发布;d) 建立解决问题技术的应用指南，并应用于服务交付过程和应急响应过程;e) 建立验证解决问题技术有效性的测试环境或测试标准。解决问题技术的有效性得到评估。</td><td rowspan="2">a) 解决问题技术在服务交付中的应用情况;b) 工程师对解决问题技术的掌握程度，以及与岗位技能要求的匹配度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 测试环境、测试标准和方法。</td></tr></table>

### 7.5 过程要求

改进（协同）级的过程要求见表 15.

<div style="text-align: center;">表 15 改进（协同）级的过程要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">GB/T 28827</td><td rowspan="2">标准</td><td rowspan="2">标准条款要求</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9.2 服务级别管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务目录；b) 与需方签订 SLA；c) 根据需方的考核评估要求，建立 SLA 考核自评估机制，包括 SLA 完成情况、达成率；d) 在 SLA 评估后制定改进内容及改进措施。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 定期评估服务目录的完整性，考评 SLA 达成率，并提出优化改进措施；b) 根据组织战略和业务目标持续优化服务目录，提高服务目录的完整性；c) 根据 SLA 完成情况及达成率的考评分析，对运维交付、质量管理、人力资源、技术研发等策略进行优化和调整。</td><td colspan="2">a) 服务目录定义的合理性和完整性；b) 服务级别协议对交付过程的指导作用；c) 服务目录与服务产品化过程的匹配。</td></tr></table>

---

<div style="text-align: center;">表 15（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">GB/T 28827 运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.3 服务报告</td><td style='text-align: center; word-wrap: break-word;'>a) 与服务报告过程一致的活动，包括建立、审批、分发、归档等；b) 服务报告计划，包括提交方式、时间、需方接收对象等；c) 服务报告模板，包括格式、提纲等。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 定期对服务报告的完整性、数据准确性、报告提交的及时性等进行评估分析，并提出优化改进措施；b) 定期对服务报告反馈进行评审，形成改进意见，提高服务报告的完整性；c) 通过运维工具的优化，提高服务报告数据的准确性；d) 通过优化服务报告审核流程，提高服务报告提交的及时性；e) 根据报告内容、提交时效、阅读对象等不同对报告做必要分类。</td><td style='text-align: center; word-wrap: break-word;'>a) 有服务报告评审分析机制；b) 服务报告为策划改进提供支撑；c) 服务报告为实施效果评估提供依据；d) 服务报告类别符合业务需求。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.4 事件管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与事件管理过程一致的活动，包括事件受理、分类和初步支持、调查和诊断、解决、进展监控与跟踪、关闭等；b) 事件分类、分级机制；c) 事件升级机制；d) 满意度调查机制；e) 事件解决评估机制，包括事件解决率、事件平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 定期对事件分布、解决率、及时率等进行评估分析，并提出优化改进措施；b) 通过对监控工具的使用，及时发现故障隐患并处理，减少重大事件发生；c) 通过提高问题管理、知识库的水平、提高发现事件和解决事件的技术手段，提高事件的解决率；d) 通过与服务台联动，提高事件响应及时率；e) 通过定期组织应急演练提高应急事件响应及时率。</td><td style='text-align: center; word-wrap: break-word;'>a) 事件评估分析记录；b) 事件处理过程对服务台、监控工具、知识库等资源的灵活调用；c) 将应急事件纳入统一的事件管理。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.5 问题管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与问题管理过程一致的活动，包括问题建立、分类、调查和诊断、解决、关闭等；b) 问题分类管理机制，包括问题的影响范围、重要程度、紧急程度并确定优先级；c) 问题导入知识库机制；d) 问题解决评估机制，包括问题解决率、问题平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 定期对问题的分类、解决率、及时率等进行评估分析，并提出优化改进措施；b) 对问题识别策略进行改进，提高问题识别率；c) 通过使用专业工具提高问题解决的及时率；d) 对已发生问题进行分析，形成发现问题的技术手段，及时消除其他存在的隐患和弱点，减少事件的发生；e) 通过提高知识库使用率和解决问题的技术手段，提高问题、事件解决率；f) 制定临时解决问题的变通方案。</td><td style='text-align: center; word-wrap: break-word;'>a) 问题评估分析记录；b) 重复事件发生减少率；c) 问题处理报告与知识库的匹配度。</td></tr></table>

---

<div style="text-align: center;">表 15（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827</td><td colspan="3">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.6 配置管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与配置管理过程一致的活动, 包括识别、记录、更新和审核等;b) 配置数据库管理机制;</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外, 还应满足以下要求:a) 建立完整的配置管理体系, 包括明确的配置管理职责、配置管理计划、配置管理制度等;b) 建立与业务相适应的完整的配置管理数据库, 建立配置管理数据库管理制度, 包括配置项命名规范、设置配置管理数据库基线、确定配置项结构的深度和配置项的属性内容、建立配置项之间的关联关系等;c) 建立配置管理审计制度, 并将该制度纳入组织级的质量管理体系中, 定期对配置项的完整性和准确性进行审计, 建立审计计划和审计报告, 并对审计结果的改进进行追踪记录;d) 配置管理应从变更管理与发布管理获得对配置项的更新和修改信息, 并向变更管理提供配置项信息及配置项间的关系信息, 同时向事件管理和问题管理提供配置项信息;e) 具备专业的配置管理工具, 至少包含支持配置项的登记和管理、配置项间关系的建立和维护等。</td><td style='text-align: center; word-wrap: break-word;'>a) 配置管理体系的完整性;b) 配置管理流程与其他流程的关联度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.7 变更管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与变更管理过程一致的活动, 包括请求、评估、审批、实施、确认和回顾等;b) 建立变更类型和范围的管理机制;</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外, 还应满足以下要求:a) 在组织级的范围内对变更进行管理, 建立组织级的变更管理委员会;b) 建立完整的变更管理体系, 包括明确的变更管理职责、变更申请制度、变更审批制度、变更实施制度等, 跟踪变更执行过程并建立相关记录文件;c) 变更管理至少应从服务级别管理、信息安全管理、配置管理、事件管理及问题管理中获得各自过程的变更请求, 并向发布管理提供变更授权, 向事件管理、问题管理提供变更的处理结果;d) 建立变更管理评估和审核机制, 并将该制度纳入组织级的质量管理体系中, 至少应包含对变更分级审批机制、变更验证机制、变更回退机制、变更评价机制等进行定期评估和审核, 并建立相关记录文件;e) 具备专业的变更管理工具, 支持创建并记录变更请求, 审查变更请求, 变更请求的归类和划分优先级, 并应对变更请求的全程跟踪和监控。</td><td style='text-align: center; word-wrap: break-word;'>a) 变更分级分类的合理性和有效性;b) 变更管理与配置管理的协同。</td></tr></table>

---

<div style="text-align: center;">表 15（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.8 发布管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与发布管理过程一致的活动，包括规划、设计、建设、配置和测试等；b) 建立发布类型和范围的管理机制；c) 制定完整的方案，包括发布计划、回退方案、发布记录等；</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 建立完整的发布管理制度，包括明确的发布管理范围和职责、发布评估制度、发布测试制度、发布申请制度、发布审核制度、发布实施制度、发布验收制度、发布回退制度、发布过程监控制度等，并建立相关记录文件；b) 建立发布测试环境，包括与业务环境相近的硬件环境、系统环境、软件环境等，并建立相关测试记录文件；c) 建立发布管理评估和审核机制，并将该制度纳入组织级的质量管理体系中，至少应包含发布数量、发布成功率、发布回退率等；d) 发布管理应从变更管理获得变更授权，以便向配置管理提供配置项的更新和修改信息，并向变更管理提供对变更记录的更新和修改信息，同时向问题管理提供已知错误信息。</td><td style='text-align: center; word-wrap: break-word;'>a) 测试及发布实施计划的完整性；b) 发布管理与变更管理、配置管理的协同；c) 发布结果对交付的影响程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.9 信息安全管理</td><td style='text-align: center; word-wrap: break-word;'>a) 符合相关法律法规的规定，满足需</td><td style='text-align: center; word-wrap: break-word;'>除达到三级要求外，还应满足以下要求：a) 建立组织级的信息安全管理体系，制定、批准并发布信息安全目标和政策；b) 定义信息安全评估方法和风险接受准则；c) 定期实施信息安全评估，评估内容至少包含：可用性、完整性和保密性；d) 制定并实施信息安全控制措施，定期评审控制措施的有效性；e) 具备专业的信息安全防护工具，至少包含用户口令的认证、权限，用户操作的日志、审计，病毒及漏洞扫描等功能。</td><td style='text-align: center; word-wrap: break-word;'>a) 信息安全管理组织和岗位；b) 风险评估方法和评估报告；c) 信息安全控制措施与应急预案的融合度。</td></tr></table>

## 8 提升（量化）级

### 8.1 管理要求

提升（量化）级的管理要求见表 16。

---

<div style="text-align: center;">表 16 提升（量化）级的管理要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="3">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.2 策划</td><td style='text-align: center; word-wrap: break-word;'>a) 根据自身业务定位和能力，策划运行维护服务对象的服务内容与要求，并形成服务目录；b) 依据组织的业务发展需要来建立组织结构和管理制度，支持服务目录的实施或实现；c) 对人员、资源、技术和过程进行规划，建立相适应的指标体系和服务保障体系；d) 策划如何管理、审核并改进服务质量，建立内部审核评估机制。a) 制定满足整体策划的实施计划，并按计划实施；b) 建立与需方的沟通协调机制；c) 按照服务能力要求实施管理活动并记录，确保服务能力管理和服务过程实施可追溯，服务结果可计量或可评估；d) 提交满足质量要求的交付物。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 根据组织业务发展历程中积累的数据，结合业务发展需要和信息技术发展趋势，对具备可持续竞争优势的服务内容及其需求进行策划，并优化改进服务目录；b) 根据运维服务业务发展目标，建立适合实现运维服务业务目标的组织架构和管理制度，支持实现目标的量化分解；c) 根据预期投资回报目标，策划构成运维服务能力的人员、过程、技术和资源的指标体系，并与服务交付的服务保障体系融合；d) 策划改进运维服务能力的评审机制和运维服务质量管理的方法，持续量化评价运维服务业务发展情况以及指标的达成情况。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务业务发展的历史数据分析模型、方法和结果的应用情况，特别是历史数据对未来业务发展的支撑作用；b) 运维服务内容与需方业务目标的融合程度；c) 运维服务业务发展的风险控制手段、方法（例如风险控制矩阵）和风险预警机制。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.3 实施</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审服务过程及相关管理体系，以确保服务能力的适宜性和有效性；b) 调查需方满意度，并对服务能力策划实施的结果进行统计分析；c) 检查各项指标达成情况。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 根据行业或服务能力管理实施历史数据，明确运维服务能力管理实施计划以及确保实施计划关键内容成功实施的保障措施；b) 使用信息技术的手段，对运维服务能力管理计划的沟通和执行进行管理，并形成的记录，提供支撑运维服务业务决策的数据，支持运维服务中各类角色对服务结果的计量或评估，支持管理者的管理和决策；c) 建立运维服务质量管理制度和测评方法，实施统计分析，确保运维服务交付满足质量要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务能力管理实施计划和历史数据的关联情况；b) 运维服务能力管理计划执行记录的结构化程度，包括记录的完整性、可用性和可分析程度。c) 运维质量的测评、统计和分析的有效性</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 5.4 检查</td><td style='text-align: center; word-wrap: break-word;'>a) 定期评审服务过程及相关管理体系，以确保服务能力的适宜性和有效性；b) 调查需方满意度，并对服务能力策划实施的结果进行统计分析；c) 检查各项指标达成情况。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立测量和分析运维服务能力管理计划实施情况的模型和方法，对运维服务业务发展趋势和风险进行预测和分析；b) 定量和定性调查客户满意度和用户体验，分析运维服务对需方业务的价值，评价运维服务和需方业务融合程度；c) 测量和分析各要素指标达成情况，并形成能指导各要素指标改进提升的基准库。</td><td style='text-align: center; word-wrap: break-word;'>a) 各类模型和方法的适用性；b) 分析运维服务业务对需方业务价值的深度和广度；c) 各指标基准库的完整性和适用性。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<div style="text-align: center;">表16（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="2">GB/T 28827.1-2012 5.5 改进</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务能力管理改进机制；b) 对不符合策划要求的行为进行总结分析；c) 对未达成的指标进行调查分析；</td><td rowspan="2">除达到二级要求外，还应满足以下要求：a) 基于量化分析的方法，建立与运维服务业务发展方向和目标一致的运维服务能力改进机制；b) 采用统计分析方法，对运维服务业务发展趋势和风险、运维服务和需方业务融合程度、各要素指标达成情况进行分析，对制约运维服务业务发展的因素和可能的风险进行识别，形成改进计划并实施；c) 建立评价运维服务能力管理改进效果的模型和方法并实施，形成服务能力管理改进的知识资产库。</td><td rowspan="2">运维服务能力改进机制和计划的合理性和有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>d) 根据分析结果确定改进措施，制定服务能力改进计划。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.2 交付策划</td><td style='text-align: center; word-wrap: break-word;'>根据需方需求和供方自身能力，双方协商签署服务级别协议；供方做好必要的交付准备，制定交付计划，确保服务正常提供。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 制定组织级的运维服务交付方案，并作为运维服务能力管理计划的组成部分；b) 制定运维服务交付的模型和方法，实现对运维服务交付成本、风险、投资回报和持续改进等的有效控制；c) 建立组织级和项目级采集和分析运维服务交付数据的制度和办法，支撑运维服务能力管理计划的实施，并形成组织级的运维服务交付基准库；d) 服务交付可视化。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织级运维服务交付方案的合理性和适用性，特别是交付方案对投资回报（ROI）的影响；b) 运维服务交付模型和方法的合理性和适用性；c) 运维服务交付基准库的完整性和适用性；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.3 交付实施</td><td style='text-align: center; word-wrap: break-word;'>供方按照交付策划向需方提供运行维护服务，完成服务级别协议规定内容。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 按照项目级运维服务交付方案和GB/T 28827.2的5.3的要求实施交付，均采用自动化工具，及时准确记录运维服务交付过程；b) 利用自动化工具，及时准确获取运维服务交付的质量、客户满意度、用户体验等数据。</td><td style='text-align: center; word-wrap: break-word;'>获取运维服务交付数据的完整性、及时性和准确性；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.4 交付检查</td><td style='text-align: center; word-wrap: break-word;'>供需双方通过交付策划与交付实施的对比检查，确认完成情况，并对发现的问题提出改进建议。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 基于运维服务交付方案和GB/T 28827.2的5.4的要求进行检查，评估与运维服务能力管理计划的符合程度；b) 根据运维服务交付的模型和方法，分析和评测运维服务交付成本、质量、风险、投资回报等情况和发展趋势；c) 确保用于交付检查数据的有效性；d) 基于量化数据分析和评测项目级运维服务交付方案执行的情况和发展趋势；e) 基于量化数据评价供方运维服务与需方业务融合程度。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务交付成本、质量、投资回报的实现情况计划之间偏差的分析；b) 运维服务交付过程中获取的数据完整性和可用性，包括用于评价运维服务与需方业务融合的程度。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 5.5 交付改进</td><td style='text-align: center; word-wrap: break-word;'>供方通过对交付各过程的总结分析，提出建议并改进，以提高效率，提升需方满意度。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 根据交付检查的结果制定改进计划，并与运维服务能力管理改进计划保持一致；b) 按照运维服务交付改进计划和GB/T 28827.2的5.4的要求实施改进；c) 基于运维服务交付过程中获取的数据，及时优化运维服务交付方案和内容；d) 建立并实施评价和分析运维服务交付改进的制度和方法。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务交付改进计划与运维服务能力管理改进计划的一致性和可实施性；b) 运维服务交付改进效果。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.2 例行操作</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供日常的预定服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立数据分析模型，定期对例行操作数据进行分析；b) 建立持续改进机制，基于数据分析结果完善例行操作服务交付方案和内容。</td><td style='text-align: center; word-wrap: break-word;'>a) 例行操作数据分析模型的合理性；b) 例行操作持续改进的效果。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.3 响应支持</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供服务请求或故障申报的即时服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立数据分析模型，定期对响应支持数据进行分析；b) 建立持续改进机制，基于数据分析的结果完善响应支持服务的交付方案。</td><td style='text-align: center; word-wrap: break-word;'>a) 响应支持数据分析模型的合理性；b) 响应支持持续改进的效果。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.4 优化改善</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供对运行维护服务对象功能和性能的调优服务等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立评价需方业务发展对运维服务要求的方法，并实施评价；b) 建立与需方沟通优化改善方案的机制，并利用可量化、可考核的方法评价优化改善方案的可行性；c) 建立跟踪优化改善方案实施的方法和手段，并形成执行记录。</td><td style='text-align: center; word-wrap: break-word;'>a) 优化改善方案的完整性和可行性；b) 优化改善实施后的效果。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 6.5 调研评估</td><td style='text-align: center; word-wrap: break-word;'>供方通过向需方提供对运行维护服务对象的调查研究或分析评价，给出报告或建议等交付内容，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立调研评估方法和流程；b) 依据历史数据和需方的业务需求，制定调研评估方案；c) 必要时，利用合理的方法和手段，评价和分析调研评估结果中后续实施方案的可行性；d) 利用调研评估实施案例库，支撑需方之间的同行对比，以及管理层对运维服务发展的决策。</td><td style='text-align: center; word-wrap: break-word;'>a) 调研评估方法的专业性和可展示度；b) 调研评估记案例库。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 7.2 现场交付</td><td style='text-align: center; word-wrap: break-word;'>供方通过现场支持的方式为需方提供服务，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立客户满意度与运维服务交付的关联关系（例如利用关联矩阵或模型），定期实施分析，形成经验数据，用于提升客户满意度；b) 分析运维服务交付不满足SLA和客户满意度的主要原因和处置措施的成效，并形成知识。</td><td style='text-align: center; word-wrap: break-word;'>a) 客户满意度与运维服务交付关联模型的合理性；b) 持续性改进的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 7.3 远程交付</td><td style='text-align: center; word-wrap: break-word;'>供方通过远程支持的方式为需方提供服务，以满足运行维护服务的服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立客户满意度与运维服务交付的关联关系（例如利用关联矩阵或模型），定期实施分析，形成经验数据，用于提升客户满意度；b) 分析运维服务交付不满足SLA和客户满意度的主要原因和处置措施的成效，并形成知识。</td><td style='text-align: center; word-wrap: break-word;'>a) 客户满意度与运维服务交付关联模型的合理性；b) 持续性改进的有效性。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.2 交付成果管理</td><td style='text-align: center; word-wrap: break-word;'>供方在提供运行维护服务交付的过程中，通过向需方提供无形的（如状态恢复、性能提升等）或有形的（如过程记录、服务报告、现场备件等）交付成果，以满足服务级别协议要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务交付成果管理的全面性和系统性；b) 运维服务交付成果对改进运维服务交付、推动运维服务业务发展的价值。</td><td rowspan="5">a) 运维服务交付成果管理的全面性和系统性；b) 运维服务交付成果对改进运维服务交付、推动运维服务业务发展的价值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.3 例行操作成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供例行操作服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td><td rowspan="4">a) 建立针对运维服务交付成果的量化分析方法，重点分析交付中的优势内容、存在的不足，以及对客户满意度的影响和对改进运维服务质量的价值等；b) 建立对运维服务交付成果的评价、复用的方法，实施定期评价，并与运维服务知识库进行关联。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.4 响应支持成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供响应支持服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.5 优化改善成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供优化改善服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.2-2012 8.6 调研评估成果</td><td style='text-align: center; word-wrap: break-word;'>供方在提供调研评估服务交付的过程中，通过向需方提供无形的或有形的交付成果，以满足服务级别协议要求。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.1 应急响应组织</td><td style='text-align: center; word-wrap: break-word;'>运行维护服务的组织由相关利益方组成，包括服务需方、服务供方、分包方、供应商等。应在运行维护服务组织基础上建立应急响应组织。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 对应急响应组织中的关键角色应提供备份人选；b) 对应急响应组织内人员应建立考核机制，明确考核指标及方法，至少每年进行一次。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急响应组织设置的合理性；b) 应急响应绩效考核的有效性。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5.2 应急响应制度</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应制度，明确应急响应的目标、原则、范围以及各项管理制度，并要求：a) 与相关利益方就应急响应制度达成一致；b) 定期对应急响应制度进行评审；c) 在组织战略、业务流程、需方要求等发生重大变化时对应急响应制度进行调整。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 应定期对应急响应制度的有效性和适宜性进行评审；b) 在组织战略、业务流程、需方要求等发生重大变化时，对应急响应制度进行调整。</td><td style='text-align: center; word-wrap: break-word;'>应急响应制度的有效性、适宜性、完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5.3 风险评估和改进</td><td style='text-align: center; word-wrap: break-word;'>组织应按照确定的方法和流程对重要信息系统实施风险评估，确保组织了解其在运行维护过程中的关键活动、所需资源、限制条件及信息系统面临的各种风险要素。组织应了解当风险演变为应急事件时所产生的影响和后果，以及信息系统服务中断所带来的损失。组织应授权组织内或组织外的服务供方进行风险识别，并将授权通知到所有相关利益方。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 形成风险评估报告，报告内容应包括但不限于：1) 结论摘要；2) 背景及现状；3) 风险要素；4) 识别出的风险及风险分析；b) 建议的应对措施。</td><td style='text-align: center; word-wrap: break-word;'>风险报告的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5.4 划分应急事件级别</td><td style='text-align: center; word-wrap: break-word;'>组织应根据信息系统的重要程度、信息系统服务时段、信息系统受损程度对可能发生的应急事件进行级别划分。组织应结合自身的业务要求，对应急事件级别对应的响应时间、处置完成时间等达成一致。组织应根据应急事件级别配置响应的保障措施，如人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 应急事件级别划分应考虑以下因素：1) 重要程度应考虑运维服务对象所支撑的业务的重要性，以及运维服务对象内信息资产的重要性；2) 服务时段应考虑应急事件发生时运维服务对象提供服务的状态；3) 受损程度应考虑应急事件发生时运维服务对象功能和性能等方面的影响程度。b) 组织应根据应急事件级别配置相应的保障措施，如人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急事件级别划分合理性；b) 不同级别应急事件与配套保障措施的关联性。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.5 预案制定</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应预案。服务需方应组织对应急响应预案进行评审，并与相关利益方达成一致。经过评审确认的应急响应预案，应由应急响应责任者负责发布。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 应急响应预案的内容应包括：1) 应急响应预案的编制目的、依据和适用范围；2) 具体的组织体系结构及人员职责；3) 应急响应的监测和预警机制；4) 应急响应预案的启动；5) 应急事件级别及对应的处置流程、方法；6) 应急响应的保障措施；7) 应急预案的附则。b) 服务需方应组织对应急响应预案进行评审，并与相关利益方达成一致；c) 经过评审确认的应急响应预案，应由应急响应责任者负责发布；d) 应急响应预案应进行版本控制。</td><td style='text-align: center; word-wrap: break-word;'>应急响应预案的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 5.6 培训和演练</td><td style='text-align: center; word-wrap: break-word;'>组织应制定应急响应培训计划，并组织相关人员参与。应急响应预案应作为培训的主要内容。为检验应急响应预案的有效性，同时使相关人员了解运行维护预案的目标和内容，熟悉应急响应的操作规程，组织应进行应急演练。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 制定应急响应培训计划，并至少每年组织一次相关人员参与。确保：1) 应急响应预案应作为培训的主要内容；2) 培训应使组织及人员明确其在应急响应过程中的责任范围、接口关系，明确应急处置的操作规范和操作流程。b) 针对应急响应预案，应确保：1) 预先制定演练计划，编制演练脚本；2) 演练的整个过程应有详细的记录，并形成报告；3) 演练不能影响业务的正常运行；4) 组织可根据演练的效果，对应急响应预案进行完善。c) 组织应定期进行应急演练。</td><td style='text-align: center; word-wrap: break-word;'>应急响应预案的有效性。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-20126.1 日常监测与预警</td><td style='text-align: center; word-wrap: break-word;'>组织应结合运行维护服务级别协议和应急响应预案，开展日常监测与预警活动；组织应建立监测、预警的记录和报告制度，并按照约定的形式和时间间隔上报现场负责人。发现应急事件时，值班人员应及时向现场负责人提交报告，并确认对方收到报告。值班人员应采取必要措施，开展应急事件的先期处置，以提高应急响应效率，避免次生、衍生事件的发生。应该对应急事件保持持续性跟踪。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：组织应结合运行维护服务级别协议和应急响应预案，采用必要的工具和手段开展日常监测与预警活动，包括：a) 确定监测项、监测时间间隔与阈值；b) 确定活动中的人员、角色和职责。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急响应日常监测的有效性；b) 监测及预警阈值的适宜性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-20126.2 核实与评估</td><td style='text-align: center; word-wrap: break-word;'>现场负责人应对报告内容进行逐项核实。现场负责人应根据事件级别定义，初步确定应急事件所对应的事件级别。应将事件级别置于动态调整控制中。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 现场负责人应及时向应急响应责任者提交核实确认后的应急事件报告；b) 应急事件报告应作为事件级别评估的输入；c) 重点时段保障需求也应作为事件级别评估的输入；d) 应将事件级别置于动态调整控制中。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急事件报告的及时率；b) 核实结果的准确性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-20126.3 应急响应预案启动</td><td style='text-align: center; word-wrap: break-word;'>组织应建立、审议应急响应预案启动的策略和程序，以控制预案启动的授权和实施。应记录应急响应预案启动的过程和结果。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 组织应建立、审议应急响应预案启动的策略和程序；b) 应急响应预案启动信息内容应包括：1) 预案启动的原因；2) 事件级别；3) 事件对应的预案；4) 要求采取的技术应对措施或处置的目标；5) 实现目标所应采取的保障措施，如人员、资金和设备等；6) 对应急处置过程及结果的报告要求，如报告程序、报告内容、报告频率等；7) 信息通报的范围和接收者。</td><td style='text-align: center; word-wrap: break-word;'>应急响应启动信息的完整性。</td></tr></table>

---

<div style="text-align: center;">表16(续)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.1 应急调度</td><td style='text-align: center; word-wrap: break-word;'>组织应按照预案，开展统一的应急调度，包括人员、资金和设备等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 应急调度中应：1) 组织人员进行勘察、分析；2)下达调度命令并保持跟踪；b) 保护可追查的相关线索。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急调度及时性；b) 应急调度的资源保障机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.2 排查与诊断</td><td style='text-align: center; word-wrap: break-word;'>组织应建立有效的排查与诊断的流程；处置过程中，现场负责人应及时与相关利益方进行沟通，并组织相关利益方对问题进行确认。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：故障排查与诊断的流程应包含以下内容：1) 现场负责人调度处置人员进行现场故障排查；2) 现场处置人员进行故障排查和诊断，必要时可寻求组织其他人员以现场或远程方式进行支持，在此过程中可借助各类排查诊断分析工具，如应用软件、电子分析工具、故障排查知识库等；3) 现场处置人员应随时向现场负责人汇报故障排查情况、诊断信息、故障定位结果等；4) 将排查与诊断的过程与结果信息进行整理与归档。</td><td style='text-align: center; word-wrap: break-word;'>排查与诊断的准确率。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.3 处理与恢复</td><td style='text-align: center; word-wrap: break-word;'>应基于应急响应预案、配置管理数据库、知识库等进行故障处理和系统恢复。必要时可启用备品备件、灾备系统等。应该对过程及结果信息进行记录，并及时告知相关利益方。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 应基于应急响应预案、配置管理数据库、知识库等进行故障处理和系统恢复；b) 采用的方法、手段不应造成次生、衍生事件的发生；c) 应对处理与恢复的结果进行初步确认。</td><td style='text-align: center; word-wrap: break-word;'>a) 应急事件处理手段的合理性和有效性；b) 应急事件恢复结果的沟通及时性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.4 升级与信息通报</td><td style='text-align: center; word-wrap: break-word;'>组织应建立、审议应急事件升级的策略和程序，升级内容应包含预案调整、人员调整、资金调整以及设备调整。应该对事件升级的过程和结果信息进行整理与归档。现场负责人应向相关利益方通报事件升级信息。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 组织应建立、审议应急事件升级的策略和程序，以控制应急事件升级的授权和实施；b) 现场负责人应向相关利益方通报事件升级信息。</td><td style='text-align: center; word-wrap: break-word;'>应急事件升级机制的合理性。</td></tr></table>

---

<div style="text-align: center;">表16（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 7.5 持续服务</td><td style='text-align: center; word-wrap: break-word;'>完成处理与恢复后，应组织运行维护人员提供持续性服务。组织应对持续性服务的效果进行评价。持续服务的评价结果，应作为应急事件关闭的输入。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 完成处理与恢复后，应组织运行维护人员提供持续性服务；b) 组织应对持续性服务的效果进行评价；c) 持续服务的评价结果，应作为应急事件关闭的输入。</td><td style='text-align: center; word-wrap: break-word;'>a) 持续性服务的效果评价记录；b) 应急事件关闭机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.1 应急工作总结</td><td style='text-align: center; word-wrap: break-word;'>组织应定期对应急响应工作进行分析和回顾，总结经验教训，并采取适当的后续措施。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 对应急响应工作的分析和总结应考虑以下方面：1) 应急响应工作的绩效；2) 应急准备工作的充分性和有针对性；3) 应急事件发生原因、数量及频率；4) 应急事件处置的经验得失；5) 应急事件的趋势信息；6) 运维对象中潜在的类似隐患。</td><td style='text-align: center; word-wrap: break-word;'>应急响应工作总结的完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.2 应急工作审核</td><td style='text-align: center; word-wrap: break-word;'>应急响应责任者应定期组织对应急响应工作的评审，以确保应急响应过程和管理符合预定的标准和要求。审核的结果应该正式存档并通知给相关利益方。评审应至少每年举行一次。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 为保证应急响应的有效性和时效性，应急响应责任者应定期组织对应急响应工作的评审，以确保应急响应过程和管理符合预定的标准和要求；b) 审核的结果应该正式存档并通知给相关利益方。评审应至少每年举行一次。</td><td style='text-align: center; word-wrap: break-word;'>应急响应的有效性和时效性评审记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.3-2012 8.3 应急工作改进</td><td style='text-align: center; word-wrap: break-word;'>应急事件总结、应急工作审核的结果应该作为应急准备阶段各项工作的改进要素。组织应根据总结报告中给出的建议项和评审结果，完善信息系统，深化应急准备工作。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 将以下要素纳入应急工作改进的输入：1) 应急工作审核报告；2) 需方的要求；3) 技术的革新和发展；</td><td style='text-align: center; word-wrap: break-word;'>应急响应工作的持续改进机制。</td></tr></table>

---

<div style="text-align: center;">表 16（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827、质量评价指标体系</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运维服务质量评价策划</td><td style='text-align: center; word-wrap: break-word;'>参照《信息技术服务质量评价指标体系》策划建立运维服务质量管理体系。</td><td style='text-align: center; word-wrap: break-word;'>a) 制定组织服务质量管理计划，定期开展组织级和项目级的服务质量评价；b) 建立运维服务质量指标评价指标体系；c) 应针对指标项区分组织级指标和项目级指标，针对不同项目类型对指标项进行裁剪，形成指标裁剪指南；d) 应针对评价指标建立相应的数据获取和统计机制，形成指标数据库，完整记录组织级和项目级的评价过程和结果；e) 必要时选择专业化的运维服务质量评价工具。</td><td style='text-align: center; word-wrap: break-word;'>a) 服务质量指标评价体系的完整性和适用性；b) 服务质量评价模型的合理性和评价指标的可实施程度，并可裁剪/组合；c) 运维服务质量评价指标的完整性和合理性；d) 运维服务质量评价指标相应的数据获取和统计机制的有效性和完整性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运维服务质量评价实施</td><td style='text-align: center; word-wrap: break-word;'>参照《信息技术服务质量评价指标体系》和运维服务质量管理体系的策划内容，对运维服务交付质量提出要求。</td><td style='text-align: center; word-wrap: break-word;'>a) 应定期对运维组织和运维项目实施质量评价，有相关计划并指定专人负责更新和完善；b) 运维服务质量管理计划中至少应包括：评价范围、时间安排、负责人等。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织级和项目级运维服务质量评价计划，包括评价频率、评价方法、评价范围等；b) 运维项目实施质量评价过程的完整性和有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运维服务质量评价检查</td><td style='text-align: center; word-wrap: break-word;'>参照《信息技术服务质量评价指标体系》建立运维服务质量管理体系，对运维服务项目进行质量评价。</td><td style='text-align: center; word-wrap: break-word;'>a) 应对组织级和项目级指标的评价结果进行分析和总结，编写评价报告，形成组织级和项目级指标基线。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务质量指标评价结果的真实性、有效性；b) 运维服务质量指标基线的完整性和适用性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运维服务质量评价改进</td><td style='text-align: center; word-wrap: break-word;'>参照《信息技术服务质量评价指标体系》对质量评价体系进行不断完善改进。</td><td style='text-align: center; word-wrap: break-word;'>a) 供需双方应根据评价结果制定质量改进计划；b) 供方应按照质量改进计划实施改进，提升运维服务质量；c) 应持续分析运维服务质量指标变化趋势，以指导人员、资源、过程和技术的改进，并保持运维服务质量评价体系在组织内部持续运行。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维服务质量改进计划的合理、可实施程度；b) 运维服务质量改进的效果。</td></tr></table>

---

### 8.2 人员要求

提升（量化）级的人员要求见表 17。

<div style="text-align: center;">表 17 提升（量化）级的人员要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td rowspan="6">6.2 人员管理</td><td style='text-align: center; word-wrap: break-word;'>a) 人员储备</td><td rowspan="6">除达到二级要求外，还应满足以下要求：a) 结合运维服务业务发展实际，建立量化和层次化的岗位结构，以及人员培养和评价指标体系，至少包括知识、技能和经验等方面，实现对运维人员的分级分类精细化管理；注：可参考《信息技术服务从业人员能力规范》标准。b) 根据运维服务业务发展对人员的需求，以历史数据为基础，综合考虑人员储备投入成本及预期效益，制定人员储备计划；c) 建立评价人员储备计划的制度，并跟踪分析人员储备计划的实施情况；d) 根据本部分a)的要求，制定人员培训计划，实施培训并跟踪分析培训效果，形成培训对提升运维人员能力的经验数据，建立改进人员培训的机制并实施改进；e) 根据本部分a)的要求，建立组织级和项目级的人员绩效考核指标体系并确保实施。</td><td rowspan="6">a) 岗位结构划分与运维服务业务的适配情况，以及人员培养和评价指标体系的合理性和适用性；b) 人才储备计划的可量化实施的程度；c) 培训的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b) 人员培训</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 绩效考核</td></tr></table>

---

<div style="text-align: center;">表 17（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.3 岗位结构</td><td style='text-align: center; word-wrap: break-word;'>a) 管理岗人员和职责为: 1) 在运行维护服务中负责管理运行维护服务; 2) 与需方建立顺畅的沟通渠道, 准确地将需方的需求传递到运维团队; 3) 规划、检查运行维护服务的各个过程, 对运行维护服务的策划、实施、检查、改进的范围、过程、信息安全和成果负责。 b) 技术支持岗人员和职责为: 1) 在运行维护服务中负责技术支持的人员, 包括网络、操作系统、数据库、中间件、应用开发、硬件、集成、信息安全等方面的专业技术人员; 2) 对运行维护服务过程中的请求、事件和问题做出响应, 保障信息安全并对处理结果负责。 c) 操作岗人员和职责为: 1) 在运行维护服务中负责日常操作实施的人员; 2) 根据规范和手册, 执行运行维护服务各过程, 并对其执行结果负责。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外, 还应满足以下要求: a) 建立评价各类岗位人员数量、层次结构与运维服务业务发展相匹配的方法和手段, 并确保实施; b) 依据岗位结构评价的结果数据, 建立优化岗位结构的机制, 优化内容至少包括组织结构、岗位结构、人员数量等。</td><td style='text-align: center; word-wrap: break-word;'>a) 岗位结构与运维服务业务的匹配程度; b) 实施岗位结构优化的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.4 知识</td><td style='text-align: center; word-wrap: break-word;'>a) 基础知识信息技术相关基础知识。 b) 专业知识从事运行维护服务所必备的知识, 应具有较为系统的内容体系和知识范围。如网络技术人员应具备网络专业整体的内容体系和知识。 c) 综合知识与运行维护服务相关的企业和行业知识。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外, 还应满足以下要求: a) 建立运维服务人员知识结构与组织知识管理的匹配关系, 评价运维服务人员对组织知识的贡献; b) 建立评价运维人员知识的机制; c) 定期评价运维人员利用知识实现创新的价值。</td><td style='text-align: center; word-wrap: break-word;'>运维人员对组织知识的贡献度。</td></tr></table>

---

<div style="text-align: center;">表 17（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.5 技能</td><td style='text-align: center; word-wrap: break-word;'>a) 确定运行维护服务人员在运行维护服务中所必备的能力；b) 要求运行维护服务人员具备从事相关运行维护服务的资格；c) 特殊环境运行维护服务人员应具备相关资格。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立量化评价运维人员技能的指标体系，并结合运维业务需求建立测评模型，实现运维人员技能与业务需求的良好匹配；b) 建立评价运维人员技能对运维服务业务发展、运维技术研发和运维服务交付的贡献机制，实施评价并形成经验数据；c) 结合运维服务业务发展情况及信息通信技术发展趋势，建立预防运维人员技能淘汰的机制，以及促进运维人员技能提升的方法和手段。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维人员技能指标体系的完整性；b) 运维人员技能指标体系实施的覆盖程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 6.6 经验</td><td style='text-align: center; word-wrap: break-word;'>a) 运行维护服务人员应具备所从事运行维护服务活动的经验；b) 供应具备一定的从事运行维护服务活动的经验。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 分析运维服务业务岗位与经验之间的关系，识别各类岗位需要的经验，并根据运维服务业务发展情况不断完善；b) 根据运维服务业务发展方向，按照本部分6.2的要求，储备具有相关业务经验的人员。</td><td style='text-align: center; word-wrap: break-word;'>运维人员、团队及组织的经验和运维服务业务发展需求的匹配程度。</td></tr></table>

### 8.3 资源要求

提升（量化）级的资源要求见表 18。

<div style="text-align: center;">表 18 提升（量化）级的资源要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">GB/T 28827 运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a) 监控工具，对运行维护服务对象进行数据的采集和监控，评估可能导致运行维护服务对象故障的因素；b) 过程管理工具，按照商定的SLA管理运行维护服务的交付过程，过程管理工具宜包括日常运行维护管理、记录、测量、监督和评估等功能；c) 专用工具，根据服务要求配备的安全工具和用于特殊要求的工具。</td><td style='text-align: center; word-wrap: break-word;'>a) 制定监控工具和过程管理工具实现数据、信息共享和交换的规范，支持运维服务业务的统计分析、报告和量化管理；b) 根据需方业务风险分析，建立使用工具支持运维服务交付的方法；c) 统计分析运维工具的应用频次、应用的重点功能以及运维工具与重点运维服务业务的关系，必要时，对运维工具的功能、使用方式等实施改进；d) 根据运维服务业务发展情况，建立动态优化运维工具的制度和方法，并与技术研发管理相关联。</td><td style='text-align: center; word-wrap: break-word;'>a) 运维工具之间数据、信息共享和交换效率，以及运维工具对促进运维服务业务发展的价值；b) 运维工具发现改进机会数量，以及改进机会实施结果所得到可量化的或者不可量化的价值。</td></tr></table>

---

<div style="text-align: center;">表 18（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">GB/T 28827 运维服务能力成熟度</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a) 设置专门的沟通渠道作为与需方的联络点，沟通渠道可以是热线电话、传真、网站、电子邮箱等；b) 设定专人负责服务请求的处理；c) 针对沟通渠道整合服务过程，建立管理制度，包括服务请求的接收、记录、跟踪和反馈等机制，以及日常工作的监督和考核。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立运维服务需方的行为分析方法并实施分析，分析内容至少包括行为习惯、知识技能域和潜在需求等；b) 建设完整有效的运维服务交付所需状态信息，实现对运维服务的高效管理及运维活动关联分析、决策支持和优化。</td><td style='text-align: center; word-wrap: break-word;'>a) 服务台对业务改进提出的相关建议或发现问题数量；b) 量化衡量服务台的资源整合和过程促进的价值。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a) 备件响应方式和级别定义，能够满足 SLA 所约定的备件支持；b) 备件供应商管理：能够规范备件的采购过程，对供应商进行选择和评价；c) 备件出入库管理：能够对入库备件进行标识，规范备件的使用和核销，备件物品的帐务管理；</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 对备件进行分类统计分析，预测备件控制水平。至少包含：1) 备件的比例模型；2) 备件数量与业务处理数量的关系模型。b) 分析需方业务变更和组织商业目标对备件管理要求，对备件响应分级控制；c) 评估备件应用的效果，至少包含变更完成后，需方给予满意度评价；d) 评估对备件管理改进获得的价值。</td><td style='text-align: center; word-wrap: break-word;'>a) 备件库对支撑运维服务级别的有效性；b) 备件管理对降低业务风险和运营成本的量化分析。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7.4 备件库</td><td style='text-align: center; word-wrap: break-word;'>d) 备件可用性管理：能够定期对备件状态进行检测，以确保其功能满足运行维护需求。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应针对常见问题的描述、分析和解决方法建立知识库；b) 确保整个组织内的知识是可用的、可共享的；c) 组织应选择一种合适的知识管理策略；d) 知识库应具备知识的添加、更新和查询功能；</td><td style='text-align: center; word-wrap: break-word;'>a) 知识管理策略的有效性；b) 知识库管理系统的使用情况，以及与服务台、运维工具的集成情况；c) 知识库对促进运维服务业务发展的价值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 7.5 知识库</td><td style='text-align: center; word-wrap: break-word;'>e) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。</td><td style='text-align: center; word-wrap: break-word;'>a) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。b) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。c) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。d) 组织应针对知识管理要求制定相关管理制度，并进行知识生命周期管理。</td><td style='text-align: center; word-wrap: break-word;'>a) 知识管理策略的有效性；b) 知识库管理系统的使用情况，以及与服务台、运维工具的集成情况；c) 知识库对促进运维服务业务发展的价值。</td></tr></table>

---

### 8.4 技术要求

提升（量化）级的技术要求见表 19。

<div style="text-align: center;">表 19 提升（量化）级的技术要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">GB/T 28827</td><td colspan="2">运维服务能力成熟度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.2 技术研发</td><td style='text-align: center; word-wrap: break-word;'>a) 根据业务和市场分析，制定研发规划，包括新技术和前沿技术的应用、技术储备等；b) 配备与规划相适应的研发环境；</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 建立跟踪、分析、选择新技术的机制，以及跟踪需方业务发展趋势和需求的机制；b) 建立新技术研发立项管理制度，实施量化的可行性研究分析，评价并识别每项技术研发对获得可持续竞争优势及满足需方业务需求的价值；c) 建立量化评价分析技术研发的投资回报和实现商业目标的方法和手段；d) 跟踪、评估技术研发成果转换为市场目标和业务目标的机会，并结合市场和业务情况及时调整技术研发方向。</td><td style='text-align: center; word-wrap: break-word;'>a) 技术研发规划对业务目标的支持程度；b) 技术研发规划对运维服务产品开发的支持程度；c) 新技术研发对业务目标的贡献程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.3 与发现问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 具有信息采集和监控的手段；b) 具有诊断和分析问题的方法。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 围绕监控工具、人工巡查、问题发生风险，针对投入产出和对需方业务影响建立分析模型，根据模型分析选择合适的策略；b) 形成独立研发运维服务交付监控工具的能力；c) 协助需方发现业务中的问题与改进机会；d) 通过定量分析，识别潜在的问题与风险。</td><td style='text-align: center; word-wrap: break-word;'>a) 发现问题技术/监控工具的成本效益分析与收益的比例；b) 发现需方业务问题的数量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 8.4 与解决问题相关的技术</td><td style='text-align: center; word-wrap: break-word;'>a) 解决问题的技术指标或标准；b) 解决问题的方案或手册；c) 测试环境、测试标准和方法。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 研发形成解决需方业务方面问题的方案；b) 建立分析运维服务与需方业务关联度的模型和技术手段。</td><td style='text-align: center; word-wrap: break-word;'>解决问题技术对需方业务改进的贡献度。</td></tr></table>

### 8.5 过程要求

提升（量化）级的过程要求见表 20。

---

<div style="text-align: center;">表 20 提升（量化）级的过程要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.2 服务级别管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立服务目录;b) 与需方签订 SLA;c) 根据需方的考核评估要求, 建立 SLA 考核自评估机制, 包括 SLA 完成情况、达成率;d) 在 SLA 评估后制定改进内容及改进措施。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外, 还应满足以下要求:a) 使用信息技术手段, 分析运维服务历史数据、需方业务发展需求、服务质量数据和组织运维服务能力现状, 形成服务级别指标基线和指标库, 以确保服务级别协议中的指标适用性和有效性;b) 根据服务级别协议的量化分析结果, 对服务目录做动态优化调整。</td><td style='text-align: center; word-wrap: break-word;'>a) 针对服务级别协议的统计分析;b) 服务目录的优化调整记录。</td></tr><tr><td rowspan="2">GB/T 28827.1-20129.3 服务报告</td><td style='text-align: center; word-wrap: break-word;'>a) 与服务报告过程一致的活动, 包括建立、审批、分发、归档等;b) 服务报告计划, 包括提交方式、时间、需方接收对象等;</td><td rowspan="2">除达到二级要求外, 还应满足以下要求:a) 对运维服务质量趋势和服务级别指标达成情况进行分析, 发现影响业务价值的风险, 以便及时采取措施;b) 分析运维交付数据、新技术或新工具的应用价值、客户满意度或服务体验调查结果等数据;c) 若需方存在第三方运维服务审计, 运维服务报告应进行调整, 满足第三方审计的要求;d) 使用信息技术手段改进服务报告管理过程, 实现数据整合和共享, 以支撑供方服务能力改进。</td><td rowspan="2">服务报告管理过程的数据整合和共享程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c) 服务报告模板, 包括格式、提纲等。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.4 事件管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与事件管理过程一致的活动, 包括事件受理、分类和初步支持、调查和诊断、解决、进展监控与跟踪、关闭等;b) 事件分类、分级机制;c) 事件升级机制;d) 满意度调查机制;e) 事件解决评估机制, 包括事件解决率、事件平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外, 还应满足以下要求:a) 使用自动化工具的手段分析事件记录, 发现分级服务或服务管理方面潜在的问题, 识别需方业务改进机会;b) 主动基于服务质量评价指标调查的事件处理的客户满意度或服务体验。并使用自动化工具在适合的图表中展示;c) 能及时识别服务目录或服务级别协议的变更, 动态调整事件分级、分类、事件管理指标等;d) 使用自动化工具主动整合事件记录, 并共享给其它管理流程或工具。</td><td style='text-align: center; word-wrap: break-word;'>a) 事件管理的量化分析和优化过程记录;b) 向其它管理流程所提供数据的准确性和时效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-20129.5 问题管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与问题管理过程一致的活动, 包括问题建立、分类、调查和诊断、解决、关闭等;b) 问题分类管理机制, 包括问题的影响范围、重要程度、紧急程度并确定优先级;c) 问题导入知识库机制;d) 问题解决评估机制, 包括问题解决率、问题平均解决时间等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外, 还应满足以下要求:a) 以可量化方式, 分析问题解决效果;b) 使用自动化工具分析问题解决效率, 识别技术能力缺陷并改进;c) 基于运维服务的问题管理结果, 提出需方在运维服务管理或需方业务方面改进建议。</td><td style='text-align: center; word-wrap: break-word;'>问题管理的量化分析和过程优化程度。</td></tr></table>

---

<div style="text-align: center;">表 20（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>标准条款要求</td><td style='text-align: center; word-wrap: break-word;'>成熟度要求</td><td style='text-align: center; word-wrap: break-word;'>关键指标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.6 配置管理</td><td style='text-align: center; word-wrap: break-word;'>a) 与配置管理过程一致的活动，包括识别、记录、更新和审核等；b) 配置数据库管理机制；c) 配置项审核机制。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 持续改进配置管理过程以适应业务变化；b) 配置管理能进一步记录信息资产与业务之间的关系，以及业务间的关系；c) 配置数据能被其他管理流程方便的获取。</td><td style='text-align: center; word-wrap: break-word;'>a) 配置管理数据库交付过程的支撑程度；b) 配置管理与设备生命周期管理的融合程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.7 变更管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与变更管理过程一致的活动，包括请求、评估、审批、实施、确认和回顾等；b) 建立变更类型和范围的管理机制；c) 对变更完成情况进行统计分析，包括未经批准变更数量及占比、不同类型的变更数量及占比、不成功的变更数量及占比、取消的变更数量及占比、变更关联的配置数。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 持续改进变更管理过程以适应业务变化；b) 主动分析变更项的业务价值及影响，以指导变更决策；c) 变更管理能主动从其他流程获取数据以支持决策。</td><td style='text-align: center; word-wrap: break-word;'>a) 变更管理量化分析和分析有效性；b) 变更管理对提升需求价值和运维服务管理水平的作用程度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.8 发布管理</td><td style='text-align: center; word-wrap: break-word;'>a) 建立与发布管理过程一致的活动，包括规划、设计、建设、配置和测试等；b) 建立发布类型和范围的管理机制；c) 制定完整的方案，包括发布计划、回退方案、发布记录等；d) 对发布完成情况进行统计分析，包括发布成功率、发布及时率、是否更新配置管理数据库等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 持续改进发布管理过程以适应业务变化；b) 主动分析发布计划对业务的价值及影响，以指导发布策略。</td><td style='text-align: center; word-wrap: break-word;'>发布管理量化分析的有效性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1-2012 9.9 信息安全管理</td><td style='text-align: center; word-wrap: break-word;'>a) 符合相关法律法规的规定，满足需方对运行维护服务过程的信息安全需求和供方本身信息安全需求；b) 建立与信息安全管理过程一致的活动，包括识别、评估、处置和改进等。</td><td style='text-align: center; word-wrap: break-word;'>除达到二级要求外，还应满足以下要求：a) 持续改进信息安全管理过程以适应业务变化；b) 参照GB/T 22080—2008建立完整的信息安全管理体系，确保运维服务人员安全、提供运维服务的物理环境安全，以及支持运维服务业务的系统安全（包括运维工具、知识库和服务台等）。</td><td style='text-align: center; word-wrap: break-word;'>信息安全管理体系的完整性和有效性。</td></tr></table>

---

## 附录 A

## (资料性附录)

## 本模型与运维系列标准的关系

### A.1 ITSS 简介

ITSS（Information Technology Service Standards，简称ITSS）是一套成体系和综合配套的信息技术服务标准库，全面规范了信息技术服务产品及其组成要素，用于指导实施标准化和可信赖的信息技术服务。

## a) ITSS的来源

ITSS是在工业和信息化部、国家标准化管理委员会的联合指导下，由国家信息技术服务标准工作组（以下简称：ITSS工作组）组织研究制定的，是我国信息技术服务行业最佳实践的总结和提升，也是我国从事信息技术服务研发、供应、推广和应用等各类组织自主创新成果的固化。

## b) ITSS的原理

ITSS充分借鉴了质量管理原理和过程改进方法，规定了信息技术服务的组成要素和生命周期，并对其进行标准化，如图A.1所示：

<div style="text-align: center;"><img src="imgs/img_in_chart_box_387_716_819_1136.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图A.1 ITSS原理</div>


## c) 组成要素

信息技术服务由人员（People）、过程（Process）、技术（Technology）和资源（Resource）四个要素组成，简称PPTR。其中：

1）人员：指提供信息技术服务所需的人员及其知识、经验和技能要求；

2）过程：指提供信息技术服务时，合理利用必要的资源，将输入转化为输出的一组相互关联和结构化的活动；

3）技术：指交付满足质量要求的信息技术服务应使用的技术或应具备的技术能力；

4）资源：指提供信息技术服务所依存和产生的有形及无形资产。

## d) 生命周期

信息技术服务生命周期由规划设计（Planning & Design）、部署实施（Implementing）、服务运营（Operation）、持续改进（Improvement）和监督管理（Supervision）5个阶段组成，简称PIOIS。其中：

---

1）规划设计：从客户业务战略出发，以需求为中心，参照 ITSS 对信息技术服务进行全面系统的战略规划和设计，为信息技术服务的部署实施做好准备，以确保提供满足客户需求的信息技术服务；

2）部署实施：在规划设计基础上，依据 ITSS 建立管理体系、部署专用工具及服务解决方案；

3）服务运营：根据服务部署情况，依据 ITSS，采用过程方法，全面管理基础设施、服务流程、人员和业务连续性，实现业务运营与信息技术服务运营融合；

4）持续改进：根据服务运营的实际情况，定期评审信息技术服务满足业务运营的情况，以及信息技术服务本身存在的缺陷，提出改进策略和方案，并对信息技术服务进行重新规划设计和部署实施，以提高信息技术服务质量；

5）监督管理：本阶段主要依据 ITSS 对信息技术服务服务质量进行评价，并对服务供方的服务过程、交付结果实施监督和绩效评估。

## e) ITSS的内容

ITSS是依据上述原理制定的一系列标准，是一套完整的信息技术服务标准体系，包含了信息技术服务的规划设计、部署实施、服务运营、持续改进和监督管理等全生命周期阶段应遵循的标准，涉及咨询设计、集成实施、运行维护、服务管控、服务运营和服务外包等业务领域。

### A.2 运维服务能力成熟度与 ITSS 标准的关系

按照ITSS体系框架的规划，涉及运维服务领域的标准共6项，如图A.2所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_154_747_969_1156.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图A.2 运维服务各项标准及其关系</div>


目前，国家标准化管理委员会已颁布三项运维服务系列标准，分别是图A.2中所示的第1部分、第2部分和第3部分。本模型规定的运维服务能力成熟度等级与运维系列标准的关系如图A.3所示。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_261_202_946_681.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图A.3 运维服务能力成熟度与ITSS标准的关系</div>


## a) 基本级与标准的关系

按照本模型第5章的规定，基本级主要依据GB/T 28827.1实施了运维服务能力管理，对模型的实施不要求全面性和系统性，而是根据业务发展情况，采用了模型提供的方法。

## b) 拓展级与标准的关系

按照本模型第6章的规定，拓展级主要依据GB/T 28827.1实施运维服务能力管理，对模型的实施要求全面性和系统性，并能与业务发展情况相结合。

## c) 改进（协同）级与标准的关系

按照本模型第7章的规定，改进（协同）级主要在全面和系统实施GB/T 28827.1的基础上，从保障运维服务交付质量的角度出发，并结合协同改进运维服务能力的要求，增加了实施GB/T 28827.2和GB/T 28827.3的要求。

## d) 提升（量化）级与标准的关系

按照本模型第8章的规定，改进（协同）级主要在全面和系统实施GB/T 28827.1，以及从量化提升运维服务能力的角度出发实施GB/T 28827.2和GB/T 28827.3的基础上，增加了实施《信息技术服务质量评价指标体系》（报批稿）中有关运维服务质量评价内容的要求。

---

## 附录 B

## (资料性附录)

## 运维服务能力成熟度各等级之间的关系

下表分别从涉及标准、运维能力管理体系的主要特征、管理体系 PDCA 循环的特征、人员要素的特征、资源要素的特征、技术要素的特征、过程要素的特征、等级特征等几个方面描述了运维服务能力成熟度各个等级之间的关系：

<div style="text-align: center;">附表 B.1 运维服务能力成熟度各等级之间的关系</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>等级维度</td><td style='text-align: center; word-wrap: break-word;'>第四级（基本级）</td><td style='text-align: center; word-wrap: break-word;'>第三级（拓展级）</td><td style='text-align: center; word-wrap: break-word;'>第二级（协同改进（协同）级）</td><td style='text-align: center; word-wrap: break-word;'>第一级（量化提升（量化）级）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>涉及标准</td><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1</td><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1</td><td style='text-align: center; word-wrap: break-word;'>GB/T 28827.1, GB/T 28827.2, GB/T 28827.1, GB/T 28827.2, GB/T 28827.3, GB/T 28827.3</td><td style='text-align: center; word-wrap: break-word;'>《信息技术服务质量评价指标体系》（报批稿）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运维能力管理体系</td><td style='text-align: center; word-wrap: break-word;'>遵照《运维通用要求》建立管理体系。要求管理体系真实存在，文档和记录基本符合通用要求的立意。</td><td style='text-align: center; word-wrap: break-word;'>管理体系与通用要求逐条对标，各种流程规范和记录文档完整。</td><td style='text-align: center; word-wrap: break-word;'>a）运维能力管理体系中的各个组成要素（人员、服务台、工具、备件、技术、流程等）相互关联和协同，共同支撑企业的运维业务；b）运维能力管理体系与企业的实际情况和业务状况是相互匹配的，管理体系具有良好的合理性和适用性。备注：成熟度二级主要解决运维能力管理体系“好不好”的问题。</td><td style='text-align: center; word-wrap: break-word;'>a）基于对历史数据的统计分析，实现量化和精确的运维能力管理，运维能力管理体系具有持续优化的特征；b）运维管理体系与组织业务现状和发展目标相互融合；c）基于运维管理通用要求，提出适用于企业的创新的管理方法。备注：成熟度一级主要解决运维能力管理体系“精不精”的问题。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>主要特征</td><td style='text-align: center; word-wrap: break-word;'>备注：成熟度四级主要解决运维能力管理体系“有没有”的问题。</td><td style='text-align: center; word-wrap: break-word;'>备注：成熟度三级主要解决运维能力管理体系“全不全”的问题。</td><td style='text-align: center; word-wrap: break-word;'>况和业务状况是相互匹配的，管理体系具有良好的合理性和适用性。备注：成熟度二级主要解决运维能力管理体系“好不好”的问题。</td><td style='text-align: center; word-wrap: break-word;'>c）基于运维管理通用要求，提出适用于企业的创新的管理方法。备注：成熟度一级主要解决运维能力管理体系“精不精”的问题。</td></tr></table>

---

<div style="text-align: center;">附表 B.1（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>等级维度</td><td style='text-align: center; word-wrap: break-word;'>第四级（基本级）</td><td style='text-align: center; word-wrap: break-word;'>第三级（拓展级）</td><td style='text-align: center; word-wrap: break-word;'>第二级（协同改进（协同）级）</td><td style='text-align: center; word-wrap: break-word;'>第一级（量化提升（量化）级）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>管理体系PDCA循环的特征</td><td style='text-align: center; word-wrap: break-word;'>a）存在运维能力管理的策划和实施活动和相关证据；b）有文档化的服务目录和运维服务能力计划。</td><td style='text-align: center; word-wrap: break-word;'>a）有完整的策划、实施、检查和改进循环；b）服务目录完全覆盖企业业务范围；c）运维服务能力计划中体现出四要素的要求。区别：除了满足四级特征，重点审查检查和改进活动，以及服务目录及服务能力计划的完整性。</td><td style='text-align: center; word-wrap: break-word;'>a）运维能力管理的PDCA过程对于改善运维服务质量具有实际效果；b）服务目录、运维能力管理计划、组织结构等管理要素之间的协调一致性；c）建立起完整的交付策划、实施、检查和改进循环；d）交付过程文档和记录是完整的、准确的；e）交付方式、交付内容和结果符合SLA要求；f）建立起了较为完整的应急响应体系，包括应急组织、应急制度、风险评估、应急预案、应急响应记录、应急工作总结和评估改进记录等。区别：除了满足三级特征，重点审查PDCA循环的合理性和适用性，以及业务目标、运维能力管理计划、服务目录、组织结构、人员能力等管理要素之间的匹配度和协调一致性。</td><td style='text-align: center; word-wrap: break-word;'>a）建立起了完善的运维过程记录及历史数据分析体系；b）基于量化数据分析结果，持续性地对运维能力管理体系进行改善；c）建立针对交付内容和交付结果的数据分析模型；d）对交付方式和交付内容进行持续改进；e）完全遵照应急响应规范（GB/T 28827.3）建立起了完善的应急响应体系；f）应急响应体系具有良好的实用性和合理性，同时确保风险评估完整，应急事件分级合理，预案启动及时；g）建立量化模型分析应急响应体系的效率和效果，并持续改进；h）参照“运维服务质量评价”标准建立完善的服务质量评价体系，包括质量评价工作的计划、实施记录、检查和改进记录。区别：除了满足二级特征，重点审查PDCA循环的量化分析过程和持续性，以及运维能力管理体系对业务的正向促进作用。</td></tr></table>

---

<div style="text-align: center;">附表 B.1（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>等级维度</td><td style='text-align: center; word-wrap: break-word;'>第四级（基本级）</td><td style='text-align: center; word-wrap: break-word;'>第三级（拓展级）</td><td style='text-align: center; word-wrap: break-word;'>第二级（协同改进（协同）级）</td><td style='text-align: center; word-wrap: break-word;'>第一级（量化提升（量化）级）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>人员要素的特征</td><td style='text-align: center; word-wrap: break-word;'>遵照运维能力管理计划，建立起基本的岗位任职体系、人员培训及绩效考核的制度。</td><td style='text-align: center; word-wrap: break-word;'>a）人员管理相关计划、文档和记录必须是完整存档的，包括岗位说明书、招聘计划和记录、培训计划和记录、考核记录、人员证书等；b）人员管理具有良好的计划性，有岗位备份、人员储备、技能提升计划等内容。区别：除了满足四级特征，重点审查人员管理完整性、计划性和前瞻性。</td><td style='text-align: center; word-wrap: break-word;'>a）根据业务现状和业务发展需要来设计和完善运维人员管理体制；b）人员储备、人员培训、人员绩效考核的结果必须对运维业务是有正向促进作用的；c）将应急人员纳入统一的运维人员管理。区别：除了满足三级特征，重点审查人员管理体制在企业的合理性，以及与运维业务发展需要的联动关系。</td><td style='text-align: center; word-wrap: break-word;'>a）量化的、精细化的人员管理体制，包括任职资格体系、人员培训和绩效考核方法；b）人员和岗位结构可根据业务需要实现动态调整和优化。区别：除了满足二级特征，重点审查人员管理体制是否可实现量化分析和持续优化。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资源要素的特征</td><td style='text-align: center; word-wrap: break-word;'>基本具备了可支撑运维业务需要的资源体系，包括服务台、必要的知识库和技术工具</td><td style='text-align: center; word-wrap: break-word;'>a）与备件库、知识库、监控工具相关的记录和信息是完整和准确的；b）建立与服务台、备件库、知识库等资源相关的规范的管理制度。区别：除了满足四级特征，重点审查资源管理过程的规范性和信息准确性。</td><td style='text-align: center; word-wrap: break-word;'>a）各种资源可完整覆盖业务种类；b）建立起了较为完善的备件库；c）监控工具、服务台、备件库、知识库等资源可以有效提升服务级别，缩短故障排出时间和客户满意度。区别：除了满足三级特征，重点审查各类资源对业务的完整覆盖和支撑作用。</td><td style='text-align: center; word-wrap: break-word;'>a）对各类资源的使用情况和业务价值进行量化分析；b）对各类资源的配备和利用进行持续优化。区别：除了满足二级特征，重点审查资源使用情况的量化分析和持续优化。</td></tr></table>

---

<div style="text-align: center;">附表 B.1（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>等级维度</td><td style='text-align: center; word-wrap: break-word;'>第四级（基本级）</td><td style='text-align: center; word-wrap: break-word;'>第三级（拓展级）</td><td style='text-align: center; word-wrap: break-word;'>第二级（协同改进（协同）级）</td><td style='text-align: center; word-wrap: break-word;'>第一级（量化提升（量化）级）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>技术要素的特征</td><td style='text-align: center; word-wrap: break-word;'>a）具备开展技术研发的基本条件；b）有与核心业务基本匹配的技术解决方案。</td><td style='text-align: center; word-wrap: break-word;'>a）有较为完整的技术研发规划；b）有满足业务发展需求的研发投入和研发人员；c）技术研发成果得到有效应用。区别：除了满足四级特征，重点审查研发规划的完整性和落实情况。</td><td style='text-align: center; word-wrap: break-word;'>a）根据业务发展情况，制定合理的技术研发规划；b）技术研发投入和研发人员与业务发展、技术研发目标协调匹配；c）运维团队能系统理解和正确使用各种技术研发成果，各种发现问题及解决问题的技术在实际运维业务活动中得到合理利用，支撑业务发展的作用明显。区别：除了满足三级特征，重点审查研发成果和各种技术对运维业务的实际应用效果和实用性。</td><td style='text-align: center; word-wrap: break-word;'>a）技术研发规划及系统覆盖支撑业务发展的综合需求，同时又具备前瞻性和创新性；b）有合理的技术研发投入和研发人员，并有明确的绩效考核机制；c）技术研发对于新业务拓展和运维业务目标达成具有显著贡献，并通过量化分析来优化研发方向和研发投入。区别：除了满足二级特征，重点审查各项技术应用于业务拓展的价值，以及技术研发与运维业务拓展之间的联动关系。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>过程要素的特征</td><td style='text-align: center; word-wrap: break-word;'>a）存在文档化的服务目录、SLA及服务报告；b）建立文件化的流程管理制度，对事件、问题、配置和变更发布等相关活动进行说明。</td><td style='text-align: center; word-wrap: break-word;'>a）依据业务需求保障服务目录的完整性、信息准确性和及时更新；b）建立服务报告的管理制度并得到有效执行；c）事件管理、问题管理、变更管理、配置管理等相关制度和流程的完整性和规范性。区别：除了满足四级特征，重点审查流程制度的完整性和规范性，以及各种文档、记录/报告的完整性和及时性。</td><td style='text-align: center; word-wrap: break-word;'>a）各流程之间具有良好的协同一致性；b）运维流程与组织运营相关管理制度有效融合，至少包括采购、财务、研发等方面的管理制度；c）必要时，实现组织运维服务相关流程与客户运维服务管理的有效衔接。区别：除了满足三级特征，重点审查运维流程之间的协同性，以及运维流程与企业内外部相关制度规范的协同性。</td><td style='text-align: center; word-wrap: break-word;'>a）建立起了对各流程的量化指标和统计分析制度；b）建立对各流程优化改善的效果评估；c）若需要对外发包，则需参照ITSS《外包服务提供方通用要求》对供应商进行外包管理。区别：除了满足二级特征，重点审查针对流程的量化分析和持续改进。</td></tr></table>

---

<div style="text-align: center;">附表 B.1（续）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>等级维度</td><td style='text-align: center; word-wrap: break-word;'>第四级（基本级）</td><td style='text-align: center; word-wrap: break-word;'>第三级（拓展级）</td><td style='text-align: center; word-wrap: break-word;'>第二级（协同改进（协同）级）</td><td style='text-align: center; word-wrap: break-word;'>第一级（量化提升（量化）级）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>等级特征</td><td style='text-align: center; word-wrap: break-word;'>a）管理层对实施运维服务能力管理具有基本的意识，依据模型初步建立运维服务能力管理体系；b）个人技术水平对运维服务能力的提升发挥关键作用；c）基本建成框架性的运维服务管理过程，并得到实施；d）具备运维技术研发基本条件，同时在体系化方面继续保持改进；e）根据各类运维服务活动要求提供资源支持，逐步积累和利用知识资源。</td><td style='text-align: center; word-wrap: break-word;'>a）管理层对实施运维服务能力管理具有较高的认识，能结合运维服务业务的发展需要，策划和实施运维服务能力管理，并初步实现运维服务的产品化；b）依据模型建立完整的运维服务能力管理体系，并得到有效实施；c）单个业务单元或运维服务团队的综合能力决定了整体运维服务能力，同时在单个业务单元或服务团队的综合能力的均衡和协同方面继续保持提升；d）运维服务管理过程全面覆盖运维相关的组织，在过程的精细化、执行效果一致性方面继续保持改进；e）运维技术研发与业务发展基本匹配，并确保技术研发的持续性；f）为运维服务业务发展提供所必须的资源支持，在核心工具、知识库、服务台等之间的集成水平和整体协调性方面继续保持改进。</td><td style='text-align: center; word-wrap: break-word;'>a）管理层对实施运维服务能力管理具有明确的方向和目标，运维业务的发展由运维交付、质量管理、人力资源管理、技术研发等部门协同推进，实现运维服务产品标准化，具备运维服务集成能力；b）依据模型建立完善的运维服务能力管理体系，在运维服务设计、研发和交付方面具备考核服务能力指标体系和方法；c）运维服务管理过程实现精细化，并能通过完备的制度保障实现一致性和准确性；d）运维技术研发与业务发展协调一致并具备前瞻性，拥有业务发展所需的核心技术；e）能够统一规划运维业务发展所需的资源，各类资源之间具有较强的关联度和协调性，共享水平高，资源的提供和使用初步实现量化管理。</td><td style='text-align: center; word-wrap: break-word;'>a）管理层对实施运维服务能力管理具有明确的量化指标，实现有效的管控，并能合理有效使用各种指标数据进行决策；b）运维服务能力管理体系能够基于量化指标进行优化提升；c）建立覆盖全面的运维服务管理过程改进量化指标体系，并能根据量化数据进行过程再造，实现改进与变革；d）运维技术研发与商业目标协调一致，具有技术创新能力，建立技术促进业务发展的合理绩效指标，并根据数据积累提升技术研发能力水平；e）根据运维服务质量的数据积累，优化改进运维服务能力。</td></tr></table>

---

## 参 考 文 献

[1] ITIL $ ^{\circledR} $ Maturity Model V1

[2] CMMI $ ^{\textregistered} $ for Service, Version 1.3

___