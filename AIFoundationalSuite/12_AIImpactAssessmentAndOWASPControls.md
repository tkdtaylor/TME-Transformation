<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 12 AI Impact Assessment (AIIA), Measurable RAI & OWASP LLM Controls

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-12` (AI Impact Assessment, Measurable Responsible AI & OWASP LLM Top 10) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Information Security (CISO), Legal & Compliance, Data Stewards, Business Unit Owners, and Technical Agent Builders |
| **Primary Internal Owner** | Business Unit Use-Case Owner (`Decision Owner`) & AI Governance / InfoSec Reviewer |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE), Information Security, and Legal teams evaluate medium- and high-risk AI workflows (`Tier 2` to `Tier 4`). It is **not** prescriptive. Sections include a completed reference example for a universal corporate use case (`UC-004`: Multi-Entity Financial Consolidation & Variance Analysis Agent) alongside measurable Responsible AI (`RAI`) thresholds and the **OWASP Top 10 for LLM Applications (`LLM01`-`LLM10`)** control matrix so teams do not have to start from a blank page. Organizations can share this template directly or adapt it to their internal risk management standards.

## 1. How the AI CoE Can Create, Customize & Review This Document

### 1.1 Purpose & Why This Document Exists

While **Tier 1 (Low Risk)** personal productivity use cases (such as summarizing public industry news or drafting internal emails in **Gateway 1**) are governed by standard enterprise SSO and Acceptable Use policies, **Tier 2 (Medium)**, **Tier 3 (High)**, and **Tier 4 (Critical)** workflows - such as multi-entity financial consolidation, legal contract obligation review, or organization-wide service desk agents in **Gateway 2** - require a structured pre-launch risk assessment.

This document provides the worked baseline for the canonical AIAF **AI Impact Assessment** ([AIImpactAssessment.md](../Templates/AIImpactAssessment.md)), translating high-level governance into three auditable engineering artifacts:

1. **The 5-Step AI Impact Assessment (`AIIA`)**: Documents the use case purpose, decision role (`Advisory / Approval-Gated / Automated`), `D1`-`D5` data inputs, named human accountability, and residual risk controls.
2. **Measurable Responsible AI (RAI) Evidence**: Converts the **6 Responsible AI Principles** (`Fairness, Reliability, Privacy, Transparency, Accountability, Inclusiveness`) from abstract statements into falsifiable test thresholds (`Groundedness >= 85%`, `Answer Relevance >= 90%`, `Cross-Entity ACL Leakage = 0%`).
3. **OWASP Top 10 for LLM Applications (`LLM01`-`LLM10`) Control Matrix**: Maps concrete technical platform and enterprise Identity Provider (IdP) security controls against prompt injection, sensitive data disclosure, excessive agency, vector leakage, and unbounded token consumption.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Initiator & Co-Authors**: Business Unit Process Owner (`Decision Owner`) and Internal Technical Builder (`L200 Champion` or `L300 AI Developer`).
- **Mandatory Internal Reviewers for Tier 2+ Promotion (`Gateway 2`)**:
  - **Data Steward**: Verifies `D3/D4` data classification, source ACL inheritance, and retention rules ([AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md)).
  - **Information Security Reviewer (CISO Office)**: Verifies OWASP `LLM01`-`LLM10` mitigations, Private Network Perimeter (VPC / Private Link), CMEK, and 90-day kill-switch drill ([AIAF-DOC-06](06_AISecurityIncidentAndKillSwitchRunbook.md)).
  - **Legal / Privacy Counsel (DPO)**: Required whenever `D4 Restricted` (confidential contracts, M&A, PII) or `D5 Regulated` data is touched.
  - **AI Center of Excellence (CoE) Lead**: Confirms registration in `AIDecisionRegister` ([AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)).

### 1.3 Recommended Approach: Running a CoE Risk & Security Sign-Off Review

The template below is pre-populated with a reference baseline for **Candidate Code-First Custom Agent #1 (`UC-004`: Multi-Entity Financial Consolidation & Variance Analysis Agent)** and pairs with the blank template at [AIImpactAssessment.md](../Templates/AIImpactAssessment.md). For each **Gateway 2** agent:

1. **Drafting by Business Unit & Builder**: Have the Business Unit `Decision Owner` and internal `L200/L300` builder complete **Sections 2 through 4** during agent design (`Phase 2`) and attach the **Golden Dataset Evaluation Report** (`>= 85%` groundedness) in **Section 2.5**.
2. **Internal AIIA Review:** The CoE convenes the Data Steward, InfoSec Reviewer, and Legal Counsel to walk through the residual risk controls (**Section 2.4**), the Measurable RAI test results (**Section 2.5**), and the OWASP `LLM01`-`LLM10` checklist (**Section 3**), recording formal sign-off in **Section 4** before production deployment.

## 2. Reference AIIA Baseline: Multi-Entity Financial Consolidation & Variance Agent (`UC-004`)

### 2.1 Use Case Summary

| Field | Reference Template Response (Customize for Each Tier 2-4 Agent) |
| :--- | :--- |
| **Use Case ID & Name** | `UC-004` - Multi-Entity Financial Consolidation & Monthly Variance Commentary Agent |
| **Business Owner (`Decision Owner`)** | `<Corporate Financial Controller / CFO Office Representative>` |
| **Technical Owner** | `<Enterprise AI Engineering Lead>` |
| **AI / Model Platform** | **Enterprise AI Platform & Enterprise Agent Runtime (Code-First Agent SDK)** - Frontier Reasoning Model Tier + Code Execution / Read-Only MCP |
| **Intended Users** | Authorized Financial Controllers and FP&A Leads (`<SG-AI-Finance-Controllers>`) |
| **People / Entities Affected** | Internal Finance leadership, business unit controllers, and executive management reviewing monthly financial performance |
| **Assigned Risk Tier** | **Tier 3 (High Risk)** - processes `D4 Restricted` financial trial balances and variance explanations |
| **Use Case Category** | `Analysis / Augmentation` (**Stage 2 Human Augmentation with Mandatory HITL**) |
| **Current Lifecycle Phase** | `Phase 1: Discover & Scope` -> `Phase 2: Pilot & Validate` -> `Phase 3: Deploy` |

### 2.2 Purpose, Decision Role & Human Accountability

| Assessment Question | Reference Template Response |
| :--- | :--- |
| **What business problem is being solved?** | Eliminates repetitive Thin Work spent manually reconciling multi-entity ERP trial balance exports, calculating currency/volume/price variances across `>500,000`-word spreadsheets, and drafting initial monthly variance commentary. |
| **Why is AI + Code Execution appropriate?** | Standard text-only RAG truncates spreadsheets exceeding 500,000 words. Combining **Code-First Agent SDK** deterministic Python/SQL calculation tools with **Frontier Reasoning Model Tier** grounded synthesis ensures 100% arithmetic accuracy alongside cited narrative explanations. |
| **What decisions does the output influence?** | Monthly management reporting, business unit budget variance reviews, and executive financial commentary packages. |
| **Is the system advisory, approval-gated, or autonomous?** | **Approval-Gated (`Stage 2 Strict HITL`)**: The agent operates in read-only mode against approved financial exports and drafts variance tables and commentary. It has **zero write access** to post journal entries or modify ERP ledgers. |
| **Named Human Accountable (`AIDecisionRegister`)** | **Corporate Financial Controller** (`ADR-004` in `AIDecisionRegister`, [AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)). Every generated variance report must be reviewed and signed off by the accountable controller against source trial balances before distribution. |

### 2.3 Data & Knowledge Inputs (`D1`-`D5`)

| Data / Knowledge Source | Classification Tier | Grounding or Training? | Data Owner | Access & Perimeter Controls | Retention & Deletion Policy |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Monthly Trial Balance & Variance Exports** (Enterprise ERP / Data Lakehouse) | **`D4 Restricted`** | **Inference-Time Grounding / Read-Only Tool Query Only** (Zero Model Training) | Corporate Finance Data Steward | Per-user IdP OAuth 2.0 + Entity RBAC; Private Network Perimeter (VPC / Private Link); CMEK encryption. | Zero training retention; session logs retained per corporate finance audit policy. |
| **Corporate Accounting Policies & Chart-of-Accounts Manual** | **`D3 Confidential`** | **Inference-Time Grounding** (Curated Finance Workspace / Index) | Accounting Policy Lead | Restricted to `<SG-AI-Finance-Controllers>` security group. | Updated quarterly upon accounting standard revisions. |

### 2.4 Risk Identification & Residual Risk Assessment

| Risk Domain | Specific Enterprise Failure Scenario | Inherent Impact | Inherent Likelihood | Mandatory Technical & Operational Controls | Residual Risk |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **1. Arithmetic or Factual Hallucination** | LLM miscalculates a budget variance or fabricates a business driver explanation without underlying source evidence. | High | Medium | Route all numerical aggregations through deterministic Python Code Execution / SQL tools (never free-text LLM math); require inline citations to source rows; enforce `>= 90%` groundedness on 100-sample Financial Golden Dataset. | **Low** |
| **2. Cross-Entity Data Leakage** | A regional analyst in Business Unit A queries confidential margin or pricing data belonging to Business Unit B. | High | Low | Enforce strict per-user IdP OAuth 2.0 identity propagation and row/folder-level ACL inheritance; run cross-entity negative access test prior to launch. | **Low** |
| **3. Unauthorized ERP Modification (Excessive Agency)** | Agent modifies a live ERP ledger or triggers an unauthorized transaction workflow. | High | Low | Configure all database/MCP connections with **strict read-only service credentials**; zero write/delete API tools exposed to the agent (`Gateway 2`). | **Low** |
| **4. External B2B Guest or Unlicensed Access** | An external vendor or contractor guest account in the corporate directory accesses the internal finance agent. | High | Low | Enforce external B2B guest exclusion (`userType EQUALS 'Member' AND accountEnabled EQUALS 'True'` + explicit security group assignment). | **Low** |

### 2.5 Measurable Responsible AI (RAI) Evidence Package

| RAI Principle | Applicable? | Measurable Engineering Target / Threshold | Verification Artifact & Pre-Launch Test |
| :--- | :---: | :--- | :--- |
| **1. Reliability & Safety** | **Yes** | **Groundedness `>= 90%`**, **Answer Relevance `>= 90%`**, **Arithmetic Accuracy `= 100%`** on the 100-sample Financial Golden Dataset. | **Automated AI Evaluation Pipeline** benchmark report stored in non-prod validation folder. |
| **2. Privacy & Data Isolation** | **Yes** | **Cross-Entity Unauthorized Retrieval Rate `= 0.0%`** across 50 negative-access test prompts. | InfoSec / Enterprise IT penetration test log verifying User A cannot retrieve Business Unit B `D4` files. |
| **3. Transparency & Explainability** | **Yes** | **`100%` of narrative variance claims** include clickable source table/document citations; clear UI banner stating *"AI-Generated Draft - Requires Controller Verification"*. | UI inspection screenshot and citation accuracy audit during User Acceptance Testing (UAT). |
| **4. Accountability** | **Yes** | Named human `Decision Owner` logged in `AIDecisionRegister` (`ADR-004`); Immutable Audit Logs of all prompts and tool calls; **90-day tested kill-switch**. | Signed `AIDecisionRegister` row + kill-switch drill log (`KSD-003` in [AIAF-DOC-06](06_AISecurityIncidentAndKillSwitchRunbook.md)). |
| **5. Fairness** | **Yes** | Consistent analysis accuracy across all regional business unit reporting formats and currencies. | Multi-region slice evaluation across representative business unit sample exports. |
| **6. Inclusiveness** | **Yes** | Accessible output tables and standardized plain-language executive commentary readable by global stakeholders. | UAT review by regional business unit representatives. |

## 3. Enterprise OWASP Top 10 for LLM Applications (`LLM01`-`LLM10`) Control Matrix

| OWASP LLM Risk | Enterprise Threat Scenario | Mandatory Platform & Identity Provider Control | Verification Status |
| :--- | :--- | :--- | :---: |
| **`LLM01` Prompt Injection** | Malicious text embedded in an external vendor PDF, invoice, or web page attempts indirect prompt injection to override agent instructions. | Enable **Runtime AI Guardrail Service** inline prompt-injection and jailbreak screening; isolate system instructions from untrusted retrieved document chunks. | **`<Verified / Pending>`** |
| **`LLM02` Sensitive Information Disclosure** | Accidental exposure of `D4` contract pricing, employee PII, or M&A data in responses or training pipelines. | Contractual zero model training guarantee; **Private Network Perimeter (VPC / Private Link)**; **CMEK** encryption; per-user IdP OAuth 2.0 source ACL enforcement. | **`<Verified / Pending>`** |
| **`LLM03` Supply Chain Vulnerabilities** | Unverified third-party plugins, unpinned model weights, or unapproved open-source packages in custom agents. | Restrict models to enterprise-governed **Fast / Lightweight and Frontier Reasoning model endpoints** on the approved AI platform; deploy custom code exclusively via reviewed CI/CD pipelines. | **`<Verified / Pending>`** |
| **`LLM04` Data and Model Poisoning** | Tampered or outdated draft SOPs uploaded into shared grounding folders distort agent answers. | Restrict curation of **Departmental Knowledge Workspaces** and authoritative grounding buckets to designated **CoE Champions** and Data Stewards ([AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)). | **`<Verified / Pending>`** |
| **`LLM05` Improper Output Handling** | Unsanitized LLM output passed directly into downstream SQL queries or scripts. | Enforce strict typed tool schemas in the **Code-First Agent SDK**; parameterize all read-only queries; never execute raw LLM-generated shell/SQL strings against prod. | **`<Verified / Pending>`** |
| **`LLM06` Excessive Agency** | An agent executes state-changing writes, approvals, or deletions in ERP, ITSM, or document stores without human oversight. | **Strict Read-Only OAuth/MCP scopes** for all standard and departmental connectors; mandatory **Human-in-the-Loop (HITL)** confirmation gate for any future action tools. | **`<Verified / Pending>`** |
| **`LLM07` System Prompt Leakage** | Users or external inputs extract proprietary system instructions or internal routing logic from an agent. | Zero credentials or secrets in system prompts; enforce IAM authentication at the tool/API layer rather than relying on prompt secrecy; Runtime AI Guardrail output filtering. | **`<Verified / Pending>`** |
| **`LLM08` Vector & Embedding Weaknesses** | Embeddings from multiple business units or subsidiaries mixed in a single index without ACL metadata filtering. | Enforce document-level ACL inheritance in **Enterprise Grounded Search** and tenant/entity-isolated vector namespaces. | **`<Verified / Pending>`** |
| **`LLM09` Misinformation & Hallucination** | Fabricated technical procedures, compliance rules, or legal clauses acted upon by staff. | Mandatory clickable inline citations; configure abstention instructions when retrieved confidence is low; validate via **25-100 sample Golden Datasets**. | **`<Verified / Pending>`** |
| **`LLM10` Unbounded Consumption** | Runaway multi-agent loops or massive batch jobs exhausting shared organizational token quotas. | Enforce `max_steps <= 10` recursion caps on custom agents; enable **Prompt / Context Caching** (`>32k` tokens); monitor project quota usage via Platform Observability alerts ([AIAF-DOC-09](09_ValueRealizationAndSeatGovernanceSOP.md)). | **`<Verified / Pending>`** |

## 4. AIIA Sign-Off & Scheduled Review Trigger

| Governance Role | Reviewer Name / Title | Decision (`Approved / Conditional / Rejected`) | Sign-Off Date | Review Cadence |
| :--- | :--- | :---: | :---: | :---: |
| **Business Owner (`Decision Owner`)** | `<Financial Controller / BU Lead Name>` | `<Pending / Approved>` | `<Sign-Off Date>` | `Quarterly` |
| **Data Steward** | `<Domain Data Steward Name>` | `<Pending / Approved>` | `<Sign-Off Date>` | `Quarterly` |
| **Information Security Reviewer** | `<InfoSec / CISO Representative Name>` | `<Pending / Approved>` | `<Sign-Off Date>` | `Quarterly` |
| **AI Governance / CoE Lead** | `<AI CoE Lead Name>` | `<Pending / Approved>` | `<Sign-Off Date>` | `Quarterly` |

- **Mandatory Re-Review Triggers**: Any upgrade from Read-Only to Write-Capable tools, change in underlying `D4/D5` data sources, groundedness drop below `85%`, or security incident.

> **Technical Alignment Note (Inline Guardrail API Integration for Custom Code-First Agents):** Built-in guardrail and content-safety toggles configured in a SaaS AI platform's administrative UI typically protect native out-of-the-box assistant surfaces, and often do **not** automatically wrap custom code-first agents hosted on external or standalone agent runtimes. To enforce equivalent `LLM01` and `LLM02` protections on custom code-first agents, developers must invoke the **Inline Prompt & Output Guardrail API** explicitly inside the agent runtime's `before_model` and `before_tool` (or equivalent pre-inference and pre-tool) callback hooks, and propagate the authenticated caller's identity token from the AI gateway to enforce per-user access controls.

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Responsible AI Model, Measurable RAI Goals, AI Impact Assessment process, and OWASP LLM Top 10 Mapping.
- [AIImpactAssessment.md](../Templates/AIImpactAssessment.md): Standalone blank AI Impact Assessment template.
- [References](../References.md): Maintained catalog of regulatory, security, and standards links.
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/) and [OWASP GenAI Security Project](https://genai.owasp.org/): Official `LLM01` through `LLM10` risk taxonomy and mitigation controls.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): AI impact assessment and risk treatment requirements.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1): Trustworthy AI characteristics and quantitative assurance practices.
