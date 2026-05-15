# AI Impact Assessment: Internal Employee Lifecycle Assistant

## 1. Use Case Summary

| Field | Response |
|---|---|
| Use case name | Internal Employee Lifecycle Assistant |
| Business owner | Head of HR Operations |
| Technical owner | IT Automation Lead |
| AI / model provider(s) | Approved enterprise LLM via AI gateway |
| Intended users | HR coordinators, IT service desk, managers, security operations, facilities, finance operations |
| People affected by outputs | Employees, contractors, managers, application owners |
| Risk tier | Tier 2 |
| Use case category | Augmentation / Analysis, with narrow Task Automation |
| Current lifecycle phase | Pilot |

## 2. Purpose and Decision Role

| Question | Response |
|---|---|
| What problem is being solved? | Employee onboarding, role changes, and offboarding are fragmented across teams, creating delays, missed tasks, and incomplete audit evidence |
| Why is AI appropriate for this use case? | The work requires synthesizing policies, role templates, tickets, checklists, and procedural exceptions across multiple internal sources |
| What actions or decisions does the output influence? | Task checklists, routing recommendations, draft ticket text, exception identification, and handoff notes |
| Is the AI advisory, approval-gated, automated, or autonomous? | Advisory and approval-gated; narrow task automation only for checklist generation and routing suggestions |
| Named human accountable for consequential outputs | HR process owner for employee lifecycle process; IT access owner for access-related outputs; security owner for offboarding evidence |

## 3. Data and Knowledge Inputs

| Data / Knowledge Source | Classification | Grounding or Training? | Owner | Access Controls | Retention / Deletion Notes |
|---|---|---|---|---|---|
| HR onboarding procedure | D2 / D3 | Grounding | HR Operations | HR and manager access | Re-index when policy changes |
| IT access request procedure | D2 / D3 | Grounding | IT Operations | ITSM and manager access | Re-index when access templates change |
| Offboarding checklist | D3 | Grounding | Security Operations | HR, IT, security, manager access | Re-index on policy update; retain evidence per audit schedule |
| Role-to-access matrix | D3 | Grounding | Identity and Access Management | IAM team and authorized managers | Review quarterly |
| Employee lifecycle event metadata | D5 where personal data applies | Prompt / runtime context | HR Operations | User-scoped; minimum necessary fields only | Retain prompts and outputs per approved retention schedule |

## 4. Risk Identification

| Risk Type | What Could Go Wrong? | Impact | Likelihood | Existing Controls | Residual Risk |
|---|---|---|---|---|---|
| Accuracy / hallucination | Assistant invents a policy step or omits a required offboarding action | High | Medium | Source citation required; human review; eval set includes edge cases | Medium |
| Bias / fairness | Different employee groups receive inconsistent lifecycle handling | Medium | Low | Templates reviewed by HR; outputs sampled by role, location, and employment type | Low |
| Privacy / data protection | Employee personal data is included unnecessarily in prompts or outputs | High | Medium | Data minimization, AI gateway logging, PII detection, access scoping | Medium |
| Security / prompt attack | User prompts assistant to reveal restricted offboarding or access procedures beyond their role | High | Medium | Retrieval-time access control; prompt injection tests; no broad document access | Medium |
| Legal / regulatory | Assistant gives employment, benefits, or legal guidance that is treated as authoritative | High | Low | Disclaimer and escalation rules; HR/legal approval required for sensitive steps | Low |
| Operational / availability | Teams rely on assistant during onboarding/offboarding windows and it is unavailable | Medium | Medium | Manual checklist fallback; ITSM process remains source of record | Low |
| Reputational | Mishandled offboarding creates employee relations or audit concern | Medium | Low | Human approval, audit evidence, exception routing | Low |

## 5. Responsible AI Evidence

| Principle | Applicable? | Evidence Artifact / Link | Gaps or Exceptions |
|---|---|---|---|
| Fairness | Yes | HR review of role/location checklist coverage | Need pilot sample across two employee types |
| Reliability | Yes | Golden eval set for onboarding, role change, and offboarding scenarios | Eval set must include regional and contractor cases before scale |
| Privacy | Yes | Data classification review and minimization rules | Confirm retention schedule for prompts with employee metadata |
| Transparency | Yes | Assistant UI label and source citation standard | Add escalation language for HR/legal ambiguity |
| Accountability | Yes | Decision register entries and human owner mapping | Complete owner mapping for application owners |
| Inclusiveness | Yes | Accessibility review of assistant surface | Confirm multilingual requirements before expansion |

## 6. Security Review

| OWASP LLM Risk | Applicable? | Mitigation / Evidence |
|---|---|---|
| LLM01 Prompt Injection | Yes | Red-team prompts against policy override and instruction leakage |
| LLM02 Sensitive Information Disclosure | Yes | Retrieval access scoping; PII detection; no cross-employee data retrieval |
| LLM03 Supply Chain | Yes | Approved enterprise model and gateway only |
| LLM04 Data and Model Poisoning | No | No fine-tuning or training planned for pilot |
| LLM05 Improper Output Handling | Yes | Outputs are drafts; not executed automatically by downstream systems |
| LLM06 Excessive Agency | Yes | No write actions, no access changes, no autonomous ticket closure |
| LLM07 System Prompt Leakage | Yes | Prompt contains no secrets or privileged system details |
| LLM08 Vector and Embedding Weaknesses | Yes | Corpus permission testing and source-level access controls |
| LLM09 Misinformation | Yes | Citations, evals, human review, and escalation language |
| LLM10 Unbounded Consumption | Yes | Per-user and per-use-case token budget through gateway |

## 7. Controls and Monitoring

| Control Area | Required Control | Owner | Evidence / Link |
|---|---|---|---|
| Human review / override | Human approval required before access, HR, payroll, benefits, legal, or external communication actions | HR Operations / IT Operations | Pilot SOP |
| Kill switch / rollback | Disable assistant surface and fall back to manual checklist | IT Operations | Runbook |
| Logging / audit trail | Log prompts, retrieved source IDs, outputs, and user identity for pilot | AI Platform Engineer | Gateway logs |
| Quality evals | Golden set covers onboarding, role change, offboarding, exceptions, and restricted data prompts | AI Quality / Eval Engineer | Eval report |
| Cost controls | Per-user and pilot-level budget alerts | AI Operations Lead | Cost dashboard |
| Incident response | AI incident category added to HR/IT/security incident process | AI Program Lead | Incident playbook |
| User disclosure / transparency | Users see assistant limitations and source citation expectations | Product owner | Pilot UI copy |

## 8. Approval and Review

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Business owner | Head of HR Operations | Approved | 2026-05-15 | Pilot only; two departments |
| AI governance owner | AI Program Lead | Conditional | 2026-05-15 | Complete eval set before production gate |
| Data steward | HR Data Steward | Conditional | 2026-05-15 | Confirm prompt retention and employee-data minimization |
| Security reviewer | Security Operations Lead | Conditional | 2026-05-15 | Offboarding access evidence must be tested |
| Legal / compliance reviewer | Employment Counsel | Conditional | 2026-05-15 | No employment determinations; escalation language required |
| Executive approver | Not required for Tier 2 pilot | Not required | 2026-05-15 | Escalate if scope changes to automated access action |

**Next scheduled review:** 2026-08-15  
**Triggered review conditions:** Scope change, model change, incident, regulation change, material data source change, addition of write actions or access changes.
