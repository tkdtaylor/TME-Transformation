<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-10` (AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE) Steering Committee, Executive Sponsors, Chief Information Officer (CIO) / Head of Enterprise IT, and Digital Transformation Leads |
| **Primary Internal Owner** | AI Center of Excellence (CoE) Lead & Head of Enterprise IT |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE) and internal teams assess readiness, benchmark maturity, and sequence their AI adoption roadmap. It is **not** prescriptive. Sections include illustrative baseline scores, readiness criteria, and phased milestone structures so teams do not have to start from a blank page. Organizations can share this template directly as an operational standard or customize the bracketed fields (`<Organization Name>`, `<Target Milestones>`) to fit their internal governance model.

## 1. How the AI CoE Can Create, Customize & Run a Readiness Scoring Session for This Document

### 1.1 Purpose & Why This Document Exists

Organizations scaling from an initial pilot to thousands of users often overestimate their operational readiness in some areas (such as assuming existing MLOps or standard IT change-management practices automatically cover generative AI prompts and retrieval indexes) while underestimating their strengths in others. This document provides the **AIAF 7-Perspective Maturity Scorecard, 20-Item AI Readiness Checklist, and Prioritized Phased Action Roadmap** aligned directly with the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) and Module 7 of the [Business Readiness Assessment Workshop](../Workshops/BusinessReadinessAssessment.md).

It exists to provide three quantitative governance tools for the AI Center of Excellence (CoE):

1. **7-Perspective AIAF Maturity Baseline (`1.0 Exploring` to `4.0 Transforming`)**: Measures current capability across all **7 Core Perspectives** (`Business Value`, `People & Workforce`, `AI Governance & Risk`, `Data & Knowledge`, `AI Platform & Integration`, `AI Security & Trust`, and `AI Operations & Quality`) on the standard `1.0 to 4.0` scale (`1: Exploring -> 2: Piloting -> 3: Scaling -> 4: Transforming`).
2. **20-Item AI Readiness Checklist (`>= 16 / 20` Threshold)**: Provides a binary, falsifiable check of whether the foundational policies, data rules, standard operating procedures (SOPs), identity controls, and support paths are in place before scaling to production users.
3. **AI CoE Evolution & Phased Action Roadmap**: Charts how the organization's AI Center of Excellence transitions from **Stage 1 (Gatekeeper)** during initial cutover to **Stage 2 (Enabler & Advisor)** and **Stage 3 (Platform & Self-Service)** as adoption matures across business units.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Internal Lead / Facilitator**: AI Center of Excellence (CoE) Lead and Enterprise IT Architecture Lead.
- **Required Internal Contributors**: Enterprise IT Architecture, Information Security (CISO), Data & Analytics Lead, HR / Enablement Lead, and Business Unit Representatives.
- **Reassessment Cadence**: Scored initially prior to production launch, then re-evaluated by the CoE on a quarterly cadence.

### 1.3 Recommended Approach: Running a CoE-Led Internal Readiness & Maturity Scoring Session

The CoE can establish and update this baseline by running a structured **internal scoring session** with the contributors above:

1. **Pre-Session Independent Scoring**: Send **Table 2.1** (7 Perspectives) and **Table 2.2** (20-Item Checklist) to IT, InfoSec, Data, and Enablement leads in advance so each lead scores their domain independently.
2. **Part 1 - Calibrate the 7-Perspective Maturity Scores (Section 2.1)**: Review the distinction between existing classical analytics/ML initiatives and the organization's corporate Generative AI baseline (`Level 2: Piloting`), reconcile any scoring differences, and lock the target maturity scores.
3. **Part 2 - Verify the 20-Item Readiness Checklist (Section 2.2)**: Walk through `CHK-01` to `CHK-20` item-by-item. Require a concrete internal artifact or configuration owner for every `YES (1)`, and verify the pre-launch remediation actions required to lift the organization's score to `>= 16 / 20` before production scaling.
4. **Part 3 - Assign Internal Milestone Owners (Section 3.3)**: Confirm named internal owners and target phases on the Action Roadmap (`ACT-01` to `ACT-07`).

## 2. 7-Perspective AIAF Maturity Scorecard & 20-Item Readiness Checklist (Template Baseline)

### 2.1 Seven-Perspective AIAF Maturity Scorecard (`1.0 Exploring -> 2.0 Piloting -> 3.0 Scaling -> 4.0 Transforming`)

| AIAF Perspective | Primary AIAF Focus | Baseline Score (Illustrative) | Target State | Net Gap | Representative Enterprise Baseline Evidence & Target State |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **1. Business Value Perspective** | Strategy, Value Case & Portfolio | **2.5 (Piloting+)** | **4.0 (Transforming)** | `+1.5` | Executive sponsorship established; quantified productivity and workflow value case defined across priority use-case families and multi-wave license ramp ([AIAF-DOC-07](07_StrategicDriversAndThinValuedWork.md)). |
| **2. People & Workforce Perspective** | Enablement, Culture & Thin-to-Valued | **2.0 (Piloting)** | **3.5 (Scaling+)** | `+1.5` | Initial pilot cohort completed evaluation; structured **3-Track Enablement** (`L100` All Users, `L200` Departmental Champions, `L300` Technical Builders + Executive Track) launching for initial rollout. |
| **3. AI Governance & Risk Perspective** | Policy, AIIA & Decision Register | **2.0 (Piloting)** | **3.5 (Scaling+)** | `+1.5` | Corporate IT and compliance policies established; standing up formal **2-Gateway Governance Model**, `AIDecisionRegister`, and Tier 2/3 `AIIA` sign-off processes ([AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md), [AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md), [AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)). |
| **4. Data & Knowledge Perspective** | Classification, Grounding & Reuse | **2.0 (Piloting)** | **3.5 (Scaling+)** | `+1.5` | Core enterprise knowledge resides in cloud collaboration suites, ERP, ITSM, and data lakehouses; implementing **Hybrid Grounding** and **25-50 Q&A Golden Datasets** ([AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md), [AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)). |
| **5. AI Platform & Integration Perspective** | Gateway, Runtime & Model Abstraction | **2.0 (Piloting)** | **4.0 (Transforming)** | `+2.0` | Transitioning from sandbox pilot to production **Enterprise AI Platform** instance with federated Identity Provider (IdP) SAML 2.0 SSO and SCIM 2.0 group provisioning. |
| **6. AI Security & Trust Perspective** | Perimeter, ACLs & Runtime Guardrails | **2.5 (Piloting+)** | **4.0 (Transforming)** | `+1.5` | Enforcing external B2B guest account exclusion, Private Network Perimeter (VPC / Private Link), Customer-Managed Encryption Keys (CMEK), Runtime AI Guardrail Service screening, and per-user OAuth 2.0 source ACL inheritance. |
| **7. AI Operations & Quality Perspective** | GenAIOps, Evals & Seat Governance | **1.5 (Exploring+)** | **3.0 (Scaling)** | `+1.5` | Standing up enterprise **GenAIOps** practices: automated Golden Dataset regression testing, 3-Tier CoE issue triage, and 60-day inactive license reclamation ([AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md), [AIAF-DOC-09](09_ValueRealizationAndSeatGovernanceSOP.md)). |
| **COMPOSITE AIAF MATURITY** | **All 7 Perspectives** | **`2.1 / 4.0` (Piloting)** | **`3.6 / 4.0` (Transforming)** | **`+1.5`** | **Current AI CoE Stage**: Transitioning from **Stage 1 (Gatekeeper)** to **Stage 2 (Enabler & Advisor)** across rollout phases. |

### 2.2 The 20-Item AI Readiness Checklist (`Target Threshold >= 16 / 20`)

| Category | Item # | Readiness Checklist Criterion | Pilot Baseline (Example) | Pre-Launch Target | Required Verification Evidence & Remediation Action |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Governance & Policy** | `CHK-01` | An AI Acceptable Use Policy exists and is communicated to employees. | **YES (1)** | **YES (1)** | Adopt and distribute [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md) (`AIAF-DOC-04`) in Day-1 onboarding. |
| **Governance & Policy** | `CHK-02` | A formal process exists to evaluate and approve AI tools (`ApprovedAIToolRegistry`). | **YES (1)** | **YES (1)** | Enforce the 2-Gateway Governance Model and `ApprovedAIToolRegistry` ([AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) & [AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)). |
| **Governance & Policy** | `CHK-03` | Data classification rules (`D1`-`D5`) for AI usage are defined. | *GAP (0)* | **YES (1)** | Ratify the 5-Tier `D1`-`D5` Data Classification Matrix in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) and [AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md). |
| **Governance & Policy** | `CHK-04` | An AI-specific incident response and issue triage plan exists. | *GAP (0)* | **YES (1)** | Adopt [06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook](06_AISecurityIncidentAndKillSwitchRunbook.md) (`AIAF-DOC-06`) and 3-Tier CoE support routing. |
| **Data & Knowledge** | `CHK-05` | A data inventory exists with named Data Stewards for major domains. | **YES (1)** | **YES (1)** | Assign Data Stewards across document collaboration, ERP, ITSM, and analytics repositories in [AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md). |
| **Data & Knowledge** | `CHK-06` | Regulated (`D5`) and restricted (`D4`) data are segregated from general prompts. | **YES (1)** | **YES (1)** | Isolate `D5` regulated/critical systems from cloud prompts; restrict `D4` to ACL-scoped enclaves ([AIAF-DOC-03](03_DataClassificationMatrixAndSourceRegister.md)). |
| **Data & Knowledge** | `CHK-07` | Data quality has been assessed for top candidate use cases. | *GAP (0)* | **YES (1)** | Score domain readiness in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) Section 2.2 and apply Layout-Aware Document Parser for complex tabular PDFs. |
| **Data & Knowledge** | `CHK-08` | Data residency requirements are mapped for operating jurisdictions. | **YES (1)** | **YES (1)** | Confirm approved multi-region boundary (`global`, `us`, or `eu`) with Legal and Data Protection Officer (DPO). |
| **Data & Knowledge** | `CHK-09` | Inference-time grounding and model weight training are governed separately. | **YES (1)** | **YES (1)** | Codify the Mandatory Inference-Time Grounding Standard (`zero model weight training` on enterprise data) in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md). |
| **People & Workforce** | `CHK-10` | Executive leadership shares a realistic understanding of AI capabilities. | **YES (1)** | **YES (1)** | Ratify [01 Enterprise AI Strategy Charter](01_EnterpriseAIStrategyCharter.md) (`AIAF-DOC-01`) and run Executive Briefing Track. |
| **People & Workforce** | `CHK-11` | Employees receive baseline AI literacy and safe-prompting training. | *GAP (0)* | **YES (1)** | Deliver Track 3 (`L100`) Mass Onboarding, role-based prompt templates (`R-C-T-V`), and citation-checking rules. |
| **People & Workforce** | `CHK-12` | A clear feedback channel exists to report AI quality or safety issues. | *GAP (0)* | **YES (1)** | Stand up 3-Tier CoE Triage intake (`Tier 1` Champions -> `Tier 2` Internal IT -> `Tier 3` Platform Vendor Support). |
| **People & Workforce** | `CHK-13` | Workforce impact on roles and manager transition needs are assessed. | *GAP (0)* | **YES (1)** | Complete Thin-vs.-Valued Work Assessment and Manager Transition Plan in [AIAF-DOC-07](07_StrategicDriversAndThinValuedWork.md) Section 4. |
| **Process & Workflow** | `CHK-14` | Standard Operating Procedures (SOPs) exist for top candidate workflows. | **YES (1)** | **YES (1)** | Verify written SOPs exist before approving use cases in [08 AI Use Case Intake Cards](08_AIUseCaseIntakeAndPortfolioBacklog.md) (`AIAF-DOC-08`). |
| **Process & Workflow** | `CHK-15` | Decision points, exceptions, and human handoffs (HITL) are documented. | *GAP (0)* | **YES (1)** | Define mandatory Human-in-the-Loop (`HITL`) approval gates in [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md) and [AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md). |
| **Process & Workflow** | `CHK-16` | Tasks are classified into Thin Work (machine-ready) vs. Valued Work (human). | *GAP (0)* | **YES (1)** | Complete Thin-vs.-Valued Work decomposition across core capabilities in [AIAF-DOC-07](07_StrategicDriversAndThinValuedWork.md). |
| **Technology & Platform** | `CHK-17` | Identity federation (SSO/SCIM) and service principals are centrally managed. | **YES (1)** | **YES (1)** | Verify Enterprise IdP directory cap, SAML 2.0 / SCIM 2.0 sync, and external B2B guest filtering. |
| **Technology & Platform** | `CHK-18` | Audit logging and 3-Tier User Success KPI telemetry are defined. | **YES (1)** | **YES (1)** | Enable Analytics Lakehouse usage audit logs and monthly ROI / seat hygiene metrics in [AIAF-DOC-09](09_ValueRealizationAndSeatGovernanceSOP.md). |
| **Technology & Platform** | `CHK-19` | At least one use case was piloted in a controlled sandbox with baseline metrics. | **YES (1)** | **YES (1)** | Document pilot evaluation outcomes and defect resolution in [11 Pilot-to-Production (P2P) Gate](11_PilotToProductionGatePackage.md) (`AIAF-DOC-11`). |
| **Technology & Platform** | `CHK-20` | A structured evaluation dataset mechanism exists for authoritative workflows. | *GAP (0)* | *Phase 2 (0)* | Curate 25-50 Q&A Golden Datasets for departmental workspaces ([AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)) and 100-sample sets for code-first custom agents ([AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)). |
| **TOTAL CHECKLIST SCORE** | - | **Phase 3 Production Entry Threshold: `>= 16 / 20`** | **`11 / 20`** | **`19 / 20`** | **Exceeds the `16 / 20` threshold required to pass the Pilot-to-Production (`P2P`) Gate.** |

## 3. Organization Starting Point Profile, CoE Evolution & Action Roadmap

### 3.1 Eleven-Dimension Organization Starting Point Profile (Template)

| Dim # | Profile Dimension | Enterprise Baseline Synthesis & Target Pattern (Customize per Organization) |
| :---: | :--- | :--- |
| `DIM-01` | **Business Context & Top 3 Drivers** | `<Organization Name>` (`<Industry / Sector>`, `<Annual Revenue / Scale>`, `<Employee Count & Geographies>`) anchoring AI investment on: (1) `<Driver 1: e.g., Knowledge Productivity & Operational Cost Efficiency>`, (2) `<Driver 2: e.g., Cross-System Decision Speed>`, and (3) `<Driver 3: e.g., Regulatory Compliance & Institutional Knowledge Continuity>`. |
| `DIM-02` | **Distinctive Core Capabilities** | Core revenue-generating and operational capabilities (`CAP-01` to `CAP-10` in [AIAF-DOC-07](07_StrategicDriversAndThinValuedWork.md)) where AI accelerates knowledge synthesis, exception handling, and decision turnaround. |
| `DIM-03` | **Proprietary Data Strengths** | Authoritative enterprise policies, engineering/operations SOPs, contract libraries, ERP financial ledgers, ITSM ticket histories, and analytical lakehouse tables. |
| `DIM-04` | **Critical Data & Knowledge Risks** | Cross-department or cross-subsidiary `D4 Restricted` data exposure if source ACLs are bypassed; retrieval truncation on dense multi-column PDFs and large tabular exports (`>500,000` words) unless routed via Hybrid Grounding and Code Execution. |
| `DIM-05` | **Shadow AI & Vendor Bypass Status** | High employee demand for AI assistance is channeled into the sanctioned **Enterprise AI Platform**, avoiding fragmented single-silo SaaS AI add-on markups ([AIAF-DOC-14](14_VendorAIProcurementChecklist.md)). |
| `DIM-06` | **AIAF Overall Maturity & CoE Stage** | Composite Maturity **`2.1 / 4.0` (Piloting)** targeting **`3.6 / 4.0` (Transforming)**; AI CoE evolving from **Stage 1: Gatekeeper** to **Stage 2: Enabler & Advisor**. |
| `DIM-07` | **Technology & Identity Context** | Enterprise architecture anchored on `<Corporate Identity Provider (IdP)>`, `<Enterprise Collaboration & Document Suite>`, `<Enterprise ERP / ITSM Platform>`, and `<Cloud Data Lakehouse>`. |
| `DIM-08` | **Top AI Disruption Risks** | Manual multi-system financial/operational reconciliation, repetitive Tier-1 IT/HR service desk triage, and siloed document retrieval consuming significant Thin Work capacity. |
| `DIM-09` | **Top AI Value Opportunities** | **Set 1 Day-1 Quick Wins** via Enterprise Grounded Search, Grounded Knowledge Notebooks, and Enterprise Deep Research; **Set 2 Agentic Workflows** via No-Code Agent Builder and Code-First Custom Agents. |
| `DIM-10` | **Primary Adoption Bottleneck** | Completing production identity/connector cutover, ratifying `D1`-`D5` governance guardrails, and nominating Early-Access CoE Champions plus initial rollout users. |
| `DIM-11` | **Readiness Score & Lifecycle Phase** | **`19 / 20`** upon adopting this foundational document suite (up from `11 / 20` pilot baseline), clearing the **Pilot-to-Production (P2P) Gate** for Phase 3 (Deploy & Integrate). |

### 3.2 AI Center of Excellence (CoE) Operating Model Evolution (`Gatekeeper -> Enabler -> Platform`)

```
+-----------------------------------------------------------------------+
|         ENTERPRISE AI CENTER OF EXCELLENCE (CoE) EVOLUTION            |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 1: GATEKEEPER MODEL (Phase 1 - Pre-Launch & Initial Launch)    |
|  * Central IT & AI CoE review all data connectors & Gateway 2 agents. |
|  * Lock external B2B guest filtering & P2P Gate prior to launch.      |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 2: ENABLER & ADVISOR MODEL (Phase 2 - Cross-BU Expansion)      |
|  * CoE Champions & L200 builders use pre-approved Knowledge Workspace |
|    and No-Code Agent Builder templates in Gateway 1.                  |
|  * 3-Tier CoE deflects >= 70% of how-to and prompt coaching tickets.  |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 3: PLATFORM & SELF-SERVICE MODEL (Phase 3 - Steady State)      |
|  * Automated policy gates embedded in platform (Runtime Guardrails,   |
|    source ACLs, Automated Eval CI/CD, 60-day license recycling).      |
+-----------------------------------------------------------------------+
```

### 3.3 Prioritized Phased Action Roadmap

| Horizon | Action ID | Priority Milestone & Deliverable | Target Window | Accountable Owner & Partners |
| :--- | :---: | :--- | :---: | :--- |
| **Phase 0: Pre-Launch** | `ACT-01` | **Close Pilot Issues Register & Lock Enablement Plan**: Conduct pre-launch working session; finalize 3-Track Enablement (`L100/L200/L300`), 3-Tier CoE Triage Model, and KPI Matrix. | `Pre-Launch Gate` | Enterprise IT, Digital Transformation & AI CoE |
| **Phase 0: Pre-Launch** | `ACT-02` | **Nominate Early-Access CoE Champions & Initial Rollout Users**: Provision identity security groups (`SG-AI-Enterprise-Champions` and `SG-AI-Enterprise-Users`) in corporate IdP. | `Pre-Launch Gate` | Business Unit Heads & Enterprise Identity Admin |
| **Phase 0: Pre-Launch** | `ACT-03` | **Production Instance Cutover & Champion Early Access**: Verify Enterprise IdP directory cap, SAML/SCIM sync with B2B guest filtering, network egress, and onboard CoE Champions first. | `Cutover Gate` | Enterprise IT Platform & Identity Team |
| **Phase 1: Initial Rollout** | `ACT-04` | **Initial Launch & Track 3 (`L100`) Mass Enablement**: Activate Day-1 onboarding ([AIAF-DOC-04](04_EmployeeAcceptableUseGuide.md)), enterprise search connectors, curated workspaces ([AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)), and floorwalking clinics. | `Initial Launch` | AI CoE Enablement Lead, IT & BU Champions |
| **Phase 2: Agent Expansion** | `ACT-05` | **Seat Expansion & Initial Gateway 2 Agents**: Expand seat allocation and deploy priority No-Code Agent Builder workflows and Code-First Custom Agents with Golden Datasets ([AIAF-DOC-08](08_AIUseCaseIntakeAndPortfolioBacklog.md), [AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)). | `Expansion Phase` | AI Engineering Team & Business Unit Decision Owners |
| **Phase 3: Broad Rollout** | `ACT-06` | **Broad Rollout & First 60-Day Seat Reclamation**: Complete enterprise license ramp; execute first 60-day inactivity license reclamation ([AIAF-DOC-09](09_ValueRealizationAndSeatGovernanceSOP.md)) and 90-day Readiness Reassessment. | `First 60-Day Review` | AI CoE Steering Committee, Finance & Identity Admin |
| **Phase 4: Steady-State Scale** | `ACT-07` | **Multi-Region Expansion & Stage 3 Self-Service Platform**: Evaluate regional data residency enclaves as required ([AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md)), expand read-only MCP connectors, and transition CoE to Stage 3. | `Ongoing Operations` | Enterprise IT, AI CoE, InfoSec & Legal |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Seven Core Perspectives, AI Maturity Model (`1: Exploring` to `4: Transforming`), and AI CoE Operating Model Evolution.
- [Business Readiness Assessment Workshop](../Workshops/BusinessReadinessAssessment.md): Module 7 (Maturity & Readiness Scoring) and Module 8 (Starting Point Summary & Priorities).
- [References](../References.md): Maintained catalog of regulatory, security, and operational standards.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Organizational AI maturity and governance measurement.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Continual improvement, management review, and readiness verification.
