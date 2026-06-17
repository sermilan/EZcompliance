---
title: "新加坡PDPC匿名化基础指南-Guide to Basic Anonymisation 31 March 2022"
source: "个人隐私安全法律法规/报告&白皮书/新加坡PDPC匿名化基础指南-Guide to Basic Anonymisation 31 March 2022.pdf"
type: "pdf"
processed: "2026-04-22T23:09:23.593323"
---

<div style="text-align: center;"><img src="imgs/img_in_image_box_0_16_1190_997.jpg" alt="Image" width="99%" /></div>


## GUIDE TO BASIC ANONYMSATION

<div style="text-align: center;"><img src="imgs/img_in_image_box_259_1488_355_1583.jpg" alt="Image" width="8%" /></div>


SG):DIGITAL pdpc PERSONAL DATA PROTECTION COMMISSION SINGAPORE

---



---

## CONTENTS

## ……

INTRODUCTION ..... 4  
ANONYMISATION VERSUS DE-IDENTIFICATION ..... 6  
An Example of De-Identification ..... 8  
INTRODUCTION TO BASIC DATA ANONYMISATION CONCEPTS ..... 9  
THE ANONYMISATION PROCESS ..... 13  
Step 1: Know Your Data ..... 18  
Step 2: De-identify Your Data ..... 20  
Step 3: Apply Anonymisation Techniques ..... 22  
Step 4: Compute Your Risk ..... 24  
Step 5: Manage Your Re-identification and Disclosure Risks ..... 25  
ANNEX A: BASIC DATA ANONYMISATION TECHNIQUES ..... 34  
ANNEX B: COMMON DATA ATTRIBUTES AND SUGGESTED ANONYMISATION TECHNIQUES ..... 44  
ANNEX C: k-ANONYMITY ..... 49  
ANNEX D: ASSESSING THE RISK OF RE-IDENTIFICATION ..... 52  
ANNEX E: ANONYMISATION TOOLS ..... 56  
ACKNOWLEDGEMENTS ..... 57

---

## INTRODUCTION

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_194_223_286.jpg" alt="Image" width="9%" /></div>


## INTRODUCTION

This guide is meant to provide an introduction and practical guidance to organisations that are new to anonymisation on how to appropriately perform basic anonymisation and de-identification of structured $ ^{1} $, textual $ ^{2} $, non-complex datasets $ ^{3} $. It presents the anonymisation workflow in the context of four common use cases.

This guide is not exhaustive in dealing with all the issues relating to anonymisation, de-identification and re-identification of datasets. Organisations are advised to consider hiring anonymisation experts, statisticians or independent risk assessors to perform the appropriate anonymisation techniques or assessment of re-identification risks, where anonymisation issues are complex (e.g. large datasets containing a wide range of longitudinal or sensitive personal data).

Implementation of the recommendations in this guide does not imply compliance with the Personal Data Protection Act (PDPA).

Different jurisdictions view anonymisation differently and hence, the recommendations provided in this guide may not apply to data protection laws in other countries.

This guide should be read together with the Personal Data Protection Commission's (PDPC) Advisory Guidelines on the Personal Data Protection Act for Selected Topics.

---

## …

## ANONYMSATION VERSUS DE-IDENTIFICATION

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_126_214_214_302.jpg" alt="Image" width="7%" /></div>


## ANONYMSATION VERSUS DE-IDENTIFICATION

Anonymisation refers to the conversion of personal data into data that cannot be used to identify any individual. PDPC views anonymisation as a risk-based process, which includes applying both anonymisation techniques and safeguards to prevent re-identification.

De-identification $ ^{4} $ refers to the removal of identifiers (e.g. name, address, National Registration Identity Card (NRIC) number) that directly identify an individual. De-identification is sometimes mistakenly equated to anonymisation, however it is only the first step of anonymisation. A de-identified dataset may easily be re-identified when combined with data that is publicly or easily accessible.

Re-identification refers to the identification of individuals from a dataset that was previously de-identified or anonymised.

Anonymised data is not considered personal data and thus, is not governed by the PDPA. For more information, please refer to the topic on anonymisation in the PDPC's  $ \underline{\text{Advisory Guidelines on the Personal Data Protection for Selected Topics.}} $

## AN EXAMPLE OF DE-IDENTIFICATION

Albert uses food ordering apps frequently. His favourite food ordering app — SuperHungry — decides to publish some information about its users for a hackathon.

## Albert's data record at SuperHungry:

Name

Albert Phua

Favourite eatery

Date of birth

01/01/1990

Katong Fried

Chicken



Favourite food

Gender

Male

3-Piece Chicken Set, 33 past orders

Company

ABC Pte Ltd

---

SuperHungry de-identifies the dataset by removing the names before publishing, thinking that this equates to anonymising the dataset.

Albert's de-identified record published by SuperHungry:

<div style="text-align: center;"><img src="imgs/img_in_image_box_277_432_908_637.jpg" alt="Image" width="52%" /></div>


However, Albert can be re-identified by combining his de-identified record with other records (e.g. personal information from his social media profile).

## Albert's social media profile:

<div style="text-align: center;"><img src="imgs/img_in_image_box_267_869_927_944.jpg" alt="Image" width="55%" /></div>


Any person with sufficient motivation can easily identify $ ^{5} $ the person as Albert from the de-identified data if there are other publicly or easily available information to enable such re-identification. If the dataset or combined dataset is sensitive, further anonymisation will be required.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_474_499_726_813.jpg" alt="Image" width="21%" /></div>


## INTRODUCTION TO BASIC DATA ANONYMISATION CONCEPTS

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_122_183_215_300.jpg" alt="Image" width="7%" /></div>


# INTRODUCTION TO BASIC DATA ANONYMSATION CONCEPTS

Data anonymisation requires a good understanding of the following elements, which should be taken into consideration when determining what constitutes suitable anonymisation techniques and appropriate anonymisation levels.

## A Purpose of anonymisation and utility

The purpose of anonymisation must be clear, because anonymisation should be done specifically for the purpose at hand. The process of anonymisation, regardless of techniques used, reduces the original information in the dataset by some extent. Hence, as the degree of anonymisation increases, utility (e.g. clarity and/or precision) of the dataset is generally reduced. Therefore, the organisation needs to decide on the degree of the trade-off between acceptable (or expected) utility and the risk of re-identification.

It should be noted that utility should not be assessed at the level of the entire dataset as it is typically different for different attributes. One extreme is that the accuracy of a specific data attribute is crucial and no generalisation or anonymisation technique should be applied (e.g. medical conditions and drugs administered to individuals may be crucial data when analysing the hospital admission trends). The other extreme is that the data attribute is of no use for the intended purpose and may be dropped entirely without affecting the utility of the data to the recipient (e.g. date of birth of individuals may not be important when analysing the purchase transaction trends).

Another important consideration in determining the trade-off between utility and anonymisation is whether it poses an additional risk if the recipient knows which anonymisation techniques and what degree of granularity have been applied; on one hand, knowing this information may help the analyst understand the results and interpret them better, but on the other hand it may contain hints, which could lead to a higher risk of re-identification.

## B Reversibility

Typically, the process of data anonymisation would be “irreversible” and the recipient of the anonymised dataset would not be able to recreate the original data. However, there may be cases where the organisation applying the anonymisation retains the ability to recreate the original dataset from the anonymised data; in such cases, the anonymisation process is “reversible”.

---

## C Characteristics of anonymisation techniques

The different characteristics of the various anonymisation techniques mean that certain techniques may be more suitable for a particular situation or data type than others. For instance, certain techniques (e.g. character masking) may be more suitable for use on direct identifiers and others (e.g. aggregation) for indirect identifiers. Another characteristic to consider is whether the attribute value is a continuous value (e.g. height = 1.61m) or discrete value (e.g. "yes" or "no"), because techniques such as data perturbation work much better for continuous values.

The various anonymisation techniques also modify data in significantly different ways. Some modify only part of an attribute (e.g. character masking); some replace the value of an attribute across multiple records (e.g. aggregation); some replace the value of an attribute with an unrelated but unique value (e.g. pseudonymisation); and some remove the attribute entirely (e.g. attribute suppression).

Some anonymisation techniques can be used in combination (e.g. suppressing or removing (outlier) records after generalisation is performed).

## D Inferred information

It may be possible for certain information to be inferred from anonymised data. For example, masking may hide personal data, but it does not hide the length of the original value in terms of the number of characters.

Organisations may also wish to consider the order in which the anonymised data is presented. For example, if the recipient knows that the data records were collected in serial order (e.g. registration of visitors as they come), it may be prudent (as long as it does not affect utility) to reshuffle the entire dataset to avoid inference based on order of the data records.

Inference is not limited to a single attribute, but may also apply across attributes even if anonymisation techniques had been applied to all. The anonymisation process must, therefore, take note of every possibility that inference may occur, both before deciding on the actual techniques and after applying the techniques.

## Expertise with the subject matter

Anonymisation techniques basically reduce the identifiability of one or more individuals from the original dataset to a level acceptable by the organisation’s risk portfolio.

An identifiability and re-identifiability $ ^{6} $ assessment should be performed before and after anonymisation techniques are applied. This requires a good understanding of the subject matter which the data pertains to. For example, if the dataset is healthcare data, the

---

organisation would likely require someone with sufficient healthcare knowledge to assess a record's uniqueness (i.e. to what degree it is identifiable or re-identifiable).

The assessment before the anonymisation process ensures that the structure and information within an attribute is clearly identified and understood, and the risk of explicit and implicit inference from such data is assessed. For example, an attribute containing the year of birth implicitly provides age, as does an NRIC number to some extent. The assessment after the anonymisation process will determine the residual risk of re-identification from the anonymised data.

Another instance is when data attributes are swapped between records and it takes a subject-matter expert to recognise if the anonymised records make sense.

The right choice of anonymisation techniques, therefore, depends on awareness of the explicit and implicit information contained in the dataset and the amount or type of information intended to be anonymised.

## F Competency in anonymisation process and techniques

Organisations that wish to share anonymised datasets should ensure that the anonymisation process is undertaken by employees who have undergone training and are familiar with anonymisation techniques and principles. If the necessary expertise is not found within the organisation, external help should be engaged.

## G The recipient

Factors such as the recipients’ expertise in the subject matter and controls implemented to limit the quantity of recipients and to prevent the data from being shared with unauthorised parties play an important role in the choice of anonymisation techniques. In particular, the expected use of the anonymised data by the recipient may impose limitations on the applied techniques because the utility of the data may be lost beyond acceptable limits. Extra caution needs to be taken when making public releases of data and organisations will require a much stronger form of anonymisation compared to the data shared under a contractual arrangement.

## H Tools

Software tools can be very useful to aid in executing anonymisation techniques. Refer to Annex E for some anonymisation tools that are available in the market.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_413_542_773_875.jpg" alt="Image" width="30%" /></div>


## THE ANONYMSATION PROCESS

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_185_251_319.jpg" alt="Image" width="12%" /></div>


## THE ANONYMISATION PROCESS

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_340_1085_718.jpg" alt="Image" width="81%" /></div>


You can use these five steps to anonymise your datasets where appropriate, depending on your use case. In this guide, we explain these steps using five common data use cases by organisations.

In all data use cases, you should ensure:

<div style="text-align: center;"><img src="imgs/img_in_image_box_230_941_345_1076.jpg" alt="Image" width="9%" /></div>


Data minimisation, such that only necessary data attributes and an extract (where possible) of your dataset is shared to third parties;

Any identifying information of the dataset that you are anonymising should not be publicly available (e.g. if you are anonymising information on a membership database, the profiles of your membership base should not be publicly available); and

<div style="text-align: center;"><img src="imgs/img_in_image_box_966_1163_1079_1284.jpg" alt="Image" width="9%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_230_1388_344_1521.jpg" alt="Image" width="9%" /></div>


---

## USE CASES: HOW YOU CAN USE ANONYMISED OR DE-IDENTIFIED DATA

Here are some ways that anonymised or de-identified data can be used in your organisation.

<div style="text-align: center;"><img src="imgs/img_in_image_box_141_342_1050_507.jpg" alt="Image" width="76%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td colspan="2">Internal data sharing (de-identified data) (e.g. De-identified customer data shared between sales and marketing departments for analysis and in-house development of targeted marketing campaigns).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td colspan="2">Data is only de-identified to support record-level data sharing and use within the organisation, which may require most details in the data to be left untouched. The de-identified data is still personal data as it is likely to be easily re-identifiable. However, it is still good practice to de-identify the data as it provides an additional layer of protection.</td></tr><tr><td colspan="2">Are additional controls needed to prevent re-identification?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td colspan="2">Is the end result considered anonymised data?</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*Applicable</td><td colspan="2">1 2 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td colspan="2">Internal data sharing (anonymised data) (e.g. Anonymised data on the demographics of high value consumers and their respective spending patterns shared with loyalty teams to develop differentiated customer value propositions).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td colspan="2">Organisations could consider anonymised data instead of de-identified data for internal sharing under the following cases where:• Internal data sharing does not require detailed de-identified personal data (e.g. for trend analysis);• Data involved is more sensitive in nature (e.g. financial information); or• Larger datasets shared with more than one department.In such cases, organisations may apply the anonymisation process suggested for external data sharing to their internal data sharing use case to reduce the risk of re-identification and disclosure.</td></tr><tr><td colspan="2">Are additional controls needed to prevent re-identification?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td colspan="2">Is the end result considered anonymised data?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*Applicable steps</td><td colspan="2">1 2 3 4 5</td></tr></table>

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_139_259_1054_434.jpg" alt="Image" width="76%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td style='text-align: center; word-wrap: break-word;'>External data sharing(e.g. Anonymised customer data shared between sales department and external business partner for analysis of customer profiles and development of co-branded products).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Record-level data shared with an authorised external party for business collaboration purposes. Anonymisation techniques are used to convert personal data to non-identifying data.</td></tr><tr><td colspan="2">Are additional controls needed to prevent re-identification?</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Is the end result considered anonymised data?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*Applicable steps</td><td style='text-align: center; word-wrap: break-word;'>1 2 3 4 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td style='text-align: center; word-wrap: break-word;'>Long-term data retention for data analysis(e.g. Historical analysis of customer trends).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Anonymisation techniques are used to convert personal data to non-identifying data, and allow the data to be kept at record-level beyond the retention period for long-term data analysis.</td></tr><tr><td colspan="2">Are additional controls needed to prevent re-identification?</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Is the end result considered anonymised data?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*Applicable steps</td><td style='text-align: center; word-wrap: break-word;'>1 2 3 4 5</td></tr></table>

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_140_260_1051_432.jpg" alt="Image" width="76%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td colspan="2">Synthetic data $ ^{7} $ for application development and testing purposes, where replication of statistical characteristics of the original data is not required (e.g. Used for testing by outsourced vendor engaged to develop and test payroll application).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td colspan="2">Record-level synthetic data can be created from the original data by heavily anonymising all data attributes using the anonymisation techniques in this guide, such that all data attributes are modified very significantly and all records created do not match any individual&#x27;s record in the original data. In this case, the application of anonymisation techniques would not retain the statistical characteristics of the original data and thus is not suitable for sophisticated purposes such as AI model training or data analytics.</td></tr><tr><td colspan="2">Are additional controls needed to prevent re-identification?</td><td style='text-align: center; word-wrap: break-word;'>No $ ^{8} $</td></tr><tr><td colspan="2">Is the end result considered anonymised data?</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*Applicable steps</td><td colspan="2">1 2 3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Note: In synthe. randomly genera combination of an</td><td colspan="2">identifiers used should not relate to an actual person, i.e. a .d name should not be the same as the NRIC and name</td></tr></table>

Note: In synthetic data, the "fake" direct identifiers used should not relate to an actual person, i.e. a randomly generated NRIC with a randomly generated name should not be the same as the NRIC and name combination of an actual person.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_155_265_286.jpg" alt="Image" width="9%" /></div>


## KNOW YOUR DATA

Applicable to:

Long-term data retention

Synthetic data

A personal data record is made up of data attributes that have varying degrees of identifiability and sensitivity to an individual.

Anonymisation typically involves removal of direct identifiers and modification of indirect identifiers. Target attributes are usually left unchanged, except where the purpose is to create synthetic data. The table and examples below illustrate how a data attribute is typically classified within a data record.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Direct identifiers</td><td style='text-align: center; word-wrap: break-word;'>Indirect identifiers</td><td style='text-align: center; word-wrap: break-word;'>Target attributes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Classification of data attributes in a dataset</td><td style='text-align: center; word-wrap: break-word;'>These are data attributes that are unique to an individual and can be used as key data attributes to re-identify an individual.</td><td style='text-align: center; word-wrap: break-word;'>These are data attributes that are not unique to an individual but may re-identify an individual when combined with other information (e.g. a combination of age, gender and postal code).</td><td style='text-align: center; word-wrap: break-word;'>These are data attributes that contain the main utility of the dataset. In the context of assessing adequacy of anonymisation, this data attribute may be sensitive in nature, and may result in a high potential for adverse effect to an individual when disclosed.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Accessibility of data</td><td style='text-align: center; word-wrap: break-word;'>These data attributes are usually public or easily accessible.</td><td style='text-align: center; word-wrap: break-word;'>These data attributes may be public or easily accessible.</td><td style='text-align: center; word-wrap: break-word;'>These data attributes are usually not public or easily accessible. They cannot be used for re-identification as they are typically proprietary.</td></tr></table>

---

## Common

## examples in a dataset

• Name

• Email address

• Mobile phone number

☑ Age

• NRIC number

• Gender

Passport number

Race



Account number

Birth certificate number

• Date of birth

• Work Permit number

Address

Foreign Identification Number (FIN)

• Social media username

• Postal code

Job title

• Company name

• Marital status

Height

• Weight

• Internet Protocol (IP) address

Vehicle license plate number

• In-vehicle Unit (IU) number

• Global Positioning System (GPS) location

• Transactions (e.g. purchases)



• Insurance policy

Salary

• Credit rating

• Medical diagnosis

• Vaccination status

## EXAMPLE 1: CLASSIFICATION OF DATA ATTRIBUTES IN AN EMPLOYEE DATA RECORD


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Staff ID</td><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Department</td><td style='text-align: center; word-wrap: break-word;'>Gender</td><td style='text-align: center; word-wrap: break-word;'>Date of birth</td><td style='text-align: center; word-wrap: break-word;'>Start date of service</td><td style='text-align: center; word-wrap: break-word;'>Employment type</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>39192</td><td style='text-align: center; word-wrap: break-word;'>Sandy Thomas</td><td style='text-align: center; word-wrap: break-word;'>Research &amp; Development</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>08/01/1971</td><td style='text-align: center; word-wrap: break-word;'>02/03/1997</td><td style='text-align: center; word-wrap: break-word;'>Part-time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>37030</td><td style='text-align: center; word-wrap: break-word;'>Paula Swenson</td><td style='text-align: center; word-wrap: break-word;'>Engineering</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>15/05/1976</td><td style='text-align: center; word-wrap: break-word;'>08/03/2015</td><td style='text-align: center; word-wrap: break-word;'>Full-time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22722</td><td style='text-align: center; word-wrap: break-word;'>Bosco Wood</td><td style='text-align: center; word-wrap: break-word;'>Engineering</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>31/12/1973</td><td style='text-align: center; word-wrap: break-word;'>30/07/1991</td><td style='text-align: center; word-wrap: break-word;'>Full-time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>28760</td><td style='text-align: center; word-wrap: break-word;'>Stef Stone</td><td style='text-align: center; word-wrap: break-word;'>Engineering</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>24/12/1970</td><td style='text-align: center; word-wrap: break-word;'>18/03/2010</td><td style='text-align: center; word-wrap: break-word;'>Part-time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13902</td><td style='text-align: center; word-wrap: break-word;'>Jake Norma</td><td style='text-align: center; word-wrap: break-word;'>Human Resource</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>15/07/1973</td><td style='text-align: center; word-wrap: break-word;'>28/05/2012</td><td style='text-align: center; word-wrap: break-word;'>Part-time</td></tr></table>

Indirect identifiers

Direct identifiers

Target variables

## EXAMPLE 2: CLASSIFICATION OF DATA ATTRIBUTES IN A CUSTOMER DATA RECORD


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Customer ID</td><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Gender</td><td style='text-align: center; word-wrap: break-word;'>Date of birth</td><td style='text-align: center; word-wrap: break-word;'>Postal code</td><td style='text-align: center; word-wrap: break-word;'>Occupation</td><td style='text-align: center; word-wrap: break-word;'>Income</td><td style='text-align: center; word-wrap: break-word;'>Education status</td><td style='text-align: center; word-wrap: break-word;'>Marital status</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>56833</td><td style='text-align: center; word-wrap: break-word;'>Jenny Jefferson</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>05/08/1975</td><td style='text-align: center; word-wrap: break-word;'>570150</td><td style='text-align: center; word-wrap: break-word;'>Data scientist</td><td style='text-align: center; word-wrap: break-word;'>$13,000</td><td style='text-align: center; word-wrap: break-word;'>Masters</td><td style='text-align: center; word-wrap: break-word;'>Widowed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>50271</td><td style='text-align: center; word-wrap: break-word;'>Peter G</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>14/12/1973</td><td style='text-align: center; word-wrap: break-word;'>787589</td><td style='text-align: center; word-wrap: break-word;'>University lecturer</td><td style='text-align: center; word-wrap: break-word;'>$12,000</td><td style='text-align: center; word-wrap: break-word;'>Doctorate</td><td style='text-align: center; word-wrap: break-word;'>Married</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>53041</td><td style='text-align: center; word-wrap: break-word;'>Tim Lake</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>02/03/1985</td><td style='text-align: center; word-wrap: break-word;'>408600</td><td style='text-align: center; word-wrap: break-word;'>Researcher</td><td style='text-align: center; word-wrap: break-word;'>$7,000</td><td style='text-align: center; word-wrap: break-word;'>Doctorate</td><td style='text-align: center; word-wrap: break-word;'>Divorced</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>17290</td><td style='text-align: center; word-wrap: break-word;'>Remy Bay</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>27/03/1968</td><td style='text-align: center; word-wrap: break-word;'>570150</td><td style='text-align: center; word-wrap: break-word;'>Database administrator</td><td style='text-align: center; word-wrap: break-word;'>$8,000</td><td style='text-align: center; word-wrap: break-word;'>Bachelor</td><td style='text-align: center; word-wrap: break-word;'>Married</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>52388</td><td style='text-align: center; word-wrap: break-word;'>Walter Paul</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>25/06/1967</td><td style='text-align: center; word-wrap: break-word;'>199588</td><td style='text-align: center; word-wrap: break-word;'>Architect</td><td style='text-align: center; word-wrap: break-word;'>$10,000</td><td style='text-align: center; word-wrap: break-word;'>Masters</td><td style='text-align: center; word-wrap: break-word;'>Single</td></tr></table>

Direct identifiers

Indirect identifiers

---

Any data attribute that is not required in the resultant dataset should be removed as part of data minimisation. A simple flowchart is provided below to assist you in classifying your data attribute appropriately.

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_368_1075_1138.jpg" alt="Image" width="80%" /></div>


Applicable to:

This step is always performed as part of the anonymisation process.

First, remove all direct identifiers. In the following example, all names are removed. Where the dataset includes other direct identifiers such as NRIC number and email address, these should also be removed.

Name

Alex

Age

Bosco

25

54

Favourite show

42

The Big Bang Theory

Friends

Grey's Anatomy

---

Optionally, assign a pseudonym to each record if there is a need to link the record back to a unique individual or to the original record for use cases such as:

a. Data merger;

b. Analysis of multiple records relating to unique individuals; or

c. Generation of synthetic datasets where direct identifier values are required for the development and testing of applications. For this use case, replace all necessary direct identifiers with pseudonyms.

The pseudonyms should be unique for each unique direct identifier (as illustrated below). Assignment of pseudonyms should also be robust (i.e. not be reversible by unauthorised parties through guessing or computing the original direct identifier values from the pseudonyms).

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_676_1014_833.jpg" alt="Image" width="71%" /></div>


Favourite show

The Big Bang Theory

Friends

If you want to retain the ability to link the de-identified data record back to the original record at a subsequent point in time, you will need to keep the mapping between the direct identifiers and the pseudonyms. The identity mapping table (illustrated below) should be kept securely as it permits re-identification.

Name

Alex

Token

Bosco

1234

Charlene

5678

5432

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_135_1076_480.jpg" alt="Image" width="80%" /></div>


Applicable to:

In this step, you will apply anonymisation techniques to the indirect identifiers so that they cannot be easily combined with other datasets that may contain additional information to re-identify individuals. For the synthetic data use case, anonymisation techniques should also be applied to the target attributes.

Do note that application of these techniques will modify the data values and may affect utility of the anonymised data for some use cases (e.g. data analytics). The anonymisation techniques recommended below take into consideration potential utility required for record-level data in each use case. Organisations may use other anonymisation techniques beyond what is recommended, if relevant to their use case.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td style='text-align: center; word-wrap: break-word;'>Suggested anonymisation techniques for record-level data</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data) or External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Record suppression: The removal of a record (i.e. row of data, especially where such data may contain unique data values that cannot be anonymised further). Attribute suppression: The removal of a data attribute (i.e. column of data, especially where such data is not needed in the dataset and may contain unique data values that cannot be anonymised further). Character masking: The replacement of some characters of the data value with a consistent symbol (e.g. * or x). For example, masking a postal code would involve changing it from &quot;235546&quot; to &quot;23xxxx&quot;. Generalisation: The reduction in granularity of the data (e.g. by converting a person&#x27;s age into an age range). For example, generalising the age of a person from &quot;26 years old&quot; to &quot;25-29 years old&quot;.</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td><td style='text-align: center; word-wrap: break-word;'>Record or attribute suppressionCharacter maskingGeneralisationData perturbation: The modification of the values in the data by adding &quot;noise&quot; to the original data (e.g. +/- random values to the data). The degree of perturbation should be proportionate to the range of values of the attribute. For example, data perturbation would involve modifying salary data of an individual from &quot;$256,654&quot; to &quot;$260,000&quot; by rounding the data up to the nearest $10,000. Alternatively, the individual&#x27;s salary can be modified to &quot;$250,554&quot; by subtracting a random number within $10,000 from its original value.Note: Data aggregation may also be performed for this use case when record-level data is not required (refer to Annex A for an example).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Synthetic data</td><td style='text-align: center; word-wrap: break-word;'>Apply heavy anonymisation to the original data to create synthetic data such that all data attributes (including target attributes) are modified significantly. The resulting dataset and individual records created using this methodology will not have any resemblance to any individual&#x27;s record and does not retain the characteristics of the original dataset.Because of the resulting dataset&#x27;s non-resemblance to the original, it is suitable for application development/testing but not AI model training.Data perturbationSwapping: The rearrangement of data in the dataset randomly such that the individual attribute values are still represented in the dataset, but generally do not correspond to the original records.</td></tr></table>

Refer to Annex A for more information on the various anonymisation techniques and how to apply them. Refer to Annex B for suggested anonymisation techniques to apply on a list of common data attributes.

Next Step: After applying the appropriate anonymisation techniques, proceed to step 4 to assess the risk level. Repeat steps 3 and 4 until you achieve a k-anonymity value of 3, 5 or more.

Note: You may also consider removing outlier records or attributes (using record or attribute suppression) that are "resistant" to other anonymisation techniques that have been applied, especially if there is a relatively low count of such outliers and the removal would not significantly impact the quality of the data for your use case.

---

## COMPUTE YOUR RISK

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_141_1076_486.jpg" alt="Image" width="81%" /></div>


Applicable to:

k-anonymity $ ^{9} $ is an easy method $ ^{10,11} $ to compute the re-identification risk level of a dataset. It basically refers to the smallest number of identical records that can be grouped together in a dataset. The smallest group is usually taken to represent the worst-case scenario in assessing the overall re-identification risk of the dataset. A k-anonymity value of 1 means that the record is unique. Generally, only indirect identifiers are considered for k-anonymity computation. $ ^{12} $

A higher k-anonymity value means there is a lower risk of re-identification while a lower k-anonymity value implies a higher risk. Generally the industry threshold for k-anonymity value is at 3 or 5. $ ^{13} $ Where possible, a higher k-anonymity threshold value should be set to minimise any re-identification risks.

Refer to Chapter 3 (Anonymisation) of PDPC's  $ \underline{\text{Advisory Guidelines on the Personal Data Protection Act for Selected Topics}} $ on the criteria for determining whether the data may be considered sufficiently anonymised.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Postal code</td><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Favourite show</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22xxxx</td><td style='text-align: center; word-wrap: break-word;'>21 to 25</td><td style='text-align: center; word-wrap: break-word;'>Emily in Paris</td><td rowspan="2">k=2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22xxxx</td><td style='text-align: center; word-wrap: break-word;'>21 to 25</td><td style='text-align: center; word-wrap: break-word;'>Emily in Paris</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41 to 45</td><td style='text-align: center; word-wrap: break-word;'>Brooklyn Nine-Nine</td><td rowspan="4">k=4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41 to 45</td><td style='text-align: center; word-wrap: break-word;'>Brooklyn Nine-Nine</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41 to 45</td><td style='text-align: center; word-wrap: break-word;'>Brooklyn Nine-Nine</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>41 to 45</td><td style='text-align: center; word-wrap: break-word;'>Brooklyn Nine-Nine</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56 to 60</td><td style='text-align: center; word-wrap: break-word;'>Attenborough&#x27;s Life in Colour</td><td rowspan="3">k=3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56 to 60</td><td style='text-align: center; word-wrap: break-word;'>Attenborough&#x27;s Life in Colour</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>58xxxx</td><td style='text-align: center; word-wrap: break-word;'>56 to 60</td><td style='text-align: center; word-wrap: break-word;'>Attenborough&#x27;s Life in Colour</td></tr></table>

Overall  $ k=2 $

The above diagram illustrates a dataset with three groups of identical records. The k value of each group ranges from 2 to 4. Overall, the dataset's k-anonymity value is 2, reflecting the lowest value (highest risk) within the entire dataset. $ ^{14} $

---

Next Step: If the k-anonymity value threshold is achieved, proceed to step 5. If the k-anonymity value is lower than set threshold, return to step 3 and repeat.

Note: Where possible, you should set a higher k-anonymity value (e.g. 5 or more) for external data sharing, while a lower value (e.g. 3) may be set for internal data sharing or long term data retention. However, if you are not able to anonymise your data further to achieve that, you should put in place more stringent safeguards to ensure that the anonymised data will not be disclosed to unauthorised parties and re-identification risks are mitigated. Alternatively, you may engage experts to provide alternative assessment methods to achieve equivalent re-identification risks.

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_660_267_792.jpg" alt="Image" width="9%" /></div>


MANAGE YOUR RE-IDENTIFICATION AND DISCLOSURE RISKS

Applicable to:

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_851_215_891.jpg" alt="Image" width="3%" /></div>


## Internal data sharing (de-identified data)

<div style="text-align: center;"><img src="imgs/img_in_image_box_578_852_617_890.jpg" alt="Image" width="3%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_266_930_308_962.jpg" alt="Image" width="3%" /></div>


Internal data sharing (anonymised data) or External data sharing

Long-term data retention

<div style="text-align: center;"><img src="imgs/img_in_image_box_692_931_729_965.jpg" alt="Image" width="3%" /></div>


Synthetic data

It is generally prudent to put in appropriate measures to safeguard your data against the risks of re-identification and disclosure. This is in view of future technological advances, as well as unknown datasets that could be used to match against your anonymised dataset and allow re-identification to be performed more easily than expected at the time of anonymisation.

---

As good practice, the details of the anonymisation process, parameters used and controls should also be clearly recorded for future reference. Such documentation facilitates review, maintenance, fine-tuning and audits. Note that such documentation should be kept securely as the release of the parameters may facilitate re-identification and disclosure of the anonymised data.

There are various types of re-identification and disclosure risks. The following explains some fundamental ones that you should assess when reviewing the sufficiency of protection measures that have been put in place.

## 1 Re-identification (Identity disclosure)

Determining, with a high level of confidence, the identity of an individual described by a specific record. This could arise from scenarios such as insufficient anonymisation, re-identification by linking or pseudonym reversal. For example, an anonymisation process which creates pseudonyms based on an easily guessable and reversible algorithm, such as replacing "1" with "a", "2" with "b" and so on.

## 2 Attribute disclosure

Determining, with a high level of confidence, that an attribute described in the dataset belongs to a specific individual even if the individual's record cannot be distinguished. Take, for example, a dataset containing anonymised client records of a particular aesthetic surgeon that reveals all his clients below the age of 30 have undergone a particular procedure. If it is known that a particular individual is 28 years old and is a client of this surgeon, we then know that this individual has undergone the particular procedure, even if the individual's record cannot be distinguished from others in the anonymised dataset.

## 3 Inference disclosure

Making an inference, with a high level of confidence, about an individual even if he or she is not in the dataset by statistical properties of the dataset. For example, if a dataset released by a medical researcher reveals that 70% of individuals above the age of 75 have a certain medical condition, this information could be inferred about an individual who is not in the dataset.

In general, most traditional anonymisation techniques aim to protect against re-identification and not necessarily other types of disclosure risks.

---

The following table explains when measures against re-identification and disclosure risks are recommended. A set of basic protection measures (technical, process and legal controls) for the use cases are outlined in the following paragraphs.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Use case</td><td style='text-align: center; word-wrap: break-word;'>Do you need to manage re-identification and disclosure risks for de-identified or anonymised datasets?</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (de-identified data)</td><td style='text-align: center; word-wrap: break-word;'>As only de-identification has been applied in order to retain high data utility, re-identification and disclosure risk for de-identified data is higher. Hence, protection is required for the de-identified dataset. The identity mapping tables, if any, should be secured. In the event of a data breach, application of de-identification techniques, how the de-identified dataset is protected and how the mapping table is secured would all be considered part of the protection mechanisms implemented.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data)</td><td style='text-align: center; word-wrap: break-word;'>To lower re-identification and disclosure risks, anonymisation should be applied to the data for internal sharing, where necessary, in the following cases. They are (a) where detailed personal data is not required, (b) where sensitive data may be shared or (c) where a large dataset is shared with more than one department. Basic protection is required for the anonymised dataset. The identity mapping tables, if any, should be secured and not be shared with the other internal departments.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Basic protection is required for the anonymised dataset. The identity mapping tables, if any, should be secured and not be shared externally.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td><td style='text-align: center; word-wrap: break-word;'>Basic protection is required for the anonymised dataset. All identity mapping tables are to be securely destroyed.</td></tr></table>

For the synthetic data use case, re-identification risks are assumed to be minimal when anonymisation is applied heavily to all indirect identifiers and target attributes such that the records do not resemble the original dataset. As such, no further protection of this dataset is required.

Technical and process controls: You should implement technical protection measures to manage the re-identification and disclosure risk of de-identified and anonymised data. Some good practices are suggested in the following table.

You should review these good practices to determine if they are sufficient to protect your de-identified/anonymised data based on the degree of anonymisation applied, sensitivity of the de-identified/anonymised data and the use case. You may refer to the PDPC's Guide to Data Protection Practices for ICT Systems for additional protection measures where relevant.

---

In the table, “Y” means you are recommended to adopt the corresponding technical control and “NA” means that particular technical control is not applicable to that use case.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Technical control</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (de-identified data)</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data)</td><td style='text-align: center; word-wrap: break-word;'>External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td></tr><tr><td rowspan="2">Access control and passwords</td><td style='text-align: center; word-wrap: break-word;'>Implement access control at the application level to restrict data access to a user level. Minimum level of password complexity (i.e. minimum 12 alphanumeric characters with a mix of uppercase, lowercase, numeric and special characters).</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Regularly review user accounts to ensure all the accounts are active and the rights assigned are necessary (e.g. remove user accounts when a user has left the organisation or update the user&#x27;s rights when he or she has changed his or her role within the organisation).</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Technical control</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (de-identified data)</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data)</td><td style='text-align: center; word-wrap: break-word;'>External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td></tr><tr><td rowspan="4">Security for storage devices/databases</td><td style='text-align: center; word-wrap: break-word;'>Protect computers by using password functions. Examples of these include keying in password during boot-up, requiring login to the operating system, locking the screen after a period of inactivity, etc.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Encrypt the dataset. Review the method of encryption (e.g. algorithm and key length) periodically to ensure that it is recognised by the industry as relevant and secure.</td><td style='text-align: center; word-wrap: break-word;'>Y (where the data involved is sensitive in nature or larger datasets is shared with more than one department but anonymisation is not applied to the dataset.)</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA (where the re-identification risk is assessed to be low (e.g. k-anonymity is 5 or more), encryption need not be applied to the anonymised dataset.)</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Encrypt the identity mapping tables. Identity mapping tables should be secured and not be shared in all use cases.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA (Identity mapping tables should be removed.)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Communicate the decryption key of the dataset separately to the target recipient of the shared/exported data.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Process control</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (de-identified data)</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data)</td><td style='text-align: center; word-wrap: break-word;'>External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Incident management</td><td style='text-align: center; word-wrap: break-word;'>Develop a data breach management plan to respond to data breaches and manage the loss of datasets more effectively. The plan should also include how to manage the loss of identity mapping tables or information that could allow reversing de-identified/anonymised data back to its original form, resulting in the lost data being re-identified. Refer below for more information on incident management.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr><tr><td rowspan="6">Internal governance controls</td><td style='text-align: center; word-wrap: break-word;'>Keep a central registry of all shared de-identified/anonymised data to ensure that the combined shared data will not result in re-identification of the de-identified/anonymised data.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Periodically conduct re-identification reviews of the de-identified/anonymised data.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ensure that the recipient (individual or department) and the purpose of using the de-identified/anonymised data have been approved by relevant authorities within the organisation.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prohibit the authorised recipient (individual or department) from sharing de-identified/anonymised data to any unauthorised parties or attempting to re-identify the data without approval from relevant authorities within the organisation.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Regularly purge de-identified/anonymised data within the organisation when its purpose has been fulfilled and there is no longer any need for the data.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Periodically conduct internal checks/audits to ensure compliance with processes.</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>Y</td></tr></table>

---

Incident Management: Organisations should identify the risks of data breaches $ ^{18} $ involving identity mapping table, de-identified data and anonymised data, and incorporate relevant scenarios into their incident management plans. The following considerations may be relevant for data breach reporting and internal investigations:

## Loss of de-identified data and identity mapping table

Breach of both de-identified data and identity management table will be akin to the breach of personal data. In such an event, the organisation must assess whether a data breach is notifiable and notify the affected individuals and/or the Commission, where it is assessed to be notifiable under the Data Breach Notification obligation.

## Loss of de-identified data only

If de-identified data has been breached externally, an assessment is necessary. The organisation must assess whether a data breach is notifiable as de-identified data has a higher risk of re-identification. However, the use of de-identification and other safeguards to protect the data and identity mapping table could be considered part of the protection mechanisms implemented by the organisation.

## Loss of anonymised data and identity mapping table

Organisations have to assess the risk of re-identification. Where it is determined to be high, organisations must then determine whether a data breach is notifiable and notify the affected individuals and/or the Commission, where it is assessed to be notifiable under the Data Breach Notification obligation.

## Loss of anonymised data only

Where the organisation has applied the anonymisation techniques properly, it need not report the breach as a notifiable breach. However, it should still proceed to investigate the incident to understand the cause to improve its internal safeguards against future data breach incidents.

## Loss of identity mapping only

If the datasets that the identity mapping table was used for are still protected, organisations need not report the breach as an identity mapping table on its own is not personal data. However, the organisation should immediately generate new pseudonyms for its datasets and a new identity mapping table. It should also proceed to investigate the incident to understand the cause to improve its internal safeguards against future data breach incidents.

---

Legal controls: Organisations should protect themselves by ensuring that third-party recipients of their anonymised data incorporate relevant protection to the shared anonymised data to minimise re-identification risks. The good practices in the following table are taken from the PDPC's Trusted Data Sharing Framework.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="4">Data sharing agreement</td><td style='text-align: center; word-wrap: break-word;'>Legal control</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (de-identified data)</td><td style='text-align: center; word-wrap: break-word;'>Internal data sharing (anonymised data)</td><td style='text-align: center; word-wrap: break-word;'>External data sharing</td><td style='text-align: center; word-wrap: break-word;'>Long-term data retention</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ensure the data is only used for permitted purposes (e.g. no disclosure to unauthorised parties) and liability is allocated for contract breaches.</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prohibit third-party recipients from attempting to re-identify anonymised datasets that have been shared.</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ensure third-party recipients comply with the relevant protection on the shared anonymised data as per organisation&#x27;s internal controls.</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>NA</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>NA</td></tr></table>

---

## 4 

## ANNEX

---

# ANNEX A: BASIC DATA ANONYMSATION TECHNIQUES


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Record Suppression</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Record suppression refers to the removal of an entire record in a dataset. In contrast to most other techniques, this technique affects multiple attributes at the same time.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Record suppression is used to remove outlier records which are unique or do not meet other criteria, such as k-anonymity, from the anonymised dataset. Outliers can lead to easy re-identification. It can be applied before or after other techniques (e.g. generalisation) have been applied.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>Delete the entire record. Note that the suppression should be permanent and not just a &quot;hide row&quot; function; similarly, &quot;redacting&quot; may not be sufficient if the underlying data remains accessible.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Other tips</td><td style='text-align: center; word-wrap: break-word;'>Refer to the example in the section on generalisation for illustration of how record suppression is used. Note that removal of records can impact the dataset (e.g. in terms of statistics such as average and median).</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Character Masking</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Character masking refers to changing the characters of a data value. This can be done by using a consistent symbol (e.g. &quot;*&quot; or &quot;x&quot;). Masking is typically applied only to some characters in the attribute.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Character masking is used when the data value is a string of characters and hiding part of it is sufficient to provide the extent of anonymity required.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>Depending on the nature of the attribute, replace the appropriate characters with a chosen symbol. Depending on the attribute type, you may decide to replace a fixed number of characters (e.g. for credit card numbers) or a variable number of characters (e.g. for email address).</td></tr><tr><td rowspan="2">Other tips</td><td style='text-align: center; word-wrap: break-word;'>Note that masking may need to take into account whether the length of the original data provides information about the original data. Subject matter knowledge is critical, especially for partial masking to ensure that the right characters are masked. Special consideration may also apply to checksums within the data; sometimes, a checksum may be used to recover (other parts of) the masked data. As for complete masking, the attribute could alternatively be suppressed unless the length of the data is of some relevance.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>The scenario of masking data in such a way that data subjects are meant to recognise their own data is a special one, and does not belong to the usual objectives of data anonymisation. One example of this is the publishing of lucky draw results, where the names and partially masked NRIC numbers of lucky draw winners are typically published for the individuals to recognise themselves as winners. Another example is information such as an individual&#x27;s credit card number being masked in an app or a statement addressed to the individual. Note that generally, anonymised data should not be recognisable even to the data subject themselves.</td></tr></table>

15. This refers to using the "hide row" function in your spreadsheet software.

---

## EXAMPLE

This example shows an online grocery store conducting a study of its delivery demand from historical data to improve operational efficiency. The company masked out the last 4 digits of the postal codes, leaving the first 2 digits, which correspond to the "sector code" within Singapore.

## Before anonymisation:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Postal code</td><td style='text-align: center; word-wrap: break-word;'>Favourite delivery time slot</td><td style='text-align: center; word-wrap: break-word;'>Average number of orders per month</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>100111</td><td style='text-align: center; word-wrap: break-word;'>8 pm to 9 pm</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>200222</td><td style='text-align: center; word-wrap: break-word;'>11 am to 12 noon</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>300333</td><td style='text-align: center; word-wrap: break-word;'>2 pm to 3pm</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>

## After partial masking of postal code:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Postal code</td><td style='text-align: center; word-wrap: break-word;'>Favourite delivery time slot</td><td style='text-align: center; word-wrap: break-word;'>Average number of orders per month</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10xxxx</td><td style='text-align: center; word-wrap: break-word;'>8 pm to 9 pm</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20xxxx</td><td style='text-align: center; word-wrap: break-word;'>11 am to 12 noon</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>30xxxx</td><td style='text-align: center; word-wrap: break-word;'>2 pm to 3pm</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Pseudonymisation</td></tr><tr><td rowspan="3">Description</td><td style='text-align: center; word-wrap: break-word;'>Pseudonymisation refers to the replacement of identifying data with made-up values. It is also referred to as coding. Pseudonyms can be irreversible when the original values are disposed of properly and the pseudonymisation is done in a non-repeatable fashion. They can also be reversible (by the owner of the original data) when the original values are securely kept, but can be retrieved and linked back to the pseudonym should the need arise $ ^{16} $.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Persistent pseudonyms allow linking by using the same pseudonym values to represent the same individual across different datasets. However, different pseudonyms may be used to represent the same individual in different datasets to prevent linking of the different datasets.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pseudonyms can also be randomly or deterministically generated.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Pseudonymisation is used when data values need to be uniquely distinguished and no character or any other implied information about the direct identifiers of the original attribute are kept.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>Replace the respective attribute values with made-up values. One way to do this is to pre-generate a list of made-up values and randomly select from this list to replace each of the original values. The made-up values should be unique and should have no relationship to the original values (such that one can derive the original values from the pseudonyms).</td></tr></table>

---

## Other tips

• When allocating pseudonyms, ensure not to re-use pseudonyms that have already been utilised in the same dataset, especially when they are randomly generated. Also, avoid using the exact same pseudonym generator over several attributes without a change (e.g. at least use a different random seed).

Persistent pseudonyms usually provide better utility by maintaining referential integrity across datasets.

For reversible pseudonyms, the identity mapping table cannot be shared with the recipient; it should be securely kept and can only be used by the organisation where it is necessary to re-identify the individual(s).

- Similarly, if encryption or a hash function is used to pseudonymise the data, the encryption key or hash algorithm and salt value for the hash must be securely protected from unauthorised access. This is because a leak of such information could result in a data breach by enabling the reversal of the encryption or using pre-computed tables to infer the data that was hashed (especially for data that follows pre-determined formats such as in NRICs).

The same applies for pseudo-random number generators, which require a seed. The security of any key used must be ensured like with any other type of encryption or reversible process $ ^{17} $. Organisations should also review the method of encryption (e.g. algorithm and key length) and hash function periodically to ensure that it is recognised by the industry as relevant and secure.

- In some cases, pseudonyms may need to follow the structure or data type of the original value (e.g. for pseudonyms to be usable in software applications); in such cases, special pseudonym generators may be needed to create synthetic datasets or in some cases, so-called "format preserving encryption" can be considered, which creates pseudonyms that have the same format as the original data.

## EXAMPLE

This example shows pseudonymisation being applied to the names of persons who obtained their driving licences and some information about them. In this example, the names were replaced with pseudonyms instead of the attribute being suppressed because the organisation wanted to be able to reverse the pseudonymisation if necessary.

## Before anonymisation:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Pre-assessment result</td><td style='text-align: center; word-wrap: break-word;'>Hours of lessons taken before passing</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Joe Phang</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Zack Lim</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Eu Cheng San</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Linnie Mok</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Jeslyn Tan</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chan Siew Lee</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

---

<div style="text-align: center;">After pseudonymising the "Person" attribute:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Pre-assessment result</td><td style='text-align: center; word-wrap: break-word;'>Hours of lessons taken before passing</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>416765</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>562396</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>964825</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>873892</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>239976</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>943145</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

For reversible pseudonymisation, the identity mapping table is securely kept in case there is a legitimate future need to re-identify individuals. Security controls (including administrative and technical ones) should also be used to protect the identity mapping table.

<div style="text-align: center;">Identity mapping table (Single coding):</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Pseudonym</td><td style='text-align: center; word-wrap: break-word;'>Person</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>416765</td><td style='text-align: center; word-wrap: break-word;'>Joe Phang</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>562396</td><td style='text-align: center; word-wrap: break-word;'>Zack Lim</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>964825</td><td style='text-align: center; word-wrap: break-word;'>Eu Cheng San</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>873892</td><td style='text-align: center; word-wrap: break-word;'>Linnie Mok</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>239976</td><td style='text-align: center; word-wrap: break-word;'>Jeslyn Tan</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>943145</td><td style='text-align: center; word-wrap: break-word;'>Chan Siew Lee</td></tr></table>

For added security regarding the identity mapping table, double coding can be used. Following from the previous example, this example shows the additional linking table, which is placed with a trusted third party. With double coding, the identity of the individuals can only be known when both the trusted third party (who has the linking table) and the organisation (which has the identity mapping table) put their data together.

<div style="text-align: center;">After anonymisation:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Pre-assessment result</td><td style='text-align: center; word-wrap: break-word;'>Hours of lessons taken before passing</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>373666</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>594824</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>26</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>839933</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>30</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>280074</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>29</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>746791</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>785282</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr></table>

---

Linking table (Securely kept by a trusted third party only and even the organisation will remove it eventually. The third party is not given any other information):


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Pseudonym</td><td style='text-align: center; word-wrap: break-word;'>Interim pseudonym</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>373666</td><td style='text-align: center; word-wrap: break-word;'>OQCPBL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>594824</td><td style='text-align: center; word-wrap: break-word;'>ALGKTY</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>839933</td><td style='text-align: center; word-wrap: break-word;'>CGFFNF</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>280074</td><td style='text-align: center; word-wrap: break-word;'>BZMHCP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>746791</td><td style='text-align: center; word-wrap: break-word;'>RTJYGR</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>785282</td><td style='text-align: center; word-wrap: break-word;'>RCNVJD</td></tr></table>

## Identity mapping table (Securely kept by the organisation)


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Interim pseudonym</td><td style='text-align: center; word-wrap: break-word;'>Person</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OQCPBL</td><td style='text-align: center; word-wrap: break-word;'>Joe Phang</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ALGKTY</td><td style='text-align: center; word-wrap: break-word;'>Zack Lim</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CGFFNF</td><td style='text-align: center; word-wrap: break-word;'>Eu Cheng San</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BZMHCP</td><td style='text-align: center; word-wrap: break-word;'>Linnie Mok</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RTJYGR</td><td style='text-align: center; word-wrap: break-word;'>Jeslyn Tan</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RCNVJD</td><td style='text-align: center; word-wrap: break-word;'>Chan Siew Lee</td></tr></table>

Note: In both the linking table and identity mapping table, it is good practice to scramble the order of the records rather than leave it in the same order as the dataset. In this example, the records in both tables are left in the original order for easier visualisation.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Generalisation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Generalisation is a deliberate reduction in the precision of data. Examples include converting a person&#x27;s age into an age range or a precise location into a less precise location. This technique is also referred to as recoding.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Generalisation is used for values that can be generalised and still be useful for the intended purpose.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>Design appropriate data categories and rules for translating data. Consider suppressing any records that still stand out after the translation (i.e. generalisation).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Other tips</td><td style='text-align: center; word-wrap: break-word;'>• Choose an appropriate data range. A data range that is too large may mean significant loss in data utility, while a data range that is too small may mean that the data is hardly modified and therefore, still easy to re-identify. If k-anonymity is used, the k value chosen will affect the data range as well. Note that the first and the last range may be a larger range to accommodate the typically lower number of records at these ends; this is often referred to as top/bottom coding.</td></tr></table>

---

## EXAMPLE

In this example, the dataset contains the person's name (which has already been pseudonymised), their age in years and residential address.

<div style="text-align: center;">Before anonymisation:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Serial number</td><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Address</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>357703</td><td style='text-align: center; word-wrap: break-word;'>24</td><td style='text-align: center; word-wrap: break-word;'>700 Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>233121</td><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>800 Ang Mo Kio Avenue 12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>938637</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>900 Jurong East Street 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>591493</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>750 Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>202626</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>5 Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>888948</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>1 Stonehenge Road</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>175878</td><td style='text-align: center; word-wrap: break-word;'>28</td><td style='text-align: center; word-wrap: break-word;'>10 Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>312304</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>50 Jurong East Street 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>214025</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>720 Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>271714</td><td style='text-align: center; word-wrap: break-word;'>37</td><td style='text-align: center; word-wrap: break-word;'>830 Ang Mo Kio Avenue 12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>341338</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>15 Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>529057</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>18 Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>390438</td><td style='text-align: center; word-wrap: break-word;'>39</td><td style='text-align: center; word-wrap: break-word;'>840 Ang Mo Kio Avenue 12</td></tr></table>

For the "Age" attribute, the approach taken is to generalise into the following age ranges.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>&lt; 20</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>51-60</td><td style='text-align: center; word-wrap: break-word;'>&gt; 60</td></tr></table>

For the "Address", one possible approach is to remove the block/house number and retain only the road name.

<div style="text-align: center;">After generalisation of the "Age" and "Address" attributes:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Serial number</td><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Address</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>357703</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>233121</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>Ang Mo Kio Avenue 12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>938637</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>Jurong East Street 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>591493</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>202626</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>888948</td><td style='text-align: center; word-wrap: break-word;'>&gt; 60</td><td style='text-align: center; word-wrap: break-word;'>Stonehenge Road</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>175878</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>312304</td><td style='text-align: center; word-wrap: break-word;'>41-50</td><td style='text-align: center; word-wrap: break-word;'>Jurong East Street 70</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>214025</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Toa Payoh Lorong 5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>271714</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>Ang Mo Kio Avenue 12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>341338</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>529057</td><td style='text-align: center; word-wrap: break-word;'>21-30</td><td style='text-align: center; word-wrap: break-word;'>Tampines Street 90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>390438</td><td style='text-align: center; word-wrap: break-word;'>31-40</td><td style='text-align: center; word-wrap: break-word;'>Ang Mo Kio Avenue 12</td></tr></table>

---

As an example, assume there is, in fact, only one residential unit on Stonehenge Road. The exact address can be derived even though the data has gone through generalisation. This could be considered "too unique".

Hence, as the next step of generalisation, record 6 could be removed (i.e. using the record suppression technique) as the address is still “too unique” after removing the unit number. Alternatively, all the addresses could be generalised to a greater extent (e.g. town or district) such that suppression is not needed. However, this may affect the utility of the data much more than suppressing a few records from the dataset.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Swapping</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>The purpose of swapping is to rearrange data in the dataset such that the values of individual attributes are still represented in the dataset but generally do not correspond to the original records. This technique is also referred to as shuffling and permutation.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Swapping is used when subsequent analysis only needs to look at aggregated data or analysis is at the intra-attribute level; in other words, there is no need for analysis of relationships between attributes at the record-level.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>First, identify which attributes to swap. Then, for each value in the attribute, swap or reassign the value to other records in the dataset.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Other tips</td><td style='text-align: center; word-wrap: break-word;'>Assess and decide which attributes (columns) need to be swapped. Depending on the situation, organisations may decide that, for instance, only attributes (columns) containing values that are relatively identifiable need to be swapped.</td></tr></table>

## EXAMPLE

In this example, the dataset contains information about customer records for a business organisation.

## Before anonymisation:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Job title</td><td style='text-align: center; word-wrap: break-word;'>Date of birth</td><td style='text-align: center; word-wrap: break-word;'>Membership type</td><td style='text-align: center; word-wrap: break-word;'>Average visits per month</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>University lecturer</td><td style='text-align: center; word-wrap: break-word;'>3 Jan 1970</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>Salesman</td><td style='text-align: center; word-wrap: break-word;'>5 Feb 1972</td><td style='text-align: center; word-wrap: break-word;'>Platinum</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>Lawyer</td><td style='text-align: center; word-wrap: break-word;'>7 Mar 1985</td><td style='text-align: center; word-wrap: break-word;'>Gold</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>IT professional</td><td style='text-align: center; word-wrap: break-word;'>10 Apr 1990</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>Nurse</td><td style='text-align: center; word-wrap: break-word;'>13 May 1995</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr></table>

## After anonymisation:

In this example, all values for all attributes have been swapped.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Job title</td><td style='text-align: center; word-wrap: break-word;'>Date of birth</td><td style='text-align: center; word-wrap: break-word;'>Membership type</td><td style='text-align: center; word-wrap: break-word;'>Average visits per month</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>Lawyer</td><td style='text-align: center; word-wrap: break-word;'>10 Apr 1990</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>Nurse</td><td style='text-align: center; word-wrap: break-word;'>7 Mar 1985</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>Salesman</td><td style='text-align: center; word-wrap: break-word;'>13 May 1995</td><td style='text-align: center; word-wrap: break-word;'>Platinum</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>IT professional</td><td style='text-align: center; word-wrap: break-word;'>3 Jan 1970</td><td style='text-align: center; word-wrap: break-word;'>Silver</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>University lecturer</td><td style='text-align: center; word-wrap: break-word;'>5 Feb 1972</td><td style='text-align: center; word-wrap: break-word;'>Gold</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

Note: On the other hand, if the purpose of the anonymised dataset is to study the relationships between job profile and consumption patterns, other methods of anonymisation may be more suitable (e.g. generalisation of job titles, which could result in “university lecturer” being modified to become “educator”).

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Data perturbation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>The values from the original dataset are modified to be slightly different.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation is used for indirect identifiers (typically numbers and dates), which may potentially be identifiable when combined with other data sources but slight changes in value are acceptable for the attribute. This technique should not be used where data accuracy is crucial.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>It depends on the exact data perturbation technique used. These include rounding and adding random noise. The example in this section shows base-x rounding.</td></tr><tr><td rowspan="2">Other tips</td><td style='text-align: center; word-wrap: break-word;'>The degree of perturbation should be proportionate to the range of values of the attribute. If the base is too small, the anonymisation effect will be weaker; on the other hand, if the base is too large, the end values will be too different from the original and utility of the dataset will likely be reduced.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Note that where computation is performed on attribute values that have been perturbed before, the resulting value may experience perturbation to an even larger extent.</td></tr></table>

## EXAMPLE

In this example, the dataset contains information to be used for research on the possible link between a person's height, weight, age, whether the person smokes and whether the person has "disease A" and/or "disease B". The person's name has already been pseudonymised.

The following rounding is then applied:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Attribute</td><td style='text-align: center; word-wrap: break-word;'>Anonymisation technique</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Height (in cm)</td><td style='text-align: center; word-wrap: break-word;'>Base-5 rounding (5 is chosen, being somewhat proportionate to the typical height value of 120 to 190 cm).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Weight (in kg)</td><td style='text-align: center; word-wrap: break-word;'>Base-3 rounding (3 is chosen, being somewhat proportionate to the typical weight value of 40 to 100 kg).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Age (in years)</td><td style='text-align: center; word-wrap: break-word;'>Base-3 rounding (3 is chosen, being somewhat proportionate to the typical age value of 10 to 100 years).</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>The remaining attributes</td><td style='text-align: center; word-wrap: break-word;'>Nil, because they are non-numerical and difficult to modify without substantial change in value.</td></tr></table>

---

<div style="text-align: center;">Dataset before anonymisation:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Height (cm)</td><td style='text-align: center; word-wrap: break-word;'>Weight (kg)</td><td style='text-align: center; word-wrap: break-word;'>Age (years)</td><td style='text-align: center; word-wrap: break-word;'>Smokes?</td><td style='text-align: center; word-wrap: break-word;'>Disease A?</td><td style='text-align: center; word-wrap: break-word;'>Disease B?</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>198740</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>287402</td><td style='text-align: center; word-wrap: break-word;'>177</td><td style='text-align: center; word-wrap: break-word;'>70</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>398747</td><td style='text-align: center; word-wrap: break-word;'>158</td><td style='text-align: center; word-wrap: break-word;'>46</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>498732</td><td style='text-align: center; word-wrap: break-word;'>173</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>598772</td><td style='text-align: center; word-wrap: break-word;'>169</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr></table>

<div style="text-align: center;">Dataset after anonymisation:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Person</td><td style='text-align: center; word-wrap: break-word;'>Height (cm)</td><td style='text-align: center; word-wrap: break-word;'>Weight (kg)</td><td style='text-align: center; word-wrap: break-word;'>Age (years)</td><td style='text-align: center; word-wrap: break-word;'>Smokes?</td><td style='text-align: center; word-wrap: break-word;'>Disease A?</td><td style='text-align: center; word-wrap: break-word;'>Disease B?</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>198740</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>51</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>287402</td><td style='text-align: center; word-wrap: break-word;'>175</td><td style='text-align: center; word-wrap: break-word;'>69</td><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>398747</td><td style='text-align: center; word-wrap: break-word;'>160</td><td style='text-align: center; word-wrap: break-word;'>45</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>498732</td><td style='text-align: center; word-wrap: break-word;'>175</td><td style='text-align: center; word-wrap: break-word;'>75</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>598772</td><td style='text-align: center; word-wrap: break-word;'>170</td><td style='text-align: center; word-wrap: break-word;'>81</td><td style='text-align: center; word-wrap: break-word;'>42</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td></tr></table>

Note: For base-x rounding, the attribute values to be rounded are rounded to the nearest multiple of x.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Data aggregation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Data aggregation refers to the conversion of a dataset from a list of records to summarised values.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>It is used when individual records are not required and aggregated data is sufficient for the purpose.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>A detailed discussion of statistical measures is beyond the scope of this guide, however typical ways include using totals or averages, etc. It may also be also useful to discuss with the data recipient about the expected utility and find a suitable compromise.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Other tips</td><td style='text-align: center; word-wrap: break-word;'>• Where applicable, watch out for groups having too few records after performing aggregation. In the below example, if the aggregated data includes a single record in any of the categories, it could be easy for someone with some additional knowledge to identify a donor. • Hence, aggregation may need to be applied in combination with suppression. Some attribute may need to be removed, as they contain details that cannot be aggregated and new attributes may need be added (e.g. to contain the newly computed aggregate values).</td></tr></table>

---

## EXAMPLE

In this example, a charity organisation has records of donations made, as well as some information about the donors.

The charity organisation assessed that aggregated data is sufficient for an external consultant to perform data analysis, hence performed data aggregation on the original dataset.

<div style="text-align: center;">Original dataset:</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Donor</td><td style='text-align: center; word-wrap: break-word;'>Monthly income ($)</td><td style='text-align: center; word-wrap: break-word;'>Amount donated in 2016 ($)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor A</td><td style='text-align: center; word-wrap: break-word;'>4000</td><td style='text-align: center; word-wrap: break-word;'>210</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor B</td><td style='text-align: center; word-wrap: break-word;'>4900</td><td style='text-align: center; word-wrap: break-word;'>420</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor C</td><td style='text-align: center; word-wrap: break-word;'>2200</td><td style='text-align: center; word-wrap: break-word;'>150</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor D</td><td style='text-align: center; word-wrap: break-word;'>4200</td><td style='text-align: center; word-wrap: break-word;'>110</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor E</td><td style='text-align: center; word-wrap: break-word;'>5500</td><td style='text-align: center; word-wrap: break-word;'>260</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor F</td><td style='text-align: center; word-wrap: break-word;'>2600</td><td style='text-align: center; word-wrap: break-word;'>40</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor G</td><td style='text-align: center; word-wrap: break-word;'>3300</td><td style='text-align: center; word-wrap: break-word;'>130</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor H</td><td style='text-align: center; word-wrap: break-word;'>5500</td><td style='text-align: center; word-wrap: break-word;'>210</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor I</td><td style='text-align: center; word-wrap: break-word;'>1600</td><td style='text-align: center; word-wrap: break-word;'>380</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor J</td><td style='text-align: center; word-wrap: break-word;'>3200</td><td style='text-align: center; word-wrap: break-word;'>80</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor K</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>440</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor L</td><td style='text-align: center; word-wrap: break-word;'>5800</td><td style='text-align: center; word-wrap: break-word;'>400</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor M</td><td style='text-align: center; word-wrap: break-word;'>4600</td><td style='text-align: center; word-wrap: break-word;'>390</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor N</td><td style='text-align: center; word-wrap: break-word;'>1900</td><td style='text-align: center; word-wrap: break-word;'>480</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor O</td><td style='text-align: center; word-wrap: break-word;'>1700</td><td style='text-align: center; word-wrap: break-word;'>320</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor P</td><td style='text-align: center; word-wrap: break-word;'>2400</td><td style='text-align: center; word-wrap: break-word;'>330</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor Q</td><td style='text-align: center; word-wrap: break-word;'>4300</td><td style='text-align: center; word-wrap: break-word;'>390</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor R</td><td style='text-align: center; word-wrap: break-word;'>2300</td><td style='text-align: center; word-wrap: break-word;'>260</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor S</td><td style='text-align: center; word-wrap: break-word;'>3500</td><td style='text-align: center; word-wrap: break-word;'>80</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Donor T</td><td style='text-align: center; word-wrap: break-word;'>1700</td><td style='text-align: center; word-wrap: break-word;'>290</td></tr></table>

## Anonymised dataset:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Monthly Income ($)</td><td style='text-align: center; word-wrap: break-word;'>Number of donations received (2016)</td><td style='text-align: center; word-wrap: break-word;'>Sum of amount donated in 2016 ($)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1000-1999</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1470</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2000-2999</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1220</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3000-3999</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>290</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4000-4999</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>1520</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5000-6000</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>870</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Grand Total</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>5370</td></tr></table>

---

# ANNEX B: COMMON DATA ATTRIBUTES AND SUGGESTED ANONYMISATION TECHNIQUES

## Direct identifiers

The following table provides suggestions on anonymisation techniques that can be applied to some common types of direct identifiers. Generally, direct identifiers should be suppressed (removed) or pseudonymised. If assigning of pseudonyms is required, usually one set (i.e. one column) of pseudonyms per dataset is sufficient.

For the synthetic data use case, all direct identifier columns can be retained but must be replaced with pseudonymised values.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Record suppression</td><td rowspan="2">Commonly used technique</td><td colspan="2">Example</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Before</td><td style='text-align: center; word-wrap: break-word;'>After</td></tr><tr><td rowspan="4">• Name
• Email address
• Mobile phone number
• NRIC number
• Passport number
• Account number
• Birth certificate number
• Foreign Identification Number (FIN)
• Work permit number</td><td style='text-align: center; word-wrap: break-word;'>Attribute suppression</td><td style='text-align: center; word-wrap: break-word;'>John Tan</td><td style='text-align: center; word-wrap: break-word;'>(Deleted)</td></tr><tr><td colspan="3">Assignment of pseudonyms, for example:</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• Replace direct identifier values with unique random values; or</td><td style='text-align: center; word-wrap: break-word;'>John Tan</td><td style='text-align: center; word-wrap: break-word;'>123456</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• Replace direct identifier values with randomly generated values that follow the format of the data.</td><td style='text-align: center; word-wrap: break-word;'>John.tan@gmail.com
S8822311H</td><td style='text-align: center; word-wrap: break-word;'>123456@abc.com
S8512345A</td></tr></table>

## Indirect identifiers

The following table provides suggestions on anonymisation techniques that can be applied to some common types of indirect identifiers. You should choose to apply one or more of the techniques to each indirect identifier (e.g. apply generalisation and swapping to age, based on your use case).

For the synthetic data use case, two useful techniques are data swapping and data perturbation. These apply to all indirect identifiers.

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Indirect identifier(s)</td><td rowspan="2">Commonly used technique(s)</td><td colspan="2">Example(s)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Before</td><td style='text-align: center; word-wrap: break-word;'>After</td></tr><tr><td rowspan="3">• Age• Height• Weight</td><td style='text-align: center; word-wrap: break-word;'>Generalisation:Generalise the age/height/weight to ranges of 5 or 10 years/cm/kg.</td><td rowspan="3">Record #1: 24Record #2: 39Record #3: 18</td><td style='text-align: center; word-wrap: break-word;'>Generalisation (age range of 5 years):Record #1: 21 to 25Record #2: 36 to 40Record #3: 16 to 20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data perturbation:Add random values (+/- 5) to the original value.</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation:Record #1: 25Record #2: 36Record #3: 17</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping:Randomly switch the age/height/weight associated with each record.</td><td style='text-align: center; word-wrap: break-word;'>Swapping:Record #1: 39Record #2: 18Record #3: 24</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• Gender</td><td style='text-align: center; word-wrap: break-word;'>This indirect data attribute typically only has two generic non-identifying values—M or F and thus, it is generally safe to retain as it is.For the synthetic data use case, the following technique may be further applied to this attribute.Swapping:Randomly switch the gender within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Record #1: MRecord #2: MRecord #3: FRecord #4: M</td><td style='text-align: center; word-wrap: break-word;'>Swapping:Record #1: MRecord #2: FRecord #3: MRecord #4: M</td></tr><tr><td rowspan="2">• Race• Marital status</td><td style='text-align: center; word-wrap: break-word;'>Generalisation:Depending on your dataset, you may combine and generalise selected ethnic groups or marital statuses into a category labelled “Others”. This is to be done if there are unique ethnic groups/marital statuses or too few of the same ethnic groups/marital statuses within your dataset.</td><td rowspan="2">Record #1: IndianRecord #2: ChineseRecord #3: ChineseRecord #4: MalayRecord #5: Eurasian</td><td style='text-align: center; word-wrap: break-word;'>Generalisation:Record #1: OthersRecord #2: ChineseRecord #3: ChineseRecord #4: OthersRecord #5: Others</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping:Randomly switch the race or marital status within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Swapping:Record #1: MalayRecord #2: ChineseRecord #3: IndianRecord #4: EurasianRecord #5: Chinese</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3">• Date of Birth</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Generalise the date of birth to year, or month and year.</td><td rowspan="3">Record #1: 1 Feb 2003 Record #2: 15 Aug 1990 Record #3: 30 Dec 1998</td><td style='text-align: center; word-wrap: break-word;'>Generalisation (month and year): Record #1: Feb 2003 Record #2: Aug 1990 Record #3: Dec 1998</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data perturbation: Randomly modify the date (e.g. +/- 30 days from the original date).</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation: Record #1: 20 Jan 2003 Record #2: 18 Aug 1990 Record #3: 6 Jan 1999</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping: Randomly switch the dates within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: 30 Dec 1998 Record #2: 1 Feb 2003 Record #3: 15 Aug 1990</td></tr><tr><td rowspan="2">• Address</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Generalise the address to pre-defined zones (e.g. with reference to the Urban Redevelopment Authority&#x27;s (URA) Master Plan $ ^{18} $).</td><td style='text-align: center; word-wrap: break-word;'>71 Punggol Central, Singapore 828755</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Punggol</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping: Randomly switch addresses within the dataset. Note: For addresses, unit numbers may be identifying. Where not required, unit numbers should be removed from the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Record #1: 71 Punggol Central, #10-1122, Singapore 828755 Record #2: 35 Mandalay Road, #13-37 Singapore 208215</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: 35 Mandalay Road, #13-37 Singapore 208215 Record #2: 71 Punggol Central, #10-1122, Singapore 828755</td></tr><tr><td rowspan="2">• Postal code</td><td style='text-align: center; word-wrap: break-word;'>Character masking: Mask the last four digits of the postal code. (Singapore has 80 postal districts).</td><td style='text-align: center; word-wrap: break-word;'>117438</td><td style='text-align: center; word-wrap: break-word;'>Character masking: 11xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping: Randomly switch the postal codes within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Record #1: 117438 Record #2: 828755</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: 828755 Record #2: 117438</td></tr><tr><td rowspan="2">• Job title</td><td rowspan="2">Generalisation: There is no easy way to anonymise job titles in an automated way because job titles are non-standard, and organisations can invent their own. One way is to generalise job titles to a pre-defined taxonomy of job natures and/or job levels. However, the mapping likely has to be done manually. Swapping: Randomly switch the job titles within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Chief Executive Officer Team Lead, Software Development</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: C-level Officer IT Manager</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Record #1: CEO Record #2: Director Record #3: Manager</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: Manager Record #2: CEO Record #3: Director</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">• Company name</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Generalise the company name to industry sector (e.g. with reference to the Singapore Standard Industrial Classification (SSIC)) $ ^{19} $.</td><td style='text-align: center; word-wrap: break-word;'>Speedy Taxi Ltd</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Transportation and Storage</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping: Randomly switch the company names within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Record #1: Speedy Taxi LtdRecord #2: Best Food LtdRecord #3: No. 1 Cold Wear Pte Ltd</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: Best Food LtdRecord #2: No. 1 Cold Wear Pte LtdRecord #3: Speedy Taxi Ltd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• IP address</td><td style='text-align: center; word-wrap: break-word;'>Character masking: Mask the last two octets $ ^{20} $ of IPv4 IP addresses and the last 80 bits of IPv6 IP addresses.Note: Swapping may be applied in addition to character masking.</td><td style='text-align: center; word-wrap: break-word;'>IPv4: 12.120.210.88IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334</td><td style='text-align: center; word-wrap: break-word;'>Character masking: IPv4: 12.120.xxx.xxxIPv6: 2001:0db8:85a3:xxxx-xxxx:xxxx:xxxx:xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• Vehicle license plate number</td><td style='text-align: center; word-wrap: break-word;'>Character masking: Mask the last four characters of the vehicle license plate number.Note: Swapping may be applied in addition to character masking.</td><td style='text-align: center; word-wrap: break-word;'>SMF1234A</td><td style='text-align: center; word-wrap: break-word;'>Character masking: SMF1xxxx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>• In-vehicle unit (IU) number</td><td style='text-align: center; word-wrap: break-word;'>Character masking: Mask the last three digits of the IU number.Note: Swapping may be applied in addition to character masking.</td><td style='text-align: center; word-wrap: break-word;'>1234567890</td><td style='text-align: center; word-wrap: break-word;'>Character masking: 1234567xxx</td></tr></table>

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3">• Global Positioning System (GPS) location</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: Round the GPS coordinates (in decimal degrees) to the nearest two decimal places (equivalent to accuracy of 1.11 km) or three decimal place (equivalent to accuracy of 111 m).</td><td rowspan="2">1.27434, 103.79967</td><td style='text-align: center; word-wrap: break-word;'>Generalisation: 1.274, 103.800 (decimal degrees rounded to three decimal places)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data perturbation: Add random values between 0.005 and -0.005 or between 0.0005 and -0.0005.</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation: 1.27834, 103.79767</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swapping: Randomly switch the GPS location values within the dataset.</td><td style='text-align: center; word-wrap: break-word;'>Record #1: 1.27434, 103.79967 Record #2: 1.26421, 103.80405 Record #3: 1.26463, 103.82226</td><td style='text-align: center; word-wrap: break-word;'>Swapping: Record #1: 1.26463, 103.82226 Record #2: 1.27434, 103.79967 Record #3: 1.26421, 103.80405</td></tr></table>

## Target attributes

Target attributes are proprietary information that is important to preserve for data utility. Hence, for most of the use cases, anonymisation techniques are not applied to target attributes. However, for the synthetic data use case, as the record-level data is typically used in development and testing environments which may not be properly secured, it is recommended that one or more anonymisation techniques are applied to the target attributes to ensure no re-identification will occur in the event of a data breach.

It is important to check and ensure that, after applying the anonymisation techniques, no record in the synthetic dataset resembles any record in the original dataset.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Target attributes</td><td rowspan="2">Commonly used technique(s)</td><td colspan="2">Example(s)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Before</td><td style='text-align: center; word-wrap: break-word;'>After</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Transactions</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation:Randomly modify the numerical data (e.g. adding or subtracting random values from the original data). Data perturbation is not possible for alphanumerical or unstructured textual data.</td><td style='text-align: center; word-wrap: break-word;'>Purchase value: $38.05Salary: $6,200</td><td style='text-align: center; word-wrap: break-word;'>Data perturbation:Purchase value: $42Salary: $7,500</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Salary</td><td style='text-align: center; word-wrap: break-word;'>Credit rating</td><td style='text-align: center; word-wrap: break-word;'>Insurance policy</td><td style='text-align: center; word-wrap: break-word;'>Swapping:Randomly switch data within the dataset.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Medical diagnosis</td><td style='text-align: center; word-wrap: break-word;'>Swapping:Randomly switch data within the dataset.</td><td rowspan="2">Vaccination status:Record#1: VaccinatedRecord#2: First doseRecord#3: Unvaccinated</td><td rowspan="2">Swapping:Vaccination status:Record#1: First doseRecord#2: UnvaccinatedRecord#3: Vaccinated</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Vaccination status</td><td style='text-align: center; word-wrap: break-word;'>Note: Swapping may be applied in addition to data perturbation.</td></tr></table>

---

## ANNEX C: k-ANONYMITY

k-anonymity (and similar extensions to it like l-diversity and t-closeness) is a measure used to ensure that the risk threshold has not been surpassed, as part of the anonymisation methodology.

k-anonymity is not the only measure available, nor is it without its limitations, but it is relatively well understood and easy to apply. k-anonymity may not be suitable for all types of datasets or other complex use cases. Other approaches and/or tools such as Special Uniques Detection Algorithm (SUDA) and μ-Argus may be more suitable for assessing the risk of large datasets. Alternative methods, such as differential privacy $ ^{21} $, have also emerged over the past few years.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">k-anonymity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>The k-anonymity model is used as a guideline before anonymisation techniques (e.g. generalisation) have been applied, and for verification after as well, to ensure that any record&#x27;s indirect identifiers are shared by at least k-1 other records. This is the key protection provided by k-anonymity against linking attacks, because k records (or at least different indirect identifiers) are identical in their identifying attributes and thus, create an equivalence class $ ^{22} $ with k members. Therefore, it is not possible to link or single out an individual&#x27;s record since there are always k identical attributes. An anonymised dataset may have different k-anonymity levels for different sets of indirect identifiers, but for “maximum risk” protection against linking, the lowest k is used as a representative value for comparison against the threshold.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>When to use it</td><td style='text-align: center; word-wrap: break-word;'>k-anonymity is used to confirm that the anonymisation measures put in place achieve the desired threshold against linking attacks.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>How to use it</td><td style='text-align: center; word-wrap: break-word;'>First, decide on a value for k (that is equal to or higher than the inverse of the equivalence class size), which provides the lowest k to be achieved among all equivalence classes. Generally, the higher the value of k, the harder it is for data subjects to be identified; however, utility may become lower as k increases and more records may need to be suppressed. After anonymisation techniques have been applied, check that each record has at least k-1 other records with the same attributes addressed by the k-anonymisation. Records in equivalence classes with less than k records should be considered for suppression; alternatively, the dataset can be anonymised further.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Other tips</td><td style='text-align: center; word-wrap: break-word;'>• Besides generalisation and suppression, synthetic data can also be created to achieve k-anonymity. These techniques (and others) can sometimes be used in combination, but do not have the specific method chosen can affect data utility. Consider the trade-offs between dropping the outliers or inserting synthetic data. • k-anonymity assumes that each record relates to a different individual. If the same individual has multiple records (e.g. visiting the hospital on several occasions), then k-anonymity will need to be higher than the repeat records, otherwise the records may not only be linkable, but may also be re-identifiable, despite seemingly fulfilling “k equivalence classes”.</td></tr></table>

---

## EXAMPLE

In this example, the dataset contains information about people taking taxis.

k = 5 is used (i.e. each record should eventually share the same attributes with four other records after anonymisation).

The following anonymisation techniques are used in combination. The level of granularity is one approach to achieving the required k level.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Attribute</td><td style='text-align: center; word-wrap: break-word;'>Anonymisation technique</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Generalisation (10-year intervals)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Occupation</td><td style='text-align: center; word-wrap: break-word;'>Generalisation (e.g. both “database administrator” and “programmer” are generalised to “IT”)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Record suppression</td><td style='text-align: center; word-wrap: break-word;'>Records that do not meet the 5-anonymity criteria after anonymisation techniques have been applied (in this case, generalisation) are removed. For example, the banker’s record is removed as it is the only such value under “Occupation”.</td></tr></table>

## Dataset before anonymisation:


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Serial number</td><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Gender</td><td style='text-align: center; word-wrap: break-word;'>Occupation</td><td style='text-align: center; word-wrap: break-word;'>Average number of trips per week</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Assistant Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>38</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>Lead IT Consultant</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Banker</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>34</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>Database Administrator</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Chief Privacy Officer</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Regional Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>38</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>Programmer</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT Analyst</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Deputy Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Manager, DPO Office</td><td style='text-align: center; word-wrap: break-word;'>11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>UX Designer</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

---

Dataset becoming 5-anonymous after the anonymisation of age and occupation, and suppression of the outlier. (The respective equivalence classes are highlighted in different colours):


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Serial number</td><td style='text-align: center; word-wrap: break-word;'>Age</td><td style='text-align: center; word-wrap: break-word;'>Gender</td><td style='text-align: center; word-wrap: break-word;'>Occupation</td><td style='text-align: center; word-wrap: break-word;'>Average number of trips per week</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>31 to 40</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Banker</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>31 to 40</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>31 to 40</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT</td><td style='text-align: center; word-wrap: break-word;'>3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>31 to 40</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>21 to 30</td><td style='text-align: center; word-wrap: break-word;'>Female</td><td style='text-align: center; word-wrap: break-word;'>Data Protection Officer</td><td style='text-align: center; word-wrap: break-word;'>11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>31 to 40</td><td style='text-align: center; word-wrap: break-word;'>Male</td><td style='text-align: center; word-wrap: break-word;'>IT</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

Note: The average number of trips per week is taken here as an example for a target attribute, without a need to further anonymise this attribute.

---

# ANNEX D: ASSESSING THE RISK OF RE-IDENTIFICATION

There are various ways to assess the risk of re-identification, and these may require rather complex calculations involving computation of probabilities.

This section describes a simplified model, using  $ k\text{-anonymity}^{27} $, and makes the following assumptions:

The release model is non-public;

The attacker is motivated to link an individual to the anonymised dataset; and

The content of the anonymised data is not taken into consideration and that the risk calculated is independent of the kind of information the attacker actually has available.

First, the risk threshold should be established. This value, reflecting a probability, ranges between 0 and 1. It reflects the risk level that the organisation is willing to accept. The main factors affecting the risk threshold should include the harm that could be caused to the data subject, as well as the harm to the organisation, if re-identification takes place; but, it also takes into consideration what other controls have been put in place to mitigate any residual risks. The higher the potential harm, the higher the risk threshold should be. There are no hard and fast rules as to what risk threshold values should be used; the following are just examples.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Potential harm</td><td style='text-align: center; word-wrap: break-word;'>Risk threshold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Low</td><td style='text-align: center; word-wrap: break-word;'>0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Medium</td><td style='text-align: center; word-wrap: break-word;'>0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>0.01</td></tr></table>

---

In computing the re-identification risk, this guide uses the "Prosecutor Risk", which assumes that the attacker knows a specific person in the dataset and is trying to establish which record in the dataset refers to that person.

The simple rule for calculating the probability of re-identification for a single record in a dataset, is to take the inverse of the record's equivalence class size:

P (link individual to a single record) = 1 / record's equivalence class size

To compute the probability of re-identification of any record in the entire dataset, given that there is a re-identification attempt, a conservative approach would be to equate it to the maximum probability of re-identification among all records in the dataset.

P (re-ID any record in dataset) = 1 / Min. equivalence class size in dataset

Note: If the dataset has been k-anonymised,

P (re-ID any record in dataset) <= 1 / k

We can consider three motivated intruder attack scenarios:

1. the deliberate insider attack;

2. the inadvertent recognition by an acquaintance; and

3. a data breach.

P (re-ID) = P (re-ID | re-ID attempt) x P (re-ID attempt)

where P (re-ID | re-ID attempt) refers to the probability of successful re-identification, given there is a re-identification attempt. As discussed earlier, we can take P (re-ID | re-ID attempt) to be (1 / Min. equivalence class size in dataset)

Therefore, P (re-ID) = (1 / Min. equivalence class size in dataset) x P (re-ID attempt)

---

For Scenario #1, the deliberate insider attack, we assume a party receiving the dataset attempts re-identification. To estimate P (re-ID attempt): the probability of a re-identification attempt, factors to consider include the extent of mitigating controls put in place as well as the motives and resources of the attacker. The following table presents example values; again, it is for the party anonymising the dataset to decide on suitable values to use.

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_474_222_548.jpg" alt="Image" width="5%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Scenario #1—... insider attack</td><td colspan="3">Motivation and resource of attacker</td></tr><tr><td colspan="2">P (re-ID attempt) = P(insider attack)</td><td style='text-align: center; word-wrap: break-word;'>Low</td><td style='text-align: center; word-wrap: break-word;'>Medium</td><td style='text-align: center; word-wrap: break-word;'>High</td></tr><tr><td rowspan="4">Extent of mitigating controls</td><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>0.03</td><td style='text-align: center; word-wrap: break-word;'>0.05</td><td style='text-align: center; word-wrap: break-word;'>0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Medium</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>0.25</td><td style='text-align: center; word-wrap: break-word;'>0.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Low</td><td style='text-align: center; word-wrap: break-word;'>0.4</td><td style='text-align: center; word-wrap: break-word;'>0.5</td><td style='text-align: center; word-wrap: break-word;'>0.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>None</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>1.0</td><td style='text-align: center; word-wrap: break-word;'>1.0</td></tr></table>

Factors affecting the motivation and resources of the attacker may include:

Willingness to violate contract (assuming contract preventing re-identification is in place)

2 Financial and time constraints

Inclusion of high-profile personalities (e.g. celebrities) or sensitive data (e.g. credit information) in the dataset

Ease of access to "linkable" data or information, whether publicly available or privately owned, that may enable re-identification of the anonymised dataset

Factors affecting the extent of mitigating controls include:

1 Organisational structures

2 Administrative/legal controls (e.g. contracts)

Technical and process controls

---

For Scenario #2, the inadvertent recognition by an acquaintance, we assume a party receiving the dataset inadvertently re-identifies a data subject while examining the dataset. This is possible because the party has some additional knowledge about the data subject due to their relationship (e.g. friend, neighbour, relative, colleague, etc.). To estimate P (re-ID attempt): the probability of a re-identification attempt, the main factor to consider is the likelihood that the data recipient knows someone in the dataset.

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_473_223_549.jpg" alt="Image" width="5%" /></div>


Scenario #2—inadvertent recognition by an acquaintance
P (re-ID attempt) = P (data recipient knowing a person in the dataset)

For Scenario #3, the probability of a data breach occurring at the data recipient's ICT system can be estimated based on available statistics about the prevalence of data breaches in the data recipient's industry. This is based on the assumption that the attackers who obtained the dataset will attempt re-identification.

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_758_223_832.jpg" alt="Image" width="5%" /></div>


Scenario #3—a data breach
P (re-ID attempt) = P (data breach in data recipient's industry)

The highest probability among the three scenarios should be used as P (re-ID attempt).

P (re-ID attempt) = Max (P(insider attack), P(data recipient knowing a person inside the dataset), P(data breach in data recipient's industry))

To put everything together,

P (re-ID) = (1 / Min. equivalence class size in dataset) x P (re-ID attempt) = (1 / k) x P (re-ID attempt) for k-anonymised dataset
where P (re-ID attempt) = Max (P (insider attack),
P (data recipient knowing a person in the dataset), P (data breach in data recipient's industry))

---

## ANNEX E: ANONYMISATION TOOLS

The following is a list of some commercial or open-source anonymisation tools.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Tool</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>URL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Amnesia</td><td style='text-align: center; word-wrap: break-word;'>Amnesia anonymisation tool is a software used locally to anonymise personal and sensitive data. It currently supports k-anonymity and km-anonymity guarantees.</td><td style='text-align: center; word-wrap: break-word;'>https://amnesia.openaire.eu/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Arcad DOT-Anonymizer</td><td style='text-align: center; word-wrap: break-word;'>DOT-Anonymizer is a tool that maintains the confidentiality of test data by concealing personal information. It works by anonymising personal data while preserving its format and type.</td><td style='text-align: center; word-wrap: break-word;'>https://www.arcadsoftware.com/dot/data-masking/dot-anonymizer/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ARGUS</td><td style='text-align: center; word-wrap: break-word;'>ARGUS stands for “Anti Re-identification General Utility System”. The tool uses a wide range of different statistical anonymisation methods such as global recoding (grouping of categories), local suppression, randomisation, adding noise, microaggregation, top- and bottom coding. It can also be used to generate synthetic data.</td><td style='text-align: center; word-wrap: break-word;'>https://research.cbs.nl/casc/mu.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ARX</td><td style='text-align: center; word-wrap: break-word;'>ARX is an open-source software for anonymising sensitive personal data.</td><td style='text-align: center; word-wrap: break-word;'>https://arxiv.deidentifier.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Eclipse</td><td style='text-align: center; word-wrap: break-word;'>Eclipse is a suite of tools from Privacy Analytics that facilitates anonymisation of health data.</td><td style='text-align: center; word-wrap: break-word;'>https://privacy-analytics.com/health-data-privacy/health-data-software/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sdcMicro</td><td style='text-align: center; word-wrap: break-word;'>sdcMicro is used to generate anonymised microdata such as public and scientific use files. It supports different risk estimation methods.</td><td style='text-align: center; word-wrap: break-word;'>https://cran.r-project.org/web/packages/sdcMicro/index.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UTD Anonymisation Toolbox</td><td style='text-align: center; word-wrap: break-word;'>UT Dallas Data Security and Privacy Lab compiled various anonymisation techniques into a toolbox for public use.</td><td style='text-align: center; word-wrap: break-word;'>http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home</td></tr></table>

---

## ACKNOWLEDGEMENTS

---

## ACKNOWLEDGEMENTS

The PDPC and Infocomm Media Development Authority (IMDA) express their sincere appreciation to the following organisations for their valuable feedback in the development of this publication.

AsiaDPO

• BetterData Pte Ltd

• ISACA (Singapore Chapter)—Data Protection SIG

• Law Society of Singapore—Cybersecurity and Data Protection Committee (CSDPC)

• Ministry of Health (MOH)

• Replica Analytics

• Privitar Ltd

• SGTech

• Singapore Business Federation (SBF)—Digitalisation Committee

• Singapore Corporate Counsel Association (SCCA)—Data Protection, Privacy and Cybersecurity (DPPC) Chapter

Singapore Department of Statistics (DOS)

• Smart Nation and Digital Government Group (SNDGO)

## The following guides were referenced in this guide

UKAN. The Anonymisation Decision Making Framework 2nd Edition: European Practitioners' Guide, by Mark Elliot, Elaine Mackey and Kieron O'Hara, 2020.

CSIRO and OAIC. The De-Identification Decision-Making Framework, by Christine M O'Keefe, Stephanie Otorepec, Mark Elliot, Elaine Mackey and Kieron O'Hara, 18 September 2017.

• IPC. De-identification Guidelines for Structured Data, June 2016, https://www.ipc.on.ca/wp-content/uploads/2016/08/Deidentification-Guidelines-for-Structured-Data.pdf.

• El Emam, K. Guide to the De-Identification of Personal Health Information, CRC Press, 2013.

• Article 29 Data Protection Working Party (European Commission). "Opinion 05/2014 on Anonymisation Techniques". 10 April 2014, http://ec.europa.eu/justice/data-protection/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf.

• NIST. NISTIR 8053: De-Identification of Personal Information, by S L Garfinkel, October 2015, http://nvlpubs.nist.gov/nistpubs/ir/2015/NIST.IR.8053.pdf.

---



---

## #SGDIGITAL

Singapore Digital (SG:D) gives Singapore's digitalisation efforts a face, identifying our digital programmes and initiatives with one set of visuals, and speaking to our local and international audiences in the same language.

The SG:D logo is made up of rounded fonts that evolve from the expressive dot that is red. SG stands for Singapore and :D refers to our digital economy. The :D smiley face icon also signifies the optimism of Singaporeans moving into a digital economy. As we progress into the digital economy, it's all about the people — empathy and assurance will be at the heart of all that we do.

BROUGHT TO YOU BY

pdpc PERSONAL DATA PROTECTION COMMISSION SINGAPORE

Copyright 2022 – Personal Data Protection Commission Singapore (PDPC)

This publication gives a general introduction to basic concepts and techniques of data anonymisation. The contents herein are not intended to be an authoritative statement of the law or a substitute for legal or other professional advice. The PDPC and its members, officers and employees shall not be responsible for any inaccuracy, error or omission in this publication or liable for any damage or loss of any kind as a result of any use of or reliance on this publication.

The contents of this publication are protected by copyright, trademark or other forms of proprietary rights and may not be reproduced, republished or transmitted in any form or by any means, in whole or in part, without written permission.