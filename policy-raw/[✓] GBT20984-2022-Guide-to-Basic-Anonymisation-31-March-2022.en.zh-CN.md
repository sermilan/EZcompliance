---
title: "Guide to Basic Anonymisation 31 March 2022.en.zh-CN"
source: "个人隐私安全法律法规/报告&白皮书/Guide to Basic Anonymisation 31 March 2022.en.zh-CN.pdf"
type: "pdf"
processed: "2026-04-22T23:05:36.811431"
---

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_12_1190_998.jpg" alt="Image" width="99%" /></div>


## 指南 基本的 匿名化

<div style="text-align: center;"><img src="imgs/img_in_image_box_259_1488_356_1583.jpg" alt="Image" width="8%" /></div>


SG: DIGITAL pdpc PERSONAL DATA PROTECTION COMMISSION SINGAPORE

---



---

## 内容

## ……

介绍 ..... 4  
匿名与去识别 ..... 6  
去标识化的一个例子 ..... 8  
基本数据匿名概念介绍 ..... 9  
匿名过程 ..... 13  
第 1 步：了解您的数据 第 2 ..... 18  
步：去识别您的数据 ..... 20  
第 3 步：应用匿名化技术 ..... 22  
第 4 步：计算您的风险 ..... 24  
第 5 步：管理您的重新识别和披露风险 ..... 25  
附件 A：基本数据匿名技术 ..... 34  
附件 B：常见数据属性和建议 ..... 44  
匿名技术 ..... 49  
附件 C：k-匿名 ..... 52  
附件 D：评估重新识别的风险 ..... 56  
附件 E：匿名工具 ..... 57  
致谢 ..... 57

---

## 介绍

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_194_224_286.jpg" alt="Image" width="9%" /></div>


## 介绍

本指南旨在为刚接触匿名化的组织提供介绍和实用指南，了解如何适当地执行基本的匿名化和结构化的去识别化。 $ ^{1} $，文字 $ ^{2} $，非复杂数据集 $ ^{3} $。它在四个常见用例的上下文中介绍了匿名化工作流程。

本指南并非详尽无遗地处理与数据集的匿名化、去识别化和重新识别相关的所有问题。建议组织考虑聘请匿名化专家、统计学家或独立风险评估员来执行适当的匿名化技术或评估重新识别风险，其中匿名化问题很复杂（例如，包含大量纵向或敏感个人数据的大型数据集）。

实施本指南中的建议并不意味着遵守个人数据保护法 (PDPA)。

不同的司法管辖区对匿名化的看法不同，因此，本指南中提供的建议可能不适用于其他国家的数据保护法。

本指南应与个人数据保护委员会 (PDPC) 一起阅读 $ \underline{\text{选定主题的个人数据保护法咨询指南}} $

---

## …

## 匿名化 相对 去识别化

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_125_214_215_302.jpg" alt="Image" width="7%" /></div>


## 匿名与 去识别化

匿名化是指将个人数据转换为不能用于识别任何个人的数据。PDPC 将匿名化视为基于风险的过程，其中包括应用匿名化技术和保护措施来防止重新识别。

去识别化 $ ^{4} $指删除直接识别个人的标识符（例如姓名、地址、国民登记身份证（NRIC）号码）。去标识化有时被错误地等同于匿名化，但这只是匿名化的第一步。当与公开或易于访问的数据结合时，去标识化的数据集很容易被重新标识。

重新识别是指从以前去识别或匿名的数据集中识别个人。

匿名数据不被视为个人数据，因此不受PDPA管辖。有关更多信息，请参阅PDPC中关于匿名化的主题选定主题的个人数据保护咨询指南。

## 去标识化的一个例子

Albert 经常使用订餐应用程序。他最喜欢的订餐应用——SuperHungry — 决定为黑客马拉松发布一些关于其用户的信息。

Albert 在 SuperHungry 的数据记录：

姓名

阿尔伯特·普瓦

最喜欢的餐馆

加东炒鸡

出生日期

1990年1月1日

性别

男性

最喜欢的食物

3 件套鸡，

33 过去的订单

公司

ABC私人有限公司

---

SuperHungry 通过在发布前删除名称来对数据集进行去标识化，认为这等同于对数据集进行匿名化。

由 SuperHungry 发布的 Albert 去识别化记录：

阿尔伯特·普瓦

最喜欢的餐馆

<div style="text-align: center;"><img src="imgs/img_in_image_box_277_433_904_636.jpg" alt="Image" width="52%" /></div>


最喜欢的食物

加东炒鸡

出生日期

性别

1990年1月1日

男性

公司

ABC私人有限公司

但是，可以通过将他的去识别记录与其他记录（例如来自他的社交媒体档案的个人信息）相结合来重新识别 Albert。

阿尔伯特的社交媒体简介：

姓名

出生日期

阿尔伯特·普瓦

1990年1月1日

性别

男性

公司

ABC私人有限公司

任何有足够动力的人都可以轻松识别 $ _{5} $如果有其他公开或容易获得的信息来启用这种重新识别，则从去识别的数据中作为 Albert 的人。如果数据集或组合数据集是敏感的，则需要进一步匿名化。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_473_498_727_812.jpg" alt="Image" width="21%" /></div>


## 介绍 基本数据 匿名化 概念

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_122_183_215_300.jpg" alt="Image" width="7%" /></div>


## 基本数据匿名概念介绍

数据匿名化需要对以下要素有很好的理解，在确定什么构成合适的匿名技术和适当的匿名级别时应考虑这些要素。

## 一 种匿名化和实用性的目的

匿名化的目的必须明确，因为匿名化应该专门针对手头的目的进行。无论使用何种技术，匿名化过程都会在一定程度上减少数据集中的原始信息。因此，随着匿名化程度的增加，数据集的实用性（例如清晰度和/或精确度）通常会降低。因此，组织需要决定可接受（或预期）效用与重新识别风险之间的权衡程度。

应该注意的是，效用不应该在整个数据集的级别上进行评估，因为它对于不同的属性通常是不同的。一个极端是特定数据属性的准确性至关重要，不应应用概括或匿名技术（例如，在分析入院趋势时，医疗条件和给予个人的药物可能是关键数据）。另一个极端是数据属性对预期目的没有用处，并且可以完全删除而不影响数据对接收者的效用（例如，在分析购买交易趋势时，个人的出生日期可能并不重要）。

在确定效用和匿名之间的权衡时，另一个重要的考虑因素是，如果接收者知道应用了哪些匿名技术和粒度程度，是否会带来额外的风险；一方面，了解这些信息可能有助于分析师理解结果并更好地解释它们，但另一方面它可能包含提示，这可能导致更高的重新识别风险。

## 乙 可逆性

通常，数据匿名化过程将是“不可逆的”，匿名数据集的接收者将无法重新创建原始数据。但是，在某些情况下，应用匿名化的组织保留了从匿名数据重新创建原始数据集的能力；在这种情况下，匿名化过程是“可逆的”。

---

## C 匿名化技术的特点

各种匿名化技术的不同特征意味着某些技术可能比其他技术更适合特定情况或数据类型。例如，某些技术（例如字符屏蔽）可能更适合用于直接标识符，而其他技术（例如聚合）可能更适合用于间接标识符。要考虑的另一个特征是属性值是连续值（例如高度 = 1.61m）还是离散值（例如“是”或“否”），因为诸如数据扰动之类的技术对于连续值效果更好。

各种匿名化技术也以截然不同的方式修改数据。有些只修改属性的一部分（例如字符屏蔽）；一些替换跨多个记录的属性值（例如聚合）；有些用不相关但唯一的值替换属性的值（例如化名）；和一些完全删除属性（例如属性抑制）。

一些匿名化技术可以组合使用（例如，在执行泛化后抑制或删除（异常值）记录）。

## D 推断信息

从匿名数据中推断出某些信息是可能的。例如，屏蔽可能会隐藏个人数据，但不会隐藏原始值的长度（以字符数计）。

组织也可能希望考虑匿名数据的呈现顺序。例如，如果接收者知道数据记录是按顺序收集的（例如，访客来时登记），则可能谨慎（只要不影响实用性）重新洗牌整个数据集以避免基于数据记录的顺序。

推理不限于单个属性，即使匿名技术已应用于所有属性，也可以跨属性应用。因此，在决定实际技术之前和应用技术之后，匿名化过程必须注意可能发生推理的每一种可能性。

## 乙 对主题的专业知识

匿名技术基本上将一个或多个个人的可识别性从原始数据集中降低到组织风险组合可接受的水平。

可识别性和可重新识别性 $ ^{6} $应在应用匿名技术之前和之后进行评估。这需要对数据相关的主题有很好的理解。例如，如果数据集是医疗保健数据，则

---

组织可能需要具有足够医疗保健知识的人来评估记录的唯一性（即在何种程度上可识别或可重新识别）。

匿名化过程之前的评估确保属性中的结构和信息被清楚地识别和理解，并评估从这些数据中进行显式和隐式推断的风险。例如，包含出生年份的属性隐含地提供年龄，在某种程度上就像 NRIC 号码一样。匿名化过程之后的评估将确定从匿名数据中重新识别的剩余风险。

另一个例子是当数据属性在记录之间交换时，需要主题专家来识别匿名记录是否有意义。

因此，匿名化技术的正确选择取决于对数据集中包含的显式和隐式信息的认识以及打算匿名的信息的数量或类型。

## F 匿名化过程和技术的能力

希望共享匿名数据集的组织应确保匿名过程由经过培训并熟悉匿名技术和原则的员工进行。如果在组织内找不到必要的专业知识，则应聘请外部帮助。

## G 收件人

诸如接收者在主题方面的专业知识以及为限制接收者数量和防止数据与未经授权的各方共享而实施的控制等因素在选择匿名技术方面发挥着重要作用。特别是，接收者对匿名数据的预期使用可能会对所应用的技术施加限制，因为数据的效用可能会超出可接受的限制。在公开发布数据时需要格外小心，与根据合同安排共享的数据相比，组织将需要更强大的匿名形式。

## H 工具

软件工具对于帮助执行匿名化技术非常有用。有关市场上可用的一些匿名工具，请参阅附件 E。

---

## 8 

## 这 匿名化 过程

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_184_251_320.jpg" alt="Image" width="12%" /></div>


## 匿名过程

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_412_278_537.jpg" alt="Image" width="10%" /></div>


## 第1步

了解你的数据

<div style="text-align: center;"><img src="imgs/img_in_image_box_347_396_483_550.jpg" alt="Image" width="11%" /></div>


## 第2步

去识别

你的数据

<div style="text-align: center;"><img src="imgs/img_in_image_box_533_365_706_585.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_718_355_849_587.jpg" alt="Image" width="10%" /></div>


## 第3步

申请

匿名化

技术

## 第四步

!

计算

你的风险

## 第5步

管理

你的风险

根据您的用例，您可以使用这五个步骤在适当的情况下对数据集进行匿名化。在本指南中，我们使用组织的五个常见数据用例来解释这些步骤。

在所有数据用例中，您应确保：

<div style="text-align: center;"><img src="imgs/img_in_image_box_234_946_346_1069.jpg" alt="Image" width="9%" /></div>


数据最小化，只有必要的数据属性和数据集的提取（如果可能）共享给第三方；

您匿名的数据集的任何识别信息都不应公开（例如，如果您在会员数据库上匿名信息，则您的会员基础资料不应公开）；和

<div style="text-align: center;"><img src="imgs/img_in_image_box_965_1163_1076_1280.jpg" alt="Image" width="9%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_233_1388_346_1516.jpg" alt="Image" width="9%" /></div>


为假名的匿名数据集和身份映射表提供适当级别的保护和保障，以防止重新识别。通常，通过匿名化修改数据集的次数越少，您就越需要保护和保护数据集，因为重新识别的风险就越高。

---

## 用例：如何使用匿名或去识别的数据

以下是可以在您的组织中使用匿名或去识别化数据的一些方法。

<div style="text-align: center;"><img src="imgs/img_in_image_box_140_339_1049_503.jpg" alt="Image" width="76%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="12">适用步骤*</td></tr><tr><td colspan="2">1</td><td colspan="2">2</td><td colspan="2">3</td><td colspan="2">4</td><td colspan="4">5</td></tr><tr><td colspan="2">了解你的数据</td><td style='text-align: center; word-wrap: break-word;'>去识别你的数据</td><td style='text-align: center; word-wrap: break-word;'>应用匿名化技术</td><td colspan="2">计算你的风险</td><td colspan="6">管理你的风险</td></tr><tr><td colspan="2">用例</td><td colspan="10">内部数据共享（去标识化数据）</td></tr><tr><td colspan="2">描述</td><td colspan="10">仅对数据进行去标识化以支持组织内的记录级数据共享和使用，这可能需要保留数据中的大多数细节。去识别的数据仍然是个人数据，因为它很可能很容易重新识别。但是，对数据进行去标识化仍然是一种很好的做法，因为它提供了额外的保护层。</td></tr><tr><td colspan="8">是否需要额外的控制来防止重新识别？</td><td colspan="4">是的</td></tr><tr><td colspan="8">最终结果是否被视为匿名数据？</td><td colspan="4">不</td></tr><tr><td colspan="2">* 适用的</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td colspan="8">5</td></tr><tr><td colspan="12"></td></tr><tr><td colspan="2">用例</td><td colspan="10">内部数据共享（匿名数据）（例如，关于高价值消费者的人口统计数据及其与忠诚度团队各自的消费模式的匿名数据，以制定差异化的客户价值主张）。</td></tr><tr><td colspan="2">描述</td><td colspan="10">在以下情况下，组织可以考虑使用匿名数据而不是去识别化数据进行内部共享：• 内部数据共享不需要详细的去识别化个人数据（例如用于趋势分析）；• 所涉及的数据本质上更敏感（例如财务信息）；要么• 与多个部门共享的更大数据集。在这种情况下，组织可以将建议用于外部数据共享的匿名化流程应用于其内部数据共享用例，以降低重新识别和披露的风险。</td></tr><tr><td colspan="8">是否需要额外的控制来防止重新识别？</td><td colspan="4">是的</td></tr><tr><td colspan="8">最终结果是否被视为匿名数据？</td><td colspan="4">是的</td></tr><tr><td colspan="2">* 适用步骤</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td colspan="6">5</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4"><img src="imgs/img_in_image_box_141_255_1054_434.jpg" alt="Image"" /></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用例</td><td colspan="3">外部数据共享（例如，在销售部门和外部业务合作伙伴之间共享匿名客户数据，用于分析客户资料和开发联合品牌产品）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td colspan="3">出于业务协作目的与授权的外部方共享的记录级数据。匿名化技术用于将个人数据转换为非识别数据。</td></tr><tr><td colspan="3">是否需要额外的控制来防止重新识别？</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td colspan="3">最终结果是否被视为匿名数据？</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 适用步骤</td><td colspan="3">1 2 3 4 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用例</td><td colspan="3">长期数据保留用于数据分析（例如客户趋势的历史分析）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td colspan="3">匿名化技术用于将个人数据转换为非识别数据，并允许数据在保留期之后保持在记录级别，以进行长期数据分析。</td></tr><tr><td colspan="3">是否需要额外的控制来防止重新识别？</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td colspan="3">最终结果是否被视为匿名数据？</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 适用步骤</td><td colspan="3">1 2 3 4 5</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3"><img src="imgs/img_in_image_box_141_256_1051_428.jpg" alt="Image"" /></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用例</td><td colspan="2">综合数据用于应用程序开发和测试目的，不需要复制原始数据的统计特征（例如，用于开发和测试工资单应用程序的外包供应商的测试）。</td></tr><tr><td rowspan="2">描述</td><td colspan="2">通过使用本指南中的匿名化技术对所有数据属性进行高度匿名化，可以从原始数据创建记录级合成数据，这样所有数据属性都会被非常显着地修改，并且创建的所有记录都不匹配原始数据中任何个人的记录。</td></tr><tr><td colspan="2">在这种情况下，匿名化技术的应用不会保留原始数据的统计特征，因此不适用于人工智能模型训练或数据分析等复杂目的。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>是否需要额外的控制来防止重新识别？</td><td colspan="2">不8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>最终结果是否被视为匿名数据？</td><td colspan="2">是的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>* 适用步骤</td><td colspan="2">1 2 3</td></tr><tr><td colspan="3">注意：在合成数据中，使用的“假”直接标识符不应与真实人相关，即随机生成的NRIC与随机生成的姓名不应与真实人员的NRIC和姓名组合相同。</td></tr></table>

7. 本指南未涉及的另一种方法是从头开始创建合成数据。这可以通过随机生成仅满足数据格式要求的数据集来完成，或者通过使用人工智能或其他方法生成还保留原始数据集统计特征的数据集来完成。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_157_263_286.jpg" alt="Image" width="8%" /></div>


## 了解您的数据

适用于：

内部数据共享（去识别的数据）

内部数据共享（匿名数据）或外部数据共享

<div style="text-align: center;"><img src="imgs/img_in_image_box_130_352_1066_491.jpg" alt="Image" width="78%" /></div>


长期数据保留

综合数据

一个⼈数据记录由具有不同程度可识别性的数据属性组成

和 对个人的敏感性。

匿名化通常涉及删除直接标识 符和修改间接标识符。目标属性通常保持不变，除非目的是创建合成数据。下面的表格和示例说明了数据属性通常如何在数据记录中进行分类。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>直接标识符</td><td style='text-align: center; word-wrap: break-word;'>间接标识符</td><td style='text-align: center; word-wrap: break-word;'>目标属性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类</td><td style='text-align: center; word-wrap: break-word;'>这些是数据属性是</td><td style='text-align: center; word-wrap: break-word;'>这些是数据属性是</td><td style='text-align: center; word-wrap: break-word;'>这些是包含数据集主要效用的数据属性。在评估匿名化充分性的背景下，该数据属性在本质上可能是敏感的，并且在披露时可能会对个人造成很大的不利影响。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据的中的属性数据集</td><td style='text-align: center; word-wrap: break-word;'>独一无二的个人和可以用作键数据属性重新识别一个个人。</td><td style='text-align: center; word-wrap: break-word;'>不是个人独有的，但可能重新识别一个个人当结合其他信息（例如组合年龄、性别和邮政编码）。</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可访问性数据的</td><td style='text-align: center; word-wrap: break-word;'>这些数据属性是通常是公开的或易于访问。</td><td style='text-align: center; word-wrap: break-word;'>这些数据属性可能是公开或容易无障碍。</td><td style='text-align: center; word-wrap: break-word;'>这些数据属性通常不公开或不易于访问。它们不能用于重新识别，因为它们通常是专有的。</td></tr></table>

---

常见的

中的示例

数据集

· 姓名

电子邮件地址

手机数字

· 身份证号码

护照号码

出生证明数字

• 帐号

外国的鉴别号码(FIN

· 性别

· 种族

工作准证数字

社交媒体用户名

· 年龄

出生日期

· 地址

邮政编码

· 职称

公司名

婚姻状况

• 高度

• 重量

互联网协议 (IP) 地址

• 车辆车牌号

车载单元 (IU) 编号

· 全球定位系统 (GPS) 位置

## • 交易

(例如购买)

薪水

信用评级

保险政策

医疗诊断

疫苗接种情况

## 例 1: C 九助会

## EMPL 中的 ATA 属性

## OYEE 数据记录


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>员工证</td><td style='text-align: center; word-wrap: break-word;'>姓名</td><td style='text-align: center; word-wrap: break-word;'>部门</td><td style='text-align: center; word-wrap: break-word;'>nt</td><td style='text-align: center; word-wrap: break-word;'>性别</td><td style='text-align: center; word-wrap: break-word;'>出生日期</td><td style='text-align: center; word-wrap: break-word;'>站 rt 日期的服务</td><td style='text-align: center; word-wrap: break-word;'>就业类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>39192</td><td style='text-align: center; word-wrap: break-word;'>小安迪·托马斯</td><td style='text-align: center; word-wrap: break-word;'>研究发展</td><td style='text-align: center; word-wrap: break-word;'>&amp;</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>1971年8月1日</td><td style='text-align: center; word-wrap: break-word;'>02/03/1997</td><td style='text-align: center; word-wrap: break-word;'>兼职</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>37030</td><td style='text-align: center; word-wrap: break-word;'>保拉·斯文森</td><td style='text-align: center; word-wrap: break-word;'>工程</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>1976年5月15日</td><td style='text-align: center; word-wrap: break-word;'>2015年8月3日</td><td style='text-align: center; word-wrap: break-word;'>全职</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22722</td><td style='text-align: center; word-wrap: break-word;'>黄宗泽木</td><td style='text-align: center; word-wrap: break-word;'>工程</td><td style='text-align: center; word-wrap: break-word;'>米</td><td style='text-align: center; word-wrap: break-word;'>1973年12月31日</td><td style='text-align: center; word-wrap: break-word;'>1991年7月30日</td><td style='text-align: center; word-wrap: break-word;'>全职</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>28760</td><td style='text-align: center; word-wrap: break-word;'>史蒂夫·斯通</td><td style='text-align: center; word-wrap: break-word;'>工程</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>1970年12月24日</td><td style='text-align: center; word-wrap: break-word;'>2010年3月18日</td><td style='text-align: center; word-wrap: break-word;'>兼职</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13902</td><td style='text-align: center; word-wrap: break-word;'>杰克诺玛</td><td style='text-align: center; word-wrap: break-word;'>人力资源</td><td style='text-align: center; word-wrap: break-word;'>米</td><td style='text-align: center; word-wrap: break-word;'>1973年7月15日</td><td style='text-align: center; word-wrap: break-word;'>28/05/2012</td><td style='text-align: center; word-wrap: break-word;'>兼职</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

直接标识符

间接标识符

目标变量

## 示例 2：客户数据记录中数据属性的分类


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>顾客 ID</td><td style='text-align: center; word-wrap: break-word;'>姓名</td><td style='text-align: center; word-wrap: break-word;'>性别 出生日期</td><td style='text-align: center; word-wrap: break-word;'>邮政代码</td><td style='text-align: center; word-wrap: break-word;'>职业</td><td style='text-align: center; word-wrap: break-word;'>收入</td><td style='text-align: center; word-wrap: break-word;'>教育</td><td style='text-align: center; word-wrap: break-word;'>婚姻状态</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>56833</td><td style='text-align: center; word-wrap: break-word;'>珍妮杰斐逊</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>1975年5月8日</td><td style='text-align: center; word-wrap: break-word;'>570150</td><td style='text-align: center; word-wrap: break-word;'>数据科学家</td><td style='text-align: center; word-wrap: break-word;'>13,000美元</td><td style='text-align: center; word-wrap: break-word;'>硕士寡</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>50271</td><td style='text-align: center; word-wrap: break-word;'>彼得·G</td><td style='text-align: center; word-wrap: break-word;'>米</td><td style='text-align: center; word-wrap: break-word;'>1973年12月14日</td><td style='text-align: center; word-wrap: break-word;'>787589</td><td style='text-align: center; word-wrap: break-word;'>大学讲师</td><td style='text-align: center; word-wrap: break-word;'>12,000美元</td><td style='text-align: center; word-wrap: break-word;'>博士学位已婚</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>53041</td><td style='text-align: center; word-wrap: break-word;'>蒂姆莱克</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>1985年2月3日</td><td style='text-align: center; word-wrap: break-word;'>408600</td><td style='text-align: center; word-wrap: break-word;'>研究员</td><td style='text-align: center; word-wrap: break-word;'>7,000美元</td><td style='text-align: center; word-wrap: break-word;'>博士学位离婚</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>17290</td><td style='text-align: center; word-wrap: break-word;'>雷米湾</td><td style='text-align: center; word-wrap: break-word;'>米</td><td style='text-align: center; word-wrap: break-word;'>1968年3月27日</td><td style='text-align: center; word-wrap: break-word;'>570150</td><td style='text-align: center; word-wrap: break-word;'>数据库行政人员</td><td style='text-align: center; word-wrap: break-word;'>8,000美元</td><td style='text-align: center; word-wrap: break-word;'>学士已婚</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>52388</td><td style='text-align: center; word-wrap: break-word;'>沃尔特·保罗</td><td style='text-align: center; word-wrap: break-word;'>米</td><td style='text-align: center; word-wrap: break-word;'>1967年6月25日</td><td style='text-align: center; word-wrap: break-word;'>199588</td><td style='text-align: center; word-wrap: break-word;'>建筑师</td><td style='text-align: center; word-wrap: break-word;'>10,000美元</td><td style='text-align: center; word-wrap: break-word;'>硕士单身的</td></tr><tr><td colspan="3">直接标识符</td><td colspan="3">间接标识符</td><td style='text-align: center; word-wrap: break-word;'>目标</td><td style='text-align: center; word-wrap: break-word;'>间接标识符</td></tr></table>

---

作为数据最小化的一部分，应删除结果数据集中不需要的任何数据属性。下面提供了一个简单的流程图，以帮助您对数据属性进行适当的分类。

<div style="text-align: center;"><img src="imgs/img_in_image_box_128_369_1069_749.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_155_812_267_937.jpg" alt="Image" width="9%" /></div>


去识别您的数据

<div style="text-align: center;"><img src="imgs/img_in_image_box_117_991_1065_1132.jpg" alt="Image" width="79%" /></div>


适用于：

蒂 s 步骤始终作为匿名化过程的一部分执行。

冷杉，删除所有直接标识符。在以下示例中，将删除所有名称。在哪里

数据集包括其他直接标识符，例如 NRIC 号码和电子邮件地址，这些也应该被删除。

<div style="text-align: center;"><img src="imgs/img_in_image_box_275_1384_856_1524.jpg" alt="Image" width="48%" /></div>


---

0 ___

（可选）如果需要将记录链接回唯一的个人或原始记录以用于以下用例，则为每条记录分配一个假名：

一种。数据合并；

湾。分析与独特个人有关的多项记录；要么

C。生成合成数据集，其中需要直接标识符值来开发和测试应用程序。对于这个用例，用假名替换所有必要的直接标识符。

每个唯一直接标识符的假名应该是唯一的（如下图所示）。假名的分配也应该是稳健的（即，未经授权的各方不能通过猜测或计算来自假名的原始直接标识符值来逆转）。

姓名

令牌

亚历克斯

黄宗泽

年龄

夏琳

最喜欢的节目

5432

大爆炸理论

朋友们

实习医生格蕾

如果您想保留在后续时间点将去标识化的数据记录链接回原始记录的能力，则需要保留直接标识符和假名之间的映射。身份映射表（如下所示）应妥善保存，因为它允许重新识别。

姓名

亚历克斯

黄宗泽

令牌

夏琳

1234

5678

5432

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_69_1078_483.jpg" alt="Image" width="81%" /></div>


在咂此步骤中，您将对间接标识符应用匿名技术，这样它们就不能轻易地与可能包含额外信息是的其他数据集结合起来以重新识别个人。对于合成数据用例，还应将匿名化技术应用于目标属性。

请注意，这些技术的应用将修改数据值，并可能影响匿名数据在某些用例（例如数据分析）中的效用。下面推荐的匿名化技术考虑了每个用例中记录级数据所需的潜在效用。如果与其用例相关，组织可以使用超出推荐范围的其他匿名技术。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>用例</td><td style='text-align: center; word-wrap: break-word;'>建议的记录级数据匿名化技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部数据分享（匿名数据）要么外部数据分享</td><td style='text-align: center; word-wrap: break-word;'>· 记录抑制：删除记录（即数据行，尤其是在此类数据可能包含无法进一步匿名的唯一数据值的情况下）。· 属性抑制：删除数据属性（即数据列，尤其是在数据集中不需要此类数据并且可能包含无法进一步匿名的唯一数据值的情况下）。· 字符掩码：将数据值的某些字符替换为一致的符号（例如* 或 x）。例如，屏蔽邮政编码将涉及将其从“235546”更改为“23xxxx”。· 概括：数据粒度的减少（例如，通过将一个人的年龄转换为一个年龄范围）。例如，将一个人的年龄从“26岁”概括为“25-29岁”。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>长期数据保留</td><td style='text-align: center; word-wrap: break-word;'>· 记录或属性抑制· 字符掩蔽· 概括· 数据扰动：通过向原始数据添加“噪声”来修改数据中的值（例如，数据中的+/-随机值）。扰动程度应与属性值的范围成比例。例如，数据扰动将涉及通过将数据四舍五入到最接近的10,000美元来将个人的工资数据从“256,654美元”修改为“260,000美元”。或者，可以通过从原始值中减去10,000美元内的随机数，将个人的工资修改为“250,554美元”。</td></tr><tr><td rowspan="3">综合数据</td><td style='text-align: center; word-wrap: break-word;'>注意：当不需要记录级数据时，也可以为此用例执行数据聚合（参见附录A示例）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对原始数据应用大量匿名化以创建合成数据，从而显著修改所有数据属性（包括目标属性）。使用此方法创建的结果数据集和个人记录不会与任何个人的记录有任何相似之处，并且不会保留原始数据集的特征。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>由于生成的数据集与原始数据集不相似，因此适用于应用程序开发/测试，但不适用于AI模型训练。· 数据扰动· 交换：数据集中数据的随机重新排列，使得单个属性值仍然在数据集中表示，但通常与原始记录不对应。</td></tr></table>

有关各种匿名技术以及如何应用它们的更多信息，请参阅附录 A。请参阅附录 B，了解建议的匿名技术以应用于公共数据属性列表。

下一步：应用适当的匿名化技术后，继续执行步骤 4 以评估风险级别。重复步骤 3 和 4，直到达到 k-匿名值 3、5 或更多。

注意：您还可以考虑删除对已应用的其他匿名化技术“抵抗”的异常记录或属性（使用记录或属性抑制），特别是如果此类异常值的数量相对较少且删除不会显着影响您的用例的数据质量。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_154_152_267_287.jpg" alt="Image" width="9%" /></div>


## 计算您的风险

内部数据共享（去识别的数据）

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_336_1021_475.jpg" alt="Image" width="74%" /></div>


内部数据共享（匿名数据）或外部数据共享

适用于：

长期数据保留

综合数据

☾-圈名9是一个简单的方法10,11计算数据集的重新识别风险级别。asically指的是可以在数据集中它⌉组合在一起的相同记录的最少数量。在评估数据集的整体重新识别风险时，通常采用最小的组来代表最坏的情况。一种☾-anonymity值为1表示该记录是唯一的。通常，只考虑间接标识符☾-匿名计算。12

更高的k-匿名值意味着重新识别的风险较低，而较低的k-匿名值意味着更高的风险。一般行业门槛为k-匿名值为3或5.13在可能的情况下，更高k-应设置匿名阈值以最小化任何重新识别风险。

请参阅 PDPC 的第 3 章（匿名化） $ \underline{\text{选定主题的个人数据保护法咨询指南}} $ 关于确定数据是否可以被视为足够匿名的标准。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>邮政代码</td><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>最喜欢的节目</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22xxxx</td><td style='text-align: center; word-wrap: break-word;'>21至25</td><td style='text-align: center; word-wrap: break-word;'>艾米丽在巴黎</td><td rowspan="6">$ k=2 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22xxxx</td><td style='text-align: center; word-wrap: break-word;'>21至25</td><td style='text-align: center; word-wrap: break-word;'>艾米丽在巴黎</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41至45</td><td style='text-align: center; word-wrap: break-word;'>布鲁克林九点九</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41至45</td><td style='text-align: center; word-wrap: break-word;'>布鲁克林九点九</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41至45</td><td style='text-align: center; word-wrap: break-word;'>布鲁克林九点九</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41至45</td><td style='text-align: center; word-wrap: break-word;'>布鲁克林九点九</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56至60</td><td style='text-align: center; word-wrap: break-word;'>爱登堡的彩色生活</td><td rowspan="3">$ k=3 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56至60</td><td style='text-align: center; word-wrap: break-word;'>爱登堡的彩色生活</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56至60</td><td style='text-align: center; word-wrap: break-word;'>爱登堡的彩色生活</td></tr></table>

上图说明了具有三组相同记录的数据集。这k每组的值范围从2到4。总体而言，数据集的k-匿名值为2，反映整个数据集中的最低值（最高风险）。 $ ^{14} $

---

下一步：如果达到k-匿名值阈值，则进行步骤5。如果k-匿名值低于设置阈值，则返回步骤3并重复。

注意：如果可能，您应该设置更高的 k-匿名值 (例如.5 或更多) 用于外部数据共享，而较低的值（例如.3）可设置为内部数据共享或长期数据保留。但是，如果您无法进一步匿名化您的数据以实现这一目标，您应该采取更严格的保护措施，以确保匿名数据不会泄露给未经授权的各方，并降低重新识别风险。或者，您可以聘请专家提供替代评估方法，以实现等效的重新识别风险。

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_669_256_789.jpg" alt="Image" width="7%" /></div>


第5步

管理您的重新识别和披露风险



<div style="text-align: center;"><img src="imgs/img_in_image_box_174_851_215_888.jpg" alt="Image" width="3%" /></div>


适用于：

内部数据共享（去识别的数据）

<div style="text-align: center;"><img src="imgs/img_in_image_box_579_852_618_887.jpg" alt="Image" width="3%" /></div>


内部数据共享（匿名数据）或外部数据共享

<div style="text-align: center;"><img src="imgs/img_in_image_box_267_930_307_961.jpg" alt="Image" width="3%" /></div>


长期数据保留

综合数据

它是一般来说，采取适当措施保护您的数据免受重新识别和披露是谨慎的做法。这是鉴于未来的风陂技术进步，以及可用于匹配您的匿名数据集并允许重新识别比匿名化时的预期更容易执行的未知数据集。

9. 更多信息 k-匿名和如何使用 k-可在附件 C 和附件 D 中找到评估重新识别风险的匿名性。

10. k-匿名性可能不适用于所有类型的数据集或其他复杂用例（例如，相同的间接标识符可能出现在多个记录中的纵向或事务性数据）。特殊唯一性检测算法（SUDA）和 μ-Argus 是评估共享数据集风险的其他方法/工具。

11.使用的已知限制k-匿名是通过同质性攻击的属性泄露，可以使用k-匿名扩展l-多样性和吨-亲密。这些主题超出了本指南的范围。

12. 在步骤 2 中应删除直接标识符，计算中不应包括假名；否则，每条记录都是唯一的。

参考自去识别化决策框架由澳大利亚信息专员办公室、CSIRO 和 Data 61 提供。

14.该指南采用更保守的方法来看待最大风险。还有其他方法（例如平均风险和严格平均风险）。

---

作为良好做法，还应清楚记录匿名化过程、使用的参数和控制的细节，以供将来参考。此类文档有助于审查、维护、微调和审计。请注意，此类文档应妥善保存，因为参数的发布可能有助于重新识别和披露匿名数据。

存在各种类型的重新识别和披露风险。以下解释了在审查已实施的保护措施的充分性时应评估的一些基本问题。

## 1 重新识别（身份披露）

以高度的信心确定特定记录所描述的个人的身份。这可能源于匿名化不足、通过链接重新识别或假名反转等情况。例如，一个基于易于猜测和可逆算法创建假名的匿名化过程，例如将“1”替换为“a”，将“2”替换为“b”等等。

## 2 属性披露

以高置信度确定数据集中描述的属性属于特定个人，即使无法区分个人的记录。举个例子，一个包含特定美容外科医生的匿名客户记录的数据集显示他所有30岁以下的客户都经历了特定的程序。如果知道某个特定的人28岁并且是该外科医生的客户，那么我们就知道该人已经经历了特定的程序，即使该人的记录无法与匿名数据集中的其他人区分开来。

## 3 推理披露

通过数据集的统计属性，以高度的置信度对个人进行推断，即使他或她不在数据集中。例如，如果医学研究人员发布的数据集显示70%的75岁以上的人患有某种疾病，则可以推断出不在数据集中的个人的信息。

一般来说，大多数传统的匿名化技术旨在防止重新识别，而不一定是其他类型的披露风险。

---

0

下表说明了何时建议采取措施应对重新识别和披露风险。以下段落概述了用例的一组基本保护措施（技术、流程和法律控制）。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>用例</td><td style='text-align: center; word-wrap: break-word;'>您是否需要管理重新识别和披露风险对于去识别或匿名数据集？</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部数据分享（去识别数据）</td><td style='text-align: center; word-wrap: break-word;'>由于仅应用了去识别化以保持较高的数据效用，因此去识别化数据的重新识别和披露风险更高。因此，需要对去识别的数据集进行保护。身份映射表（如果有）应该是安全的。如果发生数据泄露，去识别技术的应用、去识别数据集的保护方式以及映射表的保护方式都将被视为实施的保护机制的一部分。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部数据分享（匿名数据）</td><td style='text-align: center; word-wrap: break-word;'>为了降低重新识别和披露风险，在以下情况下，如有必要，应对数据进行匿名化以供内部共享。它们是(a)不需要详细的个人数据的地方，(b)可以共享敏感数据的地方，或者(c)与多个部门共享大型数据集的地方。匿名数据集需要基本保护。身份映射表（如果有）应该是安全的，并且不与其他内部部门共享。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外部数据分享</td><td style='text-align: center; word-wrap: break-word;'>匿名数据集需要基本保护。身份映射表（如果有的话）应该是安全的并且不被外部共享。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>长期数据保留</td><td style='text-align: center; word-wrap: break-word;'>匿名数据集需要基本保护。所有身份映射表都将被安全销毁。</td></tr></table>

对于合成数据用例，当对所有间接标识符和目标属性大量应用匿名化以使记录与原始数据集不相似时，重新识别风险被认为是最小的。因此，不需要进一步保护该数据集。

技术和过程控制：您应该实施技术保护措施来管理去识别和匿名数据的重新识别和披露风险。下表建议了一些良好做法。

您应该查看这些良好实践，以确定它们是否足以根据应用的匿名程度、去识别/匿名数据的敏感性和用例来保护您的去识别/匿名数据。您可以参考 PDPC 的 ICT 系统数据保护实践指南 相关的额外保护措施。

---

在表中，“是”表示建议您采用相应的技术控制和“不适用”表示特定的技术控制不适用于该用例。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">技术控制</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（德-确定数据）</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（匿名数据）</td><td style='text-align: center; word-wrap: break-word;'>外部的数据分享</td><td style='text-align: center; word-wrap: break-word;'>长-学期数据保留</td></tr><tr><td rowspan="2">访问控制和密码</td><td style='text-align: center; word-wrap: break-word;'>在应用程序级别实施访问控制，将数据访问限制在用户级别。最低级别的密码复杂性（即最少12个字母数字字符，混合大写、小写、数字和特殊字符）。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期检查用户帐户以确保所有帐户都处于活动状态并且分配的权限是必要的（例如，当用户离开组织时删除用户帐户或当他或她在组织中更改其角色时更新用户的权限）。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">技术控制</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（德-确定数据）</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（匿名数据）</td><td style='text-align: center; word-wrap: break-word;'>外部的数据共享</td><td style='text-align: center; word-wrap: break-word;'>长-学期数据保留</td></tr><tr><td rowspan="4">存储设备/数据库的安全性</td><td style='text-align: center; word-wrap: break-word;'>使用密码功能保护计算机。这些示例包括在启动期间输入密码、要求登录操作系统、在一段时间不活动后锁定屏幕等。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>加密数据集。定期审查加密方法（例如算法和密钥长度），以确保其被业界认可为相关且安全。</td><td style='text-align: center; word-wrap: break-word;'>是（其中涉及的数据是敏感的自然或更大的数据集与共享超过一个部但匿名化未应用到数据集。）</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用（其中重新识别风险评估低（例如k-匿名性是5个或更多），加密不必应用于匿名数据集。）</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>加密身份映射表。身份映射表应该是安全的，而不是在所有用例中共享。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用（身份映射表应该删除。）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>将数据集的解密密钥分别传达给共享/导出数据的目标接收者。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">过程控制</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（德-确定数据）</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（匿名数据）</td><td style='text-align: center; word-wrap: break-word;'>外部的数据分享</td><td style='text-align: center; word-wrap: break-word;'>长-学期数据保留</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>事件管理</td><td style='text-align: center; word-wrap: break-word;'>制定数据泄露管理计划，以更有效地应对数据泄露并管理数据集的丢失。该计划还应包括如何管理身份映射表或信息的丢失，这些信息可能允许将去识别/匿名数据恢复到其原始形式，从而导致丢失的数据被重新识别。有关事件管理的更多信息，请参阅下文。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr><tr><td rowspan="6">内部治理控制</td><td style='text-align: center; word-wrap: break-word;'>保留所有共享的去识别/匿名数据的中央注册表，以确保合并的共享数据不会导致重新识别去识别/匿名数据。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期对去识别/匿名数据。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>确保接受者（个人或部门）和使用去识别/匿名数据的目的已获得组织内相关部门的批准。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>禁止授权接收者（个人或部门）向任何未经授权的方共享去识别/匿名数据，或未经组织内相关当局批准试图重新识别数据。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>当其目的已经实现并且不再需要数据时，定期清除组织内的去识别/匿名数据。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>定期进行内部检查/审核，以确保符合流程。</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td></tr></table>

---

0

事件管理：组织应识别数据泄露的风险 $ ^{18} $涉及身份映射表、去识别数据和匿名数据，并将相关场景纳入其事件管理计划。以下注意事项可能与数据泄露报告和内部调查相关：

## 去标识化数据和标识映射表丢失

去识别化数据和身份管理表的破坏将类似于个人数据的破坏。在这种情况下，组织必须评估数据泄露是否需要通知，并根据数据泄露通知义务通知受影响的个人和/或委员会。

## 仅丢失去识别的数据

如果去标识化的数据在外部遭到破坏，则需要进行评估。组织必须评估数据泄露是否需要通知，因为去识别的数据具有更高的重新识别风险。但是，使用去标识化和其他保护措施来保护数据和身份映射表可以被视为组织实施的保护机制的一部分。

## 丢失匿名数据和身份映射表

组织必须评估重新识别的风险。如果确定为高，则组织必须确定数据泄露是否需要通知，并通知受影响的个人和/或委员会，根据数据泄露通知义务评估为需要通知。

## 仅丢失匿名数据

如果组织正确应用了匿名化技术，则无需将违规行为报告为应通报的违规行为。但是，它仍应继续调查该事件，以了解原因，以改进其内部保护措施，防止未来发生数据泄露事件。

## 仅丢失身份映射

如果使用身份映射表的数据集仍然受到保护，则组织无需报告违规行为，因为身份映射表本身不是个人数据。但是，组织应立即为其数据集生成新的假名和新的身份映射表。它还应该继续调查该事件，以了解原因，以改进其内部保护措施，防止未来发生数据泄露事件。

---

基本匿名指南

法律控制：组织应通过确保其匿名数据的第三方接收者将相关保护纳入共享匿名数据来保护自己，以最大程度地降低重新识别风险。下表中的良好实践取自PDPC的可信数据共享框架。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">法律控制</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（德-确定数据）</td><td style='text-align: center; word-wrap: break-word;'>内部的数据共享（匿名数据）</td><td style='text-align: center; word-wrap: break-word;'>外部的数据分享</td><td style='text-align: center; word-wrap: break-word;'>长-学期数据保留</td></tr><tr><td rowspan="3">数据共享协议</td><td style='text-align: center; word-wrap: break-word;'>确保数据仅用于允许的目的（例如，不向未经授权的方披露），并为违反合同分配责任。</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>禁止第三方接收者尝试重新识别已共享的匿名数据集。</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>根据组织的内部控制，确保第三方接收者遵守对共享匿名数据的相关保护。</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>不适用</td></tr></table>

---

## 4 

## 附件

---

## 附件 A：基本数据匿名技术


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">记录抑制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>记录抑制是指删除数据集中的整个记录。与大多数其他技术相比，该技术同时影响多个属性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>记录抑制用于删除唯一的或不符合其他标准的异常记录，例如k-匿名，来自匿名数据集。异常值可以导致轻松的重新识别。它可以在应用其他技术（例如泛化）之前或之后应用。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>删除整条记录。请注意，抑制应该是永久性的，而不仅仅是“隐藏行” $ ^{15} $功能；同样，如果基础数据仍然可以访问，“编辑”可能还不够。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>有关如何使用记录抑制的说明，请参阅泛化部分中的示例。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>请注意，删除记录可能会影响数据集（例如，在统计数据方面，例如平均值和中位数）。</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">字符掩蔽</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>字符屏蔽是指更改数据值的字符。这可以通过使用一致的符号（例如“*”或“x”）来完成。掩蔽通常仅应用于属性中的某些字符。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>当数据值是字符串并且隐藏其中的一部分足以提供所需的匿名程度时，使用字符掩码。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>根据属性的性质，用选定的符号替换适当的字符。根据属性类型，您可以决定替换固定数量的字符（例如信用卡号）或可变数量的字符（例如电子邮件地址）。</td></tr><tr><td rowspan="2">其他提示</td><td style='text-align: center; word-wrap: break-word;'>·请注意，屏蔽可能需要考虑原始数据的长度是否提供有关原始数据的信息。主题知识至关重要，特别是对于部分掩蔽以确保正确的字符被掩蔽。特殊考虑也可能适用于数据中的校验和；有时，可以使用校验和来恢复屏蔽数据的（其他部分）。至于完全屏蔽，除非数据的长度具有某种相关性，否则该属性也可以被抑制。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>·以数据主体旨在识别自己的数据的方式屏蔽数据的情况是一种特殊情况，不属于数据匿名化的通常目标。这方面的一个例子是发布幸运抽奖结果，其中通常会公布幸运抽奖获胜者的姓名和部分隐藏的NRIC号码，以便个人承认自己是获胜者。另一个例子是诸如个人信用卡号等信息在应用程序中被屏蔽或发给个人的声明。请注意，通常情况下，即使数据主体自己也无法识别匿名数据。</td></tr></table>

---

## 例子

此示例显示了一家在线杂货店从历史数据中对其交付需求进行研究以提高运营效率。该公司掩盖了邮政编码的最后4位数字，留下了前2位数字，它们对应于新加坡境内的“部门代码”。

## 匿名之前：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>邮政编码</td><td style='text-align: center; word-wrap: break-word;'>最喜欢的交货时间段</td><td style='text-align: center; word-wrap: break-word;'>平均每月订单数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>100111</td><td style='text-align: center; word-wrap: break-word;'>晚上8点至晚上9点</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>200222</td><td style='text-align: center; word-wrap: break-word;'>上午11点至中午12点</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>300333</td><td style='text-align: center; word-wrap: break-word;'>下午2点至3点</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>

## 部分屏蔽邮政编码后：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>邮政编码</td><td style='text-align: center; word-wrap: break-word;'>最喜欢的交货时间段</td><td style='text-align: center; word-wrap: break-word;'>平均每月订单数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>晚上8点至晚上9点</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20xxxx</td><td style='text-align: center; word-wrap: break-word;'>上午11点至中午12点</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>30xxxx</td><td style='text-align: center; word-wrap: break-word;'>下午2点至3点</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">化名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>假名化是指用虚构的值替换识别数据。它也被称为编码。当原始值被正确处理并且假名以不可重复的方式完成时，假名可能是不可逆的。当原始值被安全保存时，它们也可以是可逆的（由原始数据的所有者），但如果需要，可以检索并链接回假名 $ ^{16} $。</td></tr><tr><td rowspan="3">何时使用</td><td style='text-align: center; word-wrap: break-word;'>持久化假名允许通过使用相同的假名值来表示跨不同数据集的同一个人进行链接。但是，可以使用不同的假名来表示不同数据集中的同一个人，以防止不同数据集的链接。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>假名也可以随机或确定地生成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>当需要唯一区分数据值并且不保留有关原始属性的直接标识符的字符或任何其他隐含信息时，使用假名。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>用虚构的值替换相应的属性值。一种方法是预先生成一个组成值的列表，并从该列表中随机选择以替换每个原始值。虚构的值应该是唯一的，并且应该与原始值没有关系（以便可以从假名中得出原始值）。</td></tr></table>

---

## 其他提示

分配假名时，请确保不要重复使用已在同一数据集中使用过的假名，尤其是当它们是随机生成的时候。此外，避免在没有改变的情况下对多个属性使用完全相同的假名生成器（例如，至少使用不同的随机种子）。

• 持久化假名通常通过维护跨数据集的引用完整性来提供更好的效用。

对于可逆假名，身份映射表不能与接收者共享；它应该被安全保存，并且只能由组织在需要重新识别个人的情况下使用。

类似地，如果使用加密或散列函数对数据进行假名化，则必须安全保护散列的加密密钥或散列算法和盐值，以防止未经授权的访问。这是因为此类信息的泄漏可能会导致数据泄露，因为启用加密的反转或使用预先计算的表来推断经过哈希处理的数据（尤其是对于遵循预先确定的格式的数据，例如 NRIC）。

这同样适用于需要种子的伪随机数生成器。必须像使用任何其他类型的加密或可逆过程一样确保所使用的任何密钥的安全性 $ ^{17} $。组织还应定期审查加密方法（例如算法和密钥长度）和散列函数，以确保其被业界认可为相关且安全。

在某些情况下，假名可能需要遵循原始值的结构或数据类型（例如，假名可用于软件应用程序）；在这种情况下，可能需要特殊的假名生成器来创建合成数据集，或者在某些情况下，可以考虑所谓的“格式保留加密”，它会创建与原始数据具有相同格式的假名。

## 例子

这个例子显示了假名被应用于获得驾驶执照的人的名字和一些关于他们的信息。在此示例中，名称被替换为假名，而不是被隐藏的属性，因为组织希望能够在必要时扭转假名。

## 匿名之前：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>预评估结果</td><td style='text-align: center; word-wrap: break-word;'>通过之前的几个小时的课程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>乔攀</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>扎克林</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>余成三</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>林妮莫</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>杰斯琳·谭</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>陈秀利</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

17. 请注意，与使用标准的基于密钥的加密或散列相比，依赖专有或“秘密”反转过程（有或没有密钥）具有更大的被解码和破坏的风险。

---

<div style="text-align: center;">对 “Person” 属性进行假名化后：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>预评估结果</td><td style='text-align: center; word-wrap: break-word;'>通过之前的几个小时的课程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>416765</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>562396</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>964825</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>873892</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>239976</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>943145</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

对于可逆的假名化，身份映射表被安全保存，以防将来有合法的需要重新识别个人。还应使用安全控制（包括管理和技术控制）来保护身份映射表。

<div style="text-align: center;">身份映射表（单编码）：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>笔名</td><td style='text-align: center; word-wrap: break-word;'>人</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>416765</td><td style='text-align: center; word-wrap: break-word;'>乔攀</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>562396</td><td style='text-align: center; word-wrap: break-word;'>扎克林</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>964825</td><td style='text-align: center; word-wrap: break-word;'>余成三</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>873892</td><td style='text-align: center; word-wrap: break-word;'>林妮莫</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>239976</td><td style='text-align: center; word-wrap: break-word;'>杰斯琳·谭</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>943145</td><td style='text-align: center; word-wrap: break-word;'>陈秀利</td></tr></table>

为了增加身份映射表的安全性，可以使用双重编码。继上一个示例之后，此示例显示了附加的链接表，该链接表放置在受信任的第三方处。使用双重编码，只有当受信任的第三方（拥有链接表）和组织（拥有身份映射表）将他们的数据放在一起时，才能知道个人的身份。

<div style="text-align: center;">匿名化后：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>预评估结果</td><td style='text-align: center; word-wrap: break-word;'>通过之前的几个小时的课程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>373666</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>594824</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>839933</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>280074</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>746791</td><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>785282</td><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

---

## 链接表（仅由受信任的第三方安全保存，甚至组织最终也会将其删除。第三方没有得到任何其他信息）：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>笔名</td><td style='text-align: center; word-wrap: break-word;'>临时笔名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>373666</td><td style='text-align: center; word-wrap: break-word;'>OQCPBL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>594824</td><td style='text-align: center; word-wrap: break-word;'>ALGKTY</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>839933</td><td style='text-align: center; word-wrap: break-word;'>CGFFNF</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>280074</td><td style='text-align: center; word-wrap: break-word;'>BZMHCP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>746791</td><td style='text-align: center; word-wrap: break-word;'>RTJYGR</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>785282</td><td style='text-align: center; word-wrap: break-word;'>RCNVJD</td></tr></table>

<div style="text-align: center;">身份映射表（由组织安全保存）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>临时笔名</td><td style='text-align: center; word-wrap: break-word;'>人</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OQCPBL</td><td style='text-align: center; word-wrap: break-word;'>乔攀</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ALGKTY</td><td style='text-align: center; word-wrap: break-word;'>扎克林</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CGFFNF</td><td style='text-align: center; word-wrap: break-word;'>余成三</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BZMHCP</td><td style='text-align: center; word-wrap: break-word;'>林妮莫</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RTJYGR</td><td style='text-align: center; word-wrap: break-word;'>杰斯琳·谭</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RCNVJD</td><td style='text-align: center; word-wrap: break-word;'>陈秀利</td></tr></table>

注意：在链接表和恒等映射表中，最好打乱记录的顺序，而不是保持与数据集相同的顺序。在此示例中，两个表中的记录都按原始顺序保留，以便于可视化。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">概括</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>泛化是故意降低数据的精度。示例包括将人的年龄转换为年龄范围或将精确位置转换为不太精确的位置。这种技术也称为重新编码。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>泛化用于可以泛化但仍可用于预期目的的值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它化）。</td><td style='text-align: center; word-wrap: break-word;'>为翻译数据设计适当的数据类别和规则。考虑隐藏在翻译后仍然突出的任何记录（即泛化）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>选择适当的数据范围。数据范围太大可能意味着数据效用的重大损失，而数据范围太小可能意味着数据几乎没有被修改，因此仍然很容易重新识别。如果 $ k $-使用匿名， $ k $选择的值也会影响数据范围。请注意，第一个和最后一个范围可能是一个更大的范围，以容纳这些末端通常较少的记录数；这通常被称为顶部/底部编码。</td></tr></table>

---

## 例子

在这个例子中，数据集包含人的姓名（已经化名）、他们的年龄和居住地址。

<div style="text-align: center;">匿名之前：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序列号</td><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>357703</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>700大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>233121</td><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>800宏茂桥大道12号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>938637</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>900裕廊东街70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>591493</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>750大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>202626</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>5淡滨尼街90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>888948</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>巨石阵路1号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>175878</td><td style='text-align: center; word-wrap: break-word;'>28</td><td style='text-align: center; word-wrap: break-word;'>10淡滨尼街90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>312304</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>50裕廊东街70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>214025</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>720大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>271714</td><td style='text-align: center; word-wrap: break-word;'>37</td><td style='text-align: center; word-wrap: break-word;'>830宏茂桥大道12号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>341338</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>15淡滨尼街90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>529057</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>18淡滨尼街90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>390438</td><td style='text-align: center; word-wrap: break-word;'>39</td><td style='text-align: center; word-wrap: break-word;'>840宏茂桥大道12号</td></tr></table>

对于 “年龄” 属性，采用的方法是概括为以下年龄范围。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>&lt;20</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>51-60</td><td style='text-align: center; word-wrap: break-word;'>&gt;60</td></tr></table>

对于 “地址”，一种可能的方法是删除街区/门牌号并仅保留道路名称。

<div style="text-align: center;">在概括“年龄”和“地址”属性后：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序列号</td><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>357703</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>233121</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>宏茂桥大道12号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>938637</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>裕廊东街70号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>591493</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>202626</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>淡滨尼街90号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>888948</td><td style='text-align: center; word-wrap: break-word;'>&gt;60</td><td style='text-align: center; word-wrap: break-word;'>巨石阵路</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>175878</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>淡滨尼街90号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>312304</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>裕廊东街70号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>214025</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>大巴窑罗弄5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>271714</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>宏茂桥大道12号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>341338</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>淡滨尼街90号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>529057</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>淡滨尼街90号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>390438</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>宏茂桥大道12号</td></tr></table>

---

例如，假设巨石阵路上实际上只有一个住宅单元。即使数据经过了泛化，也可以推导出确切的地址。这可以被认为是“太独特了”。

因此，作为概括的下一步，可以删除记录6（即使用记录抑制技术），因为在删除单元编号后地址仍然“太唯一”。或者，所有地址都可以在更大程度上被概括（例如城镇或地区），从而不需要抑制。但是，这可能会影响数据的实用性，而不是从数据集中抑制一些记录。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">交换</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>交换的目的是重新排列数据集中的数据，使得单个属性的值仍然在数据集中表示，但通常与原始记录不对应。这种技术也称为改组和排列。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>当后续分析只需要查看聚合数据或分析处于属性内级别时，使用交换；换句话说，不需要在记录级别分析属性之间的关系。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>首先，确定要交换的属性。然后，对于属性中的每个值，将值交换或重新分配给数据集中的其他记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>· 评估并决定需要交换哪些属性（列）。根据情况，组织可能会决定，例如，只有包含相对可识别的值的属性（列）需要交换。</td></tr></table>

## 例子

在此示例中，数据集包含有关业务组织的客户记录的信息。匿名之前：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>职称</td><td style='text-align: center; word-wrap: break-word;'>出生日期</td><td style='text-align: center; word-wrap: break-word;'>会员类型</td><td style='text-align: center; word-wrap: break-word;'>每月平均访问量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>大学讲师</td><td style='text-align: center; word-wrap: break-word;'>1970年1月3日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>推销员</td><td style='text-align: center; word-wrap: break-word;'>1972年2月5日</td><td style='text-align: center; word-wrap: break-word;'>铂</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>律师</td><td style='text-align: center; word-wrap: break-word;'>1985年3月7日</td><td style='text-align: center; word-wrap: break-word;'>金子</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>IT专业人士</td><td style='text-align: center; word-wrap: break-word;'>1990年4月10日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>护士</td><td style='text-align: center; word-wrap: break-word;'>1995年5月13日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr></table>

## 匿名化后：

在此示例中，所有属性的所有值都已交换。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>职称</td><td style='text-align: center; word-wrap: break-word;'>出生日期</td><td style='text-align: center; word-wrap: break-word;'>会员类型</td><td style='text-align: center; word-wrap: break-word;'>每月平均访问量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>一种</td><td style='text-align: center; word-wrap: break-word;'>律师</td><td style='text-align: center; word-wrap: break-word;'>1990年4月10日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>护士</td><td style='text-align: center; word-wrap: break-word;'>1985年3月7日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>推销员</td><td style='text-align: center; word-wrap: break-word;'>1995年5月13日</td><td style='text-align: center; word-wrap: break-word;'>铂</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>IT专业人士</td><td style='text-align: center; word-wrap: break-word;'>1970年1月3日</td><td style='text-align: center; word-wrap: break-word;'>银</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>乙</td><td style='text-align: center; word-wrap: break-word;'>大学讲师</td><td style='text-align: center; word-wrap: break-word;'>1972年2月5日</td><td style='text-align: center; word-wrap: break-word;'>金子</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

注意：另一方面，如果匿名数据集的目的是研究工作概况和消费模式之间的关系，那么其他匿名化方法可能更合适（例如.职称的泛化，这可能导致“大学讲师”被修改为“教育者”）。

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">数据扰动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>原始数据集中的值被修改为略有不同。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>数据扰动用于间接标识符（通常是数字和日期），当与其他数据源结合时可能可以识别，但属性值的微小变化是可以接受的。在数据准确性至关重要的情况下，不应使用此技术。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>这取决于所使用的确切数据扰动技术。这些包括舍入和添加随机噪声。本节中的示例显示 base-x 舍入。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>• 扰动程度应与属性值的范围成比例。如果基数太小，匿名化效果会变弱；另一方面，如果基数太大，最终值将与原始值相差太大，数据集的效用可能会降低。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>• 请注意，在对之前已被扰动的属性值执行计算的情况下，结果值可能会受到更大程度的扰动。</td></tr></table>

## 例子

在这个例子中，数据集包含用于研究一个人的身高、体重、年龄、这个人是否吸烟以及这个人是否患有“疾病A”和/或“疾病B”之间的可能联系的信息。此人的姓名已被化名。

## 然后应用以下舍入：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>属性</td><td style='text-align: center; word-wrap: break-word;'>匿名技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高度（厘米）</td><td style='text-align: center; word-wrap: break-word;'>以5为底的四舍五入（选择5，与120到190厘米的典型高度值有些比例）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>重量（公斤）</td><td style='text-align: center; word-wrap: break-word;'>Base-3四舍五入（选择3，与40到100kg的典型重量值有些比例）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年龄（年）</td><td style='text-align: center; word-wrap: break-word;'>以3为底的四舍五入（选择3，与10到100岁的典型年龄值有些比例）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>剩余属性</td><td style='text-align: center; word-wrap: break-word;'>无，因为它们是非数字的，并且很难在不改变值的情况下进行修改。</td></tr></table>

---

<div style="text-align: center;">匿名化前的数据集：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>高度（厘米）</td><td style='text-align: center; word-wrap: break-word;'>重量（公斤）</td><td style='text-align: center; word-wrap: break-word;'>年龄（岁）</td><td style='text-align: center; word-wrap: break-word;'>抽烟？</td><td style='text-align: center; word-wrap: break-word;'>疾病A？</td><td style='text-align: center; word-wrap: break-word;'>疾病B？</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>198740</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>287402</td><td style='text-align: center; word-wrap: break-word;'>177</td><td style='text-align: center; word-wrap: break-word;'>70</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>398747</td><td style='text-align: center; word-wrap: break-word;'>158</td><td style='text-align: center; word-wrap: break-word;'>46</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>498732</td><td style='text-align: center; word-wrap: break-word;'>173</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>598772</td><td style='text-align: center; word-wrap: break-word;'>169</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr></table>

<div style="text-align: center;">匿名化后的数据集：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>人</td><td style='text-align: center; word-wrap: break-word;'>高度（厘米）</td><td style='text-align: center; word-wrap: break-word;'>重量（公斤）</td><td style='text-align: center; word-wrap: break-word;'>年龄（岁）</td><td style='text-align: center; word-wrap: break-word;'>抽烟？</td><td style='text-align: center; word-wrap: break-word;'>疾病A？</td><td style='text-align: center; word-wrap: break-word;'>疾病B？</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>198740</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>51</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>287402</td><td style='text-align: center; word-wrap: break-word;'>175</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>398747</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>45</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>498732</td><td style='text-align: center; word-wrap: break-word;'>175</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>不</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>598772</td><td style='text-align: center; word-wrap: break-word;'>170</td><td style='text-align: center; word-wrap: break-word;'>81</td><td style='text-align: center; word-wrap: break-word;'>42</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td><td style='text-align: center; word-wrap: break-word;'>是的</td></tr></table>

注意：对于 base-x 舍入，要舍入的属性值会舍入到最接近的 x 倍数。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">数据聚合</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>数据聚合是指将数据集从记录列表转换为汇总值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时用它</td><td style='text-align: center; word-wrap: break-word;'>当不需要单独的记录并且汇总数据足以达到目的时使用它。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何用它</td><td style='text-align: center; word-wrap: break-word;'>统计测量的详细讨论超出了本指南的范围，但是典型的方法包括使用总数或平均值等。与数据接收者讨论预期效用并找到合适的折衷方案也可能很有用。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>· 如果适用，请注意执行聚合后记录太少的组。在下面的示例中，如果聚合数据包含任何类别中的单个记录，则具有一些额外知识的人可能很容易识别捐赠者。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>· 因此，聚合可能需要与抑制结合使用。某些属性可能需要删除，因为它们包含无法聚合的详细信息，并且可能需要添加新属性（例如，包含新计算的聚合值）。</td></tr></table>

---

## 例子

在此示例中，慈善组织有捐赠记录，以及有关捐赠者的一些信息。

慈善组织评估聚合数据足以让外部顾问进行数据分析，因此对原始数据集进行了数据聚合。

<div style="text-align: center;">原始数据集：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>捐赠者</td><td style='text-align: center; word-wrap: break-word;'>月收入（$）</td><td style='text-align: center; word-wrap: break-word;'>2016年捐赠金额（美元）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者A</td><td style='text-align: center; word-wrap: break-word;'>4000</td><td style='text-align: center; word-wrap: break-word;'>210</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者B</td><td style='text-align: center; word-wrap: break-word;'>4900</td><td style='text-align: center; word-wrap: break-word;'>420</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者C</td><td style='text-align: center; word-wrap: break-word;'>2200</td><td style='text-align: center; word-wrap: break-word;'>150</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者D</td><td style='text-align: center; word-wrap: break-word;'>4200</td><td style='text-align: center; word-wrap: break-word;'>110</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者E</td><td style='text-align: center; word-wrap: break-word;'>5500</td><td style='text-align: center; word-wrap: break-word;'>260</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者F</td><td style='text-align: center; word-wrap: break-word;'>2600</td><td style='text-align: center; word-wrap: break-word;'>40</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者G</td><td style='text-align: center; word-wrap: break-word;'>3300</td><td style='text-align: center; word-wrap: break-word;'>130</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者H</td><td style='text-align: center; word-wrap: break-word;'>5500</td><td style='text-align: center; word-wrap: break-word;'>210</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者我</td><td style='text-align: center; word-wrap: break-word;'>1600</td><td style='text-align: center; word-wrap: break-word;'>380</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者J</td><td style='text-align: center; word-wrap: break-word;'>3200</td><td style='text-align: center; word-wrap: break-word;'>80</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者K</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>440</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者L</td><td style='text-align: center; word-wrap: break-word;'>5800</td><td style='text-align: center; word-wrap: break-word;'>400</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者M</td><td style='text-align: center; word-wrap: break-word;'>4600</td><td style='text-align: center; word-wrap: break-word;'>390</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者N</td><td style='text-align: center; word-wrap: break-word;'>1900</td><td style='text-align: center; word-wrap: break-word;'>480</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者O</td><td style='text-align: center; word-wrap: break-word;'>1700</td><td style='text-align: center; word-wrap: break-word;'>320</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者P</td><td style='text-align: center; word-wrap: break-word;'>2400</td><td style='text-align: center; word-wrap: break-word;'>330</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者Q</td><td style='text-align: center; word-wrap: break-word;'>4300</td><td style='text-align: center; word-wrap: break-word;'>390</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者R</td><td style='text-align: center; word-wrap: break-word;'>2300</td><td style='text-align: center; word-wrap: break-word;'>260</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者小号</td><td style='text-align: center; word-wrap: break-word;'>3500</td><td style='text-align: center; word-wrap: break-word;'>80</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>捐助者T</td><td style='text-align: center; word-wrap: break-word;'>1700</td><td style='text-align: center; word-wrap: break-word;'>290</td></tr></table>

<div style="text-align: center;">匿名数据集：</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>月收入（$）</td><td style='text-align: center; word-wrap: break-word;'>收到的捐款数量（2016年）</td><td style='text-align: center; word-wrap: break-word;'>2016年捐款总额（美元）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1000-1999</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1470</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2000-2999</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1220</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3000-3999</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>290</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4000-4999</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1520</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5000-6000</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>870</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>5370</td></tr></table>

---

## 附件 B：常见数据属性和建议的匿名技术

## 直接标识符

下表提供了有关可应用于某些常见类型的直接标识符的匿名化技术的建议。通常，直接标识符应被禁止（删除）或化名。如果需要分配假名，通常每个数据集一组（即一列）假名就足够了。

对于合成数据用例，可以保留所有直接标识符列，但必须用假名值替换。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">记录抑制</td><td rowspan="2">常用技术</td><td colspan="2">例子</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前</td><td style='text-align: center; word-wrap: break-word;'>后</td></tr><tr><td rowspan="4">• 姓名• 电子邮件地址• 手机数字• 身份证号码• 护照数字• 帐户数字• 出生证明数字• 外国的鉴别号码 (FIN)• 工作准证数字</td><td style='text-align: center; word-wrap: break-word;'>属性抑制</td><td style='text-align: center; word-wrap: break-word;'>约翰·谭</td><td style='text-align: center; word-wrap: break-word;'>（已删除）</td></tr><tr><td colspan="3">分配假名，例如：</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• 用唯一的随机值替换直接标识符值；要么</td><td style='text-align: center; word-wrap: break-word;'>约翰·谭</td><td style='text-align: center; word-wrap: break-word;'>123456</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• 将直接标识符值替换为遵循数据格式的随机生成的值。</td><td style='text-align: center; word-wrap: break-word;'>John.tan@gmail.comS8822311H</td><td style='text-align: center; word-wrap: break-word;'>123456@abc.comS8512345A</td></tr></table>

## 间接标识符

下表提供了有关可应用于某些常见类型的间接标识符的匿名化技术的建议。您应该选择将一种或多种技术应用于每个间接标识符（例如，根据您的用例应用泛化和交换年龄）。

对于合成数据用例，两种有用的技术是数据交换和数据扰动。这些适用于所有间接标识符。

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">间接身份标识）</td><td rowspan="2">常用技术</td><td colspan="2">例子）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前</td><td style='text-align: center; word-wrap: break-word;'>后</td></tr><tr><td rowspan="3">·年龄·高度·重量</td><td style='text-align: center; word-wrap: break-word;'>概括：将年龄/身高/体重概括为5或10岁/cm/kg的范围。</td><td rowspan="3">记录#1：24记录#2：39记录#3：18</td><td style='text-align: center; word-wrap: break-word;'>概括（5岁年龄范围）：记录#1：21到25记录#2：36到40记录#3：16到20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据扰动：将随机值(+/-5)添加到原始值。</td><td style='text-align: center; word-wrap: break-word;'>数据扰动：记录#1：25记录#2：36记录#3：17</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换与每条记录关联的年龄/身高/体重。</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：39记录#2：18记录#3：24</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>·性别</td><td style='text-align: center; word-wrap: break-word;'>这种间接数据属性通常只有两个通用的非标识值—M或F，因此，按原样保留通常是安全的。对于合成数据用例，可以将以下技术进一步应用于该属性。交换：在数据集中随机切换性别。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：M记录#2：M记录#3：F记录#4：M</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：M记录#2：F记录#3：M记录#4：M</td></tr><tr><td rowspan="2">·种族·婚姻状态</td><td style='text-align: center; word-wrap: break-word;'>概括：根据您的数据集，您可以将选定的种族群体或婚姻状况组合并概括为标记为“其他”的类别。如果您的数据集中存在独特的种族群体/婚姻状况或相同种族群体/婚姻状况的太少，则需要执行此操作。</td><td rowspan="2">记录#1：印度记录#2：中文记录#3：中文记录#4：马来语记录#5：欧亚大陆</td><td style='text-align: center; word-wrap: break-word;'>概括：记录#1：其他记录#2：中文记录#3：中文记录#4：其他记录#5：其他</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的种族或婚姻状况。</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：马来语记录#2：中文记录#3：印度记录#4：欧亚大陆记录#5：中文</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3">•日期出生</td><td style='text-align: center; word-wrap: break-word;'>概括：将出生日期概括为年份或月份和年份。</td><td rowspan="3">记录#1：2003年2月1日记录#2：1990年8月15日记录#3：1998年12月30日</td><td style='text-align: center; word-wrap: break-word;'>概括（年月）：记录#1：2003年2月记录#2：1990年8月记录#3：1998年12月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据扰动：随机修改日期（例如+/-原始日期后30天）。</td><td style='text-align: center; word-wrap: break-word;'>数据扰动：记录#1：2003年1月20日记录#2：1990年8月18日记录#3：1999年1月6日</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的日期。</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：1998年12月30日记录#2：2003年2月1日记录#3：1990年8月15日</td></tr><tr><td rowspan="3">•地址</td><td style='text-align: center; word-wrap: break-word;'>概括：将地址概括为预定义区域（例如参考市区重建局（URA）的总体规划18）。</td><td style='text-align: center; word-wrap: break-word;'>榜鹈中央71号，新加坡828755</td><td style='text-align: center; word-wrap: break-word;'>概括：榜鹈</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：在数据集中随机切换地址。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：榜鹈中央71号，#10-1122，新加坡828755</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：曼德勒路35号，#13-37新加坡208215</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>注意：对于地址，单元号可能是识别性的。如果不需要，应从数据集中删除单元编号。</td><td style='text-align: center; word-wrap: break-word;'>记录#2：曼德勒路35号，#13-37新加坡208215</td><td style='text-align: center; word-wrap: break-word;'>记录#2：榜鹈中央71号，#10-1122，新加坡828755</td></tr><tr><td rowspan="2">•邮政代码</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：屏蔽邮政编码的最后四位数字。（新加坡有80个邮区）。</td><td style='text-align: center; word-wrap: break-word;'>117438</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：11xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的邮政编码。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：117438记录#2：828755</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：828755记录#2：117438</td></tr><tr><td rowspan="2">•职称</td><td style='text-align: center; word-wrap: break-word;'>概括：没有简单的方法可以自动匿名化职位名称，因为职位名称是非标准，组织可以自己发明。一种方法是将职称概括为工作性质和/或工作级别的预定义分类。但是，映射可能必须手动完成。</td><td style='text-align: center; word-wrap: break-word;'>首席执行官团队负责人，软件发展</td><td style='text-align: center; word-wrap: break-word;'>概括：C级官员IT经理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的职位。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：首席执行官记录#2：导演记录#3：经理</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：经理记录#2：CEO记录#3：导演</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">公司姓名</td><td style='text-align: center; word-wrap: break-word;'>概括：将公司名称概括为行业部门（例如参考新加坡标准工业分类(SSIC)） $ ^{19} $.</td><td style='text-align: center; word-wrap: break-word;'>快速的士有限公司</td><td style='text-align: center; word-wrap: break-word;'>概括：运输和贮存</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的公司名称。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：Speedy Taxi Ltd记录#2：最佳食品有限公司记录#3：No. 1 ColdWear Pte Ltd</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：最佳食品有限公司记录#2：No. 1 ColdWear Pte Ltd记录#3：Speedy Taxi Ltd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IP地址</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：屏蔽最后两个八位字节 $ _{20} $IPv4 IP地址和 IPv6 IP地址的最后80位。注意：除了字符屏蔽之外，还可以应用交换。</td><td style='text-align: center; word-wrap: break-word;'>IPv4：12.120.210.88IPv6：2001:0db8:85a3:0000:0000:8a2e:0370:7334</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：IPv4：12.120.xxx.xxxIPv6：2001:0db8:85a3:xxxx-xxxx:xxxx:xxxx:xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>车辆执照盘子数字</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：屏蔽车牌号的最后四个字符。注意：除了字符屏蔽之外，还可以应用交换。</td><td style='text-align: center; word-wrap: break-word;'>SMF1234A</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：SMF1xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>车载单位(IU)数字</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：屏蔽 IU 编号的最后三位。注意：除了字符屏蔽之外，还可以应用交换。</td><td style='text-align: center; word-wrap: break-word;'>1234567890</td><td style='text-align: center; word-wrap: break-word;'>字符掩码：1234567xxxx</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3">• 全球的定位系统\n(全球定位系统)地点</td><td style='text-align: center; word-wrap: break-word;'>概括：将 GPS 坐标（十进制度）四舍五入到最接近的两位小数（相当于 1.11 km 的精度）或三位小数（相当于 111 m 的精度）。</td><td style='text-align: center; word-wrap: break-word;'>1.27434, 103.79967</td><td style='text-align: center; word-wrap: break-word;'>概括：1.274, 103.800（十进制度数四舍五入到小数点后三位）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据扰动：添加介于 0.005 和 -0.005 或 0.0005 和 -0.0005 之间的随机值。</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>数据扰动：1.27834, 103.79767</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：随机切换数据集中的 GPS 位置值。</td><td style='text-align: center; word-wrap: break-word;'>记录#1：1.27434, 103.79967\n记录#2：1.26421, 103.80405\n记录#3：1.26463, 103.82226</td><td style='text-align: center; word-wrap: break-word;'>交换：记录#1：1.26463, 103.82226\n记录#2：1.27434, 103.79967\n记录#3：1.26421, 103.80405</td></tr></table>

## 目标属性

目标属性是专有信息，对于数据实用程序而言非常重要。因此，对于大多数用例，匿名化技术不适用于目标属性。但是，对于合成数据用例，由于记录级数据通常用于可能未得到适当保护的开发和测试环境，因此建议对目标属性应用一种或多种匿名技术，以确保不会重新识别将在数据泄露的情况下进行。

重要的是要检查并确保在应用匿名化技术后，合成数据集中的任何记录都不会与原始数据集中的任何记录相似。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">目标属性</td><td rowspan="2">常用技术</td><td colspan="2">例子）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前</td><td style='text-align: center; word-wrap: break-word;'>后</td></tr><tr><td rowspan="4">• 交易• 薪水• 信用评级• 保险政策• 医疗的诊断• 疫苗接种状态</td><td style='text-align: center; word-wrap: break-word;'>数据扰动：随意修改数值数据（例如从原始数据中添加或减去随机值）。数据扰动是不可能的字母数字或</td><td style='text-align: center; word-wrap: break-word;'>购买价值：38.05 美元薪水：6,200 美元</td><td style='text-align: center; word-wrap: break-word;'>数据扰动：购买价值：42 美元薪水：7,500 美元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>非结构化文本数据。</td><td rowspan="3">疫苗接种状态：记录#1：接种疫苗记录#2：第一剂记录#3：未接种疫苗</td><td rowspan="3">交换：疫苗接种状态：记录#1：第一剂记录#2：未接种疫苗记录#3：接种疫苗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交换：在数据集中随机切换数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>注意：除了数据扰动之外，还可以应用交换。</td></tr></table>

---

## 附件 C: k-匿名

k-匿名（以及类似的扩展，如l-多样性和吨-closeness）是一种用于确保未超过风险阈值的措施，作为匿名化方法的一部分。

k-匿名不是唯一可用的措施，也不是没有限制，但它相对容易理解且易于应用。k-匿名可能不适用于所有类型的数据集或其他复杂用例。其他方法和/或工具，例如特殊唯一检测算法(SUDA)和μ-Argus，可能更适合评估大型数据集的风险。替代方法，例如差分隐私 $ ^{21} $，在过去几年中也出现了。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">k-匿名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>这k-匿名模型在应用匿名技术（例如泛化）之前用作指南，也用于验证之后，以确保任何记录的间接标识符至少被共享k-1其他记录。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>这是由提供的关键保护k-匿名反对链接攻击，因为k记录（或至少不同的间接标识符）在它们的识别属性上是相同的，因此，创建一个等价类22和k成员。因此，不可能链接或挑选出个人的记录，因为总是有k相同的属性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>匿名数据集可能有不同的k-不同组间接标识符的匿名级别，但对于链接的“最大风险”保护，最低k用作与阈值进行比较的代表值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>何时使用</td><td style='text-align: center; word-wrap: break-word;'>k-匿名性用于确认实施的匿名化措施达到了针对链接攻击的预期阈值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如何使用它</td><td style='text-align: center; word-wrap: break-word;'>首先，确定一个值k（等于或大于等价类大小的倒数），它提供了最低k在所有等价类中实现。一般来说，价值越高k，数据主体越难被识别；然而，效用可能会降低，因为k增加和更多的记录可能需要被禁止。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应用匿名化技术后，检查每条记录是否至少包含k-1具有相同属性的其他记录k-匿名化。等价类中的记录小于k应考虑压制记录；或者，可以进一步匿名数据集。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他提示</td><td style='text-align: center; word-wrap: break-word;'>• 除了泛化和抑制之外，还可以创建合成数据来实现k-匿名。这些技术（和其他技术）有时可以组合使用，但请注意所选的特定方法可能会影响数据效用。考虑在删除异常值或插入合成数据之间进行权衡。• k-匿名假设每条记录都与不同的个人有关。如果同一个人有多个记录（例如多次访问医院），那么k-匿名性需要高于重复记录，否则这些记录可能不仅是可链接的，而且可能也可以重新识别，尽管看起来很充实“k等价类”。</td></tr></table>

21. 差分隐私涉及多个概念，包括回答查询而不是提供匿名数据集、为保护个人记录添加随机噪声、提供不超过预定义“隐私预算”的数学保证等。

22. “等价类”是指数据集中在某些属性中共享相同值的记录，通常是间接标识符。

---

## 例子

在此示例中，数据集包含有关乘坐出租车的人的信息。

₫=使用 5（即在匿名化后，每个记录最终应该与其他四个记录共享相同的属性）。

以下匿名化技术组合使用。粒度级别是实现所需的一种方法k等级。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>属性</td><td style='text-align: center; word-wrap: break-word;'>匿名技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>概括（10 年间隔）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>职业</td><td style='text-align: center; word-wrap: break-word;'>泛化（例如，“数据库管理员”和“程序员”都泛化为“IT”）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>记录抑制</td><td style='text-align: center; word-wrap: break-word;'>在应用匿名技术（在本例中为泛化）后不符合5匿名标准的记录将被删除。例如，银行家的记录被删除，因为它是“职业”下唯一的此类值。</td></tr></table>

## 匿名化前的数据集：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>串行数字</td><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>性别</td><td style='text-align: center; word-wrap: break-word;'>职业</td><td style='text-align: center; word-wrap: break-word;'>平均人数每周旅行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>助理资料保护主任</td><td style='text-align: center; word-wrap: break-word;'>15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>38</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>首席IT顾问</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>银行家</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>34</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>数据库管理员</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>首席隐私官</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>区域数据保护官</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>38</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>程序员</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>IT分析师</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>副数据保护官</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>DPO办公室经理</td><td style='text-align: center; word-wrap: break-word;'>11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>用户体验设计师</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

---

在匿名化年龄和职业并抑制异常值后，数据集变为 5-匿名。（相应的等价类以不同的颜色突出显示）：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>串行数字</td><td style='text-align: center; word-wrap: break-word;'>年龄</td><td style='text-align: center; word-wrap: break-word;'>性别</td><td style='text-align: center; word-wrap: break-word;'>职业</td><td style='text-align: center; word-wrap: break-word;'>平均数每周出行次数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>数据保护官</td><td style='text-align: center; word-wrap: break-word;'>15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>31至40</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>它</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性—</td><td style='text-align: center; word-wrap: break-word;'>银行家</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>31至40</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>它</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>数据保护官</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>数据保护官</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>31至40</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>它</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>31至40</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>它</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>数据保护官</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>21至30</td><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>数据保护官</td><td style='text-align: center; word-wrap: break-word;'>11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>31至40</td><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>它</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

注：每周平均出行次数以目标属性为例，不含nee

恩多特uhrteh埃弗雷尔瑙格尼姆姆btehrisoaftttrrip这里以ibsuptee.rweek作为目标属性的示例，没有需要进一步匿名此属性。

---

## 附件 D：评估重新识别的风险

有多种方法可以评估重新识别的风险，这些方法可能需要相当复杂的计算，包括概率计算。

本节描述了一个简化的模型，使用k-匿名27，并做出以下假设：

1 发布模型是非公开的；

攻击者有动机将个人链接到匿名数据集；和

匿名数据的内容没有被考虑在内，并且计算的风险与攻击者实际可用的信息类型无关。

首先，应建立风险阈值。该值反映了一个概率，介于 0 和 1 之间。它反映了组织愿意接受的风险级别。影响风险阈值的主要因素应包括可能对数据主体造成的伤害，以及如果发生重新识别对组织的伤害；但是，它还考虑了为减轻任何残余风险而采取的其他控制措施。潜在危害越高，风险阈值就应该越高。对于应该使用什么风险阈值没有硬性规定；以下只是示例。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>潜在危害</td><td style='text-align: center; word-wrap: break-word;'>风险阈值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>低的</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>中等的</td><td style='text-align: center; word-wrap: break-word;'>0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高的</td><td style='text-align: center; word-wrap: break-word;'>0.01</td></tr></table>

23.例如，如果使用差异隐私或传统的统计披露控制进行计算，则计算会有所不同。

---

在计算重新识别风险时，本指南使用“检察官风险”，它假设攻击者认识数据集中的特定人，并试图确定数据集中的哪条记录与该人有关。

计算数据集中单个记录的重新识别概率的简单规则是取记录的等价类大小的倒数：

 $$  P( 将个人链接到单个记录 )=1/ 记录的等价类大小 $$ 

为了计算重新识别整个数据集中任何记录的概率，假设存在重新识别尝试，保守的方法是将其等同于数据集中所有记录中重新识别的最大概率。

 $$  P( 重新识别数据集中的任何记录 )=1/Min。数据集中的等价类大小 $$ 

 $$  注意：如果数据集已经被 k 匿名化 , $$ 

 $$ P( 重新识别数据集中的任何记录 )<=1/k $$ 

我们可以考虑三种有动机的入侵者攻击场景：

1. 蓄意的内线攻击；

2. 不经意间被熟人认出；和

3. 数据泄露。

P (re-ID) = P (re-ID | re-ID 尝试) x P (re-ID 尝试)
其中 P (re-ID | re-ID attempt) 是指在有重新识别尝试的情况下成功重新识别的概率。如前所述，我们可以将 P (re-ID | re-ID attempt) 设为 (1 / Min. equivalence class size in dataset)
因此，P (re-ID) = (1 / Min. equivalence class size in dataset) x P (re-ID attempt)

---

对于场景 #1，蓄意的内部攻击，我们假设接收数据集的一方尝试重新识别。估计 P（重新识别尝试）：重新识别尝试的概率，要考虑的因素包括减轻控制的程度以及攻击者的动机和资源。下表显示了示例值；同样，由匿名数据集的一方来决定要使用的合适值。

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_474_223_548.jpg" alt="Image" width="5%" /></div>


场景 #1——蓄意的内部攻击 P（re-ID 尝试）= P（内部攻击）


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2"></td><td style='text-align: center; word-wrap: break-word;'>低的</td><td style='text-align: center; word-wrap: break-word;'>中等的</td><td style='text-align: center; word-wrap: break-word;'>高的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>高的</td><td style='text-align: center; word-wrap: break-word;'>0.03</td><td style='text-align: center; word-wrap: break-word;'>0.05</td><td style='text-align: center; word-wrap: break-word;'>0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>缓解程度</td><td style='text-align: center; word-wrap: break-word;'>中等的</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.25</td><td style='text-align: center; word-wrap: break-word;'>0.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>控制</td><td style='text-align: center; word-wrap: break-word;'>低的</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>没有</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>1.0</td></tr></table>

影响攻击者动机和资源的因素可能包括：

1

违反合同的意愿（假设有防止重新识别的合同）



2

财务和时间限制



在数据集中包含知名人士（例如名人）或敏感数据（例如信用信息）

易于访问“可链接”数据或信息，无论是公开的还是私有的，都可以重新识别匿名数据集

影响缓解控制程度的因素包括：

1 组织结构

2 行政/法律控制（例如合同）

3 技术和过程控制

---

对于场景 #2，熟人的无意识别，我们假设接收数据集的一方在检查数据集时无意中重新识别了数据主体。这是可能的，因为一方由于他们的关系（例如朋友、邻居、亲戚、同事等）而对数据主体有一些额外的知识。估计P（re-ID尝试）：重新识别尝试的概率，要考虑的主要因素是数据接收者认识数据集中某人的可能性。

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_473_223_548.jpg" alt="Image" width="5%" /></div>


情景#2——熟人无意中认出

P（重新识别尝试）= P（数据接收者认识数据集中的人）

对于场景#3，数据接收方的ICT系统发生数据泄露的概率可以根据数据接收方行业中数据泄露流行率的可用统计数据进行估算。这是基于获得数据集的攻击者将尝试重新识别的假设。

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_758_223_832.jpg" alt="Image" width="5%" /></div>


场景 #3——数据泄露

P（重新识别尝试）= P（数据接收者所在行业的数据泄露）

三个场景中概率最高的应该作为P（re-ID尝试）。

P（re-ID尝试）= Max（P（内部攻击），P（数据接收者认识一个人数据集内），P（数据接收者所在行业的数据泄露））

把所有东西放在一起，

P（重新识别）

 $ =(1 / \text{数据集中最小等价类大小}) \times P(\text{re-ID 尝试}) = (1 / k) \times P(\text{re-ID 尝试}) $ 对于 k 匿名数据集



其中P（re-ID尝试）= Max（P（内部攻击），

P（数据接收者认识数据集中的人），P（数据接收者所在行业的数据泄露）

---

## 附件 E：匿名工具

以下是一些商业或开源匿名化工具的列表。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>工具</td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>网址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>健忘症</td><td style='text-align: center; word-wrap: break-word;'>失忆症匿名化工具是一种用于本地匿名个人和敏感数据的软件。目前支持k-匿名和km-匿名保证。</td><td style='text-align: center; word-wrap: break-word;'>https://amnesia.openaire.eu/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Arcad DOT-匿名者</td><td style='text-align: center; word-wrap: break-word;'>DOT-Anonymizer 是一种通过隐藏个人信息来维护测试数据机密性的工具。它的工作原理是匿名个人数据，同时保留其格式和类型。</td><td style='text-align: center; word-wrap: break-word;'>https://www.arcadsoftware.com/dot/datamasking/dot-anonymizer/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>阿格斯</td><td style='text-align: center; word-wrap: break-word;'>ARGUS 代表“反重新识别通用实用系统”。该工具使用各种不同的统计匿名化方法，例如全局重新编码（类别分组）、局部抑制、随机化、添加噪声、微聚集、顶部和底部编码。它还可用于生成合成数据。</td><td style='text-align: center; word-wrap: break-word;'>https://research.cbs.nl/casc/mu.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ARX</td><td style='text-align: center; word-wrap: break-word;'>ARX 是用于匿名化敏感个人数据的开源软件。</td><td style='text-align: center; word-wrap: break-word;'>https://arxiv.deidentifier.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>蚀</td><td style='text-align: center; word-wrap: break-word;'>Eclipse 是 Privacy Analytics 的一套工具，可促进健康数据的匿名化。</td><td style='text-align: center; word-wrap: break-word;'>https://privacy-analytics.com/health-dataprivacy/health-data-software/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sdcMicro</td><td style='text-align: center; word-wrap: break-word;'>sdcMicro 用于生成匿名微数据，例如公共和科学使用文件。它支持不同的风险估计方法。</td><td style='text-align: center; word-wrap: break-word;'>https://cran.r-project.org/web/packages/sdcMicro/index.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UTD 匿名化工具箱</td><td style='text-align: center; word-wrap: break-word;'>UT Dallas Data Security and Privacy Lab 将各种匿名化技术编译成一个工具箱供公众使用。</td><td style='text-align: center; word-wrap: break-word;'>http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home</td></tr></table>

---

## 罪

## 致谢

---

## 致谢

PDPC 和 InfocommMedia Development Authority (IMDA) 衷心感谢以下组织在编写本出版物过程中提供的宝贵反馈。

亚洲DPO

BetterData 私人有限公司

• ISACA（新加坡分会）—数据保护 SIG

• 新加坡律师会—网络安全和数据保护委员会 (CSDPC)

• 卫生部 (MOH)

· 副本分析

私人有限公司

• SGTech

新加坡商业联合会（SBF）——数字化委员会

• 新加坡企业法律顾问协会 (SCCA) — 数据保护、隐私和网络安全 (DPPC) 分会

• 新加坡统计局 (DOS)

智能国家和数字政府集团 (SNDGO)

## 本指南引用了以下指南。

英国。匿名化决策框架第2版：欧洲从业者指南，作者：马克·埃利奥特、伊莱恩·麦基和基隆·奥哈拉，2020年。

CSIRO 和 OAIC。去识别化决策框架，作者：Christine MO'Keefe、Stephanie Otorepec、Mark Elliot、Elaine Mackey 和 Kieron O'Hara，2017 年 9 月 18 日。

- 工业PC。结构化数据的去标识化指南, 2016 年 6 月, https://www.ipc.on.ca/wp-content/uploads/2016/08/Deidentification-Guidelines-for-Structured-Data.pdf。

· 艾玛姆，K.个人健康信息去识别化指南，CRC 出版社，2013 年。

第 29 条数据保护工作组（欧盟委员会）。“关于匿名化技术的意见 05/2014”。2014 年 4 月 10 日，http://ec.europa.eu/justice/data-protection/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf.

• NIST。NISTIR 8053：个人信息的去识别化，作者：SL Garfinkel，2015年10月，http://nvlpubs.nist.gov/nistpubs/ir/2015/NIST.IR.8053.pdf。

---



---

## # 新加坡数字

新加坡数字 (SG:D) 为新加坡的数字化努力提供了一个面孔，用一组视觉识别我们的数字计划和倡议，并以同一种语言与我们的本地和国际观众交谈。

SG:D 标志由圆形字体组成，这些字体由富有表现力的红色圆点演变而来。SG 代表新加坡，:D 代表我们的数字经济。:D 笑脸图标也象征着新加坡人进入数字经济的乐观态度。随着我们进入数字经济，一切都与人有关——同理心和保证将是我们所做一切的核心。

带给你的

## pdpc PERSONAL DATA PROTECTION COMMISSION SINGAPORE

版权所有 2022 - 新加坡个人数据保护委员会 (PDPC)

本出版物对数据匿名化的基本概念和技术进行了一般性介绍。此处的内容并非旨在成为法律的权威声明或替代法律或其他专业建议。PDPC及其成员、官员和雇员不对本出版物中的任何不准确、错误或遗漏负责，也不对因使用或依赖本出版物而造成的任何形式的损害或损失负责。

本出版物的内容受版权、商标或其他形式的专有权利保护，未经书面许可，不得以任何形式或任何方式全部或部分复制、再版或传播。