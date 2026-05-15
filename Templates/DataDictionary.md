# Template Data Dictionary

This data dictionary explains the CSV operational registers in this folder. Use it as a guide when converting the CSV files into spreadsheets, databases, service catalogs, GRC records, or workflow tools.

## General Conventions

| Field Type | Convention |
|---|---|
| Dates | Use `YYYY-MM-DD` where possible |
| IDs | Keep stable once assigned; do not reuse retired IDs |
| Links | Use durable links to evidence, approvals, tickets, or records |
| Scores | Use `1-5` unless a template states otherwise |
| Empty values | Leave blank when unknown; use `Not applicable` only when explicitly reviewed |

## Shared Controlled Values

| Field | Recommended Values |
|---|---|
| Risk Tier | `Tier 1`, `Tier 2`, `Tier 3`, `Tier 4` |
| Use Case Category | `Augmentation`, `Analysis`, `Generation`, `Automation`, `Agency` |
| Lifecycle Phase | `Discover`, `Pilot`, `Deploy`, `Govern`, `Optimize`, `Scale` |
| Review Cadence | `Monthly`, `Quarterly`, `Annual`, `On material change` |
| Yes / No Fields | `Yes`, `No`, `Unknown`, `Not applicable` |

## AIDecisionRegister.csv

| Column | Description |
|---|---|
| Decision ID | Stable identifier for the decision register entry, e.g. `ADR-001` |
| Decision Being Influenced | The business, operational, customer, or employee decision shaped by AI |
| AI Tool or System | AI product, model, agent, workflow, or system involved |
| Use Case Name | Related use case or initiative name |
| Decision Owner | Person or role that owns the decision process |
| Human Accountable | Named human accountable for AI-influenced outcomes |
| Risk Tier | Risk tier assigned under the AIAF |
| Use Case Category | Primary AIAF use case category |
| Guardrails in Place | Key controls such as human review, data filtering, policy checks, or scoped permissions |
| Exception Handling | How edge cases, overrides, disputes, or failures are escalated |
| Sanctioned | Whether the AI use is approved by the organization |
| Status | `Proposed`, `Active`, `Under review`, `Retired` |
| Review Cadence | How often this decision entry is reviewed |
| Last Reviewed | Most recent review date |
| Next Review | Next scheduled review date |
| Evidence Link | Link to AIIA, approval, logs, policy, or other supporting evidence |
| Notes | Additional context |

## AIUseCaseBacklog.csv

| Column | Description |
|---|---|
| Use Case ID | Stable identifier for the candidate use case, e.g. `UC-001` |
| Use Case Name | Short, descriptive use case name |
| Business Unit | Owning business unit or function |
| Business Owner | Person accountable for business value and prioritization |
| Use Case Category | Primary AIAF use case category |
| Initial Risk Tier | Initial risk tier before full AIIA |
| Business Value Score | `1-5` score using the AIAF prioritization rubric |
| Data Readiness Score | `1-5` score using the AIAF prioritization rubric |
| Risk Inverted Score | `1-5` score where lower-risk use cases score higher |
| Technical Feasibility Score | `1-5` score using the AIAF prioritization rubric |
| Strategic Fit Score | `1-5` score using the AIAF prioritization rubric |
| Time to Value Score | `1-5` score using the AIAF prioritization rubric |
| Composite Score | Weighted total score, normally out of `5.0` |
| Recommendation | `Pursue`, `Defer`, `Reject`, `Needs discovery` |
| Status | `Proposed`, `In discovery`, `Pilot`, `Production`, `Retired` |
| Target Phase | Next intended AIAF lifecycle phase |
| Dependencies | Data, platform, legal, security, vendor, or people dependencies |
| Notes | Additional context |

## ApprovedAIToolRegistry.csv

| Column | Description |
|---|---|
| Tool ID | Stable identifier for the tool entry, e.g. `TOOL-001` |
| Tool Name | Product, service, model, or platform name |
| Vendor or Provider | Vendor, provider, or internal owner |
| Owner | Person or role accountable for the registry entry |
| Approved Status | `Approved`, `Conditional`, `Prohibited`, `Under review` |
| Approved Use Cases | Permitted uses or patterns |
| Prohibited Use Cases | Disallowed uses or conditions |
| Allowed Data Classes | Data classes approved for use, e.g. `D1-D2`, `D1-D3`, or `None` |
| Training on Customer Data | Whether the provider may train on submitted customer or company data |
| Logging Available | Whether enterprise audit or usage logging is available |
| Retention Terms | Prompt, completion, file, and log retention terms |
| SSO or Enterprise Controls | SSO, SCIM, RBAC, admin console, tenant controls, or equivalent |
| Contract or DPA Link | Link to contract, DPA, vendor risk record, or procurement file |
| Security Review Date | Date of last security or vendor risk review |
| Next Review | Next scheduled review date |
| Notes | Additional context |
