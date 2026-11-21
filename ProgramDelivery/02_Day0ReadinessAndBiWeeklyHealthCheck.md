<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 02 Day-0 Readiness & Bi-Weekly Health Check

This runbook defines the technical and governance gates required before opening general user access (`Day 0`), tracks milestone progression from `M0` through `M5`, and establishes eight bi-weekly health signals (`HC-01` to `HC-08`) with explicit corrective triggers.

## 1. Seven Day-0 Pre-Launch Readiness Gates (`RDY-01` to `RDY-07`)

No production cohort may go live until all seven gates show verified evidence.

| Gate ID | Readiness Gate | Minimum Verification Evidence | Accountable Owner | Status |
| :---: | :--- | :--- | :--- | :---: |
| **`RDY-01`** | **SSO / SCIM & External Guest Exclusion** | Corporate IdP SAML/OIDC SSO live; SCIM filter (`userType EQUALS 'Member'`) tested to block external B2B guests from AI license groups. | Identity & Platform Lead | `<Pending / Ready>` |
| **`RDY-02`** | **Network & Regional Data Boundary** | Private network perimeter / egress allowlists active; tenant pinned to approved data residency region (`global`, `us`, or `eu`); CMEK verified where required. | Cloud Platform & Security Lead | `<Pending / Ready>` |
| **`RDY-03`** | **`D1`-`D5` Source Register Approved** | Authoritative sources mapped in [03_DataClassificationMatrixAndSourceRegister.md](../AIFoundationalSuite/03_DataClassificationMatrixAndSourceRegister.md); `D5` regulated/OT sources excluded from cloud prompts. | CISO & Data Stewards | `<Pending / Ready>` |
| **`RDY-04`** | **Champion Workspaces Seeded** | Priority departmental knowledge workspaces (`CAT-001`+) curated with final approved docs and benchmarked against 25-50 Q&A pairs (`>= 85%` groundedness). | AI CoE Enablement Lead & `L200` Champions | `<Pending / Ready>` |
| **`RDY-05`** | **Employee Traffic-Light AUP Ready** | [04_EmployeeAcceptableUseGuide.md](../AIFoundationalSuite/04_EmployeeAcceptableUseGuide.md) localized, linked in welcome communications, and embedded in Day-1 `L100` onboarding flow. | HR / Change Lead & InfoSec | `<Pending / Ready>` |
| **`RDY-06`** | **`<15-Minute` Kill Switch Tested** | Staging drills `KSD-001` to `KSD-004` from [06_AISecurityIncidentAndKillSwitchRunbook.md](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md) passed within target SLAs. | SOC Lead & Platform Ops | `<Pending / Ready>` |
| **`RDY-07`** | **Named Production & Ops Owners** | Named day-job production owner, on-call rotation, 3-Tier support path, and budget alert thresholds (`50%/80%/100%`) documented. | Program Lead & IT Ops Lead | `<Pending / Ready>` |

## 2. Milestone Gate Progression (`M0` to `M5`) & Blackout Calendar Check

```
+------------------------------------------------------------------------+
|            PROGRAM MILESTONE GATE PROGRESSION (M0 TO M5)               |
+------------------------------------------------------------------------+
|  [M0] Discovery    [M1] Day-0 Lock   [M2] Champion     [M3] P2P Gate   |
|  & Mobilization -> Platform/Policy -> Early Access  -> Production Go   |
|                                                              |         |
|  [M5] BAU CoE   <- [M4] Wave Rollout <-----------------------+         |
|  Warm Handoff      & 60-Day Seat Governance                            |
+------------------------------------------------------------------------+
```

| Milestone | Exit Criteria | Companion Artifact |
| :---: | :--- | :--- |
| **`M0`** | Kickoff completed; strategic drivers, RACI, and initial backlog confirmed. | [01_ExecutiveKickoffBriefingOutline.md](01_ExecutiveKickoffBriefingOutline.md) |
| **`M1`** | `RDY-01` through `RDY-07` verified; AI Policy and AUP ratified. | [02_EnterpriseAIPolicyAndDataClassification.md](../AIFoundationalSuite/02_EnterpriseAIPolicyAndDataClassification.md) |
| **`M2`** | `L200` Champions onboarded; workspaces curated; Golden Eval baselines recorded. | [05_KnowledgeNotebookAndPromptPlaybook.md](../AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md) |
| **`M3`** | 10-Dimension Pilot-to-Production Gate cleared with funded 12-month operating budget. | [11_PilotToProductionGatePackage.md](../AIFoundationalSuite/11_PilotToProductionGatePackage.md) |
| **`M4`** | Wave cohorts live; Day 30/45/60 seat reclamation active; Tier 2/3 agents gated via AIIA. | [09_ValueRealizationAndSeatGovernanceSOP.md](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md) |
| **`M5`** | Five-Part Warm Handoff Charter signed; BAU CoE cadence and registers live. | [04_CloseoutAndBAUWarmHandoffPackage.md](04_CloseoutAndBAUWarmHandoffPackage.md) |

**Cross-Region Change-Freeze & Public Holiday Blackout Check:** Before scheduling any `M1` cutover, `M2` Champion launch, or `M4` wave expansion, confirm every item below:

- [ ] No overlapping public or statutory holidays in any participating operating region during cutover week.
- [ ] No enterprise IT change-freeze windows or financial month/quarter-end close blackouts conflicting with connector launches.
- [ ] Named primary and backup platform engineers, SOC analysts, and `L200` Champions confirmed on duty for launch window.
- [ ] Rollback and Layer 1/2/3 kill-switch verification steps rehearsed ahead of the scheduled window.

## Operating Cadence Summary

| Cadence | Forum | Required Attendees | Output |
| :--- | :--- | :--- | :--- |
| **Weekly (Pre-Launch)** | Cutover & Readiness Standup | Program Lead, Platform, Security, Identity | Updated `RDY-01` to `RDY-07` tracker |
| **Bi-Weekly (`M2`-`M5`)** | Program Health Check | Program Lead, CoE Lead, Ops, Champions | Scored `HC-01` to `HC-08` log and actions |
| **Monthly** | Use Case Intake & AIIA Clinic | CoE Lead, Data Stewards, InfoSec, Legal | Updated `AIUseCaseBacklog` & AIIAs |
| **Quarterly** | Executive Steering & Maturity Review | Exec Sponsor, CIO, CISO, Finance, CoE | Updated Scorecard (`10`) & Seat Audit (`09`) |

## 3. Eight Bi-Weekly Program Health Check Signals (`HC-01` to `HC-08`)

Run this 30-minute inspection every two weeks from `M2` through `M5`. Any `Red` signal triggers immediate remediation before expanding seat waves.

| Signal ID | Health Signal | Green (Healthy) | Amber (Watch) | Red (Action Trigger) | Corrective Playbook Trigger |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **`HC-01`** | **Active Weekly Usage vs. Shelfware** | `>= 85%` seat activation; `>= 50%` WAU/MAU | `70%-84%` activation or `35%-49%` WAU/MAU | `< 70%` activation or `< 35%` WAU/MAU | Trigger Champion office hours and Day 30/45/60 seat reclamation ([09](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md)). |
| **`HC-02`** | **Citation Verification Habits** | `>= 80%` sampled Amber outputs show cited checks | `60%-79%` compliance in spot checks | `< 60%` or unverified external release | Reinforce Golden Rule #2 in `L100` refreshers and add UI disclosure banners. |
| **`HC-03`** | **Connector & ACL Sync Health** | `100%` connectors healthy; `< 1 hr` sync lag | `1-24 hr` sync lag on non-`D4` source | `> 24 hr` lag or any ACL mismatch | Run Layer 2 connector pause and purge per Runbook B ([06](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md)). |
| **`HC-04`** | **Shadow AI Channeling** | Unsanctioned web AI traffic declining toward zero | Isolated unapproved tool requests | Sensitive `D2`-`D5` upload detected | Enforce proxy blocks, run coaching outreach, fast-track safe equivalent via CoE. |
| **`HC-05`** | **Golden Eval Pass Rates** | `>= 85%` groundedness (`>= 90%` Tier 3) | `75%-84%` on staging dataset | `< 75%` or `> 0%` cross-entity leakage | Halt promotion; refresh source corpus and re-run eval pipeline ([13](../AIFoundationalSuite/13_OperationalGovernanceRegistersAndGenAIOps.md)). |
| **`HC-06`** | **Token / API Cost Burn vs. Budget** | Within `+/- 10%` of monthly forecast | `80%-99%` budget alert fired | `>= 100%` or single-agent spike `> 3x` | Enforce model tier routing, context caching, and `max_steps` caps ([09](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md)). |
| **`HC-07`** | **Security & Support Triage Velocity** | `>= 95%` tickets & incidents within SLA | `85%-94%` SLA compliance | `< 85%` or missed `SEV-1/2` target | Reallocate Tier-2 IT capacity; audit diagnostic bundle completeness. |
| **`HC-08`** | **CoE Enablement Queue Depth** | Intake backlog triaged `< 10` business days | `10-20` business days queue | `> 20` days (CoE becoming bottleneck) | Shift CoE from Gatekeeper to Enabler templates and reusable workspaces ([10](../AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md)). |

### Bi-Weekly Health Check Log & Escalation Rule

- **Green (0 Red, <= 2 Amber):** Proceed on planned wave schedule; monitor Amber items in regular working sync.
- **Amber Watch (3+ Amber or repeat Amber across 2 cycles):** Assign named owner and 10-business-day remediation target prior to next wave expansion.
- **Red Stop-Light (Any single Red signal):** Pause expansion of affected cohort or connector immediately; escalate within 24 hours to Executive Sponsor and CISO (for `HC-03`, `HC-04`, `HC-05`, or `HC-07`).

| Review Date | Current Milestone | Signals Green / Amber / Red | Top Blocker / Signal | Corrective Action & Named Owner | Next Check Date |
| :---: | :---: | :---: | :--- | :--- | :---: |
| `<YYYY-MM-DD>` | `<M2 / M3 / M4>` | `<e.g., 6G / 2A / 0R>` | `<Signal ID & summary>` | `<Action & owner>` | `<YYYY-MM-DD>` |

## 4. Program Delivery RACI Matrix

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

| Program Activity | Exec Sponsor | Program Lead | AI CoE Lead | Platform Lead | CISO / InfoSec | Data Steward | HR / Change | BU Champions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Executive kickoff & priority lock (`M0`) | **A** | R | R | C | C | I | C | I |
| Day-0 platform, SSO/SCIM & perimeter (`RDY-01/02`) | I | C | C | **A/R** | R | I | I | I |
| Source register & `D1`-`D5` approval (`RDY-03`) | I | I | C | C | **A** | R | I | C |
| Champion workspace seeding (`RDY-04`) | I | I | **A** | C | I | C | C | R |
| Workforce AUP & `L100` onboarding (`RDY-05`) | I | C | R | I | C | I | **A/R** | R |
| Kill-switch staging drills (`RDY-06`) | I | I | C | R | **A/R** | I | I | I |
| Pilot-to-Production Gate sign-off (`M3`) | **A** | R | R | R | R | C | C | C |
| Bi-weekly health check & remediation (`HC-01`..`08`) | I | **A/R** | R | R | C | C | C | C |
| Closeout & BAU warm handoff (`M5`) | **A** | R | **A/R** | R | C | C | I | C |
