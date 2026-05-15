# Pilot-to-Production Gate: Internal Employee Lifecycle Assistant

## Use Case

| Field | Response |
|---|---|
| Use case name | Internal Employee Lifecycle Assistant |
| Business owner | Head of HR Operations |
| Production owner | HR Operations Manager |
| Technical owner | IT Automation Lead |
| Risk tier | Tier 2 |
| Pilot start / end dates | 2026-06-01 / 2026-07-31 |
| Proposed production date | 2026-09-01 |

## Pilot Outcome

| Question | Response / Evidence |
|---|---|
| Did the pilot meet its predefined success thresholds? | Target state for worked example: yes, if checklist accuracy exceeds 90%, source citation precision exceeds 95%, and users rate outputs useful in at least 75% of sessions |
| What baseline was used for comparison? | Manual onboarding/offboarding checklist cycle time and sampled evidence completeness from prior quarter |
| What quality, safety, and business metrics were measured? | Checklist accuracy, retrieval citation quality, missed-task rate, time to draft checklist, user satisfaction, data policy violations |
| What unresolved issues remain? | Regional offboarding variations and contractor lifecycle cases require expanded source coverage |
| What is the go / no-go recommendation? | Conditional go for production if eval, retention, and offboarding evidence conditions are closed |

## Production Readiness

| Readiness Dimension | Required Evidence | Status | Evidence / Link |
|---|---|---|---|
| Production owner | Named owner with responsibility in objectives or operating model | Ready | HR Operations Manager named |
| Operational ownership | Runbook, on-call path, incident process | In progress | AI support runbook draft |
| Funded operating budget | 12-month budget or approved funding path | Ready | HR / IT shared operating budget |
| Eval infrastructure | Golden eval set, automated eval pipeline, thresholds, dashboard | In progress | Eval set complete for core employee scenarios; contractor cases pending |
| Platform integration | Approved gateway, logging, rate limits, data boundary controls | Ready | Enterprise AI gateway configuration |
| User support | Support channel, SLA, escalation path | Ready | HRIS / ITSM support queue |
| Change management | Rollout plan, training, communications, acceptable-use acknowledgement | In progress | Manager training draft |
| Decommission / provider-change plan | Alternative model, migration path, or sunset criteria | In progress | Provider-change plan draft |
| Security review | OWASP LLM assessment, red-team results where required | In progress | Prompt injection and retrieval leakage tests pending |
| Compliance evidence | Current AIIA and required approvals | In progress | Conditional approvals captured in AIIA |

## Decision

| Role | Name | Decision | Date | Conditions |
|---|---|---|---|---|
| Business owner | Head of HR Operations | Conditional | 2026-08-15 | Close regional offboarding gaps |
| Production owner | HR Operations Manager | Conditional | 2026-08-15 | Confirm support model |
| AI governance owner | AI Program Lead | Conditional | 2026-08-15 | Eval and retention evidence required |
| Security reviewer | Security Operations Lead | Conditional | 2026-08-15 | Complete red-team and retrieval leakage tests |
| Legal / compliance reviewer | Employment Counsel | Conditional | 2026-08-15 | Add final escalation language |

**Final gate decision:** Conditional  
**Conditions to resolve before launch:** Complete eval set, prompt retention policy, red-team testing, regional offboarding variations, and final support runbook.  
**Post-launch review date:** 2026-10-15
