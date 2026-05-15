# Internal Employee Lifecycle Assistant

This worked example shows how the AI Adoption Framework can be applied to a common internal business workflow without starting with a customer-facing or autonomous agent.

The use case supports employee onboarding, role changes, and offboarding. It helps HR, IT, security, managers, facilities, finance, and application owners coordinate lifecycle tasks, find relevant policies, draft checklists, and route exceptions. It does not make employment decisions, approve access, remove access, send termination communications, or perform legal / HR determinations autonomously.

## Why This Example

This is a good first AIAF example because it is:

- Common to most organizations
- Internal-only
- Operationally meaningful
- Rich enough to involve data, security, HR, IT, governance, and workflow ownership
- Risk-bearing without being customer-facing or fully autonomous
- A strong fit for Human Augmentation with narrow Task Automation

## AIAF Classification

| Dimension | Classification |
|---|---|
| Primary category | Augmentation / Analysis |
| Secondary category | Task Automation for checklist generation and routing suggestions |
| Initial risk tier | Tier 2: Medium |
| Maturity stage | Human Augmentation, with narrow Task Automation |
| Deployment pattern | Internal pilot before broader rollout |
| Human accountability | HR, IT, security, manager, and process owners remain accountable |
| Not in scope | Hiring, firing, promotion, compensation, discipline, legal advice, autonomous access changes |

## Included Example Artifacts

| Artifact | Purpose |
|---|---|
| [AIUseCaseCard.md](AIUseCaseCard.md) | Worked use case intake and prioritization card |
| [AIImpactAssessment.md](AIImpactAssessment.md) | Worked Tier 2 AI Impact Assessment |
| [PilotToProductionGate.md](PilotToProductionGate.md) | Worked pilot-to-production readiness review |
| [AIDecisionRegister.example.csv](AIDecisionRegister.example.csv) | Example decision register entries |
| [AIUseCaseBacklog.example.csv](AIUseCaseBacklog.example.csv) | Example backlog row with scoring |

## Guardrail Summary

- The assistant may draft checklists, summaries, routing recommendations, and policy-based guidance.
- Humans approve all access changes, employment actions, payroll / benefits changes, legal / compliance actions, and external communications.
- The assistant should cite policy and procedure sources for material guidance.
- The pilot should start with a limited group and a bounded corpus of approved HR, IT, security, and facilities procedures.
- Offboarding flows require extra care because missed access removal, equipment return, and knowledge transfer steps can create security and operational risk.

## How To Use This Example

Use this as a model for how to complete the source templates in the [Templates](../../Templates) folder. Adapt the details to your organization's policies, systems, approval paths, data classification model, and legal requirements.
