<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# AI Use Case Card: Approval-Gated Financial Variance Agent

## Summary

| Field | Response |
| :--- | :--- |
| Use case name | Approval-Gated Financial Variance Agent (`UC-004`) |
| Business unit | Corporate Finance / Financial Planning & Analysis (FP&A) |
| Business owner | Corporate Financial Controller |
| Technical owner | Enterprise AI Engineering Lead |
| Target users | Regional Financial Controllers and Senior FP&A Analysts (`SG-AI-Finance-Controllers`) |
| Current process / workflow | Month-end close analysts manually extract multi-entity trial balances from ERP and analytics warehouse exports, reconcile currency and intercompany variances in spreadsheets, and draft management variance narratives |
| Proposed AI capability | Tool-using scoped agent that queries read-only warehouse variance views via caller identity propagation, computes exact aggregations in sandboxed Python/SQL, and drafts cited commentary for controller review |
| Use case category | Agency / Analysis (Tool-Using Agent under Stage 2 Human Augmentation) |
| Initial risk tier | Tier 3: High |
| Candidate reference scenario | Agentic Workflow Automation paired with Document Analysis & Extraction (read-only, approval-gated) |

## Business Value

| Dimension | Response |
| :--- | :--- |
| Business outcome | Compress month-end variance reconciliation and executive commentary preparation while eliminating manual copy-paste arithmetic errors |
| Baseline metric | Monthly close variance pack requires 3.5 business days median across 6 regional entities, with 12% manual reconciliation rework rate |
| Target metric | Reduce variance pack drafting to 1.5 business days median and reduce arithmetic reconciliation rework under 2% within two close cycles |
| Expected time to value | 90-120 days (post-AIIA and P2P Gate clearance) |
| Estimated benefit | Faster executive close reporting, deterministic audit traceability to ledger rows, and reclaimed analyst capacity for forward-looking margin analysis |
| Strategic fit | Establishes the organization's reusable Gateway 2 blueprint for read-only, approval-gated Tier 3 tool-using agents over `D4` warehouse data |

## Feasibility

| Dimension | Response |
| :--- | :--- |
| Data readiness | High: chart of accounts and trial balance views are standardized in the enterprise analytics warehouse with entity-level RBAC |
| Integration complexity | Moderate-High: requires OAuth 2.0 identity propagation to warehouse row-level ACLs, sandboxed Python runtime, and inline guardrail API hooks |
| Existing tools / platforms | Enterprise ERP exports, Enterprise Data Warehouse, Corporate IdP, Enterprise AI Platform and Agent Runtime |
| Known dependencies | Standardized entity chart-of-accounts mapping, 100-sample Financial Golden Dataset, AIIA approval, and quarterly `KSD-003` kill-switch drill |
| Known blockers | Late intercompany adjustments during day-2 close require clear data-freshness timestamps in every cited output |

## Risk and Controls

| Dimension | Response |
| :--- | :--- |
| Sensitive or regulated data involved? | Yes (`D4 Restricted`): pre-release subsidiary financial results, segment margins, and intercompany schedules |
| Consequential decision involved? | Outputs inform executive financial management reviews and board reporting packages |
| Human review required? | Yes. Mandatory Corporate Financial Controller review and sign-off before commentary distribution |
| External-facing surface? | No (internal finance controllers and executives only) |
| Agentic tool use or write access? | Read-only SQL/warehouse tools and stateless sandboxed Python compute only; zero ERP or database write tools |
| AIIA required? | Yes (Tier 3 mandatory) |

## Prioritization Score

| Dimension | Weight | Score (1-5) | Weighted Score | Evidence |
| :--- | :---: | :---: | :---: | :--- |
| Business value | 25% | 5 | 1.25 | Compresses close cycle across 6 subsidiaries and removes recurring manual reconciliation toil |
| Data readiness | 20% | 4 | 0.80 | Standardized warehouse variance views exist with entity-level RBAC |
| Risk inverted | 20% | 2 | 0.40 | Tier 3 High Risk (`D4` pre-release financials); mitigated by read-only scope and strict controller HITL |
| Technical feasibility | 15% | 4 | 0.60 | Proven read-only SQL/MCP and sandboxed Python pattern, plus inline guardrail hooks |
| Strategic fit | 10% | 5 | 0.50 | Anchor Gateway 2 reference pattern for future `D4` tool-using agents |
| Time to value | 10% | 3 | 0.30 | 90-120 days including Golden Dataset curation, red-teaming, and P2P Gate |
| **Total** | **100%** | | **3.85 / 5.00** | |

## Decision

| Field | Response |
| :--- | :--- |
| Recommendation | Pursue |
| Next lifecycle phase | Pilot (progressing to Deploy via P2P Gate) |
| Decision owner | AI Governance Steering Committee |
| Decision date | 2026-09-15 |
| Notes | Proceed under Gateway 2 controls with read-only warehouse access, dedicated principal `sa-agent-finvar-prod`, mandatory controller sign-off, and 100-sample Golden Dataset validation prior to production close use. |
