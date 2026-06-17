---
title: "CSA云计算安全指南"
source: "云计算 参考法规、标准/CSA云计算安全指南.pdf"
type: "pdf"
processed: "2026-04-22T23:11:54.893884"
---

### 云计算关键领域 安全指南 V3.0

---

## 导论

The guidance provided herein is the third version of the Cloud Security Alliance document, “Security Guidance for Critical Areas of Focus in Cloud Computing,” which was originally released in April 2009. The permanent archive locations for these documents are:

http://www.cloudsecurityalliance.org/guidance/csaguide.v3.0.pdf (this document)

http://www.cloudsecurityalliance.org/guidance/csaguide.v2.1.pdf (version 2 guidance)

http://www.cloudsecurityalliance.org/guidance/csaguide.v1.0.pdf (version 1 guidance)

In a departure from the second version of our guidance, each domain was assigned its own editor and peer reviewed by industry experts. The structure and numbering of the domains align with industry standards and best practices. We encourage the adoption of this guidance as a good operating practice in strategic management of cloud services. These white papers and their release schedule are located at:

http://www.cloudsecurityalliance.org/guidance/

In another change from the second version, there are some updated domain names. We have these changes: Domain 3: Legal Issues: Contracts and Electronic Discovery and Domain 5: Information Management and Data Security. We now have added another domain, which is Domain 14: Security as a Service.

© 2011 Cloud Security Alliance.

All rights reserved. You may download, store, display on your computer, view, print, and link to the Cloud Security Alliance Guidance at http://www.cloudsecurityalliance.org/guidance/csaguide.v3.0.pdf subject to the following: (a) the Guidance may be used solely for your personal, informational, non-commercial use; (b) the Guidance may not be modified or altered in any way; (c) the Guidance may not be redistributed; and (d) the trademark, copyright or other notices may not be removed. You may quote portions of the Guidance as permitted by the Fair Use provisions of the United States Copyright Act, provided that you attribute the portions to the Cloud Security Alliance Guidance Version 3.0 (2011).

---

## 目录

导论 ..... 1  
目录 ..... 2  
前言 ..... 3  
V3.0 中文版 译者序 ..... 4  
英文版致谢 ..... 6  
编者寄语 ..... 8  
关于风险的编者按 ..... 10  
第一部分 云体系架构  
D1: 云计算体系架构 ..... 14  
第二部分 云的治理  
D2: 治理与企业风险管理 ..... 31  
D3: 法律问题：合同与电子发现 ..... 36  
D4: 合规与审核 ..... 44  
D5: 信息管理与数据安全 ..... 48  
D6: 互操作性与可移植性 ..... 61  
第三部分 云的运行  
D7: 传统安全、业务连续性和灾难恢复 ..... 70  
D8: 数据中心运行 ..... 83  
D9: 事故响应 ..... 87  
D10: 应用安全 ..... 96  
D11: 加密与密钥管理 ..... 119  
D12: 身份，授权和访问管理 ..... 125  
D13: 虚拟化 ..... 144  
D14: 安全即服务 SecaaS ..... 149

---

## 前言

Welcome to the third version of the Cloud Security Alliance’s “Security Guidance for Critical Areas of Focus in Cloud Computing.” As cloud computing begins to mature, managing the opportunities and security challenges becomes crucial to business development. We humbly hope to provide you with both guidance and inspiration to support your business needs while managing new risks.

The Cloud Security Alliance has delivered actionable, best practices based on previous versions of this guidance. As we continue to deliver tools to enable businesses to transition to cloud services while mitigating risk, this guidance will act as the compass for our future direction. In v3.0, you will find a collection of facts and opinions gathered from over seventy industry experts worldwide. We have compiled this information from a range of activities, including international chapters, partnerships, new research, and conference events geared towards furthering our mission. You can follow our activities at www.cloudsecurityalliance.org.

The path to secure cloud computing is surely a long one, requiring the participation of a broad set of stakeholders on a global basis. However, we should happily recognize the progress we are seeing: new cloud security solutions are regularly appearing, enterprises are using our guidance to engage with cloud providers, and a healthy public dialogue over compliance and trust issues has erupted around the world. The most important victory we have achieved is that security professionals are vigorously engaged in securing the future, rather than simply protecting the present.

Please stay engaged on this topic and continue to work with us to complete this important mission.

Best Regards,

Jerry Archer

Dave Cullinane

Nils Puhlmann

Alan Boehme

Paul Kurtz

Jim Reavis

The Cloud Security Alliance Board of Directors

---

### v3.0 中文版 译者序

云计算已经成为行业中一个轰轰烈烈的“进行时”，云计算自身的安全防护、使用云计算变革网络安全都获得了迅速上升的关注和资源投入。云安全联盟以其大量的研究发布、迅速发展的企业和个人会员成为国际范围内在云安全领域具备首屈一指影响力的组织。至本序写作之日，云安全联盟的企业会员达到150家，其中来自中国大陆的企业有7家，以LinkedIn为基准的个人会员达到46500多人。

《云安全指南》全称《云计算关键领域的安全指南》（Security Guidance for Critical Areas of Focus in Cloud Computing）。云安全指南第1版在2009年4月1日发布，也就是在2009年的RSA会议上CSA成立后的一个月。这个版本并没有引起特别大的关注。在2009年12月17日，CSA发布了《云安全指南v2.1》。在发布后的很长一段时间内，几乎是在世界范围内唯一的发布，非常引人注目，大量的下载和报道也帮助云安全联盟在行业内的被关注程度迅速上升。2010年春节后，V2.1的中文版发布。

2011 年 11 月 14 日 CSA 发布了《云安全指南 v3.0》，也就是在 V2.1 发布后的大约 2 年后。有必要说明的一点，从《云安全指南 v2.1》到《云安全指南 v3.0》的变化是非常大的，这从文档的页数从 76 页增加到 177 页足见一斑。对比来看，v3.0 除了新增第 14 域“安全即服务”一节之外，其他章节中之前许多概括性的描述在新版本中进行了丰富和细化。

V3 至今已有 1 年多时间，期间不少朋友专家同仁希望 CSA 能组织将其翻译成中文，以便于国内用户读者使用。在 2013 年春节前通过微博/邮件等方式发出中文版倡议后，得到了很多同仁的热烈响应，迅速组成了一个十多人的翻译小组。大家牺牲了春节很多和家人团聚休息的时间投入到翻译工作中，在 3 月份左右完成了每章节的翻译。随后又经过审校小组诸位同仁的认真校阅，到 5 月份终于告一段落。

在翻译工作中，D1 由臧铁军、林恒辉翻译，D2 由 Kelvin Gao、余晓光、潘吴斌翻译，D3 由杨帆、潘吴斌翻译，D4 由曹嘉、杨帆翻译，D5 由余晓光、龚习琴翻译，D6 由张荣典翻译，D7 由叶润国、曹嘉、臧铁军、林恒辉翻译，D8 由汪宏翻译，D9 由李本、王海涛、马蔚彦翻译，D10 由刘生权、马红伟翻译，D11 由徐甲甲翻译，D12 由田民、徐甲甲翻译，D13 由沈勇、杨勇涛翻译，D14 由刘弘利、王海涛、张荣典翻译。

潘柱廷审校了 D1/D2，沈勇审校了 D3/D4，Billy 审校了 D5/D6，Antony Ma 审校了 D7/D11，Otto Lee 审校了 D8，Frank Chow 审校了 D9，吴云坤审校了 D10/D14，Ricci leong 审校了 D12，Mike Lo 审校了 D13。

感谢卿思汉老师对翻译小组的指导和提出的宝贵意见。

另外，感谢王洋为最终稿排版付出了很多努力，他还帮助修正不少译稿中的小纰漏。

全文由赵粮负责组织和统稿。

当前翻译版本肯定还存在诸多问题，例如很多图表没有来得及制作中文版本，一些需要本地化的注解/注释等没有来得及添加，有些翻译不够精确，没有来得及和原作者/编辑小组沟通确认。欢迎读者批评指正。

另外，期间由于项目组织和个人方面的原因有诸多拖延，向大家致以歉意。

---

在 CSA 官方网址 https://chapters.cloudsecurityalliance.org/china 可以找到更多的研究项目和联系方式。另外，搜索新浪微群 “云安全联盟”、在 LinkedIn 搜索 “Cloud Security Alliance, Greater China Chapter” 可以找到更多中国区的更新并与同仁互动。

希望中文版的翻译发布能够在云计算安全的研究、开发、推广、应用等活动中为行业、政府、标准机构和学术的同仁、同学提供帮助。

---

## 英文版致谢

## Domain Authors/Contributors

Domain 1: Chris Hoff, Paul Simmonds

Domain 2: Marlin Pohlman, Becky Swain, Laura Posey, Bhavesh Bhagat

Domain 3: Francoise Gilbert, Pamela Jones Harbour, David Kessler, Sue Ross, Thomas Trappler

Domain 4: Marlin Pohlman, Said Tabet

Domain 5: Rich Mogull, Jesus Luna

Domain 6: Aradhna Chetal, Balaji Ramamoorthy, Jim Peterson, Joe Wallace, Michele Drgon, Tushar Bhavsar

Domain 7: Randolph Barr, Ram Kumar, Michael Machado, Marlin Pohlman

Domain 8: Liam Lynch

Domain 9: Michael Panico, Bernd Grobauer, Carlo Espiritu, Kathleen Moriarty, Lee Newcombe, Dominik Birk, Jeff Reed

Domain 10: Aradhna Chetal, Balaji Ramamoorthy, John Kinsella, Josey V. George, Sundararajan N., Devesh Bhatt, Tushar Bhavsar

Domain 11: Liam Lynch

Domain 12: Paul Simmonds, Andrew Yeomans, Ian Dobson, John Arnold, Adrian Secombe, Peter Johnson, Shane Tully, Balaji Ramamorthy, Subra Kumaraswamy, Rajiv Mishra, Ulrich Lang, Jens Laundrup, Yvonne Wilson

Domain 13: Dave Asprey, Richard Zhao, Kanchanna Ramasamy Balraj, Abhik Chaudhuri, Melvin M. Rodriguez

Domain 14: Jens Laundrup, Marlin Pohlman, Kevin Fielder

## Peer Reviewers

Valmiki Mukherjee, Bernd Jaeger, Ulrich Lang, Hassan Takabi, Pw Carey, Xavier Guerin, Troy D. Casey, James Beadel, Anton Chuvakin, Tushar Jain, M S Prasad, Damir Savanovic, Eiji Sasahara, Chad Woolf, Stefan Pettersson, M S Prasad, Nrupak Shah, Kimberley Laris, Henry St. Andre, Jim Peterson, Ariel Litvin, Tatsuya Kamimura, George Ferguson, Andrew Hay, Danielito Vizcayno,

K.S. Abhiraj, Liam Lynch, Michael Marks, JP Morgenthal, Amol Godbole, Damu Kuttikrishnan, Rajiv Mishra, Dennis F. Poindexter, Neil Fryer, Andrea Bilobrk, Balaji Ramamoorthy, Damir Savanovic

## Editorial Team

Archie Reed: Domains 3, 8, 9

---

Chris Rezek: Domains 2, 4, 5, 7, 13, 14

Paul Simmonds: Domains 1, 6, 10, 11, 12

## CSA Staff

Technical Writer/Editor: Amy L. Van Antwerp

Graphic Designer: Kendall Scoboria

Research Director: J.R. Santos

---

## 编者寄语

Over the past three years, the Cloud Security Alliance has attracted around 120 corporate members and has a broad remit to address all aspects of cloud security, including compliance, global security-related legislation and regulation, identity management, and the challenge of monitoring and auditing security across a cloud-based IT supply chain. CSA is becoming the focal point for security standards globally, aligning multiple, disparate government policies on cloud security and putting forward standards for ratification by international standards bodies.

CSA sees itself as a cloud security standards incubator, so its research projects use rapid development techniques to produce fast results. To this end, the CSA Guidance editorial team is proud to present the third version of its flagship “Security Guidance for Critical Areas of Focus in Cloud Computing.” This work is a set of best security practices CSA has put together for 14 domains involved in governing or operating the cloud (Cloud Architecture, Governance and Enterprise Risk Management, Legal: Contracts and Electronic Discovery, Compliance and Audit, Information Management and Data Security, Portability and Interoperability, Traditional Security, Business Continuity and Disaster Recovery, Data Center Operations, Incident Response, Notification and Remediation, Application Security, Encryption and Key Management, Identity and Access Management, Virtualization, and Security as a Service).

CSA guidance in its third edition seeks to establish a stable, secure baseline for cloud operations. This effort provides a practical, actionable road map to managers wanting to adopt the cloud paradigm safely and securely. Domains have been rewritten to emphasize security, stability, and privacy, ensuring corporate privacy in a multi-tenant environment.

Over the past two years, version 2.1 of the guidance has served as the foundation for research in multiple areas of cloud security. Deliverables now in use from the TCI Architecture to the GRC Stack were inspired by previous versions of the guidance, and it is our hope that this version will be no different. The guidance serves as a high level primer for chief executives, consumers, and implementers wishing to adopt cloud services as an alternative or supplement to traditional infrastructure. However, the guidance is designed with innovation in mind. Those with an entrepreneurial mindset should read this work with an eye toward the inferred services and approaches many of the authors have included in the domain creation. Investors and corporate decision makers will also find this work of interest, as it serves as a roadmap for innovation and development already in place in companies throughout the world. Security practitioners and educators will find elements of this book both authoritative and thought provoking, and as the industry evolves, the value the authors have included should prove influential and timely.

In the third edition, the guidance assumes a structural maturity in parallel with multinational cloud standards development in both structure and content. Version 3.0 extends the content included in previous versions with practical recommendations and requirements that can be measured and audited. Please note that different interpretations of the term "requirements" exist, which we use throughout the document. Our guidance does not represent a statutory obligation, but "requirements" was chosen to represent guidance appropriate for virtually all use cases we could envision, and also aligns our guidance with similar well-accepted documents. CSA industry expert authors have endeavored to present a working product that is measured and balanced between the interests of cloud providers and tenants. Controls focus on the preservation of tenant data ownership integrity while embracing the concept of a shared physical infrastructure. Guidance Version 3.0 incorporates the highly dynamic nature of cloud computing, industry learning curve, and new developments within other research projects such as Cloud Controls Matrix, Consensus Assessments Initiative, Trusted Cloud Initiative, and GRC Stack Initiative and ties in the various CSA activities into one comprehensive C-level best practice. The Security Guidance v3.0 will serve as the gateway to emerging standards being

---

developed in the world’s standards organization and is designed to serve as an executive-level primer to any organization seeking a secure, stable transition to hosting their business operations in the cloud.

On behalf of the Cloud Security Alliance, we would like to thank each and every volunteer for their time and effort in the development and editing of this new release of our flagship guidance document. While we believe this is our best, most widely reviewed work to date, the topic is still evolving and although our foremost intent is to guide, we also intend to inspire the readers to become involved in improving and commenting on the direction those composing the body of work have outlined. We humbly and respectfully submit this effort to the industry and await the most important component of any dialog, your opinion. We are eager to hear your feedback regarding this updated guidance. If you found this guidance helpful or would like to see it improved, please consider joining the Cloud Security Alliance as a member or contributor.

Best Regards,

Paul Simmonds

Chris Rezek

Archie Reed

Security Guidance v3.0 Editors

---

## 关于风险的编者按

Throughout this Guidance we make extensive recommendations on reducing your risk when adopting cloud computing, but not all the recommendations are necessary or even realistic for all cloud deployments. As we compiled information from the different working groups during the editorial process, we quickly realized there simply wasn't enough space to provide fully nuanced recommendations for all possible risk scenarios. Just as a critical application might be too important to move to a public cloud provider, there might be little or no reason to apply extensive security controls to low-value data migrating to cloud-based storage.

With so many different cloud deployment options — including the SPI service models (SPI refers to Software as a Service, Platform as a Service, or Infrastructure as a Service, explained in depth in Domain 1); public vs. private deployments, internal vs. external hosting, and various hybrid permutations — no list of security controls can cover all circumstances. As with any security area, organizations should adopt a risk-based approach to moving to the cloud and selecting security options. The following is a simple framework to help evaluate initial cloud risks and inform security decisions.

This process is not a full risk assessment framework, nor a methodology for determining all your security requirements. It’s a quick method for evaluating your tolerance for moving an asset to various cloud computing models.

## Identify the Asset for the Cloud Deployment

At the simplest, assets supported by the cloud fall into two general categories:

1. Data

### 2. Applications/Functions/Processes

We are either moving information into the cloud, or transactions/processing (from partial functions all the way up to full applications).

With cloud computing our data and applications don’t need to reside in the same location, and we can choose to shift only parts of functions to the cloud. For example, we can host our application and data in our own data center, while still outsourcing a portion of its functionality to the cloud through a Platform as a Service.

The first step in evaluating risk for the cloud is to determine exactly what data or function is being considered for the cloud. This should include potential uses of the asset once it moves to the cloud to account for scope creep. Data and transaction volumes are often higher than expected.

## Evaluate the Asset

The next step is to determine how important the data or function is to the organization. You don’t need to perform a detailed valuation exercise unless your organization has a process for that, but you do need at least a rough assessment of how sensitive an asset is, and how important an application/function/process is.

---

For each asset, ask the following questions:

1. How would we be harmed if the asset became widely public and widely distributed?

2. How would we be harmed if an employee of our cloud provider accessed the asset?

3. How would we be harmed if the process or function were manipulated by an outsider?

4. How would we be harmed if the process or function failed to provide expected results?

5. How would we be harmed if the information/data were unexpectedly changed?

6. How would we be harmed if the asset were unavailable for a period of time?

Essentially we are assessing confidentiality, integrity, and availability requirements for the asset; and how the risk changes if all or part of the asset is handled in the cloud. It’s very similar to assessing a potential outsourcing project, except that with cloud computing we have a wider array of deployment options, including internal models.

## Map the Asset to Potential Cloud Deployment Models

Now we should have an understanding of the asset's importance. Our next step is to determine which deployment models we are comfortable with. Before we start looking at potential providers, we should know if we can accept the risks implicit to the various deployment models: private, public, community, or hybrid; and hosting scenarios: internal, external, or combined.

For the asset, determine if you are willing to accept the following options:

1. Public.

2. Private, internal/on-premises.

3. Private, external (including dedicated or shared infrastructure).

4. Community; taking into account the hosting location, potential service provider, and identification of other community members.

5. Hybrid. To effectively evaluate a potential hybrid deployment, you must have in mind at least a rough architecture of where components, functions, and data will reside.

At this stage you should have a good idea of your comfort level for transitioning to the cloud, and which deployment models and locations fit your security and risk requirements.

## Evaluate Potential Cloud Service Models and Providers

In this step focus on the degree of control you'll have at each SPI tier to implement any required risk management. If you are evaluating a specific offering, at this point you might switch to a fuller risk assessment.

---

Your focus will be on the degree of control you have to implement risk mitigations in the different SPI tiers. If you already have specific requirements (e.g., for handling of regulated data) you can include them in the evaluation.

## Map Out the Potential Data Flow

If you are evaluating a specific deployment option, map out the data flow between your organization, the cloud service, and any customers/other nodes. While most of these steps have been high-level, before making a final decision it's absolutely essential to understand whether, and how, data can move in and out of the cloud.

If you have yet to decide on a particular offering, you’ll want to sketch out the rough data flow for any options on your acceptable list. This is to insure that as you make final decisions, you’ll be able to identify risk exposure points.

## Conclusions

You should now understand the importance of what you are considering moving to the cloud, your risk tolerance (at least at a high level), and which combinations of deployment and service models are acceptable. You should also have a good idea of potential exposure points for sensitive information and operations.

These together should give you sufficient context to evaluate any other security controls in this Guidance. For low-value assets you don't need the same level of security controls and can skip many of the recommendations — such as on-site inspections, discoverability, and complex encryption schemes. A high-value regulated asset might entail audit and data retention requirements. For another high-value asset not subject to regulatory restrictions, you might focus more on technical security controls.

Due to our limited space, as well as the depth and breadth of material to cover, this document contains extensive lists of security recommendations. Not all cloud deployments need every possible security and risk control. Spending a little time up front evaluating your risk tolerance and potential exposures will provide the context you need to pick and choose the best options for your organization and deployment.

---

<div style="text-align: center;"><img src="imgs/img_in_seal_box_69_599_1104_1197.jpg" alt="Image" width="84%" /></div>


## 第一部分 // 云体系架构

---

## D1: 云计算体系架构

本域是云计算体系体系架构，为云计算安全指南的其它所有部分介绍一个概念性的框架。主要内容将集中在云计算的描述上，并按照 IT 网络和安全专业人士的视角进行了裁剪。

本域的最后一节简要介绍了本指南其它域的内容。

理解本域所描述的体系架构是理解云计算安全指南其它部分的重要一步，该框架定义了很多在其它域中广泛使用的概念和术语。

简介. 下面分三个部分分别来定义云计算体系架构

为保证词汇一致性而贯穿整个指南的术语。

为保护云应用和云服务安全的架构层要求和挑战。

一个描述云服务和体系架构分类的参考模型。

### 1.1 什么是云计算？

云计算是一个模式，它是一种无处不在的，便捷的，按需的，基于网络访问的，共享使用的，可配置的计算资源（如网络，服务器，存储，应用和服务）。云计算是一种颠覆性的技术，它可以增强协作，提高敏捷性、可扩展性以及可用性。还可以通过优化资源分配、提高计算效率来降低成本。云计算模式构想了一个全新的世界，组件可以迅速调配、置备、部署和回收，还可以迅速地扩充或缩减，以提供按需的、类似于效用计算的分配和消费模式。

从架构的角度来看，云和现有计算模式有什么相似和不同，以及这些相似和不同如何在网络和信息安全实践中对企业的组织、运行和技术路线构成影响，围绕着这些问题有很多令人困惑的地方。常规计算与云计算并不遥远。但是，云计算会在数据安全、网络安全和信息安全等领域对企业的组织、运营和技术路线产生深远的影响。

现在有许多定义尝试着从学术、架构师、工程师、开发人员、管理人员和消费者等不同的角度来定义什么是云。本文档依照 IT 网络和安全专业人士的视角对云的定义进行了裁剪。

---

### 1.2 云计算的构成

这一版本的云安全指南对云计算所做出的定义，基于美国国家标准与技术研究院（NIST）的科学家所写的出版物以及他们围绕云计算定义所做出的努力。

NIST 出版物是被普遍接受的，所以，我们选择与 NIST Working Definition of Cloud Computing（写作本文时是 NIST 800-145）保持一致，这样我们能够集中精力到用例上，而不是细微的语法定义差别上，同时能保证一致性并获得广泛的共识。

值得注意的是，本指南的目的是使其具有广泛的易用性、适用于全球范围内的组织。虽然 NIST 是美国政府机构，选择此参考模型不应该被解释为是对其它观点或地域的排斥。

在 NIST 对云计算的定义中，包括了五个基本特征、三个云服务模式、以及四个云部署模型。图 1 对它们进行了形象的汇总，后面会有详细描述。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_566_1127_1209.jpg" alt="Image" width="83%" /></div>


<div style="text-align: center;">图 1: NIST 云计算定义的直观模型</div>


### 1.3 云计算的特征

---

必须认识到的重要一点是虽然云服务经常和虚拟化技术一起使用，或者云服务基于虚拟化技术，但是并不必然。没有要求将资源抽象与虚拟化技术必须绑在一起。很多云服务产品并没有使用虚拟化层或操作系统容器。

还应该注意到，多租户并没有成为 NIST 云计算定义中的一个必备特征，但在讨论中确实经常这么认为。CSA 认为多租户是云的一个重要元素。

### 1.4 多租户

在本文中多租户被认为是一个重要元素，后续的章节将描述CSA对这个重要的云计算元素的理解和定义。

多租户的最简单形式就是多个消费者同时使用属于同一组织或不同组织的资源和应用。多租户的影响主要是残留数据可见性和对其它用户或租户操作的追踪。

云服务模式中的“多租户”意味着满足不同客户场景对策略驱动的安全增强、分段、隔离、监管、服务水平以及相应的计费/返款等模型的不同需求。

<div style="text-align: center;"><img src="imgs/img_in_image_box_721_121_1125_796.jpg" alt="Image" width="33%" /></div>


消费者可以以用户的身份使用公有云服务提供商的服务，

或者是私有云服务中一个实例，一个组织可以将共享同一个公共基础的用户分隔为不同的业务单元 BU（business unit）。



从提供商的角度来看，多租户对架构和设计提出的要求是通过在很多不同消费者之间杠杆式地分享基础设施、数据、元数据、服务和应用等，来实现可扩展、可用性、管理、分区、隔离以及运行效率等方面的“经济性”。

依赖于服务商的云服务模式，“多租户”也可以有不同的定义，因为它可能在基础设施、数据库或应用等不同层面上实现。基础设施即服务（IaaS $ ^{1} $），软件即服务（SaaS $ ^{2} $）和平台即服务（PaaS $ ^{3} $）都是多租户的实现。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_231_119_1035_347.jpg" alt="Image" width="65%" /></div>


Private Cloud of Company XYZ with 3 business units, each with different security, SLA, governance and chargeback policies on shared infrastructure

Public Cloud Provider with 3 business customers, each with different security, SLA, governance and billing policies on shared infrastructure

<div style="text-align: center;">图 2: 多租户</div>


“多租户”在不同的云部署模型中的重要性也有所不同。然而，即使在私有云中，组织虽然是同一个，但是也存在来自各方的第三方顾问和临时合同人员，也存在对不同业务单元间高层逻辑分离的期望，因此，也需要考虑“多租户”。

### 1.5 云参考模型

理解云计算模式之间的关系和依赖性对于理解云计算的安全风险非常关键。IaaS 是所有云服务的基础，PaaS 建立在 IaaS 之上，而 SaaS 又建立在 PaaS 之上，它们之间的关系可参考云参考模型图示。沿着这个思路，如同云服务能力是继承的那样，信息安全风险和问题也是继承的。值得重点注意的是，商用云提供商可能并没有与这个模型的层次准确对应。然而，云参考模型对于将真实服务和某个架构框架联系在一起，进而理解需进行安全分析的资源和服务是非常重要的。

IaaS 涵盖了从机房设备到其中的硬件平台等所有的基础设施资源层面。它包括了将资源抽象化（或相反）的能力，并交付连接到这些资源的物理或逻辑网络连接，终极状态是 IaaS 提供商提供一组 API，允许消费者与基础设施进行管理和其它形式的交互。

PaaS 位于 IaaS 之上，又增加了一个层面用以与应用开发框架、中间件能力以及数据库、消息和队列等功能集成。PaaS 允许开发者在平台之上开发应用，开发的编程语言和工具由 PaaS 支持提供。

类似的，SaaS 又位于底层的 IaaS 和 PaaS 之上。SaaS 能够提供独立的运行环境，用以交付完整的用户体验，包括内容、展现、应用和管理能力。

因此，必须清楚，在三个模型中，在集成的功能特征、复杂性与开放性（可扩展性）和安全性等方面会有一些明显的权衡。一般来说，基础设施即服务（IaaS），将计算机基础设施（通常以虚拟化环境作为平台）与存储和网络资源一起作为服务交付。用户无需购买服务器，软件，数据中心空间或网络设备，而是将这些资源作为外包服务整体采购。



软件即服务（SaaS），有时也被称为“按需的软件”，是一种将软件和相关联的数据集中存储（通常位于互联网上的公有云中）的软件交付形式。用户可以使用瘦客户机上的浏览器通过互联网来访问服务。

平台即服务（PaaS），将计算平台和解决方案包作为服务来交付。PaaS提供部署应用所需的设施，消除了购买和管理底层硬件和软件以及部署这些主机所带来的成本和复杂度。所提供的能力需要为在互联网上构建和发布 Web 应用以及服务提供完整的生命周期支持。

SaaS 会在产品中提供最为集成化的功能，最小的用户可扩展性以及相对来说较高的集成化的安全（至少提供商承担安全的职责）。

---

PaaS 提供的是开发者在平台之上开发自己应用的能力。因此，它倾向于提供比 SaaS 更多的可扩展性，其代价是没有了 SaaS 那些用户即买即用的功能。这种权衡也会延伸到安全特色和能力上，虽然内置安全能力变得不够完备，但是用户却拥有更多的灵活性去实现自己的强化安全。

IaaS 几乎不提供那些和应用类似的特色功能，但却有极大的“可扩展性”。这一般是指 IaaS 在除了基础设施自身的保护之外，提供更少的集成安全保护能力和功能。IaaS 模型要求云用户自己管理和保护操作系统、应用和内容。

云安全架构的一个关键特点是云服务提供商所在的等级越低，云服务用户自己所要承担的安全能力和管理职责就越多。

如果要向消费者承诺 SLA，则意味着需要在合同里需要对服务本身和提供商的服务水平、安全、管控、合规性以及责任期望等有明确要求。目前存在两种类型的 SLA，可协商的和不可协商的。缺少 SLA 时，消费者的管理员需要控制云的所有方面。如果采用不可协商的 SLA，则提供商的管理员需要根据协议负责这一部分。在 PaaS 或 IaaS 情况下，这些内容的管理责任是用户自己的系统管理员，提供商对于安全保护底层平台和基础设施组件以确保基本服务的可用性和安全，其具体要求可能会有一些相关的出入。必须清楚一点，用户可以指派/转移职责（responsibility）而不是责任（accountability）。

如果将每种云交付模型的范围或具体能力/功能，或它们相互交叉耦合的一些功能缩小一下，将会产生很多衍生的分类。例如存储作为服务（Storage as a Service）就是 IaaS 家族中的一个具体的子服务。

云计算的解决方案正在不断地演进，虽然讨论它的全景图超出了本文档的范围，但下面这张 OpenCrowd Cloud Solutions 分类图还是给出了一个非常不错的起点，它展示了当前风起云涌的由上述几种部署模型衍生而来的种种云解决方案。CSA 并不特别支持下图所列出的任何解决方案，而只是用来说明当前市场上提供的云解决方案的多样性。

---

## Infrastructure Services

Amazon S3 & EBS

Rackspace Cloud Files

Nirvanix

AT&T Synaptic

Zetta

Amazon EC2

Serve Path GoGrid

Rackspace Cloud Servers

Joyent Cloud

Flexiant Flexiscale

Elastichosts

Terremark

iTRiCITY

LayeredTech

Savvis Cloud Compute

Verizon CaaS

AT&T Synaptic

Sungard Enterprise Cloud

Navisite

Services Manager

- Scalr

- CohesiveFT

- Ylastic

- CloudFoundry

- NewRelic

- Cloud42

- Amazon CloudWatch

- Amazon VPC

<div style="text-align: center;"><img src="imgs/img_in_image_box_72_145_1142_1224.jpg" alt="Image" width="87%" /></div>


## CLOUD TAXONOMY

## Platform Services

<div style="text-align: center;"><img src="imgs/img_in_image_box_88_1159_323_1224.jpg" alt="Image" width="19%" /></div>


## OpenCrowd

<div style="text-align: center;">图3: OpenCrowd 的云分类</div>


为了提供一个云计算用例的全面视图，Cloud Computing Use Case Group 开发了一个协同任务来描述和定义通用案例并展示云带来的好处，他们的目标设定为：“...让云用户和提供商一起来定义云计算的公共用例…强调云计算环境中需要标准化的能力和要求，以确保互操作性、更易集成、可移植性。”

---

#### 1.5.1 云安全参考模型

云安全参考模型解决的是这些分类的关系，并把它们和与其相关的安全控制和顾虑放在一起来考虑。对于初次接触云计算的组织和个人来说，注意到下面的问题以避免潜在的陷阱和困惑是很重要的：

“云服务是如何部署的”与“云服务是在哪里提供的”这样的概念频繁混用所带来的困惑。例如，公共或私有可能被描述成外部或内部云，这种互换不是所有情况下都是准确的。

云服务的使用方式经常被描述成与组织的管理或安全边界位置有关（通常定义在某个防火墙上）。虽然了解云计算中安全边界在哪里很重要，但是，“界限清晰的边界”的这一概念对于大多数组织是一个时代性错误。

在企业中正在上演的对信任边界的重组（re-perimeterization）及侵蚀，被云计算放大并加速。无处不在的连接、各种形式的信息交换、无法解决云服务动态特性的传统静态安全控制，这些都要求针对云计算的新思维。针对企业网络的边界重整，Jericho Forum 开发了相当多的材料，包括很多案例分析。

云的部署和消费模式不能仅仅在“内部”还是“外部”概念上讨论，因为它们不仅与资产、资源和信息的物理位置有关，而且还要讨论由谁消费，由谁负责治理、安全、政策标准的合规性等。

这里不是在主张某个资产、资源和信息是在 “场内” （on-premise）还是 “场外” （off-premise）对组织的安全和风险状态没有影响，它们的的确确有影响。但是，这里更想强调的是风险还与下面这些有关：

■ 所要管理的资产、资源和信息类型

■ 谁管理？如何管理？

选择了哪些控制？如何集成？

合规性问题

例如，Amazon AWS EC2 里部署的 LAMP 套件应该归类为公共的、场外的、第三方管理的 IaaS 解决方案，即使其中的实例、应用、数据是由消费者或某个第三方负责管理。部署在 Eucalyptus 的为若干个业务单元服务某个常规应用，由同一个公司控制、管理并拥有，可以归类为私有的、场内的、自管理的 SaaS 解决方案。两个例子都使用了云的弹性架构和自服务能力。

下面的表格总结了这些要点：

---

<div style="text-align: center;">表1：云计算部署模型</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Infrastructure Managed  $ By^{1} $</td><td style='text-align: center; word-wrap: break-word;'>Infrastructure Owned  $ By^{2} $</td><td style='text-align: center; word-wrap: break-word;'>Infrastructure Located $ ^{3} $</td><td style='text-align: center; word-wrap: break-word;'>Accessible and Consumed  $ By^{4} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Public</td><td style='text-align: center; word-wrap: break-word;'>Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Off-Premise</td><td style='text-align: center; word-wrap: break-word;'>Untrusted</td></tr><tr><td rowspan="2">Private/ Community</td><td style='text-align: center; word-wrap: break-word;'>Organization</td><td style='text-align: center; word-wrap: break-word;'>Organization</td><td style='text-align: center; word-wrap: break-word;'>On-Premise</td><td rowspan="2">Trusted</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Off-Premise</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hybrid</td><td style='text-align: center; word-wrap: break-word;'>Both Organization &amp; Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Both Organization &amp; Third Party Provider</td><td style='text-align: center; word-wrap: break-word;'>Both On-Premise &amp; Off-Premise</td><td style='text-align: center; word-wrap: break-word;'>Trusted &amp; Untrusted</td></tr></table>

 $ ^{1} $ Management includes: governance, operations, security, compliance, etc...

 $ ^{2} $ Infrastructure implies physical infrastructure such as facilities, compute, network & storage equipment

 $ ^{3} $ Infrastructure Location is both physical and relative to an Organization’s management umbrella and speaks to ownership versus control

 $ ^{4} $ Trusted consumers of service are those who are considered part of an organization's legal/contractual/policy umbrella including employees, contractors, & business partners. Untrusted consumers are those that may be authorized to consume some/all services but are not logical extensions of the organization.

另外一个将云服务模型、部署模型、资源物理位置、管理和所有者属性等图形化展示的方法是 Jericho Forum（www.ierichoforum.org）的云立方体模型（Cloud Cube Model），如下图所示：

云立方体模型很形象地阐述了市场上现有云产品的各种排列组合，提出了用以区分云从一种形态（formation）转换到另外一种形态的四种准则/维度，以及各种组成的供应配置方式以便理解云计算影响安全路线的方式。

云立方体模型还凸显了在理解云模型并将云模型映射到控制框架和标准上去时的挑战，这些控制框架和标准，像 ISO/IEC27002，提供了“一系列指南和通用原

云立方体模型还凸显了在理解云模型方面图像 ISO/IEC27002，提供了“一系列指南和通用原则，用以在组织内部启动、部署、维护和提升信息安全管理”。



在 ISO/IEC 27002 的 6.2 节，“外方”（External Parties）控制目标有：“……组织的信息和信息处理设施的安全不应该因为引入外方产品或服务而降低……”

因此，三种云服务模型的安全防护在方法和责任上有所不同，这意味着云服务的消费者面临很有挑战性的工作。除非云提供商愿意透露自己的安全控制以及为消费者部署的程度，同时消费者也知晓自己需要哪些控制以保持信息安全，否则，肯定会有极大可能误导风险管

<div style="text-align: center;"><img src="imgs/img_in_image_box_580_1016_1108_1392.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图 4: Jericho 的云立方模型</div>


---

理决策并损失惨重。

首先将一个云服务归类到云架构模型中。接下来对照其安全架构，以及业务、监管和其它合规要求做出差距分析。输出的结果决定了某个云服务的一般“安全”状态，以及它如何和某个资产的保障和保护要求关联到一起。

下图给出了一个很好的例子说明，如何通过对云服务组件和安全控制策略集的映射来确定哪些安全控制是存在或缺失的，这些安全控制分别由客户，云服务提供商或第三方提供。这也可以与合规框架或者强制要求（如PCI DSS）来进行比较，同样如下图所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_82_364_1114_1049.jpg" alt="Image" width="84%" /></div>


<div style="text-align: center;">图5：将云模型与安全控制和合规性进行映射</div>


完成差距分析后，按照监管方和合规方面的要求，就容易决定需要做哪些以反馈到风险评估框架了。相应地，这也可以帮助决定如何对待这些安全“差距”或最终的风险－接受、转移、或降低。

需要意识到的重要一点是，使用云计算作为一种运行模型并不会自然地提供或妨碍达成合规性。对于任何要求的合规是服务、所使用的部署模型、以及对范围内的资源的设计、部署、管理等的直接结果。

下面是几个对控制框架非常好的全面总结，它们提供了上面提及的通用控制框架的精彩阐述，包括开放安全架构小组（Open Security Architecture Group）的安全架构模式文档，还有最近刚刚更新的 NIST 800-53 修订版 3 - 联邦信息系统与组织安全控制建议（Recommended Security Controls for Federal Information Systems and Organizations）。

---

#### 1.5.2 什么是云计算的安全性？

云计算中的安全控制，其中的大部分与其它 IT 环境中的安全控制并没有什么不同。然而，由于采用云服务模式、运行模式以及用于提供云服务的技术，与传统 IT 解决方案相比云计算使组织可能面临不同的风险。

一个组织的安全状况的态势（security posture）取决于风险调整后实施的安全控制的成熟度，有效性和完整性。这些安全控制可以在一层或多层上实现，包括设施（物理安全）、网络基础设施（网络安全）、IT系统（系统安全），一直到信息和应用（应用安全）。此外，还包括人员和流程层面的安全控制，例如，职责分离和变更管理等。

如前文所述，在不同云服务模式中，提供商和用户的安全职责有很大的不同。例如，Amazon的AWS EC2基础设施作为服务，供应商负责Hypervisor层以下层次的安全责任，这意味着它们只负责诸如物理安全，环境安全和虚拟化安全等这些安全控制。与之相应，用户则负责与IT系统（实例）相关的安全控制，包括操作系统、应用和数据。

Salesforce.com 的客户关系管理（CRM）SaaS 产品正好相反。由于 Salesforce.com 提供了整个服务，提供商不仅负责物理和环境安全控制，还必须解决基础设施、应用和数据相关的安全控制。这减轻了许多用户的直接运行责任。

目前还没有一种方式，可以让一个没有经验的云服务用户简单地理解他/她的责任[虽然阅读本文将会提供帮助]，但 CSA 和其它组织正在努力进行与云审计相关的标准的制定。

云计算的吸引力之一在于由规模经济、重用和标准化带来的成本效益，为了支撑这种成本效益，云提供商提供的服务必须足够灵活，以服务最大可能的用户群、最大化他们的目标市场。不幸的是，将安全集成到这些服务方案中常会被认为使得方案变得僵化。

这种僵化往往体现在与传统 IT 相比，在云环境中无法获得同等的安全控制部署。主要原因是基础设施的抽象化、缺乏可视化和缺乏集成多种熟悉的安全控制手段的能力，特别是在网络层上。

---

下图说明了这些问题：在 SaaS 环境中，安全控制及其范围通过协商在服务合同中确认；服务等级、隐私和合规性等也都在合同中涉及。在 IaaS 环境中，底层基础设施和抽象层的安全防护属于提供商的职责，其它部分安全防护职责则属于客户。PaaS 介于两者之间提供了一个平衡，平台自身的安全防护转由提供商负责，而平台上应用的安全性及如何安全地开发这些应用则属于客户的职责。

<div style="text-align: center;">图6：如何集成安全</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_119_351_1104_1026.jpg" alt="Image" width="80%" /></div>


理解这些服务模式间的差异造成的影响以及如何进行部署对于管理组织的风险状况是至关重要的。

#### 1.5.3 架构之上: 关键关注领域

组成 CSA 指南的其它 13 个域着重介绍了云计算安全的关注领域，以解决云计算环境中战略和战术安全的“痛点”（pain points），从而可应用于各种云服务和部署模式的组合。

这些域分成了两大类：治理（governance）和运行（operations）。治理域范畴很广，解决云计算环境的战略和策略，而运行域则更关注于战术性的安全考虑以及在架构内的实现。

<div style="text-align: center;">表2a—治理域</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>域</td><td style='text-align: center; word-wrap: break-word;'>指南涉及.....</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>治理和企业风险管理</td><td style='text-align: center; word-wrap: break-word;'>组织治理和度量云计算带来的企业风险的能力。例如违约的判决先例，用户组织充分评估云提供商风险的能力，当用户和提供商都有可能出现故障时保护敏感数据的责任，及国际边界对这些问题有何影响等都是关注点。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>法律问题：合同和电子举证</td><td style='text-align: center; word-wrap: break-word;'>使用云计算时潜在的法律问题。本节涉及的问题包括信息和计算机系统的保护要求、安全漏洞信息披露的法律、监管要求，隐私要求和国际法等。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合规性和审计</td><td style='text-align: center; word-wrap: break-word;'>保持和证明使用云计算的合规性。本节涉及评估云计算如何影响内部安全策略的合规性、以及不同的合规性要求（规章、法规等）。同时还提供在审计过程中证明合规性的一些指导。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>信息管理和数据安全</td><td style='text-align: center; word-wrap: break-word;'>管理云中的数据。本节涉及云中数据的识别和控制；以及可用于处理数据迁移到云中时失去物理控制这一问题的补偿控制。也提及其它项，如谁负责数据机密性、完整性和可用性等。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可移植性和互操作性</td><td style='text-align: center; word-wrap: break-word;'>将数据或服务从一个提供商迁移到另一个提供商，或将它全部迁移回内部的能力。提供商间互操作性相关的问题也在这节讨论。</td></tr></table>

---

<div style="text-align: center;">表2b一运行域</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>域</td><td style='text-align: center; word-wrap: break-word;'>指南涉及......</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>传统安全、业务连续性和灾难恢复</td><td style='text-align: center; word-wrap: break-word;'>云计算如何影响当前用于实现安全性、业务连续性和灾难恢复的操作流程和规程。关注点是讨论和检查云计算的潜在风险，希望增加针对企业风险管理模式巨大需求的对话和讨论。进而，本节还讨论了如何帮助人们识别云计算在那些方面可以有助于减少安全风险，而在某些领域则增加了风险。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据中心运行</td><td style='text-align: center; word-wrap: break-word;'>如何评估提供商的数据中心架构和运行。主要关注帮助用户识别对持续服务不利的常见的数据中心特征，以及有助于长期稳定性的基础特征。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>事件响应、通告和补救</td><td style='text-align: center; word-wrap: break-word;'>适当的和充分的事件检测、响应、通告和补救。尝试说明为了启动适当的事件处理和取证，在用户和提供商两边都需要满足的一些条目。本域将会帮助您理解云给您现有的事件处理程序带来的复杂性。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应用安全</td><td style='text-align: center; word-wrap: break-word;'>保护在云上运行或在云中开发的应用软件。包括将某个应用迁移到或设计在云中运行是否可行，如果可行，什么类型的云平台是最合适的（SaaS, PaaS, or IaaS）。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>加密和密钥管理</td><td style='text-align: center; word-wrap: break-word;'>识别恰当的加密使用方法以及可扩展的密钥管理。本节并不是什么规范，而是提供更多信息来探讨为什么需要这些方法，识别使用过程中出现的问题，包括保护对资源的访问以及保护数据。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>身份和访问管理</td><td style='text-align: center; word-wrap: break-word;'>管理身份和利用目录服务来提供访问控制。关注点是组织将身份管理扩展到云中遇到的问题。本节提供洞察评估一个组织准备就绪进行基于云的身份、授权和访问管理(IdEA)。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>虚拟化</td><td style='text-align: center; word-wrap: break-word;'>虚拟化技术在云计算中的应用。本节论述了与多租户、VM隔离、VM共居（co-residence）、Hypervisor脆弱性相关联的风险。本域更关注系统和硬件虚拟化相关的安全问题，而不是对各种形式虚拟化的泛泛纵览。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>安全即服务</td><td style='text-align: center; word-wrap: break-word;'>提供第三方促进安全保障、事件管理、合规认证以及身份和访问监督。安全即服务是将安全基础设施的检测、修复和治理委托给一个具备恰当的工具和专业知识的可信第三方。这种服务的用户可以得益于在保护和加固敏感业务运作中获得专门的专业知识和前沿技术。</td></tr></table>

### 1.6 云部署模式

无论使用哪种服务模式（SaaS，PaaS，或 IaaS），都有四种云服务部署模式并可以衍生变化以满足特定需求。

由于市场供给和客户需求的成熟，会衍生新兴的云部署模式，意识到这一点很重要。这方面的一个例子是“虚拟专用云”——一种利用公共云基础设施中的私有或半私有的方式连接这些资源到用户数据中心的内部资源，通常是通过虚拟专用网络（VPN）连接。

---

设计 “解决方案” 时使用的架构思路，对将来方案的灵活性，安全性和流动性，以及协作能力都有明显的影响。依据经验，在四个领域中任意一个，其边界化(perimeterized)的解决方案效果都不如去边界化(de-perimeterized)的解决方案。

同样的道理，采取私有的还是开放的方案也需要仔细考量。

## 部署模式

公有云：云基础设施提供服务给一般公众或某个大型行业团体。并由销售云计算服务的组织所有。

私有云：云基础设施专为一个单一的组织运作。它可以由该组织或某个第三方管理并可以位于组织内部或外部。

社区云：云基础设施由若干个组织共享，支持某个特定的社区。社区是指有共同诉求和追求的团体（例如使命、安全要求、政策或合规性考虑等）。它可以由该组织或某个第三方管理并可以位于组织内部或外部。

混合云：云基础设施由两个或多个云（私有、社区、或公共）组成，以独立实体存在，但是通过标准的或私有的技术绑定在一起，这些技术促进了数据和应用的可移植性（例如，云间负载均衡的 cloud bursting 技术）。

### 1.7 建议

云服务的交付可以分为三种模式以及不同的衍生组合。这三种基本类型经常被称为 “SPI” 模型，其中 SPI 分别代表软件、平台和基础设施（作为服务）。

云软件即服务 (SaaS). 提供给用户的能力是使用服务商运行在云基础设施之上的应用软件。用户使用各种客户端设备通过 “瘦” 客户端接口，诸如浏览器等来访问应用（例如基于浏览器的电子邮件）。用户并不管理或控制底层的云基础设施，例如网络、服务器、操作系统、存储、甚至其中单个的应用功能，可能的例外是有限的用户特定的应用配置。

云平台即服务 (PaaS). 提供给用户的能力是在云基础设施之上部署用户创建或采购的应用，这些应用使用服务商支持的编程语言或工具开发。用户并不管理或控制底层的云基础设施，包括网络、服务器、操作系统、或存储等，但是可以控制部署的应用和应用程序托管的环境配置。

云基础设施即服务 (IaaS). 提供给用户的能力是云提供了处理、存储、网络及其它基础性的计算资源，以供用户部署和运行任意的软件，包括操作系统或应用软件。用户并不管理或控制底层的云基础设施，但是拥有对操作系统、存储和所部署的应用的控制，以及一些指定网络组件的有限控制（例如主机防火墙等）。

NIST 模型和本文并没有直接阐述新出现的云服务代理商相关的服务模式定义，这些提供商提供中介、监控、迁移/移植、治理、配置和集成服务，也提供用户和各云服务提供商之间关系的协调。

---

简而言之，由于创新会驱动快速的解决方案开发，用户和云服务提供商将会偏好诸如开发 API 和接口形式与云服务交互的各种方法。因此，云服务代理商将会成为整个云生态系统中重要的组成部分。

在通用、开放、标准化的长远解决方案出台之前，云服务代理商将各种不兼容的参数和接口进行抽象，为用户提供代理访问手段。所谓长远解决方案是指一种语义层面的功能，允许用户可以流畅和灵活地利用最能满足自己特定需求的模式。

同样重要的是要注意到出现了集中在开发开放和私有的 API 的许多努力，这些 API 用于云的管理、安全以及互操作。这些努力包括开放云计算接口工作组（Open Cloud Computing Interface Working Group），亚马逊公司的 EC2 API，Vmware 公司在 DMTF 提交的 vCloud API，Sun 公司的 Open Cloud API，Rackspace API 和 GoGrid API 等。开放的、标准的 API 会如同 DMTF 的开放虚拟化格式（OVF）这类通用容器格式一样，在云可移植性和互操作性方面将起到关键的作用。

目前有很多工作组、草案及已颁布的规范。在各种市场力量、用户需求和经济环境作用下会自然出现一个整合的过程，最终精简到更易于管理和互操作的状态。

### 1.8 要求

云服务呈现出的五个基本特征，表明了它们与传统计算方法的关系和区别：

✓ 按需自服务：用户自己可以按需自动配置计算能力，例如服务器时间和网络存储，而无需与服务提供商的服务人员交互。

✓ 多种网络访问：服务能力通过网络和标准的机制提供，促进瘦或胖客户端异构平台（例如移动电话、笔记本电脑和 PDA），以及其它传统的或基于云的软件服务的使用。

✓ 资源池化：提供商的计算资源汇集到资源池中，采用多租户模式，按照用户需要，将不同的物理和虚拟资源动态地分配或重新分配给多个消费者使用。虽然存在某种程度上的位置无关性，也就是说通常用户无法控制或根本无法知道所使用资源的确切物理位置，但是原则上可以在更高抽象层面上来指定位置（例如国家、州、省、或者数据中心）。资源的例子包括存储、处理能力、内存、网络带宽以及虚拟机等。即使是私有的“云”，在同一组织内部不同部门往往也趋向将资源池化。

✓ 快速弹性扩展：服务能力可以快速和弹性地供应，在某些情况下能自动地实现快速扩展、快速释放和回收。对于用户来说，可供应的服务能力近乎无限，可以随时按需购买。

✓ 服务可计量：云系统通过利用计量参数在某种级别抽象恰当的服务类型（例如存储、处理、带宽或者活跃用户账号等）自动控制和优化资源的使用。资源的使用可以被监控、控制并生成报表，对提供商和用户双方都透明。

了解云架构对安全架构的影响的关键是通用和简洁的词汇，加上一致的产品分类，这样云服务和架构可以被解构，映射到补偿的安全和操作控制模型、风险评估框架和管理框架，反过来遵从标准。

---

在部署云计算服务时，了解架构、技术、流程和人力资本需求是如何变化或保持不变是至关重要的。如果对高层架构的影响没有一个清醒的认识，是不可能理性地解决那些细节问题。本节架构概述，以及 13 个其它关键领域，为读者评估、运作、管理和治理云计算环境的安全提供了坚实的基础。

## 参考资料

[1] NIST 云计算定义

NIST 500-292 “NIST Cloud Computing Reference Architecture”

[2] NIST 云计算定义和 API 主页 www.cloud-standards.org

[3] Jericho Forum 云立方模型

www.opengroup.org/jericho/cloud cube model v1.0.pdf

---

<div style="text-align: center;"><img src="imgs/img_in_seal_box_101_554_1124_1150.jpg" alt="Image" width="83%" /></div>


## 第二部分 // 云的治理

---

## D2: 治理与企业风险管理

云计算中的治理和企业风险管理的基本问题关系到识别和实施适当的组织架构、流程及控制来维持有效的信息安全治理、风险管理及合规性。组织还应确保在任何云部署模型中，都有适当的信息安全措施贯穿于信息供应链，包括云计算服务的供应商和用户，及其支持的第三方供应商。

一个有效的云计算治理和企业风险管理方案源于完善的信息安全治理流程，作为组织整体企业治理责任的一部分应给予足够的重视。完善的信息安全治理流程要求信息安全管理程序支持业务的可扩展性，在整个组织中可重复执行、可测量、可持续、可防御、可持续改进，并具有持续的成本效益。

在云计算部署中，治理都将是云服务提供者和客户之间协议的主要内容。在定制的情况下，每一条款都需进行详尽的斟酌和协商。对于较大规模的客户或供应商，需要在细节关注和可扩展性之间进行权衡。可视特定工作负载的重要程度或风险价值来排定优先顺序（例如，响应时间和可用性对于邮件系统比 HR 系统更加重要）。随着云计算的不断成熟，CloudAudit 或 STAR 会提供更加标准的治理方法，并更具有可扩展性。

概览 本控制域主要讲述：

☑ 治理

☑ 企业风险管理

本章节映射到云控制矩阵控制点DG-01、IS-02、GRX-XML和CloudAudit以建立补偿控制。

### 2.1 公司治理

公司治理包括一整套流程，技术，习惯，政策，法律和机构，影响企业的指引、管理或控制。公司治理同时还包括管理众多利益相关者与企业目标之间的关系。良好的公司治理的基础，是基于承认股东作为公司实际拥有者的权利，以及高管作为受托方的模式。公司治理的模型众多,但是都遵循以下五项基本原则：

■ 供应链审计

董事会及管理层架构和流程

公司责任与合规（承诺）

财务透明和信息披露

■ 股权结构和控制权的践行

客户决定选择某公司的一个关键因素是相信他们的期望可以在这里得到满足。对于云计算服务，多个服务的相互依赖关系使客户难以理清责任方。如果客户对某厂商信心不足，该厂商获得合同的可能性将会很小。如果这成为一个普遍性问题，对单个厂商失去信心会连累到其他厂商，市场不健康的发展会增加意外发生和厂商更迭的可能性。

---

利益相关者需要仔细考量监控机制对公司持续稳定和增长是适宜和必要的。

### 2.2 企业风险管理

企业风险管理（ERM）植根于每个组织向股东提供价值的承诺。所有的业务都存在不确定性，管理层的挑战之一是决定一个组织如何测量、管理和降低不确定性。不确定性既是机遇也是风险，可能增加或减少组织及其战略的价值。

信息风险管理是识别和理解风险暴露、风险管理能力以及数据所有者风险偏好和承受能力。因此，这是基本的决策支持工具，以便持续投入以保护信息资产的保密性、完整性和可用性。

公司业务风险管理包括组织管理风险和机遇所使用的方法和流程。在云计算环境中，管理者为识别和分析出来的具体风险选择某种风险处置策略，其中可能包括：

避免：退出引起风险的活动

本章节映射到云控制矩阵控制点DG-08 和 ISO31000 的使用，ISF 和 ISACA 指引以建立补偿控制。

减少：采取措施减少相关风险的可能性或影响

分担或保险：用财务方式来转移或分担一部分风险

接受-基于成本/收益的考虑不采取行动

风险管理本质是一个平衡过程，实现目标未必需要减少不确定性或波动，而是根据风险偏好和战略一致的前提下，实现价值最大化。

在任何云的选择或方案当中，存在许多的不确定性、收益和风险，这些都会影响到从风险或业务收益的角度决策是否应用云计算服务。每一家公司都必须要权衡这些不确定性以决定是否采用云计算解决方案。

云计算为企业带来许多好处，包括：

☑ 优化资源利用率

为云计算租户节约成本

☑ 转换资本开销

资本开销（CAPEX）转化为运营成本（OPEX）

客户的 IT 动态扩展能力

缩短新应用程序开发或部署的生命周期

缩短了新业务实施的时间

---

用户应该将云服务和安全视为供应链安全问题。这意味着需要最大程度地检查和评估服务提供商的供应链（服务提供商的关联和依赖关系）。这也意味着需对服务提供商自身的第三方管理进行审查。对第三方服务提供商的评估应具体指向服务提供商在事件管理、业务连续性和灾难恢复等方面的策略、流程和规程；还应包括对共用场地（co-location）和备份设施的审查。这应包括审查提供商是否遵从其自身策略和规程的内部评估，评估服务提供商在这些领域为其控制的绩效和有效性提供信息的指标体系。

事件信息可以在合同、服务等级协议（SLA）或其他共同协议中进行定义，能进行自动或定期的沟通，并直接进入报告系统或传递给关键人员。关注等级和监督程度与风险价值相关-如果第三方无法直接访问企业数据，风险水平会显著下降，反之亦然。

使用者应审阅风险管理流程和他们服务提供者的治理并确保实践情况与之保持一致。

### 2.3 许可

## Permissions

■ 采用一个已建立的风险框架以便监控和度量公司风险。

采用风险管理效果衡量的指标（例如，SCAP $ ^{5} $、CYBEX $ ^{6} $或者GRC-XML $ ^{7} $）

确立以风险为核心的公司治理观点，高管层作为股东和利益相关人在供应链中的受信方角色。

从法律角度确立一个框架用来应对不同司法管辖区的差异。

### 2.4 建议

部分从云计算服务节省的费用须投资到提升服务提供商的安全能力、应用的安全控制和正在进行的详细评估和审计检查中，以确保能够持续满足需求。

用户组织应审查包括具体的信息安全治理架构和流程，及具体的信息安全控制，作为未来服务提供商组织的尽职调查（due diligence）的一部分。应根据用户信息安全管理流程的连续性、充足性、成熟度来评价服务提供商的安全治理流程和能力。服务提供商的信息安全控制应基于风险并明确地支持这些管理流程。

用户和服务提供商之间的协同治理架构和流程是很必要的，既是服务交付(services delivery)的设计和开发的一部分，也是风险评估和风险管理协议，最终作为服务协议的一部分。

在签订服务水平协议（SLA $ ^{8} $）及合同契约义务时应包括安全部门，来确保安全需求在合同层面上是可强制执行的。

---

在迁移进云端前，衡量信息安全管理有效性和效果的指标体系和标准都应建立起来。至少，组织应理解并记录他们当前的指标，及运营迁移至云计算平台时，这些指标会如何变动，因为云计算服务提供商可能使用不同的（有可能不兼容）指标。

由于许多云计算部署中缺少对基础设施的物理控制，因此与传统的企业拥有基础设施相比，服务水平协议(SLA)、合同需求及提供商文档化在风险管理中会扮演更重要的角色。

由于云计算中的按需提供和多租户特点，传统形式的审计和评估可能并不适用，或需要更改。例如，一些服务提供商限制脆弱性评估和渗透测试，而其他的则限制提供审计日志和实时监控数据。如果这些在内部策略中都是要求的，那么就需要寻找替代的评估方法、某些具体的合同免责条款，或寻找与风险管理需求更一致的服务提供商来替代。

如果对组织的关键功能使用云服务，风险管理方法应该包括识别和评估资产，识别和分析威胁和脆弱性，及威胁和脆弱性对资产（风险和事件场景）的潜在影响，分析事件/场景的可能性，管理层批准的风险接受水平和标准以及多种风险处置（控制、避免、转移、接受）计划的开发。风险处置计划的结果应作为服务合约的一部分。

服务提供商和用户的风险评估方法中的影响分析标准和可能性定义需保持一致。用户和服务提供商应共同开发云服务的风险场景，这应该固化在服务提供商为用户服务的设计中和用户的云服务风险评估中。

由于云计算及其服务提供商不断变化的状况，应考虑服务提供商的风险，例如，服务提供商的商业生存能力，数据和应用程序的可移植性和互操作性。

资产清单应盘点支持云服务且在服务提供商控制下的资产。用户和服务提供商的资产分类和分级方案（valuation scheme）应一致。

服务提供商及其服务都应该是风险评估的重点。云服务的使用、采用的特定服务和部署模式，都应该与组织的风险管理目标及业务目标一致。

☐ 不论是什么服务或部署模式，云计算服务的用户和服务提供商都应参与构建健全的信息安全治理。信息安全治理应由用户和服务提供商协作来达到支持业务使命和信息安全的目标。服务模式可以调整协同信息安全治理和风险管理中定义的角色和职责（基于各自对用户和服务提供商的控制范围），部署模式可能定义责任和预期（基于风险评估）。

云服务的用户应询问管理层对云服务风险和可接受残余风险的容忍程度是否已经有所定义。

如果服务提供商不能证明其服务具备全面有效的风险管理流程，用户应详细评估该服务提供商，以及是否使用用户自身的能力来补偿潜在的风险管理差距。

组织应为服务提供商制定基于业务和技术风险的风险指标。这些风险指标应包括数据涵盖类型，不同用户类型的相关信息，以及厂商和其他对手的相关信息。

### 2.5 要求

向利益相关方和股东保持透明度，并证明财政偿付能力和组织透明。

---

✓ 正视在云计算供应链相互依存的风险并与供应链各方沟通企业的风险状况，随时准备向消费者和依赖方告知风险情况。

✓ 检查和统计从其他云计算供应链继承的风险，采取积极的措施来降低风险并通过运营控制风险。

---

## D3: 法律问题：合同与电子发现

本域强调由云计算所引起的一些法律方面问题。本章提供将数据迁移到云上可能引起法律问题的一般背景、在云服务协议中要考虑的一些问题，以及在西方国家诉讼体系内电子发现（Electronic Discovery）所提出的特殊问题。

本域仅就所选择的问题提供概述，并不能替代您获得法律上的建议。

概述：本域将解决如下主题：

将数据迁移到云上所引起特殊法律问题的概述

云服务协议的考虑内容

电子发现引起的特殊问题

### 3.1 法律问题

纵观全球，众多国家有着不计其数的法律、法规以及其它的命令，它们要求公共组织和私营机构要保护个人数据的隐私性、信息和计算机系统的安全性。例如，在亚太地区、日本、澳大利亚、新西兰以及许多国家已经通过数据保护法律。这些法律要求数据的控制人依据经合组织（Organization for Economic Cooperation and Development，简称 OECD $ ^{9} $）的隐私及安全指导意见，以及亚太经合组织（Asia Pacific Economic Cooperation，简称 APEC $ ^{10} $）的隐私框架采用合理的技术、物理和管理措施来防范个人数据遭受丢失、滥用或是篡改。

在欧洲，欧洲经济区(EEA) $ ^{11} $成员国家已经制定数据保护法律，该法律延续了1995年的欧盟European Union(EU) Data Protection Directive $ ^{12} $数据保护指令、以及2002年的电子隐私指令（ePrivacy Directive，其在2009年得到修正）中阐述的准则。这些法律包含安全的组成部分，并必须将提供充分安全的职责传递给分包商。其它与欧洲经济区有紧密联系的国家，例如非洲的摩洛哥和突尼斯、中东的以色列和迪拜也已通过遵循同样准则的类似法律。

北美、中美以及南美国家也正在以快速的步伐通过数据保护法律。这些国家的法律都包括安全方面的要求，并且将确保个人数据防护和安全的重担放在了数据保管人身上。无论这些数据位于何处，特别是当向第三方传输时。譬如，除了加拿大、阿根廷以及哥伦比亚的数据保护法律已经出台多年外，最近墨西哥、乌拉圭和秘鲁也通过了数据保护法律。这些法律都主要受到欧洲模式的启发，并且也可能包括对亚太经合组织隐私框架的引用。

在日本，个人信息保护法案要求私营企业保护个人信息以及数据的安全。在医疗行业有行业特定的法律，如医疗从业者法案、公共健康护士法案、助产士和护士法案以及药剂师法案，这些法案要求注册的医疗职业人员对病人的信息进行保密。

---

在美国开展业务的组织可能受制于一个或多个数据保护法律。这些法律要求组织为他们分包商的行为负责。譬如，金融服务现代化法案（Gramm-Leach-Bliley Act (GLBA) $ ^{13} $）或是1996年发布的医疗保险及责任法案（Health Insurance Portability and Accountability Act，简称HIPAA）要求组织以书面合同的形式迫使他们的分包商采用合理的安全措施，并且遵守数据隐私条款。政府机构、例如联邦贸易委员会（Federal Trade Commission，简称FTC）或是美国司法部长一致同意组织对他们分包商的行为负有法律责任。支付行业数据安全标准（Payment Card Industry PCI Data Security Standards，简称PCI DSS）适用于世界上任何地方的信用卡数据，包括由分包商处理的数据也有类似的要求。

以下部分就个人数据被传输到云中、或是在云中处理时可能引发与之相关的法律问题提供一些例子。

<div style="text-align: center;">表一 强制性要求</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>问题</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>美国联邦法</td><td style='text-align: center; word-wrap: break-word;'>美国众多的联邦法律以及相关的规定，例如GLBA、HIPAA、1998年的儿童在线隐私保护法案（Children&#x27;s Online Privacy Protection Act，简称COPPA），它们与由联邦贸易委员会发布的命令共同要求公司在处理数据时采取专门的隐私和安全措施，从而在他们与第三方服务提供商的合同中要求类似的预防措施。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>美国州法</td><td style='text-align: center; word-wrap: break-word;'>美国众多的州法也要求公司有义务为个人数据提供充分的安全保护，并要求他们的服务提供商做同样的事情。解决信息安全问题的州法通常至少要求公司与服务提供商的书面合同里有合理的安全措施条款。例如可参见马萨诸塞州的安全法规下的广泛要求。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准</td><td style='text-align: center; word-wrap: break-word;'>例如像PCI DSS、或是ISO 27001这样的标准也引发类似联邦法以及州法那样的多米诺骨牌效应。受制于PCI DSS、或是ISO 27001标准的公司必须遵守特定的标准，并同时将类似的义务传达给他们的分包商以便满足受制约的这些标准。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>国际性规章</td><td style='text-align: center; word-wrap: break-word;'>许多国家已经通过遵循欧盟模式、经合组织或亚太经合组织模式的数据保护法律。在这些法律下，数据的控制人（通常是与个人有主要关系的法律主体）对收集和处理的个人数据负有责任，即使是在第三方处理数据的情况下。数据的控制人被要求确保任何代表它处理个人数据的第三方采取充分的技术、组织架构上的安全措施来保护数据。</td></tr><tr><td rowspan="2">合同责任</td><td style='text-align: center; word-wrap: break-word;'>即使未被规定要采取具体的活动，公司合同上可能有责任保护他们的顾客、联系人或是雇员的个人信息，以确保这些数据未被挪作他用、以及未泄漏给第三方。譬如，这个责任可能来自公司在其Web站点上发布的条款和隐私声明。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>此外，公司可能与它的客户签订合同（例如服务协议），在合同中对数据保护（个人或公司的数据）、使用限制、确保安全性、使用加密等做出具体的承诺。组织必须确保当由其监管的数据位于云中时，它会具备持续的能力满足在隐私性通告、或其它合同内所做出的许诺和承诺。</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>针对跨国界数据传输的禁令</td><td style='text-align: center; word-wrap: break-word;'>例如，公司或许已经同意数据只能用于特定的用途。在云中的数据必须只能用于它们被收集的目的。如果隐私性通告允许这些个人数据的主体访问他们的个人数据、修改或是删除信息，云服务提供商也必须允许其与在非云服务关系下同等程度地行使访问、修改和删除的权利。在全世界有许多法律禁止、或是限制信息传出该国。在大多数情况下，只有当接收信息的国家提供对个人信息、以及隐私权充分的保护时才允许信息传输。该充分保护要求的目的在于：确保那些跨国界被传输到别国数据的个人数据主体可以享有类似的、或是不低于数据传输前所在国家能够提供的隐私权利和隐私保护。因此对于云计算用户来说，知晓其雇员、客户以及其他人的个人数据将位于何处是重要的，以便能解决国外的数据保护法律可能施加给其的特定限制。依国家而定，确保该充分保护的要求可能是复杂的和严格的。在某些情况下，可能需要首先获得当地数据保护专员的许可。</td></tr></table>

### 3.2 合同考虑

当数据被传输到云中后，保护数据以及确保其安全通常是数据收集人或保管人的职责，即使在某些情况下这个责任可能与他人共享。当数据的保管人依赖第三方来持有或是处理数据时其对于任何数据的丢失、损坏或滥用仍然承担责任。数据的保管人与云服务提供商签署一份书面的（法律）协议是慎重的，并且可能是法律上需要的。该协议清晰地定义双方的角色、彼此的期望，以及在双方之间分配与数据利害攸关的众多职责。

上述讨论的法律、法规、标准以及相关的最佳实践也要求数据保管人进行尽职调查（在执行合同前）或安全审计（在合同履行期间），以确保这些责任得到履行。

#### 3.2.1 尽职调查

在签署云计算服务协议前公司应该评估自身的常规做法、需求以及限制条件，以便辨识与提议的云计算业务有关联的法律障碍和合规要求。譬如，它应该判断自身的业务模型是否允许使用云计算服务，以及在哪些情况下允许。业务的本质可能是任何放弃对公司数据的控制会受到法律的限制、或是导致公众产生严重的安全关切。

此外公司应该、并且在某些情况下可能是在法律上被要求对提议的云服务提供商进行尽职调查，以便判断是否其提供的服务能允许公司继续履行保护资产的职责。

#### 3.2.2 合同

双方必须签署书面的合同。根据服务的性质，合同通常可能是以点击协议的方式（click-wrap agreement）。此类合同是不可协商的，或是双方为特定的情况量身定造、协商一份更为复杂的书面文档。如果点击协议是唯一可用的协议，云服务客户应该对比云服务提供商承诺的实际收益、财务的节省和易于使用这些因素来权衡放弃协

---

商的风险。如果双方能够协商合同，他们应该确保在合同期内、以及合同结束后该合同的条款解决双方的需要和职责。双方应该协商详尽的、全面的条款，解决那些在云环境下运作所带来的独有需求和风险。

如果这些问题没有在合同中得到解决，云服务客户应该考虑达成该目标的备选方法，如寻找备选厂商或是不把数据传送到云中。例如，如果云服务客户打算发送 HIPAA 法案涵盖的信息到云中，他们将需要寻找愿意签署 HIPAA 职责相关协议的云服务提供商、或是根本不将数据传送到云中。

以下是一些 “云” 具体问题的简要描述。此外，附加的检查列表提供了评审云服务合同时需要考虑的一份综合的 (但不是包罗万象的) 问题清单。

#### 3.2.3 监控、测试和更新

云计算环境不是静态的。它在不断进化并且各方必须与之适应。建议对云服务进行定期的监控、测试和评估，以确保服务提供商采取了要求的隐私及安全措施，并且流程和策略得到遵循。此外，法律、法规以及技术的形势很可能以迅速的节奏发生变化。必须及时地解决新兴的安全威胁、新出现的法律和合规要求。各方必须与法律和其它要求齐头并进，并且确保运营保持在遵守可适用的法律之下；而且随着新的技术和法律浮现，要确保也有不断随之进化的到位的安全措施。

云审计以及云信任协议是自动监控和测试云供应链的两个机制。此外，国际电信联盟远程通信标准化组（ITU-T）正在致力于 X.1500 云审计规范，后者在被提及时通常被称作“网络安全信息交换框架”（Cybersecurity Information Exchange Framework，简称 CYBEX）。

### 3.3 电子证据发现引起的特殊问题

本节讨论的是美国诉讼的特殊要求。美国诉讼很大程度上依赖于文档为案件辩护。与其他大多数国家形成巨大反差的是，美国司法系统的特殊性是当事人必须提供给对手涉及到案件的所有文档。不仅必须提供有利于自己的文档，还必须提供有利于对方当事人文档。

近年来，已经有不少诉讼当事人被指控自行删除、丢失、或修改不利于自己的重要证据的丑闻。因此，议事规则也已变更来明确当事人的义务，尤其针对数字信息(ESI)。

由于云计算将成为诉讼或调查中所需要的数字信息的仓库，云服务提供商和他们的客户必须仔细规划如何识别案件涉及的所有文档，为了能够满足联邦民事诉讼规则中电子证据发现条款的严格要求，各州也要与这些法律条款相吻合。

在这点上，云服务的客户和供应商需要考虑下列问题，当面对一个客户的发现请求，并且可能相关的数据存在于云服务提供商。

#### 3.3.1 管有、保管与控制

在美国的大多数司法管辖区，各方生成相关信息的义务仅限于在其管有，保管或控制的文档和数据。相关的数据托管在第三方，即使是云服务提供商，一般也不免除一方当事人生成信息的义务，因为它可能有法律权利查阅或获得这些数据。然而，并非所有托管在云服务提供商的数据会在客户的控制下（例如，灾难恢复系统，云服

---

务提供商用于运行环境创建和维护的某些元数据）。区分哪些数据提供或不提供给客户可能牵涉到客户和供应商的利益。云服务提供商作为信息生成的云数据处理者，其法律程序方面的义务是每个司法管辖区亟待解决的遗留问题。

#### 3.3.2 相关的云应用和云环境

在某些诉讼和调查中，实际的云应用程序或云环境本身可能与解决诉讼或调查的纠纷有关。在这种情况下，云应用程序和云环境可能超出客户的控制，用户直接对供应商发出传票或其他的电子证据发现过程。

#### 3.3.3 可搜索性和电子证据发现工具

由于在云环境中客户可能无法和在自己的环境中一样申请或使用电子证据发现工具。此外，客户可能没有管理权限搜索或访问托管在云中的数据。例如，客户可以立即访问在自己服务器上的员工的电子邮件帐户，访问托管在云计算中的电子邮件帐户可能就不具备这种能力。因此，客户需要考虑导致受限访问潜在的额外的时间和费用。

#### 3.3.4 保持（Preservation）

一般来说，在美国一方有义务采取合理的措施防止在其管有、保管或控制的数据或信息被破坏或修改，它知道或理应知道保持数据或信息是有关于悬而未决或合理预期的诉讼或政府调查。根据客户使用的云服务和云部署模式，在云中保持与在其他IT基础设施中保持非常类似，也可以更复杂。

在欧盟，信息保持由欧洲议会和欧盟理事会 2006 年 3 月 15 日的指令 2006/24/EC 管辖，日本，韩国，新加坡也有类似的数据保护措施。在南美，巴西和阿根廷分别有阿泽雷多条例草案，阿根廷数据保留法 2004，以及 2004 年 2 月 6 号的 25.873 号法令。

##### 3.3.4.1 成本和存储

保持可以要求延长大规模数据的保留。根据服务等级协议这样的后果是什么？如果保持要求超出服务等级协议的条款，会发生什么情况？如果客户继续保持数据，谁支付延时存储，以及以怎样的代价？客户是否有在服务等级协议下的存储容量？客户可以有效地以友好的方式下载数据，从而可以离线或近线保持数据？

##### 3.3.4.2 保持范围

没有好的原由或具体需求，请求方仅有权访问托管在云中包含相关信息的数据，而不是所有在云中或应用程序中的数据。然而，如果客户没能以粒度方式保持相关信息或数据，可能需要过度保持（over-preserve）作为合理的保持，取决于诉讼或调查。

##### 3.3.4.3 动态和共享存储

如果客户有空间来容纳数据，保持云中数据的责任可能相对适中的，数据是相对静态的，访问的人是有限的，而且知道保持数据。然而，在云环境中以编程方式修改或清除数据，或与没有意识到数据需要保持的人共享，保

---

持变得更加困难。当客户明确这些数据是相关的，而且需要保持的，客户可能需要与供应商合作，以确定合理的方式来保持这些数据。

#### 3.3.5 收集

由于可能缺乏管理控制，客户收集来自云中的数据比收集防火墙后面的数据更困难，更耗时，更昂贵。特别是客户对其云中的数据可能不具有相同的能见度水平，和收集在云中的数据相比，可能有更多的困难来确定接口的完整性和准确性。

##### 3.3.5.1 接入和带宽

在大多数情况下，客户访问其在云中的数据将取决于服务等级协议。这可能会限制其快速、以良好的方式（即所有合理相关的元数据保持）收集大量数据的能力。客户和云服务提供商尽早地考虑了这个问题，在诉讼和调查允许收集的情况下，为额外的访问建立协议（和成本）。如果没有这些协议，当请求方和法院交涉时，客户应考虑在云中收集带来的额外的时间和成本。

##### 3.3.5.2 功能

关于接入和带宽是不同的。客户的访问权可以提供全方位的数据访问，但不提供在一个给定情况下更好地帮助他们的功能。例如，客户可访问三年的零售交易数据，但可能仅是由于功能限制，只能每2周下载一次数据。此外，客户可能无法看到所有实际存在的元数据的完整视图，而只是更有限度的元数据。

##### 3.3.5.3 取证

“云”数据源的位逐位镜像通常是困难或不可能的。为了安全起见，供应商不愿允许访问他们的硬件，特别是在多租户环境中客户能访问到其他客户的数据。即使在私有云中，取证也非常困难，客户可能需要将这些限制通知对方律师或法院。幸运的是，取证在云计算中很少批准，而不是因为它是云计算，但由于它通常是一个结构化数据层次或虚拟化，本身不适合取证分析。

##### 3.3.5.4 合理的完整性

客户面对请求发现应采取合理的措施以验证其从云供应商的收集是完整和准确的，尤其在日常业务流程不可用的情况和具体诉讼的措施被用来获取信息。这个过程除了验证都是独立的，存储在云中的数据是准确的，经过验证的，或可采纳的。

##### 3.3.5.5 无法合理访问

由于客户存储的数据及客户的访问权限和特权存在差异，并非客户在云中的所有数据都可访问。客户（和供应商）应该分析信息的要求和相关数据结构的相关性，物质性，均衡性和可访问性。

#### 3.3.6 直接访问

在云环境外，请求方对相应方的 IT 环境的直接访问是不支持的。在云环境中，更不被支持，可能和取证一样不现实。重要的是，客户可能无法提供直接访问是因为硬件和设施超出其管有、保管或控制，请求方需要传唤，或直接与供应商协商。

---

#### 3.3.7 本地生成

云服务提供商通常把数据存储在云中不受客户控制的高度专有的系统和应用程序中。原始格式的数据生成对请求方可能是无用的，因为他们将无法了解的信息生成。在这种情况下，可能最好的是要求所有有关方，包括生产方和供应商，相关信息的接口使用云计算环境中标准的报告或接口协议。

#### 3.3.8 认证

认证在这种情况下是指对被接纳为证据的数据的取证鉴定。这不应该被混淆为用户认证，用户认证只是身份管理的一个组成部分。将数据存储在云中不影响数据验证的认证分析，以确定数据是否应被接纳为证据。现在的问题是该文档是否是它所声称的。电子邮件不会因为它是存储在公司防火墙后面或存储在云中而被认为更可信或更不可信。问题是它是否被完整的存储以及法院能否相信从它被发送或接收后没有被改变。

#### 3.3.9 受理和信誉

如果没有其他证据，如篡改或黑客攻击，文件不应仅仅因为它们被创建或存储在云中就被认为更可信或者更不可信。

#### 3.3.10 在电子证据发现方面供应商与客户之间的合作

供应商和客户最好从合作的一开始就考虑（电子）发现导致的复杂度并在服务等级协议中说明，这符合他们的共同利益。供应商可能要考虑设计包括发现服务的优秀云产品来吸引客户（“发现设计”）。无论如何，客户和供应商应该考虑包含一项协议，对任何发现请求事件合理的相互配合。

#### 3.3.11 响应传票或搜索批准

云服务提供商可能被第三方以传票、搜查令或法院命令的形式要求其提供信息，获得对客户数据的访问请求。客户可能希望能对抗访问请求以实现数据的保密性和秘密性要求。为此，云服务协议应要求云服务供应商把收到传票的信息通知公司，并给公司时间来对抗访问请求。

云服务供应商可能受到诱惑答应开放其设施，并提供请求者访问请求中的任何信息。在这样做之前，云服务提供商应确保请求要求是在良好的秩序下，并采用适当的法律方法。云服务提供商在披露其保管的信息前应认真地分析要求。

复杂的法律适用取决于信息的具体性质，它的位置等。例如，访问电子邮件内容的请求适用不同的规则，这取决于电子邮件是否已经被打开，以及如何长期存储电子邮件。如果信息请求是电子邮件的内容，或只有交易数据的电子邮件适用不同的规则(例如，什么时候发送，发送给谁)。

---

## 参考文献

## International Treaties and Agreements

[1] OECD Guidelines on the Protection of Privacy and Transborder Flows of Personal Data (1980).

[2] OECD Guidelines for the Security of Information Systems and Networks (2002).

## Publications

[3] OECD Recommendation on Cross-border Cooperation in the Enforcement of Laws Protecting Privacy.

[4] GILBERT, Francoise. © 2009-2011. Global Privacy & Security. Aspen Publishing / Wolters Kluwer (2 volumes).

[5] GILBERT, Francoise. 2011. Cloud Service Providers Can Be Both Data Processors and Data Controllers (BNA Privacy & Security Law Report 10 PVLR 266 (2011)). Journal of Internet Law, Volume 15, Number 2, page 3.

[6] POWER, Michael E. AND TROPE, Roland L. 2005. Sailing in Dangerous Waters: A Director's Guide to Data Governance. American Bar Association.

[7] SMEDINGHOFF, Thomas. 2008 Information Security Law: Emerging Standard for Corporate Compliance (ITGP).

## Websites

[8] Cloud computing definitions and business models: http://p2pfoundation.net/Cloud ComputingDefinition (technical aspects, business models)

[9] Cloud Computing Incidents Database: http://wiki.cloudcommunity.org/wiki/CloudComputing:Incidents_Database (Records and monitors verifiable, noteworthy events that affect cloud computing providers, such as outages, security issues, and breaches)

---

## D4: 合规与审核

组织将其业务从传统数据中心迁移至云计算数据中心的选择将使其面临新的安全挑战，其中最重要的挑战之一即遵从众多监管条例对交付、度量和通信的合规约束。云计算服务用户和供应商需要理解和掌握当前合规和审核标准、过程和实践的区别和意义。云计算分布式和虚拟化的特性需要基于具体化的信息和过程实体进行重大的框架调整。

集中化和统一化的管理平台使云计算本身具备提升透明度和保障能力的潜力。此外，云服务供应商提供的外包方案降低了合规对规模的依赖程度。原本在云计算时代之前成本高昂的企业合规，将由于云服务供应商能够第一时间提供合规解决方案，使得企业（盈利性和非盈利性）能够获得市场准入开展业务。政府和其他原本抵触IT运维外包的组织考虑到安全性和合规性，将更积极采用云计算模型，其部分合规性需求将通过合约义务而满足。

此外对于云服务供应商和用户来说，其监管和审核机构也正在逐渐适应云计算这一新领域。仅有少量法律法规是面向虚拟化环境或者云部署模型的安全性证明而编写。云计算用户在向审核机构证明组织合规时将存在挑战。理解云计算与监管环境的相关性将是任何“云”战略的关键因素。云计算用户务必考虑并且理解以下几点：

针对特定的云服务或者服务提供商的监管含义，对适用跨境或者多管辖权的事例给予特别关注

云服务提供商和用户的合规责任分配，包括间接提供商（如你所采用云服务提供商的云服务提供商）

云服务提供商的合规呈现能力，包括及时的文档生成，证据产生以及过程合规

用户、服务提供商以及审核机构（用户和服务提供商双方）的关系，以确保按照需要的访问权（适当限制）并与治理要求相对应

## 概览 本章阐明如下主题：

☑ 合规

☑ 审核

---

### 4.1 合规

<div style="text-align: center;"><img src="imgs/img_in_image_box_210_184_1013_540.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 1—GRC Value Ecosystem</div>


公司治理：一个组织在股东，董事会和管理层之间达成控制平衡，能提供管理的一致性，方针、指南和控制项的结合应用，并支持有效地决策

企业风险管理：组织采用方法和过程（框架）来确保作出平衡的决策，该决策基于对组织目标（风险和机遇）相关的特定事件和场景的识别，可能性和影响级别评估，响应策略的采取，进展监控，从而保护和创造股东价值

合规性和审核保证：通过评估合规状态来对企业义务（企业社会责任、道德标准，适用法律，法律法规，合约，战略和方针）的感知和遵循，评估风险和不合规成本以及达成合规的开销，从而对必要纠正措施进行排序、储备和发起。

“云”所使用的信息技术受到日益增多的方针和法律法规约束。所有的股东期望组织主动遵守多重的监管准则与要求。IT治理对于满足相关要求是有必要的，同时，所有组织也需要采取战略来实现相关要求。

治理包括在外部环境约束下能够顺利达成组织目标的流程和方针。治理对合规活动提出要求，以确保运营完全满足上述流程和方针。从这层意义上说，合规的重点与外部要求相匹配（法律法规，工业标准），而治理则是与内部要求相匹配（董事会决定、企业方针）

合规可定义为对企业义务（企业社会责任、适用法律，道德指南）的感知和遵循，包括对适当和必要的纠正性措施的评估和排序。在某些高度监管的环境下，透明度可以对内部特定策略进行补充，成为组织效率的优势而非制约。

法律法规通常对信息技术和其治理来说意义重大，特别在监控、管理、防护和发布等方面。IT治理是企业总体治理、企业风险管理、合规和审核/保障的支撑要素。

“云”成为治理和合规的辅助技术，通过管理平台尤其是内部管理云实现集中化控制和透明度。透过云服务的影响，一定规模以下的组织可以与规模更大，资源优势更明显的企业达成同等级别的合规。安全和保障服务成为第三方参与合规评估和通信的一种方法。

---

任何合规方法都将需要包括 IT 部门在内的整个组织参与。外部供应商所承担的角色需要仔细思考，承担将其直接或者间接纳入治理的责任，并在用户组织内清晰地实现分配。

此外，以下标准分别代表了 ISO/IEC 和 ITU-T 发布的云安全标准：

ISO/IEC 27017：云计算安全和隐私管理系统安全控制

ISO/IEC27036-x:众多标准涉及供应商关系管理信息安全，后续计划将作为云供应链的一部分纳入。

ITU-T X.ccsec:通信领域云计算安全指引

ITU-T X.srfcts:基于云的通信服务环境安全要求和框架（X.srfcts）

ITU-T X.sfcse :软件即服务（SaaS）应用环境安全功能要求

### 4.2 审计

适当的组织治理顺理成章地包含审计与保证。必须独立地实施审计，并且应该坚定地设计审计以便表现出最佳实践、恰当的资源，以及经过检验的协议及标准。

对于客户和服务提供商而言，内审和外审以及各种控制措施都是合情合理的、可为云计算效力的角色。在引入云计算的起步阶段，更多的透明度可能是增加利益相关者舒适度的最佳选择。审计是提供保证的方法之一，其保证运营风险管理活动得到彻底地检验和评审。

组织最高级别的治理要素（例如董事会和管理层）应该采纳并支持审计计划。对至关重要的系统及控制进行定期且独立的审计，包括伴随的审计记录和文档将会支持提升效率和可靠性。

许多组织使用成熟度模型（例如 CMM、PTQM）作为分析流程有效性的框架。在某些情况下更多采用的是统计性的风险管理方法（例如用于金融服务的巴塞尔协议和偿付能力标准）。并且随着该领域的成熟，可以采用适用于职能部门、或业务线的更具专业性的风险模型。

对于云计算而言，我们需要修订和加强这些实践。正如之前的信息技术模型一样，审计需要充分利用云计算的潜力，同时增大范围和规模来管理它诸多的新颖性。

### 4.3 建议

当接洽（云计算）提供商时会牵涉到客户所属组织内适当的法务、采购以及合同团队。服务的标准条款可能并未涉及合规需求，需要就此进行协商。

对于受到高度监管的行业（例如金融业、医疗行业）来说，当使用云服务时应该考虑专门的合规要求。理解自身当前要求的组织应该考虑分布式 IT 模型的影响，包括云服务提供商运营于不同的地理位置以及不同的法律管辖区所带来的影响。

---

为每项工作负荷（例如整套的应用和数据），确定使用云服务将会如何影响现有的合规要求，特别是当与信息安全有关时。尽管有许多外包服务解决方案，组织仍需理解他们哪个云服务合作伙伴正在处理并应当处理受监管的信息。受影响的策略以及流程的例子包括活动报告、日志、数据保持、事故响应、控制测试和隐私权策略。

各方都应该理解各自的合同职责。期望值的底线将会由于部署模型而有所不同，在 IaaS 模型中客户拥有更多的控制权和职责，对于 SaaS 解决方案而言服务提供商扮演着统治性的角色。特别重要的是彼此受约束的要求和责任——不仅只是限于客户与他们直接的云服务提供商，而且也是在最终用户与提供商的云服务提供商之间。

遵守法规以及行业规定和要求（例如法规、技术、法律、合规、风险和安全等方面）是关键的，并且必须在要求确认阶段就解决。任何被处理、传输、存储的信息，或是被看作是个人可识别信息（Personal Identifiable Information，简称 PII）或私人信息都面临着世界范围内繁多的合规规定，这些合规可能随国家或州的不同而有差异。既然云计算被设计为是位于不同地区且可扩展的，解决方案中被存储、处理、传输或是检索的数据可能来自云服务提供商的众多场所或多个数据中心。一些法规明确规定的控制在某些云服务类型（例如地理上的要求可能与分布式的存储不一致）下很难、或是根本不可能实现。客户与提供商必须就如何收集、存储，以及共享合规证据（如审计日志、活动报告、系统配置）达成一致意见。

☐ 建议首选那些具有“云意识”的审计人员，他们熟悉保证虚拟化与云技术的挑战（以及优势）。

建议要求云服务提供商提供 SSAE 16 SOC2 或 ISAE 3402 类型 2 报告。这些报告将为审计人员和评估人员提供被承认的参考起点。

○ 合同应该提供给第三方（例如由双方选择的中间方）来评审 SLA 的度量标准及合规性。

### 4.4 要求

✓ 有权审计的条款赋予客户审计云提供商的能力，这支持在频繁地变化的云计算环境与法规内的可追溯性和透明度。使用有权审计的标准化规范来确保对彼此期望值的理解。最终，这个权利应由第三方的认证（例如 ISO/IEC 27001 或 27017 认证）所取代。

✓ 使用指定访问权限的透明度条款提供那些身处受到高度监管行业的用户（包括那些可将不合规作为刑事诉讼依据的行业）所需要的信息。该协议应该与自动产生或可直接访问的信息（例如日志、报告），以及“推送的”信息（例如系统架构、审计报告）区分开来。

✓ 云提供商应该定期（或是按需）地评审、更新并且发布他们的信息安全文档和 GRC（Governance, Risk and Compliance，简称 GRC）流程。这些资料应该包括漏洞分析以及相关的补救措施决策和活动。

✓ 第三方审计人员应由云提供商和客户事先共同披露或选择。

✓ 各方应就采用一个共同的 IT 治理和安全控制认证保证框架（例如 ISO 或 COBIT 标准）达成一致。

---

## D5: 信息管理与数据安全

信息安全的主要目标是保护那些为系统及应用注入动力的基础数据。伴随着企业向云计算环境的迁移，保护数据的传统方法则面临基于云的架构所带来的的全新挑战。高弹性的、多租户、全新的物理与逻辑架构，以及抽象控制均需要新的数据安全战略。在许多云部署方案中，用户往往将数据上传至外部，甚至上传到公共环境，而这一方式在数年前简直是不可想象的。

在云计算时代，管理信息对几乎所有组织来说都是所面临的一个严峻挑战，即使那些看上去并不热衷于云计算项目的组织也是如此。从管理内部数据开始，进而是云迁移，更进一步扩展至对广泛的、跨组织间的应用与服务所包含信息加以保护。因此，在云计算时代，信息管理和数据安全均要求新的战略与技术架构。幸运地是，不仅用户有所需的工具与技术，而且向云环境迁移数据也创造了在传统基础体系更好的保护数据的契机。

作者在推荐采用数据安全生命周期 Data Security Lifecycle（后面会详细介绍）来评估和定义云数据安全战略。这一安全战略应当基于明确的信息治理策略而分层细化，并通过诸如加密与特定监控工具等的关键技术实施而生效。

## 概览 本域包括三个小节：

第一节 提供云信息（存储）架构的背景资料

第二节 介绍包括数据安全生命周期 Data Security Lifecycle 在内的最佳实践

■ 第三节 详述数据安全控制及适用场景.

### 5.1 云信息架构

云信息架构与云架构本体相比较而言，都具有多样性；本小节可能不会覆盖到所有潜在的排列组合，仅针对大多数云服务中具有一定共性的架构而加以阐述。

#### 5.1.1 基础设施即服务

无论是在公有云还是私有云环境下，IaaS(基础设施即服务)，通常均包括如下存储选项：

原始存储。这包括用于存储数据的物理存储介质。原始存储在部分私有云的配置中可能会被映射为可直接访问。可能在某个私有云架构中被用于随机存取数据。

卷存储。这包括在 IaaS 实例中所附加的卷，最为典型的莫过于虚拟硬盘。这些卷通常使用 “数据离差（Data Dispersion）” 来实现可复原性与安全性。

---

- 对象存储。对象存储有时被当作文件存储来提及，较之虚拟硬盘，对象存储更像是一个通过 API $ ^{14} $或 Web 界面加以访问的文件共享。

内容分发网络。内容被保存在一个对象存储上，然后被分发到多个地理分布不同的节点以提高其网络消费速度。

#### 5.1.2 平台即服务

平台服务（PaaS）不仅提供并依赖于一个非常广泛的存储选项。

## PaaS 可提供：

数据库即服务。一个多租户数据库架构可直接被视为一项可供直接消费的服务。用户可根据交付类型不同而通过 API 或直接 SQL $ ^{15} $调用来使用该数据库。每一用户的数据则与其他租户的数据之间保持严格隔离及高度独立。，数据库本身则可能是关系型、平面型，或者任何其他通用架构。

- Hadoop/Mapreduce/大数据即服务。大数据是指具备大规模、广泛分布、异构性以及并发性/时间线等特性的数据，其必然要应用新的技术架构及分析机制。Hadoop和其他类似大数据应用或可以云平台形态交付。数据则通常被存放在对象存储或其他分布式文件系统中。数据通常与处理环境密切相关，或会会根据处理需要而临时移动。

应用存储。应用存储包括任何内置在 PaaS 应用平台中且可通过不同于其它存储类别中的 API 来调用的存储选项。

## PaaS 可消费：

数据库。信息和内容可被直接存储在数据库中（如：文本或者二级制对象）或以数据库可引用的文件形式间接存放。。数据库本身则可能是多个共享后端存储的IaaS实例集合。

对象/文件存储。文件或其他数据则存放在仅通过 PaaS API 接口可访问的对象存储中。

卷存储。数据可以被存放在那些旨在于对外提供 PaaS 服务的实例所附加的 IaaS 卷中。

其它。以上为绝大多数通用的存储模型，但这是一个不断更新的领域，因此仍会有新的选项可能出现。

#### 5.1.3 软件即服务

类似于平台即服务（PaaS），软件即服务（SaaS）可采用非常广泛的存储模型和服务模型。SaaS 存储通常可通过一个 Web UI 接口或 C/S 应用方式而加以访问。如果存储可通过应用程序接口（API）来访问，那么软件服务（SaaS）也可视为是平台即服务（PaaS）。很多软件即服务（SaaS）供应商同时也提供此类平台即服务（PaaS）的应用程序接口 APIs。

## SaaS 可提供：

---

信息存储与管理。数据通过 Web 界面输入到系统，并存储在软件即服务 SaaS 类应用程序中（通常是一个后端数据库）。某些 SaaS 服务也可提供数据集上传选项，或者平台即服务（PaaS）的应用程序接口 API。

内容/文件存储。基于文件的内容（如：报告、图片文件、文档等）可被存储在软件即服务 SaaS 应用中，并且提供基于 Web 的用户访问接口。

## SaaS 可消费：

数据库。与 PaaS 相类似，大量的 SaaS 服务依赖数据库后端于，即便是文件存储也不例外。

对象/文件存储。文件或其他数据被存放在对象存储中，且仅能通过 SaaS 应用方式加以访问。

卷存储。数据可以被存放在那些旨在于对外提供 SaaS 服务的实例所附加的 IaaS 卷中。

### 5.2 数据（信息）离差

数据（信息）离差是一种在无加密机制环境下广泛被用于提高数据安全性的技术。这些算法多（缩写为：IDA $ ^{16} $）：入侵检测算法）借助数据分段来对存储在云中的数据提供高可用性和安全保障，且被普遍应用于诸多云平台。在一个数据分段模式中，一个文件 f 被分成 n 个分段；所有这些分段都被签名并分发到 n 个远程服务器上。用户可任意选择 m 个分段来重构文件 f。分段机制也适用于云中需高安全性且长期存储的数据。

当分段机制与加密机制同时使用时，数据安全得到增强：入侵者不得不访问 m 个云节点以找回文件 f 的 m 个分段，同时还得破解已有的加密机制。

### 5.3 信息管理

在讨论特定的数据安全控制项前，我们需要一个模型来理解和管理我们的信息，信息管理包括在理解信息如何应用及如何治理应用中所采用的过程和策略。在数据安全小节，我们会讨论用于监控和治理等需求的特定的技术控制措施和建议。

### 5.4 数据安全生命周期

尽管信息生命周期管理是一个相对成熟的领域，它也还不能完全满足安全专家的需求。数据安全生命周期则不同于信息生命周期管理，它应反映安全受众差异化需求。（生命周期概述和完整版本可参考http://www.securosis.com/blog/data-security-lifecycle-2.0）生命周期从创建到销毁共有六个阶段，六个阶段尽管是以线性过程显示，但一旦创建，数据可在任意两个阶段间切换，无需一定一定遍历所有阶段（例如，并不是所有的数据最终会被销毁）。

---

1. 创建。创建就是产生新的数字内容，也可能是对已有内容的替换/更新/修改。

2. 存储。存储是将数据提交到某种存储库中，该

阶段通常在数据创建时并发产生。



3. 使用。数据被查看、处理以及不包括修改在内的其它各种使用方式。

4. 分享。信息本身就应可被诸如用户、客户、合作伙伴等所访问。

5. 归档。数据不再保持在可用状态而进入长期存储。

6. 销毁。使用物理或诸如密码粉碎之类的数字方式将数据永久销毁。

<div style="text-align: center;"><img src="imgs/img_in_image_box_706_215_1142_614.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">图一 数据生命周期</div>


#### 5.4.1 位置与访问

生命周期描述了信息的流转阶段，但并不涉及信息所在的位置及访问方式。

## 位置

可以用图解的方式来将生命周期视为一系列不同操作环境中更小的生命周期的集合，而并非单一的、线性操作。几乎处于任何阶段的数据都能在这些环境里输入或者输出。

由于所有潜在的监管、合同以及其它相关法规的要求存在，因此理解数据的逻辑和物理位置就显得非常重要。

## 访问

当人们知道数据存放在哪里以及如何移动时，他们就需要知道谁在如何访问数据。这里有两个因素：

1. 谁在访问数据？

<div style="text-align: center;"><img src="imgs/img_in_image_box_583_846_1139_1260.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图二 云访问设备</div>


2. 是如何访问的（设备及通道）？

今天，访问数据可采用各种不同的设备，这些设备又有不同的安全特性，并且使用不同的应用程序或者客户端。

---

#### 5.4.2 功能组件、操作主体和控制措施

功能组件是数据操作的功能模块，被主体执行（人或者系统），并有一个精确的位置。

## 功能组件

可使用三个组件来操作数据：

访问。浏览和访问数据，包括创建、复制、文件传输、分发，以及其它信息交换。

处理。执行数据的处理事务，如：更新数据，用来处理一个业务处理事务等。

存储。保存数据（在一个文件或数据库中）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_584_276_1115_560.jpg" alt="Image" width="43%" /></div>


下表展现了各种功能组件与数据生命周期各阶段的矩阵关系：

<div style="text-align: center;">表一 信息生命周期阶段</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>创建</td><td style='text-align: center; word-wrap: break-word;'>存储</td><td style='text-align: center; word-wrap: break-word;'>使用</td><td style='text-align: center; word-wrap: break-word;'>共享</td><td style='text-align: center; word-wrap: break-word;'>存档</td><td style='text-align: center; word-wrap: break-word;'>销毁</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>访问</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>处理</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>存储</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

一个操作主体（可以是人、应用程序或者系统/进程，而非访问设备）可在某个位置执行每个功能组件。

## 控制措施

一个控制措施限制了一系列可能发生的操作清单，直至之前已被允许的操作。下表是可能发生的操作清单的一种展现方式，用户可以使用该表来对照控制措施。

<div style="text-align: center;">表二 可能的和允许的控制措施</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">功能组件</td><td colspan="2">操作主体</td><td colspan="2">位置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可能的</td><td style='text-align: center; word-wrap: break-word;'>允许的</td><td style='text-align: center; word-wrap: break-word;'>可能的</td><td style='text-align: center; word-wrap: break-word;'>允许的</td><td style='text-align: center; word-wrap: break-word;'>可能的</td><td style='text-align: center; word-wrap: break-word;'>允许的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

---

### 5.5 信息治理

信息治理包括管理信息用途的策略和流程，有如下主要特征：

信息分类。高阶描述重要信息的分类。与数据分类不同，其目标不是为组织的每一个信息打标签，而是定义高阶分类，如“受控的”和“商业秘密”等用于明确需要的安全措施。

信息管理策略。策略用于定义各类信息被允许的操作。

位置及合规要求。数据可被存放的地理区域，以及这个区域的重要法律法规等。

■ 授权。定义各类员工和用户允许访问的信息。

所有者。谁最终应对信息负责。

保管职责。在信息所有人所遗留下来的信息中，谁该为管理这些信息承担责任。

### 5.6 数据安全

数据安全是指因信息治理的要求而采取的特定控制措施和技术。可分解成三部分，涵盖检测和预防）数据在云架构中的迁移，保护数据进入云以及在不同提供者/环境之间的传输，保护已在云中的数据。

#### 5.6.1 检测和预防数据在云架构内的迁移

组织所面临的云架构内的共同挑战就是管理数据本身。许多组织称，通常既没有得到许可，也没有作 IT 或安全通告，个人或业务单元就将敏感数据迁移到云设施上了。

除了传统的数据安全措施外（例如：访问控制或加密），还有两个步骤可帮助管理未经审批的数据向云服务设施的迁移：

1. 使用数据活动监测(DAM) $ ^{17} $和文件活动监测(FAM) $ ^{18} $来监控大量内部数据的迁移。

2. 使用 URL 过滤器和数据丢失保护 DLP 等技术监控数据向云中迁移的过程

## 内部数据迁移

在数据迁移到云之前，必须先将数据从所在的存储库中移出。数据库活动监控器可以监测到管理员或者其他用户在某个时刻将一个大数据集移出，或者做了一次数据库复制，而这可以表明有一次迁移正在发生。

文件活动监控器提供类似的文件库迁移保护，比如文件共享机制等

## 数据迁移到云

---

通过一个 URL 过滤器（比如 web 内容安全网关）和数据丢失防护（DLP: Data Loss Prevention）的联合机制可检测到有数据从企业环境迁移到云架构中。

URL 过滤器可以监控（和阻止）用户连接到云服务上，因为云服务的管理控制台通常与用户消费端位于不同的地址，所以用户能够明确的分辨出究竟是未知的某人人访问到管理控制台，抑或是真实用户访问了由供应商托管的应用程序。

与其寻找一个提供并持续更新的云服务清单的工具，还不如找到一个用于创建自定义类别及管理目标地址的用户的工具。

对于更细粒度的数据迁移，需要使用数据丢失防护（DLP）。DLP 工具监测实际传输的数据/内容，而不是仅对目标地址进行检查。因此用户就可进行基于数据分级的告警（或拦截）。例如，用户可仅允许将企业内部数据迁移到一个获得许可的云服务中，而拦截将同样内容迁移到一个未经授权服务之上。

DLP 方案的一个介入点就是数据泄漏的检测成功与否。例如，当企业网络环境外外部的各种用户（例如，员工、供应商、最终客户）进入企业边界时，是否绕过了任何 DLP 解决方案，以此来确保云解决方案的可用性。

#### 5.6.2 保护迁往云和在云内迁移的数据

在公共云和私有云部署方案中，无论什么服务模型，保护数据传输都是非常重要的。这数据传输过程包括：

数据从传统基础架构迁移到云供应商中，包括公有与私有之间转移，内部与外部之间转移，以及其他各种组合。

数据在云供应商之间的迁移。

数据在既定的云内实例间（或者其他组件之间）迁移。

有三种选项（或选择顺序）：

1. 客户端/应用程序加密。数据在终端或服务器端先加密，然后再通过网络传输，或者在已经以恰当的加密格式存储。这既包括本地客户端（代理模式）加密机制（例如，针对存储文件）或者集成在应用程序之中的加密机制。

2. 链路/网络加密模式。标准的网络加密技术包括 SSL、VPNs 和 SSH。既可以是硬件加密，也可以是软件加密。实现端到端加密当然是首选，但并适用用所有架构。

3. 基于代理的加密。数据通过一个代理设备或服务器进行传输，数据在网络传输前完成加密。通常都是将代理加密机制整合到原有的应用程序中，但我们并不推荐采用这种方式。

#### 5.6.3 保护云内数据的安全

云计算之中包括了非常广泛的技术与措施，就安全选项而言，也无法做到面面俱到。下面介绍一些更实用的技术与最佳实践，来保护各种云模型中的数全。

---

##### 5.6.3.1 内容发现

内容发现指的是用于识别存储的敏感信息的工具和过程。它允许组织定义基于信息类型、结构或分类的策略，然后使用先进的内容分析技术扫描存储数据，来确定其存储位置及是否策略违规。

内容发现一般来说是数据丢失防护 DLP 工具的特性之一，有时也会内置在数据库活动监视类 DAM 产品中。扫描可通过文件共享的访问方式或操作系统上运行本地代理的访问方式进行。这种工具必须是“云感知”化的，而且能够具备在云环境中有效工作的能力（如：能够扫描对象存储）。内容发现也可以一种可管理服务的形式存在。

##### 5.6.3.2 基础设施服务加密

###### 5.6.3.2.1 卷存储加密

卷加密可抵御如下风险：

保护卷免除快照克隆或泄漏风险

保护卷免除被云供应商（和私有云管理员）而随意查看的风险

保护卷免除物理硬盘丢失（这更像是一个实际发生的安全事件，而不是仅仅满足合规性要求那么简单）而导致的信息泄漏风险

基础设施服务的数据卷可通过以下三种方式加密：

■ 实例管理加密。这种加密引擎是在实例中运行，密钥被存放在卷中，并采用密码或密钥对进行保护。

• 外部管理加密。这种加密引擎同样在实例中运行，但密钥在外部管理，并响应实例请求而进行分配。

- 代理加密。在这一模型里，先将卷连接到一个特定的实例或设备/软件中，然后将该实例再连接到加密实例上。，代理处理所有的加密操作，并将密钥保管在代理内部或外部之中。在线方式或外携方式保管密钥。

###### 5.6.3.2.2 对象存储加密

对象存储加密用于抵御很多类似卷存储同样存在的风险。因为对象存储长期被暴露在公共网络上，并允许用户搭建虚拟私有存储（VPS）。就像 VPN 一样，VPS 在保护好数据的同时，可以使用公共共享的基础设施，即使这些数据被暴露，也只有那些有加密密钥的人才能查看。

文件/文件夹加密和企业数字版权管理 DRM。在将数据放到对象存储前，先使用标准的文件/文件夹加密工具或者企业数字版权管理工具（EDRM）加密数据。

客户端/应用程序加密。在一个应用程序（包括移动应用）里，对象存储通常被当作后端使用时，可以使用嵌入在应用程序内或客户端中的加密引擎加密数据。

代理加密。在数据发送到对象存储前，使用加密代理进行数据加密。

##### 5.6.3.3 平台服务加密

---

因为平台服务（PaaS）是多样化的，所以下面列表可能覆盖不了所有的选项：

客户端/应用加密。数据在 Paas 应用中加密，或者在访问平台的客户端程序中加密。

数据库加密。数据通过数据库内置的加密机制加密并存储于数据库中，这需要数据库平台支持这种加密机制。

代理加密。在数据发送到平台前，通过一个加密代理进行加密。

其它。其它可选项还包括在平台中内置加密 API，外部加密服务和其它可选形式。

##### 5.6.3.4 软件服务加密

软件服务（SaaS）供应商可以使用上述提到的任何一种选项，对于多租用式的隔离模型中，建议每个用户使用不同的密钥。以下选项可供软件服务用户使用：

服务提供方管理加密。数据在 SaaS 应用中加密，并通常由服务提供方管理。

代理加密。数据通过加密代理后再送到 SaaS 应用中。

使用共享密钥或公/私密钥对，以及额外的 PKI/PKO $ ^{19} $架构等在内的哪种加密操作最为适合，此处可参阅域11了解更多关于加密和密钥管理信息。

#### 5.6.4 数据防丢失保护

数据防丢失防护（DLP）可定义如下：

基于中心策略，通过深度内容分析识别、检测和保护数据的运转和使用及其它过程的产品。

DLP 能够发现是否违规操作数据并进行阻断操作（停止其工作流），或采用诸如 DRM、ZIP 或 OpenPGP 等加密机制处理后允许其继续运行。

DLP 常通过如下机制进行内容发现，监测数据运行：

专用设备/服务器。在云环境与其他网络/互联网边界，或云环境的两个子区域的抑制点部署标准的硬件。

虚拟设备

☑ 终端代理

Hypervisor 代理。相对于在实例中运行，DLP 代理则内置在 Hypervisor 层，或可在 Hypervisor 层得以访问到。

DLP SaaS。DLP 集成在一个云服务中（如：托管电子邮件），或者以一个独立标准的服务提供（一般是内容发现服务）。

---

#### 5.6.5 数据库和文件活动监测

数据库活动监测（DAM）工具定义为：

捕捉和记录细微的且实时或准实时发生的所有结构性查询语言（SQL）活动，包括数据库管理员跨多数据库平台的活动，并产生违规告警。

DAM 支持准实时的数据库活动监测并进行违规告警，如 SQL 注入攻击，或管理员未经授权的数据库复制操作。云环境下的 DAM 工具常以代理的方式连接到一个集中的收集服务器（该服务器也常是虚拟出来的）。它常被用于单个客户的数据库实例，但未来亦可用于平台服务 PaaS。

文件活动监控（FAM）定义为：

检测和记录指定文件库在用户级的所有操作记录，并产生违规告警。

在云环境中的 FAM 需使用一个终端代理，或在云存储和云用户之间部署一个物理设备。

#### 5.6.6 应用安全

较大比例的数据泄露是来自应用层攻击，特别是 Web 应用程序。可参考 D10 域了解更多应用安全信息。

#### 5.6.7 隐私保护保护

几乎所有的云存储系统都需要访问者（云用户或内容供应商）通过某种身份认证方式来建立信任关系，无论是单向通讯还是双向通讯均需如此。尽管加密证书能够为多数应用场景很多提供足够的安全性保障，但其因为与真人（云用户）而严格绑定而不适用于隐私信息。因为证书的任何一次应用均可能将证书持有者的身份泄漏给发起认证请求的团体。有很多场景（如：电子病历存储）就是因为采用了证书认证方式而不必要的暴露了证书持有者的身份。

在过去的十到十五年里，大量技术（如密码证书等）涌现，并且被用于使系统在值得信任的同时还能保护持有者的隐私信息（例如：隐藏真实持有者的身份信息等）。基于属性的证书就像普通加密证书（如 x.509 证书）一样都使用数字（或加密的）签名密钥。然而，基于属性的证书（attribute-based credentials, ABCs）允许持有者将其作为一个仅包含源证书内所含属性的子集封装在新的证书里。这些封装后的新证书能够被当作普通加密证书（使用公有密钥）来校验，以提供同样强度的安全保证。

#### 5.6.8 数字版权管理（DRM）

DRM 的核心就是用其加密内容，并应用一系列版权要求。版权要求既可以简单如防拷贝，也可以复杂如限定某组或基于用户的诸多活动集合，诸如剪切、粘贴、发送邮件、改变内容等。任何使用 DRM 进行数据保护的应用或系统必须能够解释和执行权限，这常常意味着系统需整合密钥管理系统。

这里有两种主要的数字版权管理分类：

---

消费者 DRM 多用于保护广泛分发的媒体内容，如：提供给广大受众的音频、视频和电子书。这一 DRM 可使用各种不同的技术与标准，但重点是都基于单向分发方式。

企业 DRM 是用于保护组织内部的信息和合作伙伴之间的信息。重点在于有很多复杂的权限、策略，以及与业务环境，尤其是企业目录服务 DS 的整合。

企业 DRM 能够很好地保护存储在云中的信息，但需要深度的基础架构整合。这对基于内容管理的文件和分发是非常有用的。消费者 DRM 能够为分发给消费者的内容有较好的保护，但是却因为大多数技术在单点上易被破解而无法保持很好的跟踪记录。

### 5.7 建议

理解所采用的云存储架构，有助于确定安全风险和可用的控制措施。

如果可能的话，选择支持数据离差技术的云存储。

☐ 使用数据安全生命周期 DSL 来识别易受攻击的安全，以确定最合适的控制措施。

○ 使用 DAM 和 FAM 监测内部核心数据库和文件库，识别能够表明数据向云中转移的的大数据迁移。

使用 URL 过滤和（或）DLP 工具监测员工的互联网访问，来识别是否敏感数据迁移。选择可对云服务作预分类的工具，并通过过滤规则阻断非授权行为。

所有敏感信息移入云或在云内传输时，应在网络传输前的网络层或者节点侧进行数据加密。这一建议适用于所有的云服务和部署模型。

☐ 使用任何数据加密机制时，应特别注意密钥管理（详见第 11 章）。

☐ 使用内容发现机制来扫描云存储，并识别已泄漏的敏感数据。

○ 加密 IaaS 中的敏感卷，来限制因为快照或未授权管理员访问导致的信息泄露。至于采用何种技术依赖于具体的操作需要。

☐ 采用文件/文件夹或客户端/代理加密机制加密对象存储中的敏感数据。

加密平台服务 PaaS 应用和存储中的敏感数据。通常情况下应用层加密机制为首选，因为几乎没有云数据库支持原生加密机制。

当使用应用加密时，密钥无论如何必须存放在应用系统外面。

若软件服务（SaaS）需使用加密，应尽可能使用可提供原生加密机制的供应商；若无该工具或必须到规定信任等级，则可使用代理加密机制。

○ 使用 DLP 来识别云部署的敏感数据泄漏，这种情况仅对基础设施服务（IaaS）适用，这对其他公共云供应商均不适用。

☐ 使用数据库活动监测工具（DAM）来监控敏感数据库，并对违反安全策略的行为进行告警。

---

☐ 当交付的基础设施或应用在正常访问敏感用户信息时，应考虑对可能的泄漏采取私有存储保护机制。

☐ 谨记绝大多数数据安全缺陷都源自于应用程序极为脆弱的安全性。

云供应商不仅应当遵循这些实践，并且为用户发布数据安全工具和配置选项。

无论是合同到期或其他原因，应在 SLA 中详细说明如何从云供应商供应商中转移数据，必须包括用户账号删除，从主/冗余存储中迁移或删除数据，迁移密钥等。

### 5.8 要求

✓ 使用数据安全生命周期来识别安全易受攻击点，从而确定最合适的控制措施。

✓ 考虑到潜在合规的、合约方面的以及其他法律方面的问题，应充分理解逻辑和物理数据。

✓ 使用 URL 过滤器和/或 DLP 工具监测员工的互联网访问，来识别敏感信息的传输。

✓ 在网络层或传输前在节点加密所有传输的敏感信息。

✓ 加密基础实施中的敏感卷，限制因快照或非授权访问的信息泄露。

✓ 在平台服务应用和存储中加密敏感信息。

---

## 参考文献

[1] RABIN, M. O. 1989. Efficient Dispersal of Information for Security, Load Balancing, and Fault Tolerance. J. ACM, 36(2), 335–348.

[2] SECUROSIS. 2011. The Data Security Lifecycle. http://www.securosis.com/blog/data-security-lifecycle-2.0

[3] SECUROSIS. 2011. Understanding and Selecting a Data Loss Prevention Solution. http://www.securosis.com/research/publication/report-data-loss-prevention-whitepaper

[4] SECUROSIS. 2008. Understanding and Selecting a Database Activity Monitoring solution. http://www.securosis.com/research/publication/report-selecting-a-database-activity-monitoring-solution/

[5] CHAUM, D. L. Feb. 1981. Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms. Communications of the ACM, 24 (2), 84-90.

---

## D6: 互操作性与可移植性

云计算的出现为每个组织机构的 IT 配置和管理带来了前所未有的不同于 “传统” 内部基础架构的可扩展性。组织机构得以响应动态变化中的处理需求，接近实时地添加、移动或者删除额外的容量。为满足增长的业务需求，一个新的应用支撑系统可以在数小时内而不是数周内启动起来；而当业务需求回落时，额外的容量可以同样快速地关停而不是让过剩的硬件设备在那里空转。从 IaaS 到 SaaS，任何基于云实施的系统都需要将互操作性和可移植性定为设计目标才能获得这种更加弹性环境的收益回报。

一方面，互操作性和可移植性允许你在全球范围内横跨多个独立的服务供应商来扩展一个服务，而且整个系统的运转就像是同一个系统。另一方面，互操作性和可移植性允许你轻松地将数据和应用从一个平台迁移到另一个平台，或者从一个服务供应商迁移到另一个服务供应商。

可移植性与互操作性其实并不是云环境所特有的考虑因素，并且与其相关的安全性问题也不是云计算所带来的新概念。然而，云计算中所存在的开放和往往是共享的处理环境带来了比传统处理模型中更加需要提前预防和准备的需求。多租户就意味着你的数据和应用与其它公司的数据和应用是共存的，而这种通过共享的平台、共享的存储和共享的网络访问到你的机密数据（不管是有意的还是无意的）是可能的。

本章定义了在设计互操作性和可移植性时需要重点考虑的因素。

概览 后续小节采用以下条目来定义互操作性和可移植性：

互操作性介绍

保障互操作性的建议

■ 可移植性介绍

■ 可移植性的建议

### 6.1 互操作性介绍

互操作性是对一个云生态系统中的各个组成构件的需求，以确保它们可以协同工作从而获得所期望的结果。在一个云计算的生态系统中，各个组成构件很可能来自于不同的地方，例如云和传统 IT 环境、公有云和私有云实现（所谓的混合云）。互操作性确保这些组成构件可以被不同供应商的不同的或者新的组成构件所替换并且继续工作，同样也将确保系统之间数据的交换。

随着时间的推移，商业企业一定会作出需要更换供应商的决策，需要更换的原因包括：：

合同续约时无法接受成本的增加

可以以更低的价格获得同样的服务

---

■ 供应商终止业务运营

■ 供应商突然停止一个或者多个正在使用的服务并且没有可以接受的迁移计划

无法接受的服务质量下降，例如无法满足关键性能需求或者达成服务水平协议 $ SLA's $^{20}

■ 云消费者与云供应商之间的业务纠纷争议

缺乏互操作性（可移植性同理）将导致云消费者被特定的云供应商锁定。

在考虑一个云项目的时候，互操作性所能达到或维持的程度依赖于云供应商使用开放或已公布的架构、标准协议以及标准 API's $ ^{21} $ 的程度。虽然很多声称 “开放” 和 “基于标准” 的云供应商会推出正常合理的挂接(hook)、扩展和增强(例如 Eucalyptus)，但这些也会影响阻碍互操作性和可移植性。

### 6.2 可移植性介绍

可移植性决定了应用程序组成构件无需担心供应商、平台、操作系统、基础架构、地理位置、存储、数据格式或 API，就可以被迁移和重用到别的地方的难易程度。

无论云迁移是向公有云、私有云还是混合云部署解决方案迁移，可移植性和互操作性都是必须要考虑的。无论迁移战略是向软件即服务(SaaS)，平台即服务(PaaS)还是基础架构即服务(IaaS)迁移，它们也都是服务模式选择的重要考虑要素。

可移植性是选择云供应商时一个关键考虑方面，它既可以帮助防止厂商锁定，也可以允许你在不同的云供应商解决方案之上部署相同的云以实现容灾目的或者实现分布式单一解决方案的全球部署，从而交付更多的商业价值与回报。

获得云服务的可移植性通常依赖于 D1 域所定义的云立方中采用相同架构象限的两种服务，服务是运行在不同的象限中，所以迁移一个服务往往意味着在将该服务重新外包到一个可选的云服务之前需要先将该服务迁回到“内部”。

在云迁移项目中如果不能很好地处理可移植性和互操作性有可能导致无法获得迁移到云的收益和回报，而且会因为以下本来应该避免的因素导致成本问题或者项目延误：

应用软件、厂商或服务供应商的锁定 — 选择某个特定的云解决方案可能会限制迁移到另一个云服务或者云供应商的能力

处理导致服务中断的不兼容性和冲突 — 供应商、平台或者应用的差异性可能会引发不兼容并导致应用程序在不同云基础架构中运行时发生故障

预期之外的应用程序返工或者业务流程变更 — 迁移到一个新的云供应商时，为保留应用程序原有的行为状态会产生重新制定流程运作的要求或者代码变更的需求

---

额外成本的数据迁移或数据转换 — 缺乏可互操作和可移植的数据格式可能会在迁移到新的供应商时产生计划外的数据改变

■ 新应用程序或管理软件的重新培训或者工具改造

数据或者应用的安全缺失 — 迁移到新的供应商或者平台时可能会因为供应商之间不同的安全策略或者控制点、不同的密钥管理或者数据保护措施产生无法察觉的安全缺陷

将服务迁移到云也是一种外包方式；外包的黄金原则是“预先了解并为如何退出合约作准备”。可移植性（和一定程度上的互操作性）应该成为任何迁移到云服务的组织战略的关键评判标准，以便制定可靠的退出策略。

### 6.3 建议

#### 6.3.1 互操作性建议

## 硬件—物理计算机硬件

硬件设备会随着时间的推移和供应商的更换无法避免地发生变化和改变，所以如果需要直接访问硬件设备就难免产生互操作性差异。

○ 任何时候在可能的情况下，尽可能采用虚拟化以消除硬件层的关联，需要记住的是虚拟化并不会消除所有硬件设备的考虑，尤其是在现有的系统中。

如果一定要直接访问硬件设备，重要的是要确保在从一个供应商向另一个供应商迁移时具有同等或者更好的物理和管理安全控制点。

## 物理网络设备

不同服务供应商其包括安全设备在内的网络设备和设备的 API 以及配置流程都会有所不同。

为确保互操作性，在虚拟域中应采用网络物理硬件和网络及安全的抽象。尽可能 API 应该具备相同的操作功能。

## 虚拟化

虽然虚拟化有助于消除物理硬件设备的顾忌，但是要区分出常见 Hypervisor 之间存在的差异（例如 XEN, VMware 以及其它的 Hypervisor）。

☐ 采用象 OVF 这样的开放虚拟化格式有助于保障互操作性。

o 不管采用哪种格式都需要记录并了解使用了哪种特定的虚拟化挂接（hooks）。每种格式都仍有可能在其它的 Hypervisor 上无法工作

## 梶架

不同的平台供应商会提供不同的云应用框架，而它们之间必然存在的差异性会影响互操作性。

---

通过调查研究 API 以确定差异性所在，并且为迁移到新的供应商时任何必要的应用程序处理变更作好准备。

采用开放的和已公布的 API 以确保最广泛地支持组成构件间的互操作性和便于必须要更换服务供应商时应用和数据的迁移。

云中的应用程序往往是通过互联网来交互的，而断路也是意料中会发生的事情。所以需要确定当一个组成构件发生故障（或者响应缓冲）时如何影响其它的组成构件，避免当远端组成构件发生故障时会造成系统数据完整性风险的状态依赖性。

## 存储

不同类型的数据对于存储的需求不尽相同。结构化数据多数情况下会需要数据库系统或者需要应用程序特定的格式。非结构化数据通常会遵从字处理、表格处理和幻灯片管理程序所使用的一系列常用应用格式中的某一种。这里我们需要考虑的是如何无缝地将一个服务所存储的数据迁移到另一个服务。

☐ 将非结构化数据存储为已经确立的可迁移的格式。

☐ 评估数据传送中加密的需求。

☐ 检查可兼容的数据库系统，需要的情况下评估转换需求。

## 安全

云中的应用程序和数据所处的系统不是用户所有，并且用户往往只能进行有限的控制。关于可互操作安全性需要考虑的一些要点包括：

认证采用 SAML 或者 WS-Security 以便控制点可以与其它采用标准的系统进行交互。参见域 12 了解更多细节。

在数据存放到云上之前对其进行加密可以保障其在云环境中不会被不恰当地访问。参见域 11 了解更多关于加密的细节。

如果已经使用了加密密钥，需要研究密钥是存在哪里和如何存放的以确保对于加密数据的访问可控。参见域 11 了解更多关于密钥管理的细节。

了解由于服务供应商未曾预料的保护措施“缺限”而产生安全损害时你所拥有的责任和权利。

日志文件信息需要与迁移到云上的所有其它数据一样采用相同安全级别处理。确保日志文件可以互操作以确保迁移前与迁移后日志分析的连贯性以及无论使用何种日志管理系统的兼容性。

☐ 完全迁移后应确保所有的数据、日志和其它信息从原有系统中删除。

#### 6.3.2 可移植性建议

向云上迁移的途中会存在各种各样的问题，会影响到向云上迁移的可移植性考虑因素和建议包括：

---

服务水平。不同的供应商服务水平协议(SLA)会有所差异，所以需要了解这种差异将会如何影响你更换云供应商的能力。

架构的差异。云中的系统可能会存在于不同的平台架构之上。了解服务和平台的依赖性以认识这种差异将会如何限制可移植性是非常重要的，服务和平台的依赖性可能会包括 API、Hypervisor、应用逻辑以及其它的约束条件。

☐ 安全集成。云系统引入了为保障安全性所特有的可移植性考虑因素，包括：

用户或者进程访问系统的认证和身份管理机制现在必须贯穿一个云系统的所有组成构件运作。采用类似SAML这样的开放标准对身份进行管理有助于保障可移植性。开发内部的支持SAML声明的IAM系统和可以接受SAML的内部系统有助于未来系统到云上的可移植性。

☐ 加密密钥应该在本地由第三方保管，如果可能的话也在本地维护。

元数据是数字信息的一个方面，由于（通常）在文件和文档上工作时元数据并不直接可见所以元数据经常被轻易忽视。由于元数据随着文档而移动，所以在云中元数据就变成了重要的考虑因素。将文件和其元数据迁移到新的云环境时，需要确保文件元数据的拷贝安全地清除以防止此类信息被遗留并产生可能的安全泄露。

#### 6.3.3 不同云模式的建议

以下为一些对所有云模式均适用的通常的风险和建议。

更换云供应商时遇到原有云供应商的抵触是很正常的。所以必须参照域 3 中描述的在合同流程中、域 7 中描述的在业务连续性计划中、域 2 中描述的作为完整的管控组成部分对此进行计划。

了解托管在一个云供应商的数据集合的大小。大量的数据可能会导致转换过程中服务的中断或者超出预期的转换窗口。很多客户发现对于较大的数据集采用硬盘快递要比采用电子传输快得多。

记录安全架构和每一个组成构件安全控制点的配置以便用于支持内部审计，同时还有助于向新供应商的迁移以及新环境的验证。

## 基础架构即服务（IaaS）

云供应商的职责是提供基本的计算资源例如存储、计算等等，而云消费者则需要对涉及互操作性的大部分应用设计任务负责。云供应商应该提供可以以最小代价与各种完全迥异的系统进行交互的标准化的硬件和计算资源。云供应商应该严格地遵循行业标准以确保互操作性。云供应商应该可以支持诸如云中介、云爆发（Cloud Bursting）、混合云、多云联邦(Multi-cloud federation)等等复杂应用场景。

了解虚拟机镜像如何被获取并被迁移到新的云供应商和谁可能会采用了不同的虚拟化技术。示例：DMTF(Distributed Management Task Force)的开放虚拟化格式（OVF）。

○ 识别并消除（或者至少记录）任何厂商特有的虚拟机环境扩展。

了解一个应用从云供应商迁出后有哪些可以确保恰当移除虚拟机镜像的实践可用。

---

了解可以使用的废弃磁盘和存储设备的实践。

☐ 应用/数据迁移前了解需要识别出来的硬件设备/平台的依赖性。

向原有云供应商要求访问系统日志、使用痕迹、访问记录和计费记录。

○ 识别与原有的云供应商部分或全部恢复及至扩展服务的选项如果新的服务被证明更差。

☐ 确定是否存在任何新供应商不兼容或者未实现的在用的管理层功能、界面或者 API。

了解数据在云供应商之间迁移时可能会涉及到的费用。

确定哪些手段可以用来支持类似于数据压缩这样的可以尽可能高效地将数据往云上迁移的标准能力。

了解提供了哪些安全措施以及谁来维护加密密钥的访问。

## 平台即服务（PaaS）

云供应商负责提供云消费者可以在其上构建自己系统的平台。他们提供运行环境和预集成的程序堆栈。开发人员可以快速地在所提供的平台之上开发和部署定制应用而无需自行构建基础架构。云供应商为云消费者提供完整的基础架构和维护管理。

在可能的情况下，尽可能使用采用了标准语法、开放 API 和开放标准的平台组成构件，例如 $ (OCCI)^{22} $。

☐ 了解哪些工具可以用来实现安全数据传输、备份和恢复。

了解并记录 PaaS 供应商特有的应用组件和模块，开发具有抽象层的应用架构以最小化对专有模块的直接访问。

了解类似于监控、日志和审计这类的基础服务如何转移到一个新的供应商。

了解为放置在云上与在云上产生和维护的数据提供了哪些保护措施。

了解原有云供应商所提供的控制功能以及如何将其对应转换到新的云供应商。

迁移到新的平台时，了解迁移后对应用的性能和可用性的影响以及这些影响如何度量。

了解迁移前与迁移后如何完成测试以验证应用或者服务正常运行。确保供应商和用户在测试中的职责是明确的并且记录下来。

## 软件即服务（SaaS）

云供应商在云上提供应用软件能力，云消费者只需要管理自己的操作和信息在系统中的流入和流出。客户只需要一个浏览器，而所有层面的主要的管理维护工作是由云供应商来负责。

o 定期将数据抽取和备份成没有 SaaS 供应商也可以使用的格式。

☐ 了解元数据是否可以被保存和迁移。

---

如果需要可以采用第三方数据保管服务。

理解任何定制工具都可能需要重新开发，或者新的供应商必须提供这些工具或者承诺迁移（与支持）这些工具。

☐ 检视和审计以确保新旧服务供应商的控制点有效性是一致的。

☐ 确保法务和合规原因所需的日志、访问记录和任何其它相关信息的备份和其它拷贝可以迁移。

了解管理、监控和报表接口以及它们在不同环境间的集成。

☐ 迁移之前测试和评估所有的应用程序，如果可行的话在切换之前采用双系统并行

## 私有云

私有云是云消费者在企业内部运行云环境/服务，或者采用云供应商所提供的私有云服务（通常是将企业内部网络延伸到供应商的托管中心）。

确保常见 Hypervisor,例如 KVM、VMware、Xen 之间的互操作性。

确保管理功能采用标准的 API 例如：用户和权限管理、虚拟机镜像管理、虚拟机管理、虚拟网络管理、服务管理、存储管理、基础架构管理、信息管理等等。

## 公有云

公有云的互操作性意味着开放出最通用的云接口。它们可能是厂商特定的或者像 OCCI、Libcloud 等等这样的开放的规范和接口。

☐ 确保云供应商开放出可以访问其服务所有云功能的通用的与/或开放的接口。

## 混合云

在混合云的场景下云消费者的本地私有基础架构需要具备与外部云供应商协同工作的能力。一个常见的场景是 “云爆发” (Cloud Bursting)，在这个场景下企业借用外部云供应商来分担高峰需求时的负载。

☐ 确保云供应商开放可以访问其服务中所有云功能的通用的与/或开放的接口。

确保可以与不同云供应商进行联邦的能力以实现更高水平的可扩展性

---

## 参考资料

[1] http://msdn.microsoft.com/en-us/library/cc836393.aspx

[2] http://blogs.msdn.com/b/eugeniop/archive/2010/01/12/adfs-wif-on-amazon-ec2.aspx

[3] http://download.microsoft.com/download/6/C/2/6C2DBA25-C4D3-474B-8977-E7D296FBFE71/EC2-Windows%20SSO%20v1%200--Chappell.pdf

[4] http://www.zimbio.com/SC+Magazine/articles/6P3njtcljmR/Federation+2+0+identity+ecosystem

[5] http://www.datacenterknowledge.com/archives/2009/07/27/cloud-brokers-the-next-big-opportunity/

[6] http://blogs.oracle.com/identity/entry/cloud computing identity and access

[7] http://www.opengroup.org/jericho/cloud cube model v1.0.pdf

[8] http://www.burtongroup.com

[9] http://www.pkware.com/appnote

[10] http://www.apps.ietf.org/rfc/rfc4880.html

---

<div style="text-align: center;"><img src="imgs/img_in_seal_box_125_584_1147_1177.jpg" alt="Image" width="83%" /></div>


## 第三部分 // 云的运行

---

## D7: 传统安全、业务连续性和灾难恢复

云计算作为一种广受欢迎的 IT 运营外包技术出现以来，云计算这种托管模式所带来的安全问题正受到批判，云计算安全变得越来越重要。云计算概念的内在风险是如何确保储存在第三方或纯粹云计算服务提供商(CSP) $ ^{23} $处私密和敏感数据的安全。

云计算服务模式已经演变到企业实体只需要付出较少的成本就可以做更多的事情：也就是说，提供较少的资源，但能得到更好的运营效率。这对于企业经营来说则能够获得很多实实在在的好处。但是，云计算存在很多内在安全风险，在企业具有足够的信心决定把他们的 IT 需求外包给云计算服务提供商之前，不得不去评估和试图解决这些安全风险。

本安全域的一个目标是帮助云用户去形成一个对云计算服务相关的传统安全（物理安全）共识。传统物理安全被定义为采取一些安全措施来确保数据和人员的安全和物质存在，防止被盗窃、间谍活动和

本节于云控制矩阵的IS-01 和 IS-02 以及ISO/IEC 27002 的第9条款对应.



蓄意破坏。在云计算信息安全上下文中，这些资产指的是信息、产品和人员。

正确的信息安全方案一般是采取多层安全机制来达到其安全目标，也就是通常所说的多层安全或深度防御。当实施安全措施时，管理员应该认识到，没有哪个安全措施是百分之百安全的。信息安全必须采取深度和多层防御的方法来达到一个综合安全水平。这些安全层中的任何一个脆弱点都可能导致安全被破坏。物理保护只是多层安全防御战略以确保云计算信息安全中的一个最初步骤。如果针对云计算的物理保护不存在、没有正确实施、保护力度较弱、安全执行不一致、或者只是作为一个项目对待（做完了事），则最安全的逻辑层面措施也无法弥补物理安全上的弱点，后果是，可能导致安全防护整体失败。

一种有效的传统安全流程是，首先需要一系列完好设计的风险评估、脆弱性分析，以及对业务连续性计划和灾难恢复（BCP/DR）策略、过程和流程的经常审查和测试。一个设计完好的物理安全程序应该是，物理安全可随着业务扩展，在组织内部可重复、可测量、可持续和站得住脚，整个过程能够在一个经常性的基础上进行持续改进，并且经济有效。

概览：一些和云计算相关的安全风险是云计算所特有的，在这种情形下，一个云计算服务提供商的业务连续性、灾难恢复和传统安全环境都需要全面评估（比如，采用标准的工业指南如 TOGAF $ ^{24} $、SABSA $ ^{25} $、ITIL $ ^{26} $、COSO $ ^{27} $ 或 COBIT $ ^{28} $）。本安全域解决一下安全问题：

## ■ 建立一个物理安全机能

本节对应云控制矩阵 FS-01, FS-02, FS-03, 和 FS-04，以及 ISO/IEC 27002 第 9 条款。

---

☑ 人力资源物理安全

■ 业务连续性

■ 灾难恢复

### 7.1 建立一个传统安全机能

很多组织经常忽略那些 IT 设备、网络技术和通讯网络上过时的物理安全措施。这将导致很多组织在楼宇里安装计算机设备、网络和网关时，都没有采取正确的、可确保资产安全或维护方便的物理设施。

要为云计算环境中的 IT 设备、网络技术和通讯资产建立恰当的物理安全，将责任落实到云计算服务提供商组织中具体的人员是至关重要的。在云服务提供商组织内部，一个承担具体管理职责的个体有责任对相关的规划和程序进行有效的管理、规划、实施和维护。负责物理安全的员工需要接受培训，并且需要评估其工作能力。为了建立适合云计算环境的物理安全机能，必须考虑以下问题：

各受保护设备和服务的安全需求

■ 被安排来负责物理安全的人力资源情况

将遗留应用迁移到云之前，对其物理安全是如何管理和分工的

■ 可投入到安全方面的资金情况

物理安全可以是如增加一扇带锁门一样简单，也可以像实施一个包括障碍物和武装安全保卫人员的多层安全防御方案一样复杂。一个正确的物理安全实施方案应该使用多层防御概念，采用恰当的组合，通过阻止和延迟物理安全威胁来对风险进行管理。对基础设施、人员和系统构成物理安全威胁的攻击不只是局限在入侵行为。为了抵御这些风险，必须组合部署各种主动和被动防御措施，这些措施包括：

用来阻止和延迟事件、事故和攻击的障碍

■ 用来监控安全和系统环境状态的检测系统

用来击退、拘押或劝阻攻击者的安全响应措施

物理安全在设计和实施时通常采用如下几种形式之一：

环境设计

机械的、电子的、程序控制

检测、响应和恢复过程

■ 人员识别、认证、授权和访问控制

■ 安全策略和过程，包括对人员的培训

---

#### 7.1.1 安全物理安全评估

当评估一个云服务提供商的传统物理安全时，云用户需要 IaaS 多个方面的信息，或者基础数据中心提供商的物理存在相关的信息，这包括物理设施的物理位置，以及对关键风险和恢复要素的文档记载等等。

##### 7.1.1.1 CSP 设施的物理位置

云用户应该对数据中心的物理位置进行一个关键评估。如果它们依赖于一个云供应链，清楚地知道云基础设施的哪些部分存在依赖性是非常重要的。

以下是在评估设施物理位置时的一些建议：

检查这些设施的位置是否位于任何地震活跃地带，以及地震活动可能造成的风险。

这些设施不应该位于存在以下风险的地理区域：洪水、滑坡或者其它自然灾害

这些设施不应该位于那些高犯罪率、政治或社会动荡的区域

检查对这些设施的位置的可达性（以及不可达可能发生的频率）

##### 7.1.1.2 文档审查

那些支持业务恢复操作的文档对于评估托管企业能在发生灾难性事件时及时响应的能力是至关重要的。当我们准备和一个物理数据中心提供商签约前，以下的文档集合应该被审查：

☑ 风险分析

☑ 风险评估

脆弱性评估

■ 业务连续性计划

■ 灾难恢复计划

物理和环境安全计划

■ 用户账户终止流程

意外事件计划，包括测试计划

事故报告和响应计划，包括测试协议

■ 应急响应计划

设施结构图一应急出口、CCTV监控头位置、安全入口等

消防疏散示意图和消防指令程序

紧急情况转移计划和流程

---

☑ 危机通讯流程

☑ 紧急情况联系电话号码

■ 用户设施访问审查/审计日志

■ 安全意识培训文档、报告和传单等

■ 安全意识出席记录

关键主管的连续性计划

技术文档—走线图、BMS、UPS 和 AHU 细节

电力、发电机和 CCTV 监控头的维护规划

紧急情况燃料服务供应商合同

■ 可以进入设施内部的授权人员名单

■ 安全人员档案-生物和背景信息

■ 安全人员的背景检查报告（必须每年执行一次）

对关键设备和设施的每年维护合同（主要关注 SLA $ ^{29} $ 中的设备/设施的停机和恢复时间）

当审查这些文档的时候，有一些需要云服务购买者重点关注的地方以确保可以减低他们使用云服务的风险。当云用户将他们的业务迁移到云计算平台中，需要确保他们的业务和利益，以下的建议也许证明是非常关键的：

检查是否所有的文档都是最新的。这些文档必须被 CSP 每年至少审查一次。文档中必须包含维护时间和维护者签名，以便可以验证这些文档确实在内部被审查过。

此外，策略和流程文档（从雇员视角看）必须是可以通过公共的 Intranet 网络可以获取的，CSP 中被授权的雇员可以在任何时间访问这些文档。安全团队必须足够小心，以确保这些被更新的文档是最新版本并且被管理员及时确认过。

所有的策略和流程只有当雇员有意识遵照执行时才是有效的。最后，我们需要检查一个 CSP 是否有到位的安全意识程序计划。至少，CSP 应该确保雇员接受了足够的安全意识培训，至少每年一次，并签字保证。此外，新加入组织的雇员应该接受一个安全谈话作为新员工就职程序的一部分，对这些关键的策略和流程必须维护正式的签到记录，并且是在任何时候都是可以审查的。为了使得这个程序更有效，必须请安全团队老员工来执行安全谈话。

##### 7.1.1.3 国际/工业标准安全合规

确保云服务提供商实现诸如全球安全标注 ISO 27001 信息安全管理体系或者其他工业标准，诸如 TOGAF、SABSA、ITIL、COSO 或者 COBIT 的合规。合规活动将被证明为云服务提供商的安全级别和成熟度评估提供了价值。

---

■ 验证合规性证书以及其有效性。

寻找资源分配的可验证的证据，例如为了维持合规性项目的预算和人力资源。

■ 验证内审报告和审核发现补救措施的证据。

##### 7.1.1.4 实地考察 CSP 设施

## 覆盖区域

数据中心边界安全评估时，应确定哪些方面需要物理覆盖。以下为应确保安全的高风险区域：

■ 管理区

前台

■ 停车区

储物区

火灾出口

■ 有线电视指令室

■ 空气处理机房

■ 更衣室

■ 不间断电源室

发电室

☑ 燃料存储罐

## 标志

检查下列标志应在适当的地点显著展示：

■ 火灾逃生路线图和紧急出口

■ 火灾指令须知

消防安全标志

■ 安全海报和指示

■ 制止尾随海报

■ 温度/湿度相关信息

☑ 警告和指导标志

---

☑ 紧急联系号码

事故升级流程图

#### 7.1.2 安全基础设施

边界安全作为阻止入侵者和不必要访问者的第一道防线非常重要，随着技术进步，边界安全的原则已经发生了翻天覆地的变化。边界安全针对有意访问设施的入侵者，可以用威慑（Deter）、检测(Detect)、延缓(Delay)和拒绝(Deny)等4个D来概括。

选择物理基础设施提供商上，以下特质应优先考虑。根据不同的云服务供应商的设计和功能，应严格按照过程遵循下表。应当关注以确保物理基础设施具有适当的大小、性质和经营规模。安全控制应战略性地部署和符合可接受的质量标准，并与普遍准则和最佳实践保持一致。

■ 安全入口点 - 访问控制系统（感应卡/生物识别门禁）

访问控制系统相关联的火灾紧急释放控制面板

动作传感警报系统，热跟踪设备，玻璃破损检测

火灾安全设备 - 湿喉，消防栓，软管，烟雾探测器和水喷头

☑ 灭火器

■ 火灾出口（务必不上锁或者阻塞）

■ 安全出口紧急门闸

☑ 警报器和警报灯

有线电视摄像机和数字视频记录服务器在（包括备份时间轴）

门关闭和延时报警器

■ 数据中心内气体灭火器

■ 打印机旁的碎纸机

■ 消磁设备和磁盘粉碎机

☑ 紧急响应小组工具包(ERT Kit)

保安人员双向无线设备（头戴对讲机）

保安桌下和隐蔽有利位置的胁迫告警

· 入口处门框式金属探测器和手持金属探测器（如需要）

保管重要文件和媒体的防火保险箱

---

### 7.2 人力资源物理安全

人力资源物理控制的目的是最小化接近数据的相关人员，干扰运行和危及云服务的风险。一个能够接触到控制台的有经验入侵者能够通过重启系统或者访问当前已经是 root 或者管理员权限的系统绕过大多数逻辑保护措施。配线间可能被用来隐蔽访问或者破坏现有网络。应考虑如下手段：

本节对应云控制矩阵 IS-15, FS-05, FS-06, FS-07 和 FS-08 以及 ISO/IEC 27002 第 9 条款.



角色和职责（通过类似 RACI: Responsible, Accountable, Consulted, and Informed）方式的控制矩阵）

☑ 背景调查和审查协议

雇佣协议（保密协议）

公司策略的认知和培训（代码和商业行为）

角色和职责是云计算环境的一部分，通过角色和职责，人、流程以及技术集成一起，形成了支撑租户安全的统一基础。职责分离（SOD），即要求完成端到端交易或者处理过程至少需要两名人员具备分离的工作职责。避免利益冲突对于保护云计算用户是必要的，应该通过建立监控手段以规避该风险。职责分离起源于财务和会计管理，职责分离的好处已被扩展至满足其他风险消除需要，如物理安全、可用性和系统保护。职责分离通过消除高风险组合来实现，例如，不允许相同的人员担任批准订单采购和有能力进行支付的角色。这一原则被应用于云的开发和运行的职责划分上，同样也应用于软件开发生命周期。常见情况下，云的软件开发即为分离状态，确保在最终交付物内不含有未授权的后门留存，确保不同人员管理不同的关键基础设施组件。此外，给予员工履行其职责所需的最小访问特权将进一步减少但并不是消除风险。职责分离和最小特权/访问是支持云服务提供商达成保护和影响组织信息资产目标的原则。云安全管理程序要求关键角色和职责的分配将由特定个体或者组织完成。这些角色和职责必须被组织信息安全策略框架正式定义，并被高级管理人员参照 GRC（治理、风险和合规）义务和责任正式审核和批准。

此外，开发有效的人力资源安全必须包括雇佣和保密协议，背景调查（在法律允许范围内）以及合法的雇佣和终止手段。作为额外措施可考虑是否适用于所有领域的组织，包括正式的工作描述、适当的培训、安全许可、工作轮换以及敏感或者高风险角色员工强制休假。

### 7.3 评估 CSP 安全性

一些与云计算相关的安全风险是特有的，部分原因是存在一个扩展的以数据为中心的产销监管链，在这种背景下，需要参照行业标准，对云服务提供商的业务连续性、灾难恢复和传统的安全环境进行彻底评估。

云计算服务提供商的基础设施的传统或物理安全很重要，需要按照各种参数进行彻底的评估。这是一个具有高度相似性的领域——云和非云计算数据中心的安全性要求是非常相似的。

对 CSP 的 “人员、流程、技术” 模式或理念有一个全面的观点和理解，将极大地有助于评估 CSP 的成熟度，标记还未解决的问题，并提出实现安全的解决方法。在继续之前，这些问题必须得到解决、批准和关闭。

---

组织的成熟度和经验对有效处理物理安全的程序和任何可能出现的突发事件有很大贡献。总是有很强人为因素参与有效管理物理安全程序。管理层的支持程度和安全领导的能力水平是保护公司资产的关键因素，而管理层的支持至关重要。

物理安全通常是第一道防线，防御未经授权以及经授权访问一个组织的实物资产，防御物理窃取档案资料、商业秘密、工业间谍活动和欺诈。

#### 7.3.1 程序

云服务提供商应确保可以应用户要求提供下列文件用于审查：

第三方提供的背景调查（每年一次）

☑ 保密协议（NDA）

实现“需要知道”和“需要具备”的政策，用于信息共享

■ 职责分离

■ 用户访问管理

■ 定义职位描述(角色和责任)

基于角色的访问控制系统

■ 用户访问评审

#### 7.3.2 安保人员

人工监测和干预是必要的，由警卫、监管人员和管理职员组成的物理安保人员应该部署(基于  $ 24 \times 7 $ 的基础)在 CSP 的基础设施处。

除其他事项外，站点和岗位指导应包括以下内容：

检查员工、合同员工和访客的凭证并使用登记日志

发放和回收访客证件

■ 遏制尾随员工

■ 管理访客和在设施内的行动

■ 处理安全相关的电话呼叫

监测入侵、火灾报警系统和调度人员响应警报

■ 对材料进出建筑进行控制并强制执行物业进入规定

---

强制执行建筑物相关的规章制度

☑ 在设施内巡逻

☑ 闭路电视监控

钥匙控制和管理

■ 执行应急响应程序

☑ 升级安全相关的问题到安全经理

■ 接收和分发邮件

在办公室内陪同无人随行的商务访客

#### 7.3.4 环境安全

安全服务提供商的设施需要通过实施控制来保护人员和资产，以保护环境免遭危害。这些控件包括但不限于：温度和湿度控制器，烟雾探测器和自动灭火系统。

##### 7.3.4.1 环境控制

数据中心应根据公布的内部标准，本地和/或地区的法规或法律，配备支持特定环境的设备，包括紧急/不间断电源。

必须保护环境控制所需的设备，来减少来自环境的威胁和危害的风险，及降低对信息未经授权访问的风险。

##### 7.3.4.2 设备的位置和保护

被列为包含限制或机密信息的系统，必须考虑以下控制：

设备放置在一个物理上安全的位置，以尽量减少不必要的访问。

环境条件，如湿度，会对计算机系统运行产生不利影响，需要受到监控。

安保人员应考虑在附近的楼宇发生灾难的潜在影响，例如，邻近建筑物发生火灾，从屋顶或地面以下楼层发生的漏水，或街上的爆炸等。

彻底销毁和处置废弃媒质的方法（例如，磁盘驱动器）。

##### 7.3.4.3 设备维护

为了确保设备持续的可用性和完整性，需要按照设备维护控制进行恰当的维护，包括：

■ 按照供应商推荐的维修间隔和规范维护设备。

仅允许授权的维修人员进行设备的维修和服务。

---

维护所有可疑的或实际故障和预防性及矫正性维护的记录。

当发送设备离开场所进行维护时，使用适当的控制。适当的控制措施的例子包括适当的包装和密封容器，存储在安全可靠的地方和清晰完整的运输运和追踪指导。

维护适当的资产控制政策和程序，包括保留所有硬件、固件和软件及追溯性、责任制和所有权的记录。

全面评估 CSP 的设施将使未来的用户理解和评估安全程序的成熟度和经验。一般情况下，专注于 IT 安全，物理安全仅获得有限的关注。然而，威胁场景盛行的今天，当务之急是物理安全应受到应有的关注。尤其是在一个客户的数据可能与许多其他共同托管的客户（包括竞争对手）共存环境中，物理安全承担更大的意义。物理安全是防御入侵者和恶意访问 CSP 设施的企业破坏者的防线之一。

### 7.4 业务连续性

传统意义上，信息安全的三大宗旨是保密性、完整性和可用性。业务连续性则涉及上述三方面需求的持续性部分。向云服务提供商的过渡将包括对供应商合约承诺的正常运行时间进行评估。然而仅通过服务水平协议（SLA）可能还无法满足客户，应充分考虑典型业务中断造成的潜在影响。鉴于近期受人关注的第三方服务中断，作者建议服务连续性维护应作为维持业务运营的关键保障。

应参考下文所述的指南进行特定服务的连续性维护。尽管与第三方提供服务（例如云）相比，大量指南更倾向被内部提供服务所采用，但这些指南的编写也可以成为定义第三方服务责任的依据。

### 7.5 灾难恢复

对于 IT 而言，云存储最有趣的一方面是如何利用它来完成备份与灾难恢复（DR）。云备份与灾难恢复服务的目标是降低基础架构、应用以及总体业务流程的成本。云备份与灾难恢复应该是一种可靠，相对廉价且容易管理的服务。云存储、云备份与灾难恢复所面对的挑战主要包括可移动性，可用性，可扩展性，信息如何传入传出云，保障最佳的业务连续性以及计量计费。云灾难恢复构建于以下三个基础要素：一个完全虚拟化的存储基础架构，一个可扩展的文件系统以及一个可以应对客户紧急业务需求的自服务灾难恢复程序。

客户将灾难恢复迁移到云之前应该先确认服务提供商的灾难恢复项目中包含下述组织或团队：

■ 应急响应团队（ERT）

☑ 危机管理团队

■ 事件响应团队

要按照危机处理流程仔细核查上述团队的构成。

#### 7.5.1 恢复优先级

---

核查服务提供商的恢复计划文档：计划应该包括优先级（决定恢复顺序）的细节信息，其内容应该与合约中承诺的 SLA（决定于客户所购买的服务以及服务的关键程度）相符合，RPO（恢复点目标）和 RTO（恢复时间目标）是两个重要的服务指标，应该包含在恢复计划之中。

在恢复过程中也需要认真设计和实现信息安全控制，这一部分需要考虑的细节信息如下例：

■ 明确需要介入恢复过程的员工

备用站点的物理安全控制如何实现

与恢复过程相关的特定的依赖关系（供应商和外包服务合作伙伴）

当主站点不可用时，备用站点的地理位置要尽可能集中

### 7.6 权限

■ 确保配备了必要的设施。

采用彼此相互强化的，集成式的物理与逻辑安全系统。

■ 建立服务等级协议，要遵循对供应链后端所负有的安全职责和义务。

### 7.7 建议

#### 7.7.1 策略建议

云服务提供商应该为那些在安全方面要求严格的客户建立一个安全基线（内容可包括系统，设施和流程等）。这些安全指南不应给客户体验带来负面的影响，严格的安全指南应该是经济的，并且可以有效地降低企业人员、公司收入、声誉和股东价值等方面所面对的风险。

另外，云服务提供商也要为低安全需求的用户建立安全基线，或者为所有用户提供一个基线，在此基础上为那些有需求的用户提供更多的附加服务选项。对于后一种情况，提供商应该意识到有些客户只对那些仅提供高安全等级服务的服务商有兴趣。服务商必须在系统，设施和流程等方面就安全等级进行权衡。

云服务提供商应该严格划分工作职责，实行背景调查，要求并强制员工签署保密协议，并基于最小权限原则限制员工获取客户的信息。

#### 7.7.2 透明性建议

○ 为了表明在安全方面的态度，云服务提供商需要提高服务的透明度。现场参观云服务提供商的设施和数据中心可以帮助用户更好地评估服务水平，清楚地理解各种安全标准。但是，云计算具有按需置备和多租户等特性，传统形式的审计和评估可能不适用，或者需要修改（如共享式访问与第三方检查）。

---

为了增加现场评估的效力，应该在没有事先通知的情况下（如果需要事先通知，指定一个较宽泛的时间窗口而不是一个特定的时间）拜访云服务提供商的设施或数据中心。这样可以保障用户在一个平常的工作日里进行一次真实的评估，而不是由云服务提供商在客户或第三方访问时装装门面。

如果需要直接检查，评估团队应该由两名或更多来自 IT、信息安全、业务连续性、物理安全和管理部门（如部门首脑或数据所有者）的专家组成。

在访问之前，客户应该索取业务连续性计划和灾难恢复文档，包括相关的证书（基于 ISO，ITIL 等标准），审计报告和测试协议。

#### 7.7.3 人力资源建议

客户应该检查云服务提供商是否为保障物理安全而部署了能胜任工作的安全人员。建议配置一名负责领导和推动物理安全项目的专职安全经理。业界顶尖的认证可以帮助你验证工作人员在物理安全方面的知识和技能，例如 CISA $ ^{30} $，CISSP $ ^{31} $，CISM $ ^{32} $，ITIL $ ^{33} $，or CPP $ ^{34} $ (from ASIS $ ^{35} $)。下面是一些具有代表性的认证：

客户应该索取一份全面介绍安全经理及其组织的报告。它可以帮助你判断该位置上是否安排了尽职尽责的人员。安全经理应该向部门主管或 GRC 委员会报告，而不是向物业或 IT 人员报告。为了保证这一职位的独立与客观，最好可以通过其它途径（如通过 CRO 或公司高管）向 CEO 报告。

#### 7.7.4 业务连续性建议

○ 已部署服务的连续性通常由第三方在合约中做出承诺，客户只需要审查合约，但实际上客户才是实际的数据管理者，因此有必要对服务商的能力做深入的分析。对于个人数据，通常要遵循特定的法规要求，采取相应的控制手段。即使采用第三方数据处理服务也是如此。

客户应该审查第三方的业务连续性流程和特定的认证。例如，云服务提供商可能取得了 BS25999，即业务连续性管理英国标准。客户可以审查这一认证的范围和评估细节记录。

客户应该对云服务提供商的设施进行现场评估，以确认和验证服务商为保证服务的连续性所采取的控制手段。如果要检验特定业务连续性计划的实现，一般不应采取这种不事先通告的服务商设施评估，因为这一类实现只有在灾难或事件发生时才会被启用。

客户要保证自己在云服务提供商执行完任何的业务连续性计划或灾难恢复计划测试之后都能收到确认。要特别关注的是，服务商确实是通过模拟重大事件发生来进行测试的，并通过文档承诺服务的可用性将得到保障。这在许多的建议中都曾经提到过。客户应该对业务连续性和灾难恢复测试的正式报告给予特别重视，要清楚地了解测试是否满足合约中所承诺的服务级别。不要等待灾难真的发生时才重视。

---

#### 7.7.5 灾难恢复建议

使用云服务的客户不应依赖单一服务商的服务，应该制定一个灾难恢复计划，明确当前服务商失去服务能力时，如何对业务系统进行迁移或故障切换。

基础架构云服务商应该在合约中约定，采用多种平台来提供服务，且必须拥有在服务受损之后可用于快速恢复系统的工具。

数据验证应该是一个自动化的，或者基于可由用户启动的验证协议，以便客户可以随时检查他们的数据，从而确保数据的完整性。

增量备份可以按照系统用户所设定的间隔为所有受保护系统或快照更新副本。消费者可以根据恢复点目标来决定设置。

可以通过一个用户驱动的，自助服务的门户来访问全站、系统、磁盘和文件恢复服务，这样用户就可以灵活地选择他们想要恢复哪个文件、磁盘或者系统。

云服务提供商应该提供快速的，符合服务等级协议的数据恢复服务。

服务等级协议应该预先协商好，客户只需要购买他们所需要的服务。所有的数据、文件或系统都应该在30分钟以内恢复。

客户与物理站点之间的应该采用广域网优化技术，在确保数据可移动性的同时还可以减少带宽和存储设备的利用率，从而节省成本。

### 7.8 要求

✓ 所有相关方面都必须确保基础架构的设计是满足物理安全要求的。

✓ 所有供应链的参与方应该顾及到威慑、侦查以及验证解决方案的相关性。

✓ 最终用户必须检查、记录和修正来自云供应链中其它成员的人为风险。必须通过正确的责任分工和最小权限访问原则设计和实现一种主动发现和消除人为风险的方法。

---

## D8: 数据中心运行

为了云计算的发展，提供商不仅仅是利用简单应用虚拟化技术来管理服务器资产，更必须升级企业的数据中心。为了实现业务敏捷性，绿色技术，提供商开放性，鼓励电力和数据中心的建设与管理中涌现的越来越多的创新理念，数据中心应该寻求向云计算上的长期成功而转变。

“下一代数据中心”，一个已经被提出好几年的术语，现在已经发展成为数据中心的运行，包括数据中心内的商业智能适应，对数据中心中运行的应用程序的了解，以及大规模分析集群的托管。数据中心不再是一个独立的实体，而是和应用一样灵活并且与其他数据中心连接的实体，因此延迟以及安全都要管理。

## 概览 本单元将讨论以下主题：

☑ CCM 相关的物理安全方面的考虑

■ 自动化数据中心使用案例

新型数据中心？家庭云计算（Cloud computing at home）

CCM 的注意事项以及云数据中心的

新思路如何互相影响



云基础设施分散部署和数据中心

### 8.1 数据中心运行

本节中的新概念：

云应用任务 安置在数据中心内的行业或应用任务。例如，一个医疗保健或电子商务应用任务。

数据中心分散部署 协同运行的但是分布在独立物理区域中的云基础设施。

基于服务的自动化和以预测分析，使服务为基础的自动化在很长一段时间内被信息技术服务管理（Information Technology Service Management $ ^{36} $，ITSM）所代表，ITSM 使用信息技术基础设施库（Information Technology Infrastructure Library $ ^{37} $，ITIL）标准指导数据中心的发展。

安置在数据中心内的不同类型的应用程序需要自动化。当理解了数据中心中正在运行什么以及数据中心需要如何作为一个整体来应对不同的使用时，数据中心的经营者将大大受益。

云安全联盟撰写的“云控制矩阵”根据不同的标准和管理需求制定了相应的一些物理要求。数据中心的专业人员应阅读本版本指南中的“物理安全”单元和“云控制矩阵”以理解数据中心内部和外部的需求。为方便读者参考，下表举例说明了数据中心中的不同应用程序的任务所需的控制。该列表并不详尽但提供了一些交叉引用“云控制矩阵”和规范的应用类型或任务的示例。

---

<div style="text-align: center;">表1——应用任务控制</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>应用任务</td><td style='text-align: center; word-wrap: break-word;'>控制</td><td style='text-align: center; word-wrap: break-word;'>规范</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>医疗保健（HIPAA） $ ^{38} $</td><td style='text-align: center; word-wrap: break-word;'>设施安全-安全政策</td><td style='text-align: center; word-wrap: break-word;'>应建立政策和规程以保持办公室，房间，设施和安全区域中的安全工作环境</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>卡处理/支付（PCI） $ ^{39} $</td><td style='text-align: center; word-wrap: break-word;'>设施安全-用户访问</td><td style='text-align: center; word-wrap: break-word;'>应限制对信息资产的物理访问以及用户和保障人员的权限功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>发电（NERC CIP） $ ^{40} $</td><td style='text-align: center; word-wrap: break-word;'>设施安全-受控的访问点</td><td style='text-align: center; word-wrap: break-word;'>应实施物理边界安全（围栏，围墙，栅栏，守卫，门，电子监控，物理验证机制，接待处，安保巡逻）来保护敏感数据和信息系统</td></tr></table>

上表不再在本章赘述。读者可以参考“云控制矩阵”并根据相关组织希望遵守的标准或必须遵从的规范。

数据中心中运行的包含管控信息的应用程序（受信息安全或应用程序安全标准管辖）将被审核。数据中心运营商进行的物理审计结果可以公布给数据中心运营商的客户或由应用程序查询基础设施如云审计提供的基础设施来发布。

在以往版本的“指南”中，读者被指示建立自己的审计。对于很多数据中心运营商或云提供商来说，该做法可能不可行。在多租户的环境中，运营商或提供商通常不能满足对每个用户的访问进行审计。用户应该要求运营商或提供商提供独立的审计结果。

这个想法带来了服务自动化。通过基于应用任务的自动化的报告，日志，以及审计结果的发布，数据中心运营商能够使它们的用户确信，数据中心的具体管制措施是到位并令人满意的。云审计，云信任协议和 CYBEX（X.1500）能通过一个通用的访问接口自动发布审计结果。

数据中心的更进一步的自动化依赖于包含数据中心中资产的库。通过理解库中的资产如何使用数据中心中的资源，运营管理中心可以预测哪些租户正在使用资源。如果数据中心使用如 PoD’s $ ^{41} $和虚拟数据中心 VMDC $ ^{42} $的理念，那么数据中心就能足够灵活使其可以迅速促进云或虚拟化业务。

#### 8.1.1 新型和新兴模型

最近（2011 年夏天）出现了更多关于家庭（home-based）云平台的新闻。在这些类似 SETI@home $ ^{43} $模型的基础设计类型中，云是基于志愿者提供其家中或办公室中的电脑的计算资产来支持其他的应用。这些情况下数据

---

中心由每个志愿者的家组成。这些类型的云在以社区为基础的应用托管环境中将可以良好运行，但这种环境不是标准中可审核的规范环境。例如，如果一个云建立在 100,000 个家中的计算机之上，可能就没有办法来审计这样一个被有效分割成 100,000 个部分并且分散在一大片地理区域的数据中心。这种类型的基础设施可以托管基于兴趣（如读书俱乐部）或住宅信息网站的基于社区的应用。

云正越来越多地被视为一种商品或一个工具。因为一些其他的原因，行业内正努力在为身份识别，互操作性和业务连续性而建立 SecaaS 或建设代理基础设施。这些应用将被分离并运行在特定的物理环境中，以满足组织或组织运行的应用程序的特殊需求。

数据中心分散部署将应用程序放置在需要满足特定管理需求的多个其他的专门数据中心中。通过将应用分散跨越多个物理边界，应用程序在云中的负担变轻了，但是更难于控制和管理。

### 8.2 权限

数据中心合作分散部署。跨越多个物理上没有关联的数据中心的自动化需要软件精心协调数据中心的需求来在审计中记录和报告生成日志。

数据中心属于个人的家庭共享云。标准和规范的审计在家庭共享云中几乎不可能实现。合规的环境和合乎标准的环境的控制要求也将在家庭共享云中遇到困难。可能在某些情况下应用程序的某些部分可以被分散部署到以家庭为基础设施中。

### 8.3 建议

○ 建设云数据中心的组织应纳入管理过程，实践和软件来了解运行在数据中心中的技术并对它们做出反应。

购买云服务的组织应该确保提供商已通过服务管理流程和实践运行其数据中心，并且使用了机架化技术来保证数据中心中资源的灵活和高可用性。

了解在数据中心中正在运行哪些任务。在建或购买的数据中心必须满足“云控制矩阵”中的物理和资产控制要求。

☐ 数据中心的位置是重要的。如果技术和应用组件跨越多个数据中心，那么数据中心之间会存在延迟。

购买云服务的组织必须清楚地了解当遇到合规性要求时哪个部门应该为其负责，以及当进行合规性评估时他们和他们的云提供商所扮演的角色，并将它们记录成文件。

### 8.4 要求

云安全联盟拥有多种信息来源来帮助服务于云的数据中心的建设或改建。控制矩阵强调在一个非常广泛范围的安全标准和法规上的需求。云安全联盟的云审计和其他项目同样可以为数据中心的建设和管理以及其中运行的技术提供帮助。

---

✓ 通过了解数据中心中将要运行什么来全面理解控制矩阵要求。使用其共同点以满足大部分应用程序的任务。

✓ 使用 IT 服务管理技术来确保可靠性，安全性，以及资产交付和管理。

✓ 如果数据中心为提供商所拥有，应通过一个规章制度和安全标准模板进行审计并将结果发布给用户。

---

## D9: 事故响应

事故响应（IR - incident Response，下同）是信息安全管理的基石之一，即使最周详的计划、实施并执行了相关的预防性安全措施，也无法完全避免信息资产遭到攻击。因此，当机构转向云的时候，面临的核心问题之一就是：怎样才能有效处理关于云资源的安全事故。

云计算不需要一个新的事故响应概念框架，只需将原有的 IR 程序、处理机制和工具与云计算相关的环境对应起来。这一观点贯穿了本指南文档，通常情况下，需要首先进行对组织内 IR 功能的控制进行差距分析。

本部分（Domain）力图明确这些与云计算独有特性相关的 IR 差距项，供安全专家作为参考，用于 IR 生命周期中的准备阶段制定响应计划和指导相关活动。为了理解云计算对事故处理带来的挑战，我们必须明确云计算及变化的部署和服务方式给事故处理带来了什么特殊性。

本部分（domain）按照“事故响应生命周期”来编制，这是由美国国家标准技研究院的计算机安全事故处理指南(NIST800-61)定义的，并已经被业界广泛接受。首先确定云计算对IR最直接特征影响，然后将这些特征对应到生命周期的每个阶段，并探讨响应者应该考虑的问题。

概览 本部分将讨论如下题目：

■ 云计算对事故响应的影响

■ 事故响应生命周期

■ 取证责任

### 9.1 影响事故响应的云计算特征

尽管云计算在很多层面带来了变化，但其中某些云计算的特性相比其他特性对 IR 活动更具有直接的挑战。

首先，由于云计算的按需自服务性质，客户在处理安全事故的时候很可能会发现很难甚至不可能从云服务商(CSP) $ ^{44} $那里获得协助。服务和部署模式不同，客户与 CSP 的 IR 互动方式就会不同。关于安全事故的检测、分析、遏制（containment）和恢复能力通常已经被工程化到服务承诺中，这是 CSP 和客户需要重点关注的问题。

第二，云服务的资源池化，除了使云基础设施可提供快速弹性的交付外，可能还会导致 IR 过程复杂化，特别是作为事故分析的取证（forensic）活动部分，必须在高度动态的环境下实现，这对基本的取证工作带来了挑战，例如界定事故的范围、数据的收集和归属性、保留数据的语义完整性、维护全部证据不变性。这些问题当取证活动时会被强化，这是由于是在一个对他们不透明的环境下进行（取证）操作（就像前面提到的，这是云服务商必须提供的支持）。

---

第三，在合租（co-tenants）场景下，如果没有关于隐私信息处理的妥协（compromising），资源池化的云服务方式，对于收集和分析事故的非直接数据和原始数据（telemetry and artifacts）（例如：日志、netflow 数据、内存、设备映像、存储等）可能会带来对隐私性问题的担忧。这是云提供商必须首要解决的技术挑战。同时，也取决于云服务消费者来确保他们的云服务提供商具备了适当的数据收集和分离流程、能提供所要求的事故处理支持。

第四，尽管没有被描述成云的基本特性，云计算可能导致数据跨越地理区域和司法管辖边界，对这种状况，客户可能并没有这方面的明确知识，后续的法律和监管的介入（implications）可能会对事故处理过程有不利影响，法律和监管的介入会在事故生命周期的各个阶段限制什么可以做/什么不可以做或者规定什么必须做/什么一定不能做。法律部门应该为机构或代表处的事故响应团队制订处理类似问题的指南。

云计算也给事故响应者带来了新的机会，对于云的持续监控机制，可以减少承担事故处理练习所需的时间或者事故响应。

虚拟化技术和云计算平台固有的弹性特质，会允许更有效率和效果的遏制（containment）和恢复。通常会比传统数据中心技术减少服务中断时间。并且在某些方面使得事故调查变得更容易，因为虚拟机可以很容易地被移动到试验环境中，在那里可以管理运行环境、取得鉴定映像并进行检查。

### 9.2 云结构安全参考模型

很大程度上，当涉及到云生态系统中的 IR，部署和服务模式决定了分工，参考 D1 中（Figure 1.5.2a 的云参考模型）提出的结构性框架和安全控制，将有助于标示出那个技术或过程单元，应该由那个机构负责并负责到什么层面。

云服务模式（IaaS, PaaS, SaaS）明确区分了客户对于基础 IT 系统和其它提供计算环境的基础架构的可见程度和控制程度，该模式适用于事故响应的各个阶段，本指南的其它域也是依据这个模式来处理的。

例如：对于 SaaS 解决方案，事故响应责任很可能几乎完全属于云服务商（CSP）。而对于 IaaS，很大程度上的事故检测和响应的责任和能力主要属于客户。但是，即使是 IaaS，对云服务商也有明显的依赖性，源于主机、网络设备、共享服务、像防火墙等安全设备、及后端的管理系统的数据必须由 CSP 提供。有些供应商已经准备好了为他们的用户提供这种数据，某些管理安全服务商也正在大力推广处理云的这些数据的解决方案。

考虑到问题的复杂性，在 D1(图 1.5.1c)中描述的安全控制模式，及组织执行的与企业云部署相关联的具体安全控制活动，应该关联到 IR 规划，反之亦然。通常情况下，IR 控制关注更窄和更高层的机构需求，但是，安全专家必须保持更全面的视角，以确保 IR 的有效性，安全专家也有责任和权利介入到可能直接和间接影响（事故）响应的任何安全技术（手段）的选择、购买和部署过程中去。这最起码有助于划分 IR 生命周期各个阶段的角色和责任。

在审查云环境下的 IR 能力的时候，应该考虑云部署模式（公有，私有，混合，社区）。对于每一种部署模式，获取 IR 数据的难易程度会不同，模式不同所需的控制和责任也不同。在这部分（domain）中，主要关注的是公共端的问题。作者认为，云（应用）越私有，越需要开发适当的安全控制手段或者由服务商提供给客户更多安全控制手段，以提高客户满意度。

---

### 9.3 事故响应生命周期研究

NIST 800-61 定义了如下的事故响应生命周期的主要阶段：准备，检测&分析，抑制，根除&恢复。下面章节分析云计算对这些阶段带来的挑战，并为如何应对这些挑战提出了建议。

#### 9.3.1 准备

当信息资产部署在云中时，准备可能是事故响应生命周期中最重要的阶段。识别事故响应的挑战（和机会）是信息安全专家在客户迁移到云之前应该提前进行的一项正式工作。如果机构这方面经验不足，可聘请外部专家进行咨询，并应该在每一次企业更新事故响应计划时进行。

下面讨论的每个生命周期阶段，将提出问题并给出解决建议，这可以用于指导给客户的规划过程。将结论记录到正式文档中，将有助于驱动利用任何机会对差距进行矫正。

准备（阶段）是从清晰了解和全面核查对客户的流动和驻留数据，考虑到客户的信息资产会分散在机构内，并可能跨地理边界，这会导致需要从物理和逻辑两个层面去进行威胁建模。采用对应到物理资产、组织机构、网络、管辖边界的数据流图，可以用于明确在响应时的依赖关系。

由于涉及到多个机构，服务水平承诺和多方合同变成了在事故响应生命周期各个阶段中沟通和实现对责任预期的主要依据。建议与各方共享事故响应计划，并且精确定义和澄清术语是明智选择，如果可能，任何模糊之处应该在事故发生前明确下来。

期望 CSP 为每个客户都建立一个特别的事故响应计划，但是，在合同或者(SLA) $ ^{45} $协议中给出的如下要点，能够说明 CSP 已经事先做出了事故响应计划，这样会提升客户（关于事故响应）的信心。

联系人，沟通渠道，可用的事故响应团队

■ 服务商提供给客户和其他外部团体的事故定义和通知标准

云服务商为客户提供的事件检测的支持（例如：可用的事件数据，关于可疑事件的通知，等。）

定义安全事故处理的角色/责任，明确 CSP 提供的事故处理支持（例如：通过事故数据/处理过的中间数据的采集实现的取证支持，参与/支持事故分析等）

定义根据合同进行的常规事故响应测试责任方规范以及结果是否会被公开

■ 定义事后分析活动的范围（例如：根源分析，事故响应报告，通过经验教训改进安全管理等）

在 SLA 中清晰定义 IR 中的供应商及客户的责任

一旦角色和任务确定，客户可以有效地培训事故响应团队，来处理那些他们有直接责任的事故。例如，如果在 PaaS 环境下由客户负责应用，且云服务商承诺提供（或允许检索）平台的日志，客户自然需要具备技术/工具和人员对这些日志进行接收，处理和分析。对于 IaaS 和 PaaS，与虚拟化相关的能力及对虚拟机调查取证的

---

办法将影响响应效果。关于需要客户组织自身的特定技能的自行解决还是外包给第三方，要在准备阶段确认下来。请注意，外包需要由另外的一套合同/NDA's⁴⁶(保密协议)来管理的。

必须准备好连接各介入方的沟通渠道。应考虑传输的那些信息是敏感的，用加密手段确保信息的完整性和真实性。最好参照现有标准进行事故响应过程中的沟通，以便于方便其他各方参与到调查中。例如，由(IETF) $ ^{47} $编制的事件描述和交换格式(IODEF) $ ^{48} $及相关实时网间防御(RID) $ ^{49} $标准，这些标准也被国际电联(ITU) $ ^{50} $包括在网络安全交换Cybersecurity Exchange (CYBEX) $ ^{51} $项目中。IODEF 定义了一个标准的 XML 语言模式，用于描述事故，RID 描述了一种标准方法来实现实体间关于事故信息的通信，至少是租户和云服务商之间的通信。

关于事故（响应）准备阶段最重要的事是对计划进行进行测试，测试应该是全面的并且组织全部可能参与到真实事故响应的各方参加。云服务商不一定有资源参与所有客户的测试；客户可以用角色扮演的方式确定哪些任务或信息需求是属于运营商的，这些信息将用于以后与运营商进行准备阶段的讨论。另一种可能是客户自愿参加云服务商可能已经计划了的任何测试。

#### 9.3.2 检测与分析

及时发现安全事故，和成功的进行事后的事故分析（回答发生了什么，如何发生的，涉及到哪些资源等问题），依赖于相关数据的可用性，和对数据进行正确解析的能力。如上文所述，云计算同时带来了这双方面的挑战。第一，数据的可用性在很大程度上取决于云服务商提供给客户的资源，并可能被云计算的高度动态特性所限制。第二，分析工作涉及的基础设施，至少部分是由运营商所持有的，非透明化的。这使得分析作业变得复杂。由于客户只掌握有限的基础设施信息，加上云计算的动态特性，数据的解读变得困难，甚至成为不可能的任务。

暂不论事故分析面临的技术挑战，关于应如何在云环境中进行数字化调查，争取在书写记录时，最大化所持证据的证明力的这一问题上，也并不存在令人满意的答案。因此，在与云技术事故相关的司法案件变得更为普遍，和在被广泛接受的最佳实践性指导方案存在之前，云计算的安全事故分析结果存在无法被司法部门视为有效证据的风险。

在用于检测与分析安全事故的相关标准、方法和工具能够赶上云计算所带来的技术革新之前，事故的检测与分析将会一直是云环境中的重要挑战。云客户必须迎接这一挑战，确定己方掌握获取如下两项资源的途径：（1）与事故检测及分析相关的数据源及信息，（2）在所使用的云环境中进行事故分析的相关取证支持。

#### 9.3.3 数据源

与任何 IT 集成托管服务（hosted IT service integration）中一样，事故响应团队需要确定适当的事件记录方法，以求能够有效的检测并识别那些影响其资产的异常事件与恶意行为。客户必须对三个问题进行评估，即哪些记录（以及其他数据）是可用的，如何收集并处理数据，数据会在何时，以何种方法由云服务供应商交付。

---

在客户侧，用于事故检测和随后分析的主要数据源是日志信息。以下几个有关的日志信息的问题必须被纳入考量。

- 应记录哪些信息？相关日志类型示例有：审计日志（例如网络活动日志，系统活动日志，应用程序活动日志，云管理角色及其访问活动日志，备份和恢复活动日志，维护和变更管理活动日志），错误日志（例如 Hypervisor 的核心消息报错日志，操作系统报错日志，应用程序报错日志等），安全性日志（例如，入侵检测系统日志，防火墙记录日志等），性能日志等。在现有日志信息中存在不足之处，须进行协商，并添加额外的日志源。

信息记录是否一致和完整？导致信息记录不一致的一个典型原因是信息源间的时钟同步处理失败。同样，缺少时区记录的不完整的信息记录，会导致在分析过程中，收集到的数据无法被准确地解读。

记录的信息是否充分反映出云服务的动态性质？云服务环境的动态行为也是一个导致信息记录不一致或不完整的常见原因。例如，在新的云资源（如虚拟机等）被添加入网络环境以满足需要时，需要将新资源产生的相关日志信息添加到日志数据流之中。未能在日志信息中明确环境中发生的动态变化是另外一个可能存在的问题。例如，web 服务请求一定的 PaaS 组件这一事件被记录，但也可以是由这项服务的各种实例之一动态提供。信息不完整的问题，例如服务的请求，可能导致难于或无法进行正确的分析，例如，如果一个事件的根本原因是一个单一的不完全的事件。

与法规是否存在冲突？一些因素可能会限制日志数据的收集，储存、使用。它们包括使用同云空间的租户间的隐私问题，一般性日志数据的规定，和特定的个人识别信息的规定等。在不同司法管辖区中，数据处理或存储中所涉及的相关规定会存在差异。客户必须理解并重视这些规定。

- 日志应以何种方式保存？法律及合规要求会直接明确日志留存方式。云客户应理解并定义任何扩充的日志保存方式，以满足他们不断更新的对事故分析和取证的需求。

如何防止信息记录日志是防篡改的吗？为了进行准确的取证分析，确保储存的日志是防篡改的是至关重要的。可以考虑使用一次性记录设备，区分用于储存日志的服务器和应用的服务器，加强储存日志用服务器的访问控制，作为这一需求的关键因素。

信息记录应采用何种格式进行通信？日志数据格式的标准化是一个很大的挑战。运用通用格式（如一般事件表达法）可简化客户对数据的处理。

云供应商只能检测到一部分的事故。原因是这些事故发生在云供应商所拥有的基础设施的内部。需要特别注意的是，服务级别协议必须包含有关云供应商应及时，准确地通知云客户，以执行达成共识的事故响应。至于其他一些客户都有能力检测到的事故，云供应商进行检测可能更佳。云客户应该选择那些通过关联与过滤日志数据提供最佳的事件检测协助的云供应商。

云部署所产生的数据可能相当大的。也许需要去研究云服务供应商提供的有关日志过滤手段的可选方案，用于在交给客户之前减轻网络压力与客户内部处理的影响。其他一些应考虑的因素有，云服务供应商或云租户进行的分析与关联的水平以在取证（forensics）之前识别可能的事故。如果是由云服务供应商进行分析，那么事故调查的关键点（升级点和切换点）必须提前确定。

#### 9.3.4 用于事件分析的电子取证与其它调查性支持

尽管还不成熟，在法律调查取证的社区中已经在尝试开发一些工具和协议，用以采集和检查特别是从虚拟环境中获得的与法律取证相关的产出物。同时 PaaS 和 SaaS 环境中所需要的电子取证支持也正在进行研究中。

---

客户要了解在进行事件分析时的电子取证需求，并要调研云服务供应商满足这些需求的程度，而且选择相应合适的供应商，并解决与自身需求间剩余的差距，这是非常重要的。不同的云服务和部署模式下，能够提供给客户的潜在证据的数量是有非常大差异的。

对于 IaaS 服务，客户可以在他们自己的虚拟机实例内进行调查取证，但无法调查云服务供应商控制的网络组件。此外，标准的电子取证活动，如通常的对于网络流量的调查，对于内存快照的访问，或是硬盘镜像的创建，都需要供应商提供支持。由于虚拟化而成为可能的高级电子取证技术，如在活动系统上生成虚拟机状态的镜像或者进行 VM 的自我测试，均需要云服务供应商提供取证支持。

对于问题根源发生在底层基础设施的 PaaS 和 SaaS 安全事件，云的客户几乎完全依赖于云服务供应商提供的分析支持，并且如之前提及的，必须对事件响应（IR）中的角色和职责在 SLA 中进行约定。对于 PaaS，客户的组织要对部署在云中的任何应用层代码负责。对于问题根源存在应用中（如应用代码中的缺陷）这类场景下的事件分析，需要进行充分的应用日志记录。这种情况下，云服务供应商的支持可以采取为应用日志的产生、安全存储、以及通过只读 API 的安全访问提供便利的形式来提供。SaaS 供应商生成更广泛的客户特定应用的日志、提供安全的存储以及附加的分析功能，可以减轻客户一方的事件响应负担。这可能能够减少相当多的应用级安全事件。

那些使用他们自己的管理平面/系统来确定调查安全事件范围，识别系统中已经或正在遭受攻击的部分，并将这些数据提供给自己云的客户的供应商，将大大地增强所有服务模式下的响应能力。

为在特定云环境中进行事件分析做准备，客户的事件响应团队应使自己熟悉云供应商提供给客户的用以辅助操作和事件响应流程的信息工具。知识库文章、FAQ、事件诊断矩阵等，可以帮助云的客户弥补其在云基础设施和云操作规范方面存在的经验上的欠缺。例如，这些信息可以辅助事件响应团队将操作性问题与真正的安全事态和事件区别开来。

#### 9.3.5 遏制、根除和恢复

如同事件响应的其它阶段一样，为确保所定义的事件遏制、根除和恢复策略是可用的、高效率的，并且考虑了所有涉及的法律和隐私相关要求，需要所有的利益相关方密切协作。所定义的这些策略必须与业务目标一致，并且力图将对服务所造成的中断最小化。在事件响应涉及多个组织时，如云计算情形下，这是相当具有挑战性的。

部署和服务模式以及攻击目标所处层次的不同，这一阶段可选择的选项也不同。在这里可以有多种策略，可能由具备不同技术解决方案的不同实体来采用。如果有可能的话，应在准备阶段进行思考以对这些场景进行预测，确定一个冲突解决流程。客户除了考虑那些直接以他们自己的组织为目标的事件之外，也应考虑他们的供应商如何处理影响到供应商自身或者共享平台上其他租户的事件。

IaaS 情况下，服务使用者对于事件的遏制、根除和恢复负主要责任。云的部署方式可能会为此带来一些好处。例如，可以通过暂停虚拟机镜像达到在不破坏证据的情况下将受影响的镜像隔离起来的目的。如之前讨论过的，当要部署更新代码时，节点可以相对容易的关闭，新的实例可以相对容易的建立，这可以将对服务所造成的中断最小化。如果某个特定的 IaaS 云有问题，那么客户可以选择将服务迁移到另一个云，特别是如果他们已经实施了 meta-cloud 解决方案的情况下。

SaaS 和 PaaS 部署方式下情况更为复杂。服务使用者除了关闭用户访问和在重新开放前检视/清理托管在服务内的数据之外，可能很少有技术能力来遏制 SaaS 或 PaaS 事件。尤其是 SaaS 情景下，即使是这些基本的措施，

---

在缺少云服务供应商的足够支持下，如服务商细粒度的访问控制机制以及服务商允许客户对其数据的直接访问（而不是通过 WEB 界面），也难以或不可能执行。

在所有服务模式下，供应商可能对某些种类的攻击能够提供帮助，，如拒绝服务攻击（DOS）。例如，较小的企业可以受益于云的规模效益，能将运营商部署的比较昂贵的风险缓解技术，如对于 DoS 的防护，延伸到他们的站点。同之前的阶段一样，供应商的设施，在帮助应对攻击时，能够向客户提供到什么程度，应该在准备阶段就确定。此外，在什么情况下供应商有义务为应对攻击提供帮助，也应加以合同性的定义。

SLA 和事件响应计划应具有灵活度，为事件恢复后进行的教训总结活动留有空间。应编写一份基于事件响应活动的详尽的事件报告，并在受影响的各方之间共享，如云的客户、云服务供应商、以及其他受影响/涉及的组织。事件报告中应包含事件的时间跨度、对于事件根本原因或弱点的分析、消除问题和恢复服务所采取的措施、以及对于长期性纠正措施的建议。

纠正性措施可能会是客户特定措施和供应商支持措施的混合，供应商的事件响应团队应提供一节文字用以说明他们对于事件的看法以及所建议的解决方法。在客户和云服务供应商完成对于事件报告的初步回顾后，应组织进行共同讨论，以开发和批准补救计划。

### 9.4 建议

云的客户必须理解云服务供应商如何区别岁感兴趣的事态的定义与安全事件的定义、以及供应商以哪种方式向客户报告哪些事件/事态。以公开格式提供的事态信息能够方便于在客户方一侧进行这些报告的处理工作。

云的客户必须建立起与云服务供应商的正规之沟通渠道、在事故发生时可以应用。使用现有的公开标准能够方便于事件的沟通。

云的客户必须了解云服务供应商对于事件分析所提供的支持，特别是供应商所提供的用于分析目的之数据的性质（内容和格式）以及与供应商事件响应团队的互动水平。特别是，必须对可获得的用以进行事件分析的数据进行评估，判断其是否能够满足可能涉及到云服务客户的电子取证调查的法律需求。

云的客户应当倾向于选择利用了虚拟化为电子取证分析和事件恢复所带来机会（如对于虚拟环境的快照的访问和回滚、虚拟机的自我测试等）的那些云服务供应商，尤其是在IaaS的情况下。

云的客户应当倾向于选择利用了硬件辅助的虚拟化和具备电子取证分析能力的加固的 Hypervisor 的那些云服务供应商。

对于每一项云服务，云的客户应当识别与自身最为相关的事件类别，并为事件的遏制、根除和恢复准备好策略；必须确保每一云服务供应商能够提供执行这些策略所必需的协助。

云的客户应当获取到云服务供应商在事件响应方面的历史记录并进行考察。供应商可以提供来自其现有客户的对于其IRP的业内推荐。

### 9.5 要求

---

✓ 在企业的事件响应计划中，针对所用到的每个云服务供应商，必须对托管在该供应商的资源的事件检测和处理方法加以计划和描述。

✓ 对于所用到的每一个服务供应商，在与其约定的 SLA 中，必须保证对于企业事件响应所需要的事件处理支持，确保企业事件处理流程中检测、分析、遏制、根除和恢复每一阶段所对应企业事件响应计划的有效执行。

✓ 至少每年进行一次事件响应的测试。客户应尽最大可能寻求将自己的测试过程与其供应商（及其他合作伙伴）的测试过程集成到一起。理想情况下，应有一个团队（由客户和云服务供应商的成员共同组成）来针对一份事件响应计划执行各种健康检查，并相应的将改进建议应用于新一版的事故响应计划。

---

## 参考文献

[1] GRANCE, T., KENT, K., and KIM, B. Computer Security Incident Handling Guide. NIST Special Publication 800-61.

[2] MELL, P. and GRANCE, T. The NIST Definition of Cloud Computing, NIST Special Publication 800-145.

[3] GROBAUER, B. and SCHRECK, T. October 2010. Towards Incident Handling in the Cloud: Challenges and Approaches. In Proceedings of the Third ACM Cloud Computing Security Workshop (CCSW), Chicago, Illinois.

[4] WOLTHUSEN, S. 2009. Overcast: Forensic Discovery in Cloud Environments. In Proceedings of the Fifth International Conference on IT Security Incident Management and IT Forensics.

[5] REED, J. 2011. Following Incidents into the Cloud. SANS Reading Room

[6] DANYLIW, R., et al. 2007. The Incident Object Description Exchange Format, IETF Internet Draft RFC 5070.

[7] MORIARTY, K. 2010. Real-time Inter-network Defense, IETF Internet Draft RFC 6045.

[8] MORIARTY, K., and TRAMMELL, B. 2010. Transport of Real-time Inter-network Defense (RID) Messages, IETF Internet Draft RFC 6046.

[9] FITZGERALD, E., et al. 2010. Common Event Expression (CEE) Overview. Report of the CEE Editorial Board.

[10] BIRK, D. and WEGENER, C. 2011. Technical Issues of Forensic Investigations in Cloud Computing Environments In Proceedings of 6th International Workshop on Systematic Approaches to Digital Forensic Engineering (IEEE/SADFE), Oakland, CA, USA.

---

## D10: 应用安全

云环境，尤其是公有云环境，以其灵活性和开放性的优势颠覆了许多有关应用安全的基本假设。这些假设中一部分很好理解，但大部分并非如此。本文期望提供一份关于云计算如何影响一个应用的一生（从设计到运营到最后下线）的指南。这个指南可以指导所有的干系人（包括应用设计者、安全专家、运营人员以及技术管理者）如何在设计云计算应用时降低风险，确保过程可管理。

对于那些跨软件即服务（SaaS）、平台即服务（PaaS）和基础设施即服务（IaaS）多个层面的应用来说，云计算是一个特别的挑战。基于云的软件应用要求设计严密，这类似于一个连接到原始网络的应用－应用必须提供安全性，不能有任何有关外部环境的假设。但是暴露在云环境中的应用要面对的威胁要远超过在传统数据中心中经历的威胁。这就需要制定严格的实践，在云中开发或迁移至云中时，必须严格遵循这些实践。

## 概览 应用安全领域有以下焦点领域：

安全开发生命周期  $ S D L C^{52} $ （用于确保 S D L C 安全的一般实践及特定云的细微差别）

认证、授权、合规 - 云中的应用安全架构

身份验证，以及与云计算应用安全相关的身份验证的使用。授权流程和基于风险的访问管理以及与之相关的云计算应用中的云加密

■ 应用授权管理（策略制定/更新，执行）

针对云的应用渗透测试（一般实践与云应用下的细微差别）

■ 云计算应用的监控

应用认证、合规、风险管理及其在多租户及共享基础设施下的影响

■ 规避恶意软件和提供应用安全的区别

---

### 10.1 安全软件开发生命周期（SDLC）

安全软件开发生命周期（SSDLC）（也有些人称为安全开发生命周期 SDLC $ ^{53} $），在向云中迁移和部署应用时其重要性日益凸显。组织应该确保其开发过程和整个应用的生命周期中贯彻应用安全、身份管理、数据管理和隐私权的最佳实践。

云环境下的开发与传统托管环境在如下几个方面有所不同：

在公有云环境中，对物理安全的控制大幅度减少。

当服务（例如存储）从一个厂商迁移到另一个厂商时，可能不兼容。

必须考虑整个生命周期中对数据的保护，包括传输、处理和存储。

在云环境中，Web 服务的聚合导致的安全脆弱性开始显现。

访问日志的能力变得更加困难，尤其是在共享的公有云中，应该将其指定为服务水平承诺的一部分。

云中的数据故障转移和数据安全必须比传统环境更详细、分层更明确。

在云环境中，保障（并提供证据）合乎相关行业和政府的规则通常会更加困难。

在执行一个 SSDLC 时，企业必须采用开发的最佳实践。为此，要么企业自己拥有一套自主的流程、工具和技术，要么就采用一个成熟度模型，比如：

利用成熟度模型构建安全（BSIMM2）（最新的标准是 BSIMM4）

■ 软件保障成熟度模型（SAMM）

系统安全工程能力成熟度模型

#### 10.1.1 应用安全保证程序

企业应该有一个应用安全保障程序，确保在向云环境中迁移、开发或维护应用时能达到以下几点要求：

在足够的高层支持下，目标和指标被定义、实现以及追踪。

已针对云中应用建立起安全策略和隐私策略，用来满足法律和监管合规性需求，这些需求符合组织的业务需要和监管义务。

通过及时的聘用新员工或者培训合适的员工，来保证组织在架构、设计、开发、测试以及部署安全的应用时拥有充足的资源和安全保障的能力。

在所有应用上执行安全及隐私评估，来确保需求定义恰当。

定义并实施一系列流程，使云中的开发和维护过程达到确保安全和隐私要求。

---

配置及变更管理必须是可审计和可验证的。

执行针对应用和数据的物理安全风险评估，且所有云基础设置部件的访问都足以满足这些需求。

在开发阶段需要遵循规范化的编码最佳实践，要考虑到所使用语言的优势和劣势。

■ 隐私和安全评估必须是可审计且可验证的。

#### 10.1.2 验证及鉴权（V&V）

##### 10.1.2.1 设计复核

有些功能的安全敏感性远高于其他功能，运行在云环境中可能不是一个可行的候选方案，这个时候，需要考虑特殊的设计或者特定的需求。

在执行应用程序的安全设计时，应遵循以下原则。如果云计算架构无法满足这些原则，应该通过适当的技术和/或补偿控制予以修复。否则，将会对云计算的部署可行性带来问题。

最小特权。该原则主张个人、程序或其它类型的实体都应只在完成一项任务所需的最少时间内、持有最小特权和资源。在很多情况下，最小特权只能使用精细的、前后关联的应用程序授权管理与安全政策自动化机制得以有效实施。

职责分离 SOD。这是一项控制策略，根据这项策略，每个人的职责或者访问权限被控制住对应的范围内，不能对超越范围的部分拥有职责或者访问权限。

- 深度防御（Defense in depth）。这是一个多层次防护的应用，在这种应用中，如果前面的层被攻破，后面会提供保护。

失效安全（Fail safe）。如果云系统崩溃了，它应该处于系统的安全性以及数据不被危及的状态。例如，为了确保失效安全，系统默认进入这样一种状态，该系统会拒绝用户或程序的访问。

- 机制经济（Economy of mechanism）。该原则推崇简单、可理解的设计和实施保护机制，因此非计划的访问路径不存在或者很容易识别并拒绝。

- 完备仲裁（Complete mediation）。这种原则下，计算机系统中的实体 $ ^{54} $对某一个对象的所有访问请求都必须得到授权。

开放设计。指通过专家社区来评估和同行评审的开放访问的云系统设计，从而使设计更加安全。

最少公用机制（Least common mechanism）。指最小化跨多个应用程序的共用机制（尤其是保护机制）的数量，最大限度的减少一个应用程序出问题导致其它应用程序破坏或颠覆的能力。

最薄弱环节（Weakest link）。最重要的是识别安全链和防护层次中的最薄弱机制，并进行提升，从而将系统的风险降低到可接受的水平。

#### 10.1.3 构造

##### 10.1.3.1 代码审查

---

建议在企业级别定义并且遵从安全软件开发。可以遵从 SAFECode $ ^{55} $、CERT（SEI） $ ^{56} $ 或 ISO 标准等的基础实践部分描述的安全软件开发指南。

动态代码分析当代码在运行的云应用中执行时检查该代码，测试器跟踪源代码中的外部接口与执行代码的相互作用，因此任何出现在执行接口中的漏洞或异常现象也同时在源代码中被定位，从而可以在源代码中修复。

和静态分析不同，动态分析启用测试器来不断执行软件，以暴露用户交互、配置变更或环境组件的行为等方式引入的漏洞。

下面列举了一些编写安全代码和审查的最佳实践：

云服务器代码中应该包含最少的必要信息。注释应该从运行代码中剥离，并且避免带有姓名和其它个人信息。

- 利用源代码分析工具来检查典型的编程错误，比如缓存溢出、格式化字符串攻击、条件竞争（Race Conditions）等。

验证并确认所有输入、用户、计算机和交互系统。当云基础架构接受任意输入并将该输入的内容应用到命令或SQL语句时，可能发生内容注入和一些其它攻击。

- 使用目标代码（二进制）时，例如，正在使用第三方库，在目标代码上使用能够测试静态漏洞的测试服务。

##### 10.1.3.2 安全测试

渗透测试是一种安全测试方法，它通过模拟恶意来源的攻击让测试者掌握目标网络的安全强度。该过程包含寻找任意潜在漏洞的云系统主动分析，这些漏洞可能由于系统配置不足或不当、已知或未知的软硬件缺陷、或者操作规程或技术措施的缺陷而导致。该分析以潜在攻击者的角度执行，可能会包含安全漏洞的主动利用。

云模型的类别极大地影响了渗透测试或者决定渗透测试是否可行。一般来说，平台即服务（PaaS）和基础设施及服务（IaaS）可能允许渗透测试。然而，软件即服务（SaaS）提供商不太可能允许客户对其应用和基础设施进行渗透测试，除了云提供商自己为了合规或安全最佳实践而让第三方执行的渗透测试。

渗透测试通常在 “黑盒” 场景中执行，也就是说，预先不了解将要测试的基础设施。在其最简单的级别，渗透测试包括三个阶段：

1. 准备。这个阶段执行止式合同，合同包含对客户数据保密以及对测试者的法律保护。至少，合同需列出要测试的 IP 地址。

2. 执行。这个阶段中执行渗透测试，测试者寻找潜在的漏洞。

3. 交付。评估结果交付给测试者在企业中的联络人，并且会提供纠正措施。

不管渗透测试是全了解（白盒）测试、部分了解（灰盒）测试还是零了解（黑盒）测试，得到报告和结果后，必须应用缓解技术来将泄漏风险降低到可接受水平。该测试应在尽可能大的范围来确定某些领域的漏洞和相应的风险，如应用、远程访问系统和其它相关IT资产。