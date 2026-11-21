<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 03 Agent Requirement & Design Specification (`Agent PRD`)

Complete this 3-part specification before building any Tier 2-4 custom or tool-using agent. Pair this design record with [AIUseCaseCard.md](../Templates/AIUseCaseCard.md) during intake and [AIImpactAssessment.md](../Templates/AIImpactAssessment.md) prior to Pilot-to-Production promotion.

## Document Header

| Field | Entry |
| :--- | :--- |
| **Agent ID & Name** | `<UC-XXX> - <Agent Name>` |
| **Product / Business Owner (`Decision Owner`)** | `<Named Business Owner & Role>` |
| **Technical Owner** | `<Named Engineering / Platform Lead>` |
| **Assigned Risk Tier & Category** | `<Tier 2 / Tier 3 / Tier 4>` / `<Automation / Analysis / Agency>` |
| **Linked SOP & Intake Card** | `<Link to Written Business SOP>` / `<Link to AIUseCaseCard>` |
| **Target Deployment Gateway** | `<Gateway 1 (Personal/Scoped) / Gateway 2 (Enterprise Shared)>` |

---

## Part 1: Workflow SOP & Task Decomposition

### 1.1 Prerequisite Process Verification

An AI agent must automate or augment a documented workflow rather than invent ad-hoc steps. Confirm:

- [ ] Current workflow SOP is documented end-to-end with inputs, decision criteria, exception paths, and system-of-record handoffs.
- [ ] Target progression stage is explicitly chosen: **Stage 1: Task Automation**, **Stage 2: Human Augmentation (HITL)**, or **Stage 3: Agentic Autonomy** (only after documented Stage 2 reliability).
- [ ] Baseline manual cycle time, error rate, and weekly volume are measured ahead of pilot launch.

### 1.2 Step-by-Step Thin Work vs. Valued Work Decomposition

| Step # | Current Workflow Step | Work Class (`Thin / Valued`) | Agent Responsibility | Named Human Responsibility |
| :---: | :--- | :---: | :--- | :--- |
| `01` | `<e.g., Extract and normalize source tables>` | Thin | Executes deterministic read/parse tool | Reviews schema mismatch exceptions |
| `02` | `<e.g., Compute variances and retrieve policy>` | Thin | Runs deterministic script + cited RAG lookup | Spot-checks edge-case flags |
| `03` | `<e.g., Draft narrative commentary>` | Thin -> Valued | Prepares cited draft with confidence notes | Verifies numbers, applies business judgment |
| `04` | `<e.g., Approve and publish / post record>` | Valued | **Prohibited** (read-only / draft-only) | Signs off and triggers system-of-record action |

---

## Part 2: Non-Human Actor Architecture, Tool Boundaries & Guardrails

### 2.1 Non-Human Actor & Identity Model

Align with [02_EnterpriseAIPolicyAndDataClassification.md](../AIFoundationalSuite/02_EnterpriseAIPolicyAndDataClassification.md) (Section 4) and [AIAdoptionFramework.md](../AIAdoptionFramework.md):

| Architectural Element | Specification |
| :--- | :--- |
| **Non-Human Actor Persona** | `<Scoped Agent / Service Agent / Tool-Using Agent / Multi-Agent System>` |
| **Dedicated Service Principal** | `<sa-agent-<id>-<env>>` (never shares credentials with other agents or human admins) |
| **Caller Identity Propagation** | `<Per-user OAuth 2.0 / OIDC token passthrough enforcing row/doc ACLs>` |
| **Allowed Data Tiers (`D1`-`D5`)** | `<e.g., D2 Internal to D4 Restricted; D5 strictly prohibited>` |
| **Network & Encryption Controls** | `<Private network perimeter, TLS in transit, CMEK at rest, immutable audit logs>` |

### 2.2 Explicit Per-Tool Allowlist

| Tool / API Connector | Access Mode | Permitted Scope & Parameter Constraints | Approval Gate (`Auto / HITL / Prohibited`) |
| :--- | :--- | :--- | :---: |
| `<e.g., Enterprise Warehouse View>` | Read-Only SQL | Parameterized queries against approved read-only views; row-level ACL enforced | `Auto (Read-Only)` |
| `<e.g., Sandboxed Python Runtime>` | Stateless Compute | No external network egress; arithmetic and table formatting only | `Auto (Sandboxed)` |
| `<e.g., Policy Knowledge Workspace>` | Read-Only RAG | Scoped to `<CAT-XXX>` index; returns clickable source citations | `Auto (Read-Only)` |
| `<e.g., ERP / ITSM / Email Write API>` | State-Changing Write | **Disabled in v1** (or explicit human confirmation token required per call) | **`Prohibited / Strict HITL`** |

### 2.3 Runtime Guardrails & Cost Ceilings

1. **Inline Pre-Model & Pre-Tool Guardrail Hooks**: Invoke the organization's prompt and output guardrail API explicitly inside the runtime's `before_model` and `before_tool` (or equivalent pre-inference and pre-tool) hooks to screen for prompt injection (`LLM01`) and sensitive data leakage (`LLM02`), independent of UI-level SaaS toggles.
2. **Typed Output & Parameterized Execution (`LLM05`)**: Enforce strict JSON schemas on tool calls and outputs; never pass raw generated strings directly into shell commands or unparameterized database queries.
3. **Hard Recursion, Timeout & Token Cost Ceilings (`LLM10`)**:
   - `max_steps`: `<e.g., <= 10 tool/reasoning steps per task>`
   - `per_task_token_budget`: `<e.g., max 150,000 input / 8,000 output tokens>`
   - `request_timeout`: `<e.g., 30 seconds per tool call; 120 seconds end-to-end>`
   - `model_routing`: `<Fast/lightweight tier for routing/extraction; frontier tier for synthesis>`

---

## Part 3: Golden Dataset Evaluation, Abstention & Rollback

### 3.1 Pre-Launch Acceptance Thresholds

| Evaluation Metric | Target Threshold | Test Dataset & Execution Method |
| :--- | :--- | :--- |
| **Groundedness / Citation Accuracy** | `>= 90%` (Tier 3) / `>= 85%` (Tier 2) | `<100-sample Golden Dataset via Automated Eval Pipeline>` |
| **Answer Relevance & Completeness** | `>= 90%` | Automated LLM-as-judge + SME review panel |
| **Tool Selection & Deterministic Math Accuracy** | `100%` arithmetic; `>= 95%` tool call | Deterministic unit tests + Golden Dataset replay |
| **Cross-Entity / Unauthorized ACL Leakage** | **`0.0%`** (Zero tolerance) | Negative-access penetration test across >= 50 cross-scope prompts |

### 3.2 Failure Mode & Circuit-Breaker Matrix

| Failure Mode | Detection Trigger | Automated System Behavior | Fallback / Human Escalation |
| :--- | :--- | :--- | :--- |
| **Low Retrieval Confidence / Conflict** | Confidence score below threshold or missing source rows | Abstain with *"Insufficient verified data in authorized sources"* | Route prompt + trace ID to `<Process Owner Queue>` |
| **Guardrail Block (`LLM01` / `LLM02`)** | Inline `before_model` or `before_tool` verdict `BLOCK` | Halt request before model/tool execution; emit SIEM log | Notify SOC on repeated blocks; return safe error text |
| **Step Loop or Token Cap Breach (`LLM10`)** | `steps > max_steps` or `tokens > budget` | Terminate loop via circuit breaker; log partial trace | Alert AI Engineering on-call; user retries narrower scope |
| **Upstream Tool / Warehouse Outage** | Tool timeout (`> 30s`) or HTTP `5xx` error | Fail fast without blind retries; surface outage banner | Fall back to manual SOP / standard BI report template |

### 3.3 Emergency Kill Switch & Design Sign-Off

- **Emergency Kill Switch (`<= 5 Minutes`)**: Document the exact IAM command or gateway toggle to disable `<sa-agent-<id>-<env>>` and verify graceful fallback to the manual SOP (`KSD-003` drill in [06_AISecurityIncidentAndKillSwitchRunbook.md](../AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md)).

| Review Role | Reviewer Name | Decision (`Approved / Conditional / Hold`) | Date | Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Business / Decision Owner** | `<Name & Role>` | `<Pending / Approved>` | `<YYYY-MM-DD>` | Confirms SOP & HITL step |
| **Technical Lead** | `<Name & Role>` | `<Pending / Approved>` | `<YYYY-MM-DD>` | Confirms tool schemas & cost caps |
| **Data Steward** | `<Name & Role>` | `<Pending / Approved>` | `<YYYY-MM-DD>` | Confirms `D1`-`D4` ACLs |
| **Security Reviewer** | `<Name & Role>` | `<Pending / Approved>` | `<YYYY-MM-DD>` | Confirms inline hooks & kill switch |
