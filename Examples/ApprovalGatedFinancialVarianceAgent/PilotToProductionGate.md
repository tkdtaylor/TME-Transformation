<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Pilot-to-Production Gate: Approval-Gated Financial Variance Agent

## Use Case

| Field | Response |
| :--- | :--- |
| Use case name | Approval-Gated Financial Variance Agent (`UC-004`) |
| Business owner | Corporate Financial Controller |
| Production owner | FP&A Operations Manager |
| Technical owner | Enterprise AI Engineering Lead |
| Risk tier | Tier 3: High |
| Pilot start / end dates | 2026-08-01 / 2026-09-30 |
| Proposed production date | 2026-11-01 |

## Pilot Outcome

| Question | Response / Evidence |
| :--- | :--- |
| Did the pilot meet its predefined success thresholds? | Yes: achieved `93%` groundedness and `100%` arithmetic accuracy across the 100-sample Financial Golden Dataset, cutting pilot variance pack preparation from 3.5 days to 1.6 days |
| What baseline was used for comparison? | Prior 3 monthly close cycles across two pilot subsidiaries (time-motion logs and reconciliation rework counts) |
| What quality, safety, and business metrics were measured? | Groundedness (`93%`), arithmetic accuracy (`100%`), cross-entity leakage (`0.0%`), close drafting cycle time (`-54%`), per-task token cost (`$0.14` median) |
| What unresolved issues remain? | None blocking launch; quarterly onboarding checklist added for newly acquired regional entities |
| What is the go / no-go recommendation? | Go for controlled Gateway 2 production launch for `SG-AI-Finance-Controllers` |

## Production Readiness

| Readiness Dimension | Required Evidence | Status | Evidence / Link |
| :--- | :--- | :--- | :--- |
| Production owner | Named owner with responsibility in objectives or operating model | Ready | FP&A Operations Manager assigned with 20% dedicated time allocation |
| Operational ownership | Runbook, on-call path, incident process | Ready | Agent Ops runbook and 24x7 SOC `SEV-1`/`SEV-2` bridge path live |
| Funded operating budget | 12-month budget or approved funding path | Ready | Approved FY2027 CFO Office AI platform budget line (`$18,000/yr` token cap) |
| Eval infrastructure | Golden eval set, automated eval pipeline, thresholds, dashboard | Ready | 100-sample Financial Golden Dataset wired to CI/CD eval pipeline (`>= 90%` gate) |
| Platform integration | Approved gateway, logging, rate limits, data boundary controls | Ready | Dedicated principal `sa-agent-finvar-prod`, OAuth 2.0 passthrough, inline guardrail hooks, CMEK |
| User support | Support channel, SLA, escalation path | Ready | Tier-1 Finance Champions -> Tier-2 Agent Ops (`<= 30 min` close-week SLA) |
| Change management | Rollout plan, training, communications, acceptable-use acknowledgement | Ready | `L200/L300` controller clinic completed; AUP acknowledgement logged for 100% of cohort |
| Decommission / provider-change plan | Alternative model, migration path, or sunset criteria | Ready | Model-abstraction gateway supports provider swap; manual BI fallback tested |
| Security review | OWASP LLM assessment, red-team results where required | Ready | OWASP `LLM01`-`LLM10` verified; 50-prompt cross-entity red-team passed; `KSD-003` kill switch `3m 10s` |
| Compliance evidence | Current AIIA and required approvals | Ready | Tier 3 AIIA signed off by Legal, InfoSec, Data Steward, and CFO (`2026-10-16`) |

## Decision

| Role | Name | Decision | Date | Conditions |
| :--- | :--- | :--- | :--- | :--- |
| Business owner | Corporate Financial Controller | Approve | 2026-10-20 | Mandatory human sign-off retained for all close packs |
| Production owner | FP&A Operations Manager | Approve | 2026-10-20 | Close-week on-call calendar published |
| AI governance owner | AI Program Lead | Approve | 2026-10-21 | Conditional pilot items from September review verified closed |
| Security reviewer | CISO Security Architect | Approve | 2026-10-21 | Quarterly `KSD-003` kill-switch drill cadence enforced |
| Legal / compliance reviewer | Senior Finance & Privacy Counsel | Approve | 2026-10-21 | Quarterly AIIA reassessment scheduled (`2027-01-15`) |

**Final gate decision:** Approve  
**Conditions to resolve before launch:** None remaining (pre-launch Golden Dataset expansion, inline guardrail hook verification, and `KSD-003` kill-switch drill completed prior to final sign-off).  
**Post-launch review date:** 2026-12-05
