<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 08 AI Use Case Intake Cards & Scored Portfolio Backlog

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-08` (AI Use Case Intake Cards & Weighted Portfolio Backlog) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Digital Transformation Leads, Business Unit Champions, and Enterprise IT Architecture Leads |
| **Primary Internal Owner** | Business Unit Process Owners & AI CoE Intake Lead |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE) and internal teams standardize AI use-case intake, scoring, and portfolio prioritization. It is **not** prescriptive. Sections include a pre-structured 10-use-case enterprise backlog (`UC-001` to `UC-010`) and 3 sample intake cards covering universal corporate workflows (Enterprise Knowledge Synthesis, Financial Consolidation & Variance Analysis, and IT/HR Service Desk Triage) so teams do not have to start from a blank page. Organizations can share this template directly or customize the bracketed fields to fit their internal governance standards.

## 1. How the AI CoE Can Create, Customize & Run an Intake Clinic with This Document

### 1.1 Purpose & Why This Document Exists

When employees and Departmental Champions gain access to the **Enterprise AI Platform**, business units rapidly propose dozens of ideas for custom agents and data connectors. Without a standardized intake and scoring mechanism, engineering teams get pulled into high-risk, low-data-readiness science projects ("Overbroad AI Ambition") while high-value, low-risk quick wins sit unbuilt.

This document provides the worked baseline for the canonical AIAF **AI Use Case Card** ([AIUseCaseCard.md](../Templates/AIUseCaseCard.md)) and **Scored Portfolio Backlog** ([AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv)). It enforces three portfolio management rules:

1. **The SOP Prerequisite**: Before any workflow is approved for a custom agent, the owning business unit must provide a documented Standard Operating Procedure (SOP) defining the step-by-step workflow, decision criteria, exception paths, and human handoffs.
2. **The 3-Stage Use Case Progression ("Do Not Start at Stage 3")**:
   - **Stage 1: Task Automation (Thin Work)** - Out-of-the-box Enterprise AI Assistant Chat, Public Web Grounding, File Upload, and Departmental Knowledge Workspaces (Initial Rollout).
   - **Stage 2: Human Augmentation (Valued Work / HITL)** - Scoped No-Code Agent Builder workflows and Code-First Custom Agents that synthesize cross-system data and prepare recommendations for a named human decision-maker (Expansion Phase).
   - **Stage 3: Agentic Autonomy (Bounded Execution)** - Permitted only after an agent proves `>= 85%` groundedness and `>= 90%` relevance in Stage 2 with a verified 90-day kill-switch (Advanced Scale).
3. **The 6-Dimension Weighted Prioritization Rubric**: Every proposed use case is scored from `1` to `5` across six weighted dimensions:
   - **Business Value (`25%`)** | **Data Readiness (`20%`)** | **Risk Inverted (`20%` - where `5 = Tier 1 Low Risk` and `1 = Tier 4 Critical Risk`)** | **Technical Feasibility (`15%`)** | **Strategic Fit (`10%`)** | **Time to Value (`10%`)**.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Use Case Card Submitter**: Departmental Champion (`L200`) or Business Unit Process Owner.
- **Internal Technical & Risk Scorers**: Enterprise IT Architecture, Enterprise Data Steward, and Information Security Reviewer.
- **Portfolio Approver**: AI Center of Excellence (CoE) Steering Committee, routing approved items to either **Gateway 1 (Self-Service)** or **Gateway 2 (Enterprise Controlled)**.

### 1.3 Recommended Approach: Running a CoE Use-Case Intake & Portfolio Scoring Clinic

The best way for the AI CoE to qualify and prioritize candidate agents is to run a recurring internal Use-Case Intake & Portfolio Scoring Clinic (ahead of each wave and monthly thereafter):

1. **Pre-Clinic Intake Gate**: Require any nominating Business Unit Process Owner or `L200` Champion to complete a draft intake card (using [AIUseCaseCard.md](../Templates/AIUseCaseCard.md) or **Section 3.4**) and attach the underlying documented SOP ahead of the clinic.
2. **Step 1 - SOP & Stage-Progression Check**: Verify that a written SOP exists and confirm whether the request should start as a **Stage 1** grounding/Knowledge Workspace workflow or a **Stage 2** Human-in-the-Loop (`HITL`) agent.
3. **Step 2 - 6-Dimension Collaborative Scoring (Section 2)**: Have the Business Unit Owner score `Business Value` and `Strategic Fit`, while Enterprise IT, the Data Steward, and InfoSec score `Data Readiness`, `Risk Inverted`, `Technical Feasibility`, and `Time to Value` in **Table 2** (exportable to [AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv)).
4. **Step 3 - Gateway Routing & Backlog Lock**: Route high-scoring `Tier 1/2` departmental workflows to **Gateway 1 / No-Code Agent Builder** and route complex cross-system `Tier 2/3` workflows (`UC-004`, `UC-006`) to **Gateway 2 (Code-First Custom Agent)** with a mandatory AI Impact Assessment ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)).

## 2. Scored Enterprise AI Use Case Portfolio Backlog (`AIUseCaseBacklog` Baseline Template)

> **Companion CSV Template:** Maintain the live sortable portfolio register using [../Templates/AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv) and its controlled vocabularies in [../Templates/DataDictionary.md](../Templates/DataDictionary.md).

| Use Case ID | Use Case Name | Business Unit | Category | Risk Tier | Value (25%) | Data (20%) | Risk Inv. (20%) | Tech Feas. (15%) | Strat Fit (10%) | Time to Val (10%) | Composite Score (`/ 5.00`) | Gateway & Rollout Stage |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `UC-001` | **Enterprise Document Retrieval & Operational SOP Synthesis** | All BUs / Operations & Engineering | Augmentation | Tier 1 | 5 | 4 | 5 | 5 | 5 | 5 | **`4.80`** | **Gateway 1 - Initial Rollout (Immediate)** |
| `UC-002` | **Corporate Communications, Proposal & Multilingual Drafting** | All BUs / Commercial & Marketing | Generation | Tier 1 | 5 | 5 | 5 | 5 | 4 | 5 | **`4.90`** | **Gateway 1 - Initial Rollout (Immediate)** |
| `UC-003` | **Market Intelligence, Competitor & Regulatory Deep Research** | Strategy, Commercial & ESG | Analysis | Tier 1 | 4 | 5 | 5 | 5 | 5 | 5 | **`4.75`** | **Gateway 1 - Initial Rollout (Immediate)** |
| `UC-004` | **Multi-Entity Financial Consolidation & Variance Analysis Agent** | Finance / CFO Office | Analysis | Tier 3 | 5 | 4 | 2 | 4 | 5 | 3 | **`3.85`** | **Gateway 2 (Code-First Agent) - Expansion Phase** |
| `UC-005` | **IT & HR Internal Employee Service Desk Triage Agent** | Enterprise IT & Human Resources | Automation | Tier 2 | 4 | 4 | 4 | 5 | 4 | 4 | **`4.15`** | **Gateway 2 (No-Code Builder) - Expansion Phase** |
| `UC-006` | **Conversational Operational & Commercial Analytics Agent** | Operations, Commercial & Data | Analysis | Tier 2 | 5 | 4 | 3 | 4 | 5 | 3 | **`4.05`** | **Gateway 2 (Code-First Agent) - Expansion Phase** |
| `UC-007` | **Enterprise Contract Obligation & Renewal Clause Reviewer** | Legal & Compliance | Analysis | Tier 3 | 5 | 4 | 2 | 4 | 5 | 3 | **`3.85`** | **Gateway 2 (Scoped Workspace/Agent) - Expansion Phase** |
| `UC-008` | **Procurement Multi-Vendor RFP Comparison Assistant** | Corporate Procurement | Analysis | Tier 2 | 4 | 4 | 4 | 4 | 4 | 4 | **`4.00`** | **Gateway 1/2 (No-Code Builder) - Expansion Phase** |
| `UC-009` | **Customer Operations Incident & Disruption Advisory Drafter** | Customer Operations & Support | Generation | Tier 2 | 4 | 4 | 4 | 4 | 5 | 4 | **`4.10`** | **Gateway 2 (No-Code Builder) - Expansion Phase** |
| `UC-010` | **Autonomous Cross-System ERP Journal & PO Execution** | Finance / Procurement | Agency | Tier 4 | 4 | 2 | 1 | 2 | 3 | 1 | **`2.30`** | **DEFERRED (Stage 3 Autonomous - Do Not Start Here)** |

## 3. Reusable AI Use Case Intake Cards (`AIUseCaseCard` Templates)

> **Companion Blank Form:** Use [../Templates/AIUseCaseCard.md](../Templates/AIUseCaseCard.md) as the standalone blank intake card template for new business unit submissions.

### 3.1 Template Card 1: `UC-001` - Enterprise Document Retrieval & Operational SOP Synthesis (`Stage 1 -> Stage 2`)

| Field | Baseline Template Response (Customize Bracketed Values per Organization) |
| :--- | :--- |
| **Use Case ID & Name** | `UC-001` - Enterprise Document Retrieval, Policy Lookup & Operational SOP Synthesis |
| **Business Unit & Owner** | All Corporate Functions & Operational Divisions (CoE Champions & Departmental Knowledge Curators) |
| **Target Users** | `<All Licensed Knowledge Workers>` |
| **Current Process & Friction** | Employees spend significant weekly time searching across cloud document repositories, PDF technical manuals, and policy folders (High Thin Work). Standard keyword search struggles with dense multi-column procedures and tables. |
| **Proposed AI Capability** | **Stage 1 -> Stage 2 Grounded Synthesis**: Combine **Federated Enterprise Search Connectors** (general discovery across authorized workspaces) with curated **Departmental Knowledge Workspaces** (authoritative SOPs) featuring mandatory clickable inline citations. |
| **Use Case Category & Risk Tier** | `Augmentation / Analysis` - **Tier 1 (Low)** for `D2` internal policies; **Tier 2 (Medium)** for `D3` technical/operational manuals |
| **Quantified Business Value** | Foundational **Set 1 Quick Win**: substantially reduces document search and synthesis time, recovering weekly capacity per active user. |
| **Data & Grounding Readiness** | `D2 Internal` and `D3 Confidential` PDF/formatted documents in enterprise document repositories. Validated via a **25 to 50 Q&A Golden Dataset** (`>= 85%` groundedness) prior to broad departmental publishing. |
| **Security & Controls** | Strictly bounded by per-user **Identity Provider (IdP) OAuth 2.0** source ACLs (`Gateway 1`); external B2B guests excluded via directory filter; zero model weight training. |
| **Weighted Priority Score** | **`4.80 / 5.00`** (Recommend: PURSUE - Initial Rollout Quick Win) |

### 3.2 Template Card 2: `UC-004` - Multi-Entity Financial Consolidation & Variance Analysis Agent (`Gateway 2 Code-First Agent`)

| Field | Baseline Template Response (Customize Bracketed Values per Organization) |
| :--- | :--- |
| **Use Case ID & Name** | `UC-004` - Multi-Entity Financial Consolidation & Monthly Variance Commentary Agent |
| **Business Unit & Owner** | Corporate Finance / CFO Office (Technical Delivery: Enterprise AI Engineering Team) |
| **Target Users** | Financial Controllers, Regional Finance Leads, and FP&A Analysts (`<SG-AI-Finance-Controllers>`) |
| **Current Process & Friction** | Analysts spend days during month-end close manually extracting trial balances and variance tables across ERP exports, reconciling currency/intercompany differences in spreadsheets (High Thin Work), and drafting executive variance commentary. |
| **Proposed AI Capability** | **Stage 2 Human Augmentation (Code-First Agent on Enterprise Agent Runtime)**: Uses deterministic Python code execution and read-only SQL/MCP tools over structured financial exports (bypassing text-RAG token limits on `>500,000`-word spreadsheets) to calculate exact variances and draft cited narrative commentary for human controller sign-off. |
| **Use Case Category & Risk Tier** | `Analysis / Augmentation` - **Tier 3 (High Risk)** (`D4 Restricted` financial data) |
| **Quantified Business Value** | Compresses monthly variance analysis and board commentary preparation cycle time significantly while eliminating manual formula copy-paste errors. |
| **Data & Grounding Readiness** | `D4 Restricted` structured tables in ERP exports and enterprise data lakehouse. Requires standardized chart-of-accounts mapping and a **100-sample Financial Golden Dataset**. |
| **Security & Controls** | **Gateway 2 Controlled Governance**: Read-only scoped credentials; strict per-entity ACL isolation; **mandatory Human-in-the-Loop (HITL) controller sign-off** (zero autonomous ERP journal posting); completed `AIIA` ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)); **90-day tested kill-switch**. |
| **Weighted Priority Score** | **`3.85 / 5.00`** (Recommend: PURSUE - Priority Code-First Custom Agent, Decoupled from Initial Seat Launch) |

### 3.3 Template Card 3: `UC-005` - Internal IT & HR Employee Service Desk Triage Agent (`Gateway 2 No-Code Agent Builder`)

| Field | Baseline Template Response (Customize Bracketed Values per Organization) |
| :--- | :--- |
| **Use Case ID & Name** | `UC-005` - Internal IT & HR Employee Service Desk Policy Q&A and Ticket Triage Agent |
| **Business Unit & Owner** | IT Service Management (ITSM) & Human Resources (built by CoE Champions in **No-Code Agent Builder**) |
| **Target Users** | `<All Licensed Employees>` (Self-Service Tier-0/Tier-1 Support) and IT/HR Helpdesk Specialists |
| **Current Process & Friction** | IT and HR service desks receive high volumes of repetitive Tier-1 tickets covering leave policies, benefits, onboarding steps, VPN/SSO setup, and software requests (High Thin Work). |
| **Proposed AI Capability** | **Stage 2 Scoped Agent (`No-Code Agent Builder`)**: Grounded exclusively on curated HR policy workspaces and IT knowledge base articles; answers routine policy questions with exact section citations and drafts structured ITSM ticket summaries when human escalation is needed. |
| **Use Case Category & Risk Tier** | `Automation / Augmentation` - **Tier 2 (Medium Risk)** (`D2 Internal` and `D3 Confidential` employee support policies) |
| **Quantified Business Value** | **Set 2 Value Case**: Deflects routine Tier-1 how-to queries and accelerates ticket triage turnaround. |
| **Data & Grounding Readiness** | Curated HR/IT policy PDFs and sanitized ITSM resolution guides (`AI Readiness: 4.0 / 5.0`). |
| **Security & Controls** | Read-only grounding scope; inherits caller's corporate IdP ACLs; explicit *"Escalate to Human IT/HR Specialist"* path on every response; registered in `AIDecisionRegister` (`ADR-003` in [AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)). |
| **Weighted Priority Score** | **`4.15 / 5.00`** (Recommend: PURSUE - Priority No-Code Agent Builder Workflow) |

### 3.4 Blank Intake Card Template for New Business Unit Submissions (`UC-XXX`)

| Field | Submitter Input (Complete Ahead of CoE Intake Clinic) |
| :--- | :--- |
| **Use Case ID & Name** | `UC-<XXX>` - `<Descriptive Workflow Name>` |
| **Business Unit & Process Owner** | `<Business Unit / Department>` - `<Named Human Decision Owner & Title>` |
| **Target Users & Scope** | `<Target Roles & User Groups>` |
| **Current Process, SOP Link & Friction** | `<Link to Written SOP>` - `<Describe current manual steps and Thin Work friction>` |
| **Proposed AI Stage & Capability** | `<Stage 1 Grounded Search/Workspace OR Stage 2 Scoped/Code-First Agent with HITL>` |
| **Use Case Category & Risk Tier** | `<Augmentation / Analysis / Generation / Automation>` - `<Tier 1 / Tier 2 / Tier 3 / Tier 4>` |
| **Quantified Business Value Formula** | `<Hours saved/week x Active Users OR Cycle-time % reduction>` |
| **Data Sources & Highest Tier (`D1`-`D5`)** | `<Source Systems & D1-D5 Tier per AIAF-DOC-03>` |
| **Mandatory Security & HITL Controls** | `<Per-User OAuth ACLs, Read-Only Scope, Named Human Approver, Golden Eval Set>` |
| **6-Dimension Weighted Score** | `Value (__/5, 25%) / Data (__/5, 20%) / Risk Inv. (__/5, 20%) / Tech Feas. (__/5, 15%) / Strat Fit (__/5, 10%) / Time to Val (__/5, 10%) -> Composite: __/5.00` |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Use Case Classification (5 categories, 4 risk tiers), Reference Scenarios, and 6-Dimension Use Case Prioritization Rubric.
- [AIUseCaseCard.md](../Templates/AIUseCaseCard.md): Standalone blank use-case intake card template.
- [AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv): Standalone sortable portfolio backlog template.
- [References](../References.md): Maintained catalog of adoption and governance references.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Risk mapping and prioritization before system design.
