---
title: "PCI-DSS-v4_0-ZH"
source: "支付卡行业数据安全标准（PCI-DSS）/PCI-DSS-v4_0-ZH.pdf"
type: "pdf"
processed: "2026-04-23T06:50:47.031054"
---

Payment Card Industry

数据安全标准

## 要求及测试程序

4.0 版

2022年3月

---

<div style="text-align: center;">文件变更</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>日期</td><td style='text-align: center; word-wrap: break-word;'>版本</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2008年10月</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>将PCI DSS 1.2版介绍为“PCI DSS要求和安全评估程序”，消除了文件之间的冗余，并对PCI DSS安全审核程序1.1版进行了一般和具体修改。如需完整信息，请参见PCI数据安全标准1.1版至1.2版的变更摘要。</td></tr><tr><td rowspan="4">2009年7月</td><td rowspan="4">1.2.1</td><td style='text-align: center; word-wrap: break-word;'>添加PCI DSS 1.1版和1.2版之间被错误删除的句子。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>将测试程序6.3.7.a和6.3.7.b中的“then（然后）”更正为“than（比）”。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>移除测试程序6.5.b中“in place（到位）”和“not in place（未到位）”列的灰色标记。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对于补偿性控制工作表-已完成的示例，将页面顶部的措辞更正为：“使用本工作表为任何通过补偿性控制指出为“到位”的要求确定补偿性控制。”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2010年10月</td><td style='text-align: center; word-wrap: break-word;'>2.0</td><td style='text-align: center; word-wrap: break-word;'>更新并实施1.2.1版的变更。请参阅PCI DSS-PCI DSS 1.2.1版至2.0版的变更摘要。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2013年11月</td><td style='text-align: center; word-wrap: break-word;'>3.0</td><td style='text-align: center; word-wrap: break-word;'>更新于2.0版。请参阅PCI DSS-PCI DSS 2.0版至3.0版的变更摘要。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2015年4月</td><td style='text-align: center; word-wrap: break-word;'>3.1</td><td style='text-align: center; word-wrap: break-word;'>更新于PCI DSS 3.0版。有关变更详情，请参阅PCI DSS-PCI DSS 3.0版至3.1版的变更摘要。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2016年4月</td><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>更新于PCI DSS 3.1版。有关变更详情，请参阅PCI DSS-PCI DSS 3.1版至3.2版的变更摘要。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2018年5月</td><td style='text-align: center; word-wrap: break-word;'>3.2.1</td><td style='text-align: center; word-wrap: break-word;'>更新于PCI DSS 3.2版。有关变更详情，请参阅PCI DSS-PCI DSS 3.2版至3.2.1版的变更摘要。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2022年3月</td><td style='text-align: center; word-wrap: break-word;'>4.0</td><td style='text-align: center; word-wrap: break-word;'>将文件名称改为“支付卡行业数据安全标准：要求及测试程序”。更新于PCI DSS v3.2.1。要了解变更详情，请参阅PCI DSS-PCI DSS 3.2.1版至4.0版的变更摘要。</td></tr></table>

确认通知：在所有使用目的和情况下，PCI SSC 网站上的英文文本应作为此文件的官方版本。当翻译文本和英文文本之间出现任何歧义和不一致之处时，正确的内容应以该位置的英文文本为准。

---

## 目录

1 导言和 PCI 数据安全标准概述 ..... 1  
2 PCI DSS 适用性信息 ..... 4  
3 PCI DSS 与 PCI SSC 软件标准之间的关系 ..... 8  
4 PCI DSS 要求的范围 ..... 10  
5 实施 PCI DSS 到正常业务过程的最佳做法 ..... 21  
6 评估商：PCI DSS 评估的抽样 ..... 24  
7 PCI DSS 要求中使用的时间框架说明 ..... 27  
8 实施和认证 PCI DSS 的方法 ..... 30  
9 保护有关实体安全状况的信息 ..... 33  
10 PCI DSS 要求的测试方法 ..... 35  
11 遵从性报告的说明和内容 ..... 36  
12 PCI DSS 评估流程 ..... 37  
13 其他参考资料 ..... 38  
14 PCI DSS 版本 ..... 39  
15 详细的 PCI DSS 要求和测试程序 ..... 40  
建立和维护安全网络和系统 ..... 42  
要求 1：安装和维护网络安全控制 ..... 42  
要求 2：安全配置应用于所有系统组件 ..... 64

---

保护帐户数据.....77  
  
要求3：保护所存储帐户数据.....77  
  
要求4：在开放的公共网络上传输过程中使用强效加密法保护持卡人数据.....108  
  
维护漏洞管理计划.....117  
  
要求5：保护所有系统和网络免受恶意软件侵害.....117  
  
要求6：开发和维护安全系统和软件.....130  
  
实施强有力的访问控制措施.....154  
  
要求7：根据“必须知道”原则限制系统组件和持卡人数据的访问权限.....154  
  
要求8：识别用户并验证系统组件的访问权限.....166  
  
要求9：限制持卡人数据的实体访问权限.....195  
  
定期监控和测试网络.....217  
  
要求10：记录并监控系统组件和持卡人数据的所有访问权限.....217  
  
要求11：定期测试系统和网络的安全性.....236  
  
维护信息安全政策.....260  
  
要求12：使用组织政策和计划支持信息安全.....260  
  
附录A 额外PCI DSS要求.....297  
  
附录A1：针对多租户服务提供商的额外PCI DSS要求.....297  
  
附录A2：针对使用SSL/早期TLS进行实体信用卡POSPOI终端连接的实体的额外PCI DSS要求.....303  
  
附录A3：指定的实体补充认证(DESV).....307  
  
附录B 补偿性控制.....329  
  
附录C 补偿性控制工作表.....331  
  
附录D 定制方法.....332  
  
附录E 支持定制方法的样本模板.....334

---

附录 F 利用 PCI 软件安全框架以支持要求 6.....341  
附录 G PCI DSS 术语、缩略语和缩写词汇表.....344

---

## 1 导言和 PCI 数据安全标准概述

制定支付卡行业数据安全标准（PCI DSS）是为了鼓励和加强支付卡账户数据的安全性，并促进全球广泛采用一致的数据安全措施。PCI DSS提供了一个旨在保护账户数据的技术和操作要求的基线。虽然PCI DSS专门为关注支付卡账户数据的环境而设计，但也可以用来保护支付生态系统中的其他元素免受威胁和安全。

表 1 显示了 12 项主要的 PCI DSS 要求。

<div style="text-align: center;">表 1。主要 PCI DSS 要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">PCI 数据安全标准 - 高级别概述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建立和维护安全网络和系统</td><td style='text-align: center; word-wrap: break-word;'>1. 安装和维护网络安全控制。2. 安全配置应用于所有系统组件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保护帐户数据</td><td style='text-align: center; word-wrap: break-word;'>3. 保护所存储帐户数据。4. 在开放的公共网络上传输过程中使用强效加密法保护持卡人数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>维护漏洞管理计划</td><td style='text-align: center; word-wrap: break-word;'>5. 保护所有系统和网络免受恶意软件侵害。6. 开发和维护安全系统和软件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>实施强有力的访问控制措施</td><td style='text-align: center; word-wrap: break-word;'>7. 根据“必须知道”原则限制系统组件和持卡人数据的访问权限。8. 识别用户并验证系统组件的访问权限。9. 限制持卡人数据的实体访问权限。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期监控和测试网络</td><td style='text-align: center; word-wrap: break-word;'>10. 记录并监控系统组件和持卡人数据的所有访问权限。11. 定期测试系统和网络的安全性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>维护信息安全政策</td><td style='text-align: center; word-wrap: break-word;'>12. 使用组织政策和计划支持信息安全。</td></tr></table>

支付卡行业数据安全标准：要求及测试程序，4.0版

---

本文件《支付卡行业数据安全标准要求和测试程序》由 12 项 PCI DSS 主要要求、详细的安全要求、相应的测试程序以及与每个要求相关的其他信息组成。以下章节提供了详细的指导方针和最佳实践，以帮助各实体准备、实施和报告 PCI DSS 评估的结果。PCI DSS 要求和测试程序始于第 40 页。

PCI DSS 包括一套保护帐户数据的最低要求，并可能通过额外的控制和实践来加强，以进一步降低风险，并纳入当地、区域和部门的法律和法规。此外，立法或监管要求可能要求对个人信息或其他数据元素（例如，持卡人姓名）进行特别保护。

## 限制条件

如果本标准中的任何要求与国家、州或地方法律相冲突，则适用国家、州或地方法律。PCI DSS 资源

PCI 安全标准委员会（PCI SSC）网站（www.pcisecuritystandards.org）提供了以下额外资源，以协助组织进行 PCI DSS 评估和认证；

文件库，包括：

– PCI DSS 变更摘要

– PCI DSS 快速参考指南

- 信息补充和指南

– PCI DSS 的优先处理方法

- 遵从性报告（ROC）报告模板和报告说明

一 自我评估调查问卷（SAQ）和 SAQ 说明和指南

- 遵从性测试 (AOC)

常见问题解答 (FAQ)

■ 小商户网站的 PCI

PCI 培训课程和信息网络研讨会

---

合格安全性评估商（QSA）和授权扫描服务商名单（ASV）

PCI 批准的设备、应用程序和解决方案的清单

PCI SSC 网站上有 60 多份指导文件和信息补充，为 PCI DSS 提供具体的指导和注意事项。示例包括：

PCI DSS 范围界定和网络分段指南

PCI SSC 云计算指南

■ 多因素验证指南

第三方安全保证

有效的日常日志监控

穿透测试指南

注：信息补充是对 PCI DSS 的补充，并确定了满足 PCI DSS 要求的额外注意事项和建议。信息补充不会取代、替代或扩展 PCI DSS 或其任何要求。

实施安全意识计划的最佳做法

维护 PCI DSS 遵从性的最佳做法

■ 大型机构的 PCI DSS

- 使用 SSL/早期 TLS 和对 ASV 扫描的影响

- 使用 SSL/早期 TLS 进行 POS POI 终端连接

☑ 令牌化产品安全指南

保护基于电话的支付卡数据

如需这些信息和其他资源，请参考文件库：www.pcisecuritystandards.org。

此外，请参阅附录 G 了解 PCI DSS 术语的定义。

---

## 2 PCI DSS 适用性信息

PCI DSS 适用于所有存储、处理或传输持卡人数据（CHD）和/或敏感验证数据（SAD）或可能影响持卡人数据环境（CDE）安全性的实体。这包括所有参与支付卡账户处理的实体—包括商户、处理商、收单机构、发卡机构和其他服务提供商。

是否要求任何实体遵守或认证其是否遵从 PCI DSS 的要求，由管理遵从性计划的组织（例如支付品牌和收单机构）自行决定。要了解任何额外标准，请联系相关组织。

## 确定帐户数据、持卡人数据和敏感验证数据

持卡人数据和敏感验证数据被视为帐户数据，确定方式如下：

<div style="text-align: center;">表 2。帐户数据</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">账户数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>持卡人数据包括：</td><td style='text-align: center; word-wrap: break-word;'>敏感验证数据包括：</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• 主账户号（PAN）• 持卡人姓名• 到期日• 业务码</td><td style='text-align: center; word-wrap: break-word;'>• 全磁道数据（磁条数据或芯片上的同等数据）• 卡验证代码• PIN/PIN 数据块</td></tr></table>

---

PCI DSS 要求适用于具有存储、处理或传输帐户数据（持卡人数据和/或敏感验证数据）环境的实体，以及具有可能影响 CDE 安全的环境的实体。一些 PCI DSS 要求也可能适用于拥有不存储、处理或传输帐户数据的环境的实体—例如，将其 CDE 1 的支付操作或管理外包的实体。将其支付环境或支付操作外包给第三方的实体仍有责任确保第三方根据适用的 PCI DSS 要求保护账户数据。

主帐户号（PAN）是持卡人数据的决定因素。因此，帐户数据这一术语涵盖了以下内容：完整的 PAN、与 PAN 一起出现的任何其他持卡人数据元素，以及任何敏感验证数据元素。

如果持卡人姓名、业务码和/或到期日与 PAN 一起存储、处理或传输，或以其他方式出现在 CDE 中，则必须根据适用于持卡人数据的 PCI DSS 要求进行保护。

如果实体存储、处理或传输 PAN，则存在适用 PCI DSS 要求的 CDE。有些要求可能不适用，例如，如果该实体不存储 PAN，那么要求 3 中有关保护存储的 PAN 的要求将不适用于该实体。

即使实体不存储、处理或传输 PAN，一些 PCI DSS 要求仍可适用。请考虑以下情况：

如果该实体存储 SAD，要求 3 中专门与 SAD 存储有关的要求将适用。

如果该实体聘请第三方服务提供商代表其存储、处理或传输 PAN，则要求 12 中与服务提供商管理有关的要求将适用。

如果该实体可以影响 CDE 的安全，因为实体的基础设施的安全可以影响持卡人数据的处理方式（例如，通过控制生成支付表格或页面的网络服务器），则一些要求将适用。

如果持卡人数据只存在于物理介质（如纸张）上，则要求9中与物理介质的安全和处理有关的要求将适用。

与事件响应计划有关的要求适用于所有实体，以确保在怀疑或实际违反持卡人数据保密性的情况下有程序可循。

---

## 在 PCI DSS 中使用帐户数据、敏感验证数据、持卡人数据和主帐户号

PCI DSS 包括特别提到帐户数据、持卡人数据和敏感验证数据的要求。需要注意的是，这些类型的数据各不相同，这些术语不可互换使用。要求中对帐户数据、持卡人数据或敏感验证数据的具体引用是有明确目的的，并且要求特别适用于所引用的数据类型。

---

## 帐户数据的元素和存储要求

表 3 列出了持卡人和敏感验证数据的元素，每个数据元素的存储是否被允许或禁止，以及每个数据元素在存储时是否必须不可读—例如，使用强效加密法。本表并非详尽无遗，并且仅用于说明所述要求如何适用于不同的数据元素。

<div style="text-align: center;">表 3。帐户数据元素存储要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2"></td><td style='text-align: center; word-wrap: break-word;'>数据元素</td><td style='text-align: center; word-wrap: break-word;'>存储限制</td><td style='text-align: center; word-wrap: break-word;'>要求使存储的数据不可读</td></tr><tr><td rowspan="7">账户数据</td><td rowspan="4">持卡人数据</td><td style='text-align: center; word-wrap: break-word;'>主帐户号（PAN）</td><td style='text-align: center; word-wrap: break-word;'>根据要求 3.2 的规定，存储量保持在最低水平</td><td style='text-align: center; word-wrap: break-word;'>是的，根据要求 3.5 的规定</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>持卡人姓名</td><td rowspan="3">根据要求 3.2 的规定，存储量保持在最低水平 $ ^{2} $</td><td rowspan="3">没有</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>到期日</td></tr><tr><td rowspan="3">敏感验证数据</td><td style='text-align: center; word-wrap: break-word;'>全磁道数据</td><td rowspan="3">根据要求 3.3.1 $ ^{3} $ 的规定，授权后无法存储。</td><td rowspan="3">对，在授权完成之前存储数据必须使用要求 3.3.2 中规定的强效加密法进行保护。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>卡验证代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PIN/PIN 数据块</td></tr></table>

如果 PAN 与持卡人数据的其他元素一起存储，根据 PCI DSS 要求 3.5.1，则必须只有使 PAN 不可读。

授权后不得存储敏感验证数据（即使是加密的验证数据）。这甚至适用于不存在 PAN 的环境。

---

## 3 PCI DSS 与 PCI SSC 软件标准之间的关系

PCI SSC 通过支付应用程序数据安全标准（PA-DSS）和软件安全框架（SSF）支持在持卡人数据环境（CDE）中使用安全支付软件，该框架由安全软件标准和安全软件生命周期（安全 SLC）标准组成。经过 PCI SSC 认证并列出的软件可以提供保证，该软件采用安全做法开发，并满足了一系列规定的软件安全要求。

PCI SSC 安全软件计划包括已被认证为符合适用的 PCI SSC 软件标准的支付软件和软件供应商的列表。

认证软件：PCI SSC 网站上列出的支付软件是经过认证的支付应用程序（PA-DSS）或经过认证的支付软件（安全软件标准），已经由合格的评估商进行评估，以确认该软件符合该标准中的安全要求。这些标准中的安全要求着重于保护支付交易和账户数据的完整性和保密性。

认证软件供应商：安全 SLC 标准确定了软件供应商的安全要求，以在整个软件生命周期中整合安全软件开发实践。经过认证符合安全 SLC 标准的软件供应商在 PCI SSC 网站上被列为安全 SLC 合格的供应商。

注：PA-DSS 和相关计划将于 2022 年 10 月退役。关于 PA-DSS 认证应用程序的到期日，请参考 PCI SSC 认证支付应用程序列表。在到期日之后，应用程序被列为“仅可接受用于预设部署”。关于实体是否可以继续使用已过期列表的 PA-DSS 应用程序，由管理遵从性计划的组织（例如支付品牌和收单机构）自行决定；实体应联系相关组织以了解更多细节。



有关 SSF 或 PA-DSS 的更多信息，请参考各自的计划指南：www.pcisecuritystandards.org。

所有存储、处理或传输帐户数据的软件，或者可能影响帐户数据或 CDE 安全的软件，都在实体的 PCI DSS 评估范围内。虽然使用经过认证的支付软件支持实体 CDE 的安全，但使用这种软件本身并不能使实体符合 PCI DSS。该实体的 PCI DSS 评估应包括验证该软件是否正确配置并安全实施，以支持适用的 PCI DSS 要求。此外，如果已定制被列入 PCI 名单的支付软件，则在 PCI DSS 评估期间将需要进行更为深入的审核，因为该软件可能不再是最初认证的版本的代表。

由于安全威胁不断演变，不再受供应商支持的软件（例如，被供应商认定为“寿命结束”）可能无法提供与支持版本相同的安全水平。我们强烈建议各实体保持其软件的时效性，并更新到现有的最新软件版本。

我们鼓励自行开发软件的实体参考 PCI SSC 的软件安全标准，并将其中的要求作为最佳实践，用于其开发环境中。在符合 PCI DSS 的环境中实施的安全支付软件将有助于最大限度地减少导致帐户数据受到威胁和欺诈的安全漏洞的可能性。请参阅订制和定制软件。

---

## PCI DSS 对支付软件供应商的适用性

如果支付软件供应商也是存储、处理或传输帐户数据的服务提供商，或者可以访问客户的帐户数据—例如，以支付服务提供商的身份或通过远程访问客户环境，则 PCI DSS 可能适用于该供应商。PCI DSS 可能适用的软件供应商包括那些提供支付服务的供应商，以及在云中提供支付终端、软件即服务（SaaS）、云中电子商务和其他云支付服务的云服务提供商。

## 订制和定制软件

所有存储、处理或传输帐户数据的订制和定制软件，或者可能影响帐户数据或 CDE 安全的软件，都在实体的 PCI DSS 评估范围内。

根据 PCI SSC 的软件安全框架标准（安全软件标准或安全 SLC 标准）之一开发和维护的订制和定制软件将支持实体满足 PCI DSS 要求 6。

有关详情，请参见附录 F。

注：PCI DSS 要求 6 完全适用于未按照 PCI SSC 的软件安全框架标准之一进行开发和维护的订制和定制软件。使用软件供应商开发可能影响帐户数据或其 CDE 安全性的订制和定制软件的实体，有责任确保这些软件供应商根据 PCI DSS 要求 6 开发软件。

---

## 4 PCI DSS 要求的范围

持卡人数据环境（CDE）由以下部分组成：

存储、处理和传输持卡人数据和/或敏感验证数据的系统组件、人员和流程，和

一 可能不存储、处理或传输 CHD/SAD 的系统组件，但它们可以不受限制地连接到那些存储、处理或传输 CHD/SAD 的系统组件。和

■ 可能影响 CDE 安全的系统组件、人员和流程。 $ ^{4} $

“系统组件”包括网络设备、服务器、计算设备、虚拟组件、云组件和软件。系统组件的包括但不限于：

存储、处理或传输帐户数据的系统（例如，支付终端、授权系统、清算系统、支付中间件系统、支付后台系统、购物车和店面系统、支付网关/开关系统、欺诈监控系统）。

- 提供安全服务的系统（例如，验证服务器、访问控制服务器、安全信息和事件管理（SIEM）系统、物理安全系统（例如，标记访问或CCTV）、多因素验证系统、反恶意软件系统）。

促进分段的系统（例如，内部网络安全控制）。

■ 可能影响帐户数据或 CDE 安全的系统（例如，名称解析，或电子商务（网络）重定向服务器）。

虚拟化组件，例如虚拟机、虚拟交换机/路由器、虚拟设备、虚拟应用程序/桌面和虚拟机监视器。

云基础设施和组件，包括外部和内部，并包括容器或图像的实例、虚拟私有云、基于云的身份和访问管理、驻留在内部或云中的CDE、带有容器化应用程序的服务网格以及容器协调工具。

---

网络组件，包括但不限于网络安全控制、交换机、路由器、VoIP网络设备、无线接入点、网络设备和其他安全设备。

- 服务器类型，包括但不限于 Web、应用程序、数据库、验证、邮件、代理、网络时间协议（NTP）和域名系统（DNS）。

终端用户设备，例如计算机、笔记本、工作站、管理工作站、平板电脑和移动设备。

打印机，以及扫描、打印和传真的多功能设备。

任何格式的存储帐户数据（例如，纸质、数据文件、音频文件、图像和视频记录）。

应用程序、软件和软件组件、无服务器应用程序，包括所有购买的、订阅的（例如，软件即服务）、订制和定制软件，包括内部和外部（例如，互联网）应用程序。

实施软件配置管理的工具、代码库和系统，或用于将对象部署到 CDE 或可能影响 CDE 的系统。

---

图 1 显示了为 PCI DSS 界定系统组件范围的注意事项。

<div style="text-align: center;">图 1。了解 PCI DSS 的范围界定</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_444_255_1173_1047.jpg" alt="Image" width="46%" /></div>


---

## 年度 PCI DSS 范围确认

准备进行 PCI DSS 评估的第一步是实体准确地确定审核的范围。被评估实体必须根据 PCI DSS 要求 12.5.2 确认其 PCI DSS 范围的准确性，确定帐户数据的所有位置和流向，并确定所有连接到 CDE 的系统，或者如果被威胁，可能影响 CDE 的系统（例如，验证服务器、远程访问服务器、日志服务器），以确保它们被纳入 PCI DSS 范围内。在范围界定过程中应考虑所有类型的系统和地点，包括备份/恢复站点和故障转移系统。

PCI DSS 要求 12.5.2 中规定了实体确认其 PCI DSS 范围准确性的最少步骤。该实体应保留文件，以显示 PCI DSS 范围的确定方式。保留该文件供评估商审核，并在实体的下一次 PCI DSS 范围确认活动中用作参考。对于每一次 PCI DSS 评估，评估商都要认证该实体是否准确确定并记录了评估的范围。

注：PCI DSS 要求 12.5.2 规定了该年度 PCI DSS 范围确认，是实体应该执行的活动。该活动不同于实体的评估商在评估期间执行的范围界定确认，也不打算被其取代。

## 分段

将 CDE 与实体网络的其余部分分段（或隔离），并不是 PCI DSS 的要求。但是，我们强烈建议采用这种方法，因为它可以减少：

PCI DSS 评估的范围

PCI DSS 评估的成本

实施和维护 PCI DSS 控制的成本和难度

组织相对于支付卡帐户数据的风险（通过将该数据合并到更少、更多的控制地点来减少）

如果分段不充分（有时称为“扁平网络”），整个网络都在 PCI DSS 评估的范围内。可以通过一些物理或逻辑方法来实现分段，例如正确配置的内部网络安全控制、具有强大访问控制列表的路由器，或其他限制网络特定分段的访问权限的技术。要被视为非 PCI DSS 范围，系统组件必须与 CDE 适当分段（隔离），这样，即使该组件被威胁，非范围系统组件也不会影响 CDE 的安全。

---

缩小 CDE 范围的一个重要前提是清楚了解与帐户数据的存储、处理和传输有关的业务需求和流程。通过消除不必要的数据和合并必要的数据，将帐户数据限制在尽可能少的位置，可能需要对长期存在的业务实践进行重新设计。

通过数据流程图记录帐户数据流有助于实体充分了解帐户数据如何进入组织，它在组织内的位置，以及它如何在组织内各个系统中穿行。数据流程图还显示了存储、处理和传输帐户数据的所有位置。这些信息支持实施分段的实体，也可以支持确认分段用于将 CDE 与非范围网络隔离开来。

如果分段用于减少 PCI DSS 评估的范围，评估商必须核实分段是否足以减少评估的范围，如图 2 所示。在高层次上，适当分段将存储、处理或传输帐户数据的系统与不存储、处理或传输帐户数据的系统隔离开来。然而，一个特定分段实施的充分性是高度可变的，并取决于几个因素，例如一个特定的网络配置、部署的技术和其他可能实施的控制。

---

<div style="text-align: center;">图 2。分段和对 PCI DSS 范围的影响</div>


要使用分段来缩小 PCI DSS 范围，所有范围内系统组件必须与范围外系统分隔开来，这样范围外系统就不能影响任何范围内系统组件的安全。

<div style="text-align: center;"><img src="imgs/img_in_image_box_280_221_1324_814.jpg" alt="Image" width="65%" /></div>


## 无线技术

如果无线技术用于存储、处理或传输帐户数据（例如，无线销售点设备），或者如果无线局域网（WLAN）是 CDE 的一部分或连接到 CDE，则适用并必须执行 PCI DSS 关于保护无线环境的要求和测试程序。

即使在 CDE 中不使用无线技术，并且实体有禁止在其环境中使用无线技术的政策，也必须根据 PCI DSS 要求 11.2.1 执行非法无线检测。这是因为无线接入点可以轻松地连接到网络上，很难检测到它的存在，以及未经授权的无线设备带来的风险增大。

---

在实施无线技术之前，实体应该仔细评估对该技术的需求和风险。考虑只将无线技术部署在非敏感数据的传输上。

## 加密持卡人数据和对 PCI DSS 范围的影响

根据 PCI DSS 要求 3.5，使用强效加密法对持卡人数据进行加密是一种可接受的使数据不可读的方法。然而，仅靠加密通常不足以使持卡人数据不在 PCI DSS 的范围内，也不能消除该环境中对 PCI DSS 的需求。由于持卡人数据的存在，该实体的环境仍在 PCI DSS 的范围内。例如，在商户实体支付卡交易环境中，可以实际接触到支付卡以完成交易，还可能有包含持卡人数据的纸质报告或收据。同样，在商户虚拟支付卡交易环境中，例如邮购/电话订购和电子商务，支付卡的详细信息通过渠道提供，需要根据 PCI DSS 进行评估和保护。

以下各项均在 PCI DSS 的范围内：

执行持卡人数据加密和/或解密的系统，以及执行密钥管理功能的系统。

未与加密和解密以及密钥管理流程隔离开来的加密持卡人数据。

- 加密持卡人数据存在于同时包含解密密钥的系统或媒体上，

与解密密钥存在于同一环境中的加密持卡人数据，

加密持卡人数据可以被一个同时拥有解密钥匙的实体所访问。

注：列入 PCI 的 P2PE 解决方案可以显著减少适用于商户的持卡人数据环境的 PCI DSS 要求的数量。但是，它并不能完全消除 PCI DSS 在商户环境中的适用性。

## 加密持卡人数据和对第三方服务提供商的 PCI DSS 范围的影响

如果第三方服务提供商（TPSP）只接收和/或存储由另一实体加密的数据，并且他们无法解密数据，那么如果满足某些条件，TPSP可能会认为加密数据不在范围之内。这是因为数据的责任通常由有能力解密数据或影响加密数据安全的一个或多个实体承担。确定哪一方对特定的PCI DSS控制负责，将取决于几个因素，包括谁可以访问解密密钥，每一方履行的角色，以及各方之间的协议。应该明确规定和记录责任，以确保TPSP和提供加密数据的实体都了解哪个实体负责哪些安全控制。

---

举个例子，一个提供存储服务的 TPSP 接收并存储客户提供的加密持卡人数据用于备份目的。该 TPSP 没有加密或解密密钥的访问权限，也不为其客户进行任何密钥管理。TPSP 在确定其 PCI DSS 范围时可以排除任何此类加密数据。然而，作为其与客户签订的服务协议的一部分，TPSP 确实有责任控制加密数据存储的访问权限。

确保根据适用的 PCI DSS 要求保护加密数据和加密密钥的责任通常由实体之间共享。在上述例子中，客户决定其哪些人员被授权访问存储介质，而存储设施则负责管理物理和/或逻辑访问控制，以确保只有客户授权的人员才能获得存储介质的访问权限。适用于 TPSP 的具体 PCI DSS 要求将取决于所提供的服务和双方之间的协议。在提供存储服务的 TPSP 的示例中，TPSP 提供的物理和逻辑访问控制将需要至少每年审核一次。这种审核可以作为商户的 PCI DSS 评估的一部分来执行，或者，审核可以由 TPSP 执行，控制也可以由 TPSP 认证，并向商户提供适当证据。有关“适当证据”的信息，请参阅 TPSP 的选择：认证符合客户 PCI DSS 要求的 TPSP 服务是否遵从 PCI DSS。

再举一个例子，TPSP 只接收加密持卡人数据，用于路由到其他实体，并且没有数据或密钥的访问权限，可能对该加密数据不承担任何 PCI DSS 责任。在这种情况下，TPSP 不提供任何安全服务或访问控制，他们可能被视为与公共或不信任网络相同，因此，通过 TPSP 的网络发送/接收账户数据的实体有责任确保应用 PCI DSS 控制来保护传输的数据。

## 使用第三方服务供应商

实体（在本节中称为“客户”）可能会选择使用第三方服务提供商（TPSP）来存储、处理或传输帐户数据，或代表客户管理范围内系统组件。使用 TPSP 可能会对客户的 CDE 安全生产影响。

注：使用符合 PCI DSS 的 TPSP 并不能使客户符合 PCI DSS，也不能免除客户对其自身 PCI DSS 遵从性的责任。即使客户使用 TPSP 来满足所有帐户数据功能，该客户仍然有责任按照管理遵从性计划的组织（例如，支付品牌和收单机构）的要求确认其自身的遵从情况。客户应联系相关组织了解任何要求。

### 使用 TPSP 和对客户满足 PCI DSS 要求 12.8 的影响

在许多不同的情况下，客户可能使用一个或多个 TPSP 来实现客户 CDE 内或相关的功能。在使用 TPSP 的所有情况下，客户必须根据要求 12.8 管理和监督其所有 TPSP 的 PCI DSS 遵从性状态，包括 TPSP：

---

可以访问客户的 CDE。

代表客户管理范围内系统组件，和/或

■ 能影响客户 CDE 的安全。

根据要求 12.8 管理 TPSP，包括进行尽职调查，制定适当协议，确定哪些要求适用于客户，哪些要求适用于 TPSP，并至少每年监测 TPSP 的遵从性状态。

要求 12.8 没有规定客户的 TPSP 必须符合 PCI DSS，只是要求客户按照要求中的规定监控其遵从性状态。因此，TPSP 无需符合 PCI DSS 即可使其客户满足要求 12.8。

## TPSP 用于满足客户 PCI DSS 要求的服务的影响

当 TPSP 代表客户提供符合 PCI DSS 要求的服务，或者该服务可能影响客户 CDE 的安全性时，那么这些要求就在客户的评估范围内，该服务的遵从性将影响客户的 PCI DSS 遵从性。TPSP 必须证明其符合适用的 PCI DSS 要求，才能为其客户实施这些要求。例如，如果一个实体聘请 TPSP 来管理其网络安全控制，而 TPSP 没有提供证据证明它符合 PCI DSS 要求 1 中的适用要求，那么这些要求对客户的评估是未到位的。再举一个例子，代表客户存储持卡人数据备份的 TPSP 需要满足与访问控制、物理安全等相关的适用要求，以便其客户在评估时考虑这些要求。

## 了解 TPSP 客户和 TPSP 之间责任的重要性

客户和 TPSP 应该清楚地识别和理解以下内容：

包括在 TPSP 的 PCI DSS 评估范围内的服务和系统组件。

TPSP 的 PCI DSS 评估所涵盖的特定 PCI DSS 要求和子要求。

任何由 TPSP 的客户负责、纳入其自身 PCI DSS 评估中的要求，以及

任何由 TPSP 和其客户共同负责的 PCI DSS 要求。

---

例如，云提供商应明确界定其哪些 IP 地址作为其季度漏洞扫描过程的一部分进行扫描，哪些 IP 地址是其客户的责任。

根据要求 12.9.2，TPSP 需要支持其客户关于 TPSP 提供给客户的服务相关的 PCI DSS 遵从性状况的信息请求，以及哪些 PCI DSS 要求是 TPSP 的责任，哪些是客户的责任，以及哪些是客户和 TPSP 之间的责任。有关责任矩阵模板，请参考了解 PCI DSS 4.0 版的提示和工具。该模板可用于记录和澄清 TPSP 和客户之间如何分担责任。

## TPSP 的选择：认证符合客户 PCI DSS 要求的 TPSP 服务是否遵从 PCI DSS。

TPSP 负责按照管理遵从性计划的组织（例如，支付品牌和收单机构）的要求，展示其 PCI DSS 遵从性。TPSP 应联系相关组织了解任何要求。

当 TPSP 提供的服务旨在满足或促进满足客户的 PCI DSS 要求，或可能影响客户 CDE 的安全性时，这些要求都在客户的 PCI DSS 评估范围内。在这种情况下，TPSP 有两种选择来认证遵从性：

年度评估：TPSP 接受年度 PCI DSS 评估，并向其客户提供证据，表明 TPSP 符合适用的 PCI DSS 要求；或

多项按需评估：如果 TPSP 不进行年度 PCI DSS 评估，它必须在其客户的要求下进行评估，并且/或者参与其客户的每项 PCI DSS 评估，并将每次审核的结果提供给各自的客户。

如果 TPSP 接受了其自身的 PCI DSS 评估，它应该向其客户提供足够的证据，以核实 TPSP 的 PCI DSS 评估的范围涵盖了适用于客户的服务，并且相关的 PCI DSS 要求已被审查并确定到位。如果供应商持有 PCI DSS 遵从性证明（AOC），TPSP 必须应要求向客户提供 AOC。客户还可以要求 TPSP 的 PCI DSS 遵从性报告（ROC）的相关部分。可以编辑 ROC 来保护任何机密信息。

如果 TPSP 没有接受其自身的 PCI DSS 评估，因此没有 AOC，TPSP 应该提供与适用的 PCI DSS 要求有关的明确证据，以便客户（或其评估商）能够确认 TPSP 是否符合这些 PCI DSS 要求。

---

## TPSP 列入支付品牌的 PCI DSS 合规服务供应商名单

对于根据要求 12.8 监控 TPSP 遵从性状态的客户来说，TPSP 列入支付品牌的 PCI DSS 合规服务提供商名单上可能是 TPSP 遵从性状态的充分证据 - 如果从名单上可以清楚地看到，TPSP 的 PCI DSS 评估覆盖了适用于客户的服务。如果从清单上无法清楚地看到，客户应该获得其他书面确认，以解决 TPSP 的 PCI DSS 遵从性状态。

对于寻找 PCI DSS 遵从性证据的客户来说，如果 TPSP 代表客户满足要求，或者所提供的服务会影响客户 CDE 的安全，则 TPSP 列入支付品牌的 PCI DSS 合规服务提供商名单上，并不能充分证明该 TPSP 的适用 PCI DSS 要求被纳入评估。如果 TPSP 具有 PCI DSS AOC，则应根据要求将其提供给客户。

---

## 5 实施 PCI DSS 到正常业务过程的最佳做法

作为其整体安全战略的一部分，实施业务正常流程（又称 BAU）的实体正在采取措施，确保为保护数据和环境而实施的安全控制措施继续正确实施，并在正常业务过程中正常运作。

一些 PCI DSS 要求旨在作为 BAU 流程，通过监控安全控制来确保其持续有效。该实体的这种监督有助于提供合理保证，即在 PCI DSS 评估之间保持其环境的遵从性。虽然目前标准中确定了一些 BAU 要求，但在可能的情况下，实体应该采用针对其组织和环境的额外 BAU 流程。BAU 流程是核实自动和手动控制是否按预期执行的一种方式。无论 PCI DSS 要求是自动还是手动，BAU 流程必须检测到异常情况，并发出警报和报告，以便负责的个人及时处理这种情况。

如何将 PCI DSS 纳入 BAU 活动的示例包括但不限于：

- 将 PCI DSS 遵从性的总体责任和义务分配给个人或团队。这可以包括由行政管理部门为特定的 PCI DSS 遵从性计划制定的章程，并与行政管理部门沟通。

制定性能指标，以衡量安全举措的有效性，并持续监控安全控制，包括那些大量依赖的安全控制，例如网络安全控制、入侵检测系统/入侵防御系统（IDS/IPS）、变更检测机制、反恶意软件解决方案和访问控制，以确保它们有效地按照预期运行。

更频繁地审核记录数据，以了解趋势或行为，而这些趋势或行为仅靠监控可能不那么明显。

确保检测并及时响应安全控制中的所有故障。响应安全控制失效的流程应包括：

- 恢复安全控制。

识别失效的原因。

识别并解决安全控制失效期间出现的任何安全问题。

一 实施缓解措施，例如流程或技术控制，以防止失效原因再次发生。

恢复安全控制监控，也许在一段时间内加强监控，以核实控制是否有效运行。

在完成变更之前，审核可能给环境带来安全风险的变更（例如，添加新系统、更换系统或网络配置），并包括以下内容：

---

- 执行风险评估，以确定变更对 PCI DSS 范围的潜在影响（例如，允许 CDE 中的一个系统与另一个系统之间的连接的新网络安全控制规则，可能将其他系统或网络纳入 PCI DSS 的范围内）。

确定适用于受变更影响的系统和网络的 PCI DSS 要求（例如，如果新系统在 PCI DSS 的范围内，则需要根据系统配置标准进行配置，包括变更检测机制、反恶意软件、补丁和检查记录。需要将这些新的系统和网络添加到范围内系统组件清单和季度漏洞扫描时间表中）。

更新 PCI DSS 范围，并视情况实施安全控制。

- 更新文件以反映已实施变更。

审核组织结构变更对 PCI DSS 范围和要求的影响（例如，公司合并或收购）。

定期审核外部连接和第三方访问。

对于使用第三方进行软件开发的实体，定期确认这些软件开发活动继续遵守要求6中的软件开发要求。

执行定期审核，以确认 PCI DSS 要求继续到位，并且人员遵循既定流程。定期审核应涵盖所有设施和地点，包括零售网点和数据中心，无论是自我管理还是使用 TPSP 例如，定期审核可用于确认配置标准已应用于适用的系统，默认供应商帐户和密码已被删除或禁用，补丁和反恶意软件解决方案保持时效性，检查日志正被审查，等等。如果 PCI DSS 中未另行规定，定期审核的频率应由实体根据其环境的规模和复杂性确定。

这些审核也可用于核实是否备存了 PCI DSS 评估所需的证据。例如，检查日志、漏洞扫描报告以及网络安全控制规则集的审核等证据，对于协助实体准备下一次 PCI DSS 评估是必要的。

与所有受影响的各方（包括外部和内部）建立沟通，讨论新发现的威胁和组织结构变更。沟通材料应帮助接收者了解威胁的影响、缓解措施以及进一步信息或升级的联络点。

至少每 12 个月审核一次硬件和软件技术，以确认它们继续得到供应商的支持，并能满足实体的安全要求，包括 PCI DSS。如果供应商不再支持技术，或技术不能满足实体的安全需求，则实体应准备一个补救计划，包括在必要时替换技术。

---

注：本节中的一些最佳实践也被列为某些实体的 PCI DSS 要求。例如，那些正在进行全面 PCI DSS 评估的实体、按照额外的“仅服务提供者”要求进行认证的服务提供者，以及需要按照附录 A3 进行认证的指定实体：指定的实体补充认证。

每个实体都应考虑在其环境中实施这些最佳实践，即使该实体不需要对它们（例如，正在进行自我评估的商户）进行认证。

有关更多指导，请参考 PCI SSC 网站文件库中的维护 PCI DSS 遵从性的最佳做法。

---

## 6 评估商：PCI DSS 评估的抽样

对于执行 PCI DSS 评估的评估商来说，抽样是一种选择，当被测试的群体中有大量项目时，可以促进评估流程。

虽然评估商在审核实体的 PCI DSS 遵从性时，从被测群体中的类似项目中抽样是可以接受的，但实体仅将 PCI DSS 要求应用于其环境的一个样本是不可接受的（例如，每季度的漏洞扫描要求适用于所有系统组件）。同样，评估商仅对 PCI DSS 要求进行抽样审核，以确定是否符合要求，也是不可接受的。

虽然抽样允许评估商对低于100%的特定抽样群体进行测试，但评估商应始终努力实现最全面的审核。如果能够快速有效地测试完整群体（无论规模如何），并且对被评估实体的资源影响最小，我们鼓励评估商使用自动程序或其他机制。如果没有自动程序来测试100%的群体，抽样也是一种同样可以接受的方法。

在考虑了被评估环境的整体范围、复杂性和一致性，以及实体用于满足要求的流程的性质（无论是自动还是手动）后，评估商可以从被审核的群体中独立选择具有代表性的样本，以评估实体是否遵从PCI DSS要求。样本必须是群体中所有变体的代表性选择，并且必须足够大，以保证评估商在整个群体中按预期实施控制。在测试某项要求的定期执行情况时（例如，每周或每季度，或定期），评估商应尝试选择代表评估所涵盖的整个时期的样本，以便评估商可以合理判断该要求在整个评估期间得到满足。年复一年地测试相同的项目样本，可能不会检测到非样本项目的未知变体。评估商必须重新认证每次评估的抽样理由，并考虑以前的样本集。每次评估必须选择不同的样本。

适当选择样本取决于检查样本成员时考虑的内容。例如，确定已知受恶意软件影响的服务器上是否存在反恶意软件，可能会导致确定该群体是环境中的所有服务器，或环境中所有运行特定操作系统的服务器，或所有非大型机的服务器等。然后，选择一个适当的样本将包括所确定群体的所有成员的代表，包括运行确定的操作系统的所有服务器，包括所有版本，以及群体中用于不同功能的服务器（网络服务器、应用服务器、数据库服务器等）。

在考虑特定配置项目的情况下，可以适当地划分群体，并确定单独的样本组。例如，在审核操作系统配置设置时，如果环境中存在不同的操作系统，所有服务器的样本可能并不合适。在这种情况下，每个操作系统类型的样本将适合于识别配置已经为每个操作系统适当地设置。每个样本集应该包括每个操作系统类型的代表性服务器，包括版本，以及代表性功能。

其他抽样的示例包括根据被评估的要求，选择具有类似或不同角色的人员，例如，管理员的样本，以及所有员工的样本。

---

评估商需要在计划、执行和评估样本时使用专业判断，以支持他们关于该实体是否和如何满足要求的结论。评估商抽样的目的是为了获得足够的证据，为他们的意见提供合理依据。在独立选择样本时，评估商应考虑以下几点：

评估商必须在不受被评估实体影响的情况下从完整的群体中选择样本。

如果该实体拥有确保一致性的标准化流程和控制，并且适用于群体中的每个项目，则样本可能比实体没有标准化流程/控制的情况下更小。样本必须足够大，以向评估商提供合理保证，即群体中的项目遵守适用于群体中每个项目的标准化流程。评估商必须核实标准化控制的实施和有效运作。

如果该实体制定了一个以上的标准化流程（例如，针对不同类型的业务设施/系统组件），样本必须包括适用于每种流程的项目。例如，可以根据可能影响评估要求一致性的特征（例如使用不同的流程或工具）将群体划分为子群体。然后从每个子群体中选择样本。

如果该实体没有制定标准化的 PCI DSS 流程/控制，并且是通过非标准化流程来管理群体中的每个项目，则样本必须更大，以便评估商确信 PCI DSS 要求适当地适用于群体中的每个项目。

系统组件的样本必须包括所使用的每种类型和组合。当实体拥有一个以上的 CDE 时，样本必须包括所有范围内系统组件的群体。例如，当抽样应用程序时，样本必须包括每种应用程序的所有版本和平台。

样本量必须始终大于 1，除非在给定群体中只有一个项目，或使用自动控制，评估商已确认该控制在每个被评估的样本群体中按程序运行。

如果评估商依靠制定的标准化流程和控制措施作为选择样本的基础，但在测试过程中发现标准化流程和控制措施没有到位或没有有效运行，则评估商应增加样本量，以试图获得满足 PCI DSS 要求的保证。

对于每个使用抽样的实例，评估商必须：

记录抽样技术和样本量的理由。

认证并记录用于确定样本量的标准化流程和控制。

■ 解释样本合适并代表整个群体的方式。

---

<div style="text-align: center;">图 3 显示了确定样本大小的注意事项。</div>


<div style="text-align: center;">图 3. PCI DSS 抽样注意事项</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_430_256_1192_893.jpg" alt="Image" width="48%" /></div>


注：在 PCI DSS 4.0 版中，所有测试程序都移除了对抽样的具体引用。之所以移除这些引用，是因为在某些测试程序中只提及抽样，可能意味着这些测试程序必须进行抽样（其实不然），或者只有在特别提及的地方才允许抽样。评估商应在适合被测群体的情况下选择样本，并根据上述情况，在考虑环境的整体范围和复杂性后做出这些决定。

---

## 7 PCI DSS 要求中使用的时间框架说明

某些 PCI DSS 要求已经为需要通过定期和可重复的流程持续执行的活动制定了具体的时间框架。其目的是，在尽可能接近该时间框架的间隔内执行该活动，但不超过该时间框架。实体可以自行决定更频繁地执行某项活动（例如，每月执行一项活动，而 PCI DSS 要求规定每三个月执行一次）。

表 4 概述了 PCI DSS 要求中使用的不同时间段的频率。

<div style="text-align: center;">表 4。PCI DSS 要求的时间框架</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>PCI DSS 要求中的时间框架</td><td style='text-align: center; word-wrap: break-word;'>描述和示例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每日</td><td style='text-align: center; word-wrap: break-word;'>一年中的每一天（不仅仅是在工作日）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每周</td><td style='text-align: center; word-wrap: break-word;'>至少每七天一次。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每月</td><td style='text-align: center; word-wrap: break-word;'>至少每 30 至 31 天一次，或在每月的第  $ n $ 天。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每三个月（“每季度”）一次</td><td style='text-align: center; word-wrap: break-word;'>至少每 90 至 92 天一次，或在每三个月的第  $ n $ 天。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每 6 个月</td><td style='text-align: center; word-wrap: break-word;'>至少每 180 至 184 天一次，或在每六个月的第  $ n $ 天。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>每 12 个月（“每年”）一次</td><td style='text-align: center; word-wrap: break-word;'>至少每 365 天（或闰年为 366 天）一次，或在每年的同一天。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期</td><td style='text-align: center; word-wrap: break-word;'>发生的频率由实体自行决定，并由实体的风险分析予以记录和支持。该实体必须证明，该频率对于活动的有效性和满足要求的意图是适当的。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>立即</td><td style='text-align: center; word-wrap: break-word;'>毫不拖延。实时或接近实时。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>迅速</td><td style='text-align: center; word-wrap: break-word;'>在合理范围内尽快进行。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>PCI DSS 要求中的时间框架</td><td style='text-align: center; word-wrap: break-word;'>描述和示例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>重大变化</td><td style='text-align: center; word-wrap: break-word;'>有一些要求，在实体环境发生重大变化时，对其性能进行规定。虽然构成重大变更的因素在很大程度上取决于特定环境的配置，但以下每项活动至少对 CDE 的安全性产生潜在影响，必须在相关 PCI DSS 要求的背景下被视为重大变更：• 添加新的硬件、软件或网络设备到 CDE 中。• CDE 中硬件和软件的任何更换或重大升级。• 帐户数据流动或存储的任何变更。• CDE 的边界和/或 PCI DSS 评估范围的任何变更。• CDE 底层支持基础设施的任何变更（包括但不限于目录服务、时间服务器、日志和监控的变更）。• 支持 CDE 或代表该实体满足 PCI DSS 要求的第三方供应商/服务提供商（或提供的服务）的任何变更。</td></tr></table>

对于其他 PCI DSS 要求，如果标准没有规定定期活动的最低频率，而是允许“定期”满足要求，实体应根据其业务情况规定频率。实体的安全政策和根据 PCI DSS 要求 12.3.1 执行的风险分析必须支持实体规定的频率。该实体还必须能够证明其规定的频率对于活动的有效性和满足要求的意图是适当的。

在这两种情况下，如果 PCI DSS 规定了所需的频率，以及在 PCI DSS 允许“定期”执行的情况下，那么实体应该持有记录和实施的流程，以确保在合理的时间框架内执行该活动，并至少包括以下几点：

当某项活动没有按照其规定的时间表执行时，该实体会被及时通知；

该实体确定导致错过预定活动的事件；

该实体在错过活动后尽快执行该活动，并按计划恢复或制定新的计划；

该实体制作文件，显示上述元素的发生。

当实体制定了上述流程来检测和处理错过的预定活动时，允许采取合理的方法，也就是说，如果规定至少每三个月执行一次活动，那么，如果该活动推到很迟才执行，但遵循了该实体的书面和实施的流程（按上述规定），则并不会自动导致该实体不合规。但是，如果没有此类流程和/或

---

由于监督、管理不善或缺乏监督而未按计划执行活动，则该实体未满足要求。在这种情况下，只有当实体 1）记录（或重新确认）上述流程以确保预定活动按时进行，2）重新制定时间表，以及 3）提供证据证明实体已按其时间表至少执行一次预定活动时，该要求才算到位。

注：对于最初的 PCI DSS 评估（指实体从未接受过先前的评估），如果某项要求有规定的活动时间框架，则不要求在上一年度的每个此类时间框架中都执行该活动，但要求评估商核实：

该活动是在最近的时间范围内（例如，最近的三个月或六个月）按照适用的要求执行的，并且

该实体制定了书面政策和程序，以便在规定的时间内继续执行该活动。

对于初次评估后的后续年份，该活动必须在每个规定的时间框架内至少执行一次。例如，要求每三个月执行一次的活动必须在前一年至少执行了四次，间隔时间不超过90-92天。

---

## 8 实施和认证 PCI DSS 的方法

为了支持在实现安全目标方面的灵活性，有两种方法来实施和认证 PCI DSS。各实体应确定最适合其安全实施的方法，并使用该方法来认证控制。

## 规定的方法

遵循实施和认证 PCI DSS 的传统方法，使用标准中规定的要求和测试程序。在规定的方法中，实体实施安全控制，以满足规定的要求，评估商按照规定的测试程序来核实是否满足了要求。

规定的方法支持拥有符合 PCI DSS 要求的控制措施的实体，如上所述。这种方法也可能适合那些希望在如何满足安全目标方面获得更多指导的实体，以及那些刚接触信息安全或 PCI DSS 的实体。

## 补偿性控制

作为规定的方法的一部分，由于合理的书面技术或业务制约因素而无法明确满足PCI DSS要求的实体可以实施其他控制或补偿性控制，以充分减轻与要求相关的风险。每年，实体必须记录任何补偿性控制措施，并由评估商审核和认证，并包括在提交的遵从性报告中。

注：更多详细信息，请参见附录B：补偿性控制和附录C：补偿性控制工作表。



## 定制方法

重点关注每个 PCI DSS 要求的目标（如果适用），允许实体实施控制以满足要求所述的定制方法目标，其方式并不严格遵循规定的要求。由于每个定制的实施都是不同的，因此没有规定的测试程序；评估商需要制定适合特定实施的测试程序，以认证所实施的控制措施是否满足所述目标。

定制方法支持安全实践创新，允许实体更灵活地展示他们当前的安全控制如何满

注：更多详细信息，请参阅

附录 D：定制方法和附录

E：支持定制方法的样本模

板。



足 PCI DSS 目标。这种方法适用于那些能很好处理风险的实体，即他们展示了强大的安全风险管理方法，包括但不限于专门的风险管理部门或整个组织的风险管理方法。

使用定制方法实施和认证的控制措施预计将达到或超过规定方法中的要求所提供的安全性。认证定制实施所需的文件和努力程度也会比规定的方法更多。

---

可以通过定义或定制的方法来满足大多数 PCI DSS 要求。然而，一些要求没有明确的定制方法目标；定制方法不是这些要求的选择。

各实体可以在其环境中同时使用定义的和定制的方法。这意味着实体可以使用定义的方法来满足一些要求，并使用定制的方法来满足其他要求。这也意味着，实体可以使用定义的方法来满足一个系统组件或一个环境中的特定 PCI DSS 要求，并使用定制的方法来满足不同系统组件或不同环境中的相同 PCI DSS 要求。通过这种方式，PCI DSS 评估可以包括定义和定制的测试程序。

图 4 显示了 PCI DSS 4.0 版的两个认证选项。

---

<div style="text-align: center;">图 4。PCI DSS 认证方法</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_416_209_1197_888.jpg" alt="Image" width="49%" /></div>


---

## 9 保护有关实体安全状况的信息

与成为和维护 PCI DSS 遵从性环境有关的流程会产生许多实体可能认为敏感的人工伪造产物，并可能希望以此来保护这些人工伪造产物，包括以下项目：

遵从性报告或自我评估调查问卷（相关遵从性证明不被认为是敏感的，第三方服务提供商（TPSP）应与客户分享其 AOC）。

网络图和帐户数据流程图，以及安全配置和规则。

系统配置标准。

加密和密钥管理方法和协议。

各实体应审核与 PCI DSS 控制或评估有关的所有人工伪造产物，并根据实体对此类信息的安全政策进行保护。

TPSP 需要（PCI DSS 要求 12.9）为其客户提供以下支持：

客户监控 TPSP 的 PCI DSS 遵从性状态所需的信息（使客户能够遵守要求 12.8），以及

如果 TPSP 的服务旨在满足或促进满足客户的 PCI DSS 要求，或者这些服务可能影响客户 CDE 的安全，则证明 TPSP 符合适用的 PCI DSS 要求。

本节不影响或否定 TPSP 根据要求 12.9 向其客户提供支持和信息的义务。

关于对 TPSP 的期望以及 TPSP 与客户之间关系的更多详细信息，请参见第三方服务供应商的使用。

## 合格安全性评估商公司保护机密和敏感信息

每个合格安全性评估商（QSA）公司都会与 PCI SSC 签署协议，表明他们将遵守 QSA 的资格要求。该文件的保护机密和敏感信息部分包括以下内容：

"QSA 公司必须拥有并遵守保护机密和敏感信息的书面流程。这必须包括符合行业公认做法的充分物理、电子和程序保障措施，以保护机密和敏感信息存储、处理和/或交流这些信息时不受任何威胁或未经授权的访问。

---

QSA 公司必须维护其在履行 QSA 公司职责和义务过程中获得的信息的隐私权和保密性，除非（以及在一定程度上）法律授权要求披露这些信息。

---

## 10 PCI DSS 要求的测试方法

每项要求的测试程序中确定的测试方法描述了评估商为确定实体是否满足要求而要执行的预期活动。每个测试方法的目的描述如下：

检查：评估商严格评估数据证据。常见示例包括文件（电子或物理），屏幕截图，配置文件，检查日志，和数据文件。

观察：评估员观察其环境中的某些事物或动作。观察对象的实例包括执行任务或流程的人员、执行功能或响应输入的系统、环境条件和物理限制。

询问：评估商与个别工作人员进行交谈。询问的目的可能包括确认是否执行了某项活动，描述如何执行某项活动，以及相关人员是否具有特定的知识或理解。

测试方法旨在让被评估实体证明他们满足要求的具体方式。它们还让被评估实体和评估商共同了解到将要执行的评估活动。要检查或观察的特定项目和要询问的人员应该适合于被评估的要求和每个实体的特定实施。在记录评估结果时，评估商确定所执行的测试活动以及每项活动的结果。

---

## 11 遵从性报告的说明和内容

PCI DSS 遵从性报告（ROC）模板提供了遵从性报告（ROC）的说明和内容。

必须使用 PCI DSS 遵从性报告（ROC）模板作为创建 PCI DSS 遵从性报告的模板。

是否要求任何实体遵守或认证其是否遵从 PCI DSS 的要求，由管理遵从性计划的组织（例如支付品牌和收单机构）自行决定。各实体应联系相关组织，以确定任何报告要求和指示。

---

## 12 PCI DSS 评估流程

PCI DSS 评估流程包括以下高层次步骤： $ ^{5} $

1. 确认 PCI DSS 评估的范围。

2. 执行 PCI DSS 环境评估。

3. 根据 PCI DSS 指南和说明，完成适用的评估报告。

4. 完整填写《服务供应商或商户遵从性证明》（如适用）。正式的遵从性证明仅在 PCI SSC 网站上提供。

5. 将适用的 PCI SSC 文件和遵从性证明，以及任何其他要求的文件，例如 ASV 扫描报告，提交给提出请求的组织（那些管理遵从性计划的组织，例如支付品牌和收单机构（针对商户），或其他请求者(针对服务提供商)。

6. 如果需要，执行补救措施，以解决未到位的要求，并提供一份最新报告。

注：如果控制措施尚未实施或计划在未来某个日期完成，则不认为 PCI DSS 要求已经到位。在实体解决了任何开放或未到位的项目后，评估商将重新评估，以确认补救措施已经完成，并满足所有要求。请参考以下资源（可在 PCI SSC 网站查询），以记录 PCI DSS 评估：

• 关于完成遵从性报告（ROC）的指示，请参阅 PCI DSS 遵从性报告（ROC）模板。

- 有关填写自我评估调查问卷（SAQ）的指示，请参阅 PCI DSS SAQ 指示和指南。

- 有关提交 PCI DSS 遵从性认证报告的指示，请参阅 PCI DSS 遵从性证明。

---

## 13 其他参考资料

表 5 列出了在 PCI DSS 要求或相关指南中引用的外部组织。这些外部组织及其参考资料仅作为信息提供，并不取代或扩展任何 PCI DSS 要求。

<div style="text-align: center;">表 5。PCI DSS 要求中引用的外部组织</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参考资料</td><td style='text-align: center; word-wrap: break-word;'>完整名称</td><td style='text-align: center; word-wrap: break-word;'>来源</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ANSI</td><td style='text-align: center; word-wrap: break-word;'>美国国家标准协会</td><td style='text-align: center; word-wrap: break-word;'>www.ansi.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CIS</td><td style='text-align: center; word-wrap: break-word;'>互联网安全中心</td><td style='text-align: center; word-wrap: break-word;'>www.cisecurity.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CSA</td><td style='text-align: center; word-wrap: break-word;'>云安全联盟</td><td style='text-align: center; word-wrap: break-word;'>www.csa.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ENISA</td><td style='text-align: center; word-wrap: break-word;'>欧盟网络安全局（前称欧洲网络和信息安全局）</td><td style='text-align: center; word-wrap: break-word;'>www.enisa.europa.eu</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FIDO 联盟</td><td style='text-align: center; word-wrap: break-word;'>FIDO 联盟</td><td style='text-align: center; word-wrap: break-word;'>www.fidoalliance.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ISO</td><td style='text-align: center; word-wrap: break-word;'>国际标准化组织</td><td style='text-align: center; word-wrap: break-word;'>www.iso.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NCSC</td><td style='text-align: center; word-wrap: break-word;'>英国国家网络安全中心</td><td style='text-align: center; word-wrap: break-word;'>www.ncsc.gov.uk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NIST</td><td style='text-align: center; word-wrap: break-word;'>国家标准与技术研究所</td><td style='text-align: center; word-wrap: break-word;'>www.nist.gov</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OWASP</td><td style='text-align: center; word-wrap: break-word;'>开放式网络应用程序安全项目</td><td style='text-align: center; word-wrap: break-word;'>www.owasp.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SAFEcode</td><td style='text-align: center; word-wrap: break-word;'>卓越代码软件保障论坛</td><td style='text-align: center; word-wrap: break-word;'>www.safecode.org</td></tr></table>

---

## 14 PCI DSS 版本

截至本文件发布之日，PCI DSS v3.2.1 的有效期至 2024 年 3 月 31 日，此日期后将停用。此日期后，所有 PCI DSS 认证必须参考 PCI DSS 4.0 版或更新版本。

PCI DSS 3.2.1 版或 4.0 版均可用于 2022 年 3 月至 2024 年 3 月 31 日之间执行的评估。

表 6 概述了 PCI DSS 版本及其相关日期。 $ ^{6} $

<div style="text-align: center;">表 6. PCI DSS 版本</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>版本</td><td style='text-align: center; word-wrap: break-word;'>已发布</td><td style='text-align: center; word-wrap: break-word;'>已退役</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCI DSS 4.0 版 (本文件)</td><td style='text-align: center; word-wrap: break-word;'>2022 年 3 月</td><td style='text-align: center; word-wrap: break-word;'>待定</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCI DSS 3.2.1 版</td><td style='text-align: center; word-wrap: break-word;'>2018 年 5 月</td><td style='text-align: center; word-wrap: break-word;'>2024 年 3 月 31 日</td></tr></table>

---

## 15 详细的 PCI DSS 要求和测试程序

图 5 描述了 PCI DSS 要求的列标题和内容。

<div style="text-align: center;">图 5。了解要求的各个部分</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_123_345_1432_948.jpg" alt="Image" width="82%" /></div>


定义

可以帮助理解要求的术语。

示例描述了满足要求的方法。

更多信息包括相关外部文件的引用。

---

## 仅针对服务供应商的额外要求

有些要求仅在被评估实体是服务提供商的情况下适用。这些要求在要求中被确定为“仅针对服务供应商的额外要求”，并适用于所有其他适用的要求。如果被评估的实体既是商户又是服务提供商，则注明为“仅针对服务提供商的额外要求”的要求适用于该实体业务中的服务提供商部分。标有“仅针对服务提供商的额外要求”的要求也被推荐为最佳实践，供所有实体考虑。

## 附录，针对不同类型实体的额外 PCI DSS 要求

除了 12 项主要要求之外，PCI DSS 附录 A 还包含针对不同类型实体的额外 PCI DSS 要求。在附录 A 中，章节包括：

附录 A1：针对多租户服务提供商的额外 PCI DSS 要求。

附录 A2：针对使用 SSL/早期 TLS 进行实体信用卡 POS POI 终端连接的实体的额外 PCI DSS 要求

■ 附录 A3：指定的实体补充认证(DESV)

---

## 建立和维护安全网络和系统

<div style="text-align: center;">要求 1： 安装和维护网络安全控制</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>章节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>确定和理解安装和维护网络安全控制的流程和机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>配置和维护网络安全控制（NSC）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>限制持卡人数据环境的网络访问权限。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>控制可信网络和不可信网络之间的网络连接。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.5</td><td style='text-align: center; word-wrap: break-word;'>减轻能够连接到不可信网络和 CDE 的计算设备对 CDE 产生的风险。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>概述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>网络安全控制（NSC），例如防火墙和其他网络安全技术，是网络策略执行点，通常根据预先定义的策略或规则控制两个或多个逻辑或物理网络分段（或子网）之间的网络流量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NSC 检查所有进入（入口）和离开（出口）网络分段的网络流量，并根据确定的策略决定是否允许网络流量通过，或是否应该拒绝通过。通常情况下，NSC 被置于具有不同安全需求或信任程度的环境之间，然而在一些环境中，NSC 不分信任界限控制着个别设备的流量。政策执行通常发生在 OSI 模型的第 3 层，但存在于更高层的数据也经常被用来确定政策决策。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>传统上，该功能由物理防火墙提供；然而，现在该功能可能由虚拟设备、云访问控制、虚拟化/容器系统和其他软件定义网络技术提供。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NSCs 用于控制实体自身网络内的流量—例如，在高敏感区域和低敏感区域之间，也用于保护实体的资源免于不可信网络的影响。持卡人数据环境（CDE）是一个实体网络中较敏感区域的例子。通常情况下，进出不可信网络的看似微不足道的路径可以提供进入敏感系统的无保护途径。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NSCs 提供了任何计算机网络的关键保护机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不可信网络的常见例子包括互联网、专用连接，例如企业对企业的通信渠道、无线网络、运营商网络（例如手机）、第三方网络，以及实体控制能力之外的其他来源。此外，不可信网络还包括被认为是 PCI DSS 范围外的企业网络，因为它们没有接受评估，因此必须被视为不可信，因为安全控制的存在尚未得到验证。虽然实体可能从基础设施的角度认为内部网络是可信的，但如果网络不在 PCI DSS 的范围内，则该网络对于 PCI DSS 必须被视为不可信网络。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>请参阅附录 G 了解 PCI DSS 术语的定义。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">1.1 确定和理解安装和维护网络安全控制的流程和机制。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="2">目的要求 1.1.1 涉及有效管理和维护整个要求 1 规定的各种政策和程序。虽然定义要求 1 中规定的具体政策或程序很重要，但同样重要的是确保适当地记录、维护和传播这些政策或程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.1.1 要求 1 中确定的所有安全政策和操作程序都：• 有文件记录。• 保持时效性。• 在使用中。• 为所有受影响的各方所了解。</td><td style='text-align: center; word-wrap: break-word;'>1.1.1 检查文件并询问相关人员，以核实是否根据要求中规定的所有元素管理了要求 1 中确定的安全政策和操作程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标受影响人员确定满足要求 1 的活动的期望、控制和监督，并由其理解并遵守。所有支持性活动都可重复一致适用，并符合管理层的意图。</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>良好做法视情况更新政策和程序，以应对流程、技术和业务目标的变化，这一点很重要。出于这个原因，考虑在变化发生后尽快更新这些文件，而不仅仅是在定期周期内。定义安全政策定义了实体的安全目标和原则。操作程序描述了如何执行活动，并确定了为以一致的方式并根据政策目标实现预期结果而遵循的控制、方法和流程。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的如果没有正式分配角色和责任，相关人员可能不知道他们的日常责任，关键活动可能不会发生。良好做法可以将角色和责任记录在政策和程序中，也可以保存在单独的文件中。作为沟通角色和责任的一部分，实体可以考虑让人员承认他们接受并理解所分配的角色和责任。示例记录角色和责任的一种方法是责任分配矩阵，包括谁负责、谁问责、谁咨询、谁知情（也称为RACI矩阵）。</td></tr><tr><td rowspan="2">1.1.2 记录、分配和理解执行要求 1 中活动的角色和责任。</td><td style='text-align: center; word-wrap: break-word;'>1.1.2.a 检查文件，以核实是否记录和分配了执行要求 1 中活动的角色和责任的描述。</td></tr><tr><td rowspan="2">1.1.2.b 询问负责执行要求 1 中的活动的人员，以核实是否按照文件规定分配了角色和责任，这些角色和责任是否被理解。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标分配执行要求 1 中所有活动的日常责任。人员要对这些要求的成功和持续运行负责。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">1.2 配置和维护网络安全控制（NSC。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td rowspan="2">规定的方法测试程序</td><td rowspan="2">目的实施这些配置标准导致 NSC 的配置和管理，以正确执行其安全功能（通常称为规则集）。良好做法这些标准通常确定了可接受协议的要求，允许使用的端口，以及可接受的具体配置要求。配置标准也可能概述了实体认为在其网络内不可接受或不允许的元素。定义NSC 是网络架构的关键组成部分。最常见的是，NSC 被用于 CDE 的边界，以控制输入和输出CDE 的网络流量。配置标准概述了实体对配置其 NSC 的最低要求。示例这些配置标准所涵盖的 NSC 的例子包括但不限于防火墙、配置有访问控制列表的路由器和云虚拟网络。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.1 NSC 规则集的配置标准：• 已确定。• 已实施。• 已维护。定制方法目标确定并持续运用配置和运行 NSC 的方式。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>良好做法</td></tr><tr><td rowspan="3">1.2.2 根据要求 6.5.1 中确定的变更控制流程审批和管理网络连接和 NSC 配置的所有变更。</td><td style='text-align: center; word-wrap: break-word;'>1.2.2.a 检查书面程序，核实网络连接和 NSC 配置的变更是否根据要求 6.5.1 的规定纳入了正式的变更控制流程。</td><td style='text-align: center; word-wrap: break-word;'>变更应该由具有适当权力和知识的个人批准，以了解变更的影响。核实应该提供合理保证，即变更没有对网络安全产生不利影响，并且变更按预期执行。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.2.b 检查网络配置设置，以确定对网络连接所做的变更。询问负责人员并检查变更控制记录，核实是否根据要求 6.5.1 的规定批准和管理了确定的网络连接变更。</td><td rowspan="7">为了避免不得不解决由变更引入的安全问题，所有变更都应在实施前获得批准，并在变更实施后进行核实。一旦获得批准和核实，网络文件应予更新（纳入这些变更），以防止网络文件和实际配置之间存在不一致。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.2.c 检查网络配置设置，以确定对 NSC 配置所做的变更。询问负责人员并检查变更控制记录，核实是否根据要求 6.5.1 的规定批准和管理了确定的 NSC 配置变更。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>网络连接和 NSC 的变更不能导致错误的配置、非安全服务的实施或未经授权的网络连接。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>网络连接的变更包括增加、移除或修改连接。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NSC 配置的变更包括那些与组件本身有关的变更，以及那些影响其如何执行安全功能的变更。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td rowspan="2">1.2.3 保持一份准确的网络图，显示 CDE 和其他网络之间的所有连接，包括任何无线网络。</td><td style='text-align: center; word-wrap: break-word;'>1.2.3.a 检查网络图和网络配置，以核实是否存在符合本要求中规定的所有元素的准确网络图。</td><td style='text-align: center; word-wrap: break-word;'>保持一个准确、最新的网络图可以防止网络连接和设备被忽视，并在不知情的情况下留在不安全的位置和易于遭到威胁。</td></tr><tr><td rowspan="10">1.2.3.b 检查文件和询问负责人员，以核实网络图是否准确，并在环境发生变化时进行更新。</td><td style='text-align: center; word-wrap: break-word;'>适当维护的网络图通过识别连接到 CDE 的系统，帮助组织核实其 PCI DSS 范围。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保持并提供显示 CDE、所有可信网络和所有不可信网络之间的边界的图示。</td><td style='text-align: center; word-wrap: break-word;'>与 CDE 的所有连接应予以确定，包括为 CDE 系统组件提供安全、管理或维护服务的系统。各实体应考虑在其网络图中包括以下元素：</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'>· 所有地点，包括零售地点、数据中心、公司地点、云提供商等。</td></tr><tr><td rowspan="6">当前网络图或其他确定网络连接和设备的技术或拓扑解决方案可用于满足这项要求。</td><td style='text-align: center; word-wrap: break-word;'>· 所有网络分段的明确标识。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>· 提供分段的所有安全控制，包括每个控制的唯一标识符（例如，控制的名称、品牌、型号和版本）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>· 所有范围内系统组件，包括 NSC、网络应用程序防火墙、反恶意软件解决方案、变更管理解决方案、IDS/IPS、日志聚合系统、支付终端、支付应用程序、HSM 等。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>· 通过阴影框或其他机制对图中任何超出范围的区域进行明确标识。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>· 最后更新日期，以及作出和批准更新的人的姓名。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>（下一页继续）</td></tr></table>

支付卡行业数据安全标准：要求及测试程序，4.0版

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>· 解释图表的图例或密钥。授权人员应该更新网络图，以确保该等图继续提供网络的准确描述。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="7">目的一个随时可用的最新数据流程图通过显示帐户数据如何在网络上以及在单个系统和设备之间流动，帮助组织了解和跟踪其环境范围。保持最新的数据流程图可以防止帐户数据被忽视，并在不知情的情况下留在不安全的位置。良好做法数据流程图应包括所有接收帐户数据进入和送出网络的连接点，包括与开放的公共网络的连接、应用程序处理流、存储、系统和网络之间的传输以及文件备份。数据流程图是网络图的补充，应该与网络图相协调并对其进行补充。作为一种最佳实践，实体可以考虑在其数据流程图中包括以下内容：·所有帐户数据的处理流程，包括授权、采集、结算、拒付和退款。·所有不同的受理渠道，包括实体信用卡、虚拟信用卡和电子商务。·所有类型的数据接收或传输，包括任何涉及硬拷贝/纸质媒体。·帐户数据从进入环境到最终处置的流程。·传输和处理帐户数据的位置，储存帐户数据的位置，以及储存是短期的还是长期的。（下一页继续）</td></tr><tr><td rowspan="2">1.2.4 保持一份满足以下要求的准确数据流程图：·显示所有帐户数据在系统和网络间的流动情况。·在环境发生变化时视需要进行更新。</td><td style='text-align: center; word-wrap: break-word;'>1.2.4.a 检查数据流程图并询问相关人员，以核实该图是否根据本要求规定的所有元素显示了所有帐户数据流。</td></tr><tr><td rowspan="5">1.2.4.b 检查文件和询问负责人员，以核实数据流程图是否准确，并在环境发生变化时进行更新。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保持并提供显示系统组件之间和跨网络分段的所有帐户数据传输的图示。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据流程图或其他确定帐户数据在系统和网络间的流动的技术或拓扑解决方案可用于满足这项要求。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">规定的方法要求1.2.5 确定并批准所有允许的服务、协议和端口，并且具有明确的业务需求。定制方法目标未经授权的网络流量（服务、协议或以特定端口为目的地的数据包）不能进入或离开网络。</td><td style='text-align: center; word-wrap: break-word;'>· 收到的所有帐户数据的来源（例如，客户、第三方等），以及与之共享帐户数据的任何实体。· 最后更新日期，以及作出和批准更新的人的姓名。</td><td rowspan="2"></td></tr><tr><td rowspan="2">规定的方法测试程序1.2.5.a 检查文件以核实是否存在所有允许的服务、协议和端口的清单，包括每项服务的业务理由和批准。1.2.5.b 检查 NSC 的配置设置，核实是否只有经批准的服务、协议和端口在使用。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>目的由于未使用或非安全服务（例如 telnet 和 FTP）、协议和端口，威胁频频发生，因为这些因素会导致开放进入 CDE 的不必要访问点。此外，对于已启用但未使用的服务、协议和端口，它们往往被忽视，留在不安全的位置，并且未执行补充程式。通过识别业务所需的服务、协议和端口，实体可以确保所有其他服务、协议和端口均已禁用或移除。良好做法应该了解与允许的每个服务、协议和端口相关的安全风险。应由独立于管理配置的人员授予批准。审批人员应具备适合做出审批决定的知识和责任。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的威胁利用非安全网络配置。良好做法如果非安全服务、协议或端口对业务来说是必要的，那么组织应该清楚地理解和接受这些服务、协议和端口所带来的风险，该服务、协议或端口的使用应该是合理的，并且实体应该确定和实施减轻使用这些服务、协议和端口风险的安全功能。更多信息关于被视为非安全服务、协议或端口的指导，请参考行业标准和指导（例如，来自 NIST、ENISA、OWASP）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.6 确定并实施所有正在使用的、被视为是非安全服务、协议和端口的安全功能，以至于风险得到缓解。</td><td rowspan="3">1.2.6.a 检查识别所有正在使用的非安全服务、协议和端口的文件，核实是否确定了每个服务、协议和端口的安全功能，以至于风险得到缓解。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>了解、评估与使用不安全服务、协议和端口有关的具体风险，并适当地加以缓解。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td rowspan="2">1.2.7 至少每六个月对 NSC 的配置进行一次审核，以确认其相关性和有效性。</td><td style='text-align: center; word-wrap: break-word;'>1.2.7.a 检查文件，核实是否制定了相应程序，至少每六个月对 NSC 的配置进行一次审核。</td><td rowspan="2">这种审核使组织有机会清理任何不需要的、过时的或不正确的规则和配置，因为未经授权的人可能会利用这些规则和配置。此外，它确保所有规则和配置只允许授权的服务、协议和端口，以符合书面业务理由。良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.7.b 检查有关审核 NSC 配置的文件并询问负责人员，核实审核是否至少每六个月执行了一次。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="3">1.2.7.c 检查 NSC 配置，核实是否移除或更新了被确定为不再受业务理由支持的配置。</td><td style='text-align: center; word-wrap: break-word;'>这项审核可以使用手动、自动或基于系统的方法实施，目的是确认管理流量规则的设置、允许进出网络的内容与批准的配置相符。</td></tr><tr><td rowspan="2">定期核实允许或限制访问可信网络的 NSC 配置，以确保只允许具有当前业务理由的授权连接。</td><td style='text-align: center; word-wrap: break-word;'>审核应确认所有允许的访问权限都有合理的业务理由。任何关于规则或配置的差异或不确定性都应上报予以解决。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>虽然该要求规定这项审核至少每六个月执行一次，但对其网络配置进行大量更改的组织来说，他们可能会考虑更频繁地执行审核，以确保配置继续满足业务需求。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的为了防止未经授权的配置被应用到网络中，具有网络控制配置的存储文件需要保持最新，并确保其不受未经授权的更改。确保配置信息的时效性和安全性确保每当运行配置时都能应用正确的 NSC 设置。示例如果路由器的安全配置存储在非易失性存储器中，当重启该路由器时，这些控制应确保其安全配置得到恢复。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.2.8 NSC 的配置文件：· 受到保护免于未经授权的访问。· 与现行网络配置保持一致。</td><td style='text-align: center; word-wrap: break-word;'>1.2.8. 检查 NSC 的配置文件，以核实它们是否符合本要求中规定的所有元素。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>不能使用不可信的配置对象（包括文件）确定或修改NSC。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'>任何用于配置或同步 NSC 的文件或设置都被视为是“配置文件”。这包括文件、自动和基于系统的控制、脚本、设置、作为代码的基础设施，或其他备份、存档或远程存储的参数。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">1.3 限制持卡人数据环境的网络访问权限。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的本要求旨在防止恶意者通过未经授权的 IP 地址访问实体的网络，或以未经授权的方式使用服务、协议或端口。良好做法应该评估所有输入 CDE 的流量，无论流量来自哪里，以确保它遵循既定的授权规则。应该对连接进行检查，以确保流量只限于授权通信—例如，通过限制源/目的地址和端口，以及阻止内容。示例实施一项规则，拒绝所有非特别需要的输入和输出流量—例如，通过使用明确的“拒绝所有”或允许声明后的隐含拒绝，有助于防止无意中的漏洞，允许非预期和潜在的有害流量。</td></tr><tr><td rowspan="2">1.3.1 限制输入 CDE 的流量，具体如下：· 只限制必要的流量。· 明确拒绝所有其他流量。</td><td style='text-align: center; word-wrap: break-word;'>1.3.1.a 检查 NSC 的配置标准，核实它们所确定的限制输入 CDE 的流量是否符合本要求中规定的所有元素。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.3.1.b 检查 NSC 的配置，核实是否根据本要求中规定的所有元素限制了输入 CDE 的流量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>未经授权的流量不能进入 CDE。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.3.2 限制输出 CDE 的流量，具体如下：• 只限制必要的流量。• 明确拒绝所有其他流量。</td><td style='text-align: center; word-wrap: break-word;'>1.3.2.a 检查 NSC 的配置标准，核实它们所确定的限制输出 CDE 的流量是否符合本要求中规定的所有元素。</td><td rowspan="3">本要求旨在防止实体网络内的恶意者和受威胁系统组件与不可信的外部主机进行通信。良好做法应该评估所有输出 CDE 的流量，无论其目的地是哪里，以确保它遵循既定的授权规则。应该对连接进行检查，以便流量只限于授权通信—例如，通过限制源/目的地址和端口，以及阻止内容。示例实施一项规则，拒绝所有非特别需要的输入和输出流量—例如，通过使用明确的“拒绝所有”或允许声明后的隐含拒绝，有助于防止无意中的漏洞，允许非预期和潜在的有害流量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">1.3.2.b 检查 NSC 的配置，核实是否根据本要求中规定的所有元素限制了输出 CDE 的流量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未经授权的流量不得离开 CDE。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td rowspan="4">规定的方法测试程序</td><td rowspan="4">目的网络中已知的（或未知的）无线技术的实施和利用是恶意者访问网络和帐户数据的常见途径。如果在实体不知情的情况下安装了无线设备或网络，那么恶意者可以轻松地“隐身”进入网络。如果 NSC 不限制从无线网络进入 CDE，未经授权访问无线网络的恶意者可以轻松地连接到 CDE 并威胁帐户信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.3.3 NSC 安装在所有无线网络和 CDE 之间，无论无线网络是否为 CDE，为此：• 默认拒绝所有从无线网络进入 CDE 的无线流量。• 仅允许具有授权商业目的的无线流量进入 CDE。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未经授权的流量不得穿越 CDE 中任何无线网络和有线环境之间的网络边界。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">1.4 控制可信网络和不可信网络之间的网络连接。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.4.1 NSC 在可信网络和不可信网络之间实施。</td><td style='text-align: center; word-wrap: break-word;'>1.4.1.a 检查配置标准和网络图，以核实 NSC 是否在可信和不可信的网络之间实施。</td><td style='text-align: center; word-wrap: break-word;'>在进入和离开可信网络的每个连接处实施 NSC，允许实体监控和控制访问权限，并最大限度地降低恶意者通过不受保护的连接获得内部网络访问权限的机会。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">1.4.1.b 检查网络配置，以核实 NSC 是否根据书面配置标准和网络图在可信和不可信的网络之间实施。</td><td rowspan="2">示例实体可以实施 DMZ，它是网络的一部分，负责管理不可信网络（关于不可信网络的例子，请参考要求 1 概述）和组织需要向公众提供的服务（例如 Web 服务器）之间的连接。请注意，如果实体的 DMZ 处理或传输 帐户数据（例如，电子商务网站），它也被视为 CDE。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未经授权的流量不能穿越可信网络和不可信网络之间的网络边界。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.4.2 限制从不可信网络输入可信网络的流量，具体如下：• 与获授权提供公开访问的服务、协议和端口的系统组件进行通信。• 有状态响应可信网络中系统组件启动的通信。• 拒绝所有其他通信。</td><td rowspan="2">1.4.2. 检查供应商的文件和 NSC 的配置，核实是否根据本要求规定的所有元素限制了从不可信网络输入到可信网络的流量。</td><td rowspan="4">确保明确授权系统组件的公共访问权限，减少系统组件不必要地暴露在不可信网络中的风险。良好做法提供公开访问服务的系统组件，例如电子邮件、网络和 DNS 服务器，最易受到来自不可信网络的威胁。理想情况下，这些系统被置于一个专门的可信网络中，该网络面向公众（例如，DMZ），但通过 NSC 与更敏感的内部系统分离开来，这有助于在这些外部访问系统被威胁时保护网络的其余部分。此功能的目的是防止恶意行为者从互联网访问组织的内部网络，或以未经授权的方式使用服务、协议或端口。如果作为 NSC 的内置功能提供该功能，该实体应确保其配置不会导致该功能被禁用或绕过。定义维护每个连接到网络的“状态”意味着 NSC“知道”对先前连接的明显响应是有效的授权响应（因为 NSC 保留了每个连接的状态），还是试图欺骗 NSC 以允许连接的恶意流量。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>只有经过授权或响应可信网络中的系统组件的流量才能从不可信网络进入可信网络。</td><td rowspan="2">适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本要求旨在解决可信和不可信网络之间的通信会话，并非解决协议的具体细节。如果状态由 NSC 维护，该要求并不限制 UDP 或其他无连接网络协议的使用。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求1.4.3 实施反欺骗措施，以检测和阻止伪造的源 IP 地 址进入可信网络。定制方法目标具有伪造 IP 源地址的数据包不得进入可信网络。</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序1.4.3 检查供应商的文件和 NSC 的配置，核实是否实施了反欺骗措施，以检测和阻止伪造的源 IP 地址进入可信网络。</td><td style='text-align: center; word-wrap: break-word;'>目的过滤进入可信网络的数据包有助于，除其他外，确保数据包不会被“欺骗”，使其看起来像是来自组织自己的内部网络。例如，反欺骗措施防止来自互联网的内部地址进入 DMZ。良好做法产品通常将反欺骗设置为默认，可能无法对其进行配置。各实体应查阅供应商的文件以了解更多信息。示例通常，数据包包含最初发送它的计算机的 IP 地址，因此网络中的其他计算机知道该数据包的来源。恶意者通常会试图欺骗（或模仿）发送的 IP 地址，以愚弄目标系统，使其相信该数据包来自可信来源。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="6">目的如果可以从可信网络直接访问持卡人数据，例如，因为它存储在 DMZ 内的系统或云数据库服务中，外部攻击者便可轻松地访问持卡人数据，因为可以穿透的防御层更少。使用 NSC 来确保只能从可信网络直接访问存储持卡人数据的系统组件（例如数据库或文件），可以防止未经授权的网络流量进入系统组件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.4.4 不能从不可信网络直接访问存储持卡人数据的系统组件。</td><td style='text-align: center; word-wrap: break-word;'>1.4.4.a 检查数据流程图和网络图，核实是否有文件规定不能从不可信网络直接访问存储持卡人数据的系统组件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>1.4.4.b 检查 NSC 的配置，核实是否实施了控制措施，确保不能从不可信网络直接访问存储持卡人数据的系统组件。</td></tr><tr><td colspan="2">不能从不可信网络访问存储的持卡人数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本要求不旨在适用于在易失性存储器中存储帐户数据，但确实在存储器被视为持久性存储器的情况下适用（例如，RAM 磁盘）。帐户数据只能在支持相关业务流程所需的时间内存储在易失性存储器中（例如，直到相关支付卡交易完成为止）。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的限制内部、私人和本地 IP 地址的披露，有助于防止黑客了解这些 IP 地址，并利用这些信息来访问网络。良好做法用于满足这项要求的方法可能有所不同，视所使用的特定网络技术而定。例如，用于满足该要求的控制对于 IPv4 网络和 IPv6 网络可能有所不同。示例掩盖 IP 地址的方法可能包括，但不限于：• IPv4 网络地址转换（NAT）。• 将系统组件置于代理服务器/NSC 后面。• 删除或过滤使用注册地址的内部网络的路由广告。• 内部使用 RFC 1918（IPv4）或在向互联网发起外发会话时使用 IPv6 隐私扩展（RFC 4941）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.4.5 内部 IP 地址和路由信息仅披露给授权方。</td><td style='text-align: center; word-wrap: break-word;'>1.4.5.a 检查 NSC 的配置，以核实内部 IP 地址和路由信息是否仅披露给授权方。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">1.4.5.b 询问相关人员并检查文件，核实是否实施了控制措施，使内部 IP 地址和路由信息仅披露给授权方。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保护内部网络信息免于未经授权的披露。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">1.5 减轻能够连接到不可信网络和 CDE 的计算设备对 CDE 产生的风险。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的允许从非企业环境连接到互联网的计算设备（例如，台式计算机、笔记本电脑、平板电脑、智能手机和员工使用的其他移动计算设备）更容易受到基于互联网的威胁。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.5.1 安全控制施加于任何连接到不可信网络（包括互联网）和 CDE 的计算设备，包括公司和员工拥有的设备，具体如下：• 确定具体配置设置，以防止威胁被引入实体的网络中。• 安全控制主动运行。• 计算设备的用户不能改变安全控制，除非有明确记录并由管理层在有限时间内逐案授权。</td><td rowspan="3">1.5.1.a 检查政策和配置标准并询问相关人员，以核实是否根据本要求中规定的所有元素实施了连接到不可信网络和 CDE 的计算设备的安全控制。</td><td rowspan="3">使用安全控制措施，例如基于主机的控制措施（例如，个人防火墙软件或终端保护解决方案）、基于网络的安全控制措施（例如，防火墙、基于网络的启发式检查和恶意软件模拟）或硬件，有助于保护设备免受基于互联网的攻击，因为当设备重新连接到网络时，攻击者可以利用设备获得组织的系统和数据的访问权限。（下一页继续）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>连接到不可信环境并同时连接到 CDE 的设备不能将威胁引入到实体的 CDE。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'>良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>仅当有合理技术需要时，经管理层逐案授权，才可以暂时禁用这些安全控制。如果出于特定目的需要禁用这些安全控制，必须经正式授权。在这些安全控制未被激活期间，可能还需要实施其他安全措施。这项要求适用于员工拥有和公司拥有的计算设备。不能由公司政策管理的系统会引入弱点，并提供恶意者可能加以利用的机会。</td><td style='text-align: center; word-wrap: break-word;'>具体配置设置由实体决定，应符合其网络安全政策和程序。如果有合理需要暂时禁用连接到不可信网络和CDE的公司或员工拥有的设备上的安全控制—例如，支持特定的维护活动或调查技术问题—适当的管理代表应理解采取这种行动的原因，并予以批准。对于这些安全控制的任何禁用或更改，包括在管理员自己的设备上的禁用或更改，都由授权人员执行。一般认为，管理员拥有的特权可能允许他们禁用自己计算机上的安全控制，但当禁用这些控制时，应该要有警报机制，并采取后续行动以确保程序得到遵循。示例做法包括禁止为员工拥有的或企业拥有的移动设备分割VPN隧道，并要求这些设备启动时进入VPN。</td></tr></table>

---

## 要求 2： 安全配置应用于所有系统组件


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>章节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>确定和理解安全配置应用于所有系统组件的流程和机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2</td><td style='text-align: center; word-wrap: break-word;'>安全配置和管理系统组件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>安全配置和管理无线环境。</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>概述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>恶意者，无论是来自外部还是内部，经常使用默认密码和其他供应商的默认设置来威胁系统。这些密码和设置为我们所知，可轻松通过公共信息予以确定。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>将安全配置应用于系统组件，可以减少攻击者威胁系统的可用手段。更改默认密码，删除不必要的软件、功能和帐户，以及禁用或删除不必要的服务都有助于减少潜在的攻击面。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>请参阅附录 G 了解 PCI DSS 术语的定义。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">2.1 确定和理解安全配置应用于所有系统组件的流程和机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="3">目的要求 2.1.1 涉及有效管理和维护整个要求 2 规定的各种政策和程序。虽然定义要求 2 中规定的具体政策或程序很重要，但同样重要的是确保适当地记录、维护和传播这些政策或程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1.1 要求 2 中确定的所有安全政策和操作程序都：• 有文件记录。• 保持时效性。• 在使用中。• 为所有受影响的各方所了解。</td><td style='text-align: center; word-wrap: break-word;'>2.1.1 检查文件并询问相关人员，以核实是否根据要求中规定的所有元素管理了要求 2 中确定的安全政策和操作程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>受影响人员确定满足要求 2 的活动的期望、控制和监督，并由其遵守。所有支持性活动都可重复一致适用，并符合管理层的意图。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="4">目的如果没有正式分配角色和责任，相关人员可能不知道他们的日常责任，关键活动可能不会发生。良好做法可以将角色和责任记录在政策和程序中，也可以保存在单独的文件中。作为沟通角色和责任的一部分，实体可以考虑让人员承认他们接受并理解所分配的角色和责任。示例记录角色和责任的一种方法是责任分配矩阵，包括谁负责、谁问责、谁咨询、谁知情（也称为RACI矩阵）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1.2 记录、分配和理解执行要求 2 中活动的角色和责任。</td><td style='text-align: center; word-wrap: break-word;'>2.1.2.a 检查文件，以核实是否记录和分配了执行要求 2 中活动的角色和责任的描述。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">2.1.2.b 询问负责执行要求 2 中的活动的人员，以核实是否按照文件规定分配了角色和责任，这些角色和责任是否被理解。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分配执行要求 2 中所有活动的日常责任。人员要对这些要求的成功和持续运行负责。</td></tr></table>

---

## 要求和测试程序


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.1 制定、实施和维护配置标准，以：·涵盖所有系统组件。·解决所有已知的安全漏洞。·与行业公认的系统加固标准或供应商加固建议保持一致。·按照要求6.3.1的规定，在发现新漏洞问题时进行更新。·当配置新系统并在系统组件连接到生产环境之前或之后立即核实是否到位时予以应用。</td><td rowspan="2">2.2.1.a 检查系统配置标准，以核实它们确定的流程是否包括本要求中规定的所有元素。</td><td rowspan="2">许多操作系统、数据库、网络设备、软件、应用程序、容器镜像以及实体使用的或实体环境内的其他设备都存在已知弱点。也有配置这些系统组件以修复安全漏洞的已知方法。修复安全漏洞可以减少攻击者可用的机会。通过制定标准，实体确保将一致和安全地配置他们的系统组件，并解决可能更难完全加固的设备的保护问题。良好做法掌握最新的行业指南将有助于实体保持安全配置。应用于系统的具体控制措施会有所不同，应该适合于系统的类型和功能。许多安全组织已建立系统加固指南和建议，建议如何纠正常见的已知弱点。更多信息关于配置标准的指导来源包括但不限于：互联网安全中心（CIS）、国际标准化组织（ISO）、美国国家标准与技术研究所（NIST）、云安全联盟以及产品供应商。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标以安全和一致的方式配置所有系统组件，并符合行业公认的加固标准或供应商建议。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td rowspan="2">2.2.2 管理供应商的默认帐户，具体如下：• 如果将使用供应商的默认帐户，则根据要求 8.3.6更改默认密码。• 如果不使用供应商的默认帐户，则将删除或禁用该帐户。</td><td style='text-align: center; word-wrap: break-word;'>2.2.2.a 检查系统配置标准，核实它们是否根据本要求规定的所有元素管理了供应商默认帐户。</td><td style='text-align: center; word-wrap: break-word;'>恶意者经常使用供应商的默认帐户名和密码来威胁操作系统、应用程序以及它们所处的系统。因为通常公布这些默认设置，并且为人所知，更改这些设置将使系统不易受到攻击。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.2.b 检查供应商文件，观察使用供应商默认帐户登录的系统管理员，核实是否根据本要求中规定的所有元素实施了帐户。</td><td style='text-align: center; word-wrap: break-word;'>良好做法应识别所有供应商的默认帐户，并了解其目的和用途。务必建立用于应用程序和系统帐户的控制措施，包括那些用于部署和维护云服务的应用程序和系统帐户，以便它们不使用默认密码，并且不能由未经授权的个人使用。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>2.2.2.c 检查配置文件并询问相关人员，核实所有不使用的供应商默认帐户是否已被删除或禁用。</td><td style='text-align: center; word-wrap: break-word;'>在不打算使用默认帐户的情况下，将默认密码改为符合 PCI DSS 要求 8.3.6 的唯一密码，取消任何默认帐户访问权限，然后禁用该帐户，这将防止恶意者重新启用该帐户并使用默认密码获得访问权限。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不能使用默认密码访问系统组件。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">这适用于所有供应商的默认帐户和密码，包括但不限于操作系统、提供安全服务的软件、应用程序和系统帐户、销售点（POS）终端、支付应用程序以及简单网络管理协议（SNMP）所使用的默认帐户和密码。这一要求也在系统组件没有安装在实体环境中的情况下适用，例如，作为 CDE 的一部分，通过云端订阅服务访问的软件和应用程序。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="2">目的包含其主要功能的一组服务、协议和守护程序的系统将有适当的安全配置文件，以允许该功能有效运行。例如，需要直接连接到互联网的系统会有一个特定的配置文件，如DNS服务器、网络服务器或电子商务服务器。相反，其他系统组件可能运行一个主要功能，包括一组不同的服务、协议和守护程序，执行一个实体不希望暴露于互联网的功能。这一要求旨在确保不同的功能不会影响其他服务的安全状况，从而导致它们以更高或更低的安全级别运行。良好做法理想情况下，每个功能应该置于不同的系统组件上。为此，可以在每个系统组件上只实施一个主要功能。另一个选择是在同一系统组件上隔离具有不同安全级别的主要功能，例如，将网络服务器（需要直接连接到互联网）与应用程序和数据库服务器隔离开来。（下一页继续）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.3 管理需要不同安全级别的主要功能，具体如下：• 一个系统组件上只存在一个主要功能，或• 存在于同一系统组件上具有不同安全级别的主要功能相互隔离，或• 保护存在于同一系统组件上具有不同安全级别的主要功能，以达到具有最高安全需求的功能所需的级别。定制方法目标具有较低安全需求的主要功能不能影响同一系统组件上具有较高安全需求的主要功能的安全。</td><td style='text-align: center; word-wrap: break-word;'>2.2.3.a 检查系统配置标准，以核实它们是否包括管理本要求中规定的需要不同安全级别的主要功能。2.2.3.b 检查系统配置，以核实是否根据本要求规定的方式之一管理了需要不同安全级别的主要功能。2.2.3.c 如果使用虚拟化技术，检查系统配置，以核实是否根据以下方式之一管理了需要不同安全级别的系统功能：• 具有不同安全需求的功能不并存于同一个系统组件上。• 存在于同一系统组件上具有不同安全需求的功能相互隔离。• 保护存在于同一系统组件上具有不同安全需求的功能，以达到具有最高安全需求的功能所需的级别。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>如果一个系统组件包含需要不同安全级别的主要功能，第三种选项是实施额外控制，以确保具有较高安全需求的主要功能的最终安全级别不会因为较低安全的主要功能的存在而降低。此外，应该隔离和/或保护安全级别较低的功能，以确保它们不能访问或影响另一个系统功能的资源，并且不会将安全弱点引入同一服务器上的其他功能。可以通过物理或逻辑控制将不同安全级别的功能隔离开来。例如，一个数据库系统不应该同时托管网络服务，除非使用虚拟化技术等控制措施，将这些功能隔离并包含在独立的子系统中。另一个例子是使用虚拟实例或按系统功能提供专用内存访问。如果使用虚拟化技术，应该确定和管理每个虚拟组件的安全级别。虚拟化环境的考虑因素实例包括：• 每个应用程序、容器或虚拟服务器实例的功能。• 如何存储和保护虚拟机（VM）或容器。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.4 只启用必要的服务、协议、守护程序和功能，删除或禁用所有不必要的功能。</td><td style='text-align: center; word-wrap: break-word;'>2.2.4.a 检查系统配置标准，核实是否识别和记录了必要的系统服务、协议和守护程序。</td><td style='text-align: center; word-wrap: break-word;'>不必要的服务和功能可以提供更多机会，让恶意者获得系统的访问权限。通过删除或禁用所有不必要的服务、协议、守护程序和功能，组织可以专注于保护所需的功能，并减少未知或不必要的功能被利用的风险。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">2.2.4.b 检查系统配置，核实以下情况：• 是否删除或禁用了所有不必要的功能。• 是否只启用配置标准中记录的必要功能。</td><td style='text-align: center; word-wrap: break-word;'>良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不能利用系统组件中存在的不必要功能来威胁系统组件。</td><td style='text-align: center; word-wrap: break-word;'>默认情况下可以启用许多协议，它们通常被恶意者用来威胁网络。禁用或删除所有不使用的服务、功能和协议，可以将潜在攻击面降到最低—例如，通过删除或禁用不使用的 FTP 或 Web 服务器。示例不必要的功能可能包括，但不限于脚本、驱动程序、功能、子系统、文件系统、接口（USB 和蓝牙）和不必要的网络服务器。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求2.2.5 如果存在任何非安全服务、协议或守护程序：• 记录商业理由。• 记录并实施额外安全功能，以减少使用非安全服务、协议或守护程序的风险。定制方法目标不能利用非安全服务、协议或守护程序来威胁系统组件。</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序2.2.5.a 如果存在任何非安全服务、协议或守护程序，检查系统配置标准并与询问相关人员，核实它们是否根据本要求中规定的所有元素进行管理和实施。2.2.5.b 如果存在任何非安全服务、协议或守护程序，检查配置设置，以核实是否实施了额外安全功能，以减少使用非安全服务、守护程序和协议的风险。险。</td><td style='text-align: center; word-wrap: break-word;'>目的确保使用适当的安全功能充分保护所有非安全服务、协议和守护程序，使恶意者更难利用网络中的常见威胁点。良好做法在部署新系统组件之前启用安全功能，将防止非安全配置引入到环境中。一些供应商解决方案可能会提供额外安全功能，以协助确保非安全流程的安全。更多信息关于被视为非安全服务、协议或守护程序的指导，请参考行业标准和指导（例如，发布自 NIST、ENISA 和 OWASP）。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td rowspan="2">2.2.6 配置系统安全参数以防止误用。</td><td style='text-align: center; word-wrap: break-word;'>2.2.6.a 检查系统配置标准，核实它们是否包括防止误用的配置系统安全参数。</td><td style='text-align: center; word-wrap: break-word;'>正确配置系统组件中提供的安全参数，利用系统组件的能力来攻克恶意攻击。良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.6.b 询问系统管理员和/或安全经理，核实他们是否对系统组件的常见安全参数设置有所了解。</td><td style='text-align: center; word-wrap: break-word;'>系统配置标准和相关流程应专门处理对所使用的每一类系统具有已知安全影响的安全设置和参数。为了安全配置系统，负责配置和/或管理系统的人员应该了解适用于系统的具体安全参数和设置。考虑因素还应该包括用于访问云门户的参数的安全设置。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">2.2.6.c 检查系统配置，核实是否适当设置了常见安全参数并符合系统配置标准。</td><td style='text-align: center; word-wrap: break-word;'>更多信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不正确的安全参数配置不会对系统组件产生威胁。</td><td style='text-align: center; word-wrap: break-word;'>参考供应商文件和要求 2.2.1 中提到的行业参考资料，了解每种类型系统的适用安全参数。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td rowspan="4">加密法对所有非控制台的管理访问进</td><td style='text-align: center; word-wrap: break-word;'>2.2.7.a 检查系统配置标准，核实它们是否包括使用强效加密法来加密所有非控制台管理访问权限。</td><td style='text-align: center; word-wrap: break-word;'>如果非控制台（包括远程）管理不使用加密通信，窃听者可能会发现管理授权因素（例如 ID 和密码）。恶意者可以利用这些信息来访问网络，成为管理员，并窃取数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.7.b 观察登录到系统组件的管理员并检查系统配置，核实是否根据本要求管理了非控制台管理访问。</td><td style='text-align: center; word-wrap: break-word;'>良好做法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.7.c 检查系统组件和验证服务的设置，以核实非安全远程登录服务是否可用于非控制台管理访问。</td><td style='text-align: center; word-wrap: break-word;'>无论使用哪种安全协议，都应配置为只使用安全版本和配置，以防止使用非安全连接—例如，只使用可信证书，只支持强效加密法，不支持回退到较弱的非安全协议或方法。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.2.7.d 检查供应商的文件并询问访谈人员，以核实是否根据行业最佳实践和/或供应商的建议实施了所使用技术的强效加密法。</td><td style='text-align: center; word-wrap: break-word;'>示例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>目标</td><td style='text-align: center; word-wrap: break-word;'>2.2.7.e 调查网络传输中读取或截获明文管理授权因</td><td style='text-align: center; word-wrap: break-word;'>明文协议（例如 HTTP、telnet 等）不对流量或登录细节进行加密，使窃听者轻松截获这些信息。提供系统的替代访问权限的技术可以促进非控制台访问，包括但不限于带外（OOB）、熄灯管理（LOM）、智能平台管理接口（IPMI）和具有远程功能的键盘、视频、鼠标（KVM）开关。必须使用强效加密法来确保这些和其他非控制台访问技术和方法的安全。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>性说明</td><td colspan="2">更多信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>包括通过基于浏览器的接口和应用程序编程接口（API）的管理访问权限。</td><td colspan="2">请参考行业标准和最佳实践，例如 NIST SP 800-52 和 SP 800-57。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">2.3 安全配置和管理无线环境。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的如果无线网络的实施没有足够的安全配置（包括改变默认设置），无线嗅探器可以窃听流量，轻松捕获数据和密码，并轻易进入和攻击网络。良好做法应构造无线密码，使其能够抵御离线蛮力攻击。</td></tr><tr><td rowspan="2">2.3.1 对于连接到 CDE 或传输帐户数据的无线环境，在安装时改变所有无线供应商的默认值或确认其安全性，包括但不限于：• 默认无线密钥。• 无线接入点上的密码。• SNMP 默认值。• 任何其他与安全有关的无线供应商默认值。</td><td style='text-align: center; word-wrap: break-word;'>2.3.1.a 检查政策和程序并询问负责人员，核实是否制定了相应程序，根据本要求的所有元素，在安装时改变所有无线供应商的默认值或确认其安全性。</td><td rowspan="6">目的如果无线网络的实施没有足够的安全配置（包括改变默认设置），无线嗅探器可以窃听流量，轻松捕获数据和密码，并轻易进入和攻击网络。良好做法应构造无线密码，使其能够抵御离线蛮力攻击。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.3.1.b 检查供应商的文件并观察登录到无线设备的系统管理员，以核实：• 不使用 SNMP 的默认值。• 不使用无线接入点上的默认密码/口令。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>2.3.1.c 检查供应商文件和无线配置设置，以核实是否改变了其他与安全有关的无线供应商默认值（如果适用）。</td></tr><tr><td colspan="2">不能使用供应商默认密码或默认配置访问无线网络。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这包括但不限于默认无线密钥、无线接入点的密码、SNMP 默认值以及任何其他与安全相关的无线供应商默认值。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.3.2 对于连接到 CDE 或传输帐户数据的无线环境，更换无线密钥，具体如下：• 每当了解密钥的人员离开公司或离开需要了解密钥的角色时。• 每当怀疑或知道密钥被威胁时。</td><td style='text-align: center; word-wrap: break-word;'>2.3.2 询问负责人员并检查密钥管理文件，核实是否根据本要求中规定的所有元素更换了无线密钥。</td><td rowspan="2">每当知道密钥的人离开组织或转到一个不再需要知道密钥的角色时，更换无线密钥，这有助于将密钥的信息仅限于那些有业务需要的人。另外，在怀疑或知道某个密钥被威胁的情况下更换无线密钥，可以使无线网络更不易遭到威胁。良好做法</td></tr><tr><td rowspan="2">定制方法目标</td><td rowspan="2">了解无线密钥不能使未经授权的人员访问无线网络。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这一目标可以通过多种方式实现，包括定期更换密钥、通过确定的“joiners-movers-leavers”（JML）流程更换密钥、实施额外技术控制，以及不使用固定的预共享密钥。此外，任何已知或怀疑被威胁的密钥应根据要求12.10.1 中实体的事件响应计划进行管理。</td></tr></table>

---

## 保护帐户数据

<div style="text-align: center;">要求 3： 保护所存储帐户数据</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>章节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.1</td><td style='text-align: center; word-wrap: break-word;'>确定和理解保护所存储帐户数据的流程和机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>帐户数据的存储保持在最低限度。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3</td><td style='text-align: center; word-wrap: break-word;'>敏感验证数据（SAD）在授权后不予以存储。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.4</td><td style='text-align: center; word-wrap: break-word;'>限制完整 PAN 显示屏的访问权限和复制持卡人数据的能力。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.5</td><td style='text-align: center; word-wrap: break-word;'>确保主帐户号码（PAN）安全，无论它们存放在哪里。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.6</td><td style='text-align: center; word-wrap: break-word;'>确保用于保护存储帐户数据的密钥安全。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.7</td><td style='text-align: center; word-wrap: break-word;'>当加密法用于保护存储帐户数据时，确定并实施涵盖密钥生命周期所有方面的密钥管理流程和程序。</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>概述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>加密、截词、掩盖和散列等保护方法是帐户数据保护的关键组成部分。如果一个入侵者规避了其他安全控制并获得了加密帐户数据的访问权限，那么没有适当的加密密钥，这些数据是不可读的，对该入侵者来说是不可用的。其他保护存储数据的有效方法也应被视为潜在的风险缓解机会。例如，最大限度地减少风险的方法包括：除非有必要，否则不存储帐户数据；如果不需要完整的 PAN，则截断持卡人数据；以及不使用最终用户的信息传递技术（例如电子邮件和即时信息传递）发送未受保护的 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如果帐户数据存在于非持久性存储器中（例如，RAM，易失性存储器），则无需对帐户数据进行加密。然而，必须制定适当的控制措施，以确保内存保持非持久性状态。达到业务目的（例如，相关交易）后，数据应从易失性存储器中删除。在数据存储成为持久性的情况下，所有适用的 PCI DSS 要求将适用，包括加密存储数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>要求 3 适用于保护存储的帐户数据，除非在个别要求中特别指出。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>关于“强效加密法”和其他 PCI DSS 术语的定义，请参阅附录 G。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">3.1 确定和理解保护所存储帐户数据的流程和机制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="2">目的要求 3.1.1 涉及有效管理和维护整个要求 3 规定的各种政策和程序。虽然定义要求 3 中规定的具体政策或程序很重要，但同样重要的是确保适当地记录、维护和传播这些政策或程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.1.1 要求 3 中确定的所有安全政策和操作程序都：• 有文件记录。• 保持时效性。• 在使用中。• 为所有受影响的各方所了解。</td><td rowspan="2">3.1.1 检查文件并询问相关人员，以核实是否根据本要求中规定的所有元素管理了要求 3 中确定的安全政策和操作程序。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标受影响人员确定满足要求 3 的活动的期望、控制和监督，并由其遵守。所有支持性活动都可重复一致适用，并符合管理层的意图。</td><td style='text-align: center; word-wrap: break-word;'>良好做法视情况更新政策和程序，以应对流程、技术和业务目标的变化，这一点很重要。出于这个原因，考虑在变化发生后尽快更新这些文件，而不仅仅是在定期周期内。定义安全政策定义了实体的安全目标和原则。操作程序描述了如何执行活动，并确定了为以一致的方式并根据政策目标实现预期结果而遵循的控制、方法和流程。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>目的如果没有正式分配角色和责任，相关人员可能不知道他们的日常责任，关键活动可能不会发生。良好做法可以将角色和责任记录在政策和程序中，也可以保存在单独的文件中。作为沟通角色和责任的一部分，实体可以考虑让人员承认他们接受并理解所分配的角色和责任。示例记录角色和责任的一种方法是责任分配矩阵，包括谁负责、谁问责、谁咨询、谁知情（也称为RACI矩阵）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.1.2 记录、分配和理解执行要求 3 中活动的角色和责任。</td><td style='text-align: center; word-wrap: break-word;'>3.1.2.a 检查文件，以核实是否记录和分配了执行要求 3 中活动的角色和责任的描述。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2">3.1.2.b 询问负责执行要求 3 中的活动的人员，以核实是否按照文件规定分配了角色和责任，这些角色和责任是否被理解。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分配执行要求 3 中所有活动的日常责任。人员要对这些要求的成功和持续运行负责。</td></tr></table>

---

## 要求和测试程序


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.2.1 通过实施至少包括以下内容的数据保留和处置政策、程序和流程，帐户数据存储将保持在最低水平：• 覆盖所有储存帐户数据的位置。• 覆盖授权完成前存储的任何敏感认证数据（SAD）。本项内容在其生效日期前是最佳实践；详情请参考下面的适用性说明。• 限制数据存储量和保留时间，以至于其在法律或监管和/或业务要求所需的范围内。• 存储帐户数据的具体保留要求，确定了保留期限，并包括书面业务理由。• 根据保留政策，在不再需要时，安全删除或使帐户数据无法恢复的程序。• 至少每三个月审核一次超过规定保留期的存储帐户数据是否已被安全删除或无法恢复。</td><td style='text-align: center; word-wrap: break-word;'>3.2.1.a 检查数据保留和处置的政策、程序和流程并询问相关人员，核实是否制定了相应流程，以包括本要求中规定的所有元素。</td><td rowspan="3">正式的数据保留政策确定了需要保留的数据，保留的时长，以及这些数据的存放位置，以便在不再需要时，可以立即安全地销毁或删除。授权后可能被保存的唯一帐户数据是主帐户或PAN（变得不可读）、到期日、持卡人姓名和业务码。在完成授权过程之前，SAD数据的存储也被列入数据保留和处置政策中，以将这种敏感数据的存储保持在最低限度，并且仅在规定的时间内予以保留。良好做法在确定存储帐户数据的位置时，必须考虑所有能接触到数据的流程和人员，因为数据可能已被转移并存储在与最初确定不同的位置。经常被忽视的存储位置包括备份和存档系统、可移动数据存储设备、纸质媒体和录音。为了确定适当的保留要求，实体首先需要了解自己的业务需求，以及适用于其行业或被保留数据类型的任何法律或监管义务。实施一个自动程序，确保在规定的保留期限内自动和安全地删除数据，有助于确保帐户数据的保留不会超出业务、法律或监管目的所必需的范围。（下一页继续）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td rowspan="2"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>帐户数据只在必要时保留，并且保留最少时间，当不再需要时，安全地删除或使帐户数据无法恢复。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td rowspan="2">当数据超过保留期时，消除数据的方法包括安全删除，以完全删除数据或使其无法恢复和无法重建。识别并安全地消除已经超过其指定保留期的存储数据，防止不必要地保留不再需要的数据。这个过程可以通过自动、手动或结合两者完成。大多数操作系统中的删除功能并不是“安全删除”，因为它允许恢复已被删除的数据，因此，必须使用专门的安全删除功能或应用程序来使数据无法恢复。请记住，如果你不需要它，就不要储存它！示例可以运行自动程序化程序来定位和删除数据，也可以对数据存储区进行人工审核。无论使用哪种方法，监控该过程是一个好主意，以确保其成功完成，并记录结果和认证其是否完整。实施安全删除方法可以确保在不再需要时无法检索到数据。更多信息见 NIST SP 800-88 Rev.1，媒体消毒指南。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>当帐户数据由 TPSP 存储时（例如，在云环境中），实体负责与他们的服务提供商合作，了解 TPSP 如何满足实体的这一要求。考虑因素包括确保安全删除数据元素的所有地理实例。上述内容（在完成授权之前覆盖的存储 SAD）在2025 年 3 月 31 日之前是最佳实践，在此日期后将作为要求 3.2.1 的一部分并且必须在 PCI DSS 评估中予以充分考虑。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">3.3 敏感验证数据（SAD）在授权后不予以存储。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的SAD 对于恶意者来说是非常有价值的，因为它可以让他们生成伪造的支付卡并制造欺诈性交易。因此，禁止在完成授权过程后储存 SAD。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3.1 授权后不保留 SAD，即使已加密。所有收到的敏感验证数据在授权过程完成后将无法恢复。</td><td style='text-align: center; word-wrap: break-word;'>3.3.1.a 如果收到了 SAD，检查书面政策、程序和系统配置，核实数据在授权后是否不予保留。</td><td rowspan="3">定义当商户收到一个交易响应（例如，批准或拒绝）时，授权过程即完成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td><td style='text-align: center; word-wrap: break-word;'>3.3.1.b 如果收到了 SAD，检查书面程序并观察安全数据删除流程，核实数据在完成授权过程后是否无法恢复。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这项要求不适用于定制方法。</td><td style='text-align: center; word-wrap: break-word;'>适用性说明本要求不适用于支持发卡服务的发卡服务的公司（需要 SAD 来满足合理发卡业务的需要），并且有业务理由来存储敏感验证数据。有关针对发卡机构的额外要求，请参考要求 3.3.3。敏感验证数据包括要求 3.3.1.1 至 3.3.1.3 中引用的数据。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定。</td><td rowspan="6">道的全部内容（如果存在的话，来，千背面的磁条，芯片上包含的同等数据，或其他地方），获得该数据的恶意者可以使用它来复制支付卡并完成欺诈性交易。定义全磁道数据也称为全磁道、磁道、磁道1、磁道2和磁条数据。每个磁道都包含一些数据元素，本要求只规定了那些在授权后可能被保留的数据元素。示例为确保在授权过程结束后不保留任何磁道的全部内容，需要审核的数据来源包括但不限于：· 输入的交易数据。· 所有日志（例如，交易、历史、调试、错误）。· 历史文件· 跟踪文件· 数据库模式。· 数据库的内容，以及内部和云数据存储。· 任何现有的内存/崩溃转储文件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3.1.1 在完成授权过程后，不保留任何磁道的全部内容。</td><td rowspan="5">3.3.1.1 检查数据源，核实元。留任何磁道的全部内容。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这项要求不适用于定制方法。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在正常业务过程中，可能需要保留磁道上的以下数据元素：· 持卡人姓名。· 主帐户号码（PAN）。· 到期日。· 业务码。为了将风险降到最低，只在业务需要时安全地存储这些数据元素。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td rowspan="6">规定的方法测试程序</td><td rowspan="6">目的如果卡验证代码数据被盗，恶意者可以执行欺诈性的互联网和邮件订单/电话订单（MO/TO）交易。不存储这些数据可以减少其被威胁的可能性。示例如果在完成授权之前将支付卡验证代码存储在纸质媒体上，那么在完成授权之后，应采用擦除或覆盖验证代码的方法来防止其被读取。使代码不可读的方法包括：用剪刀将代码剪掉，并在代码上贴上适当的不透明的、不可去除的标记。为确保在授权过程结束后不保留支付卡验证代码，需要审核的数据来源包括但不限于：• 输入的交易数据。• 所有日志（例如，交易、历史、调试、错误）。• 历史文件• 跟踪文件• 数据库模式。• 数据库的内容，以及内部和云数据存储。• 任何现有的内存/崩溃转储文件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3.1.2 在完成授权过程后，不保留支付卡验证代码。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这项要求不适用于定制方法。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支付卡验证代码是印在支付卡正面或背面的三位或四位数字，用于验证虚拟信用卡交易。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="6">目的PIN 和 PIN 数据块应该只为持卡人或发卡实体所知。如果这些数据被盗，恶意者可以执行基于 PIN 码的欺诈性交易（例如，店内购物和自动取款机取款）。不存储这些数据可以减少其被威胁的可能性。示例为确保在完成授权过程后不保留 PIN 和 PIN 数据块，需要审核的数据来源包括，但不限于：• 输入的交易数据。• 所有日志（例如，交易、历史、调试、错误）。• 历史文件• 跟踪文件• 数据库模式。• 数据库的内容，以及内部和云数据存储。• 任何现有的内存/崩溃转储文件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3.1.3 在完成授权过程后，不保留个人识别码（PIN）和 PIN 数据块。</td><td rowspan="5">3.3.1.3 检查数据源，核实完成授权过程后是否不保留 PIN 和 PIN 数据块。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这项要求不适用于定制方法。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在交易过程的自然过程中，将对 PIN 数据块进行加密，但即使实体再次对 PIN 数据块进行加密，仍然不允许在授权过程完成后予以存储。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.3.2 在完成授权之前，使用强效加密法来加密以电子方式存储的 SAD。</td><td rowspan="5">3.3.2 检查数据存储、系统配置和/或供应商文件，以核实在完成授权之前是否使用了强效加密法来加密以电子方式存储的 SAD。</td><td rowspan="5">恶意者可以利用 SAD 来增加成功生成伪造的支付卡和创造欺诈性交易的概率。良好做法实体应该考虑使用与加密 PAN 不同的密钥来加密 SAD。请注意，这并不意味着需要单独加密存在于 SAD 中的 PAN（作为磁道数据的一部分）。定义一旦收到授权请求响应（即批准或拒绝）授权过程即告完成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>这项要求不适用于定制方法。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>管理合规计划（例如，支付品牌和收单机构）的组织将决定是否允许在授权前存储 SAD。要了解任何额外标准，请联系相关组织。这项要求适用于所有 SAD 的存储，即使环境中不存在 PAN。如果在完成授权之前存储 SAD，则参考要求 3.2.1 的额外要求。本要求不适用于发卡机构和支持发卡服务的公司，因为这些公司具备合理的发卡业务理由来存储 SAD。）有关针对发卡机构的要求，请参考要求 3.3.3。本要求并不取代要求 PIN 数据块的管理方式，也不意味着经过适当加密的 PIN 数据块需要再次加密。本要求在 2025 年 3 月 31 日之前是最佳实践，在此日期后规定并且必须在 PCI DSS 评估中予以充分考虑。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="7">目的恶意者可以利用 SAD 来增加成功生成伪造的支付卡和创造欺诈性交易的概率。良好做法实体应该考虑使用与加密 PAN 不同的密钥来加密 SAD。请注意，这并不意味着需要单独加密存在于 SAD 中的 PAN（作为磁道数据的一部分）。定义合理的发卡业务需求是指需要该数据来促进发卡业务流程。更多信息参考 ISO/DIS 9564-5《金融服务—个人识别码（PIN）管理和安全—第 5 部分。使用高级加密标准生成、更改和验证 PIN 和支付卡安全数据的方法。</td></tr><tr><td rowspan="2">3.3.3 针对支持发卡服务和存储敏感验证数据的发卡机构和公司的额外要求：任何敏感验证数据的存储：• 只限于合理发卡业务需要的数据，并且受到保护。• 使用强效加密法进行加密。本项内容在其生效日期前是最佳实践；详情请参考下面的适用性说明。</td><td style='text-align: center; word-wrap: break-word;'>3.3.3.a 针对支持发卡服务和存储敏感验证数据的发卡机构和公司的额外测试程序：检查书面政策并询问相关人员，核实是否有书面业务理由来存储敏感验证数据。</td></tr><tr><td rowspan="5">3.3.3.b 针对支持发卡服务和存储敏感验证数据的发卡机构和公司的额外测试程序：检查数据存储和系统配置，核实是否安全存储了敏感验证数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>仅在支持发卡职能所需的情况下保留敏感验证数据，并受到保护免于未经授权的访问。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本要求仅适用于发卡机构和支持发卡服务并存储敏感验证数据的公司。发行支付卡的实体或执行或支持发卡服务的实体通常会创建和控制敏感验证数据，作为发卡职能的一部分。执行、促进或支持发卡服务的公司允许存储敏感验证数据，但前提是他们具备存储这些数据的合理业务需求。（下一页继续）</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PCI DSS 要求适用于所有存储、处理或传输帐户数据的实体，包括发卡机构。发卡机构和发卡处理机构的唯一例外是，如果有合理理由，则可以保留敏感验证数据。必须安全地存储任何此类数据，并符合所有PCI DSS 和特定支付品牌要求。上述内容（使用强效加密法来加密存储的 SAD）在2025 年 3 月 31 日之前是最佳实践，在此日期后将作为要求 3.3.3 的一部分并且必须在 PCI DSS 评估中予以充分考虑。</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">3.4 限制显示完整 PAN 的访问权限和复制 PAN 的能力。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td rowspan="3">目的在计算机屏幕、支付卡收据、纸质报告等物品上显示完整 PAN，可能会导致未经授权的人员获得并欺诈性使用这些数据。确保仅对具有合理业务需求的人显示完整的 PAN，可以将未经授权的人员获取 PAN 数据的风险降到最低。良好做法根据确定的角色应用访问控制是限制只有那些具有明确的业务需求的个人才能查看完整的 PAN 的一种方法。掩盖方法应始终只显示执行特定业务功能所需的数字数量。例如，如果只需要最后四位数字来执行一项业务功能，PAN 应该被掩盖，只显示最后四位数字。再举一个例子，如果一个功能需要查看银行识别码(BIN)以确定路线，那么只需为该功能取消掩盖 BIN 数字。定义截词不是截词的同义词，这些术语不能互换使用。掩盖是指在显示或打印过程中隐藏某些数字，即使整个 PAN 都被储存在系统中。这与截词不同，在截词中，将移除被截断的数字，无法在系统内检索。被掩盖的 PAN 可以被“解除掩盖”，但如果不从另一个来源重新创建 PAN，就不会“解除截断”。（下一页继续）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.4.1 PAN 在显示时被掩盖（BIN 和最后四位数字是显示的最大数字），这样只有具有合理业务需求的人员可以看到比 BIN 和 PAN 的最后四位数字更多的内容。定制方法目标PAN 显示被限制在满足明确业务需求所需的最小数字。</td><td style='text-align: center; word-wrap: break-word;'>3.4.1.a 检查书面政策和程序，以掩盖 PAN 的显示，核实：• 记录需要访问比 BIN 和 PAN 的最后四位数字更多的内容（包括完整的 PAN）的角色列表，以及每个角色拥有这种访问权限的合理业务需求。• PAN 在显示时被掩盖，只有具有合理业务需求的人员才能看到比 BIN 和 PAN 的最后四位数字更多的内容。• 所有未经明确授权查看完整 PAN 的角色必须只能看到被掩盖的 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明本要求并不取代显示持卡人数据的现有的更严格要求—例如，销售点（POS）收据的法律或支付品牌要求。本要求自在 PAN 在屏幕、纸质收据、打印输出等显示时提供保护，并且不应与存储、处理或传输时保护 PAN 的要求 3.5.1 相混淆。</td><td style='text-align: center; word-wrap: break-word;'>3.4.1.b 检查系统配置，核实完整的 PAN 是否只显示给有书面业务需求的角色，而对于所有其他请求 PAN 都被掩盖。</td></tr></table>

支付卡行业数据安全标准：要求及测试程序，4.0版

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.4.1.c 检查显示的 PAN（例如，在屏幕上，在纸质收据上），核实 PAN 在显示时是否被掩盖，并且只有具备合理业务需求的人员才能够看到比 BIN 和/或 PAN 的最后四位数字更多的信息。</td><td style='text-align: center; word-wrap: break-word;'>更多信息关于掩盖和截断的更多信息，请参阅 PCI SSC 关于这些主题的常见问题。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.4.2 当使用远程访问技术时，技术控制可以防止所有人员复制和/或重新安置 PAN，除非是那些有书面、获明确授权和具备合理的明确业务需求。</td><td rowspan="2">3.4.2.a 检查书面政策和程序以及技术控制书面证据，防止在使用远程访问技术时将 PAN 复制和/或重新安置到本地硬盘或可移动电子媒体上，核实以下情况：· 技术控制防止所有未经明确授权的人员复制和/或重新安置 PAN。· 维护一份有权复制和/或重新安置 PAN 的人员名单，以及有书面、获明确授权和具备合理的明确业务需求。</td><td rowspan="5">重新安置 PAN 到未经授权的存储设备上，是获取和使用这种数据的常见方式。确保只有经明确授权和具备合理商业理由的人员才能复制或重新安置 PAN 的相应方法，将未经授权的人员获得 PAN 的风险降到最低。良好做法PAN 的复制和重新安置应仅在允许和授权给该个人的存储设备上进行。定义虚拟桌面是远程访问技术的一个例子。存储设备包括但不限于本地硬盘、虚拟驱动器、可移动电子媒体、网络驱动器和云存储。更多信息所使用的远程访问技术的供应商文件将提供有关实施这项要求所需的系统设置的信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未经授权的人员无法使用远程访问技术复制或重新安置 PAN。</td><td style='text-align: center; word-wrap: break-word;'>3.4.2.b 检查远程访问技术的配置，核实防止所有人员复制和/或重新安置 PAN 的技术控制，除非经明确授权。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'>3.4.2.c 观察流程并询问相关人员，核实在使用远程访问技术时，仅那些有书面、获明确授权和具备合理的明确业务需求的人员才有权限复制和/或重新安置 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>存储或重新安置 PAN 到本地硬盘、可移动电子媒体和其他存储设备上，使这些设备进入 PCI DSS 的范围。</td><td style='text-align: center; word-wrap: break-word;'>3.4.2.c 观察流程并询问相关人员，核实在使用远程访问技术时，仅那些有书面、获明确授权和具备合理的明确业务需求的人员才有权限复制和/或重新安置 PAN。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td colspan="3">3.5 确保主帐户号码（PAN）安全，无论它们存放在哪里。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td rowspan="4">规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的如果未经授权的个人利用实体的主要访问控制的漏洞或错误配置而获得存储数据的访问权限，那么删除明文存储 PAN 是一种旨在保护数据的深度防御控制。二级独立控制系统（例如，管理加密法和解密密钥的访问和使用）可防止因一级访问控制系统的失效而导致违反存储 PAN 的保密条款。如果散列用于删除存储的明文 PAN，通过关联一个给定 PAN 的散列和截断版本，那么恶意者就可以轻松地得出原始的 PAN 值。防止这种数据关联的控制措施将有助于确保原始 PAN 不可读。更多信息有关截词格式和一般截词的信息，请参见 PCI SSC 关于该主题的常见问题。有关索引令牌的信息来源包括：· PCI SSC 的令牌化产品安全指南（https://www.pcisecuritystandards.org/documents/Tokenization_Product_Security_Guidelines.pdf）· ANSI X9.119-2-2017：零售金融服务 - 保护敏感支付卡数据的要求 - 第 2 部分：实施授权后令牌化系统</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.5.1 通过使用以下任何一种方法，使 PAN 在任何存储位置都不可读：· 基于整个 PAN 的强效加密法的单向散列。· 截词（不能使用散列法来替换 PAN 的截断部分）。- 如果相同 PAN 的散列和截断版本，或者相同 PAN 的不同截断格式，存在于一个环境中，则要有额外控制，使不同的版本无法相互关联以重建原始 PAN。· 索引令牌。· 强效加密法以及相关密钥管理流程和程序。</td><td rowspan="3">3.5.1.a 检查有关用于使 PAN 不可读的系统的文件，包括供应商、系统/程序的类型和加密算法（如果适用），核实是否使用了本要求中规定的任何方法使 PAN 不可读。3.5.1.b 检查数据存储库和检查日志，包括支付应用程序的日志，核实是否使用了本要求中规定的任何方法使 PAN 不可读。3.5.1.c 如果环境中存在同一 PAN 的散列和截断版本，检查所实施的控制，核实散列和截断版本是否无法相互关联以重建原始 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标不能从存储媒介中读取明文 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明如果恶意者能够访问某个 PAN 的截断和散列版本，那么重建原始 PAN 数据是一个相对微不足道的工作。（下一页继续）</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>此要求适用于存储在主存储体（数据库，或平面文件，例如文本文件电子表格）以及非主存储体（备份、检查日志、异常日志、或故障排除日志）的PAN，它们都必须受到保护。此要求并不排除在加密和解密 PAN 时使用包含明文 PAN 的临时文件。</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">要求和测试程序</td><td style='text-align: center; word-wrap: break-word;'>指南</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.5.1.1 用于使 PAN 不可读的散列（根据要求 3.5.1 的第一条）是整个 PAN 的加密散列，以及符合要求 3.6 和 3.7 的相关密钥管理流程和程序。</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.1.a 检查有关用于使 PAN 不可读的散列方法的文件，包括供应商、系统/程序类型和加密算法（如适用），核实该散列方法是否导致整个 PAN 的加密散列，以及相关密钥管理流程和程序。</td><td rowspan="3">如果未经授权的个人利用实体的主要访问控制的漏洞或错误配置而获得存储数据的访问权限，那么删除明文存储 PAN 是一种旨在保护数据的深度防御控制。二级独立控制系统（例如，管理加密法和解密密钥的访问和使用）可防止因一级访问控制系统的失效而导致违反存储 PAN 的保密条款。良好做法结合随机生成的秘密密钥以提供抗蜜力攻击和秘密验证完整性的散列函数。更多信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.1.b 检查有关与加密散列相关的密钥管理程序和流程的文件，核实是否根据要求 3.6 和 3.7 管理了密钥。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>此要求适用于存储在主存储体（数据库，或平面文件，例如文本文件电子表格）以及非主存储体（备份、检查日志、异常日志、或故障排除日志）的 PAN，它们都必须受到保护。</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.1.c 检查数据存储库，核实 PAN 是否不可读。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>此要求并不排除在加密和解密 PAN 时使用包含明文 PAN 的临时文件。</td><td rowspan="2">3.5.1.1.d 检查检查日志，包括支付应用程序的日志，核实 PAN 是否不可读。</td><td rowspan="2">适当的加密散列算法包括但不限于：HMAC、CMAC 和 GMAC，其有效加密强度至少为 128 位（NIST SP 800-131Ar2）。关于 HMAC、CMAC 和 GMAC 的更多信息，请参考以下内容：NIST SP 800-107r1、NIST SP 800-38B 和 NIST SP 800-38D）。请参见 NIST SP 800-107（修订版 1）：对使用授权散列算法的应用程序的建议§5.3。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本要求在 2025 年 3 月 31 日之前被视为最佳实践，在此日期后规定并且必须在 PCI DSS 评估中予以充分考虑。</td></tr></table>

---

<div style="text-align: center;">要求和测试程序</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>规定的方法要求</td><td style='text-align: center; word-wrap: break-word;'>规定的方法测试程序</td><td style='text-align: center; word-wrap: break-word;'>目的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3.5.1.2 如果磁盘级或分区级加密（而不是文件级、列级或字段级的数据库加密）被用来使 PAN 不可读，实施方法如下：• 在可移动电子媒介上或• 如果用于非可移动电子媒介，也将通过另一种符合要求 3.5.1 的机制使 PAN 不可读。</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.2.a 检查加密流程，以核实如果磁盘级或分区级加密被用来使 PAN 不可读，它是否只按以下方式实施：• 在可移动电子媒介上，或• 如果用于非可移动电子媒介，检查使用的加密过程，核实是否也通过另一种符合要求 3.5.1 的方法使 PAN 不可读。</td><td rowspan="3">磁盘级和分区级加密通常使用相同的密钥对整个磁盘或分区进行加密，所有数据在系统运行时或授权用户要求时自动解密。由于这个原因，磁盘级加密不适合用来保护计算机、笔记本电脑、服务器、存储阵列或任何其他在用户验证时提供透明解密的系统上的存储 PAN。更多信息如果有的话，以下供应商的加固和行业最佳实践指南可以帮助保护这些设备上的 PAN。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定制方法目标这项要求不适用于定制方法。</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.2.b 检查配置和/或供应商文件，观察加密流程，核实是否根据供应商文件配置了系统，其结果是磁盘或分区不可读。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>适用性说明作为数据中心架构一部分的媒（例如，热插拔驱动器、批量磁带备份）被视为要求 3.5.1 所适用的非可移动电子媒介。磁盘或分区加密实施还必须满足所有其他 PCI DSS 加密和密钥管理要求。本要求在 2025 年 3 月 31 日之前是最佳实践，在此日期后规定并且必须在 PCI DSS 评估中予以充分考虑。</td><td style='text-align: center; word-wrap: break-word;'>3.5.1.2.b 检查配置和/或供应商文件，观察加密流程，核实是否根据供应商文件配置了系统，其结果是磁盘或分区不可读。</td></tr></table>