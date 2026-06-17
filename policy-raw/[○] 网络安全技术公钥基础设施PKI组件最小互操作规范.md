---
title: "网络安全技术公钥基础设施PKI组件最小互操作规范"
source: "z.政策梳理/2.标准/2.1国家推荐标准/网络安全技术公钥基础设施PKI组件最小互操作规范.pdf"
type: "pdf"
processed: "2026-04-22T19:33:07.030805"
---

ICS 35.030

CCS L 80

<div style="text-align: center;"><img src="imgs/img_in_image_box_798_89_1031_210.jpg" alt="Image" width="19%" /></div>


## 中华人民共和国国家标准 GB/T 19771—XXXX

# 网络安全技术 公钥基础设施 PKI 组件最小互操作规范

# Cyberspace security technology – Public key infrastructure – Minimum interoperability specification for PKI components

(点击此处添加与国际标准一致性程度的标识)

(征求意见稿)

在提交反馈意见时，请将您知道的相关专利连同支持性文件一并附上。

XXXX - XX - XX 发布

XXXX - XX - XX 实施

发布

国家市场监督管理局

国家标准化管理委员会

---

## 网络安全技术 公钥基础设施 PKI 组件最小互操作规范

## 1 范围

本文件规定了公钥基础设组件最小互操作的基本功能要求和数据格式要求，给出了测试评价方法。本文件适用于电子签名、电子签章、身份管理等中的PKI的设计、开发、测试及其应用。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。其中，注日期的引用文件，仅该日期对应的版本适用于本文件；不注日期的引用文件，其最新版本（包括所有的修改单）适用于本文件。

GB/T 15852.2 信息技术 安全技术 消息鉴别码 第2部分: 采用专门设计的杂凑函数的机制

GB/T 16262.1 信息技术 抽象语法记法

GB.T 19714-XXXX 网络安全技术 公钥基础设施 证书管理协议

GB/T 20518-2018 信息安全技术 公钥基础设施 数字证书格式

GB/T 32905-2016 信息安全技术 SM3密码杂凑算法

GB/T 32907-2016 信息安全技术 SM4分组密码算法

GB/T 32918.2-2016 信息安全技术 SM2椭圆曲线公钥密码算法 第2部分：数字签名算法

GB/T 37092-2018 信息安全技术 密码模块安全要求

## 3 术语和定义

下列术语和定义适用于本文件。

### 3.1 

公钥基础设施 public key infrastructure

基于公钥密码技术，具有普适性，可用于提供保密性、完整性、真实性及抗抵赖性等安全服务的基础设施。

[来源：GM/Z 4001-2013，2.29，有修改]

### 3.2 

数字证书 digital certificate

也称公钥证书，由证书认证机构对用户的公钥和身份信息进行确认，并用私钥进行签名的数据。

### 3.3 

加密证书 encipherment certificate

用于证明加密公钥的数字证书。

[来源：GM/Z 4001-2013，2.43，有修改]

证书认证机构 Certificate Authority

### 3.4 

负责创建和颁发证书，受用户信任的权威机构。

---

### 3.5 

## 注册机构 Registration Authority

为用户办理证书申请、身份审核、证书下载、证书更新、证书注销以及密钥恢复等实际业务的办事机构或业务受理点。

### 3.6 

证书持有者 certificate holder

与有效证书的主体相对应的实体。

### 3.7 

证书使用者 certificate user

需要获取另一实体的公钥，并利用PKI获取证书并执行验证证书和签名功能的实体。

### 3.8 

资料库 repository

存储数字证书和CRL等信息，并提供无需验证的信息检索服务的数据库。

### 3.9 

证书策略 certificate policy

预先定义的界定证书的通用安全要求和适用范围的一组规则集。

### 3.10 

认证业务声明 Certification Practice Statement

证书认证机构颁发某证书策略的证书时遵循的相关业务操作的声明。

### 3.11 

## 证书认证路径 certification path

基于起始可信证书的有序证书序列。

注：通过处理该有序序列及其起始对象的公钥能得知该路径的末端对象的公钥。

### 3.12 

证书撤销列表 Certificate Revocation List

列出一组证书发布者认为无效的已签名列表。

## 4 缩略语

下列缩略语适用于本文件。

BYOD: 自带设备（Bring Your Own Device）

CA: 证书认证机构（Certificate Authority）

CRL：证书撤销列表（Certificate Revocation List）

LDAP：轻量级目录访问协议（Lightweight Directory Access Protocol）

PKCS: 公钥密码学标准（Public Key Cryptography Standard）

PKI：公钥基础设施（Public Key Infrastructure）

RA: 注册机构（Registration Authority）

## 5 基本功能要求

### 5.1 概述

本文件描述的PKI系统由四个需要互相通信的组件构成，分别是：

- 负责颁发和撤销证书的CA；

---

——确保公钥和证书持有者的身份以及别的属性之间绑定的RA；

--获得证书和签署文档的证书持有者；

--验证签名并且执行密钥管理协议以及验证证书认证路径的证书使用者。

这四个组件分别提供不同的功能，但一个实体可以承担多个组件的角色。CA可以也是RA。在功能上是证书持有者的实体也是证书使用者，证书使用者可以不是证书持有者。

本文件描述的互操作指的是PKI组件之间通过互相通信和协作，共同完成PKI功能的操作。最小互操作指的是PKI组件为了实现证书注册、证书更新、证书撤销、资料库访问等PKI基本功能所需要的最低限度的互操作。文本描述的最小互操作的基本功能要求指的是这些组件为了实现基本的PKI功能，所必须具备的基本功能集合。

### 5.2 CA

CA应支持以下功能：

--颁发并传送证书给终端实体和其他的CA；

--接收来自RA的证书撤销请求；

--将证书和CRL存入资料库；

——为下级CA颁发证书。

CA生成自己的公私钥对并公布自己的证书，CA生成、估定相应的参数以便生成/验证所颁发证书的签名。CA授权RA去确认申请证书的使用者的身份或其他的特征属性。授权通过离线接受来自某个RA的证书请求完成。CA具备5.4中证书持有者的功能：请求、撤销、更新由其他CA颁发的证书；也具备5.5中证书使用者的功能：检索证书和CRL、验证证书认证路径。

CA与其他组件进行互操作时，基本功能要求为：

## a）颁发数字签名证书

CA应支持两种数字签名证书的证书请求: RA发起的注册请求和自我注册请求。根据不同类型，CA采用不同方式鉴别申请证书主体的身份。

1）RA发起的证书请求。RA应确保用户身份与公钥的绑定。CA处理来自经授权的RA的证书请求。如请求被接受，CA生成新证书并存储在资料库中，然后将该证书发给相应的RA或证书持有者。如请求由非经授权的RA发送，即签名无效或信息不匹配，CA拒绝请求并向RA报告失败并说明原因。CA应至少能支持GB/T 20518-2018中定义的颁发机构密钥标识符（authorityKeyIdentifiers）、主体密钥标识符（subjectKeyIdentifier）、基本限制（basicConstraints）、密钥用法（keyUsage）、证书策略（certificatePolicies）等扩展。

2）自我注册请求。RA为提交请求的实体提供一份秘密信息。请求实体生成公私钥对，创建证书请求消息并使用相应私钥签名，被签名的部分包括基于RA提供的秘密信息导出的认证信息。CA接收请求，通过认证信息验证请求者身份，并确认其实体拥有私钥。若验证成功，CA生成新证书并存入资料库，随后发送至证书持有者。若验证失败、签名无效或信息不匹配，CA拒绝请求并向申请者报告失败原因。

## b) 颁发加密证书

CA应支持实体进行加密证书的申请。CA处理来自授权的RA的加密证书的请求。如请求被接受，CA验证响应证书申请，用户的加解密公私钥对可由第三方产生，CA通过安全的方式获得加密公钥和用户加密私钥数据信封。CA颁发加密证书并存储在资料库中，并将该证书和加密私钥数据信封返回给相应的RA或证书持有者。

## c) 交叉认证

---

CA应具备向其他CA颁发证书的能力。交叉认证决策通过物理形式进行，并应按照与证书策略相关的认证业务声明进行安全可信检查。CA应对颁发的交叉证书的路径验证做出适当约束，应将basicConstraints $ \leftarrow $nameConstraints和policyConstraints设置为关键扩展并配置相应约束条件，包括路径长度的约束。如未设置这些扩展或不进行路径验证约束，即允许对方CA无限制地进行签名传递，即，颁发交叉证书的CA应承担其证书策略对应的认证业务声明中承诺的全部责任，包括给其他无关CA颁发的所有证书的责任。

## d）证书更新请求

申请者通过其原有私钥对更新请求消息进行签名以完成身份验证。CA处理证书更新请求，若签名有效，则颁发新证书给证书持有者并存入资料库。若签名无效、请求实体处于非法状态或更新请求不符合CA认证业务声明或证书策略，CA拒绝该请求。

## e) 证书撤销

CA应按照相关书策略对应的认证业务声明，按时生成和发布包含所有被撤销但尚未到期的证书的完整证书撤销列表(CRL)。颁发CRL的形式和周期由相关证书策略对应的认证业务声明决定。

## f）为下级CA颁发证书

CA应能向层次更高的CA申请证书。在生成证书请求时，应使用basicConstraints扩展来明确该请求来自一个CA实体。在颁发下级CA证书时，应在证书中明确授权的证书策略、层级限制以及名称限制。如缺少这些扩展，或者这些扩展存在但被设置为非关键项，则上级CA应对下级CA颁发的所有证书承担与证书策略对应的认证业务声明中所承诺的所有的法律责任。

### 5.3 RA

#### 5.3.1 与互操作性有关的功能要求

RA应支持以下功能：

——接受和验证证书请求；

——向CA发送证书请求；

——生成证书撤销请求。

RA与其他组件进行互操作时，基本功能要求为：

a）当物理证书介质与RA进行物理连接时，RA通过验证签名消息来验证该介质中拥有与公钥相应的私钥材料(见6.5.2)。在密钥对和实体身份均经过验证之后，RA签署并向相应的CA发送电子证书请求。

b）未与RA进行过物理接触的证书请求者，在发起证书请求时，应持有RA提供的认证信息。此信息将作为实体在自我注册请求中向CA证明其身份的证据。

c）RA应支持对CA授权其所管理的实体证书请求进行证书撤销操作。该功能可与CA集成，也可在不同的设施中执行。

d）RA应将新颁发的证书与CA的证书一同发送给证书持有者。

e）RA应代表不再拥有私钥并且怀疑该私钥已泄露的证书持有者产生并签署证书撤销请求。如果CA的认证业务声明允许，RA应代表证书持有者的组织产生并签署证书撤销请求。

#### 5.3.2 使用 BYOD 请求证书的 RA 功能要求

RA应验证BYOD设备的密码模块是否符合GB/T 37092-2018的要求。RA应鉴别密码模块的安全等级是否与认证业务声明一致。

### 5.4 证书持有者

#### 5.4.1 与互操作性相关的功能要求

---

证书持有者包括CA、RA和其他的终端实体。终端实体是个人、企业、用户、计算机系统、或应用程序(CA和RA除外)。

证书持有者应包括以下功能：

——生成签名；

——生成证书注册请求；

——生成证书撤销请求；

——生成证书更新请求。

证书持有者同时也是证书使用者，具备5.5中定义证书使用者的功能。

#### 5.4.2 证书持有者的 BYOD 功能要求

证书持有者BYOD作为证书介质申请或使用证书服务时，该设备应安装有符合GB/T37092-2018的密码模块并具备未被破坏的可信启动。该设备也应具备数字证书展示和通信能力，如，使用二维码交换证书和签名。BYOD设备不应要求物理接入他人的设备进行证书展示和验证。

### 5.5 证书使用者

#### 5.5.1 与互操作性有关的功能要求

证书使用者是使用证书的实体，包括CA、RA、个人、企业、用户和计算机系统。

证书使用者应包括以下功能：

——验证证书；

——从查询服务器中检索证书和CRL；

——验证证书认证路径。

具有证书持有者身份的证书使用者也能产生签名、支持撤销或更新证书。

#### 5.5.2 验证证书的最小步骤要求

证书使用者应能获得从信任起点开始的完整的证书路径。信任起点可以是预埋的根证书，也可以是预埋的CA证书，也可以是经过验证后缓存的可信CA的证书。

证书使用者应从信任起点的证书开始，针对每个证书，逐一完成以下验证：

a) 验证证书基本信息。

1) 使用颁发该证书的CA的公钥验证签名；

2) 验证有效期；

3) 验证证书是否被撤销；

4) 验证证书颁发者的名称。

b) 验证关键证书扩展。

c) 如果证书是自签名证书，且不是路径中的最终证书，跳过本步骤。否则，验证主体名称是否在颁发该证书的CA证书中的nameConstraints扩展（如适用）中一个允许的子树中，并验证subjectAltName扩展中的每个替代名称（关键或非关键）是否在该名称类型的一个允许的子树中。

d) 如果证书是自签名证书，且不是验证路径中的最终证书，跳过本步骤。否则，验证主体名称不在颁发该证书的CA证书中的nameConstraints扩展（如适用）中的任何排除子树中，并验证subjectAltName扩展中的每个替代名称（关键或非关键）不在该名称类型的任何排除子树中。

e) 如果有证书策略（certificatePolicies）扩展，验证该扩展是否使用符合预期的策略。

任何未通过都表示该证书不能被信任。

### 5.6 密码算法

---

## GB/T 19771—XXXX

本文件的PKI组件使用四类算法：密码杂凑函数、数字签名算法、消息鉴别码算法和对称加密算法。PKI组件使用密码算法的总体安全要求如下：

a) 一个PKI组件应实现一个数字签名算法，其他组件应能够产生和验证由其中一个算法生成的签名

b）组件应支持一个加密算法。

对四类算法的要求如下:

c）应支持GB/T 32905-2016规定的SM3密码杂凑算法；

d）应支持GB/T 32918.2-2016规定的SM2数字签名算法；

e）应支持GB/T 15852.2规定的MAC算法2（HMAC）；

f）应支持GB/T 32907-2016规定的SM4分组密码算法。

## 6 数据格式要求

### 6.1 数字证书

证书的数据结构、证书扩展、证书撤销列表应符合GB/T 20518-2018的要求。

### 6.2 PKI 事务消息内容

#### 6.2.1 总体要求

PKI事务包括：注册请求、更新证书、撤销证书、访问目录服务。CA、RA和证书持有者应能实现这些事务。PKI事务的消息格式应符合GB/T 19714-XXXX第6章的要求。

对于CA和RA物理上在一起且不支持远端RA的PKI产品，可忽略CA和RA之间的消息交互。

#### 6.2.2 注册请求

##### 6.2.2.1 RA 发起的注册请求

RA请求CA为一个终端实体颁发签名证书，终端实体通过物理方式(如，提交实体U盘)，在签名消息中向RA提供其公钥。RA产生认证请求，利用签名消息保护请求，向CA为终端实体申请证书。CA产生响应并发送给RA，响应消息中包含证书或错误代码的签名。RA通过物理形式向终端实体提供CA的公钥和所颁发的证书，终端实体也可以直接从CA获得证书。

在这个过程中包括三条消息：

## a) 从RA到CA的证书请求

RA建立证书请求的PKIMessage，并发送给CA，其PKIBody的请求代码为cr。其中，PKIHeader的sender是RA的可辨别名，recipient是CA的可辨别名。PKIBody是CertReqMessages，是一个CertReqMessage字段的序列，应包括如下信息：

• certReq含有请求者希望包含在证书中的信息；

• pop证明了对新证书私钥的拥有。

本文件只支持终端实体产生签名密钥对，不支持终端实体产生加密密钥对。在进行签名私钥的拥有性证明时，如果由RA来实现，RA修改了主体名，popoSKInput域出现，并且包含了原来的主体名。否则，RA不修改主体名，pop域与请求者提交的主体名一致。

与证书内容相关的信息放入为CertRequest的certReq中。

PKIProtection字段含有根据消息头和消息体的DER编码序列计算的RA的签名。

## b) 从CA到RA的证书响应

CA返回证书响应请求的PKIMessage给RA，其PKIBody的响应代码为cp。其中PKIHeader的sender是CA的可辨别名，recipient是RA的可辨别名。如果在证书请求中提供了senderNonce，响应的PKIHeader应

---

将其作为recipNonce。PKIBody是CertRepMessage，CertRepMessage含有唯一的response字段，是包含certReqId、status和certifiedKeyPair的序列。如果CA颁发了一张证书，PKIBody应含有如下信息：

• certReqId与请求中的certReqId匹配；

status是granted或者是grantedWithMods;

• certifiedKeyPair序列至少含有一个字段certificate。

## 证书应满足如下性质：

• version号应是v3(2);

• publicKey字段应与证书请求中相同或者是由CA所产生的公钥；

主体可辨别名应与证书请求中相同；

- 颁发者名字应是CA的可辨别名；

- 如果notBefore出现在证书请求中, 证书应从颁发日和notBefore所指之日的较晚者之后生效;

如果notAfter出现在证书请求中，证书应在该日或之前期满。

证书应包括如下扩展(extensions):

- subjectKeyIdentifier域;

- 在certificatePolicies字段中至少包括一个证书策略的OID；

• authorityKeyIdentifier域。

如果status是granted和grantedWithMods, failInfo字段可不存在。

如果CA拒绝了请求，PKIBody应含有如下信息：

• status是rejected;

• failInfo包含适当的错误代码。

如果status是rejected, certifiedKeyPair字段可以不出现。

PKIProtection字段含有根据消息头和消息体的DER编码序列计算的CA的签名。

##### 6.2.2.2 新实体的自我注册请求

如果新实体尚未从某一特定CA获取证书，可直接向该CA申请一张新的证书。在申请过程中，请求实体生成一个请求代码为ir的PKIMessage以请求新证书，该消息中包含对所请求证书中公钥相对应的私钥的拥有证明。实体利用RA提供的一个秘密密钥和消息鉴别码算法对PKIMessage进行保护。

如果CA接受自我注册请求，向证书持有者返回一个响应代码为ip的PKIMessage。该消息包含证书或者事务出错的原因代码。

## a) RA与实体之间的事务

RA给实体发送一个共享的秘密密钥。通过从该共享秘密中生成消息鉴别码，CA对实体进行认证。

本文件不指定该事务明确的内容和格式。但是，秘密密钥和CA的公钥信息应以可信方式传递给实体。

b) 从证书持有者到CA的自我注册请求

请求者建立一个PKIMessage，其PKIBody的请求代码为ir。PKIHeader的sender是请求者的可辨别名，recipient是CA的可辨别名。PKIBody是CertReqMessages，是一个CertReqMessage字段的序列。CertReqMessage包括如下信息：

• certReq含有请求者希望包含在证书中的信息；

• popoSKInput包含公钥的MAC值；

• pop证明了对证书私钥的拥有。

其中pop域通过与CertTemplate中的公钥相对应的私钥来产生，产生pop的输入数据包括popoSKInput中的公钥MAC值和CertTemplate中的公钥。

与证书内容相关的信息放入为CertRequest的certReq中。

---

PKIProtection域包含一个请求者利用从RA获得的秘密产生的值。

## c) 从CA到证书请求者的自我注册请求的响应

CA返回证书响应请求的PKIMessage给证书持有者，其PKIBody的响应代码为ip。其中，PKIBody的sender是CA的可辨别名，recipient是证书请求消息头中sender域的值。如果在证书请求中提供了transactionID，响应的PKIHeader中包括同样的transactionID。如果在证书请求中提供了senderNonce，响应的PKIHeader应将其作为recipNonce。PKIBody是CertRepMessage。如果CA颁发了一张证书，PKIBody应含有如下信息：

status是granted或者是grantedWithMods;

• certificate包含新的证书。

如果status是granted和grantedWithMods, failInfo字段可以不存在。

如果CA拒绝了请求，PKIBody应含有如下信息：

• status是rejected;

failInfo包含适当的错误代码。

如果status是rejected, certificate域可能不存在。

证书应包括如下扩展(extensions):

- subjectKeyIdentifier域;

• 在certificatePolicies字段中至少包括一个证书策略的OID;

• authorityKeyIdentifier域。

PKIProtection字段含有根据消息头和消息体的DER编码序列计算的CA的签名。

##### 6.2.2.3 已知实体的自我注册请求

如果某一实体并非当前证书持有者，但是先前曾从特定CA获得过证书，该实体可直接向该CA提出新证书的申请。在申请过程中，请求实体生成请求代码为cr的PKIMessage以请求新证书，该消息中包含与证书请求中公钥所对应的私钥的拥有证明。实体利用RA提供的一个秘密密钥和消息鉴别码算法PKIMessage进行保护。。

如果CA接受自我注册请求，向证书持有者返回一个响应代码为cp的PKIMessage。该消息包含证书或者事务出错的原因代码。

## a) RA与实体的事务

RA给实体发送一个共享的秘密密钥。CA通过从共享的秘密中产生的消息鉴别码，对实体进行认证。

本文件不指定该事务明确的内容和格式。但是，秘密密钥和CA的公钥信息应以可信方式传递给实体。

b) 从证书持有者到CA的自我注册请求

请求者建立一个PKIMessage，其PKIBody的请求代码为cr。PKIHeader的sender是请求者的可辨别名，recipient是CA的可辨别名。PKIBody是CertReqMessages，是一个CertReqMessage字段的序列。CertReqMessage包括如下信息：

- certReq含有请求者希望包含在证书中的信息；

• popoSKInput包含公钥的MAC值；

• pop证明了对证书私钥的拥有。

其中pop域通过与CertTemplate中的公钥相对应的私钥来产生，产生pop的输入数据包括popoSKInput中的公钥MAC值和CertTemplate中的公钥。

与证书内容相关的信息放入为CertRequest的certReq中。

PKIProtection域包含一个请求者利用从RA获得的秘密产生的值。

c）从CA到证书请求者的自我注册请求的响应

---

CA返回证书响应请求的PKIMessage给证书持有者，其PKIBody的响应代码为cp。其中，PKIBody的sender是CA的可辨别名，recipient是证书请求消息头中sender域的值。如果在证书请求中提供了transactionID，响应的PKIHeader中包括同样的transactionID。如果在证书请求中提供了senderNonce，响应的PKIHeader应将其作为recipNonce。PKIBody是CertRepMessage。如果CA颁发了一张证书，PKIBody应含有如下信息：

status是granted或者是grantedWithMods;

• certificate包含新的证书。

如果status是granted和grantedWithMods, failInfo字段可以不存在。

如果CA拒绝了请求，PKIBody应含有如下信息：

• status是rejected;

failInfo包含适当的错误代码。

如果status是rejected, certificate域可能不存在。

证书应包括如下扩展(extensions):

- subjectKeyIdentifier域;

- 在certificatePolicies字段中至少包括一个证书策略的OID；

• authorityKeyIdentifier域。

PKIProtection字段含有根据消息头和消息体的DER编码序列计算的CA的签名。

##### 6.2.2.4 加密证书申请

拥有当前有效证书的PKI实体可向该证书的颁发CA提出申请，申请产生加密密钥对并颁发相应的证书。发出申请的实体产生临时的密钥管理密钥，并生成请求代码为cr的PKIMessage，以申请密钥管理证书，PKIMessage中包括了临时的密钥管理密钥。利用当前有效证书的对应私钥，对PKIMessage进行签名并发送给CA。

如果CA的CPS支持集中产生加密密钥对，则CA执行如下操作：

--CA按请求消息的要求产生密钥对，颁发加密证书；

--CA产生对称密钥，利用对称密钥加密新产生的私钥，使用临时公钥加密对称密钥，产生和返回响应消息给证书持有者。响应消息中包括了新生成的证书和加密后的私钥，或者是事务失败的代码。

用户的加解密公私钥对也可由可信第三方（如，密钥管理系统）产生，应采用符合GB/T 19714-XXXX中7.5节规定的协议和消息格式获得产生的公钥和加密私钥数字信封。CA颁发加密证书并存储在资料库中，并将该证书和以用户公钥保护的加密私钥返回给相应的RA或证书持有者。

##### 6.2.2.5 组合证书申请

签名密钥证书和密钥管理密钥证书的申请可以由一次事务完成。RA发起的注册请求和自我注册请求（见6.2.2.1、6.2.2.2、6.2.2.3）可以和加密证书申请（见6.2.2.4）组合在一起。在此情况下，CertReqMessages包括了两个CertReqMessage的序列。一个CertReqMessage等同于RA发起的注册请求和自我注册请求的情况，另一个CertReqMessage等同于加密证书申请的情况。消息使用了签名证书申请的方式来加以保护。

如果组合申请中包括的是自我注册请求，则要么签名密钥证书申请成功，要么两个证书的申请都不成功。如果还需要额外的信息来提供pop，申请者则使用自我注册请求中的私钥来对消息做签名。

#### 6.2.3 证书更新

---

拥有当前有效(指在有效期内、未被撤销)证书的PKI实体可直接向该证书的颁发CA要求颁发一份新的证书。PKI实体生成请求代码为kr的PKIMessage，包括证书申请和相应的pop。证书持有者使用有效证书的对应私钥对该PKIMessage进行签名。

如果CA的CPS支持证书更新，则CA返回请求代码为kp的PKIMessage，包含新生成的证书或者是事务失败的代码。

如果新证书成功生成，则还有两个可选的消息。分别是：PKI实体在收到新的证书后给CA发出确认，CA响应确认消息。

## a）从证书持有者到CA的证书更新申请

证书持有者建立一个PKIMessage，其PKIBody的请求代码为kr。PKIHeader的sender是证书持有者的可辨别名，recipient是CA的可辨别名。PKIBody是CertReqMessages，是一个CertReqMessage字段的序列。CertReqMessage包括如下信息：

- certReq包含了申请者要求包括在证书中的各种信息；

• pop是新证书公钥的对应的pop证明。

pop应由publicKey域的公钥对应的私钥产生。CertReq的publicKey域是新证书的公钥。

如果消息中没有signingAlg, CA应使用终端实体的公钥对应的算法签名。

PKIProtection域是使用当前有效证书的对应私钥对消息头和消息体的DER编码信息的签名结果。

## b）从CA到证书持有者的证书更新响应

CA返回证书更新响应请求的PKIMessage给证书持有者，其PKIBody的响应代码为kp。其中，PKIBody的sender是CA的可辨别名，recipient是证书请求消息头中sender域的值。如果在证书请求中提供了transactionID，响应的PKIHeader中包括同样的transactionID。如果在证书请求中提供了senderNonce，响应的PKIHeader应将其作为recipNonce。PKIBody是CertRepMessage。如果CA颁发了新证书，PKIBody应含有如下信息：

status是granted或者是grantedWithMods;

• certificate包含新的证书。

如果status是granted和grantedWithMods, failInfo字段可以不存在。

如果CA拒绝了请求，PKIBody应含有如下信息：

• status是rejected;

failInfo包含适当的错误代码。

如果status是rejected, certificate域可能不存在。

证书应包括如下扩展(extensions):

- subjectKeyIdentifier域:

• 在certificatePolicies字段中至少包括一个证书策略的OID;

• authorityKeyIdentifier域。

PKIProtection字段含有根据消息头和消息体的DER编码序列计算的CA的签名。

#### 6.2.4 撤销请求

证书持有者可以请求撤销自己的证书。证书持有者产生RevReq消息，对该消息进行签名并发送给相应RA，并在RA审查通过用户的身份后向CA发出相应撤销信息。该签名必须用未过期、未被撤销的签名证书的相应私钥产生(可为要撤销的证书)。RevReq消息要标识出想撤销的证书以及要撤销的原因。CA回应RA一个RevReq消息。RA再回应证书持有者相应的RevReq消息。

如果消息rr(RevReq)中包含transactionID，则CA和RA所响应的rp(RevRep)消息中也应包含相同的transactinID，注意其中从证书持有者所发出的rr和RA所发出的rr消息中的transactinID可以不同。rp消息至少要包含status字段以反映请求的状态和revCerts字段以表示将撤销的证书。

---

## a）从证书持有者到RA的撤销请求

证书持有者建立一个PKIMessage，其PKIBody的请求代码为rr。PKIHeader的sender是证书持有者的可辨别名，recipient是RA的可辨别名。PKIBody是RevReqContent，是RevDetails的序列，由CertDetails和三个可选字段组成的序列：原因标志、怀疑或丢失的日期和时间、crlEntryDetails(CRL Entry扩展的序列)。CertDetails最少包括以下信息：

• serial证书序列号:

issuer证书发放者的标识名。

或是

- subject证书持有者的标识名；

issuer证书发放者的标识名。

CertDetails还可在extensions字段中包含subjectKeyIdentifier。(如果请求者希望撤销颁发给某个主体的所有证书，CertDetails应仅含有subject和issuer。即，仅希望撤销单个证书的请求只含有相应的序列号或是subjectKeyIdentifier)。

RevDetails应包括带有reasonCode扩展的crlEntryDetails, 也可包括invalidityDate扩展来说明何时该证书作废。原因代码也可不是removeFromCRL。

PKIProtection字段含有请求者的签名，即消息头和消息体的DER编码进行签名。终端实体用相应CA所颁发的当前有效签名证书的相应私钥进行签名。

## b）从RA到CA的撤销请求

RA或证书持有者生成包含PKIBody元素rr的 PKIMessage。PKIHeader包含以下信息：

pvno是103;

• transactionID标识RA名一起唯一标识一个RA与CA之间事务的整数；

• messageTime为当前精确到秒的时间；

• sender为RA的可辨别名；

• recipient为CA的可辨别名；

• protectionAlg为保护消息而使用的签名算法标识符。

消息体与从证书持有者到RA的撤销请求相同。

PKIProtection字段含有RA的签名，即对头和正文的DER编码进行签名。RA要用相应CA所颁发的当前有效签名证书的相应私钥进行签名。

## c）从CA到RA的撤销响应

CA返回证书更新响应请求的PKIMessage给证书持有者，其PKIBody的响应代码为rp。其中，PKIBody的sender是CA的可辨别名，recipient是RA的可辨别名。如果在证书请求中提供了senderNonce，响应的PKIHeader应将其作为recipNonce。PKIBody是RevRepContent。如果CA撤销了证书，正文将包含以下信息：

status是granted或是grantedWithMods;

• revDetails将包含已撤销证书的CertId。

如果status是granted或grantedWithMods, failInfo字段也可以不出现。

如果CA拒绝了请求，PKIBody应含有如下信息：

• status是rejected;

failInfo包含适当的错误代码。

对于能够确定有问题的证书，revCerts包含被拒绝撤销证书的CertId。PKIProtection字段包含CA的签名，即对头和正文的DER编码进行签名。

若CA生成CRLs，并且撤销请求被接受，CRL将有以下值：

- userCertificate字段中的被撤销证书的序列号；

---

• revocationDate收到撤销请求的日期和时间；

• crlEntryExtensions。

crlEntryExtensions包括：

• revCerts字段中的reasonCode, 除非CA的策略有专门规定；

(可选的) revCerts字段中的badSinceDate扩展可以是invalidaityDate。

## d）从RA到证书持有者的撤销响应

RA在收到CA的回应消息后，返回含有响应代码为rp的PKIMessage给证书持有者。其中，PKIBody的sender是CA的可辨别名，recipient是RA的可辨别名。如果响应的从证书持有者到RA的撤销请求消息中有senderNonce，则响应的PKIHeader中应把它作为recipNonce。PKIBody是RevReqContent，内容与从CA到RA的撤销响应相同，PKIProtection字段包含RA的签名，即对消息头和消息体的DER编码进行签名。

#### 6.2.5 访问资料库

##### 6.2.5.1 从资料库请求证书

证书使用者可使用LDAP V3向资料库请求证书。当使用LDAP时，证书使用者可以通过LDAP搜索请求从资料库中请求证书，或是利用给定的LDAP URL来请求证书(即authorityInformationAccess扩展)。

##### 6.2.5.2 从资料库请求 CRL

证书使用者可使用LDAP V3向资料库请求CRLs。证书使用者可使用LDAP从资料库中请求CRLs。当使用LDAP时，实体可以通过LDAP搜索请求从资料库中请求CRLs，或是利用给定的LDAP URL来请求CRLs（即，cRLDistributionPoints扩展中的distributionPoint字段）。

## 7 测试评价方法

### 7.1 通用测试评价方法

可采用人工访谈、文档查阅、人工核查等方法，确认CA的功能是否符合5.2的要求，确认RA的功能是否符合5.3的要求，确认证书持有者的功能是否符合5.4的要求，确认证书使用者的功能是否符合5.4的要求。

可采用人工访问、文档查阅、人才核查等方法，确认与互操作有关的数字证书的格式是否符合6.1的要求，确认与互操作有关的PKI事务消息内容的格式是否符合6.2的要求。

### 7.2 基本功能测试评价方法

#### 7.2.1 CA 功能测试评价

可采用人员访谈、文档查阅、人工核查等方法。内容包括：

a）确认CA在处理RA发起的注册签名证书请求时的方法是否符合5.2 a1的要求；

b）确认CA在处理自我注册签名证书的请求时的方法是否符合5.2 a)2)的要求；

c）确认CA在处理加密证书请求时的方法是否符合5.2 b)的要求；

d）确认CA在处理证书更新请求时的方法是否符合5.2 c)的要求；

e）确认CA在处理证书撤销时的方法是否符合5.2 d)的要求；

f）确认CA在为下级CA证书颁发证书时的处理方法是否符合5.2 e)的要求；

g）确认CA是否能够实现注册请求、更新证书、撤销证书、访问目录服务等事务；

h）确认CA是否支持5.6中要求的相关密码算法。

---

#### 7.2.2 RA 功能测试评价

可采用人员访谈、文档查阅、人工核查等方法。内容包括：

a）确认RA在处理物理接触的证书请求者发起的证书请求时的方法是否符合5.3.1 a)的要求；

b）确认RA在处理未进行物理接触的证书请求者发起的证书请求时的方法是否符合5.3.1 b)的要求

c）确认RA是否支持对CA授权其所管理的实体证书请求进行证书撤销操作；

d）确认RA是否支持将新颁发的证书与CA的证书一同发送给证书持有者；

e）确认RA是否可以代表不再拥有私钥并且怀疑该私钥已泄露的证书持有者产生并签署证书撤销请求；

f）确认RA是否能验证BYOD设备的密码模块符合GB/T 37092-2018的要求，并是否能鉴别密码模块的安全等级与认证业务声明的一致性；

g）确认RA是否能够实现注册请求、更新证书、撤销证书、访问目录服务等事务；

h）确认RA是否支持5.6中要求的相关密码算法。

#### 7.2.3 证书持有者功能测试评价

可采用人员访谈、文档查阅、人工核查等方法。内容包括：

a）确认证书持有者是CA、RA或其他的终端实体中的一种；

b）确认证书持有者是否能够生成签名、生成注册证书请求、发起证书撤销请求、发起证书更新请求；

c）确认证书持有者是否具备5.5中定义证书使用者的功能；

d）确认证书持有者是否能够实现注册请求、更新证书、撤销证书、访问目录服务等事务；

e）确认证书持有者是否支持5.6中要求的相关密码算法。

#### 7.2.4 证书使用者功能测试评价

可采用人员访谈、文档查阅、人工核查等方法。内容包括：

a）确认证书使用者是否是CA、RA、个人、企业、用户或计算机系统中的一种；

b）确认证书使用者是否能够验证证书、从查询服务器中检索证书和CRL、验证证书认证路径；

c）确认具有证书持有者身份的证书使用者是否能够产生签名、支持撤销或更新证书：

d）查看并确认证书使用者是否能获得从信任起点开始的完整的证书路径，验证路径的步骤是否符合5.5.2的要求；

e）确认证书使用者是否支持5.6中要求的相关密码算法。

### 7.3 数据格式测试评价方法

#### 7.3.1 数字证书格式测试评价

可采用人员访谈、文档查阅、人工核查等方法。内容包括：

a）查看并确认RA发起的注册请求事务消息内容是否符合6.2.2.1的要求；

b）查看并确认新实体发起的自我注册请求事务消息内容是否符合6.2.2.2的要求；

c）查看并确认已知实体发起的自我注册请求事务消息内容是否符合6.2.2.3的要求；

d）查看并确认加密证书申请事务消息内容是否符合6.2.2.4的要求；

e）查看并确认组合证书申请事务消息内容是否符合6.2.2.1的要求；

f）查看并确认证书更新事务消息内容是否符合6.2.3的要求；

g）查看并确认证书撤销事务消息内容是否符合6.2.4的要求；

h）查看并确认从资料库请求证书事务消息内容是否符合6.2.5.1的要求；

---

i）查看并确认从资料库请求CRL事务消息内容是否符合6.2.5.2的要求。

___