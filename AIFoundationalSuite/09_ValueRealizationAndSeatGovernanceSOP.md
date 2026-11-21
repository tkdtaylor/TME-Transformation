<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 09 AI Value Realization, FinOps & 60-Day License Governance SOP

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-09` (AI Value Realization, FinOps & 60-Day License Governance SOP) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE) Program Managers, Digital Transformation Leads, Finance Business Partners, Identity License Admins, and Business Unit Sponsors |
| **Primary Internal Owner** | AI Center of Excellence (CoE) & Digital Transformation Lead, with Corporate Finance & Enterprise IT Identity Administration |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE), Corporate Finance, and IT Identity teams measure AI value realization, govern seat utilization, and control cloud consumption costs. It is **not** prescriptive. Sections include **4 Finance-Approved ROI Formulas (`VAL-01` to `VAL-04`)**, a **Quarterly 3-Question Micro-Survey**, an automated **30 / 45 / 60-Day Inactive License Reclamation SOP**, and **11 Technical FinOps Cost Optimization Levers** so teams do not have to start from a blank page.

## 1. How the AI CoE & Corporate Finance Can Create, Customize & Run This SOP

### 1.1 Purpose & Why This Document Exists

After the initial launch of an enterprise AI platform, executive sponsors and Corporate Finance inevitably ask two questions at quarterly business reviews and expansion gates:

1. **"Are employees actively using the licenses we contracted across the organization, and what measurable operational value did the organization realize?"**
2. **"How do we prevent inactive seats ('shelfware') or inefficient custom agent prompts from inflating our cloud bill?"**

While [07 Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment](07_StrategicDriversAndThinValuedWork.md) (`AIAF-DOC-07`) establishes the baseline productivity value model and [10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap](10_AIMaturityScorecardAndReadinessRoadmap.md) (`AIAF-DOC-10`) defines the rollout milestones, this Standard Operating Procedure (SOP) provides the **operational measurement pipeline, the automated 30/45/60-day license reclamation workflow, and the 11 technical FinOps cost levers** to govern the deployment continuously.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Primary Custodians**: AI Center of Excellence (CoE) Program Lead, Corporate Finance Business Partner, and Enterprise IT Identity Administrator.
- **Required Internal Contributors**: Business Unit Champions (collecting quarterly workflow cycle-time benchmarks) and Cloud Platform / AI Platform Engineers (configuring FinOps budget alerts and context caching).

### 1.3 Recommended Internal CoE & Finance Production Process (FinOps & Seat Hygiene Setup)

To establish this governance rhythm internally without external facilitation, the AI CoE Lead, Corporate Finance Partner, and IT Identity Admin can complete a FinOps & Seat Hygiene Setup Session:

1. **Enable Analytics Lakehouse Usage Audit Log Export:** Configure Immutable Audit Logs for `enterprise-ai-gateway` and `model-inference-api` to stream into a central Enterprise Data Warehouse / Analytics Lakehouse dataset (`ai_finops_telemetry`) in the production environment.
2. **Automate the Inactive License Reclamation Workflow:** Connect the analytics lakehouse 30-day active-user view to corporate Identity Provider (IdP) group management (`SG-AI-Enterprise-Users`) so inactive seats are automatically nudged at Day 30, warned at Day 45, and reallocated to waitlisted users at Day 60.
3. **Lock In the Executive Value Scorecard:** Agree with Corporate Finance on the conservative realization formulas in **Section 2** so monthly steering committee updates use finance-approved math.

## 2. Monthly Value Realization & ROI Tracking Methodology

To avoid subjective "vanity metrics" (such as raw prompt counts alone), the AI CoE combines **automated analytics lakehouse telemetry** with **quarterly 3-question micro-surveys** and **workflow cycle-time benchmarks** to track progress against the organization's business case across rollout cohorts:

```
+-----------------------------------------------------------------------+
|       ENTERPRISE AI VALUE REALIZATION & FINOPS TELEMETRY PIPELINE     |
+-----------------------------------------------------------------------+
|                                                                       |
|  [1. System Telemetry (Automated)]   [2. User & Process Validation]   |
|  - Immutable Audit Logs (WAU/MAU)    - Quarterly 3-Question Pulse     |
|  - Connector Query Volume by BU      - ITSM / ERP / RFP Workflow      |
|  - Model Token & Cache Metrics         Cycle-Time Reduction Delta     |
|                 |                                   |                 |
|                 +-----------------+-----------------+                 |
|                                   |                                   |
|                                   v                                   |
|  +-----------------------------------------------------------------+  |
|  |         MONTHLY AI CoE VALUE & SEAT HYGIENE DASHBOARD           |  |
|  |  - Active Seat Utilization % (Target >= 85% Activation,         |  |
|  |    >= 50% WAU/MAU Stickiness across Active Cohorts)             |  |
|  |  - Thin-to-Valued Hours Reclaimed per Active User / Week        |  |
|  |  - Day-60 Inactive Seat Reallocation Queue                      |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

### 2.1 The 4 Core Value & Adoption KPIs (Finance-Approved Formulas)

| KPI ID | Metric Name | Exact Calculation Formula | Data Source | Target Threshold |
| :--- | :--- | :--- | :--- | :--- |
| **`VAL-01`** | **License Activation & Active Stickiness (`WAU / MAU %`)** | `Activation = (Users with >= 1 session within 14 days of provisioning) / (Assigned Seats in SG-AI-Enterprise-Users)`; `Stickiness = (7-Day WAU) / (30-Day MAU)` | Immutable Audit Logs (`enterprise-ai-gateway`) + IdP SCIM Roster | **`>= 85%` Activation**, **`>= 50%` WAU/MAU Stickiness** |
| **`VAL-02`** | **Verified Thin-Work Hours Reclaimed (`Hours/User/Week`)** | `(Active Users in Cohort) x (Median Weekly Hours Saved from Quarterly Pulse & Time-Motion Samples) x (0.75 Conservative Finance Realization Haircut)` | Quarterly 3-Question Pulse Survey + Champion Spot-Checks | **Positive net weekly hours reclaimed per active user** (after 0.75 Finance realization haircut) |
| **`VAL-03`** | **Workflow Cycle-Time Reduction (`% Delta`)** | `(Baseline Pre-AI Mean Time to Resolve or Draft - Post-AI Mean Time) / (Baseline Pre-AI Mean Time)` | ITSM Tickets (`UC-005`), Monthly Financial Variance Close (`UC-004`), RFP Comparisons (`UC-008`) | **Measurable cycle-time reduction across `UC-001` to `UC-009`** ([08 AI Use Case Intake Cards & Scored Portfolio Backlog](08_AIUseCaseIntakeAndPortfolioBacklog.md)) |
| **`VAL-04`** | **SaaS Consolidation & Vendor Bypass Savings (`USD/Year`)** | `Sum of Annualized Contract Value of Third-Party SaaS AI Tools Bypassed at Stage 1 Procurement Gate (AIAF-DOC-14)` | Corporate Procurement Bypass Log (`VREV-001` to `VREV-003` in [AIAF-DOC-14](14_VendorAIProcurementChecklist.md)) | **Avoided duplicate third-party SaaS spend logged at Stage 1 Procurement Gate** |

### 2.2 The Quarterly 3-Question "Thin-to-Valued Work" Micro-Survey

Every 90 days, licensed users receive a brief pulse form (3 questions only) to pair system logs with concrete operational outcomes:

1. **Primary Capability Used:** *"Over the past 2 weeks, which AI capability helped you the most? (a) Enterprise Grounded Search across workspace folders/emails, (b) Curated Departmental Knowledge Workspace (`CAT-001` to `CAT-008`), (c) Scoped No-Code Agent Builder or Code-First Custom Agent Workflow (`UC-004` to `UC-009`), (d) I did not use it."*
2. **Conservative Time Reclaimed:** *"Approximately how many hours of manual searching, reading, summarizing, or first-drafting ('Thin Work') did this save you last week? (`0 hrs`, `1-2 hrs`, `3-5 hrs`, `6+ hrs`)"*
3. **Concrete Work Artifact Example:** *"Briefly name one specific task where AI helped you move faster or improve quality (for example: 'Located preventive maintenance fault procedure in `CAT-001` in minutes instead of searching manually across folders')."*

## 3. The 60-Day Rolling License Governance & Seat Reclamation SOP

To ensure near-100% active utilization across contracted **Enterprise AI Platform** licenses, seat assignment in the corporate Identity Provider (`SG-AI-Enterprise-Champions`, `SG-AI-Enterprise-Users`) is governed by an **automated 30 / 45 / 60-day activity lifecycle**:

| Lifecycle Milestone | Trigger Condition (Analytics Lakehouse Audit View) | Automated Action Taken by AI CoE / IT Admin | User Experience & Re-Onboarding Path |
| :--- | :--- | :--- | :--- |
| **Day 0: Seat Assignment** | User added to `SG-AI-Enterprise-Users` (or `SG-AI-Enterprise-Champions`) and synced via SCIM to Enterprise AI Platform directory. | Provision license; send **Day-1 Welcome Notice**, [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md) (`AIAF-DOC-04`), and link to their BU's **Curated Knowledge Workspace (`CAT-*`, [AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md))**. | Immediate corporate SAML 2.0 SSO access to the Enterprise AI Assistant and Grounded Knowledge Notebooks. |
| **Day 30: Enablement Nudge** | `0` active queries or sessions logged between Day 1 and Day 30. | Automated email/chat nudge sent to user with 3 role-specific sample prompts (`R-C-T-V` template) and an invitation to a CoE Champion office hour. | License remains active; user receives targeted coaching to overcome initial friction. |
| **Day 45: Reclamation Warning** | `0` active queries or sessions logged between Day 1 and Day 45. | Automated notice sent to user: *"Your Enterprise AI Platform seat has had no activity for 45 days. To maintain high utilization across our organization, inactive seats are returned to the department waitlist at Day 60 unless used."* | User simply executes 1+ work query or clicks **"Keep My Seat (Parental / Medical Leave / Project Transition)"** to reset the clock. |
| **Day 60: Automatic Seat Reclamation & Reallocation** | `0` active queries or sessions logged for 60 consecutive days (and no leave exemption logged). | User is removed from `SG-AI-Enterprise-Users` in the corporate IdP; SCIM de-assigns the seat on the next sync cycle and assigns it to the next approved nominee on the **BU Seat Waitlist**. | Zero penalty; if the user needs a license later, their Department Head can re-nominate them at any time. |

## 4. The 11 FinOps Cost Optimization Levers for Custom Agents & API Workloads

While **Enterprise AI Platform (Standard Tier)** licenses operate on predictable per-seat subscription pricing with edition-level daily quota pooling, custom **Code-First Custom Agents** built on the **Enterprise Agent Runtime** (`UC-004` Finance Consolidation Agent, `UC-006` Analytics Agent) consume usage-based tokens and search calls. The AI CoE enforces **11 technical FinOps controls** prior to Production Gate ([AIAF-DOC-11](11_PilotToProductionGatePackage.md)):

| Lever # | FinOps Control | Enterprise Implementation Standard | Expected Cost Impact |
| :---: | :--- | :--- | :--- |
| **1** | **Edition Overage Toggle Lock** | Keep the **Overage Checkbox UNCHECKED (Off)** for the general workforce `Standard` tier in the Platform Admin Console (`Usage & Spending`); if using a `Power-User` tier, enable overages **only** on that tier with a hard monthly spend limit. | **USD 0 unexpected overage risk** across the general workforce seat pool. |
| **2** | **Model Tier Routing (Fast-Tier-First Default)** | Route **`>= 80%`** of high-volume extraction, classification, and routine summarization calls in custom agent pipelines to the **Fast / Lightweight Model Tier**; reserve the **Frontier Reasoning Model Tier** for complex multi-step reasoning or code execution (`UC-004`). | **60% to 80% lower** token cost per API request. |
| **3** | **Prompt / Context Caching for Static Manuals (`>32k Tokens`)** | Enable **Prompt / Context Caching** ([AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md), Sec 3.1) whenever an agent repeatedly references the same large system instruction, chart-of-accounts mapping, or technical manual across multiple queries. | Up to **75% reduction** on cached input token costs. |
| **4** | **Asynchronous Batch Inference API for Non-Urgent Workloads** | Run overnight document classification, historical log tagging, and bulk report extraction via the **Asynchronous Batch Inference API** rather than synchronous online endpoints. | **50% discount** vs. synchronous online inference pricing. |
| **5** | **Prompt & Output Token Budgeting (`max_output_tokens`)** | Set explicit `max_output_tokens` caps and concise structured JSON output schemas on every sub-agent step so models do not generate verbose conversational filler in machine-to-machine pipelines. | **25% to 40% reduction** in output token spend. |
| **6** | **RAG Top-K & Chunk Size Tuning** | Restrict ingested data store retrieval to the top `k = 5 to 8` highest-relevance chunks rather than stuffing 50+ full documents into every prompt context window. | **40% to 60% reduction** in input token volume and lower p95 latency. |
| **7** | **Semantic / Exact Query Caching for High-Frequency FAQs** | Cache verified answers for identical non-personalized queries (for example, standard corporate holiday schedules or common IT helpdesk steps in `UC-005`) with a 24-hour TTL. | Eliminates redundant LLM inference calls on top 15% repeat questions. |
| **8** | **Hard Loop Guards (`max_steps <= 10`) on Custom Agents** | Configure every tool-calling custom agent (`NHA-04`, `NHA-05`) with a strict maximum step count (`max_steps <= 10`) and automatic circuit-breaker timeout (`30 seconds`) to prevent infinite retry loops. | Prevents runaway token spikes during backend API outages (`SEV-2` in [AIAF-DOC-06](06_AISecurityIncidentAndKillSwitchRunbook.md)). |
| **9** | **Per-Agent Service Principal Billing Labels** | Attach mandatory FinOps cost-allocation tags (`bu: <unit>`, `use_case: uc-004`, `env: prod`, `cost_center: <id>`) to every agent service principal and model inference endpoint call. | Enables 100% transparent chargeback/showback by Business Unit. |
| **10** | **Automated Cloud FinOps & Billing Budget Alerts (`50% / 80% / 100%`)** | Configure programmatic event-driven budget webhook alerts on every AI project that notify the CoE at 50% and 80% of monthly forecast and trigger Layer 3 non-critical staging suspension at 120%. | Zero end-of-month billing surprises for Corporate Finance. |
| **11** | **Provisioned Throughput (PT) Threshold Evaluation** | Monitor steady-state token volume across production custom agents; once sustained baseline traffic exceeds the break-even utilization threshold, convert baseline load from Pay-As-You-Go (PAYG) to **Provisioned Throughput**. | Predictable flat monthly capacity cost + guaranteed latency SLAs during peak operational periods. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Cost Optimization Levers (Detailed), Business Outcomes KPIs, and Operational Outcomes KPIs.
- [References](../References.md): Maintained catalog of adoption, operational, and financial governance references.
- [FinOps Foundation - FinOps for AI](https://www.finops.org/topic/finops-for-ai/): Cloud AI financial governance, unit economics, and token budget enforcement practices.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Lifecycle monitoring and organizational governance metrics.
