<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 01 Executive Kickoff Briefing Outline

Use this 10-slide Assertion-Evidence blueprint to open an enterprise technology and AI rollout. Each slide pairs an action headline (what leadership must decide or verify) with concrete evidence anchored in the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) and [Technology Adoption Framework (TAF)](../TechAdoptionFramework.md).

## Deck Metadata

| Field | Guidance |
| :--- | :--- |
| **Target Milestone** | `M0` Discovery & Program Mobilization (Week 1) |
| **Presenter & Owner** | Executive Sponsor and Program Lead |
| **Required Attendees** | CIO/CTO, CISO, Chief Data Officer, Finance Partner, HR/Change Lead, Business Unit Sponsors, AI CoE Lead |
| **Session Goal** | Confirm scope, Day-0 boundaries, upfront Pilot-to-Production (`P2P`) expectations, and immediate 7-day actions |
| **Recommended Duration** | 60-90 minutes (15 min strategy/scope, 30 min readiness/data boundaries, 30 min RACI/milestones/actions) |

## 10-Slide Assertion-Evidence Structure

| Slide # | Action Headline (Assertion) | Key Evidence & Visual Content | Source Artifact(s) |
| :---: | :--- | :--- | :--- |
| **1** | **Our AI program targets measurable Thin-to-Valued work shifts aligned to board priorities** | Executive North Star vision statement, top 3 strategic drivers, and baseline target metrics (`VAL-01` to `VAL-04`). | [01_EnterpriseAIStrategyCharter.md](../AIFoundationalSuite/01_EnterpriseAIStrategyCharter.md), [07_StrategicDriversAndThinValuedWork.md](../AIFoundationalSuite/07_StrategicDriversAndThinValuedWork.md) |
| **2** | **Dual-track execution pairs technical platform delivery with workforce governance from Day 1** | Track A (Platform, identity federation, repository connectors, Champion workspaces) running in lockstep with Track B (AI policy, acceptable use training, risk triage). | [AIAdoptionFramework.md](../AIAdoptionFramework.md), [TechAdoptionFramework.md](../TechAdoptionFramework.md) |
| **3** | **Every pilot must clear the Pilot-to-Production Gate before broad deployment** | Six-phase AIAF lifecycle map showing the upfront `P2P` Gate: named day-job owner, 12-month operating budget, eval pipeline, and rollback plan settled early so pilots do not stall on volunteer goodwill. | [11_PilotToProductionGatePackage.md](../AIFoundationalSuite/11_PilotToProductionGatePackage.md), [PilotToProductionGate.md](../Templates/PilotToProductionGate.md) |
| **4** | **D1-D5 classification and zero-training rules protect sensitive data without halting adoption** | `D1`-`D5` matrix summary: inference-time grounding inherits source ACLs; `D4` stays in scoped enclaves; `D5` regulated/OT data stays outside cloud LLM prompts; external B2B guests blocked at IdP. | [02_EnterpriseAIPolicyAndDataClassification.md](../AIFoundationalSuite/02_EnterpriseAIPolicyAndDataClassification.md), [03_DataClassificationMatrixAndSourceRegister.md](../AIFoundationalSuite/03_DataClassificationMatrixAndSourceRegister.md) |
| **5** | **Three-tier enablement empowers Champions early while channeling Shadow AI safely** | Role-based cohort charter: `L100` Workforce Literacy (all licensed users), `L200` Departmental Curators (shared knowledge workspaces and no-code flows), and `L300` Agent Builders (code-first agents). | [04_EmployeeAcceptableUseGuide.md](../AIFoundationalSuite/04_EmployeeAcceptableUseGuide.md), [05_KnowledgeNotebookAndPromptPlaybook.md](../AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md) |
| **6** | **Initial rollout focuses on high-readiness Wave-1 workflows rather than premature autonomy** | Scored candidate backlog showing Wave-1 `Stage 1/2` quick wins (`Tier 1-2`) prioritized ahead of `Tier 3` tool-using agents and deferred `Tier 4` autonomous ideas. | [08_AIUseCaseIntakeAndPortfolioBacklog.md](../AIFoundationalSuite/08_AIUseCaseIntakeAndPortfolioBacklog.md), [AIUseCaseBacklog.csv](../Templates/AIUseCaseBacklog.csv) |
| **7** | **Clear RACI ownership prevents committee bottlenecks and establishes single-point accountability** | Program RACI across Sponsor, Program Lead, CoE Lead, Platform, CISO, Data Steward, HR, and BU Champions, plus escalation SLAs for unresolved blockers. | [02_Day0ReadinessAndBiWeeklyHealthCheck.md](02_Day0ReadinessAndBiWeeklyHealthCheck.md) |
| **8** | **Seven Day-0 readiness gates must pass before opening general access** | Live status snapshot of `RDY-01` through `RDY-07` (SSO/SCIM guest filter, regional boundary, source register, seeded workspaces, AUP sign-off, tested `<15-min` kill switch, named owners). | [02_Day0ReadinessAndBiWeeklyHealthCheck.md](02_Day0ReadinessAndBiWeeklyHealthCheck.md) |
| **9** | **30 / 60 / 90-day milestones respect regional change freezes and public holiday blackouts** | Phased timeline from `M0` through `M4` overlaid with financial close windows, change freezes, and public holidays across participating hubs so cutovers never launch unstaffed. | [02_Day0ReadinessAndBiWeeklyHealthCheck.md](02_Day0ReadinessAndBiWeeklyHealthCheck.md), [10_AIMaturityScorecardAndReadinessRoadmap.md](../AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md) |
| **10** | **Immediate 7-day actions and bi-weekly governance cadence lock accountability today** | Named owners and due dates for the next 7 days, confirmed bi-weekly health check slot, and standing CoE intake review schedule. | [02_Day0ReadinessAndBiWeeklyHealthCheck.md](02_Day0ReadinessAndBiWeeklyHealthCheck.md) |

## Slide-by-Slide Presenter Prompts & Decision Checklist

Use these prompts in the room to drive concrete decisions rather than passive updates:

- **Slide 1 (North Star & Outcomes):** Confirm the top 3 strategic drivers (`DRV-*`) and lock the single financial/productivity metric Finance will audit at Day 90 (`VAL-01` to `VAL-04`).
- **Slide 2 (Dual-Track Model):** Verify Track B (policy, acceptable use training, risk triage) has dedicated staff capacity matching Track A (platform engineering and connectors).
- **Slide 3 (Upfront P2P Gate):** Ask Business Unit Sponsors to identify who will hold day-job production ownership and 12-month operating budget responsibility if the initial pilot meets its targets.
- **Slide 4 (Data & Identity Lock):** Confirm with CISO and Data Stewards which sources clear Wave-1 grounding (`D1`-`D3`), which stay in scoped enclaves (`D4`), and which systems remain air-gapped (`D5`).
- **Slide 5 (Champion Cohort Charter):** Lock exact `L200` Champion names per participating department and ratify `L100` onboarding timelines for Wave-1 cohorts.
- **Slide 6 (Use Case Portfolio):** Confirm that every Wave-1 candidate has a written SOP and that Tier 4 autonomous proposals remain deferred until Stage 2 reliability is demonstrated.
- **Slide 7 (RACI & Escalation):** Ratify single-point accountable owners (`A`) and confirm the 24-hour escalation path for security or ACL blockers.
- **Slide 8 (Day-0 Dependencies):** Review every `Pending` item across `RDY-01` to `RDY-07` and assign an owner and target completion date prior to `M1` cutover.
- **Slide 9 (30/60/90 Milestones & Blackout Check):** Cross-check cutover dates against regional public holidays, quarter-end close freezes, and IT maintenance windows before confirming the calendar.
- **Slide 10 (Next 7 Days & Cadence):** Assign owners to `KO-01` through `KO-05` and confirm the recurring bi-weekly health check slot on calendars.

## Dual-Track Mobilization View

```
+------------------------------------------------------------------------+
|  TRACK A (PLATFORM & BUILD)        TRACK B (GOVERNANCE & PEOPLE)       |
|  * SSO/SCIM + Guest Filter         * Strategy Charter & AI Policy      |
|  * Network Perimeter & CMEK        * D1-D5 Source Control Register     |
|  * Champion Workspaces             * Traffic-Light AUP & L100/L200     |
|  * Staging Kill-Switch Drill       * P2P Gate & Decision Register      |
+------------------------------------------------------------------------+
```

## Facilitation & Preparation Notes

1. **Pre-read packet (48 hours prior)**: Send the completed [Business Readiness Assessment](../Workshops/BusinessReadinessAssessment.md) summary alongside [01_EnterpriseAIStrategyCharter.md](../AIFoundationalSuite/01_EnterpriseAIStrategyCharter.md) so executives spend meeting time confirming decisions rather than reading definitions.
2. **Pre-announce the Pilot-to-Production bar (Slide 3)**: Confirm upfront that no pilot advances past `M2` without an identified production owner and 12-month operating budget line.
3. **Avoid tool-first detours**: Redirect debates about specific vendor model versions back to business outcomes, data readiness, and model-abstraction design.
4. **Keep Slide 8 factual**: Mark any unfinished Day-0 dependency as `In Progress` or `Blocked` with a named owner and target date rather than rounding up to green.
5. **Verify Slide 9 calendars early**: Cross-check all participating regional teams for quarter-end freezes, national holidays, and peak operational periods before locking cutover dates.

## Kickoff Exit Checklist

- [ ] Executive Sponsor ratified strategic drivers and Thin-to-Valued work targets (Slide 1).
- [ ] CISO and DPO confirmed `D1`-`D5` boundaries and external B2B guest exclusion rules (Slide 4).
- [ ] Business Unit Heads named `L200` Champions for initial workspace curation (Slide 5).
- [ ] Initial Wave-1 backlog items confirmed with written SOP owners (Slide 6).
- [ ] Program RACI, escalation SLAs, and Day-0 readiness owners confirmed (Slides 7-8).
- [ ] Cutover milestones checked against regional holiday and change-freeze calendars (Slide 9).
- [ ] Next-7-days action list and bi-weekly health check cadence booked on calendars (Slide 10).

## Immediate Next-7-Days Action Tracker

| Action ID | Task Description | Owner | Target Date | Dependency / Output |
| :---: | :--- | :--- | :---: | :--- |
| `KO-01` | Finalize IdP security groups and SCIM guest exclusion filter | Identity & Platform Lead | `<YYYY-MM-DD>` | Clears `RDY-01` |
| `KO-02` | Ratify `D1`-`D5` source control register for Wave-1 connectors | CISO & Data Stewards | `<YYYY-MM-DD>` | Clears `RDY-03` |
| `KO-03` | Nominate `L200` Champions and lock initial workspace list | BU Heads & AI CoE Lead | `<YYYY-MM-DD>` | Starts `RDY-04` |
| `KO-04` | Schedule staging kill-switch drill (`KSD-001` to `KSD-004`) | SOC Lead & Platform Ops | `<YYYY-MM-DD>` | Clears `RDY-06` |
| `KO-05` | Book recurring bi-weekly health check and CoE intake clinics | Program Lead | `<YYYY-MM-DD>` | Establishes `M1`-`M4` rhythm |

## References & Companion Frameworks

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Core perspectives, lifecycle phases, Pilot-to-Production Gate, and RACI.
- [Technology Adoption Framework (TAF)](../TechAdoptionFramework.md): Platform foundation, governance layers, and migration wave sequencing.
- [Business Readiness Assessment](../Workshops/BusinessReadinessAssessment.md): Pre-kickoff capability, data, and maturity baseline workshop.
- [References](../References.md): Maintained catalog of regulatory, security, and standards guidance.
