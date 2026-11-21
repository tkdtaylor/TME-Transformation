<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 14 Third-Party SaaS & Vendor AI Procurement Assessment Checklist

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-14` (Third-Party SaaS & Vendor AI Procurement Assessment Checklist) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | Corporate Procurement Officers, Business Unit Sponsor Leads, IT Vendor Managers, Legal Counsel, InfoSec Reviewers, and AI Center of Excellence (CoE) |
| **Primary Internal Owner** | Corporate Procurement, Information Security (CISO), Legal & AI Center of Excellence (CoE) |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's Corporate Procurement, Information Security, Legal, and AI Center of Excellence (CoE) teams prevent duplicate SaaS AI spend and govern third-party vendor AI risk. It is **not** prescriptive. Sections include a **Two-Stage Procurement Gate** (Stage 1 Core Platform Bypass Check + Stage 2 10-Point Vendor Security & Legal Checklist `VND-001` to `VND-010`) and 3 illustrative vendor evaluation patterns (`VREV-001` to `VREV-003`) so teams do not have to start from a blank page.

## 1. How the AI CoE & Procurement Can Create, Customize & Enforce This Checklist

### 1.1 Purpose & Why This Document Exists

Across large enterprises, the fastest-growing source of AI security risk and wasted software budget is **SaaS AI Sprawl** - where incumbent software vendors (across HR, Finance, Legal, Operations, CRM, and document utilities) pitch expensive per-seat "AI Copilot / Assistant" add-ons or silently enable generative AI features by default during contract renewals.

While [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`, Section 3.3) establishes the architectural *Vendor Bypass Standard* and [01 Enterprise AI Strategy Charter & Public AI Trust Statement](01_EnterpriseAIStrategyCharter.md) (`AIAF-DOC-01`, Principle `STR-06`) sets the executive principle of horizontal platform consolidation, Corporate Procurement and Information Security need an operational **Two-Stage Procurement Gate Checklist** to evaluate vendor requests day-to-day. Without this gate:

1. The organization pays twice for capabilities already included in its **Enterprise AI Platform seats, Grounded Knowledge Notebooks, No-Code Agent Builder, and Code-First Agent SDK** platform.
2. Third-party SaaS vendors may process `D3 Confidential` or `D4 Restricted` data outside approved regional boundaries or use customer telemetry to train shared commercial models.
3. Siloed SaaS AI tools create fragmented search experiences that cannot reason across the organization's unified enterprise knowledge base.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Primary Custodians**: Corporate Procurement Lead, Information Security (CISO), Legal / Data Protection Officer (DPO), and AI Center of Excellence (CoE) Lead.
- **Required Internal Contributors**: Business Unit Sponsor submitting the software requisition and IT Vendor / Enterprise Architecture Reviewer.

### 1.3 Recommended Internal CoE & Procurement Production Process (Procurement Integration Sync)

To operationalize this checklist internally without external facilitation, the AI CoE Lead and Corporate Procurement Lead can run a Procurement Integration Sync:

1. **Embed Stage 1 ("Core Platform Bypass Check") into the Purchase Requisition Workflow:** Require any business unit requesting a new AI tool or SaaS AI add-on to first verify with the AI CoE whether `>= 80%` of the capability can be delivered using the organization's existing **Enterprise AI Platform, Grounded Knowledge Notebooks, or Code-First Agent SDK** at **zero incremental SaaS license cost**.
2. **Attach Stage 2 (`VND-001` to `VND-010`) to the Third-Party Risk Management (TPRM) Questionnaire:** Require written vendor evidence against all 10 security, legal, and architecture gates before any `D2 Internal`, `D3 Confidential`, or `D4 Restricted` data is connected.
3. **Audit Upcoming SaaS Renewals:** Review enterprise software renewals ahead of contract renewal to strike out "opt-in by default" vendor AI training clauses prior to signature and log approved/rejected tools in [13 Operational Governance Registers (Decision, Tool & Data Dictionary) & GenAIOps Guide](13_OperationalGovernanceRegistersAndGenAIOps.md) (`ApprovedAIToolRegistry`, `AIAF-DOC-13`).

## 2. Two-Stage Vendor AI Procurement Decision Flow

```
+-----------------------------------------------------------------------+
|       ENTERPRISE TWO-STAGE THIRD-PARTY AI PROCUREMENT GATEFLOW        |
+-----------------------------------------------------------------------+
|                                                                       |
|  [BU Requests New Third-Party AI Tool or SaaS "AI Add-On" License]    |
|                                  |                                    |
|                                  v                                    |
|  +-----------------------------------------------------------------+  |
|  | STAGE 1: CORE PLATFORM BYPASS CHECK (AI CoE Architecture Triage)|  |
|  | Can >= 80% of this capability be met using our existing         |  |
|  | Enterprise AI Platform, Knowledge Notebooks, or Agent SDK?      |  |
|  +-----------------------------------------------------------------+  |
|            |                                         |                |
|     [YES - Covered]                           [NO - Specialized]      |
|            |                                         |                |
|            v                                         v                |
|  +-------------------------------+   +-----------------------------+  |
|  | BYPASS EXTERNAL PURCHASE      |   | STAGE 2: 10-POINT TPRM GATE |  |
|  | Deliver on existing           |   | InfoSec, Legal & Data       |  |
|  | Enterprise AI platform        |   | Residency Verification      |  |
|  | (USD 0 incremental SaaS cost) |   | (Gates VND-001 to VND-010)  |  |
|  +-------------------------------+   +-----------------------------+  |
+-----------------------------------------------------------------------+
```

## 3. Stage 1: Core Platform Bypass Evaluation (Zero-Cost Consolidation Gate)

Before Corporate Procurement opens a vendor security review, the requesting Business Unit and the AI CoE evaluate whether the requested capability duplicates the organization's core AI platform ([AIAF-DOC-08](08_AIUseCaseIntakeAndPortfolioBacklog.md) and [AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)):

| Requested Vendor Capability Category | Duplicate External SaaS Pitch | Core Platform Equivalent (Already Licensed / Available) | Default Procurement Decision |
| :--- | :--- | :--- | :--- |
| **Document Summarization, SOP Q&A & Policy Research** | Standalone PDF chat tools, legal/HR doc assistants, or SaaS knowledge add-ons (per-seat SaaS markups). | **Grounded Knowledge Notebooks (`1M-2M` context)** & **Enterprise AI Assistant** grounded on enterprise document repositories (`D1-D3`, or `D4` in scoped enclave workspaces `CAT-008`). | **Bypass External Vendor** - Onboard BU to Curated Knowledge Workspaces (`CAT-001` to `CAT-008` in [AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)) at zero incremental software cost. |
| **No-Code Workflow Assistants & Multi-Source Search** | Departmental workflow bots or standalone enterprise search SaaS platforms. | **No-Code Agent Builder (`Gateway 1 & 2`)** with Federated Enterprise Repository & ITSM Connectors. | **Bypass External Vendor** - Build internal low-code agent via AI CoE Champion (`L200`) template (`UC-005`, `UC-008`, `UC-009`). |
| **Custom Domain Agents Calling Internal APIs / Lakehouse** | Bespoke third-party agent SaaS platforms charging per-workflow or platform fees. | **Code-First Agent SDK** on **Enterprise Agent Runtime (`Gateway 2`)** with read-only MCP/SQL gateways to ERP & Cloud Data Lakehouse (`UC-004`, `UC-006`). | **Bypass External Vendor** - Build on governed Code-First Agent blueprint inside the organization's Private Network Perimeter. |
| **Embedded Domain-Specific Physical / OT / CAD Models** | Specialized engineering simulation, industrial PLC diagnostics, or proprietary statutory tax-filing engine. | Not natively covered by general-purpose foundation models without specialized vendor IP. | **Proceed to Stage 2 (`VND-001` to `VND-010`)** for formal InfoSec and Legal vetting. |

## 4. Stage 2: The 10 Mandatory Vendor AI Security, Legal & Architecture Gates (`VND-001` to `VND-010`)

If a third-party SaaS AI tool passes Stage 1 as a genuine specialized need, the vendor must provide written contractual and technical evidence satisfying all 10 gates below before any `D2 Internal`, `D3 Confidential`, or `D4 Restricted` data is connected (`D5 Regulated / Critical` data remains strictly prohibited from external cloud SaaS LLMs per [AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md)):

| Gate ID | Assessment Domain | Mandatory Enterprise Requirement | Minimum Acceptable Vendor Evidence | Red-Flag Disqualifier (Auto-Reject) |
| :--- | :--- | :--- | :--- | :--- |
| **`VND-001`** | **Zero Model Training Guarantee** | Vendor contractually guarantees that corporate prompts, uploaded documents, embeddings, and user feedback are **never** used to train, fine-tune, or improve foundation models shared with other customers. | Signed Data Processing Addendum (DPA) with explicit Zero-Training & Zero-Retention clause across vendor and all sub-processors. | Vendor relies on "opt-out via support ticket" or uses customer feedback/telemetry to train global models. |
| **`VND-002`** | **Sub-Processor & Foundation Model Transparency** | Vendor discloses the exact underlying LLM providers (for example, Managed Cloud AI Endpoints or self-hosted models) and provides 30-day advance notice before switching models. | Written Sub-Processor Register specifying model provider, hosting region, and API tier (Enterprise vs. Consumer). | Vendor routes calls through consumer-tier APIs or undisclosed third-party model routers. |
| **`VND-003`** | **Data Residency & Sovereignty Alignment** | Data at rest (vector indexes, chat history, logs) and inference processing must reside in organization-approved jurisdictions (`global`, `us`, `eu`, or specific national regions per Legal/DPO mandate). | Architecture diagram and tenant configuration screenshot proving regional pinning. | Uncontrolled cross-border processing with no regional isolation option for `D3/D4` data. |
| **`VND-004`** | **Enterprise Identity & B2B Guest Exclusion** | Supports SAML 2.0 / OIDC SSO via the corporate Identity Provider (IdP) and SCIM 2.0 automated provisioning, enforcing external B2B guest exclusion (`userType EQUALS 'Member'`). | Live SSO test in staging tenant; no local username/password backdoors permitted. | Tool only supports email magic links, shared passwords, or cannot block external guest accounts. |
| **`VND-005`** | **Source-System ACL Inheritance** | If the vendor indexes enterprise repositories, it must enforce **query-time document-level ACLs** so users only see snippets they have permission to open in the source system. | Technical whitepaper + live red-team verification test using two accounts from different business units. | Tool uses a single admin service principal to index files and exposes answers to all licensed users equally. |
| **`VND-006`** | **Audit Logging & SIEM Export** | Vendor exports immutable audit logs of admin actions, data connector changes, and user/agent tool calls to the corporate SIEM within 15 minutes. | API/Webhook schema documentation and sample log payload. | No customer-accessible audit logs or logs retained for `< 90` days. |
| **`VND-007`** | **Prompt Injection & Output Safety Controls** | Vendor implements input sanitization, indirect prompt injection defenses (`LLM01`), and DLP redaction comparable to the organization's **Runtime AI Guardrail Service** ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)). | Latest third-party penetration test / OWASP LLM Top 10 assessment report (`< 12` months old). | No documented defenses against indirect prompt injection or jailbreaks. |
| **`VND-008`** | **Human-in-the-Loop (HITL) for Write Actions** | Any feature capable of modifying records, sending external emails, or executing financial/operational transactions must support mandatory human confirmation gates. | Product configuration guide demonstrating read-only vs. write-action role separation. | Autonomous write actions cannot be disabled or restricted to read-only mode. |
| **`VND-009`** | **Tenant Offboarding & Cryptographic Erasure** | Upon contract termination or pilot rejection, vendor deletes all organizational data, vector embeddings, and caches within 30 days and provides a certificate of destruction. | Contractual termination clause + documented data purge SLA. | Vendor retains derived embeddings or anonymized transcripts indefinitely. |
| **`VND-010`** | **Transparent Unit Economics & Exit Portability** | Pricing is predictable without hidden token overage multipliers; prompts, Golden Eval Sets, and knowledge assets can be exported in standard formats (JSON/Markdown/CSV). | Full pricing schedule + data export verification during pilot. | Proprietary lock-in where curated prompts or knowledge bases cannot be exported. |

## 5. Illustrative Vendor AI Assessment Patterns (`Template Examples`)

| Evaluation ID | Proposed Vendor / SaaS Feature | Requesting BU | Stage 1 Bypass Result | Stage 2 Risk Findings (`VND-001` to `VND-010`) | Final CoE & Procurement Decision |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`VREV-001`** | **Standalone PDF Contract Summarizer SaaS** (Per-seat SaaS add-on) | Legal & Commercial | **FAILED Stage 1 (Duplicate)** - Covered 100% by **`UC-007` (Enterprise Contract Obligation & Renewal Clause Reviewer)** using Restricted Enclave Workspaces (`CAT-008`, `D4 Restricted`). | Not required - Stage 1 bypass avoids duplicate annual SaaS spend (logged under `VAL-04` in [AIAF-DOC-09](09_ValueRealizationAndSeatGovernanceSOP.md)). | **REJECTED EXTERNAL PURCHASE** - Onboarded team to Enterprise AI Platform & Restricted Enclave Workspace (`CAT-008`). |
| **`VREV-002`** | **Incumbent HR / ITSM SaaS "AI Copilot Add-On"** (Renewal upsell) | Human Resources & IT Service Management | **FAILED Stage 1 (Duplicate)** - 85%+ of employee policy Q&A and ticket triage is covered by **`UC-005` (IT & HR Internal Employee Service Desk Triage Agent)** and `CAT-002` (`D2/D3`). | Vendor add-on required high minimum annual commitment and lacked cross-repository grounding across enterprise policy folders. | **REJECTED ADD-ON UPSELL** - Retained base SaaS license; delivered cross-source HR/IT Q&A via `UC-005` in No-Code Agent Builder. |
| **`VREV-003`** | **Specialized Industrial Equipment Vibration Anomaly Module** (Embedded OT ML) | Operations & Fleet Engineering | **PASSED Stage 1 (Specialized OT IP)** - Requires proprietary physical sensor models not covered by general LLMs. | Passed `VND-001` (Zero training), `VND-003` (Isolated enclave hosting), and `VND-008` (Read-only diagnostic alert output; zero direct equipment actuation). | **APPROVED WITH CONDITIONS** - Deployed strictly inside `D5` operational boundary (`SRC-012`); de-identified maintenance manuals (`D3`, `SRC-002`) grounded in `UC-001` (`CAT-001`). |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): AI Governance & Risk Perspective (third-party AI vendor risk, build vs. buy reassessment) and AI Security & Trust Perspective (AI supply chain security).
- [References](../References.md): Maintained catalog of regulatory, security, and operational standards.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Third-party and supply chain risk management (`Govern 6.1 & 6.2`).
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/): Controls for `LLM03` (Supply Chain) and `LLM01` (Prompt Injection).
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Supplier management, contractual data controls, and auditability.
