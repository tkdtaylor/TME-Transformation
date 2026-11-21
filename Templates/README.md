# Templates

These templates are vendor-neutral source artifacts for applying the AI Adoption Framework. They are not meant to dictate your working tools.

Use them as canonical starting points, then convert them into the format your organization actually uses: documents, spreadsheets, forms, tickets, GRC records, service catalog entries, or workflow approvals.

## Format Guidance

| Format | Use For | Why |
|---|---|---|
| Markdown | Judgment artifacts | Good for narrative, rationale, approvals, and evidence links |
| CSV | Operational registers | Easy to sort, filter, import, and convert into spreadsheets or databases |

## Included Templates

### AI Adoption Framework (AIAF) Templates

| Template | Purpose |
|---|---|
| [AIImpactAssessment.md](AIImpactAssessment.md) | AI Impact Assessment for Tier 2+ use cases |
| [AIUseCaseCard.md](AIUseCaseCard.md) | Use case intake, value framing, and prioritization |
| [PilotToProductionGate.md](PilotToProductionGate.md) | Production readiness review before rollout |
| [AIDecisionRegister.csv](AIDecisionRegister.csv) | Register of AI-influenced decisions, owners, guardrails, and reviews |
| [AIUseCaseBacklog.csv](AIUseCaseBacklog.csv) | Scored backlog of candidate AI use cases |
| [ApprovedAIToolRegistry.csv](ApprovedAIToolRegistry.csv) | Approved, conditional, and prohibited AI tools |

### Technology Adoption Framework (TAF) Templates

| Template | Purpose |
|---|---|
| [WorkloadPortfolio7Rs.csv](WorkloadPortfolio7Rs.csv) | Workload inventory, criticality tiers, 7 Rs migration strategies, and wave assignments |
| [ArchitectureDecisionRecord.md](ArchitectureDecisionRecord.md) | Platform, landing zone, and workload architecture decision records |
| [MigrationWaveReadinessGate.md](MigrationWaveReadinessGate.md) | Pre-cutover readiness gate for Phase 3 workload migration waves |

### Shared Schema & Definitions

| Template | Purpose |
|---|---|
| [DataDictionary.md](DataDictionary.md) | Column definitions, recommended values, and conversion guidance for CSV registers |

## Pre-Populated Baselines & Worked Examples

- **[AI Foundational Suite](../AIFoundationalSuite/README.md)** (`00` through `14`): Use these pre-populated, industry-agnostic program policies, classification matrices, incident runbooks, and CoE playbooks when establishing organization-wide governance rather than starting from blank templates.
- **[Internal Employee Lifecycle Assistant Example](../Examples/InternalEmployeeLifecycleAssistant/README.md)**: Reference a completed Tier 2 Human Augmentation worked example (`AIUseCaseCard`, `AIImpactAssessment`, `PilotToProductionGate`, and CSV registers).
- **[Approval-Gated Financial Variance Agent Example](../Examples/ApprovalGatedFinancialVarianceAgent/README.md)**: Reference a completed Tier 3 tool-using scoped agent worked example with deterministic Python/SQL tools, inline guardrails, and tested kill-switch evidence.

## Conversion Rule

When converting these templates into another tool, preserve the core fields for ownership, risk tier, evidence, review cadence, and decision history. The working format can change; the accountability structure should not.
