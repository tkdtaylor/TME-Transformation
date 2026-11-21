<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# AI Foundational Suite

A vendor-neutral, 15-document operational governance and implementation starter suite (`00` through `14`) designed to help an organization's **AI Center of Excellence (CoE)** operationalize the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) from Day-0 executive mandate through custom agent production gates and continuous GenAIOps.

All documents in this folder are **non-prescriptive reference templates** pre-populated with industry-agnostic enterprise baselines so internal teams do not have to start from a blank page. Adapt, consolidate, or replace any document to fit your internal risk appetite, regulatory regime, and technology stack.

---

## How to Use This Suite

1. **Start with the Production Guide:** Read [00 CoE Production Guide](00_CoEProductionGuide.md) for the chronological priority order, internal ownership roles, and working-session facilitation pattern across all four execution tiers.
2. **Anchor in the Parent Framework:** Use the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) for the full lifecycle, 7 Core Perspectives, maturity model, and RACI definitions, and consult [References](../References.md) for underlying standards and regulatory review cadences.
3. **Pair Prose Playbooks with Blank Working Templates:** Use the standalone Markdown forms and CSV registers in [Templates](../Templates/README.md) when capturing live intake cards, impact assessments, gate sign-offs, and operational registers.

---

## Document Catalog (`00` to `14` Across 4 Execution Tiers)

### Master Overview

| Doc # | Document | Purpose | Typical Internal Owner |
| :---: | :--- | :--- | :--- |
| **`00`** | [00 CoE Production Guide](00_CoEProductionGuide.md) | Master overview, priority sequencing across 4 execution tiers, and internal CoE production instructions | AI CoE Lead & Digital Transformation Lead |

### Tier 1: Day-0 Executive Mandate & Core Data / Workforce Guardrails (`01` to `04`)

| Doc # | Document | Purpose | Typical Internal Owner |
| :---: | :--- | :--- | :--- |
| **`01`** | [01 Enterprise AI Strategy Charter & Public AI Trust Statement](01_EnterpriseAIStrategyCharter.md) | Dual-speed AI strategy, 8 "We Will / We Will Not" trade-off principles (`STR-01` to `STR-08`), and public trust statement | Executive Sponsors, Transformation Lead & Corporate Comms |
| **`02`** | [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) | Binding corporate AI policy, `D1`-`D5` tiers, 7 AI knowledge asset classes (`KNA-01` to `KNA-07`), and 5 Non-Human Actor personas (`NHA-01` to `NHA-05`) | CISO / InfoSec, DPO, Head of IT & AI CoE Lead |
| **`03`** | [03 AI Data Classification Matrix & Enterprise Data Source Control Register](03_DataClassificationMatrixAndSourceRegister.md) | `D1`-`D5` x 10 AI tool surface matrix plus 12-repository Enterprise Data Source Control Register (`SRC-001` to `SRC-012`) | CISO / InfoSec, Data Governance & System Owners |
| **`04`** | [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md) | 5 Golden Rules, `GREEN / AMBER / RED` desk guide, 10-second safety check, and onboarding acknowledgement | AI CoE, HR, Internal Comms & InfoSec |

### Tier 2: Wave-1 Value Enablement, Emergency Safety Net & Use-Case Selection (`05` to `08`)

| Doc # | Document | Purpose | Typical Internal Owner |
| :---: | :--- | :--- | :--- |
| **`05`** | [05 Departmental Knowledge Notebook & Prompt Library Curation Playbook](05_KnowledgeNotebookAndPromptPlaybook.md) | 5-stage curation SOP, `R-C-T-V` prompt pattern, 90-day freshness attestation, and catalog (`CAT-001` to `CAT-008`) | AI CoE Enablement Lead & BU Champions |
| **`06`** | [06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook](06_AISecurityIncidentAndKillSwitchRunbook.md) | `SEV-1` to `SEV-4` matrix, 5-layer `<15-minute` containment hierarchy, CLI runbooks, and quarterly drill log (`KSD-001` to `KSD-004`) | CISO / SOC Incident Response, AI CoE & IT Ops |
| **`07`** | [07 Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment](07_StrategicDriversAndThinValuedWork.md) | 14 strategic drivers (`DRV-01` to `DRV-14`), hard constraints (`CON-01` to `CON-06`), 10 capabilities (`CAP-01` to `CAP-10`), and Thin-vs.-Valued matrix | AI CoE Lead, Strategy Lead & BU Heads |
| **`08`** | [08 AI Use Case Intake Cards & Scored Portfolio Backlog](08_AIUseCaseIntakeAndPortfolioBacklog.md) | 6-dimension weighted prioritization rubric, scored backlog (`UC-001` to `UC-010`), and sample intake cards | AI CoE Intake Lead & BU Champions |

### Tier 3: FinOps Seat Governance & Capability Maturity Roadmap (`09` to `10`)

| Doc # | Document | Purpose | Typical Internal Owner |
| :---: | :--- | :--- | :--- |
| **`09`** | [09 AI Value Realization, FinOps & 60-Day License Governance SOP](09_ValueRealizationAndSeatGovernanceSOP.md) | Finance-approved ROI formulas (`VAL-01` to `VAL-04`), 30/45/60-day inactive seat reclamation SOP, and 11 FinOps cost levers | AI CoE Program Lead, Finance & Identity Admin |
| **`10`** | [10 AI Maturity Scorecard, 20-Item Readiness Checklist & Action Roadmap](10_AIMaturityScorecardAndReadinessRoadmap.md) | 7-perspective AIAF maturity baseline (`1.0` to `4.0`), 20-item checklist (`CHK-01` to `CHK-20`), CoE evolution model, and action roadmap | AI CoE Steering Committee & Head of Enterprise IT |

### Tier 4: Custom Agent Production Gates, Deep Risk, GenAIOps & Procurement (`11` to `14`)

| Doc # | Document | Purpose | Typical Internal Owner |
| :---: | :--- | :--- | :--- |
| **`11`** | [11 Pilot-to-Production (P2P) Gate Review Package](11_PilotToProductionGatePackage.md) | 10-dimension Production Readiness Gate (`P2P-01` to `P2P-10`), pilot outcome summary, and Go/No-Go sign-off record | AI CoE Lead, Platform Lead & InfoSec Lead |
| **`12`** | [12 AI Impact Assessment (AIIA), Measurable RAI & OWASP LLM Controls](12_AIImpactAssessmentAndOWASPControls.md) | 5-step AIIA baseline, falsifiable RAI test thresholds, and OWASP `LLM01`-`LLM10` technical control matrix | BU Decision Owner & AI Governance / InfoSec |
| **`13`** | [13 Operational Governance Registers & GenAIOps Guide](13_OperationalGovernanceRegistersAndGenAIOps.md) | Decision Register (`ADR-001` to `ADR-006`), Approved Tool Registry (`TOOL-001` to `TOOL-006`), Data Dictionary, and 3-step GenAIOps flywheel | AI CoE Operations Lead & IT Governance Lead |
| **`14`** | [14 Third-Party SaaS & Vendor AI Procurement Assessment Checklist](14_VendorAIProcurementChecklist.md) | 2-stage procurement gate (Stage 1 Core Platform Bypass Check + Stage 2 `VND-001` to `VND-010` TPRM checklist) | Procurement, CISO / InfoSec, Legal & AI CoE |

---

## Companion Blank Templates

The narrative baselines in this folder pair directly with the blank working templates in [Templates](../Templates/README.md):

- **Use Case Intake & Backlog (`08`)**: [AIUseCaseCard.md](../Templates/AIUseCaseCard.md) and [AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv)
- **Pilot-to-Production Gate (`11`)**: [PilotToProductionGate.md](../Templates/PilotToProductionGate.md)
- **AI Impact Assessment (`12`)**: [AIImpactAssessment.md](../Templates/AIImpactAssessment.md)
- **Operational Registers & Data Dictionary (`13`)**: [AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv), [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv), and [DataDictionary.md](../Templates/DataDictionary.md)
