<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 13 Operational Governance Registers (Decision, Tool & Data Dictionary) & GenAIOps Guide

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-13` (Operational Governance Registers & GenAIOps Guide) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Enterprise IT Governance, Information Security (CISO), Data Stewards, and Technical Delivery Leads |
| **Primary Internal Owner** | AI Center of Excellence (CoE) Operations Lead & Enterprise IT Governance Lead |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE) and internal teams maintain living operational governance registers and stand up continuous GenAIOps evaluation practices. It is **not** prescriptive. Sections include pre-structured baselines for the **AI Decision Register** ([AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv)), **Approved AI Tool Registry** ([ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv)), **Governance Data Dictionary** ([DataDictionary.md](../Templates/DataDictionary.md)), and **Golden Evaluation Dataset starter schemas** so teams do not have to start from a blank page. Organizations can share this template directly or adapt it to their internal governance model.

## 1. How the AI CoE Can Create, Customize & Maintain These Operational Registers

### 1.1 Purpose & Why This Document Exists

Static PDF policies quickly become outdated once thousands of employees and dozens of business units begin building prompts, knowledge workspaces, and agents. To prevent shadow deployments and maintain audit readiness across operating regions, the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) pairs three living operational registers ([AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv), [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv), and [DataDictionary.md](../Templates/DataDictionary.md)) with a continuous **GenAIOps Evaluation Flywheel**.

This document exists to solve three operational governance challenges for the AI Center of Excellence (CoE):

1. **Explicit Human Accountability (`AIDecisionRegister`)**: Tracks every business, operational, financial, legal, or employee decision influenced by AI across the enterprise, enforcing the rule that **every AI workflow must have a named human `Decision Owner` and `Human Accountable`** - never an AI agent or service principal.
2. **Clear Tool & Data Boundaries (`ApprovedAIToolRegistry`)**: Gives all employees and regional IT teams a single authoritative list of which AI platforms are **Approved**, **Conditional**, or **Prohibited**, mapped to allowed data classification tiers (`D1` to `D5`).
3. **Bridging Classical MLOps to Enterprise GenAIOps**: While many organizations have classical **MLOps** for predictive analytics or operational systems (where the unit of change is the *trained model weight*), corporate generative AI requires **GenAIOps**, where the unit of change is the **prompt template, retrieval index, and agent configuration** - verified continuously against curated **Golden Datasets**.

### 1.2 Who Normally Produces & Maintains These Registers Internally

- **Internal Register Custodian**: AI Center of Excellence (CoE) Operations Lead (within Enterprise IT / Digital Transformation).
- **Internal Contributors**:
  - **Business Unit Decision Owners**: Register new Tier 2+ workflows in `AIDecisionRegister` prior to Gateway 2 promotion.
  - **Information Security (CISO) & Procurement**: Update `ApprovedAIToolRegistry` when evaluating vendor AI features or MCP connectors ([AIAF-DOC-14](14_VendorAIProcurementChecklist.md)).
  - **CoE Champions & Technical Builders**: Maintain the 25-100 sample Golden Datasets and run **Automated AI Evaluation Pipeline** checks on prompt/index updates.
- **Review Cadence**: Reviewed monthly during initial rollout and quarterly thereafter by the AI CoE Steering Committee.

### 1.3 Recommended Approach: Running a Monthly CoE Governance & GenAIOps Cadence

1. **Stand Up the Live Registers (`Sections 2, 3 & 4`)**: Maintain `AIDecisionRegister` (**Table 2**) and `ApprovedAIToolRegistry` (**Table 3**) using the CSV templates ([AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv) and [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv)) and the controlled vocabulary in **Section 4** ([DataDictionary.md](../Templates/DataDictionary.md)), replacing role placeholders with named leaders for `ADR-001` through `ADR-006`.
2. **Curate Initial Golden Datasets During Early Access (`Section 5.3`)**: Have the **Early-Access CoE Champions** use the Golden Dataset starter schema in **Table 5.3** to compile 25 to 50 ground-truth Q&A pairs for their departmental SOP workspaces ([AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)).
3. **Run a Regular CoE Review:** On a regular cadence, the CoE Operations Lead convenes Business Unit Decision Owners, InfoSec, and Enterprise IT to (a) approve new rows in `AIDecisionRegister`, (b) review `ApprovedAIToolRegistry` requests, and (c) verify that all active Gateway 2 agents maintain `>= 85%` groundedness on their Golden Datasets.

## 2. Operational Register 1: Enterprise AI Decision Register (`AIDecisionRegister` Template Baseline)

> **Companion CSV Template:** [../Templates/AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv)

**Important: Mandatory Accountability Rule**: Every row in `AIDecisionRegister` must name a human **`Decision Owner`** and **`Human Accountable`**. An AI model, no-code agent app, or cloud service principal can never bear accountability for a business outcome.

| Decision ID | Decision Being Influenced | AI Tool / System | Use Case Name (`UC-ID`) | Decision Owner (Role) | Human Accountable (Role) | Risk Tier (`1`-`4`) | Category | Non-Human Actor Persona | Guardrails & Exception Handling | Sanctioned? | Status & Review Cadence |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| `ADR-001` | **Interpretation of Corporate Policies & Operational/Technical SOPs** | Enterprise Grounded Search & Grounded Knowledge Notebooks (`Gateway 1`) | `UC-001` Enterprise SOP Synthesis | Departmental Knowledge Curators | Business Unit Head / Operations Lead | **Tier 1 / Tier 2** (`D2/D3`) | Augmentation / Analysis | `Interactive AI Assistant` | Per-user IdP OAuth ACLs; mandatory clickable inline citations; user verifies underlying SOP document before operational action. | **Yes** | `Active` (Monthly Review) |
| `ADR-002` | **Market Intelligence, Competitor & ESG Strategic Briefings** | Enterprise Deep Research (`Gateway 1`) | `UC-003` Market & ESG Deep Research | Head of Corporate Strategy / Sustainability | Strategy / ESG Analyst Authoring Report | **Tier 1** (`D1/D2`) | Analysis / Generation | `Interactive AI Assistant` | Full bibliography and reasoning trace inspected by human analyst before executive or board distribution. | **Yes** | `Active` (Quarterly Review) |
| `ADR-003` | **Tier-1 IT & HR Employee Service Desk Policy Guidance & Ticket Triage** | **No-Code Agent Builder** (`Gateway 2`) | `UC-005` IT & HR Helpdesk Agent | Head of ITSM & Head of HR Operations | IT / HR Service Desk Duty Manager | **Tier 2** (`D2/D3`) | Automation / Augmentation | `Scoped Agent` | Read-only grounding on curated HR/IT workspaces; zero write access to ERP/HRIS; one-click *"Escalate to Human Specialist"* path. | **Yes** | `Active / Planned (Monthly Review)` |
| `ADR-004` | **Multi-Entity Financial Consolidation & Variance Commentary** | **Enterprise Agent Runtime (Code-First Agent SDK)** (`Gateway 2`) | `UC-004` Multi-Entity Finance Agent | Corporate Financial Controller | CFO Office / Regional Controller | **Tier 3** (`D4`) | Analysis / Augmentation | `Tool-Using Agent` | Deterministic Python/SQL math; read-only ERP/Lakehouse access; **mandatory human controller sign-off**; 90-day kill-switch drill. | **Yes** | `Planned (Monthly Review)` |
| `ADR-005` | **Enterprise Contract Obligation & Renewal Clause Review** | Scoped Legal Knowledge Workspace / Agent (`Gateway 2`) | `UC-007` Contract Obligation Reviewer | General Counsel | Regional / Commercial Legal Counsel | **Tier 3** (`D4`) | Analysis / Augmentation | `Scoped Agent` | Strict per-entity security group isolation; mandatory legal counsel review before commercial action. | **Yes** | `Planned (Quarterly Review)` |
| `ADR-006` | **Conversational Operational & Commercial KPI Analytics** | **Code-First Agent SDK** + Read-Only Lakehouse MCP (`Gateway 2`) | `UC-006` Conversational Analytics Agent | Head of Data & Analytics | Business Unit Operations Director | **Tier 2 / Tier 3** (`D3/D4`) | Analysis | `Tool-Using Agent` | Read-only OAuth 2.0 token passthrough enforcing catalog row/column ACLs; Golden SQL evaluation benchmark (`>= 85%`). | **Yes** | `Planned (Monthly Review)` |

## 3. Operational Register 2: Approved AI Tool Registry (`ApprovedAIToolRegistry` Template Baseline)

> **Companion CSV Template:** [../Templates/ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv)

| Tool ID | Tool / Platform Name | Vendor / Provider | Internal Owner | Approved Status | Approved Use Cases & Cohort | Prohibited Use Cases | Allowed Data Tiers (`D1`-`D5`) | Trains on Enterprise Data? | Enterprise Controls & Audit Logging | Review Cadence |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| `TOOL-001` | **Enterprise AI Platform (Standard Tier)** (Web Chat, Search, File Upload, Deep Research, Grounded Knowledge Notebooks) | `<Enterprise AI Platform Vendor>` | `<Enterprise IT Platform Lead>` | **`Approved`** | **All Licensed Users** + **CoE Champions**: `Gateway 1` daily productivity, document synthesis, Enterprise Deep Research, Grounded Knowledge Notebooks. | Uploading `D5 Regulated / Critical` live control data; sharing restricted workspaces outside authorized security groups. | **`D1` to `D3`** (`D4` only in ACL-isolated Workspaces) | **No** (Contractual Zero Training) | Corporate IdP SAML 2.0 + SCIM 2.0; External B2B Guest Filter; Immutable Audit Logs. | `Quarterly` |
| `TOOL-002` | **No-Code / Low-Code Agent Builder** | `<Enterprise AI Platform Vendor>` | `<Enterprise IT & AI CoE>` | **`Approved`** (`Gateway 1` Personal / `Gateway 2` Shared) | Personal workflow assistants (`Gateway 1`); CoE-approved departmental helpdesk & SOP agents (`Gateway 2`). | Publishing org-wide agents touching `D3/D4` data without `Gateway 2` 4-Stage HITL approval and Golden Dataset test. | **`D1` to `D3`** (`D4` requires `AIIA`) | **No** | Per-user IdP OAuth 2.0 ACL inheritance; Platform Admin Console sharing controls. | `Quarterly` |
| `TOOL-003` | **Code-First Agent SDK & Enterprise Agent Runtime** | `<Enterprise AI Platform Vendor>` | `<Enterprise AI Engineering Lead>` | **`Conditional`** (`Gateway 2` Only) | **Code-First Custom Agents** and `L300` technical builder workflows. | Autonomous write/delete actions in production ERP/ITSM without HITL gate; deployment without `P2P Gate` & `AIIA`. | **`D1` to `D4`** (per approved `AIIA`) | **No** | Private Network Perimeter (VPC / Private Link); CMEK; Runtime AI Guardrail Service; dedicated service principals; 90-day kill-switch. | `Quarterly` |
| `TOOL-004` | **Existing Productivity Suite In-App Assistants** (`<Productivity Suite AI Add-On>`) | `<Enterprise Productivity Suite Vendor>` | `<Collaboration Suite Admin>` | **`Approved`** (Scoped Cohort) | In-app document formatting and meeting recaps for existing licensed cohort. | Cross-platform multi-hop Deep Research or custom agent orchestration (use Enterprise AI Platform). | **`D1` to `D3`** | **No** | Corporate IdP tenant and DLP controls. | `Quarterly` |
| `TOOL-005` | **Internal Domain-Specific ML & Operational Systems** (`<Predictive Analytics / OT / Core Engineering ML>`) | `<Internal Data Science / Domain Vendor>` | `<Head of Domain Operations>` | **`Approved`** (Domain-Scoped) | Specialized predictive maintenance, demand forecasting, fraud detection, or industrial/operational control within isolated environments. | Mixing unredacted `D5` regulated or control commands into corporate cloud chat prompts. | **`D1` to `D5`** (within isolated boundary) | **No** (Internal Models) | Network segmentation and domain security architecture. | `Quarterly` |
| `TOOL-006` | **Unsanctioned Public Consumer AI Web Bots & Unverified Extensions** | Various Consumer Vendors | Prohibited by InfoSec | **`Prohibited`** (for Corporate Data) | Safe personal learning off corporate network using **`D1 Public` data only**. | **Strictly Prohibited** for any `D2`-`D5` enterprise data, corporate SSO login, source code, or meeting recording. | **`D1 Public` Only** | **Yes** (High Risk of Training Leakage) | Blocked/monitored via corporate web proxy; employee demand channeled to `TOOL-001`. | `Continuous` |

## 4. Operational Register 3: Governance Data Dictionary (`DataDictionary` Schema & Controlled Vocabularies)

> **Companion Markdown Spec:** [../Templates/DataDictionary.md](../Templates/DataDictionary.md)

| Register Field | Controlled Vocabulary / Allowed Values | Definition & Governance Rule |
| :--- | :--- | :--- |
| **`Record IDs`** | `ADR-001`..`ADR-999`, `UC-001`..`UC-999`, `TOOL-001`..`TOOL-999` | Zero-padded lexicographically sortable identifiers; never reuse an ID once retired. |
| **`Dates`** | `YYYY-MM-DD` (ISO 8601) | Mandatory ISO 8601 date format across all trackers, registers, and audit logs. |
| **`Data Classification`** | `D1 Public`, `D2 Internal`, `D3 Confidential`, `D4 Restricted`, `D5 Regulated / Critical` | Defined in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) and [AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md); if a dataset contains both `D3/D4` and statutory `D5` elements, apply both labels. |
| **`Risk Tier`** | `Tier 1 (Low)`, `Tier 2 (Medium)`, `Tier 3 (High)`, `Tier 4 (Critical)` | `Tier 1`: Internal `D1/D2` read-only assistance; `Tier 2`: Departmental `D2/D3` scoped agents; `Tier 3`: High-impact `D4` financial/legal/customer workflows (`AIIA` mandatory); `Tier 4`: Autonomous or `D5` regulated actions. |
| **`Use Case Category`** | `Augmentation`, `Analysis`, `Generation`, `Automation`, `Agency` | Standard AIAF functional taxonomy used in `AIUseCaseCard` ([AIAF-DOC-08](08_AIUseCaseIntakeAndPortfolioBacklog.md)) and `AIDecisionRegister`. |
| **`Gateway Path`** | `Gateway 1 (Self-Service)` vs. `Gateway 2 (Enterprise Controlled)` | `Gateway 1` is bounded by per-user IdP OAuth permissions; `Gateway 2` requires 4-stage HITL sign-off (`Intake -> Security/ACL -> Golden Dataset Eval -> Decision Register`). |
| **`Non-Human Actor Persona`** | `Interactive AI Assistant`, `Scoped Agent`, `Service Agent`, `Tool-Using Agent`, `Multi-Agent System` | Defined in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) Section 4; dictates identity principal rules and 90-day kill-switch testing. |

## 5. Bridging Classical MLOps to Enterprise GenAIOps (Operational Playbook Summary)

### 5.1 How Enterprise GenAIOps Differs from Classical MLOps

| Operational Dimension | Classical Predictive MLOps (Forecasting, Scoring, Industrial ML) | Enterprise GenAIOps (Enterprise AI Platform, Knowledge Workspaces, Custom Agents) |
| :--- | :--- | :--- |
| **Primary Unit of Change** | **Trained Model Weights & Feature Pipelines** (retrained monthly or quarterly by data scientists). | **Prompts, Grounding Indexes (`Workspaces/Indexes`), and Agent Tool Configs** (updated daily or weekly by champions and engineers). |
| **Primary Failure Mode** | Statistical feature drift or sensor/distribution shift. | Retrieval snippet truncation, stale source documents, prompt regressions, or cross-department ACL misconfiguration. |
| **Quality Assurance Gate** | Hold-out test set precision / recall / RMSE before weight deployment. | **25-100 Sample Golden Evaluation Dataset** scored via **Automated AI Evaluation Pipeline** (`Groundedness >= 85%`, `Relevance >= 90%`). |
| **Runtime Security Boundary** | Isolated analytics or operational network environment. | **Corporate IdP SAML/SCIM**, **Per-User OAuth 2.0 Source ACLs**, **Runtime AI Guardrail Service**, and **2-Gateway HITL Governance** (`D1`-`D4`). |

### 5.2 The 3-Step GenAIOps Continuous Evaluation Flywheel

```
+-----------------------------------------------------------------------+
|          ENTERPRISE 3-STEP GenAIOps CONTINUOUS EVAL FLYWHEEL          |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 1: CURATE GOLDEN EVALUATION DATASET                             |
|  * CoE Champions & BU SMEs compile 25 to 50 Q&A pairs for priority    |
|    departmental SOPs (and 100 Q&A pairs for code-first custom agents).|
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 2: AUTOMATED PRE-DEPLOYMENT EVALUATION GATE                     |
|  * Run Automated AI Evaluation Pipeline whenever a prompt, Knowledge  |
|    Workspace corpus, or model changes (Groundedness >= 85% gate).     |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 3: PRODUCTION TELEMETRY, DRIFT MONITORING & FEEDBACK LOOP       |
|  * Track 3-Tier KPI Matrix (Adoption, Efficiency, Quality) & 60-day   |
|    seat usage; convert thumbs-down traces into new Golden Test cases. |
+-----------------------------------------------------------------------+
```

### 5.3 Golden Dataset Starter Schema for CoE Champions (`25-50 Q&A Pairs`)

| Test Case ID | Domain / Workspace Corpus | Representative User Prompt | Authoritative Source Document & Page/Section | Required Ground-Truth Facts in Answer | Pass Criteria (`Groundedness & Citation`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GLD-001` | Operations & Engineering SOPs | *"What is the preventive maintenance inspection interval and safety lockout procedure for `<Equipment / System Type A>` under high-load operations?"* | `<Engineering_Maintenance_Manual_v4.pdf>` (Section 6.2, Table 4) | Must state exact interval and lockout sequence from Table 4 without conflating standard vs. high-load rows. | Groundedness `= 1.0`; clickable citation to Section 6.2 Table 4. |
| `GLD-002` | Corporate HR & Travel Policy | *"What is the approval hierarchy and daily meal reimbursement limit for a `<Band / Level>` employee traveling internationally for a 5-day audit?"* | `<Global_Business_Travel_Policy.pdf>` (Section 3.1 & Appendix B) | Must cite applicable regional per-diem rate and Department Head pre-approval requirement. | Groundedness `= 1.0`; zero fabrication of unstated allowances. |
| `GLD-003` | Corporate Finance Variance (`Code-First Agent #1`) | *"Summarize the top 3 operating expense variance drivers for Q3 across regional business units and show exact percentage changes."* | `<Regional_Q3_Trial_Balance_Export.csv>` | Deterministic Python/SQL calculation of top 3 OPEX deltas (`100%` arithmetic match) + cited commentary. | Arithmetic error `= 0%`; Groundedness `>= 0.90`. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): AI Operations & Quality Perspective, GenAIOps vs. MLOps, AI Decision Register, and GenAIOps & Agent Outcomes KPIs.
- [AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv): Standalone CSV template for the Enterprise AI Decision Register.
- [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv): Standalone CSV template for the Approved AI Tool Registry.
- [DataDictionary.md](../Templates/DataDictionary.md): Column definitions, controlled values, and conversion guidance for CSV registers.
- [References](../References.md): Maintained catalog of regulatory, security, and operational references.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Continuous monitoring, measurement, and accountability tracking.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Operational documentation, system inventories, and ongoing evaluation controls.
