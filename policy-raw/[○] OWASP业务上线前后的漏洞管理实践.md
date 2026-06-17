---
title: "OWASP业务上线前后的漏洞管理实践"
source: "政策、报告、文件/OWASP业务上线前后的漏洞管理实践.pdf"
type: "pdf"
processed: "2026-04-23T07:10:41.419083"
---

## 业务上线前后的漏洞管理实践

李俊 魔方安全

---

## 目录

## 1 -业界实践

2-业务上线前后面临的挑战

3-漏洞管理思路和实践

4-实践案例介绍

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_63_226_185.jpg" alt="Image" width="5%" /></div>


## 业界实践—互联网公司业界实践

## ➢小米

https://sec.xiaomi.com/article?id=5（安全扫描自动化检测平台建设）

➢ 携程

http://mp.weixin.qq.com/s/OtqJ-14vEPEcLmf4Ctk7vQ（携程安全自动化测试之路）

## ➢ 腾讯

https://security.tencent.com/index.php/blog/msg/100 （自研之路：腾讯漏洞扫描系统的十年历程）

原始社会

01

拿来主义

02

啊D、穿山甲、JSKY

工业革命

03

## 国外的商业扫描器

## 黑客自行开发

AWVS, WenInspect, AppScan

## 自研扫描器

BAT的自研扫描器之路分布式扫描、安全工单

## 未来世界

04

## 云安全扫描平台

安全即服务

基于插件的扫描平台

000

100

011

000

1010

1000

000

00

1000

1000

0011

001

1010

1000

0011

0010

1010

1010

---

## 某大型券商漏洞管理实践

<div style="text-align: center;"><img src="imgs/img_in_image_box_293_252_1618_876.jpg" alt="Image" width="69%" /></div>


---

## 某大型券商漏洞管理实践

## 漏洞运营过程中的痛点

<div style="text-align: center;"><img src="imgs/img_in_image_box_36_382_982_878.jpg" alt="Image" width="49%" /></div>


## 我们的实践

科学、高效的漏洞修复策略

<div style="text-align: center;"><img src="imgs/img_in_image_box_1455_447_1872_878.jpg" alt="Image" width="21%" /></div>


持续、全面和高频的自动化漏洞检测

可视化的度量和跟踪

---

## 某大型券商漏洞管理实践


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>漏洞检测手段</td><td style='text-align: center; word-wrap: break-word;'>检测方式</td><td style='text-align: center; word-wrap: break-word;'>检测频率</td><td style='text-align: center; word-wrap: break-word;'>扫描目标</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>互联网侧主机层漏洞扫描</td><td style='text-align: center; word-wrap: break-word;'>网络扫描</td><td style='text-align: center; word-wrap: break-word;'>每周三次</td><td style='text-align: center; word-wrap: break-word;'>全网互联网IP地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>互联网web应用层漏洞扫描</td><td style='text-align: center; word-wrap: break-word;'>网络扫描</td><td style='text-align: center; word-wrap: break-word;'>每周一次</td><td style='text-align: center; word-wrap: break-word;'>全网互联网web应用URL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内网侧主机层漏洞扫描</td><td style='text-align: center; word-wrap: break-word;'>网络扫描+Agent扫描</td><td style='text-align: center; word-wrap: break-word;'>每周一次</td><td style='text-align: center; word-wrap: break-word;'>核心网所有IP地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外部渗透测试</td><td style='text-align: center; word-wrap: break-word;'>人工</td><td style='text-align: center; word-wrap: break-word;'>每两个月一次</td><td style='text-align: center; word-wrap: break-word;'>公司所有互联网应用，含APP应用</td></tr></table>

---

## 某大型券商漏洞管理实践


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>漏洞类型</td><td style='text-align: center; word-wrap: break-word;'>举例</td><td style='text-align: center; word-wrap: break-word;'>修复优先级</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已被exploited的RCE（远程命令执行）漏洞</td><td style='text-align: center; word-wrap: break-word;'>Struts2 S-045、S-046、S-048、Oracle WebLogic Server Java Deserialization Remote Code Execution、MS17-010等等，常用于直接拿下互联网边界的一台服务器，再做进一步渗透或横向移动。</td><td style='text-align: center; word-wrap: break-word;'>极高</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他已被exploited的远程利用漏洞</td><td style='text-align: center; word-wrap: break-word;'>Struts2 S2-049等一些可导致拒绝服务攻击，服务器信息泄漏类型的漏洞。</td><td style='text-align: center; word-wrap: break-word;'>高</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已被exploited的本地利用漏洞</td><td style='text-align: center; word-wrap: break-word;'>多用于提权，如Nginx的本地提权漏洞CVE-2016-1247</td><td style='text-align: center; word-wrap: break-word;'>中高</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其它漏洞</td><td style='text-align: center; word-wrap: break-word;'>SSL自签证书、SSL版本低，SSL证书不被信任等</td><td style='text-align: center; word-wrap: break-word;'>中低</td></tr></table>

---

## 某大型券商漏洞管理实践

<div style="text-align: center;"><img src="imgs/img_in_image_box_437_223_1435_1032.jpg" alt="Image" width="51%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_63_225_185.jpg" alt="Image" width="5%" /></div>


## 某大型银行漏洞管理实践

互联网资产庞大：子域名、高危端口与组件、可扫描站点众多，难以覆盖全面，频度要求一天一扫描

➢风险监控：无法有效对互联网业务进行持续的风险监测和0day漏洞预警

➢ 源码监控：无法有效国内外开源社区进行监控

内网扫描全面性与频度：nessus、awvs、appscan，无法统一管理，也无法横向对比，扫描频度要求每周一次

A. 守量

---

## ③ 某大型银行漏洞管理实践

<div style="text-align: center;"><img src="imgs/img_in_image_box_28_399_254_532.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_489_375_691_581.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_941_320_1203_389.jpg" alt="Image" width="13%" /></div>


## 各类扫描工具联动

<div style="text-align: center;"><img src="imgs/img_in_image_box_950_446_1209_518.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_956_579_1201_623.jpg" alt="Image" width="12%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_1444_327_1806_653.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_674_776_944_954.jpg" alt="Image" width="14%" /></div>


## 渗透测试

---

## 目录

## 1 -业界实践

2-业务上线前后面临的挑战

3-漏洞管理思路和实践

4-实践案例介绍

---

## 业务上线前后面临的挑战

## 挑战来自于三个方面：

1、外部威胁：安全漏洞的爆发频率、范围，使得突发性的漏洞应急工作越来越普遍；

2、IT格局变化：企业的IT规模可以快速扩张，边界开始模糊；

3、自身业务发展：企业的互联网化带来业务和开发的快速迭代，使得安全问题更为普遍；

漏洞发现与管理的主要演变：

1、从单一的针对漏洞发现，扩展到资产识别、资产异动变化；

2、从单一节点的扫描方式，扩展到分布式可扩展；

3、从安全主动发起到如何与业务、流程结合；

4、漏洞有效跟踪和管理、沉淀；

---

## 目录

1-业界实践

2-业务上线前后面临的挑战

3-漏洞管理思路和实践

4-实践案例介绍

---

## 应用安全实践方法论

<div style="text-align: center;"><img src="imgs/img_in_chart_box_30_169_1920_1018.jpg" alt="Image" width="98%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_63_225_184.jpg" alt="Image" width="5%" /></div>


## 新一代安全扫描实践

在企业的规模与业务快速增长的需求下，安全团队通过建设云扫描平台，提高风险发现能力与安全工作效率

建设目标

业务场景

## 安全漏洞收敛，整体风险可控

## 内网扫描

• 内网资产发现

• 风险持续监控

## 上线前扫描

· 被动扫描

• 安全能力服务化

• 人工安全测试

## 互联网扫描

漏洞数据运营

• 互联网资产监控

• 安全扫描覆盖度

扫描运营

• 开源社区监控

扫描能力运营

安全应急响应

---

## 全网安全扫描与漏洞管理平台

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_202_615_772.jpg" alt="Image" width="22%" /></div>


小型网络10.0.2.0/24

<div style="text-align: center;"><img src="imgs/img_in_image_box_649_191_1708_764.jpg" alt="Image" width="55%" /></div>


动态扫描节点

<div style="text-align: center;">资产发现、漏洞监控</div>


上线前扫描

1、适应快速变化的环境，可弹性扩展；

2、可与内部流程、系统快速整合；

3、扫描可运营；

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_407_347_578_517.jpg" alt="Image" width="8%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_837_599_1016_726.jpg" alt="Image" width="9%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_1713_335_1916_571.jpg" alt="Image" width="10%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_63_227_183.jpg" alt="Image" width="5%" /></div>


## 内网扫描

特点：环境复杂覆盖难度大

## 要求：全面覆盖，出现紧急事件时可快速响应

## 资产发现与持续监控

☐ 全网资产发现

## 扫描策略制定

☐ 风险持续监控

☐ 全量扫描

应急扫描

扫描工具集中管理

☐ 红线扫描

上线前扫描

☐ 扫描工具集中管理

☐ 结果统一回收

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_64_227_184.jpg" alt="Image" width="5%" /></div>


## 主要业务场景介绍—全网资产发现与持续监控

## 主要业务场景：

1. 应急扫描：紧急任务，0day漏洞，安全事件，安全制度

2. 全量扫描：周期性的对全网安全资产进行全插件扫描

3. 上线前扫描：对新上线的Web/服务器和存在服务变更的资产进行扫描

4.红线扫描：特定高危漏洞、默认口令的合集，全网持续性扫描

<div style="text-align: center;"><img src="imgs/img_in_image_box_915_179_1866_902.jpg" alt="Image" width="49%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_122_64_226_186.jpg" alt="Image" width="5%" /></div>


## 业务场景--扫描能力集成

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_385_423_682.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">内网扫描平台</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_978_231_1349_328.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_1412_230_1791_325.jpg" alt="Image" width="19%" /></div>


## 各类扫描工具联动

<div style="text-align: center;"><img src="imgs/img_in_image_box_1008_384_1319_564.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_1413_422_1806_567.jpg" alt="Image" width="20%" /></div>


1、统一管理

2、单一目标多个分发

3、结果统一回收

<div style="text-align: center;"><img src="imgs/img_in_image_box_999_723_1397_789.jpg" alt="Image" width="20%" /></div>


BURPSUITE PROFESSIONAL

---

## 互联网扫描

特点：最大的风险暴露面

要求：快速感知互联网的变化，并发现自身的风险

互联网资产监控

☐ 未知资产发现

☐ 高危端口发现

安全扫描覆盖度

敏感信息监控

管理后台发现

☐ 持续周期性扫描

高危漏洞快速预警

应用站点梳理

Github开源社区

---

## 业务场景--互联网资产发现与梳理

从黑盒与白盒两个角度发现企业外部资产并进行梳理

➢ 新增域名、IP业务

➢ 高危端口与管理后台发现

可扫描站点（200）、无法扫描站点（404、500等）

<div style="text-align: center;"><img src="imgs/img_in_chart_box_46_507_1798_1065.jpg" alt="Image" width="91%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_117_64_226_183.jpg" alt="Image" width="5%" /></div>


## 上线前扫描

特点：业务快速迭代，守门式的安全测试效率低下

要求：在上线前仅可能的发现更多问题

被动扫描

安全能力服务化

人工安全测试

☐ 基于流量镜像

☐ 基于流量代理

☐ 内部系统集成

☐ 基于Web日志

☐ 安全工具集合

业务逻辑

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_64_227_184.jpg" alt="Image" width="5%" /></div>


## 主要业务场景介绍—被动扫描

➢ 被动扫描，结合用户访问流量，获取会话并进行扫描。相比主动扫描：

1、自动化程度高

2、可对具有交互行为的链接进行扫描





3、快速检查常规安全漏洞，覆盖度高

适合在开发测试环境中部署。

<div style="text-align: center;"><img src="imgs/img_in_image_box_1_228_1920_1075.jpg" alt="Image" width="99%" /></div>


---

<div style="text-align: center;"><img src="imgs/img_in_image_box_118_64_226_184.jpg" alt="Image" width="5%" /></div>


## 业务场景一安全能力服务化

安全能力服务化，将安全检测能力通过对接内部系统或简易的工具集成到开发测试流程中，提高安全工作效率。

<div style="text-align: center;"><img src="imgs/img_in_image_box_37_307_1031_1029.jpg" alt="Image" width="51%" /></div>


➢ 扫描能力集成至CMDB、研发管理平台等

简易的安全门户与扫描API，研发人员可简易使用

➢ 各类插件、流量代理等收集流量，执行被动扫描

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_117_63_227_185.jpg" alt="Image" width="5%" /></div>


## 数据运营

## 漏洞数据运营

□ 漏洞管理

漏洞归档

☐ 安全工作量化

## 扫描能力运营

## 应急响应

扫描能力优化

扫描规则自定义

☐ 0day爆发全网预警

---

## 业务场景一漏洞跟踪与管理

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_0_1920_785.jpg" alt="Image" width="100%" /></div>


· 自动化扫描

· 人工渗透测试

· 众测





## 漏洞发现

·漏洞评级

## 漏洞验证

·漏洞分析

·漏洞检测方案

·漏洞修复方案

·漏洞修复指导

## 修复建议

·漏洞归属部门整改

## 漏洞处置

·二次验证

## 漏洞复测

## 漏洞归档

· 漏洞知识库

· 安全培训



• 工作量化

• 安全开发规范



将漏洞作为企业一种有价值的“资产”来做管理

---

## 业务场景一扫描能力运营与应急响应

第三方扫描器

漏洞情报

内部安全测试

插件制作、优化

全网普查

外部漏洞平台

---

## 目录

1-业界实践

2-业务上线前后面临的挑战

3-漏洞管理思路和实践

4-实践案例介绍

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_119_63_225_186.jpg" alt="Image" width="5%" /></div>


## 某大型企业漏洞威胁感知云平台

<div style="text-align: center;"><img src="imgs/img_in_image_box_28_216_1031_626.jpg" alt="Image" width="52%" /></div>


小型网络10.0.2.0/24

资产发现、漏洞监控

IT安全基础架构部搭建扫描云平台服务于内部云与

内部安全建设

➢ 能力输出：作为内部HIC云平台的安全产品。

自动化上线评估：安全扫描嵌入开发测试环节

全网资产梳理：摸底内网资产与特定应用

➢ 全网漏洞稽查：持续风险监测与高危漏洞预警。

✓ IP总扫描量 230万IP，

✓ 日扫描IP量峰值可达百万级别

✓ HIC云客户上百个

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_64_226_185.jpg" alt="Image" width="5%" /></div>


## 某企业漏洞管理建设项目介绍

某企业开发业务迭代频繁而安全工作滞后，内部考虑将安全扫描融入至开发测试环节

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_280_1884_1080.jpg" alt="Image" width="98%" /></div>


魔方采用产品+服务方式实现协助其SDL落地

➢ 将安全扫描与开发测试流程相结合

➢ 定期对业务逻辑安排人工检测

结合漏洞数据提供针对性的改善方案

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_63_227_184.jpg" alt="Image" width="5%" /></div>


## 某证券漏洞管理项目

<div style="text-align: center;"><img src="imgs/img_in_image_box_10_202_938_787.jpg" alt="Image" width="48%" /></div>


某证券安全组通过魔方的漏洞管理系统，实现以下场景的漏洞管理工作：

1. 通过自动采集和人工填入，整合漏洞结果，满足稽核部门的要求。

2. 结合系统自带的跟踪机制，落实到负责人。

3. 基于漏洞数据优化安全策略，并制定下一步的安全工作措施。

---

谢谢关注·THANKS