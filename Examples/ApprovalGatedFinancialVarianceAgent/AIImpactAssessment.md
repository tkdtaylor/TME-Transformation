<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# AI Impact Assessment: Approval-Gated Financial Variance Agent

## 1. Use Case Summary

| Field | Response |
| :--- | :--- |
| Use case name | Approval-Gated Financial Variance Agent (`UC-004`) |
| Business owner | Corporate Financial Controller |
| Technical owner | Enterprise AI Engineering Lead |
| AI / model provider(s) | Approved Enterprise AI Platform and Agent Runtime (Frontier Reasoning tier for synthesis; Fast/Lightweight tier for routing) |
| Intended users | Regional Financial Controllers and Senior FP&A Analysts (`SG-AI-Finance-Controllers`) |
| People affected by outputs | Executive leadership, finance controllers, and business unit budget owners |
| Risk tier | Tier 3: High |
| Use case category | Agency / Analysis (Tool-Using Scoped Agent, Stage 2 Human Augmentation) |
| Current lifecycle phase | Deploy (cleared Phase 2 Pilot and P2P Gate) |

## 2. Purpose and Decision Role

| Question | Response |
| :--- | :--- |
| What problem is being solved? | Manual multi-entity trial balance reconciliation, FX/volume variance calculation across `> 500,000`-word exports, and initial narrative drafting slow down monthly financial close |
| Why is AI appropriate for this use case? | Deterministic Python and read-only SQL handle exact arithmetic over large tables while the LLM synthesizes multi-source accounting context with inline ledger citations |
| What actions or decisions does the output influence? | Monthly executive management commentary, subsidiary budget variance reviews, and close exception follow-up |
| Is the AI advisory, approval-gated, or autonomous? | Approval-gated (`Stage 2 Strict HITL`): generates cited variance tables and draft commentary only; zero write access to ERP or general ledger |
| Named human accountable for consequential outputs | Corporate Financial Controller (`ADR-010`) and Regional Finance Controllers (`ADR-011`) |

## 3. Data and Knowledge Inputs

| Data / Knowledge Source | Classification | Grounding or Training? | Owner | Access Controls | Retention / Deletion Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Multi-entity trial balance & variance warehouse views | `D4 Restricted` | Inference-time read-only SQL query only (zero training) | Corporate Finance Data Steward | Per-user OAuth 2.0 token passthrough enforcing subsidiary row-level ACLs; private network perimeter; CMEK | Zero model training retention; immutable audit logs retained per 7-year financial audit policy |
| Corporate accounting policy & chart-of-accounts manual | `D3 Confidential` | Inference-time grounding (curated index `CAT-004`) | Accounting Policy Lead | Restricted to `SG-AI-Finance-Controllers` | Re-indexed quarterly upon accounting standard updates |
| User variance prompt & session context | `D4 Restricted` | Runtime context only | Corporate Financial Controller | Encrypted in transit and at rest; external B2B guests excluded via SCIM filter | Session cache purged after close window or 30 days |

## 4. Risk Identification

| Risk Type | What Could Go Wrong? | Impact | Likelihood | Existing Controls | Residual Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Accuracy / hallucination | Model invents a variance explanation or misstates an FX delta | High | Medium | All math executed via sandboxed Python/SQL; inline row citations required; `>= 90%` groundedness on 100-sample Golden Set; low-confidence abstention rule | Low |
| Bias / fairness | Commentary applies inconsistent thresholds or tone across regional entities | Medium | Low | Standardized `R-C-T-V` prompt template and multi-entity slice checks during evals | Low |
| Privacy / data protection | Cross-entity `D4` margin data leaks to an analyst from another subsidiary | High | Low | Per-user OAuth 2.0 passthrough enforces warehouse row ACLs; 50-prompt cross-entity negative access test (`0.0%` leakage) | Low |
| Security / prompt attack | Malicious text inside an expense memo or vendor invoice note triggers indirect prompt injection (`LLM01`) | High | Medium | Inline guardrail API invoked in `before_model` and `before_tool` hooks; system prompt isolated from retrieved text | Low |
| Legal / regulatory | Pre-release earnings or statutory figures exposed outside authorized finance insiders | High | Low | `SG-AI-Finance-Controllers` IdP lock; SCIM external guest filter (`userType EQUALS 'Member'`); zero-training DPA | Low |
| Operational / availability | Close-week traffic spike or provider outage stalls month-end variance drafting | Medium | Medium | Automated fallback to standard BI warehouse extracts and manual close spreadsheet templates | Low |
| Reputational | Unverified draft variance figure circulates to executive committee without controller review | High | Low | Mandatory UI watermark *"AI Draft - Controller Sign-Off Required"* and named `Decision Owner` sign-off gate | Low |

## 5. Responsible AI Evidence

| Principle | Applicable? | Evidence Artifact / Link | Gaps or Exceptions |
| :--- | :---: | :--- | :--- |
| Fairness | Yes | Multi-entity eval slice report across all 6 subsidiaries | None; re-verify when adding acquired entities |
| Reliability | Yes | 100-sample Financial Golden Dataset report (`93%` groundedness, `100%` arithmetic accuracy) | None |
| Privacy | Yes | Zero cross-entity leakage penetration test log (`0 / 50` unauthorized retrievals) and CMEK verification | None |
| Transparency | Yes | UI review confirming clickable ledger citations, data-freshness timestamp, and draft banner | None |
| Accountability | Yes | `AIDecisionRegister` (`ADR-010`, `ADR-011`), immutable audit logs, and tested `< 5 min` kill switch (`KSD-003`) | None |
| Inclusiveness | Yes | Plain-language summary formatting check across regional finance teams | None |

## 6. Security Review

| OWASP LLM Risk | Applicable? | Mitigation / Evidence |
| :--- | :---: | :--- |
| LLM01 Prompt Injection | Yes | Inline prompt guardrail API executed in `before_model` and `before_tool` hooks; adversarial red-team test suite passed |
| LLM02 Sensitive Information Disclosure | Yes | Private network perimeter, CMEK, zero-training contract, and per-user warehouse row-level ACL passthrough |
| LLM03 Supply Chain | Yes | Approved enterprise model endpoints and signed internal container images built via CI/CD |
| LLM04 Data and Model Poisoning | Yes | Only Finance Data Stewards update `CAT-004` accounting policies; no fine-tuning performed |
| LLM05 Improper Output Handling | Yes | Parameterized read-only SQL views and strict JSON tool schemas; zero dynamic shell or write SQL execution |
| LLM06 Excessive Agency | Yes | Dedicated principal `sa-agent-finvar-prod` holds read-only grants; zero ERP write/posting APIs connected |
| LLM07 System Prompt Leakage | Yes | Zero credentials in prompts; authorization enforced strictly at warehouse/API layer |
| LLM08 Vector and Embedding Weaknesses | Yes | Tenant- and group-isolated index (`CAT-004`) with document-level ACL metadata filtering |
| LLM09 Misinformation | Yes | Deterministic Python/SQL math + mandatory row citations + abstention on missing ledger evidence |
| LLM10 Unbounded Consumption | Yes | Hard `max_steps <= 8` loop cap, 150k/8k token budget per task, 30s tool timeout, and FinOps alerts (`50%/80%/100%`) |

## 7. Controls and Monitoring

| Control Area | Required Control | Owner | Evidence / Link |
| :--- | :--- | :--- | :--- |
| Human review / override | Mandatory Financial Controller review and sign-off before commentary release | Corporate Financial Controller | Close Sign-Off SOP & `ADR-010` |
| Kill switch / rollback | Disable `sa-agent-finvar-prod` in IAM (`<= 5 min` SLA) and revert to BI extracts | SOC Lead & AI Engineering Lead | Kill-Switch Drill Log (`KSD-003`) |
| Logging / audit trail | Immutable logging of caller ID, agent principal, SQL view queries, guardrail verdicts, and outputs | Cloud Platform & Security Ops | Audit Log Pipeline & SIEM Rule |
| Quality evals | Pre-release and monthly regression run against 100-sample Financial Golden Dataset | AI Quality / Eval Engineer | Automated Eval Dashboard |
| Cost controls | Per-agent FinOps tags, `max_steps <= 8`, fast-tier routing, and budget webhook alerts | AI Operations & Finance Partner | FinOps Budget Alert Policy |
| Incident response | `SEV-1` (`<= 15 min`) and `SEV-2` (`<= 60 min`) AI incident escalation runbook | CISO / SOC Incident Lead | AI Incident Runbook (`AIAF-DOC-06`) |
| User disclosure / transparency | Persistent draft banner, source row citations, and close-cutoff timestamp | Corporate Financial Controller | UAT UI Sign-Off Record |

## 8. Approval and Review

| Role | Name | Decision | Date | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Business owner | Corporate Financial Controller | Approved | 2026-10-15 | Approved for monthly close variance drafting with mandatory human sign-off |
| AI governance owner | AI Program Lead | Approved | 2026-10-15 | Registered as `ADR-010` and `ADR-011` in Decision Register |
| Data steward | Corporate Finance Data Steward | Approved | 2026-10-14 | Verified read-only views, entity RBAC, and CMEK retention |
| Security reviewer | CISO Security Architect | Approved | 2026-10-15 | Verified `before_model`/`before_tool` guardrail hooks, `LLM01`-`LLM10`, and `KSD-003` (`3m 10s`) |
| Legal / compliance reviewer | Senior Finance & Privacy Counsel | Approved | 2026-10-15 | Verified zero-training DPA and pre-release financial handling controls |
| Executive approver | Chief Financial Officer (CFO) | Approved | 2026-10-16 | Required Tier 3 executive authorization recorded |

**Next scheduled review:** 2027-01-15  
**Triggered review conditions:** Addition of write-capable tools, new subsidiary ERP onboarding, model tier upgrade, groundedness drop below `90%`, or any `SEV-1`/`SEV-2` incident.
