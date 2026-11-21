<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Program Delivery & Rollout Execution Kit

This folder turns discovery outputs from the [Business Readiness Assessment](../Workshops/BusinessReadinessAssessment.md) and policy baselines from the [AI Foundational Suite](../AIFoundationalSuite/README.md) into day-to-day execution artifacts. It guides program leads, platform engineers, security reviewers, and AI Center of Excellence (CoE) leads from executive kickoff through Day-0 readiness gates, bi-weekly health checks, custom agent design reviews, and steady-state business-as-usual (BAU) handover.

Each document is vendor-neutral and adapts cleanly to both the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) and the [Technology Adoption Framework (TAF)](../TechAdoptionFramework.md).

## Execution Artifacts (`01` to `04`)

| Doc # | Document | Target Timing | Primary Owner | Companion Framework & Suite Artifacts |
| :---: | :--- | :--- | :--- | :--- |
| **`01`** | [01 Executive Kickoff Briefing Outline](01_ExecutiveKickoffBriefingOutline.md) | Program Mobilization (`M0`) | Executive Sponsor & Program Lead | [Strategy Charter](../AIFoundationalSuite/01_EnterpriseAIStrategyCharter.md), [P2P Gate](../AIFoundationalSuite/11_PilotToProductionGatePackage.md), [AIAF](../AIAdoptionFramework.md), [TAF](../TechAdoptionFramework.md) |
| **`02`** | [02 Day-0 Readiness & Bi-Weekly Health Check](02_Day0ReadinessAndBiWeeklyHealthCheck.md) | Pre-Launch (`M1`) through Rollout (`M4`) | Program Lead, Platform Lead & CISO | [AI Policy](../AIFoundationalSuite/02_EnterpriseAIPolicyAndDataClassification.md), [Kill-Switch Runbook](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md), [Seat SOP](../AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md) |
| **`03`** | [03 Agent Requirement & Design Specification](03_AgentRequirementAndDesignSpec.md) | Tier 2-4 Agent Design (`Phase 2`) | Product Owner & Technical Lead | [Use Case Card](../Templates/AIUseCaseCard.md), [AI Impact Assessment](../Templates/AIImpactAssessment.md), [AIIA & OWASP](../AIFoundationalSuite/12_AIImpactAssessmentAndOWASPControls.md) |
| **`04`** | [04 Closeout & BAU Warm Handoff Package](04_CloseoutAndBAUWarmHandoffPackage.md) | Rollout Exit (`M5` BAU Handoff) | Program Lead & Steady-State CoE Lead | [Operational Registers](../AIFoundationalSuite/13_OperationalGovernanceRegistersAndGenAIOps.md), [Maturity Scorecard](../AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md) |

## End-to-End Delivery Flow

```
  [Business Readiness Workshop] + [AI Foundational Suite Policies]
                                |
                                v
  (01) Executive Kickoff ---> (02) Day-0 Gates & M0-M5 Health Checks
                                |
                                +---> (03) Tier 2-4 Agent PRD & Controls
                                |
                                v
                   (04) Closeout & BAU Warm Handoff
```

## Lifecycle Alignment (`AIAF` and `TAF`)

- **Phase 1 to Phase 2 (`M0`-`M2`)**: Use `01` to establish executive sponsorship and `02` (`RDY-01` to `RDY-07`) to clear Day-0 identity, data, and security controls before Champion early access opens.
- **Phase 2 to Phase 3 (`M3`)**: Use `03` to design and test Tier 2-4 agents against Golden Datasets before clearing the [Pilot-to-Production Gate](../Templates/PilotToProductionGate.md) or [Migration Wave Readiness Gate](../Templates/MigrationWaveReadinessGate.md).
- **Phase 3 to Phase 5 (`M4`-`M5`)**: Track `HC-01` to `HC-08` bi-weekly during rollout waves, then execute `04` to transfer durable ownership, FinOps budgets, and recurring registers to the steady-state CoE.

## How to Use These Templates

1. **Adapt to your cadence**: Use `01` to align leadership on Day-1 scope, data boundaries, and upfront Pilot-to-Production criteria before provisioning pilot cohorts.
2. **Gate launch with evidence**: Track `RDY-01` through `RDY-07` in `02` before opening production seats, then inspect `HC-01` through `HC-08` every two weeks during rollout waves.
3. **Specify custom agents before coding**: Require a completed `03` Agent PRD alongside [AIImpactAssessment.md](../Templates/AIImpactAssessment.md) before approving Tier 2-4 tool-using agents.
4. **Prevent post-launch drift**: Complete the Five-Part Warm Handoff Charter in `04` before disbanding the rollout team so day-job owners inherit clear budgets, SLAs, and recurring review cadences.

## Primary Program Roles

| Role | Primary Kit Responsibilities |
| :--- | :--- |
| **Executive Sponsor** | Chairs kickoff (`01`), removes cross-unit blockers, signs BAU handoff (`04`) |
| **Program Lead** | Drives `RDY-01` to `RDY-07` readiness, bi-weekly `HC-01` to `HC-08` checks (`02`), and closeout (`04`) |
| **AI CoE Lead** | Coordinates Champions, intake clinics, and steady-state governance cadence (`02`, `04`) |
| **Platform & Security Leads** | Enforces identity/network perimeters, inline guardrails, and kill-switch drills (`02`, `03`) |
| **Business Unit Champions** | Curates departmental workspaces and validates Tier 2-4 workflow SOPs (`01`, `03`) |

## Related Standards

Consult [References](../References.md) for underlying standards (`NIST AI RMF 1.0`, `ISO/IEC 42001`, `OWASP Top 10 for LLM Applications`, `NIST SP 800-207`, and `FinOps for AI`).
