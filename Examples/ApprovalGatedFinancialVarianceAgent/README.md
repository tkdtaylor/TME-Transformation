<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Approval-Gated Financial Variance Agent

This worked example shows how the [AI Adoption Framework (AIAF)](../../AIAdoptionFramework.md) applies to a **Tier 3: High Risk, Tool-Using Scoped Agent** operating over restricted enterprise financial data (`D4`). It complements the [Internal Employee Lifecycle Assistant](../InternalEmployeeLifecycleAssistant/README.md) example: whereas that Tier 2 pilot focuses on read-only document synthesis and Human Augmentation without external tool execution, this example demonstrates the full technical and governance controls required when an agent calls read-only data warehouse views and executes deterministic calculation tools.

## Why This Example

This workflow models a high-value Tier 3 pattern with strict non-human actor safeguards:

- Processes `D4 Restricted` multi-entity trial balances and variance exports across regional subsidiaries
- Combines read-only SQL/warehouse tool calls with sandboxed Python arithmetic to eliminate LLM math hallucinations on large tabular files (`> 500,000` words)
- Runs under a dedicated Non-Human Actor service principal (`sa-agent-finvar-prod`) with caller identity propagation
- Enforces inline pre-model and pre-tool guardrail API checks, hard recursion caps (`max_steps <= 8`), and per-task token cost ceilings
- Maintains strict approval gating: Financial Controllers review and sign off on every variance commentary package before management reporting; the agent holds zero ERP write access

## AIAF Classification

| Dimension | Classification |
| :--- | :--- |
| Primary category | Analysis / Agency (Tool-Using Scoped Agent) |
| Initial risk tier | Tier 3: High |
| Maturity stage | Stage 2: Human Augmentation (strict approval-gated HITL) |
| Non-human actor persona | Tool-Using Agent (`sa-agent-finvar-prod` + per-user OAuth 2.0 passthrough) |
| Deployment pattern | Controlled Gateway 2 production rollout following AIIA and P2P Gate clearance |
| Human accountability | Corporate Financial Controller (`Decision Owner`) signs off on all variance commentary |
| Not in scope | Autonomous ERP journal posting, intercompany adjustments, statutory filings, or unapproved external reporting |

## Included Example Artifacts

| Artifact | Purpose |
| :--- | :--- |
| [AIUseCaseCard.md](AIUseCaseCard.md) | Completed Tier 3 intake and 6-dimension prioritization card (`3.85 / 5.00`) |
| [AIImpactAssessment.md](AIImpactAssessment.md) | Completed Tier 3 AIIA with measurable RAI evidence and OWASP `LLM01`-`LLM10` controls |
| [PilotToProductionGate.md](PilotToProductionGate.md) | Completed P2P Gate showing all 10 production readiness dimensions cleared (`Approved`) |
| [AIDecisionRegister.example.csv](AIDecisionRegister.example.csv) | Example decision register entries (`ADR-010`, `ADR-011`) matching `Templates/AIDecisionRegister.csv` |
| [AIUseCaseBacklog.example.csv](AIUseCaseBacklog.example.csv) | Example scored backlog row (`UC-004`) matching `Templates/AIUseCaseBacklog.csv` |
| [ApprovedAIToolRegistry.example.csv](ApprovedAIToolRegistry.example.csv) | Example tool registry entries (`TOOL-010` approved, `TOOL-011` prohibited) matching `Templates/ApprovedAIToolRegistry.csv` |

## Guardrail Summary

1. **Zero ERP Write Access**: All database views and MCP connectors use strictly scoped read-only credentials.
2. **Deterministic Math Only**: Variance deltas, currency conversions, and aggregations execute in sandboxed Python/SQL rather than free-text LLM generation.
3. **Inline Guardrail Hooks**: Prompt-injection (`LLM01`) and sensitive-data (`LLM02`) checks run inside explicit `before_model` and `before_tool` hooks on every invocation.
4. **Hard Cost & Step Caps**: Tasks enforce `max_steps <= 8`, a 150k input / 8k output token ceiling, and a 30-second tool timeout.
5. **Verified Kill Switch**: Disabling `sa-agent-finvar-prod` halts all tool execution in under 5 minutes without interrupting ERP close workflows.

## How To Use This Example

Compare this Tier 3 package with [InternalEmployeeLifecycleAssistant](../InternalEmployeeLifecycleAssistant/README.md) (Tier 2) and use the blank forms in [Templates](../../Templates/README.md) alongside [03_AgentRequirementAndDesignSpec.md](../../ProgramDelivery/03_AgentRequirementAndDesignSpec.md) and [12_AIImpactAssessmentAndOWASPControls.md](../../AIFoundationalSuite/12_AIImpactAssessmentAndOWASPControls.md) to build your own Gateway 2 agent submissions.
