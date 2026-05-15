# AI Use Case Card: Internal Employee Lifecycle Assistant

## Summary

| Field | Response |
|---|---|
| Use case name | Internal Employee Lifecycle Assistant |
| Business unit | HR Operations, IT Operations, Security Operations |
| Business owner | Head of HR Operations |
| Technical owner | IT Automation Lead |
| Target users | HR coordinators, IT service desk, managers, security operations, facilities, finance operations |
| Current process / workflow | Onboarding, role-change, and offboarding tasks are coordinated through a mix of HRIS events, tickets, spreadsheets, email, manager checklists, and application-owner follow-up |
| Proposed AI capability | Generate lifecycle checklists, summarize relevant policies, suggest routing, draft access request language, flag missing steps, and prepare handoff notes for human review |
| Use case category | Augmentation / Analysis, with narrow Task Automation |
| Initial risk tier | Tier 2: Medium |
| Candidate reference scenario | Internal knowledge assistant plus document analysis and workflow triage |

## Business Value

| Dimension | Response |
|---|---|
| Business outcome | Reduce missed onboarding/offboarding tasks and shorten time to employee readiness or access removal completion |
| Baseline metric | New hire readiness takes 5 business days median; offboarding access-removal evidence is incomplete in 18% of sampled exits |
| Target metric | Reduce new hire readiness to 3 business days median; reduce incomplete offboarding evidence to under 5% within 6 months |
| Expected time to value | 60-90 days for pilot users |
| Estimated benefit | Less manual coordination, fewer access gaps, improved employee and manager experience, better audit evidence |
| Strategic fit | Builds a reusable internal workflow pattern for policy-grounded lifecycle support without starting with agentic autonomy |

## Feasibility

| Dimension | Response |
|---|---|
| Data readiness | Medium: HR, IT, security, facilities, and finance procedures exist but need ownership and source-of-truth confirmation |
| Integration complexity | Medium: pilot can begin without write access by reading approved policy/procedure documents and drafting checklist/ticket text |
| Existing tools / platforms | HRIS, ITSM, identity provider, document repository, collaboration tools |
| Known dependencies | Data classification, document owners, access templates by role, ITSM ticket schema, HR/legal review of employee-data handling |
| Known blockers | Inconsistent application-owner lists; offboarding steps vary by region, employment type, and role sensitivity |

## Risk and Controls

| Dimension | Response |
|---|---|
| Sensitive or regulated data involved? | Yes. Employee lifecycle metadata, role, department, location, manager, access needs, and potentially employment status |
| Consequential decision involved? | Outputs may influence HR, access, payroll, benefits, and security workflows, but humans retain decision authority |
| Human review required? | Yes. Required before access changes, employment actions, payroll / benefits changes, legal / compliance steps, or external communications |
| External-facing surface? | No |
| Agentic tool use or write access? | No for pilot. Future write actions require reassessment and higher scrutiny |
| AIIA required? | Yes |

## Prioritization Score

| Dimension | Weight | Score (1-5) | Weighted Score | Evidence |
|---|---:|---:|---:|---|
| Business value | 25% | 4 | 1.00 | Offboarding gaps create security and audit exposure; onboarding delays affect productivity |
| Data readiness | 20% | 3 | 0.60 | Documents exist, but ownership and freshness need cleanup |
| Risk inverted | 20% | 3 | 0.60 | Tier 2 internal use with sensitive employee data and required human review |
| Technical feasibility | 15% | 4 | 0.60 | Pilot can operate with read-only document access and draft outputs |
| Strategic fit | 10% | 4 | 0.40 | Establishes reusable policy-grounded workflow pattern |
| Time to value | 10% | 4 | 0.40 | Limited pilot can be run inside 90 days |
| **Total** | **100%** | | **3.60 / 5.00** | |

## Decision

| Field | Response |
|---|---|
| Recommendation | Pursue |
| Next lifecycle phase | Pilot |
| Decision owner | AI Governance Working Group |
| Decision date | 2026-05-15 |
| Notes | Proceed with read-only, human-reviewed pilot scoped to two departments and one country. Offboarding flows require security review before production rollout. |
