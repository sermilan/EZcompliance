---
title: "SAQ-Instructions-Guidelines-PCI-DSS-v4-0-ZH"
source: "支付卡行业数据安全标准（PCI-DSS）/SAQ-Instructions-Guidelines-PCI-DSS-v4-0-ZH.pdf"
type: "pdf"
processed: "2026-04-23T06:54:36.696614"
---

# Payment Card Industry 数据安全标准

自我评估问卷说明和指南

4.0版

2023年9月

---

<div style="text-align: center;">文件变更</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>日期</td><td style='text-align: center; word-wrap: break-word;'>版本</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2008年10月1日</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>使内容符合新的PCI DSS 1.2版，并实施自最初1.1版以来注意到的微小更改。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2010年10月28日</td><td style='text-align: center; word-wrap: break-word;'>2.0</td><td style='text-align: center; word-wrap: break-word;'>使内容与新PCI DSS 2.0版保持一致，并阐明SAQ环境类型和资格标准。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2012年6月</td><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>为基于网络的虚拟终端商户添加SAQ C-VT。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2015年4月</td><td style='text-align: center; word-wrap: break-word;'>3.1</td><td style='text-align: center; word-wrap: break-word;'>为仅通过经过验证和PCI SSC列出的PCI点对点加密（P2PE）解决方案中包含硬件支付终端处理持卡人数据的商户增加SAQ P2PE-HW。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2016年5月</td><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>与PCI DSS v3.1保持一致，包括添加SAQ A-EP和B-IP，并明确现有SAQ的符合标准。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2018年6月</td><td style='text-align: center; word-wrap: break-word;'>3.2.1</td><td style='text-align: center; word-wrap: break-word;'>更新以与PCI DSS v3.2保持一致，并明确现有SAQ的符合标准。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2023年9月</td><td style='text-align: center; word-wrap: break-word;'>4.0</td><td style='text-align: center; word-wrap: break-word;'>与PCI DSS 3.2.1版保持一致的小幅更新。</td></tr></table>

确认通知：在所有使用目的和情况下，PCI SSC 网站上的英文文本应作为此文件的官方版本。当翻译文本和英文文本之间出现任何歧义和不一致之处时，正确的内容应以该位置的英文文本为准。

---

## 内容

文件变更 ..... i  
关于本文件 ..... 1  
PCI DSS 自我评估：如何适合全部 ..... 1  
SAQ 概述 ..... 2  
了解 PCI DSS 4.0 版 SAQ ..... 4  
PCI DSS 4.0 版 SAQ 有哪些新内容？ ..... 5  
为什么 SAQ 中的一些 PCI DSS 要求包含多个响应复选框 ..... 5  
SAQ 更新对我的组织有哪些影响？ ..... 5  
SAQ SPoC – PCI DSS 4.0 版新 SAQ ..... 6  
SAQ SPoC 的目的是什么？ ..... 6  
SAQ SPoC 与 SAQ P2PE 相比如何？ ..... 6  
P2PE 和 SPoC 缩略语、标准和列表 ..... 7  
概述：SAQ A 和 SAQ A-EP ..... 8  
哪些类型的电子商务实施适用于 SAQ A 与 SAQ A-EP？ ..... 8  
为 PCI DSS 4.0 版增加 SAQ A 新要求的重要性 ..... 9  
SAQ A 与 SAQ A-ep 对比如何？ ..... 10  
概述：SAQ B 和 SAQ B-IP ..... 11  
SAQ B-IP 与 SAQ B 对比如何？ ..... 11  
概述：SAQ C-VT 和 SAQ C ..... 12  
SAQ C-VT 与 SAQ C 对比如何？ ..... 12  
SAQ 资格标准 ..... 13  
SAQ A – 无卡商户，所有帐户数据功能完全外包 ..... 13  
SAQ A-EP – 部分外包 使用第三方网站进行支付处理的电子商务商户 ..... 14  
SAQ B – 仅使用印刷机或独立拨号终端，无电子账户数据存储的商户 ..... 15  
SAQ B-IP – 具有独立、PCI 列出的经批准的 PTS POI 设备，无电子账户数据存储 ..... 16  
SAQ C-VT – 采用基于网络的第三方虚拟支付终端解决方案的商户，不存储电子账户数据 ..... 17  
SAQ C – 连接到互联网的支付应用系统的商户，不存储电子账户数据 ..... 18

---

SAQ P2PE – 仅使用 PCI 所列 P2PE 解决方案支付终端的商户，不存储电子账户数据。……19  
  
SAQ SPoC – 商户仅使用 PCI 列出的经批准的 PTS SCRP 设备和 COTS 设备作为经验证的 PCI 所列 SPoC 解决方案的一部分。……20  
  
适用于商户的 SAQ D – 所有其他符合 SAQ 资格的商户……21  
  
服务提供商 SAQ D – 符合 SAQ 标准的服务提供商……21  
  
哪种 SAQ 最适用于我的环境？……22  
  
附录 A：PCI DSS 4.0 版的 SAQ 有何变化……23

---

## 关于本文件

本文件旨在帮助商户和服务提供商了解支付卡行业数据安全标准（PCI DSS）自我评估问卷（SAQ）。为了解 SAQ 并帮助您所在组织完成 PCI DSS SAQ，以及确定您所在组织适合完成哪种 SAQ，我们建议您完整审阅本说明和指南文件。

## PCI DSS 自我评估：如何适合全部

PCI DSS 及其支持文件代表了一套行业工具，旨在确保安全处理持卡人账户数据。该标准本身提供了一个可行框架，用于制定强大的安全流程，包括预防、检测和应对安全事件。为了降低数据泄露的风险，减轻其可能造成的影响，对于存储、处理或传输账户数据的所有实体来说，通过实施适用的 PCI DSS 要求来保护这些数据十分重要。

下表概述了帮助组织了解 PCI DSS 和自我评估过程的可用工具。

您可以在  $ \underline{\text{www.pcisecuritystandards.org}} $ 找到这些以及其他相关文件。

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_622_1054_1117.jpg" alt="Image" width="72%" /></div>


注意：信息补充仅提供补充信息和指导，不取代或替换 PCI DSS 中的任何要求。

---

## SAQ 概述

PCI DSS 自我评估问卷（SAQ）是符合 SAQ 资格的商户和服务提供商在执行和报告其 PCI DSS 自我评估结果时使用的验证工具。有多个版本的 PCI DSS SAQ 满足不同的商业场景。本文档是为了帮助符合 SAQ 资格的组织确定哪些 SAQ 最适合其所在环境。

PCI DSS SAQ 是商户和服务提供商的替代验证工具，收单行或支付品牌无需提交 PCI DSS 合规性报告（ROC）。“符合 SAQ 资格”是指商户或服务提供商：

根据支付品牌合规计划，有资格进行自我评估以验证其 PCI DSS 合规性，

符合所选 SAQ 中指定的 SAQ 资格标准。

在开始自我评估之前，各组织有责任确认其符合特定 SAQ 的所有资格标准。

注意：鼓励所有完成 SAQ 的实体联系管理合规计划并将提交 SAQ 的组织，例如收单行（商户银行）或支付品牌，以确认其符合完成 SAQ 的资格，以验证 PCI DSS 合规性，并了解具体要求或说明。

## 每个 PCI DSS SAQ 由以下部分组成:

1. 完成自我评估调查问卷：此部分包括具体 SAQ 资格标准，以及协助自我评估过程的完成说明和指导。有关每个 SAQ 资格标准，请参阅本文档中“选择最适用于您所在组织的 SAQ 和认证”。

此外，每个 SAQ 包括自我评估完成步骤、预期的测试活动、需求响应选项、不适用需求的指导、法律例外使用和其他 PCI SSC 资源。

2. 遵从性证明书：该认证是实体完成适用 SAQ 的资格声明，以及其对 PCI DSS 自我评估结果的认证。每个 SAQ 中的合规性证明由第 1 部分组成：评估资料及第 3 部分：认证和验证详细信息。

3. PCI DSS 要求：每个 SAQ 的第 2 部分包括适用于在 SAQ 资格标准中确定的环境的 PCI DSS 要求，以及一个供实体记录每个要求响应的位置。此部分还包括适用于该 SAQ 的附录（例如，用于记录补偿控制的使用，以及描述任何不适用的响应）。

---

## 补偿性控制

当组织因合法和记录的技术或业务限制而无法满足所述的 PCI DSS 要求，但通过实施替代控制已充分减轻了相关风险时，可以考虑补偿控制。为实现一个或多个 PCI DSS 要求的补偿控制，您所在组织应做以下工作：

1. 按照 PCI DSS 附录 B“补偿控制”中概述的程序定义和记录补偿控制，包括完成补偿控制每项要求的补偿控制工作表（CCW）。

2. 通过填写附录 B 记录每项补偿控制：SAQ 中补偿控制工作表。

对于符合补偿控制的各项要求，必须填写补偿控制工作表（CCW）。

额外的补偿控制工作表可以在 PCI SSC 网站上找到。

3. 对于符合补偿控制的各项要求，请通过检查“CCW 就位”一栏来回应 SAQ 中的要求。

## 专业协助及培训

如果您希望聘请安全专业人员帮助您进行自我评估，我们建议您考虑联系合格安全评估员（QSA）。QSA已接受PCI SSC培训，进行PCI DSS评估，并在PCI SSC网站上列出。

PCI SSC 网站是获取其他资源的主要来源，包括：

• PCI DSS 术语、缩略语和缩写词汇表

· 常见问题解答（FAQ）

· 网络研讨会

· 信息补充和指南

• SAQ 表格和合规证明

· 小商户资源。

注意：信息补充材料是对 PCI DSS 的补充，用于识别满足 PCI DSS 要求的额外考虑因素和建议。不会改变、消除或取代 PCI DSS 或其任何要求。

PCI SSC 还提供了一些培训计划，帮助建立组织人员的意识。例如 PCI 意识、PCI 专业（PCIP）计划和内部安全评估员（ISA）计划。

请参阅 www.pcisecuritystandards.org 获取更多信息。

付款相关的培训计划和资源也可以从支付品牌和/或您的商户收单组织获得。

---

### 了解 PCI DSS 4.0 版 SAQ

下表总结了几种 SAQ 类型，并在接下来的页面中进行了更详细的描述。使用该表来帮助确定适用于您所在组织的 SAQ，然后查看接下来的详细描述，以确保您符合该 SAQ 的所有资格标准。

注意：鼓励所有完成 SAQ 的实体与管理合规计划并将 SAQ 提交给其组织联系，例如收单行（商户银行）或支付品牌，以确认其有资格完成 SAQ 以验证 PCI DSS 合规性，并了解任何特定要求或说明。

对于有资格进行自我评估的服务提供商，唯一适用的 SAQ 是面向服务提供商的 SAQ D。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>SAQ</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>无卡商户（电子商务或邮件/电话订购），将所有帐户数据功能完全外包给 PCI DSS 验证和兼容的第三方。不得在其系统或场所进行电子存储、处理或传输账户数据。 不适用面对面渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A-EP</td><td style='text-align: center; word-wrap: break-word;'>部分将支付处理外包给 PCI DSS 验证和合规的第三方的电子商务商户，其网站本身不接收帐户数据，但会影响支付交易的安全性和/或接受客户帐户数据的页面的完整性。不得在商户的系统或场所进行电子存储、处理或传输账户数据。 仅适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>商户只使用： • 不带电子账户数据存储的印刷机，和/或 • 不带电子账户数据存储的独立拨号终端。 不适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B-IP</td><td style='text-align: center; word-wrap: break-word;'>商户只使用独立、PCI 认证的 PIN 交易安全（PTS）交互点（POI）设备，这些设备与支付处理器有 IP 连接。无电子账户数据存储。 不适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C-VT</td><td style='text-align: center; word-wrap: break-word;'>通过键盘逐笔手动输入付款账户数据到经 PCI DSS 验证和合规的第三方虚拟支付终端解决方案，使用单独计算设备和安全连接的网络浏览器进行交易的商户。无电子账户数据存储。 不适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>与互联网连接的支付应用系统的商户，不存储电子账户数据。 不适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P2PE</td><td style='text-align: center; word-wrap: break-word;'>商户只使用经过验证、PCI 列出的点对点加密（P2PE）解决方案。无法访问明文账户数据，也无法进行电子账户数据存储。 不适用于电子商务渠道。不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPoC*</td><td style='text-align: center; word-wrap: break-word;'>商户使用商用现成移动设备（例如手机或平板电脑），其中配有经 PCI SSC 验证 SPoC 解决方案列表中的安全刷卡读取器。无法访问明文账户数据，也无法进行电子账户数据存储。 不适用于无人值守刷卡、邮购/电话订购（MOTO）或电子商务渠道。 不适用于服务提供商。</td></tr><tr><td rowspan="2">D</td><td style='text-align: center; word-wrap: break-word;'>商户 SAQ D：上述 SAQ 类型描述中未包含的所有商户。 不适用于服务提供商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>服务提供商 SAQ D：由支付品牌定义为有资格完成 SAQ 的所有服务提供商。</td></tr></table>

 $ ^{*} $PCI DSS 4.0 版新 SAQ

---

### PCI DSS 4.0 版 SAQ 有哪些新内容？

4.0 版 SAQ 已更新，提供更多指导、报告信息和资源，支持实体完成自我评估流程。一般来说，每个 SAQ 都进行了更新，反映 PCI DSS 4.0 版中要求的更改，重述每个 SAQ 要求，反映 PCI DSS 中使用措辞，并使每个 SAQ 要求的报告响应与 PCI DSS 4.0 版合规模板报告中使用的报告响应保持一致。有关所有 SAQ 的一般更改的详细信息，请参见附录 A：SAQS 在 PCI DSS 4.0 版中的变化

## 为什么 SAQ 中的一些 PCI DSS 要求包含多个响应复选框

对于 SAQ 中的大多数 PCI DSS 要求，只有一个复选框供实体选择；然而少数要求包括每个子项都有一个复选框（例如，PCI DSS 要求 6.4.3）。该方法仅用于 SAQ 中的某些需求，通常用于新的和/或复杂的需求，其中每个项目需要不同的测试方法，并强调每个项目都应单独考虑。

有关 SAQ 格式的其他指导和信息，请参阅每个 SAQ 的“填写自我评估问卷”部分。

## SAQ 更新对我的组织有哪些影响？

在 PCI DSS 4.0 版中，有新的 SAQ 以及现有 SAQ 明确资格标准。各组织需要审阅该资格标准，了解哪个 SAQ 最适合贵组织。例如，新 SAQ 可能比以前使用的 SAQ 更符合您所在组织的特定环境。同样，以前完成一种 SAQ 类型的组织也需要审查更新后的 SAQ 资格标准，以确定是否仍然适合其环境。

更新后的 SAQ 包括 PCI DSS 3.2.1 版 SAQ 中未包含的其他 PCI DSS 要求。此更新会影响商户进行自我评估的方式。

欲了解在 PCI DSS 4.0 版对 SAQ A 添加新要求的原因，请参见概述：SAQ A 和 SAQ A-EP 如下。

商户应根据每个 SAQ 定义的资格标准，并根据其收单行或支付品牌的说明，继续选择适用的 SAQ。鼓励商户阅读相关的 PCI DSS 4.0 版 SAQ，1) 确认商户仍然符合资格标准，2) 熟悉该 SAQ 中包含的所有更新措辞和全部要求。

商户不得假设 PCI DSS

3.2.1 版和 4.0 版特定

SAQ 是相同的。



---

### SAQ SPoC – PCI DSS 4.0 版新 SAQ

SAQ SPoC（基于软件的 COTS PIN 输入）是一种新 SAQ，适用于使用商用现成配有安全读卡器移动设备的商户（例如，手机或平板电脑），是 PCI SSC 验证基于软件 COTS PIN 输入（SPoC）解决方案列表 SPoC 解决方案的一部分。要符合此 SAQ 的资格，商户必须仅通过安全卡读取器 PIN（SCRP）输入账户数据，作为经过验证的 PCI SSC SPoC 解决方案的一部分。

SPoC 解决方案的列表可在此处找到：PCI SPoC 解决方案

## SAQ SPoC 的目的是什么？

SAQ SPoC 是为使用通用商用现货（COTS）移动设备刷卡商户开发的。这意味着移动设备（例如，手机或平板电脑）不必仅用于支付或移动设备专用于支付渠道。COTS 移动设备与 PCI 所列安全读卡器-PIN（SCRP）设备一起使用，作为 PCI SSC SPoC 解决方案的一部分，从而安全处理帐户数据。请注意，此 SAQ 不适用于带有非 PTS 列出的磁条读取器（MSR）的 SPoC 解决方案。此 SAQ 可用于 PTS 所列包含 MSR 功能的 SCRP。

SAQ SPoC 显著减少了使用 PCI SSC 所列的 SPoC 解决方案的商户适用的 PCI DSS 要求数量。

## SAQ SPoC 与 SAQ P2PE 相比如何？

下表提供了 SAQ P2PE 和 SAQ SPoC 之间一些关键相似点和不同点的高级概述。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>SAQ P2PE</td><td style='text-align: center; word-wrap: break-word;'>SAQ SPoC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCI 所列 P2PE 解决方案中经 PTS 批准的 POI 设备</td><td style='text-align: center; word-wrap: break-word;'>PCI 所列 SPoC 解决方案中 COTS 设备和经 PTS 批准的 SCRP 设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用于：</td><td style='text-align: center; word-wrap: break-word;'>有卡或无卡（邮寄/电话订购）商户</td><td style='text-align: center; word-wrap: break-word;'>有人值守刷卡商户（接触式芯片、非接触式、基于 SCRP 磁条）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支付终端</td><td style='text-align: center; word-wrap: break-word;'>付款是通过 PTS 批准的 POI 处理，作为 PCI 所列 P2PE 解决方案的一部分</td><td style='text-align: center; word-wrap: break-word;'>持卡人数据被输入到 PTS 批准的 SCRP 设备中，作为 PCI 列出的 SPoC 解决方案的一部分</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账户数据传输</td><td style='text-align: center; word-wrap: break-word;'>仅来自 PTS POI 设备作为经过验证 PTI 所列 P2PE 解决方案的一部分</td><td style='text-align: center; word-wrap: break-word;'>仅使用 PTS SCRP 设备作为经过验证的 PTI 所列 SPoC 解决方案的一部分</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业系统</td><td colspan="2">无法访问任何计算机系统上的明文帐户数据商户不得以其他方式存储、处理或以电子方式传输账户数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据保留</td><td colspan="2">商户只保留带有账户数据的纸质报告或收据，这些文件不会以电子方式接收</td></tr></table>

此表旨在提供 SAQ P2PE 和 SAQ SPoC 的对比，不取代或替换任何 SAQ 资格标准。

---

## P2PE 和 SPoC 缩略语、标准和列表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>首字母缩略词</td><td style='text-align: center; word-wrap: break-word;'>定义及相关标准</td><td style='text-align: center; word-wrap: break-word;'>解决方案/设备清单 $ ^{*} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>P2PE</td><td style='text-align: center; word-wrap: break-word;'>点对点加密标准</td><td style='text-align: center; word-wrap: break-word;'>$ \underline{\text{PCI P2PE 解决方案}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PTS POI</td><td style='text-align: center; word-wrap: break-word;'>PIN 交易安全（PTS）标准交互点（POI）批准类</td><td style='text-align: center; word-wrap: break-word;'>$ \underline{\text{经批准的 PTS 设备}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPoC</td><td style='text-align: center; word-wrap: break-word;'>基于软件的 COTS（商用现成）标准上的 PIN 输入</td><td style='text-align: center; word-wrap: break-word;'>$ \underline{\text{PCI SPoC 解决方案}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PTS SCRP</td><td style='text-align: center; word-wrap: break-word;'>PIN 交易安全（PTS）标准安全读卡器-PIN（SCRP）批准等级</td><td style='text-align: center; word-wrap: break-word;'>$ \underline{\text{经批准的 PTS 设备}} $</td></tr></table>

* 确认所列解决方案和设备符合 PCI 标准和相关程序指南中定义的要求。

---

## 概述：SAQ A 和 SAQ A-EP

SAQ A 适用于完全将所有账户数据功能外包给经 PCI DSS 验证和合规的第三方服务提供商（TPSP）的无卡支付（邮寄/电话订购或电子商务）商户。SAQ A 商户不以电子方式存储、处理或传输其系统或场所的任何帐户数据。

SAQ A-EP 适用于部分外包电子商务交易管理的商户，但其网站功能会影响支付交易的安全性。

使用 SAQ A，SAQ A-EP 商户不会在其系统或场所上电子存储、处理或传输任何账户数据，而是完全依赖第三方支付服务提供商（TPSP）来处理这些功能。所有帐户数据的处理都外包给 SAQ A 和 SAQ A-EP 的 PCI DSS 验证的 TPSP/支付处理方。

SAQ A-EP 包括额外的安全控制，用于保护控制或管理支付交易的商户网站，即使这些网站不存储、处理或传输帐户数据。这是为了减少这些网站的漏洞被用来泄露帐户数据的可能性。

## 哪些类型的电子商务实施适用于 SAQ A 与 SAQ A-EP?

为了符合 SAQ A 的资格，电子商务商户必须满足 SAQ A 中详细列出的所有资格标准，包括在商户网站上没有捕获付款信息的程序或应用代码。SAQ 解决的电子商务实施示例包括：

商户无法访问其网站，网站完全由兼容 TPSP/支付处理方托管和管理。

商户网站包含一个 URL 链接，将用户从商户网站重定向到 PCI DSS 兼容的 TPSP/处理方，促进支付过程。

商户网站提供一个内联框架（iframe）到 PCI DSS 兼容的 TPSP/处理方，促进支付过程。

如果支付页面中的任何元素来自商户网站，则不适用 SAQ A；然而可能适用 SAQ A-EP。SAQ A-EP 涉及的电子商务实施示例包括：

商户网站创建支付表单，支付数据直接从消费者浏览器传递到支付处理器（通常称为“直接交付”）。

商户网站加载或提供在消费者浏览器中运行的脚本（例如 JavaScript），并提供支持创建支付页面和/或将数据传输给支付处理器的功能。

---

下表说明了常见的电子商务方法和 SAQ 可能适用的方法：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>电子商务法</td><td style='text-align: center; word-wrap: break-word;'>符合资格商户的SAQ类型</td><td style='text-align: center; word-wrap: break-word;'>PCI DSS 4.0 版要求数量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>完全外包。商家无法访问自己网站。</td><td rowspan="3">SAQ A</td><td style='text-align: center; word-wrap: break-word;'>11*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>完全外包。商户网站将客户重定向到符合规定的 TPSP（例如，URL 重定向）。</td><td style='text-align: center; word-wrap: break-word;'>27*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>完全外包。商户网站包含一个符合规定的 TPSP 嵌入式付款页面/表单（例如，内联框架）。</td><td style='text-align: center; word-wrap: break-word;'>29*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>除支付页面外全部外包。</td><td rowspan="2">SAQ A-EP</td><td style='text-align: center; word-wrap: break-word;'>139</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商户网站创建支付表单，支付数据直接从消费者浏览器传递给 TPSP（通常称为“直接交付”）。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>除支付页面外全部外包。</td><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商户网站加载或提供在消费者浏览器中运行的脚本（例如，JavaScript）。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>所有其他电子商务方法和实现。</td><td style='text-align: center; word-wrap: break-word;'>商户 SAQ D</td><td style='text-align: center; word-wrap: break-word;'>所有 PCI DSS 要求</td></tr></table>

SAQ A 邮寄/电话订购（MOTO）渠道的标准不包括在本表中。

* 通过 SAQ A 中的解释注释中查看适用要求。

### 为 PCI DSS 4.0 版增加 SAQ A 新要求的重要性

PCI DSS 4.0 版的 SAQ A 包括解决针对 SAQ A 商家的常见漏洞所需的额外安全控制，特别是保护以下网站：1）将支付交易重定向到符合 PCI DSS 的 TPSP 或 2）包含符合 PCI DSS 的 TPSP 的嵌入式付款页面/表格。为了降低常见违规行为，SAQ A 中包括以下新要求（注意：此列表强调专门解决近期电子商务违规行为而增加的要求；这非 SAQ A 包含的所有新要求列表）：

PCI DSS 要求 6.4.3 管理支付页面脚本。目的是让商户管理商户网站上的支付页面脚本。

PCI DSS 要求 11.3.2 每 90 天至少扫描一次外部漏洞，要求 11.3.2.1 在发生重大变化后进行外部漏洞扫描。目的是让商户扫描并解决商户网站上的任何漏洞。

PCI DSS 要求 11.6.1 部署更改和篡改检测机制，用于检测 HTTP 标头和支付页面内容未经授权的修改，并提供警报。目的是让商户在商家网站上部署此种机制，并响应警报。

---

## SAQ A 与 SAQ A-EP 对比如何？

下表提供了 SAQ A 和 SAQ A-EP 的一些关键相似点和不同点的高级概述。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>SAQ A</td><td style='text-align: center; word-wrap: break-word;'>SAQ A-EP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>所有账户数据功能完全外包</td><td style='text-align: center; word-wrap: break-word;'>部分外包电子商务支付渠道</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用于：</td><td style='text-align: center; word-wrap: break-word;'>无卡支付商户（电子商务或邮件/电话订购） $ ^{*} $</td><td style='text-align: center; word-wrap: break-word;'>电子商务商户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>功能外包</td><td style='text-align: center; word-wrap: break-word;'>所有账户数据的处理完全外包给符合PCI DSS的第三方服务提供商（TPSP）/支付处理方</td><td style='text-align: center; word-wrap: break-word;'>除付款页面外，所有账户数据的处理都完全外包给符合PCI DSS的TPSP/支付处理方</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支付页面</td><td style='text-align: center; word-wrap: break-word;'>提供给客户浏览器的所有支付页面/表格元素仅来自且直接来自于符合PCI DSS的TPSP/支付处理方</td><td style='text-align: center; word-wrap: break-word;'>提供给客户浏览器支付页面的每个要素都来自商户的网站或符合PCI DSS的TPSP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>第三方合规性</td><td colspan="2">商户确认所有TPSP均符合商户所使用服务的PCI DSS标准</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业系统</td><td colspan="2">商户不在商户系统或内部以电子方式存储、处理或传输任何账户数据，而是完全依靠TPSP来处理所有这些功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据保留</td><td colspan="2">商户保留的任何账户数据是纸质形式（例如，打印报告或收据），这些文件不以电子方式接收</td></tr></table>

*SAQ A 邮寄/电话订购（MOTO）渠道标准不包括在此对比中。

此表旨在提供 SAQ A 和 SAQ A-EP 的对比，不替代或取代任何 SAQ 资格标准。

---

## 概述：SAQ B 和 SAQ B-IP

SAQ B 适用于通过压印机或独立拨出终端处理账户数据的商户。SAQ B 商户可以是实体店（有卡）或邮寄/电话订购商户。符合此 SAQ，独立拨出终端不得连接到商业环境中的其他系统，也不连接到互联网。SAQ B 商家不以电子格式存储账户数据。本 SAQ 不适用于电子商务渠道。

SAQ B-IP 适用于仅使用通过基于 IP 的连接连接到其支付处理器的独立支付终端的商户。为符合 SAQ B-IP 标准，商户必须使用 PCI 认证的 PIN 交易安全（PTS）交互点（POI）设备的支付终端。请注意，使用被归类为安全卡阅读器（SCR）或带有 PIN 的安全卡阅读器（SCRP）的 PTS POI 设备的商户不符合 SAQ B-IP 的资格。

SAQ B-IP 的其他资格标准包括批准的 PTS POI 设备未连接到商业环境中的任何其他类型的系统。这可以通过将 PTS POI 设备与环境中的其他系统隔离开来分段得以实现。与不符合 SAQ B-IP 资格标准的其他类型系统的连接包括但不限于与收银机系统的连接，以及如果 PTO POI 设备依赖于任何其他设备（例如计算机、手机、平板电脑等）来连接到支付处理器。此外，为符合 SAQ B-IP 标准，唯一允许的账户数据传输是从 PTS POI 设备到支付处理器，且商户不得以电子格式存储账户数据。SAQ B-IP 与 SAQ B 一样，不适用于电子商务渠道。

## SAQ B-IP 与 SAQ B 对比如何？

下表提供了 SAQ B 和 SAQ B-ip 的一些关键相似点和不同点的高级概述。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>SAQ B</td><td style='text-align: center; word-wrap: break-word;'>SAQ B-IP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>印刷机或独立拨号终端</td><td style='text-align: center; word-wrap: break-word;'>独立经 PTS 批准且带有 IP 连接的支付终端</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用于:</td><td colspan="2">实体店（有卡）或邮寄/电话订购（无卡）商户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支付终端</td><td style='text-align: center; word-wrap: break-word;'>独立拨号终端</td><td style='text-align: center; word-wrap: break-word;'>独立经 PTS 认证的交互点（POI）设备（不包括安全读卡器（SCR 和安全读卡器 PIN（SCRP））</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>连接</td><td style='text-align: center; word-wrap: break-word;'>通过电话线连接到处理器未连接到其他商业系统或互联网</td><td style='text-align: center; word-wrap: break-word;'>通过 IP 连接到处理器其他 IP 连接 PTS 认证 POI 设备可以位于同一网络区域，但必须与所有其他类型的系统隔离。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账户数据传输</td><td style='text-align: center; word-wrap: break-word;'>仅通过电话线到处理器</td><td style='text-align: center; word-wrap: break-word;'>仅通过 IP 从 PTS 批准的 POI 设备到处理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业系统</td><td colspan="2">商户不以电子格式存储账户数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据保留</td><td colspan="2">商户只保留带有账户数据的纸质报告或收据，这些文件不会以电子方式接收</td></tr></table>

此表旨在提供 SAQ B 和 SAQ B-IP 的对比，不取代或替换任何 SAQ 资格标准。

---

## 概述：SAQ C-VT 和 SAQ C

SAQ C-VT 适用于仅通过与互联网连接的单独计算设备上的第三方虚拟支付终端解决方案处理帐户数据的商户。商户通过安全连接的网络浏览器，将账户数据手动输入到单独计算设备上的虚拟支付终端解决方案中，并由符合 PCI DSS 标准的第三方服务提供商托管的虚拟支付终端解决方案提交付款卡交易以进行授权。SAQ C-VT 商户可以是实体（有卡）或邮寄/电话订购商户。为了符合此 SAQ 资格，商户只能通过一个位于单一位置且与其他位置或系统没有连接的计算设备访问符合 PCI DSS 标准的虚拟支付终端解决方案。

SAQ C 适用于与互联网连接的商户支付应用系统（例如，销售点系统）。SAQ C 商户可以是实体店（有卡）或邮寄/电话订购商户。为了符合此 SAQ 资格，商户支付应用系统不连接到商户环境中的其他系统，并且环境的物理位置未连接到其他场所或位置（仅单个门店）。

## SAQ C-VT 与 SAQ C 对比如何？

下表提供了 SAQ C-VT 与 SAQ C 的一些关键相似点和不同点的高级概述。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>SAQ C-VT</td><td style='text-align: center; word-wrap: break-word;'>SAQ C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基于网络第三方虚拟支付终端解决方案</td><td style='text-align: center; word-wrap: break-word;'>连接到互联网的支付应用系统</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用于:</td><td colspan="2">实体店（有卡）或邮寄/电话订购（无卡）商户</td></tr><tr><td rowspan="2">支付方式</td><td style='text-align: center; word-wrap: break-word;'>账户数据手动输入到第三方虚拟支付终端解决方案中</td><td style='text-align: center; word-wrap: break-word;'>销售点（POS）或其他支付应用系统</td></tr><tr><td colspan="2">单独计算设备和安全连接的网络浏览器</td></tr><tr><td rowspan="3">连接</td><td style='text-align: center; word-wrap: break-word;'>连接到互联网</td><td style='text-align: center; word-wrap: break-word;'>连接到互联网</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未连接到其他位置或系统</td><td style='text-align: center; word-wrap: break-word;'>未连接到其他商户系统</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>与其他场所或地点无连接（仅单个门店）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账户数据传输</td><td style='text-align: center; word-wrap: break-word;'>仅通过互联网连接到符合PCI DSS标准的第三方虚拟支付终端系统的提供商</td><td style='text-align: center; word-wrap: break-word;'>仅通过互联网到处理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业系统</td><td colspan="2">商户不以电子格式存储帐户数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据保留</td><td colspan="2">商户只保留带有账户数据的纸质报告或收据，这些文件不会以电子方式接收</td></tr></table>

此表旨在提供 SAQ C-VT 和 SAQ C 的对比，并不取代或替换任何 SAQ 资格标准。

---

## SAQ 资格标准

## SAQ A—无卡商户，所有帐户数据功能完全外包

SAQ A 仅包括适用于帐户数据功能完全外包给 PCI DSS 认证和合规第三方的商户的 PCI DSS 要求，这些商户仅保留有帐户数据的纸质报告或收据。

SAQ A 商户可能是电子商务或邮购/电话订购商户（虚拟），在其系统或场所不存储、处理或传输任何电子格式的帐户数据。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。



## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ A 商户将确认其符合该支付渠道的资格标准，具体如下：

商户只接受虚拟（电子商务或邮购/电话订购）交易；

所有帐户数据的处理都完全外包给符合 PCI DSS 的第三方服务提供商（TPSP）/支付处理商；

商户不在商户系统或内部以电子方式存储、处理或传输任何帐户数据，而是完全依靠 TPSP 来处理所有这些功能；

商户已经审查了其 TPSP 的 PCI DSS 遵从性证明书，并确认 TPSP 在商户使用的服务方面符合 PCI DSS 的要求；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

此外，对于电子商务渠道：

传递给客户浏览器的所有支付页面/表格元素仅来自于符合 PCI DSS 的 TPSP/支付处理商，并且直接来自于 PCI DSS/支付处理商。

---

## SAQ A-EP – 部分外包 使用第三方网站进行支付处理的电子商务商户

SAQ A-EP 仅包括适用于拥有网站的电子商务商户的 PCI DSS 要求，而该网站本身并不接收帐户数据，但确实影响了支付交易的安全性和/或接受客户帐户数据的页面的完整性。

SAQ A-EP 商户是指将其电子商务支付渠道部分外包给经 PCI DSS 认证并符合要求的第三方并在其系统或场所内不以电子方式存储、处理或传输任何帐户数据的电子商务商户。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。



## 本 SAQ 仅适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ A-EP 商户将确认他们符合该支付渠道的资格标准，具体如下：

商户只接受电子商务交易；

除支付页面外，所有帐户数据的处理都完全外包给符合 PCI DSS 的第三方服务提供商（TPSP）/支付处理商；

商户的电子商务网站不接收帐户数据，但控制客户或其帐户数据如何被重定向到符合 PCI DSS 的 TPSP/支付处理商。

如果商户网站由 TPSP 托管，则 TPSP 符合所有适用的 PCI DSS 要求（如果 TPSP 是一个多用户托管提供商，则包括 PCI DSS 附录 A）；

传递给客户浏览器的支付页面的每个要素都来自商户的网站或符合 PCI DSS 的 TPSP;

商户不在商户系统或内部以电子方式存储、处理或传输任何帐户数据，而是完全依靠 TPSP 来处理所有这些功能；

商户已审查其 TPSP 的 PCI DSS 遵从性证明书，并确认 TPSP 在商户使用的服务方面符合 PCI DSS 的要求；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

注意：就 SAQ A-EP 而言，涉及“持卡人数据环境”的 PCI DSS 要求适用于商户网站。这是因为商户网站会直接影响帐户数据的传输方式，尽管网站本身并不接收帐户数据。

---

## SAQ B – 仅使用印刷机或独立拨号终端，无电子账户数据存储的商户

SAQ B 仅包括适用于仅通过印钞机或独立拨出式终端处理帐户数据的商户的 PCI DSS 要求。SAQ B 商户可以是实体店（实体信用卡）或邮购/电话订购（虚拟信用卡）商户，并且不在任何计算机系统上存储帐户数据。

## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ B 商户将确认其符合该支付渠道的资格标准，具体如下：

商户仅使用印钞机和/或只使用独立的拨出式终端（通过电话线连接到商户处理商）来获取客户的支付卡信息；

独立的拨出式终端没有连接到商户环境内的任何其他系统；

独立的拨出式终端没有连接到互联网；

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。

商户不以电子格式存储帐户数据；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

---

## SAQ B-IP – 具有独立、PCI 列出的经批准的 PTS POI 设备，无电子账户数据存储

SAQ B-IP 仅包括适用于仅通过独立的、列于 PCI 的经认证 PIN 交易安全（PTS）交互点（POI） $ ^{1} $设备处理账户数据并 IP 连接到支付处理商的商户的 PCI DSS 要求。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。



例外情况适用于被归类为安全读卡器（SCR）和密码安全读卡器

（SCRP）的 PTS POI 设备；使用 SCR 或 SCRP 的商户不合资格填写本 SAQ。

SAQ B-IP 商户可以是实体店（实体信用卡）或邮购/电话订购（虚拟信用卡）商户，并且不在任何计算机系统上存储帐户数据。

## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ B-IP 商户将确认其符合该支付渠道的资格标准，具体如下：

商户仅使用独立的、列于 PCI 的经认证  $ ^{1} $PTS POI 设备（不包括 SCR 和 SCRP），通过 IP 连接到商户的支付处理商，以获取客户的支付卡信息；

- 根据列于 PCI SSC 网站上的 PTS POI 计划（不包括 SCR 和 SCRP）认证与 IP 连接的独立 POI 设备；

与 IP 连接的独立 PTS POI 设备不与商家环境中的任何其他系统连接（这可以通过网络分段实现，将 PTS POI 设备与其他系统隔离开来） $ ^{2} $;

- 帐户数据的唯一传输是由经批准的 PTS POI 设备传输到支付处理商；

PTS POI 设备不依赖任何其他设备—（例如电脑、手机、平板电脑等）来—连接到支付处理商；

商户不以电子格式存储帐户数据；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

---

## SAQ C-VT – 采用基于网络的第三方虚拟支付终端解决方案的商户，不存储电子账户数据

SAQ C-VT 仅包括适用于仅通过连接到互联网的隔离计算设备上的第三方虚拟支付终端解决方案处理帐户数据的商户的 PCI DSS 要求。

虚拟支付终端是第三方解决方案，用于将支付卡交易提交给符合 PCI DSS 的第三方服务提供商（TPSP）网站进行授权。使用这种解决方案，商户通过安全连接的网络浏览器，从一个隔离的计算设备上手动输入帐户数据。与物理终端不同，虚拟支付终端不会直接从支付卡中读取数据。

有关选择 SAQ 类型的图形指南，请参阅第 23 页和第 24 页的“哪种 SAQ 最适用于我的环境”。



该 SAQ 选项仅适用于通过键盘向基于互联网的虚拟支付终端解决方案手动输入一次交易的商户。SAQ C-VT 商户可以是实体店（实体信用卡）或邮购/电话订购（虚拟信用卡）商户，并且不在任何计算机系统上存储账户数据。

## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ C-VT 商户将确认其符合该支付渠道的资格标准，具体如下：

唯一的支付处理是通过一个虚拟的支付终端，由一个连接互联网的网络浏览器访问；

虚拟支付终端解决方案由符合 PCI DSS 要求的第三方服务提供商提供和托管；

符合 PCI DSS 要求的虚拟支付终端解决方案只能通过隔离在单一位置的计算设备进行访问，而不连接到其他地点或系统；

计算设备没有安装可促使帐户数据被存储的软件（例如，没有用于批量处理或存储转发的软件）；

计算设备没有任何可用于收集或存储帐户数据的附加硬件设备（例如，没有附加读卡器）；

商户不通过任何渠道（例如，通过内部网络或互联网）以电子方式进行帐户数据的接收、传输或存储；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

---

## SAQ C – 连接到互联网的支付应用系统的商户，不存储电子账户数据

SAQ C 仅包括适用于拥有连接到互联网的支付应用系统（例如，销售点系统）且不存储电子帐户数据的商户的 PCI DSS 要求。

SAQ C 商户通过销售点（POS）系统或其他连接到互联网的支付应用系统处理帐户数据，不将帐户数据存储在任何计算机系统上，可能是实体店（实体信用卡）或邮购/电话订购（虚拟信用卡）商户。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。



## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ C 商家将确认其符合此支付渠道的以下资格标准：

商户在同一设备和/或同一局域网（LAN）上拥有一个支付应用系统和一个互联网连接。

支付应用程序系统不连接到商户环境中的任何其他系统（这可以通过网络分段实现，将支付应用程序系统/互联网设备与所有其他系统隔离开来）；

POS 环境的物理位置不连接到其他场所或地点，任何局域网都只适用于单一商店；

商户不以电子格式存储帐户数据；以及

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收的。

---

## SAQ P2PE – 仅使用 PCI 所列 P2PE 解决方案支付终端的商户，不存储电子账户数据

SAQ P2PE 仅包括适用于仅通过列于  $ ^{3} $PCI 的经认证 P2PE 解决方案处理帐户数据的商户的 PCI DSS 要求。SAQ P2PE 商户无法访问任何计算机系统上的明文帐户数据，帐户数据只能通过列于 PCI 的经认证  $ ^{3} $P2PE 解决方案的支付终端输入。

SAQ P2PE 商户可以是实体店（实体信用卡）或邮购/电话订购（虚拟信用卡）商户。例如，如果邮购/电话订购商户通过纸质或电话接收帐户数据，并仅将其直接输入到 3 列于 PCI 的经认证 P2PE 解决方案的支付终端，便有资格填写 SAQ P2PE。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。



## 本 SAQ 不适用于电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ P2PE 商户将确认其符合该支付渠道的资格标准，具体如下：

所有支付处理均通过一个列于  $ ^{3} $ PCI 的经认证 P2PE 解决方案进行；

商户环境中唯一存储、处理或传输帐户数据的系统是来自列于 $ ^{3} $PCI的经认证P2PE解决方案的支付终端；

商户不以其他方式接收、传输或存储电子帐户数据；

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收；以及

商户已实施 P2PE 解决方案提供商提供的 P2PE 指导手册（PIM）中的所有控制。

---

## SAQ SPoC – 商户仅使用 PCI 列出的经批准的 PTS SCRP 设备 和 COTS 设备作为经验证的 PCI 所列 SPoC 解决方案的一部分。

SAQ SPoC 仅包括通过安全读卡器-PIN（SCRP）设备和商用现成移动设备（COTS）（例如：手机或平板电脑）处理账户数据的商家的 PCI DSS 要求，是验证 PCI SSC 基于 COTS（SPoC）软件 PIN 输入解决方案的一部分。

SAQ SPoC 商户无法访问任何计算机系统上的明文账户数据，仅能通过 SCRP 在验证的 PCI SSC SPoC 解决方案的框架内使用商户 COTS 移动设备进入账户数据。这些 COTS 移动设备是通用移动设备，即移动设备不必仅用于支付或专用于支付渠道。

SAQ SPoC 商户处理刷卡现场交易（包括接触芯片交易、非接触式交易和基于 SCRP 的磁条交易）。

使用未列入 PTS 磁条读取器（MSR）的商户例外；这些商户不符合 SAQ 的条件。此 SAQ 可用于包 MSR 功能 PTS 列出的 SCRP。

此 SAQ 不适用于无人值守刷卡——（例如，售货亭、自助结账）——、邮购/电话订购（MOTO）或电子商务渠道。

## 本 SAQ 不适用于服务提供者。

SAQ SPoC 商户将确认其符合该支付渠道的资格标准，具体如下：

所有支付处理仅通过卡支付渠道进行。

所有持卡人数据输入通过一个经 PCI SSC 批准和列入名单的验证 SpoC 解决方案中的 SCRP 进行；

- 商户 SPoC 环境中唯一存储、处理或传输账户数据的系统是经 PCI SSC 批准和列入验证 $ ^{4} $ SPoC 解决方案所使用的系统；

商户不以其他方式接收、传输或存储电子帐户数据；

此支付渠道未连接到商户环境中的任何其他系统/网络。

商户以纸质形式保留任何帐户数据（例如，打印的报告或收据），而这些文件不是以电子方式接收；以及

商户已实施 SPoC 解决方案提供商提供的 SPoC 用户指南中的全部控制措施。

---

## 适用于商户的 SAQ D – 所有其他符合 SAQ 资格的商户

SAQ D 适用于有资格完成自我评估问卷但不符合其他任何 SAQ 类型的商户。SAQ D 可能适用的商户环境的示例包括但不限于：

在其网站上接受账户数据的电子商务商户；

☑ 用电子方式存储账户数据的商户；

不以电子方式存储账户数据但不符合另一种 SAQ 标准的商户；

环境可能符合另一种 SAQ 类型的条件，但拥有适用于其环境的额外 PCI DSS 要求的商户。

## 服务提供商 SAQ D – 符合 SAQ 标准的服务提供商

服务提供商 SAQ D 适用于支付品牌定义为有资格完成自我评估问卷的所有服务提供商。

请注意，对于 PCI DSS 4.0 版，服务提供商的 SAQ D 现在要求在第 2a 部分中提供额外文件，并指定服务提供商需要为每个 PCI DSS 要求“描述结果”。

有关选择适合您环境的 SAQ 类型的图形指南，请参阅第 23 页和第 24 页上的“哪种 SAQ 最适合我的环境？”。

---

## 哪种 SAQ 最适用于我的环境？

<div style="text-align: center;"><img src="imgs/img_in_image_box_204_214_492_685.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_584_210_1378_760.jpg" alt="Image" width="50%" /></div>


✓ 拥有多个支付渠道的商家应就验证和报告要求咨询其合规接受实体（例如：支付品牌和收单机构）。

和

✓ 商家必须满足任何适用 SAQ 的全部资格标准。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_115_1436_1077.jpg" alt="Image" width="81%" /></div>


---

### 附录 A：PCI DSS 4.0 版的 SAQ 有何变化

以下是从 3.2.1 版到 4.0 版的所有 SAQs 所做的一般更改摘要。

PCI DSS 4.0 版中添加了“定义帐户数据、持卡人数据和敏感身份验证数据”表，用于定义 PCI DSS 中使用的各个术语。

在完成 SAQ 时，添加了一个“报告响应”表，用于描述实体为每个 PCI DSS 要求选择的每个报告响应的含义。

每个 SAQ 中的要求已更新，以反映对 PCI DSS v4.0 所做的更改，并与其他 PCI DSS 4.0 版文档更加一致。例如：

• 每个 PCI DSS 要求的措辞现在与 PCI DSS 4.0 版中的措辞相同，而不是以问题形式陈述。

• 一些复杂的需求被拆分成子项需求，其他需求得已澄清。

每个 PCI DSS 要求的报告响应已更新，与 PCI DSS 4.0 版合规性报告（ROC）模板中的语言保持一致-例如，“是”现变为“就位”。

合规性证明（AOC）部分已更新，以与 ROC AOC 的措辞和内容保持一致。

对于一些更复杂的需求，添加了解释 $ ^{5} $，用于帮助商户了解如何在给定的 SAQ 中评估该需求。

增加了新的附录，用于补充关于具体报告答复的额外信息。

除了上述变更外，服务提供商的 SAQ D 现要求在第 2a 部分中提供额外的文件，并指定服务提供商为每个 PCI DSS 要求“描述结果”。