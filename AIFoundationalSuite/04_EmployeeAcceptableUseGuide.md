<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-04` (Employee-Facing 1-Page AI Acceptable Use Policy & Traffic-Light Guide) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | All Enterprise AI Platform Users, Early-Access Power Users / CoE Champions, Human Resources, Legal, and Information Security |
| **Primary Internal Owner** | Information Security (CISO Office), Human Resources, Legal & AI Center of Excellence (CoE) |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE), Human Resources, and Information Security teams communicate clear, everyday AI usage rules to employees. It is **not** prescriptive. Sections include the **5 Golden Rules**, a 1-page **`GREEN / AMBER / RED` Traffic-Light Usage Guide**, a **10-Second Pre-Prompt Decision Flowchart**, and a ready-to-use **Employee Onboarding Acknowledgement Form** so teams do not have to start from a blank page. Organizations can share this guide directly or customize the bracketed fields (`<Organization Name>`, `<@company.com>`) to fit their internal policies.

## 1. How the AI CoE, HR & InfoSec Can Customize & Roll Out This Policy

### 1.1 Purpose & Why This Document Exists

To clear **Readiness Checklist Item `CHK-01`** (*"An AI Acceptable Use Policy exists and is communicated to employees"*) in [10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap](10_AIMaturityScorecardAndReadinessRoadmap.md) (`AIAF-DOC-10`) before launching to general users, employees need clear, practical rules they can read quickly. While [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`) provides the technical standard for CISO, IT, and Data Stewards, end users need a concise **"Traffic Light" Acceptable Use Guide** (`Green / Amber / Red`) that answers three daily questions:

1. *Which AI tools am I approved to use for work?*
2. *What can I safely prompt or upload today (`Green`), what requires human verification before sharing (`Amber`), and what is strictly off-limits (`Red`)?*
3. *What are my personal responsibilities when using AI-generated content?*

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Primary Internal Authors**: AI Center of Excellence (CoE) Lead, Information Security (CISO Office), and Human Resources / Internal Communications.
- **Accountable Sign-Off**: CISO, General Counsel, and Head of Human Resources.
- **Recommended Rollout Process**: Attach Sections 2, 3, and 4 to the Welcome Email, display the 5 Golden Rules during **Track 3 (`L100`) Mass Onboarding Webinars**, and capture employee acknowledgement via the corporate learning management or onboarding portal.

## 2. Employee AI Acceptable Use Policy (Template)

### 2.1 Five Golden Rules for Every Colleague

When using the **Enterprise AI Assistant**, **Grounded Knowledge Notebooks**, or any other approved AI tool at `<Organization Name>`, every colleague must follow five core rules:

1. **You Own the Final Output (Human Accountability)**: AI is a productivity assistant, not a decision-maker. You are personally accountable for the accuracy, tone, calculations, and compliance of any email, report, spreadsheet, code snippet, or presentation you send or publish using AI.
2. **Always Check Citations Before Acting ("Trust, but Verify")**: Generative AI can occasionally misinterpret complex tables or generate plausible-sounding errors (*hallucinations*). Whenever an output influences a technical procedure, financial report, legal clause, or customer communication, click the **inline source citation links** to verify the underlying source document.
3. **Log In Only with Your Corporate Identity (No Shadow AI)**: Use the **Enterprise AI Platform** signed in with your `<@company.com>` corporate Single Sign-On (SSO) account. Under `<Organization Name>`'s enterprise agreement, your prompts and files in the Enterprise AI Platform are private to our organization and **never used to train external public AI models**. Never paste non-public corporate data into free consumer web chatbots, personal AI accounts, or unapproved browser extensions.
4. **Respect Confidentiality, Customer & Critical System Boundaries**: Only upload or query documents you are authorized to access in your role. Never paste live critical infrastructure or operational control commands (`D5`), security credentials, API keys, or unredacted sensitive personal data (such as national ID numbers, payment card numbers, or medical records) into chat prompts.
5. **Label & Escalate When Unsure**: If you are sharing an AI-assisted financial, legal, or technical draft for formal review, note that AI assisted in the initial synthesis so reviewers know to verify key figures. If you encounter an unexpected access result or safety issue, report it immediately to your departmental **AI CoE Champion**.

### 2.2 The Employee "Traffic Light" AI Usage Guide (`Green / Amber / Red`)

| Traffic Light | What You Can Do (`Permitted Workflow`) | Concrete Daily Enterprise Examples | Required Employee Action |
| :---: | :--- | :--- | :--- |
| **GREEN: ENCOURAGED DAILY USE** (`D1 Public` & `D2 Internal` Data) | **Personal & Team Productivity in Enterprise AI Assistant**: - Summarizing long email threads, meeting notes, and internal policies. - Searching across your authorized cloud document folders and intranet files. - Translating documents across languages for global collaboration. - Running **Enterprise Deep Research** on public market trends, competitor announcements, and regulatory developments. - Creating **Audio Briefings** and study guides in Grounded Knowledge Notebooks from training materials. | - *"Summarize the key action items and owners from my email thread on the Q4 operational review."* - *"Compare the travel reimbursement rules in our Global Business Travel Policy PDF."* - *"Run a Deep Research report on recent industry regulatory updates and competitor product launches."* | Read the output for sensibility and tone before sending. |
| **AMBER: PERMITTED WITH MANDATORY HUMAN VERIFICATION** (`D3 Confidential` & Scoped `D4` Data) | **High-Judgment Technical, Financial, Legal & Customer Work (`Stage 2 HITL`)**: - Synthesizing technical manuals or operational SOPs in a **Departmental Knowledge Workspace**. - Analyzing multi-entity financial variances or vendor RFP bids. - Drafting customer incident advisories or reviewing contract obligations in a Legal-scoped workspace. - Writing or refactoring internal Python, SQL, or automation scripts. | - *"Using the Operations Maintenance Notebook, list the preventive inspection steps and cite the exact manual section."* - *"Draft a customer status update based on this approved incident summary."* - *"Summarize the renewal notice obligations in Section 14 of this commercial contract."* | **Mandatory Human Check**: 1. Click every inline source citation to verify exact numbers, tolerances, and legal terms. 2. Have the qualified engineer, financial controller, legal counsel, or peer reviewer sign off before execution or external release. |
| **RED: STRICTLY PROHIBITED** (`D5 Regulated / Critical` & Unsanctioned Tools) | **Strictly Off-Limits Across All Staff**: - Pasting any non-public corporate data (`D2`-`D5`) into **free public consumer AI websites**, personal accounts, or unapproved mobile apps. - Inviting external third-party AI recording/note-taking bots into internal virtual meetings. - Inputting live operational control commands (`D5`), network topologies, passwords, SSH/API keys, or cryptographic secrets into any chat prompt. - Allowing an AI agent to autonomously approve financial payments, sign contracts, or make hiring/disciplinary HR decisions. | - Pasting a financial trial balance or customer pricing sheet into a personal consumer chatbot account. - Allowing an external meeting-recorder bot to join an internal executive, legal, or operations call. - Asking an AI tool to make a final candidate screening or employee performance decision. | **STOP**: Do not execute. Use sanctioned **Enterprise AI Platform** tools for `D1`-`D3` work, and consult your **CoE Champion** or **InfoSec** for `D4` workflows. |

## 3. Quick Decision Flowchart Before You Hit "Send" on a Prompt

```
+-----------------------------------------------------------------------+
|         EMPLOYEE 10-SECOND SAFETY CHECK BEFORE PROMPTING AI           |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  1. AM I LOGGED INTO OUR OFFICIAL ENTERPRISE AI TENANT?               |
|     * NO (Public consumer bot / personal account) -> STOP (D1 Only).  |
|     * YES (Authenticated via Corporate SSO)       -> Go to Step 2.    |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  2. DOES MY PROMPT CONTAIN CRITICAL SYSTEM SECRETS OR REGULATED (D5)? |
|     * YES (Passwords, API keys, raw regulated IDs, OT cmds) -> STOP.  |
|     * NO (Public, Internal, or Authorized Dept Docs)        -> Go 3.  |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  3. WILL THIS OUTPUT INFLUENCE A TECHNICAL, FINANCIAL, LEGAL,         |
|     OR EXTERNAL CUSTOMER DECISION?                                    |
|     * YES (Amber) -> Click inline citations & verify with human owner.|
|     * NO (Green)  -> Review for clarity and use to accelerate work.   |
+-----------------------------------------------------------------------+
```

## 4. Employee Onboarding Acknowledgement Template (Ready for HR / L100 Training)

> **Enterprise AI Acceptable Use Acknowledgement**
>
> By activating my **Enterprise AI Platform** license, I confirm that I have read and understood the *Employee AI Acceptable Use Policy*:
>
> - [ ] I will use only organization-sanctioned AI tools authenticated via my corporate Single Sign-On (SSO) account for company business, and I will never paste non-public corporate information (`D2` to `D5`) into unapproved public consumer AI tools.
> - [ ] I will never input live critical infrastructure / operational control commands (`D5`), passwords, API keys, or unauthorized sensitive personal data into AI prompts.
> - [ ] I understand that I remain personally accountable for all work products I produce with AI assistance, and I will verify inline source citations and obtain required human sign-offs before acting on technical, financial, legal, or customer-facing outputs.
> - [ ] I understand that allocated Enterprise AI Platform licenses are reviewed every **60 days** for active usage so unutilized seats can be reallocated to waitlisted colleagues.

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): People & Workforce Perspective, Guiding Principles (human accountability and Shadow AI governance), and Human-in-the-Loop requirements.
- [References](../References.md): Maintained catalog of standards and regulatory review cadences.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1): Guidance on accountable, transparent, and safe workplace generative AI usage.
- [European Commission AI Act Policy Page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai): Workplace AI literacy and transparency obligations.
