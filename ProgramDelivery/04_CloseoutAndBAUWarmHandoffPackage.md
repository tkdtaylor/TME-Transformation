<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 04 Closeout & BAU Warm Handoff Package

Use this package at Milestone `M5` to close out an initial rollout program and cleanly transfer operational, financial, security, and governance ownership from temporary rollout teams to steady-state business-as-usual (BAU) owners.

## 1. Executive Closeout Briefing Outline (8-Slide Assertion-Evidence Structure)

| Slide # | Action Headline (Assertion) | Required Evidence & Visuals | Companion Source(s) |
| :---: | :--- | :--- | :--- |
| **1** | **Program delivered verified Thin-to-Valued capacity and adoption targets** | Baseline-vs.-actual chart for `VAL-01` (activation and WAU/MAU), `VAL-02` (hours reclaimed), `VAL-03` (cycle-time delta), and `VAL-04` (avoided SaaS spend). | [09_ValueRealizationAndSeatGovernanceSOP.md](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md) |
| **2** | **All live capabilities cleared the 10-Dimension Pilot-to-Production Gate** | Summary of production workloads, `P2P-01` to `P2P-10` status, and active `AIDecisionRegister` entries (`ADR-*`). | [11_PilotToProductionGatePackage.md](../AIFoundationalSuite/11_PilotToProductionGatePackage.md), [AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv) |
| **3** | **60-day seat reclamation and FinOps controls keep unit economics within budget** | Reclaimed vs. reallocated seats, token cost per task trend, model-tier routing ratio, and budget alert history. | [09_ValueRealizationAndSeatGovernanceSOP.md](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md) |
| **4** | **Zero critical security breaches; kill-switch drills and RAI gates operate as designed** | Summary of `KSD-001` to `KSD-004` measured containment times, OWASP `LLM01`-`LLM10` audit status, and Golden Dataset scores. | [06_AISecurityIncidentAndKillSwitchRunbook.md](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md), [12_AIImpactAssessmentAndOWASPControls.md](../AIFoundationalSuite/12_AIImpactAssessmentAndOWASPControls.md) |
| **5** | **Workforce enablement shifted teams from ad-hoc prompting to curated reuse** | `L100/L200/L300` completion rates, active curated workspaces (`CAT-*`), and cross-team asset reuse rate. | [05_KnowledgeNotebookAndPromptPlaybook.md](../AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md) |
| **6** | **Key lessons learned address data readiness and workflow SOP prerequisites** | Top 3 technical/process friction points resolved during rollout and guardrails added to intake clinics. | [08_AIUseCaseIntakeAndPortfolioBacklog.md](../AIFoundationalSuite/08_AIUseCaseIntakeAndPortfolioBacklog.md) |
| **7** | **BAU ownership, on-call paths, and recurring governance cadences are transferred** | Summary of the Five-Part Warm Handoff Charter (Section 2 below) with named day-job owners and SLAs. | Section 2 of this document |
| **8** | **Phase 5-6 optimization and next-wave roadmap are prioritized and funded** | Updated AIAF 7-perspective maturity score (`1.0` to `4.0`), CoE evolution toward Stage 2/3, and next-quarter backlog. | [10_AIMaturityScorecardAndReadinessRoadmap.md](../AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md) |

### Closeout Evidence Packet Checklist

Assemble these five evidence items ahead of the Executive Closeout Briefing so steady-state acceptance relies on verified metrics rather than qualitative summaries:

- [ ] **Outcome Telemetry Snapshot**: Exported `VAL-01` through `VAL-04` metrics covering at least two complete 30-day cycles (`09_ValueRealizationAndSeatGovernanceSOP.md`).
- [ ] **Security & Drill Attestation**: Signed `KSD-001` through `KSD-004` kill-switch drill timestamps (`<= 15 mins`) and zero unresolved `SEV-1` or `SEV-2` findings (`06_AISecurityIncidentAndKillSwitchRunbook.md`).
- [ ] **Gate & Impact Records**: Archived `PilotToProductionGate` and Tier 2+ `AIImpactAssessment` sign-offs for every live capability (`11`, `12`).
- [ ] **FinOps Tagging & Budget Verification**: Confirmed cost-allocation tags (`bu`, `use_case`, `env`, `cost_center`) and active `50%/80%/100%` billing alerts.
- [ ] **Updated Governance Registers**: Current `AIDecisionRegister.csv`, `ApprovedAIToolRegistry.csv`, and `AIUseCaseBacklog.csv` entries with named owners (`13`).

---

## 2. Five-Part BAU Warm Handoff Charter

### Part 1: Delivered Capabilities, Active Connectors & Verified Outcome Baseline

| Deliverable ID | Capability / Connector / Agent | Risk Tier & Gateway | Baseline Metric -> Achieved Outcome | Verification Artifact |
| :--- | :--- | :---: | :--- | :--- |
| `<DEL-001>` | `<e.g., Enterprise AI Assistant & Federated Repo Search>` | `Tier 1-2 / Gateway 1` | `<e.g., 88% activation, 54% WAU/MAU>` | `<Telemetry dashboard link>` |
| `<DEL-002>` | `<e.g., Curated Departmental Workspaces (CAT-001..008)>` | `Tier 2-3 / Gateway 1` | `<e.g., >= 90% Golden Eval groundedness>` | `<Eval report link>` |
| `<DEL-003>` | `<e.g., Code-First Custom Agent (UC-004)>` | `Tier 3 / Gateway 2` | `<e.g., Close commentary cycle -45%>` | `<P2P Gate & AIIA links>` |

### Part 2: Production & On-Call Ownership Transfer

| Operational Domain | Named Day-Job Owner (Role & Person) | Support Channel & Response SLA | Primary Runbook / Escalation Path |
| :--- | :--- | :--- | :--- |
| **Platform, Identity & Connectors** | `<Head of Enterprise IT Platform>` | `<ITSM Queue / Sev-1 <= 15 min>` | [03_DataClassificationMatrixAndSourceRegister.md](../AIFoundationalSuite/03_DataClassificationMatrixAndSourceRegister.md) |
| **AI Security & Kill Switch** | `<CISO / SOC Incident Lead>` | `<24x7 SOC Bridge / <= 15 min>` | [06_AISecurityIncidentAndKillSwitchRunbook.md](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md) |
| **Custom Agents (`Gateway 2`)** | `<Enterprise AI Engineering Lead>` | `<Agent Ops On-Call / <= 30 min>` | [03_AgentRequirementAndDesignSpec.md](03_AgentRequirementAndDesignSpec.md) |
| **CoE Enablement & Triage** | `<Steady-State AI CoE Lead>` | `<Tier-1 Champion Channel / 1 BD>` | [05_KnowledgeNotebookAndPromptPlaybook.md](../AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md) |
| **FinOps & License Hygiene** | `<IT Identity Admin & Finance Partner>` | `<Monthly FinOps Review>` | [09_ValueRealizationAndSeatGovernanceSOP.md](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md) |

### Part 3: Living Governance Registers & Recurring Cadence Calendar

| Recurring Governance Activity | Cadence | Responsible Role | Register / Artifact Updated |
| :--- | :---: | :--- | :--- |
| **Inactive Seat Nudge & Reclamation** | Day 30 / 45 / 60 | Identity Admin & CoE Ops | IdP license group + `VAL-01` dashboard |
| **Knowledge Workspace Freshness Attestation** | Every 90 days | `L200` Departmental Curators | `CAT-001`..`CAT-008` in [05](../AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md) |
| **Kill-Switch Containment Drills (`KSD-001`..`004`)** | Every 90 days | SOC Lead & Platform Ops | Drill log in [06](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md) |
| **Decision & Approved Tool Register Audit** | Quarterly (Monthly Tier 3+) | CoE Ops Lead & InfoSec | [AIDecisionRegister.csv](../Templates/AIDecisionRegister.csv), [ApprovedAIToolRegistry.csv](../Templates/ApprovedAIToolRegistry.csv) |
| **AIAF Maturity & Readiness Re-Scoring** | Quarterly | AI CoE Steering Committee | [10_AIMaturityScorecardAndReadinessRoadmap.md](../AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md) |
| **Tier 3/4 AIIA & Golden Eval Regression Review** | Quarterly / On Model Change | Decision Owner & Eval Engineer | [AIImpactAssessment.md](../Templates/AIImpactAssessment.md) |

### Part 4: Open Risks, Conditional Approvals & Prioritized Next-Wave Backlog

| Item ID | Category (`Open Risk / P2P Condition / Next Wave`) | Description & Impact | Named Owner | Target Resolution Date |
| :--- | :--- | :--- | :--- | :---: |
| `<OPN-001>` | `<e.g., Conditional Approval>` | `<e.g., Complete multi-region data residency sign-off for Region B>` | `<Legal / DPO>` | `<YYYY-MM-DD>` |
| `<OPN-002>` | `<e.g., Next-Wave Backlog>` | `<e.g., Promote UC-006 Analytics Agent from Phase 2 to P2P Gate>` | `<Data & Analytics Lead>` | `<YYYY-MM-DD>` |

### Part 5: Formal BAU Handoff Sign-Off

| Handoff Role | Designated Signer (Name & Title) | Decision (`Accepted / Conditional`) | Sign-Off Date | Conditions / Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Outgoing Program Lead** | `<Name & Title>` | `<Accepted>` | `<YYYY-MM-DD>` | All `M0`-`M4` evidence archived |
| **Incoming Steady-State CoE Lead** | `<Name & Title>` | `<Accepted / Conditional>` | `<YYYY-MM-DD>` | Assumes intake, cadence & register custody |
| **Platform & IT Operations Lead** | `<Name & Title>` | `<Accepted / Conditional>` | `<YYYY-MM-DD>` | Assumes production runbooks & on-call SLA |
| **CISO / InfoSec Representative** | `<Name & Title>` | `<Accepted / Conditional>` | `<YYYY-MM-DD>` | Confirms drill schedule & audit logging |
| **Business Unit Owner(s)** | `<Name & Title>` | `<Accepted / Conditional>` | `<YYYY-MM-DD>` | Confirms `Decision Owner` accountability |

---

## 3. Pre-Handoff Verification & 30-Day Post-Handoff Check

Confirm all operational transfer steps before formally closing the rollout program:

- [ ] Usage telemetry, FinOps budget alerts (`50%/80%/100%`), and 60-day license reclamation scripts run under steady-state service principals.
- [ ] All production runbooks, architecture diagrams, and Golden Datasets live in durable team repositories with backup custodians assigned.
- [ ] Temporary project implementation accounts and elevated deployment permissions are revoked following cutover.
- [ ] `AIDecisionRegister.csv`, `ApprovedAIToolRegistry.csv`, and `AIUseCaseBacklog.csv` reflect live production state with scheduled review dates.
- [ ] **Post-Handoff 30-Day Stabilization Check** scheduled on the CoE Steering Committee calendar (`<YYYY-MM-DD>`) to confirm zero unowned incidents or SLA drift.

## References & Companion Frameworks

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Phase 4 (Govern & Control), Phase 5 (Optimize & Measure), Phase 6 (Scale & Innovate), and CoE Operating Model Evolution.
- [Technology Adoption Framework (TAF)](../TechAdoptionFramework.md): Phase 5 (Optimize & Manage), Operations & Management Perspective, and SRE/FinOps handover standards.
- [References](../References.md): External regulatory, security, and FinOps standards with review cadences.
