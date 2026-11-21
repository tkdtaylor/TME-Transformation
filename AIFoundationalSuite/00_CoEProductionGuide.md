<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 00 AI Adoption Framework: Foundational Documents & CoE Production Guide

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-00` (Master Overview & CoE Production Guide - 14-Document Suite) |
| **Document Version** | `v2.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Digital Transformation Leadership, Enterprise IT Architecture, Information Security (CISO), Legal, Procurement, Finance, and Business Unit Sponsors |
| **Primary Internal Owner** | AI Center of Excellence (CoE) Lead & Digital Transformation Lead |
| **Document Status** | Master Reference Guide & Reusable Template Catalog (Ordered by Operational Priority `01` to `14` Across 4 Tiers) |

**Note: Reference Template & Non-Prescriptive Accelerator Notice:** This guide and the 14 companion documents (`01` through `14`) in this folder are provided as **reusable templates and optional starting baselines** to help an organization's AI Center of Excellence (CoE) and internal teams build and scale their own AI governance, security, and operational capabilities. **These templates are non-prescriptive.** Sections have been pre-populated with representative enterprise patterns so your teams do not have to start from a blank page. Every document also includes a self-contained production guide at the top in case it is shared independently without this master guide. Internal teams should freely adapt, consolidate, replace, or discard any section to fit their governance model. Pair these documents with the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) and the standalone blank forms in [Templates](../Templates/README.md).

## 1. Executive Summary: Purpose & Priority Ordering of This 14-Document Suite

Scaling enterprise artificial intelligence across global knowledge workers and power-user champions requires more than provisioning licenses and configuring cloud infrastructure. Organizations that achieve sustained, auditable business value pair their technical rollout with a clear set of **Foundational & Operational AI Governance Documents** owned and maintained by their internal **AI Center of Excellence (CoE)** in partnership with Information Security, Enterprise IT, Legal, Procurement, Finance, and Business Unit leaders.

This folder provides a complete, **14-document reference template suite (`01` through `14`)** anchored on the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) and sequenced in **chronological operational priority across four execution tiers**:

- **Tier 1 (`01` to `04`) - Day-0 Executive Mandate & Core Data / Workforce Guardrails (Pre-Launch & Initial Go-Live):** Highest blast-radius governance that aligns executive leadership (`01 Strategy Charter`), establishes binding corporate policy and `D1-D5` data tiers (`02 Enterprise AI Policy`), maps `D1-D5` across AI tool surfaces and core data repositories (`03 Data Classification Matrix & Source Register`), and equips every employee with a 1-page Traffic-Light Acceptable Use card (`04 Employee AUP`) on Day 1.
- **Tier 2 (`05` to `08`) - Wave-1 Value Enablement, Emergency Safety Net & Use-Case Selection (Early Access & Initial Rollout):** Drives immediate Day-1 productivity through Champion-curated departmental workspaces (`05 Knowledge Notebook & Prompt Curation Playbook`), gives InfoSec/SOC a `<15-minute` emergency shutoff for live connectors (`06 Incident Response & Kill-Switch Runbook`), decomposes *Thin Work* vs. *Valued Work* across business capabilities (`07 Strategic Drivers & Thin-vs.-Valued Work`), and ranks candidate workflows (`08 Use Case Intake & Scored Portfolio Backlog`).
- **Tier 3 (`09` to `10`) - FinOps Seat Governance & Capability Maturity Roadmap (Post-Launch Adoption & Seat Governance):** Protects license utilization across the seat pool via automated 30/45/60-day seat reclamation and finance-verified ROI telemetry (`09 Value Realization, FinOps & 60-Day Seat SOP`), and tracks programmatic readiness across all 7 AIAF perspectives (`10 AI Maturity Scorecard & 20-Item Readiness Roadmap`).
- **Tier 4 (`11` to `14`) - Custom Agent Production Gates, Deep Risk, GenAIOps & Vendor Procurement (Custom Agent Rollout & Ongoing Operations):** Governs custom code-first agents and Gateway 2 connectors moving from sandbox to production (`11 Pilot-to-Production [P2P] Gate`), evaluates high-risk or regulated agent workflows against falsifiable RAI metrics and OWASP `LLM01-LLM10` (`12 AI Impact Assessment [AIIA]`), maintains Day-2 operational governance registers and Golden Dataset regression testing (`13 Operational Registers & GenAIOps Guide`), and blocks shadow SaaS AI sprawl (`14 Third-Party SaaS & Vendor AI Procurement Checklist`).

### How an Organization's AI CoE Should Use These Templates

1. **Non-Prescriptive Starting Point (Zero "Blank Page" Friction):** Each document (`01` to `14`) is pre-populated with realistic, industry-agnostic enterprise baselines (covering corporate functions such as Finance, Legal, HR, IT, Procurement, and Strategy alongside core operations) and aligned with reference enterprise production architectures (**Synchronized Enterprise Identity** with SAML 2.0 SSO & SCIM 2.0, **2-Gateway agent governance**, and **4-Tier Hybrid Grounding**). They can be shared directly as-is or used as a base to generate industry- or organization-specific versions.
2. **Self-Contained Opening Production Guide in Every Document:** Section 1 of every document explains **what the document is**, **which internal role normally owns and produces it**, **why it exists**, and **how the CoE can co-create or customize it internally** (for example, by running a focused internal working session with specified stakeholders).
3. **Single Source of Truth per Topic (Zero Unnecessary Duplication):** Each document owns one distinct governance artifact and cross-references companion documents for adjacent details.
4. **Chronological Priority Flow (`01` -> `14`):** Documents are numbered in the exact order an AI CoE establishes them, starting with Day-0 executive and workforce guardrails (`01` to `04`) before advancing to Wave-1 enablement (`05` to `08`), Day 30-60 FinOps and maturity tracking (`09` to `10`), and Wave 2+ custom agent production gates (`11` to `14`).

## 2. Master Directory of the 14 Foundational & Operational Template Documents (Ordered `01` to `14`)

All 14 template documents reside alongside this guide in the [AI Foundational Suite](README.md) folder:

| Doc # | Document Title & Direct Link | When to Establish | Typical Internal Owner | Priority & Impact Rationale |
| :---: | :--- | :--- | :--- | :--- |
| **TIER 1** | **DAY-0 EXECUTIVE MANDATE & CORE DATA / WORKFORCE GUARDRAILS (`01` to `04`)** | **Pre-Launch & Initial Go-Live** | **Executive Sponsors, CISO, IT & CoE** | **Highest blast-radius governance: aligns leadership, locks data boundaries, and protects all employees on Day 1.** |
| **`01`** | [01 Enterprise AI Strategy Charter & Public AI Trust Statement](01_EnterpriseAIStrategyCharter.md) (`AIAF-DOC-01`) | **Phase 0 (Pre-Launch)** | Executive Sponsors, Digital Transformation & Corporate Comms | **#1 Strategic Foundation:** Sets the executive North Star, the 8 strategic trade-off rules (`STR-01` to `STR-08`) that guide all downstream AI decisions, and approved external customer/partner trust messaging. |
| **`02`** | [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`) | **Phase 0 (Pre-Launch)** | CISO / InfoSec, Data Protection Officer (DPO), Head of IT & AI CoE Lead | **#1 Corporate Governance Gate:** Establishes the binding corporate AI policy, defines the `D1-D5` data sensitivity tiers, and sets Non-Human Actor (`NHA-01` to `NHA-05`) autonomy rules before production access opens. |
| **`03`** | [03 AI Data Classification Matrix & Enterprise Data Source Control Register](03_DataClassificationMatrixAndSourceRegister.md) (`AIAF-DOC-03`) | **Phase 0 (Connector Setup)** | CISO / InfoSec, Enterprise Data Governance & System Owners | **Direct Operationalization of `02`:** Maps `D1-D5` across 10 AI tool surfaces and registers 12 core enterprise systems (`SRC-001` to `SRC-012`) so IT knows immediately what can connect on Day 1 vs. what is off-limits (`D5 Regulated/OT`). |
| **`04`** | [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md) (`AIAF-DOC-04`) | **Initial Go-Live (Day 1)** | AI CoE, HR, Internal Comms & InfoSec | **Highest Workforce Impact:** Translates `02` and `03` into a 1-page `GREEN / AMBER / RED` Do/Don't desk reference, 5 Golden Rules, and onboarding sign-off that every employee reads during Day-1 (`L100`) onboarding. |
| **TIER 2** | **WAVE-1 VALUE ENABLEMENT, EMERGENCY SAFETY NET & USE-CASE SELECTION (`05` to `08`)** | **Early Access & Initial Rollout** | **AI CoE, BU Champions, SOC & Strategy** | **Drives immediate Day-1 user adoption, gives InfoSec an emergency shutoff, and prioritizes high-value use cases.** |
| **`05`** | [05 Departmental Knowledge Notebook & Prompt Library Curation Playbook & Asset Catalog](05_KnowledgeNotebookAndPromptPlaybook.md) (`AIAF-DOC-05`) | **Phase 0 Early Access (Champions)** | AI CoE Enablement Lead & BU Champions (`L200`) | **#1 Immediate Productivity Driver:** Needed during Champion Early Access so CoE Champions curate certified Departmental Knowledge Workspaces (`CAT-001` to `CAT-008`) and `R-C-T-V` prompts before general users log in. |
| **`06`** | [06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook](06_AISecurityIncidentAndKillSwitchRunbook.md) (`AIAF-DOC-06`) | **Initial Go-Live** | CISO / SOC Incident Response, AI CoE & IT Operations | **Operational Safety Net for Live Connectors:** Gives InfoSec/SOC and Enterprise IT a `<15-minute` 5-layer emergency shutoff (`SEV-1` to `SEV-4` + quarterly drills `KSD-001` to `KSD-004`) as soon as live enterprise connectors are enabled. |
| **`07`** | [07 Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment](07_StrategicDriversAndThinValuedWork.md) (`AIAF-DOC-07`) | **Initial Rollout (CoE Discovery)** | AI CoE Lead & Strategy / Digital Transformation Lead | **Business Work-Redesign Foundation:** Once Day-1 guardrails and notebooks are live, the CoE uses this (`DRV-01..14`, `CAP-01..10`) to identify repetitive *Thin Work* to automate away in favor of high-judgment *Valued Work*. |
| **`08`** | [08 AI Use Case Intake Cards & Scored Portfolio Backlog](08_AIUseCaseIntakeAndPortfolioBacklog.md) (`AIAF-DOC-08`) | **Initial Rollout (Agent Prioritization)** | AI CoE Intake Lead & Business Unit Champions | **Portfolio Prioritization:** Directly follows `07` to score and rank departmental and code-first custom agent candidates (`UC-001` to `UC-010`) across 6 weighted dimensions so engineering builds the highest-ROI agents first. |
| **TIER 3** | **FINOPS SEAT GOVERNANCE & CAPABILITY MATURITY ROADMAP (`09` to `10`)** | **Post-Launch Adoption & Seat Governance** | **AI CoE, Finance, Identity Admin & Steering Committee** | **Protects license utilization across the seat pool, proves hard ROI, and tracks quarterly capability maturity.** |
| **`09`** | [09 AI Value Realization, FinOps & 60-Day License Governance SOP](09_ValueRealizationAndSeatGovernanceSOP.md) (`AIAF-DOC-09`) | **Post-Launch Seat Review** | AI CoE Program Lead, Finance & Identity Admin | **Seat Utilization & ROI Proof:** Active by Post-Launch Seat Review to run automated Day 30/45 nudges, reclaim 60-day inactive seats, enforce 11 FinOps levers, and track verified ROI KPIs (`VAL-01` to `VAL-04`) for Finance. |
| **`10`** | [10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap](10_AIMaturityScorecardAndReadinessRoadmap.md) (`AIAF-DOC-10`) | **Recurring Governance Cadence** | AI CoE Steering Committee & Head of Enterprise IT | **Programmatic Maturity Benchmark:** Scores the organization across all 7 AIAF perspectives (`1: Exploring` to `4: Transforming`) and the 20-Item Readiness Checklist (`CHK-01` to `CHK-20`), sequencing the quarterly capability roadmap. |
| **TIER 4** | **CUSTOM AGENT PRODUCTION GATES, DEEP RISK, GENAIOPS & VENDOR PROCUREMENT (`11` to `14`)** | **Custom Agent Rollout & Ongoing Operations** | **Cloud Platform, InfoSec, AI Engineering & Procurement** | **Governs custom code-first agents moving from sandbox to production, high-risk compliance, and external SaaS requests.** |
| **`11`** | [11 Pilot-to-Production (P2P) Gate Review Package](11_PilotToProductionGatePackage.md) (`AIAF-DOC-11`) | **Pre-Production Custom Agent Launch** | AI CoE Lead, Cloud Platform Lead & InfoSec Lead | **Custom Agent Production Gate:** Required before promoting custom code-first agents (`UC-004`, `UC-006`) or Gateway 2 connectors from sandbox into production across 10 readiness dimensions (`>= 85%` Golden Dataset pass rate). |
| **`12`** | [12 AI Impact Assessment (AIIA), Measurable RAI & OWASP LLM Controls](12_AIImpactAssessmentAndOWASPControls.md) (`AIAF-DOC-12`) | **Custom Agent Rollout (High-Risk Use Cases)** | BU Use-Case Owner & AI Governance / InfoSec Reviewer | **Deep Risk & Regulatory Gate:** Triggered for medium/high-risk or regulated agent use cases (`Tier 2-4`, illustrated for `UC-004` Finance Agent) requiring falsifiable RAI thresholds and OWASP `LLM01-LLM10` control verification. |
| **`13`** | [13 Operational Governance Registers (Decision, Tool & Data Dictionary) & GenAIOps Guide](13_OperationalGovernanceRegistersAndGenAIOps.md) (`AIAF-DOC-13`) | **Ongoing Operations (Sustained Scale)** | AI CoE Operations Lead & Enterprise IT Governance Lead | **Day-2 GenAIOps & Fleet Operations:** Maintains living governance registers (`AIDecisionRegister`, `ApprovedAIToolRegistry`, `DataDictionary`) and the 3-step Golden Dataset evaluation flywheel to prevent silent model/prompt drift. |
| **`14`** | [14 Third-Party SaaS & Vendor AI Procurement Assessment Checklist](14_VendorAIProcurementChecklist.md) (`AIAF-DOC-14`) | **Ongoing Procurement Gate** | Procurement, CISO / InfoSec, Legal & AI CoE | **External Vendor Filter (`VND-001` to `VND-010`):** Used by Procurement, Legal, and InfoSec whenever a BU requests an external SaaS AI add-on to block shadow data training and avoid paying twice for core platform capabilities. |

## 3. How the 14 Documents Fit Together Across the 4-Tier AI CoE Rollout Lifecycle

The diagram below illustrates the chronological `00 -> 14` priority flow across the four operational tiers:

```
+-----------------------------------------------------------------------+
|   ENTERPRISE AI CENTER OF EXCELLENCE (CoE) 14-DOCUMENT PRIORITY FLOW  |
+-----------------------------------------------------------------------+
|                                                                       |
|  TIER 1: DAY-0 EXECUTIVE MANDATE & CORE DATA / WORKFORCE GUARDRAILS   |
|  +-----------------------------------------------------------------+  |
|  | [Doc 01] Enterprise AI Strategy Charter & Public Trust Statement|  |
|  | [Doc 02] Enterprise AI Policy (D1-D5) & Non-Human Actor Standard|  |
|  | [Doc 03] Data Classification Matrix & Source Control Register   |  |
|  | [Doc 04] Employee AI Acceptable Use Policy (Traffic-Light Guide)|  |
|  +-----------------------------------------------------------------+  |
|                                   |                                   |
|                                   v                                   |
|  TIER 2: WAVE-1 ENABLEMENT, SAFETY NET & USE-CASE PRIORITIZATION      |
|  +-----------------------------------------------------------------+  |
|  | [Doc 05] Knowledge Notebook & Prompt Curation Playbook          |  |
|  | [Doc 06] AI Incident Response & 90-Day Kill-Switch Drill Runbook|  |
|  | [Doc 07] Strategic Drivers, Capabilities & Thin-vs.-Valued Work |  |
|  | [Doc 08] AI Use Case Intake Cards & Scored Portfolio Backlog    |  |
|  +-----------------------------------------------------------------+  |
|                                   |                                   |
|                                   v                                   |
|  TIER 3: DAY 30-60 FINOPS SEAT GOVERNANCE & MATURITY ROADMAP          |
|  +-----------------------------------------------------------------+  |
|  | [Doc 09] Value Realization, FinOps & 60-Day Seat Governance SOP |  |
|  | [Doc 10] AI Maturity Scorecard, 20-Item Checklist & Roadmap     |  |
|  +-----------------------------------------------------------------+  |
|                                   |                                   |
|                                   v                                   |
|  TIER 4: CUSTOM AGENT P2P GATES, DEEP RISK, GENAIOPS & PROCUREMENT    |
|  +-----------------------------------------------------------------+  |
|  | [Doc 11] Pilot-to-Production (P2P) 10-Dimension Gate Package    |  |
|  | [Doc 12] AI Impact Assessment (AIIA), Measurable RAI & OWASP    |  |
|  | [Doc 13] Operational Registers (Decision, Tool, Data) & GenAIOps|  |
|  | [Doc 14] Third-Party SaaS & Vendor AI Procurement Checklist     |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

## 4. Detailed Document-by-Document Breakdown (`01` to `14` in Priority Order)

### 4.1 Document `01` (`AIAF-DOC-01`): Enterprise AI Strategy Charter & Public AI Trust Statement

- **Link:** [01 Enterprise AI Strategy Charter & Public AI Trust Statement](01_EnterpriseAIStrategyCharter.md)
- **Tier & Timing:** **Tier 1** - Phase 0 (Pre-Launch Executive Mandate).
- **Who Produces It:** Executive Leadership (CEO / CIO / Chief Digital Officer) & Corporate Communications.
- **What It Covers:** Sets the organization's internal **Enterprise AI Strategy Charter** (Executive AI Vision Statement, Dual-Speed Operational AI + Corporate GenAI model, **8 Guiding Decision Principles `STR-01` to `STR-08`**, and 3-Horizon Evolution), paired with external-ready **Public AI Trust Statement & Annual/Sustainability Report disclosure wording**.

### 4.2 Document `02` (`AIAF-DOC-02`): Enterprise AI Policy, Data Classification (`D1-D5`) & Non-Human Actor Standard

- **Link:** [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md)
- **Tier & Timing:** **Tier 1** - Phase 0 (Pre-Launch Corporate Governance Gate).
- **Who Produces It:** CISO / InfoSec, Data Protection Officer (DPO), Head of Enterprise IT & AI CoE Lead.
- **What It Covers:** Establishes the overarching Enterprise AI Policy, defines the 5-tier AI data taxonomy (`D1 Public`, `D2 Internal`, `D3 Confidential`, `D4 Restricted`, `D5 Regulated / Critical Infrastructure`), scores domain readiness, inventories the 7 classes of AI knowledge assets (`KNA-01` to `KNA-07`), mandates inference-time RAG grounding over model weight training, and defines the **Non-Human Actor Governance Standard** across 5 agent personas (`NHA-01` to `NHA-05`).

### 4.3 Document `03` (`AIAF-DOC-03`): AI Data Classification Matrix & Enterprise Data Source Control Register

- **Link:** [03 AI Data Classification Matrix & Enterprise Data Source Control Register](03_DataClassificationMatrixAndSourceRegister.md)
- **Tier & Timing:** **Tier 1** - Phase 0 (Connector Setup & Data Boundary Lock).
- **Who Produces It:** CISO / InfoSec, Data Protection Officer (DPO), Enterprise Data Governance & IT System Owners.
- **What It Covers:** Operationalizes the policy definitions in Document `02` (`AIAF-DOC-02`) into **Stage 1 (a `D1-D5 x 10 AI Tool Surfaces` Permission Matrix)** showing exactly where each data classification is `PERMITTED`, `CONDITIONAL`, or `PROHIBITED`, and **Stage 2 (an Enterprise Data Source & Control Register)** mapping **12 core enterprise repositories (`SRC-001` to `SRC-012`)** (including Document Management Systems, Cloud Document Repositories, Email/Calendar, ITSM, Procurement ERP, Core Financial ERP, Data Lakehouse, Legal Contract Vaults, Customer Ops Platforms, Compliance Libraries, and Core OT/Production Control Systems) to their highest data classification tier, permitted AI mode, technical controls, and named Data Steward.

### 4.4 Document `04` (`AIAF-DOC-04`): Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide

- **Link:** [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md)
- **Tier & Timing:** **Tier 1** - Wave 1 Go-Live (Day-1 Workforce Guardrail).
- **Who Produces It:** AI CoE, HR, Internal Communications & InfoSec.
- **What It Covers:** Translates the technical rules in Documents `02` and `03` (`AIAF-DOC-02`, `AIAF-DOC-03`) into a scannable, 1-page **`GREEN / AMBER / RED` Traffic-Light Usage Guide**, **5 Golden Rules for Every Colleague**, a **Before-You-Hit-Send Decision Flowchart**, and a ready-to-use **Employee Onboarding Acknowledgement Form** for `L100` training across all licensed users.

### 4.5 Document `05` (`AIAF-DOC-05`): Departmental Knowledge Notebook & Prompt Library Curation Playbook & Asset Catalog

- **Link:** [05 Departmental Knowledge Notebook & Prompt Library Curation Playbook & Asset Catalog](05_KnowledgeNotebookAndPromptPlaybook.md)
- **Tier & Timing:** **Tier 2** - Phase 0 Early Access (Champion Enablement).
- **Who Produces It:** AI CoE Enablement Lead & Business Unit Champions (`L200`).
- **What It Covers:** Operationalizes `KNA-01` to `KNA-03` from Document `02` (`AIAF-DOC-02`) with a **5-Stage Curation Lifecycle SOP** (Nominate & Scope -> Sanitize & Format -> Ground & Benchmark `25-50 Q&A` -> Publish with Viewer-Only Identity Group ACLs -> **90-Day Freshness Audit**), the **4-Part Role-Based Prompt Template (`R-C-T-V` Pattern)**, and a baseline **Shared AI Knowledge Asset Catalog (`CAT-001` to `CAT-008`)**.

### 4.6 Document `06` (`AIAF-DOC-06`): AI Security Incident Response & 90-Day Kill-Switch Drill Runbook

- **Link:** [06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook](06_AISecurityIncidentAndKillSwitchRunbook.md)
- **Tier & Timing:** **Tier 2** - Initial Go-Live (Operational Safety Net for Live Connectors).
- **Who Produces It:** CISO / SOC Incident Response Team, AI CoE & Enterprise IT Operations.
- **What It Covers:** Establishes an AI-specific **`SEV-1` to `SEV-4` Incident Severity Matrix**, a **5-Layer 15-Minute Containment & Kill-Switch Hierarchy** (Layer 1 Identity Group Removal & IdP Session Reset -> Layer 2 Connector/Knowledge Notebook Purge -> Layer 3 Dedicated Agent Service Principal Disable -> Layer 4 Runtime AI Guardrail Blockade -> Layer 5 Tenant / Private Network Perimeter Lockdown), step-by-step SOC/Platform CLI runbooks, and a **90-Day Kill-Switch Drill Log Template (`KSD-001` to `KSD-004`)**.

### 4.7 Document `07` (`AIAF-DOC-07`): Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment

- **Link:** [07 Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment](07_StrategicDriversAndThinValuedWork.md)
- **Tier & Timing:** **Tier 2** - Month 1 (CoE Work-Redesign & Discovery).
- **Who Produces It:** AI CoE Lead & Strategy / Digital Transformation Lead, with Business Unit Heads.
- **What It Covers:** Connects AI investments to the 14 canonical enterprise strategic drivers (`DRV-01` to `DRV-14`) and hard constraints (`CON-01` to `CON-06`), maps 10 baseline business capabilities (`CAP-01` to `CAP-10`), and decomposes daily knowledge work into **Thin Work** vs. **Valued Work** across a 2x2 Disruption Priority Matrix and Workforce Transition Plan.

### 4.8 Document `08` (`AIAF-DOC-08`): AI Use Case Intake Cards & Scored Portfolio Backlog

- **Link:** [08 AI Use Case Intake Cards & Scored Portfolio Backlog](08_AIUseCaseIntakeAndPortfolioBacklog.md)
- **Tier & Timing:** **Tier 2** - Initial Rollout (Agent Prioritization).
- **Who Produces It:** AI CoE Intake Lead & Business Unit Champions.
- **What It Covers:** Directly follows Document `07` (`AIAF-DOC-07`) with a 6-dimension weighted **Portfolio Prioritization Matrix** (`Value 25%`, `Data Readiness 20%`, `Risk Inverted 20%`, `Tech Feasibility 15%`, `Strategic Fit 10%`, `Time to Value 10%`), scores 10 representative enterprise candidate use cases (`UC-001` to `UC-010`), and includes full **AI Use Case Intake Cards** for `UC-001` (Document/SOP Synthesis), `UC-004` (Code-First Finance Agent), and `UC-005` (IT & HR Service Desk Agent), paired with [AIUseCaseCard.md](../Templates/AIUseCaseCard.md) and [AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv).

### 4.9 Document `09` (`AIAF-DOC-09`): AI Value Realization, FinOps & 60-Day License Governance SOP

- **Link:** [09 AI Value Realization, FinOps & 60-Day License Governance SOP](09_ValueRealizationAndSeatGovernanceSOP.md)
- **Tier & Timing:** **Tier 3** - Post-Launch Seat Review (Seat Hygiene & ROI Telemetry).
- **Who Produces It:** AI CoE Program Manager, Digital Transformation, Corporate Finance & Identity Administration.
- **What It Covers:** Provides finance-approved formulas (`VAL-01` to `VAL-04`) and a quarterly 3-question micro-survey to track real business value across licensed seats against the enterprise business case (`AIAF-DOC-07`), an automated **Day-30 / Day-45 / Day-60 Inactive Seat Reclamation SOP** for the enterprise identity provider (`SG-AI-Enterprise-Users`), and **11 FinOps Cost Optimization Levers** for the Enterprise AI Platform and code-first custom agents.

### 4.10 Document `10` (`AIAF-DOC-10`): AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap

- **Link:** [10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap](10_AIMaturityScorecardAndReadinessRoadmap.md)
- **Tier & Timing:** **Tier 3** - Recurring Steering Committee Cadence.
- **Who Produces It:** AI CoE Steering Committee & Head of Enterprise IT.
- **What It Covers:** Evaluates the organization across all **7 Core Perspectives** of the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) on a `1.0 to 4.0` scale (`1: Exploring -> 2: Piloting -> 3: Scaling -> 4: Transforming`; illustrating a composite baseline of `2.1 / 4.0 Piloting` transitioning to `3.6 / 4.0 Transforming`), scores the 20-Item Organizational Readiness Checklist (`CHK-01` to `CHK-20`), synthesizes an 11-dimension starting-point profile (`DIM-01` to `DIM-11`), charts the 3-stage CoE operating model evolution, and sequences technical and governance remediation actions across rollout waves.

### 4.11 Document `11` (`AIAF-DOC-11`): Pilot-to-Production (`P2P`) Gate Review Package

- **Link:** [11 Pilot-to-Production (P2P) Gate Review Package](11_PilotToProductionGatePackage.md)
- **Tier & Timing:** **Tier 4** - Pre-Production Custom Agent Launch.
- **Who Produces It:** AI CoE Lead, Cloud Platform Lead & InfoSec Lead.
- **What It Covers:** Summarizes pilot lessons learned and enforces the **10-Dimension Production Readiness Gate Checklist** (Named Owner, Runbook/Escalation, Budget/Quota, Golden Eval Set `>= 85%`, Latency/SLA, Monitoring/Audit, Change Comms, Rollback/Reclamation, Security/Guest Isolation, and Governance Registers) before promoting custom code-first agents or Gateway 2 connectors to production, paired with [PilotToProductionGate.md](../Templates/PilotToProductionGate.md).

### 4.12 Document `12` (`AIAF-DOC-12`): AI Impact Assessment (`AIIA`), Measurable RAI & OWASP LLM Controls

- **Link:** [12 AI Impact Assessment (AIIA), Measurable RAI & OWASP LLM Controls](12_AIImpactAssessmentAndOWASPControls.md)
- **Tier & Timing:** **Tier 4** - Custom Agent Rollout (High-Risk & Regulated Workflows).
- **Who Produces It:** Business Unit Use-Case Owner (`Decision Owner`) & AI Governance / InfoSec Reviewer.
- **What It Covers:** Provides a completed 5-Step AI Impact Assessment (`AIIA`) baseline illustrated for `UC-004` (`Multi-ERP Financial Consolidation & Variance Agent`, `Tier 3 High Risk`), converts the 6 Responsible AI principles into measurable evaluation thresholds (`Groundedness >= 85%`, `ACL Leakage = 0%`), and maps each risk in the **OWASP Top 10 for LLM Applications (`LLM01` to `LLM10`)** to concrete technical and identity controls, paired with [AIImpactAssessment.md](../Templates/AIImpactAssessment.md).

### 4.13 Document `13` (`AIAF-DOC-13`): Operational Governance Registers & GenAIOps Guide

- **Link:** [13 Operational Governance Registers (Decision, Tool & Data Dictionary) & GenAIOps Guide](13_OperationalGovernanceRegistersAndGenAIOps.md)
- **Tier & Timing:** **Tier 4** - Ongoing Operations (Sustained Fleet Scale & Day-2 GenAIOps).
- **Who Produces It:** AI CoE Operations Lead & Enterprise IT Governance Lead.
- **What It Covers:** Contains three living governance registers (**`AIDecisionRegister`** `ADR-001` to `ADR-006`, **`ApprovedAIToolRegistry`** `TOOL-001` to `TOOL-006`, and **`DataDictionary`** controlled vocabularies) plus the **GenAIOps Evaluation Flywheel** bridging classical deterministic MLOps with corporate GenAIOps (`25-50 Q&A` and `100-sample` Golden Datasets), paired with [AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv), [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv), and [DataDictionary.md](../Templates/DataDictionary.md).

### 4.14 Document `14` (`AIAF-DOC-14`): Third-Party SaaS & Vendor AI Procurement Assessment Checklist

- **Link:** [14 Third-Party SaaS & Vendor AI Procurement Assessment Checklist](14_VendorAIProcurementChecklist.md)
- **Tier & Timing:** **Tier 4** - Ongoing Procurement & Vendor Security Gate.
- **Who Produces It:** Procurement, CISO / InfoSec, Legal & AI CoE.
- **What It Covers:** Operationalizes the Vendor Bypass Standard from Document `02` (`AIAF-DOC-02`, Sec 3.3) via a two-stage gate: **Stage 1 (Core Platform Bypass Check)** redirects duplicate SaaS AI requests to the organization's existing Enterprise AI Platform, Grounded Knowledge Workspaces (`CAT-001` to `CAT-008` in `AIAF-DOC-05`), or Code-First Agent Framework (`UC-001` to `UC-009` in `AIAF-DOC-08`) at zero incremental SaaS cost; **Stage 2 (`VND-001` to `VND-010`)** enforces 10 mandatory contractual and technical security gates, illustrated with 3 vendor evaluations (`VREV-001` to `VREV-003`).

## 5. Summary of the 4-Tier Operational Rollout Flow (`00 -> 14`)

| Execution Tier | Target Timing | Ordered Document Sequence (`01` to `14`) | Core Governance & Business Outcome Achieved |
| :--- | :--- | :--- | :--- |
| **Tier 1: Day-0 Executive Mandate & Core Guardrails** | **Pre-Launch & Initial Go-Live** | `01 Strategy Charter` -> `02 Enterprise AI Policy (D1-D5 & NHA)` -> `03 Data Matrix & Source Register` -> `04 Employee 1-Page Traffic-Light AUP` | Aligns leadership on strategic trade-offs, locks `D1-D5` data boundaries across all 12 core repositories, and equips every licensed employee with a 1-page Day-1 safety guide. |
| **Tier 2: Wave-1 Value Enablement, Safety Net & Intake** | **Early Access & Initial Rollout** | `05 Knowledge Notebook & Prompt Curation Playbook` -> `06 Incident & Kill-Switch Runbook` -> `07 Strategic Drivers & Thin-vs.-Valued Work` -> `08 Use Case Intake & Scored Backlog` | Delivers immediate Day-1 productivity via Champion-curated workspaces (`CAT-001..008`), gives InfoSec/SOC a `<15-min` emergency shutoff, and ranks custom agent candidates objectively. |
| **Tier 3: FinOps Seat Governance & Maturity Roadmap** | **Post-Launch Adoption & Seat Governance** | `09 Value Realization, FinOps & 60-Day Seat SOP` -> `10 AI Maturity Scorecard & 20-Item Readiness Roadmap` | Automates Day 30/45/60 inactive license reclamation, proves finance-verified ROI (`VAL-01..04`), and tracks quarterly capability maturity across all 7 AIAF perspectives for the Steering Committee. |
| **Tier 4: Custom Agent P2P Gates, Deep Risk & GenAIOps** | **Custom Agent Rollout & Ongoing Operations** | `11 Pilot-to-Production (P2P) Gate` -> `12 AI Impact Assessment (AIIA) & OWASP` -> `13 Operational Registers & GenAIOps` -> `14 Third-Party Vendor AI Checklist` | Promotes custom code-first agents safely to production (`>= 85%` Golden Eval pass rate), enforces OWASP `LLM01-LLM10` controls, prevents model/prompt drift, and blocks duplicate shadow SaaS AI spend. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Parent vendor-agnostic adoption framework defining the 7 Core Perspectives, 6 Lifecycle Phases, Pilot-to-Production Gate, and 4 Maturity Levels.
- [References](../References.md): Maintained catalog of regulatory, security, operational, and adoption standards with suggested review cadences.
- [Templates](../Templates/README.md): Companion standalone Markdown forms and CSV operational registers.
- [ISO/IEC 42001: Artificial Intelligence Management System](https://www.iso.org/standard/42001): International standard for establishing, implementing, maintaining, and continually improving an AI management system.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1): Risk management vocabulary, lifecycle controls, and generative AI risk profiles.
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/) and [OWASP GenAI Security Project](https://genai.owasp.org/): Industry security risk taxonomy (`LLM01`-`LLM10`) and mitigation guidance.
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final): Identity-centric security and least-privilege network segmentation principles.
- [FinOps Foundation - FinOps for AI](https://www.finops.org/topic/finops-for-ai/): Cloud AI financial governance and token cost optimization practices.
