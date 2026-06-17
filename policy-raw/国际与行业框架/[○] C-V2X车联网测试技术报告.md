---
title: "C-V2X车联网测试技术报告"
source: "工业信息化&工业互联网/C-V2X车联网测试技术报告.pdf"
type: "pdf"
processed: "2026-04-23T06:25:49.345919"
---

## C-V2X车联网 测试技术报告

<div style="text-align: center;"><img src="imgs/img_in_chart_box_0_442_1190_1419.jpg" alt="Image" width="100%" /></div>


---

## 前言

C-V2X 车联网系统相较于传统的蜂窝移动通信网络系统，引入了新的通信接口，新的终端和业务平台，车联网应用对通信系统有低时延、高可靠性的需求。因此，对于 C-V2X 车联网系统的测试验证需适应车联网的系统架构和车联网应用特点，面向车联网应用的需求，结合业务场景对终端、网络、平台等各部分开展测试。

本技术报告基于 C-V2X 车联网系统架构，从车联网系统测试验证需求出发，提出了 C-V2X 车联网测试技术体系。中国移动联合产业合作伙伴基于此测试技术体系完成了 LTE-V2X 车联网测试实践，正在开展 5G-V2X 车联网测试，希望为产业开展 C-V2X 车联网测试提供参考，并期待与更多的产业合作伙伴共同开展测试实践，推进车联网产业发展。

---

## 联合编写单位（排名不分先后）

中国移动通信有限公司研究院：郑银香、潘洁、张彦、李凤、董耘天、金杰敏、沈

旭、徐要强、张翼鹏、牛亚文

中移物联网有限公司：杨松、谢星伟

中国移动上海产业研究院：蒋鑫、王宇欣

公安部交通管理科学研究所：孙正良

中国信息通信研究院：郭美英

华为技术有限公司：张平

中兴通讯股份有限公司：张俊彦

大唐高鸿数据网络技术股份有限公司：赵丽

上海国际汽车城(集团)有限公司：李霖

上海汽车集团股份有限公司：高吉

北京星云互联科技有限公司：姚知含

北京千方科技股份有限公司：孙亚夫

北京智能车联产业创新中心有限公司：吴琼、王想亭

大唐移动通信设备有限公司：张岩

---

## 目录

1. 概述 ..... 7  
2. C-V2X 车联网测试技术体系 ..... 9  
3. LTE-V2X 车联网测试 ..... 14  
3.1 概述 ..... 14  
3.2 测试方法研究 ..... 14  
3.2.1 子系统测试 ..... 14  
3.2.2 业务场景测试 ..... 21  
3.3 测试仪表研发 ..... 24  
3.3.1 设备性能测试仪表 ..... 25  
3.3.2 网络优化测试仪表 ..... 26  
3.4 测试实践 ..... 26  
4. 5G-V2X 车联网测试 ..... 30  
4.1 概述 ..... 30  
4.2 测试内容 ..... 30  
4.2.1 面向 5G-V2X R15 技术试验的测试内容 ..... 30  
4.2.2 面向 5G-V2X R16 概念验证的测试内容 ..... 31  
4.3 测试方法研究 ..... 32  
4.3.1 子系统测试 ..... 32  
4.3.2 业务场景测试 ..... 37  
4.4 测试仪表研发 ..... 38

---

4.4.1 设备性能测试仪表 ..... 39  
4.4.2 网络优化测试仪表 ..... 39  
4.4.3 应用功能仿真测试仪表 ..... 39  
4.5 测试计划 ..... 40  
5. 结束语 ..... 42  
缩略语列表 ..... 43  
参考文献 ..... 44

---

### 1. 概述

---

### 1. 概述

C-V2X（Cellular-V2X）是基于蜂窝网通信技术演进形成的车用无线通信技术，包含LTE-V2X技术和5G-V2X技术。与LTE-V2X类似，5G-V2X支持基于Uu接口的网络通信模式（NR Uu）以及基于PC5接口的终端直连通信模式（NR PC5）。根据5GUu接口支持3GPP标准版本能力的不同，5G-V2X分成R15和R16两个阶段。

随着 C-V2X 技术的不断发展，标准体系不断完善，车联网设备与产品也日渐成熟。为满足 C-V2X 车联网系统端到端测试验证及测试需求，自 2017 年至 2020 年 11 月，中国移动联合公安部交科所、华为、中兴、大唐、星云互联、上汽、上海汽车城等产业合作伙伴，开展了 C-V2X 车联网测试技术体系研究，制定了业务应用以及终端、无线、网络、平台的端到端测试方案，先后完成 LTE-V2X 概念验证和技术试验，验证了 LTE-V2X 车联网端到端通信及业务性能和业务解决方案的可行性，促进了车联网设备成熟，推动了车联网产业发展。

5G－V2X 可以为更高等级的车联网应用提供更大带宽、更低时延、更高可靠性的通信服务。2021 年中国移动联合通信、汽车、交通、应用企业等产业合作伙伴正在逐步开展基于 5G NR R15 的技术试验以及 5G-V2X R16 概念验证，评估 5G 终端、网络、平台等对典型车联网应用的支持能力，探索有价值自动驾驶应用场景。希望在 5G-V2X 测试中与更多的产业伙伴合作，开展完备的 5G-V2X 技术试验，促进车联网产业成熟。

---

### 2. C-V2X车联网测试技术体系

<div style="text-align: center;"><img src="imgs/img_in_image_box_1_438_968_1221.jpg" alt="Image" width="81%" /></div>


---

### 2. C-V2X 车联网测试技术体系

随着车联网业务的发展及逐渐成熟，产业上逐渐发展出一套基于“云-管-端”的车联网系统架构以支持车联网应用的实现。

<div style="text-align: center;"><img src="imgs/img_in_image_box_224_388_963_913.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2-1 车联网系统架构</div>


“云”是指 V2X 基础平台、高精度定位平台等基础能力平台，以及第三方行业应用平台。其中，V2X 基础能力平台与数据交换网关、边缘计算云上的 V2X 边缘计算节点共同构成了多级的 V2X 平台，是“云”平台层的核心，它汇聚来自车辆、路侧设备、公安交管系统以及各类应用平台的 V2X 相关信息，并实现各类信息数据的高速计算与实时分发、数据的存储与分析功能。高精度定位平台与高精度定位基准站共同为车联网应用提供高精度定位服务。V2X 平台对接高精度定位平台、其他行业平台以及上层应用平台，协同实现智慧出行、地图导航等多种应用。

“管”指为车联网业务数据提供传输的通信网络，包括 4G 网络、5G 网络及行业专网等。相较于普通的蜂窝网络，为满足车联网业务对时延、可靠性等严格的通信

---

指标要求，4G、5G 网络都做了相应的技术增强。例如 4G 网络为支持车联网业务的低时延要求增强了直连通信、基站资源调度等特性。5G 网络支持直连通信的单播、组播等特性以保证车联网业务的高可靠性。行业专网可为行业应用平台提供专门的数据管道，如公安交管平台可通过专网连接至路侧设备获取交通信息数据，专网可保障行业应用数据传输的 QoS 以及安全性等要求。

“端”在广义上包括路侧单元（road side unit，RSU）、车载终端、便携式终端等多形态的设备。路侧单元是路侧信息的汇集点，一方面可将收集到的道路交通信息，发送给云平台或用户终端，另一方面可将云平台下发的业务数据广播给附近的用户终端。车载终端、便携式终端是用户获取车联网业务的入口，车联网交通参与者通过终端经通信网络，最终接入至云平台层，可获取“云”上各方提供的多种多样的车联网应用服务。

C-V2X 车联网系统相较于传统的蜂窝移动通信网络系统，引入了新的通信接口、新的平台、新的终端。为了满足 C-V2X 车联网系统端到端测试验证及测试需求，中国移动联合各单位基于 C-V2X 车联网系统架构，围绕“端-管-云-应用”，开展了 C-V2X 车联网测试技术及体系研究，C-V2X 车联网测试技术体系架构。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_184_156_957_658.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 2-2 C-V2X 车联网测试技术体系架构</div>


本测试技术体系包括测试系统、测试指标、测试仪表几个部分。

## 1 ）测试系统

C-V2X 车联网系统测试主要围绕 “应用” 以及 “云”、“管”、“端” 侧设备进行。“应用” 主要是针对车联网应用场景的端到端测试；“云” 侧包括 V2X 基础平台、高精度定位平台等；“管” 侧主要评估 4G、5G 核心网和基站；“端” 侧包括路侧设备单元（RSU）、路边计算单元 MEC，感知设备毫米波雷达和相机，以及车载设备单元（OBU）等。根据上述对车联网系统的拆解，可以将测试系统分为两部分：一部分是业务场景测试，主要完成基于车联网应用场景的业务功能测试和不同用户规模的性能测试；另一部分是将 “端”、“管”、“云” 的测试组件对应到终端、无线、网络、平台几个测试子系统，对各个测试子系统开展对应的测试。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_149_1030_472.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2-3 C-V2X 车联网测试技术体系分解</div>


## 2 ）测试指标

车联网系统除了传统通信网络的网络覆盖性能、信号强度、用户容量、峰值速率、边缘速率等性能指标要求外，还包括面向车联网应用的时延性能要求、可靠性性能要求等。

## 3 ）测试仪表

测试仪表是测试技术体系重要组成部分，可以有效支撑各子系统测试。

测试仪表可用于测量模拟覆盖信号强度、模拟信号变化、模拟背景业务等，可支持性能统计如时延统计，丢包率统计等，还可支持测试消息打点等。测试仪表包括设备性能相关仪表和网络规划相关仪表。设备性能相关仪表用于评测设备功能、射频性能、时延、容量等性能。网络规划相关仪表用于评测网络建设覆盖、干扰、切换等相关性能。

---

### 3. LTE-V2X车联网 测试

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_423_1189_1433.jpg" alt="Image" width="99%" /></div>


---

### 3. LTE-V2X 车联网测试

### 3.1 概述

基于上述 C-V2X 车联网测试技术体系研究，中国移动联合公安部交科所、华为、中兴、大唐、星云互联、上海汽车城等合作伙伴开展了面向 LTE-V2X 车联网子系统（包括终端、无线、平台）以及业务场景的测试方法研究，并完成了对应测试验证。通过 LTE-V2X 车联网测试，验证了 LTE-V2X 关键技术，评估了 C-V2X 终端、平台等产品成熟度，评估了大规模终端设备场景下的业务通信性能，验证了辅助驾驶业务场景的方案可行性，促进了车联网设备的成熟，推动了车联网产业发展。

### 3.2 测试方法研究

#### 3.2.1 子系统测试

##### 3.2.1.1 终端测试

车联网基础通信终端设备包括路侧设备单元 RSU 以及车载单元 OBU。终端测试主要包括射频测试、协议一致性测试、可靠性测试、互操作性测试、覆盖性能测试和 V2X 功能测试等几个部分。

## 1 ) 射频测试

车联网 RSU 及 OBU 设备射频测试方法参考 CCSA 行标 YDT 3755-2020《基于 LTE 的车联网无线通信技术 支持直连通信的路侧设备技术要求》和 YDT 3755-2020《基于 LTE 的车联网无线通信技术 支持直连通信的终端设备技术要求》进行。主要包括发射机和接收机两部分测试，发射机主要是发射功率测试、输出功率动态调整测

---

试、频率误差测试等，接收机主要是参考灵敏度电平测试、最大输入电平测试等。

## 2 ) 协议一致性测试

设备满足协议一致性要求是设备规范化以及后续实现互联互通的基础。协议一致性测试又分成不同层的协议测试，典型的协议栈分层架构从下到上分别为：接入层、网络层、安全层、消息层、应用层，各层需遵循所对应的标准规范进行测试。其中，接入层应遵循 YDT 3593-2019《基于 LTE 的车联网无线通信技术 总体技术要求》、YDT 3340-2018《基于 LTE 的车联网无线通信技术 空口技术要求》；网络层和安全层应遵循 YDT 3707-2020《基于 LTE 的车联网无线通信技术 网络层技术要求》、《基于 LTE 的车联网无线通信技术 应用标识分配及映射》和《基于 LTE 的车联网无线通信技术 安全认证技术要求》，消息层应遵循 YDT 3709-2020《基于 LTE 的车联网无线通信技术 消息层技术要求》。

协议一致性测试采用被测终端与系统模拟器通过射频线缆互联的测试方式，根据具体测试点不同，适当增加频谱仪、信道模拟器、干扰信号发生器等仪器设备以满足监测和测试条件的要求。

<div style="text-align: center;"><img src="imgs/img_in_image_box_342_1030_888_1285.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图3-1 协议一致性测试拓扑示意图</div>


## 3 ) 可靠性测试

由于路侧设备一般要固定安装在室外，因此需要满足公路室外部署条件可靠性需求：

---

• MTBF>50000 小时

• 温度  $ -40^{\circ}C \sim +70^{\circ}C $

• 保护级别 IP65

• 功率  $ 23\text{dBm} \pm 2\text{dB} $

• EIRP 29dbm±2dB

• 相对湿度 5% RH ~ 95% RH

• 防雷 5KA

- 抗震 满足国家抗震要求，参考 GR-63-CORE Zone4 等级要求、中国通信行业标准 YD5083 要求

• EMC 满足国家 EMC 认证要求，参考 GB9254 或 EN301 489 标准

## 4 ) 互操作性测试

终端的互操作性测试包括 PC5 接口通信的互联互通和 V2X 消息的互联互通两个方面。

PC5 接口通信的互联互通测试，主要是验证异厂商设备 PC5 ☐基本通信功能的互通性，可参考 C-V2X 工作组《LTE V2X 终端间互操作测试规范》进行。

应用层互联互通测试主要是验证不同厂家终端设备的应用层 V2X 消息互通性。测试时一厂家终端设备发送 V2X 消息，其余厂家设备接收，通过比对接收到的 V2X 消息与发送 V2X 消息内容是否一致来判断是否实现互联互通。

## 5 ) 覆盖性能测试

终端设备的覆盖测试主要是测试 RSU 设备及 OBU 设备的通信传输覆盖距离，为后续设备部署提供参考依据。

测试时，分别选择 LOS 场景及典型 NLOS 场景，接收终端从距离发送终端 0 米

---

的地方开始逐渐拉远，直至丢包率大于10%的点停止，记录该点的位置及发送与接收终端的log信息，测量终止点与起始点之间的距离得到发送终端的覆盖距离。

## 6 ) V2X 功能测试

终端 V2X 功能测试主要是验证终端设备是否具备实现 V2X 业务的功能, 以及 V2X 应用场景功能的触发是否及时，预警是否合理。LTE-V2X 阶段的 V2X 消息主要包括 TCSAE 53-2020《合作式智能运输系统车用通信系统应用层及应用数据交互标准（第一阶段）》中的 BSM、SPAT、RSI、MAP 等消息。

V2X 应用场景功能预警测试主要通过外部高精度定位设备采集测试车辆位置信息、实时计算两车间距与 TTC，并通过数据采集设备采集车端 HMI 预警的声、光、图像等信息完成对应用场景的测试与评估。

##### 3.2.1.2 无线测试

LTE-V2X 无线测试主要聚焦于 LTE-V2X 引入的无线特性及关键技术相关的无线性能测试和容量测试。

## 1 ）无线关键技术测试

为支持车联网应用的实现，3GPP R14 版本中引入了 QCI 值为 3 的专用承载新技术特性，考虑到上行预调度也与资源调度相关，可以将 QCI3 专载与上行预调度相结合进行测试验证。

- 专用 QoS 承载：V2X 消息可以通过 non-GBR 和 GBR 承载传输，对 V2X 消息的单播传输，为满足 V2X 消息传送的 QoS 要求，采用一个 Non-GBR QCI 值（QCI 79）和一个 GBR QCI 值（QCI 3）。

上行预调度：预调度可以减少系统时延，当打开预调度开关时，在上行给UE

---

保留资源，当 UE 有调度需求时，有较大概率能得到最快响应，使得数据传输的时延变小，但响应系统的额外开销会增大。

LTE-V2X 无线性能测试主要关注 R14 引入的 QCI3 专载以及 QCI3 专载与上行预调度相结合对网络时延性能的改善性。测试时，在不同信号强度及网络负荷条件下，通过对比用户使用 QCI3 专载与 QCI9 默载的时延性能对比、上行预调度功能是否开启的时延性能对比、用户使用 QCI3 专载且与上行预调度结合和用户使用 QCI9 默载的时延性能来评估 QCI3 与上行预调度对时延性能的改善效果。

## 2 ) 容量测试

LTE-V2X 车联网业务与传统业务不同，具有大并发、高频次的特点。通过车联网容量测试，可评估网络可支持的车联网用户数，为网络优化提供一定依据。

大容量测试需借助测试工具接入并同时控制多终端设备，实现模拟业务数据的发送，同时使用测试工具监测各个用户终端的平均上下行速率、端到端平均时延、端到端平均丢包率。在满足车联网业务需求条件下，即用户的速率、时延和丢包率性能均达到一定指标的条件下，得到不同基站 PRB 利用率所对应的车联网用户数，从而可以有效评估车联网用户容量。

##### 3.2.1.3 平台测试

在辅助驾驶阶段开展的平台测试主要验证 V2X 基础平台对车联网应用落地的支撑能力，包括接口测试、功能测试及性能测试。接口测试是指各类消息接入接口的连通性测试；功能测试是验证平台业务功能的准确性和完备性，包括终端接入授权认证流程测试、业务消息高速转发功能以及异常测试。性能测试是测试平台在满足低时延、高可靠性要求下的数据并发量指标，性能测试还可以给出服务器数量、并发用户数、

---

时延的关系，以满足对平台服务器部署评估的要求。

平台测试网络拓扑以及软硬件环境如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_297_274_906_785.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 3-2 平台测试网络拓扑图</div>


## 1 ）平台接口测试

平台接口测试的目的是测试平台是否可以正确解析与 RSU 及 OBU 接口的 V2X 消息，包括 SPAT、MAP、RSI、RSM、BSM 等。测试时用 RSU 和 OBU 按照一定频率发送 SPAT、MAP、RSI、RSM 和 BSM 消息，查看平台能否按照发送频率正常接收到消息并成功解析。

## 2 ) 平台功能测试

平台功能测试包括终端接入鉴权测试、业务消息计算转发功能测试和异常处理测试。

终端接入鉴权测试是测试终端鉴权功能，包括终端授权认证测试、终端获取加密密钥测试、终端初始化测试等。

业务消息计算转发功能测试的目的是测试平台实现将 V2X 消息推送至对应 OBU

---

设备的功能，V2X 消息包括 SPAT、MAP、RSI、RSM 等。测试时 OBU 按照 10Hz 频率发送 BSM 信息到平台，RSU 按照 2Hz 频率发送 SPAT 消息和 MAP 消息到平台，按照 1Hz 频率发送 RSI、RSM 消息到平台；V2X 平台接收并解析 BSM 消息得到车辆位置信息，并根据位置信息下发相应的 SPAT 和 MAP 消息以及 RSI、RSM 消息；OBU 接收到 V2X 平台推送的 SPAT、MAP、RSI、RSM 消息。

异常处理测试是测试平台收到异常消息时的处理功能。处理流程为：平台解析接收到的消息，发现与协议不一致时，丢弃此数据包，继续处理其他数据，不影响测试平台的运行。测试的异常消息包括异常的 SPAT、MAP、BSM、RSI、RSM 等消息。测试时利用测试工具发送 SPAT、MAP、RSI、RSM 的数据包，使用 OBU 发送 BSM 数据包，所发的数据包的报文不符合国标 ASN.1 的 PER 编解码的报文数据包，查看平台对异常数据的处理是否影响平台正常运行。

## 3 ) 平台系统测试功能模拟

平台需具备场景模拟功能，如通过 RSM、RSI 消息模拟安全类、信息指示类场景。

能控制场景触发频率和影响范围，用以测试“管”、“端”侧设备功能和性能。

## 4 ) 平台性能测试

平台性能测试是测试平台在满足低时延、高可靠性要求下的数据并发量指标，性能测试还可以给出服务器数量、并发用户数、时延的关系，以满足对服务器部署评估的要求。

测试时通过 Jmeter 模拟不同并发量的 BSM 消息，其中 BSM 的位置信息是在测试区域范围内随机生成，本区域内路口的 SPAT 消息由 RSU 模拟器发送。测试平台（单节点）在 1 万/秒并发及 10 万/秒并发、平台（三个节点）在 30 万/秒并发、平台（五个节点）在 50 万/秒并发时的处理时延及丢包率。

---

#### 3.2.2 业务场景测试

C-V2X 业务场景测试主要包括面向车联网应用场景的业务功能测试和性能测试，性能测试包括单用户以及不同规模用户设备条件下的性能测试。

C-V2X 业务场景按照自动驾驶级别不同可分为两大类：辅助驾驶业务及自动驾驶业务。结合 SAE 和 5GAA 中对于车联网具体应用场景的定义，对具体应用场景进行场景分级，可参考表 3-1：

<div style="text-align: center;">表 3-1 C-V2X 应用场景分类表</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>行业分类</td><td style='text-align: center; word-wrap: break-word;'>具体应用场景</td><td style='text-align: center; word-wrap: break-word;'>场景阶段</td><td style='text-align: center; word-wrap: break-word;'>场景分级</td><td style='text-align: center; word-wrap: break-word;'>场景要求</td></tr><tr><td rowspan="5">安全类</td><td style='text-align: center; word-wrap: break-word;'>事故预警</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>限速预警</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>匝道汇入</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>施工预警</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>行人预警</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td rowspan="5">信息服务类</td><td style='text-align: center; word-wrap: break-word;'>交通信息播报</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>红绿灯信息推送</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>路面状态播报</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>局部气象播报</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高精地图动态更新</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'>L1\L2辅助驾驶</td></tr><tr><td rowspan="4">效率类</td><td style='text-align: center; word-wrap: break-word;'>特种车辆优先通行</td><td style='text-align: center; word-wrap: break-word;'>阶段一</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>汽车近场支付</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>安全加密</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态车道管理</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>协作式车辆编队</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="5">控类</td><td style='text-align: center; word-wrap: break-word;'>远程遥控自主泊车</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性、高速率</td><td style='text-align: center; word-wrap: break-word;'>L4\L5自动驾驶，5G网络、OBU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>远程遥控驾驶</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性、高速率</td><td style='text-align: center; word-wrap: break-word;'>L4\L5自动驾驶，5G网络、OBU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>远程遥控驾驶-港口或园区作业</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>局域覆盖、时延小、高可靠性、高速率</td><td style='text-align: center; word-wrap: break-word;'>L4\L5自动驾驶，5G网络、OBU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>VR游戏</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L4\L5自动驾驶，5G网络、OBU</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>务类</td><td style='text-align: center; word-wrap: break-word;'>阶段二</td><td style='text-align: center; word-wrap: break-word;'>广域覆盖、时延小、高可靠性</td><td style='text-align: center; word-wrap: break-word;'>L4\L5自动驾驶，5G网络、OBU</td></tr></table>

在 LTE-V2X 阶段（对应阶段一），主要是支持 L1\L2 辅助驾驶业务，在 5G-V2X

---

阶段（对应阶段二），网络可支持 L3-L4 的高级别自动驾驶业务。

辅助驾驶业务提供驾驶员驾驶时所需要的辅助信息，此类业务的业务逻辑相对简单，对网络、终端的性能要求相对较低，易于实现，目前 LTE-V2X 即可满足辅助驾驶业务的需求

## (1) 业务功能测试

业务功能测试主要验证车联网设备端到端实现该业务的流程是否正确，V2X 消息是否可以正确解析，需要显示的 UI 信息或者预警功能是否可正常实现。

虽然不同车联网业务的业务流程不同，但业务功能测试的测试方法是一致的。以PC5接口实现信息提醒类业务为例，其业务流程图如图3-3所示，测试时，RSU与信号机通过网线连接，RSU通过PC5口广播V2X消息；记录OBU展示界面的状态，验证PC5口端到端实现的信息提醒类业务能否正常运行

<div style="text-align: center;"><img src="imgs/img_in_image_box_331_828_804_1359.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">图 3-3 PC5 信息提醒类业务的业务流程</div>


对于 Uu 口的业务功能测试，仍以信息提醒类业务为例，其业务流程图如图 3-4 所示，测试时，RSU 上报提醒类 V2X 消息至 V2X 平台，OBU 上报 BSM 消息至 V2X

---

平台，V2X 平台将接收到的消息进行匹配/更新后推送至 OBU；记录 OBU 展示界面的状态，验证 Uu 口端到端实现的信息提醒类业务能否正常运行。

<div style="text-align: center;"><img src="imgs/img_in_image_box_327_269_832_705.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 3-4 Uu 口信息提醒类业务的业务流程</div>


## (2) 业务性能测试

在辅助驾驶阶段车联网业务较为重要的性能指标主要有时延、可靠性（即丢包率），在自动驾驶阶段，除上述性能指标外，一般还会加上传输速率的指标要求。

本阶段主要关注辅助驾驶类业务的性能。业务性能测试时使用测试工具统计车联网设备在实现具体业务时的端到端时延、丢包率、传输速率以及通信距离、信道繁忙率（CBR：Channel Busy Ratio）、发包间隔（ITT：Inter-Transmit Time）、收包间隔（IPG：Inter-Packet Gap）、位置跟踪误差（TE：Tracking Error）等。

业务性能与测试环境密切相关，在测试时，需选择具有典型参考意义的测试环境，

考虑测试区域内的遮挡情况、路口 RSU 可覆盖的范围、道路测试条件等。

业务性能还与终端设备数量有关，随着 V2X 终端渗透率不断提升，大量终端设备对通信资源的竞争势必会导致终端通信性能的下降。因此在实际测试方案设计时，需要考虑单用户、不同规模用户的场景。为了验证未来商用实际组网的场景，还需要测

---

试大规模终端设备同时发送业务消息时的性能，即所谓的实际道路条件下的大规模测

试验证。C-V2X 规模化的通信性能测试的目的旨在测试验证真实交通场景下 LTE-V2X

在不同的通信环境和信道占用情况下的通信性能，评估智能网联车辆在高渗透率下是

否能够满足最小性能要求，是否能够支撑道路安全应用的正常的工作。

规模化直连通信测试系统架构如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_205_492_986_883.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 3-5 规模化 C-V2X 直连通信的测试系统</div>


### 3.3 测试仪表研发

通信技术是车联网的技术基础，是智能网联汽车发展的重要助推剂，由此对车联网业务来说智能化、网联化测试需求并存。车联网网联化测试包括从网络通信测试到应用功能验证、应用场景测试验证等多角度测试，测试仪表的开发需要从通信底层到业务上层，满足不同层次的测试需求。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_324_149_859_510.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 3-6 测试仪表对应测试功能框图</div>


#### 3.3.1 设备性能测试仪表

车联网的发展离不开车载和路侧设备，如果将针对终端的测试和针对车联网设备的测试相比的话，针对车联网设备的测试要求更加严格，测试范畴更倾向于实际的安全以及效率，需要对设备的通信能力，比如被测设备的硬件射频性能指标等进行严格的测试。

该类仪表包括非信令射频测试仪表和协议测试仪表。非信令射频测试仪表主要测试信号功率，需对 PC5 接口和 Uu 接口两个接口的射频能力都进行测试，包括信号质量（误差适量幅度，频率误差），信号杂散，信号接收灵敏度等。

协议测试又分成不同层的协议测试，比如接入层的协议一致性测试和应用层的协议一致性测试。接入层的测试应遵循 YDT 3593-2019《基于 LTE 的车联网无线通信技术 总体技术要求》、YDT 3340-2018《基于 LTE 的车联网无线通信技术 空口技术要求》来完成，而应用层的协议一致性根据各个地区的车联网特点进行规范测试。各个地区，如北美，欧盟，日本都有自己的上层协议标准。国内的应用层一致性测试依据 YDT 3709-2020《基于 LTE 的车联网无线通信技术 消息层技术要求》来完成。目

---

前，已有少数仪表公司已投入到 V2X 协议测试仪表的开发中，初步具备了从接入层协议到应用层协议的测试能力。随着车联网场景的丰富和业务能力不断提高，该类仪表还需继续完善。

#### 3.3.2 网络优化测试仪表

基于 LTE-V2X 通信相关测试是车联网业务测试的基础,通信网络作为承载基础,是车联网业务的性能验证是必不可少的一环。LTE-V2X 网络部署和建设是极为重要的,与传统移动蜂窝通信网络类似,有效的检测和评估方法是衡量网络质量的、检验网络性能的主要手段。LTE-V2X 网络优化测试仪表可进行实际道路上的车联网用户路测,能够自适应不同的车联网业务场景,针对车联网业务测试 LTE-V2X 网络通信能力,对覆盖范围、吞吐量、时延、可靠性等关键指标进行采集分析,用于 LTE-V2X 无线网络评估及验证,为 RSU 部署及网络优化提供测试支撑。

车联网 V2X 业务涉及了多个产业的融合，网络测试处于发展初期，V2X 网络优化测试仪表发展仍然比较滞后。芯片、模组、应用集成厂家从自身需求角度开发了一些自用工具，但普遍存在测试数据采集不全面，使用不方便，缺乏统一标准等缺陷。目前，已有专业测试工具厂家开始研发 V2X 网络优化测试仪表，测试工具将可逐步支持从物理层到应用层外场测试各个环节，有望改善目前无合适 V2X 网络优化测试仪表的局面。

### 3.4 测试实践

2017 至 2018 年，中国移动联合华为、上汽、大唐等产业伙伴完成了 LTE-V2X 技术试验，在上海示范区建设 LTE-V2X 试验网，研究包括终端、无线、网络、V2X 平

---

台以及应用的端到端测试方案，验证车联网关键技术有效性、端到端通信性能以及业务方案的可行性。

2019 至 2020 年，中国移动联合公安部交科所、华为、中兴、星云互联、上海汽车城等合作伙伴共同完成了更大规模的 LTE-V2X 测试，验证 C-V2X 芯片及终端、平台等设备成熟度；测试评估了大规模终端设备场景下的业务通信性能，为未来 LTE-V2X 商用提供依据。

1）在终端测试方面，验证了参测设备的射频特性及协议一致性均符合标准要求；

验证参测的后视镜终端及 RSU 设备、OBU 设备可实现 SPAT、BSM、RSI、RSM 消息的收发；验证了异厂商 RSU 及 OBU 设备在通信层面以及消息应用层的互联互通性符合要求；测试了 RSU 设备的覆盖性能，在 LOS 场景下覆盖大于 1000 米，NLOS 场景下当有大型建筑物遮挡时，覆盖约为 250 米，而一般树木遮挡，覆盖范围可达 1000 米；验证了在规模终端设备场景下的测试中，终端性能稳定，可实现 SPAT、BSM、RSI、RSM 等消息的收发且丢包率小于 10%，从而评估了终端设备的成熟度已基本达到预商用要求。

2）在无线测试方面，通过 QCI3 专载与 QCI9 默载对比测试、上行预调度是否开启对比测试以及 QCI3 与上行预调度结合与 QCI9 默载对比测试，验证了 QCI3 专载与上行预调度可减小一定的网络时延；测试了 Uu 口 LTE 小区车联网用户容量，与大网容量基本相符。

3) 在 V2X 基础平台测试方面，验证了平台可实现 V2X 消息的正确解析及根据业务需求进行转发推送，同时测试了平台的大并发时延和丢包率性能满足设定的指标要求。

4) 在业务测试方面，测试了城区环境 20 用户规模下的 V2I 业务的通信性能，

---

参测设备均能达到时延小于 40ms，丢包率小于 10%；测试了 20 用户规模下预警类 V2I 及 V2V 应用的预警性能，所有消息的收发均正常，预警消息均正常触发，相对报警时间较早，给驾驶员预留反应时间充足；在信通院联合星云互联、上海国际汽车城集团举办的“新四跨”暨大规模测试活动，对行业 60 余家终端及整车厂提供了 180 多台终端设备规模下的 V2X 通信性能测试与 V2X 应用场景测试服务，整体上，参加测试的设备平均时延小于 60ms，丢包率小于 10%，均满足辅助驾驶业务需求。由此验证了未来实际交通场景，规模用户场景下的通信性能可以满足 V2X 辅助驾驶业务需求。

---

### 4. 5G-V2X车联网 测试

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_422_1181_1404.jpg" alt="Image" width="99%" /></div>


---

## 4 ．5G-V2X 车联网测试

### 4.1 ．概述

5G – V2X 可以为更高等级的车联网应用提供更大带宽、更低时延、更高可靠性的通信服务，可支持 L3 级别以上的自动驾驶场景。LTE – V2X 技术试验的顺利开展为 5G–V2X 测试积累了宝贵经验，中国移动将继续联合产业合作伙伴，在 2021 年开展 5G–V2X 车联网测试，包括基于 5G NR R15 的技术试验以及 5G–V2X R16 概念验证。

#### 4.2. 测试内容

#### 4.2.1 面向 5G-V2X R15 技术试验的测试内容

5G-V2X R15 技术试验测试技术体系架构与 LTE-V2X 相同，测试系统也包含终端、无线、网络、平台子系统以及业务场景几个部分，在开展测试时包括实验室测试及外场测试。

1）终端测试：

终端实现应用数据交互标准第二阶段中的 V2X 消息的收发功能测试、处理时

延及丢包率性能测试

2）无线测试：

5G 典型车联网业务场景下的用户容量测试

3）网络测试：

单用户/多用户及多业务场景下的网络性能,包括时延、可靠性、传输速率等测试;专网方案测试,包括 V2X 专网用户面下沉到不同位置时延测试、切片选择、ULCL 分流及用户位置区管理等

---

## 4 ）平台测试：

平台与 RSU、OBU 设备收发应用数据交互标准第二阶段中的 V2X 消息的功能及性能测试；高精度定位平台的系统功能、性能、用户体验等多个维度的服务性能指标测试

## 5 ）业务场景测试：

远程遥控驾驶、视野阻碍协助、车载娱乐等典型自动驾驶应用场景端到端的功能及性能测试

#### 4.2.2 面向 5G-V2X R16 概念验证的测试内容

5G-V2X R16 概念验证主要对 5G-V2X Uu 接口 uRLLC 特性与 PC5 接口的组播、单播等特性进行验证。

5G-V2X Uu 方面，将结合大带宽、低时延、高可靠应用场景，如远程遥控驾驶、高精度地图实时更新及共享等自动驾驶场景等，评估及优化与自动驾驶场景技术指标需求相匹配的组网方案。

5G-V2X PC5 方面，将结合车辆编队、路侧传感器辅助感知等典型场景对组内通信、低时延视频及传感器数据传输的需求，引入的单播、组播、HARQ 反馈等关键技术，初步评估 5G-V2X PC5 对典型自动驾驶应用场景的支撑能力和关键技术引入的必要性。

---

### 4.3 测试方法研究

#### 4.3.1 子系统测试

##### 4.3.1.1 终端测试

终端测试主要包括射频测试、协议一致性测试、互操作性测试、覆盖性能测试和V2X功能测试等几个部分。具体的测试方法可参考LTE-V2X阶段的测试方法进行，在协议一致性以及V2X功能上需对包括《合作式智能运输系统车用通信系统应用层及应用数据交互标准第二阶段》中定义的二阶段消息进行测试。

##### 4.3.1.2 无线测试

5G-V2X 无线测试主要聚焦于 5G-V2X 引入的无线特性及关键技术相关的无线性能测试和容量测试。

## 1 ）无线关键技术测试

在 Uu 口方面，为支持车联网应用的实现，3GPP R16 版本中 uRLLC 的关键技术可应用于车联网，如低 MCS、uRLLC 与 eMBB 混合组网优先等技术以满足车联网应用低时延的要求，此外端到端 QoS 预测可预先通知应用程序采取相应调整，提升车联网应用服务质量。

a. 不同可靠性目标的 MCS：5G 支持以两种不同 BLER 为目标的 CQI 与 MCS 映射表格，分别对应 90% 的可靠性要求与 99.999%（低码率）的可靠性要求。针对 eMBB 业务，可选择 90% 可靠性要求的 CQI 与 MCS 映射表格；针对 uRLLC 业务，可选择 99.999% 可靠性要求的 CQI 与 MCS 映射表格，在相同的 MCS 下，uRLLC 的调制阶数偏低，目标码率偏低，增强了调制解

---

调的容错性。

b. QoS 预测：业务数据传输的 QoS 预测，通过收集网络性能、特定区域业务负荷等信息，利用可靠网络性能分析和预测模型，实现对 QoS 的统计和预测，根据应用的订阅请求周期性或者按需地向应用层提供分析或预测结果，使得应用能够调整其运行参数。

c. uRLLC 与 eMBB 混合组网优先：当涉及上行终端间多业务复用时，引入 UL 取消指示，一个用户的 uRLLC 业务达到时可取消另一个用户已调度的 eMBB 传输，以此来及时启动 uRLLC 业务传输，并减少 uRLLC 业务传输时延；同时引入上行功率控制增强，一个用户的 uRLLC 业务与另一个用户已调度的 eMBB 传输冲突时，提高 uRLLC 业务的上行发射功率，从而保证 uRLLC 业务传输可靠性的同时降低对另一个用户 eMBB 性能影响。当涉及上行终端内多业务复用时，引入优先级指示，使高优先级的业务先进行传输。引入不同业务优先级间上行信道的抢占规则，使不同优先级业务冲突时高优先级的业务先传输。

在 PC5 口方面，NR-V2X 对直通链路除了支持广播通信，还增加了单播组播的通信机制；同时对资源分配进行了增强，在测试过程中将重点关注 NR-V2X 增强的关键技术。

a. 单播组播通信方式：NR-V2X 物理层支持广播、单播和多播。直连链路支持单播、组播的 HARQ 反馈机制，支持单播的功率控制机制、CSI 测量和反馈机制。

b. 资源分配增强：NR 直通链路引入 2 阶段 SCI，对占用资源和调制编码信息进行指示，赋予 UE 进行灵活选择资源和调制编码信息的灵活度。NR-V2X

---

的资源分配流程中包含不同窗长的资源感知、灵活的资源排除、考虑反馈机制的资源选择等流程，采用 SPS 和动态资源选择等机制，满足周期性业务和非周期性业务的需求。对于面向自动驾驶等增强应用，业务类型更加复杂，对不同优先级业务提供差异化服务，NR-V2X 引入了资源重评估、抢占及资源重选等过程，保证高优先级业务的传输可靠性，降低资源碰撞概率，提高系统可靠性。

c. 拥塞控制机制：NR-V2X 重用 LTE-V2X 拥塞控制机制基本原理，可以显著减轻拥塞对系统的影响，减少系统干扰，将拥塞控制在系统可以正常工作的范围内。UE 将调整最大发送功率，调制编码策略，最大资源占用比例，最大传输次数等，以适应当前的拥塞程度。

针对无线关键技术的测试主要采用对比测试的方式进行。Uu 口的测试可以对比是否引入该关键技术进行对比，PC5 口的测试可以参考 LTE-V2X PC5 的性能进行对比。

## 2 ) 容量测试

5G-V2X 车联网业务相比 LTE-V2X 阶段，增加了很多大带宽、低时延、高可靠性的业务。通过车联网容量测试，可评估网络可支持的车联网用户数，为网络优化提供一定依据。

大容量测试仍需借助测试工具接入并同时控制多终端设备，模拟业务需针对5G-V2X自动驾驶业务设计。测试工具实现模拟业务数据的发送，同时使用测试工具监测各个用户终端的平均下行速率、端到端平均时延、端到端平均丢包率。在满足车联网业务需求条件下，即用户的传输速率、时延和丢包率性能均达到一定指标的条件下，得到不同基站PRB利用率所对应的车联网用户数，从而可以有效评估车联网用户容

---

量。

##### 4.3.1.3 网络测试

5G-V2X 网络测试包括网络性能测试和专网方案测试。

网络性能测试主要是测试单用户/多用户及多业务场景下的网络性能，包括时延、可靠性、传输速率等，可与无线测试中的容量测试和业务场景测试结合进行。

专网方案测试主要验证 5G SA 网络在通信时延，以及切片选择、ULCL 分流、用户位置区管理等关键技术对车联网应用落地的支撑能力。测试内容包括专网用户面下沉到地市或园区的时延测试，以及切片选择、ULCL 分流及用户位置区管理等关键技术的测试。

## 1 ）V2X专网用户面下沉到不同位置时延测试

为满足车联网应用对低时延的要求，V2X 专网用户面可下沉到地市、园区等不同位置，UPF 对接的 V2X 平台需要就近部署。

V2X 专网用户面下沉到不同位置时延测试目的是测试 V2X 专网不同组网方案的时延性能，为组网设计提供依据。

测试时需搭建典型 UPF 下沉场景，在不同场景下，通过业务 ping 包的方式，测量端到端业务时延，对终端无特殊要求，V2X 平台需要于 UPF 下沉位置就近部署。

针对不同的组网场景，使用不同的测试方法，得到用户面下沉到不同位置时的业务时延：

• 通用组网，使用省通用 UPF，测量端到端业务时延。

• 道路边缘计算，使用下沉到地市的UPF，测量端到端业务时延。

园区边缘计算，使用下沉至园区的UPF，测量端到端业务时延。

---

## 2 ）V2X 专网关键技术测试-切片选择

V2X 专网关键技术测试主要是测试终端支持切片的能力，以及网络切片选择功能是否可以满足 V2X 业务需求。

测试时，V2X 终端签约专用切片 A，专用 UPF 和 V2X 平台，选择接入 2B 大网做测试。V2X 终端发起注册请求，携带请求切片。RAN 选择 AMF 时考虑切片信息。AMF 基于终端请求的、签约的切片信息决策出 Allowed NSSAI。AMF 基于切片选择 SMF，SMF 基于切片选择 UPF。

## 3 ）V2X 专网关键技术测试-ULCL 分流

ULCL 分流所采用的拓扑图如图 4-1 所示，验证网络是否具备 ULCL 分流关键技术能力。

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_789_982_1125.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 4-1 ULCL 分流测试拓扑图</div>


测试时，使用 5G SA 终端，专用 UPF 和 V2X 平台，选择接入大网做测试。PCF 上配置基于用户位置的分流策略(就近接入 V2X 平台)。支持 5G SA 的 V2X 终端注册成功，并建立 PDU 会话。PCF 在建立 PDU 会话时向 SMF 下发该终端的分流策略。终端位置移动，进入特定区域，SMF 为当前终端用户插入 ULCL UPF 进行本地流量卸载。

---

## 4 ）V2X专网关键技术测试-用户位置区管理和移动性管理

本项测试主要是测试用户位置区管理功能是否可以满足园区 V2X 业务需求。

测试时，使用 5G SA 终端，选择接入大网做测试。PCF 上配置 5G SA 终端的感兴趣位置区域 PRA，并在终端建立 PDU 会话时向 SMF 订阅园区位置上报（PRA）。SMF 向 AMF 传递 PRA 信息并订阅 PRA 状态改变事件。用户在园区（在 PRA 区域内）时，可使用专用 DNN 或切片建立会话。用户离开园区（在 PRA 区域外）后，触发 PCF 下发 SM 策略，禁止会话建立或将已存在会话删除。

另外，需要测试用户从 5G 覆盖区域，移动到 LTE-V2X PC5 网络覆盖区域时，业务保持连续，验证不同网络间移动时接口和流程互通正常。

##### 4.3.1.4 平台测试

本阶段的平台测试包括 V2X 基础平台和高精度定位平台的测试。

V2X 基础平台测试主要验证 V2X 平台对车联网应用落地的支撑能力，包括接口测试、功能测试、性能测试。测试方法沿用 LTE-V2X 阶段的测试方法，支持的 V2X 消息集将扩展到《合作式智能运输系统车用通信系统应用层及应用数据交互标准第二阶段》所定义的消息集。

高精度定位平台测试将对平台的系统功能、性能、用户体验等多个维度的服务性能指标测试。测试将基于北斗/GNSS产品技术规范、地基增强系统服务性能规范等相关标准开展。

#### 4.3.2 业务场景测试

参考表 3-2 业务场景分类，在 5G-V2X 阶段（对应阶段二），网络可支持 L3 以

---

上的高级别自动驾驶业务。业务场景测试也主要针对阶段二的业务场景开展。

业务场景测试主要包括车联网应用的业务功能测试和性能测试，性能测试包括单用户以及不同规模终端设备场景下的性能测试。

## 1 ) 业务功能测试

业务功能测试主要验证端到端实现该业务的流程是否正确，V2X 消息是否可以正确解析，需要显示的 UI 信息或者预警功能是否可正常实现。

在 5G-V2X 阶段，业务功能测试可选择远程遥控驾驶、视野阻碍协助、车载娱乐等自动驾驶业务进行验证。

## 2 ) 业务性能测试

车联网业务较为关心的性能指标在自动驾驶阶段一般包括时延、可靠性（即丢包率）和传输速率等。

业务性能测试的方法可以参考 LTE-V2X 阶段的测试方法进行。除了之前关注的时延、丢包率、传输速率等指标，还将关注实现 V2X 业务时的其他性能指标，如信道繁忙率（CBR：Channel Busy Ratio）、发包间隔（ITT：Inter-Transmit Time）、收包间隔（IPG：Inter-Packet Gap）、位置跟踪误差（TE：Tracking Error）等。

### 4.4 测试仪表研发

随着无线通信技术的不断演进，智能网联汽车也向更高级别、更复杂应用方向发展，基于5G构建“人-车-路-云”高度协同的互连环境，实现车路协同控制、车车协同驾驶、高级/完全自动驾驶业务，最终支撑实现完全自动驾驶。对于5G-V2X阶段的车联网测试包括从5G网络通信测试到自动驾驶应用功能验证、应用场景测试验证等多角度测试，测试仪表的开发需要从通信底层到业务上层，满足本阶段的测试需求。

---

#### 4.4.1 设备性能测试仪表

设备性能测试仪表在 LTE-V2X 设备性能测试仪表（参见第 3.3.1 章节）的基础上升级支持 5G，支持 5G Uu 和 PC5 双接口的测试。该类仪表仍需要继续研发升级。

#### 4.4.2 网络优化测试仪表

网络优化测试仪表在 LTE-V2X 网络优化测试仪表（参见第 3.3.2 章节）的基础上升级支持 5G，支持 5G Uu 和 PC5 双接口的测试。该类仪表仍需要继续研发升级。

#### 4.4.3 应用功能仿真测试仪表

该类仪表基于场景模拟 C-V2X 的测试方案, 使用综测仪进行 C-V2X 接入层模拟, 信号收发, 通过专业的车联网仿真软件模拟传输层和网络层, 仿真车辆产生的动态数据, 如车速、位置、车辆之间的距离、障碍物、交通场景等信息, 驱动被测车辆做出决策, 判断是否将产生相关的响应消息, 通过对比结果, 对真实使用场景进行系统级的功能性测试。V2X 应用功能仿真测试仪表需支持 YDT 3709-2020《基于 LTE 的车联网无线通信技术 消息层技术要求》的上层协议, 可以在实现全协议栈的场景模拟下, 进行各种 BSM 消息的发送和接收从而实现各种交通场景下测试, 如紧急制动, 左转辅助, 异常车辆提醒等功能。

此外，该类仪表还需能适配未来车联网中不同形态的车载终端以及路侧设备单元的性能评估需求，兼容实验室和外场多种测试场景，这些将是该类仪表未来的主攻方向，对车联网业务开展及质量保障具有重要的意义。

---

### 4.5 测试计划

结合产业发展现状, 中国移动联合产业合作伙伴正逐步开展 5G-V2X R15 技术试验和 R16 概念验证。

5G-V2X R15 技术试验按照完成实验室测试后开展外场测试的原则进行。目前已经初步完成了实验室测试方案的制定，测试计划按照图 4-2 开展，在 2021 年 12 月完成所有测试。

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_564_1003_778.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 4-2 5G-V2X R15 车联网测试计划</div>


在 5G-V2X R16 概念验证方面，2021 年，中国移动将联合通信、汽车、应用企业等产业合作伙伴开展 5G-V2X R16 概念验证，测试车联网自动驾驶场景对带宽、时延、可靠性的要求。2021 年上半年将进行 5G-V2X Uu 接口 uRLLC 特性与 PC5 接口的组播、单播等特性进行验证。针对 5G-V2X Uu 接口，结合大带宽、低时延应用场景，如远程遥控驾驶、高精度地图实时更新及共享等自动驾驶场景等，评估及优化与自动驾驶场景技术指标需求相匹配的组网方案。针对 5G-V2X PC5 接口，将结合车辆编队、路侧传感器辅助感知等典型场景对组内通信、低时延视频及传感器数据传输的需求，引入的单播、组播、HARQ 反馈等关键技术，初步评估 5G-V2X PC5 对自动驾驶典型应用的支撑能力和关键技术引入的必要性。2021 年后半年及 2022 年，将根据产业发展情况，开展 5G-V2X R16 其他特性的验证，提出未来车联网技术引入建议。

---

### 5. 结束语

<div style="text-align: center;"><img src="imgs/img_in_image_box_3_389_1186_1417.jpg" alt="Image" width="99%" /></div>


---

### 5. 结束语

伴随着 C-V2X 技术的发展以及产业的逐渐成熟，基于 C-V2X 的车联网商用已越来越近。建立完善的 C-V2X 车联网测试技术体系，研究端到端测试方法，对车联网端到端开展测试评估，为车联网走向商用的提供有力保障。

C-V2X 车联网涉及到通信、交通、汽车等各行业，需凝聚产业各方力量共同完成。中国移动非常感谢过去几年中产业合作伙伴的支持，也非常希望在 5G-V2X 测试中与更多的产业伙伴合作，开展完备的 5G-V2X 车联网测试，促进车联网产业成熟。

---

## 缩略语列表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>缩略语</td><td style='text-align: center; word-wrap: break-word;'>英文全名</td><td style='text-align: center; word-wrap: break-word;'>中文解释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BSM</td><td style='text-align: center; word-wrap: break-word;'>Basic Safety Message</td><td style='text-align: center; word-wrap: break-word;'>基本安全消息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C-V2X</td><td style='text-align: center; word-wrap: break-word;'>Cellular Vehicle to Everything</td><td style='text-align: center; word-wrap: break-word;'>基于蜂窝的车用无线通信技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LTE-V2X</td><td style='text-align: center; word-wrap: break-word;'>LTE Vehicle to Everything</td><td style='text-align: center; word-wrap: break-word;'>基于LTE的车用无线通信技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OBU</td><td style='text-align: center; word-wrap: break-word;'>On-Board Unit</td><td style='text-align: center; word-wrap: break-word;'>车载单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCF</td><td style='text-align: center; word-wrap: break-word;'>Policy Control Function</td><td style='text-align: center; word-wrap: break-word;'>策略控制功能网元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PDU</td><td style='text-align: center; word-wrap: break-word;'>Protocol Data Unit</td><td style='text-align: center; word-wrap: break-word;'>协议数据单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSI</td><td style='text-align: center; word-wrap: break-word;'>Rode Side Information</td><td style='text-align: center; word-wrap: break-word;'>路侧信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSM</td><td style='text-align: center; word-wrap: break-word;'>Road Side Message</td><td style='text-align: center; word-wrap: break-word;'>路侧单元消息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSU</td><td style='text-align: center; word-wrap: break-word;'>Road Side Unit</td><td style='text-align: center; word-wrap: break-word;'>路侧单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5G SA</td><td style='text-align: center; word-wrap: break-word;'>5G Standalone</td><td style='text-align: center; word-wrap: break-word;'>5G独立组网</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SMF</td><td style='text-align: center; word-wrap: break-word;'>Session Management Function</td><td style='text-align: center; word-wrap: break-word;'>会话管理功能网元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPAT</td><td style='text-align: center; word-wrap: break-word;'>Signal Phase and Timing Message</td><td style='text-align: center; word-wrap: break-word;'>信号灯相位与配时消息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UL CL</td><td style='text-align: center; word-wrap: break-word;'>Uplink Classifier</td><td style='text-align: center; word-wrap: break-word;'>上行分类器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UPF</td><td style='text-align: center; word-wrap: break-word;'>User Plane Function</td><td style='text-align: center; word-wrap: break-word;'>用户面功能网元</td></tr></table>

---

## 参考文献

[1] YDT 3755-2020《基于 LTE 的车联网无线通信技术 支持直连通信的路侧设备技术要求》

[2] YDT 3755-2020《基于 LTE 的车联网无线通信技术 支持直连通信的终端设备技术要求》

[3] YDT 3593-2019《基于 LTE 的车联网无线通信技术 总体技术要求》

[4] YDT 3340-2018《基于 LTE 的车联网无线通信技术 空口技术要求》

[5] YDT 3707-2020《基于 LTE 的车联网无线通信技术 网络层技术要求》

[6]《基于LTE的车联网无线通信技术 应用标识分配及映射》

[7]《基于 LTE 的车联网无线通信技术 安全认证技术要求》

[8] YDT 3709-2020《基于 LTE 的车联网无线通信技术 消息层技术要求》

[9] TCSAE 53-2020《合作式智能运输系统 车用通信系统应用层及应用数据交互标准（第一阶段）》

[10] T/CSAE 53-2020《合作式智能运输系统车用通信系统应用层及应用数据交互标准第二阶段》