<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-06` (AI Security Incident Response & 90-Day Kill-Switch Drill Runbook) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | Chief Information Security Officer (CISO) / SOC Analysts, Cloud Platform Engineers, Identity Administrators, and AI Center of Excellence (CoE) Leads |
| **Primary Internal Owner** | Information Security (CISO / SOC Incident Response) & AI Center of Excellence (CoE), with Enterprise IT Operations |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's Security Operations Center (SOC), Enterprise IT Operations, and AI Center of Excellence (CoE) respond to AI-specific security incidents and verify emergency containment controls. It is **not** prescriptive. Sections include a **4-Level AI Incident Severity Matrix (`SEV-1` to `SEV-4`)**, a **5-Layer 15-Minute Containment & Kill-Switch Hierarchy**, step-by-step execution runbooks, and a **90-Day Kill-Switch Drill Log (`KSD-001` to `KSD-004`)** so teams do not have to start from a blank page.

## 1. How the AI CoE & SOC Can Create, Customize & Drill This Runbook

### 1.1 Purpose & Why This Document Exists

Traditional enterprise cybersecurity playbooks cover malware, phishing, and network intrusion, but they rarely address Generative AI failure modes such as **over-shared cloud documents surfacing in enterprise search**, **external B2B guest accounts syncing into AI license groups**, **indirect prompt injection hidden inside external vendor PDFs**, or **runaway autonomous agent tool loops**. Furthermore, an emergency kill switch required by [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`, Section 4) and [11 Pilot-to-Production (P2P) Gate Review Package](11_PilotToProductionGatePackage.md) (`AIAF-DOC-11`) that has never been tested under realistic conditions often fails during an actual incident.

This runbook gives the Security Operations Center (SOC) and Enterprise IT Operations teams a **4-Level AI Incident Severity Matrix (`SEV-1` to `SEV-4`)**, a **5-Layer 15-Minute Containment & Kill-Switch Hierarchy**, and a **90-Day Recurring Kill-Switch Drill Log (`KSD-001` to `KSD-004`)**.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Primary Custodians**: Information Security (SOC / Incident Response Lead), Cloud Platform Lead, and AI Center of Excellence (CoE) Lead.
- **Required Internal Contributors**:
  - **Identity Provider (IdP) & Directory Administrators**: Verify Layer 1 user/group revocation procedures (`SG-AI-Enterprise-Users`, `SG-AI-Enterprise-Champions`).
  - **Document Repository & Enterprise AI Connector Admins**: Verify Layer 2 connector pause and document purge procedures.
  - **Legal & Data Protection Officer (DPO)**: Confirm regulatory notification thresholds for `D4 Restricted` and `D5 Regulated / Critical` incidents under applicable privacy and sector cybersecurity mandates.

### 1.3 Recommended Internal CoE & SOC Production Process (Tabletop & Sandbox Drill)

To operationalize this runbook internally without external facilitation, the AI CoE and SOC Lead can run a Tabletop & Live Sandbox Drill prior to the Production Gate ([AIAF-DOC-11](11_PilotToProductionGatePackage.md)):

1. **Pre-Work (SOC & Cloud Platform Admins):** Verify that the on-call SOC runbook includes the exact Platform Admin Console links, Cloud IAM CLI commands, and corporate IdP group object IDs (`SG-AI-Enterprise-Champions`, `SG-AI-Enterprise-Users`).
2. **Tabletop Walkthrough:** Walk through `SEV-1` to `SEV-4` in **Section 2** and confirm who holds emergency revocation authority outside business hours without waiting for committee approval.
3. **Live Sandbox Kill-Switch Test:** Execute the 4 quarterly drill scenarios (`KSD-001` through `KSD-004`) in the non-production sandbox environment, record the measured time-to-contain in **Section 5**, and attach the log evidence to the Production Gate ([AIAF-DOC-11](11_PilotToProductionGatePackage.md)) package.

## 2. AI Incident Severity Matrix & Escalation SLAs (`SEV-1` to `SEV-4`)

All data tier references below align with the canonical 5-tier taxonomy in [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`) and [03 AI Data Classification Matrix & Enterprise Data Source Control Register](03_DataClassificationMatrixAndSourceRegister.md) (`AIAF-DOC-03`: `D1 Public`, `D2 Internal`, `D3 Confidential`, `D4 Restricted`, `D5 Regulated / Critical`):

| Severity Level | AI Incident Definition & Operational Triggers | Initial Triage SLA | Containment Target (Kill Switch) | Mandatory Notification & Escalation Path |
| :--- | :--- | :--- | :--- | :--- |
| **`SEV-1` (Critical / Emergency)** | - Confirmed cross-entity or unauthorized exposure of `D4 Restricted` data (for example, unredacted financial trial balances in `SRC-007`, confidential legal agreements in `SRC-009`, or customer pricing) or any `D5 Regulated / Critical` data (`SRC-012`) via AI search or Grounded Knowledge Notebooks. - Unauthorized autonomous agent execution modifying a production system of record without mandatory human approval (`Tier 3/4` write violation). - Confirmed external B2B guest account bypassing the SCIM directory filter and gaining access to internal Enterprise AI connectors. | **`<= 15 mins`** (24x7 SOC On-Call) | **`<= 15 mins`** from confirmation | - Immediate page to CISO, Data Protection Officer (DPO), Head of Enterprise IT, and AI CoE Lead. - Convene Emergency Incident Bridge. - Assess statutory breach notification clock under applicable data privacy and sector regulations. |
| **`SEV-2` (High)** | - Successful indirect prompt injection (`LLM01`) observed in production (for example, adversarial instructions embedded in an external vendor RFP PDF in `SRC-006` attempting to exfiltrate session context), even if blocked by secondary controls. - Runaway Code-First Custom Agent loop (`UC-004` or `UC-006`) or API token spike exceeding **300%** of daily budget threshold. - Unapproved `D3 Confidential` or `D4 Restricted` document folder indexed into a broad shared datastore without Data Steward sign-off. | **`<= 30 mins`** | **`<= 60 mins`** | - Notify AI CoE Security Lead, Cloud Platform Lead, and affected Business Unit Data Steward. - Suspend affected connector or agent service principal within 60 minutes. |
| **`SEV-3` (Medium)** | - Repeated Runtime AI Guardrail Service filter triggers from an internal user attempting to bypass policy guardrails. - Hallucinated or outdated citation in a Curated Departmental Knowledge Workspace (`CAT-001` to `CAT-008` in `AIAF-DOC-05`) affecting operational SOP guidance. - Connector sync error or stale ACL cache exceeding 24 hours. | **`<= 4 hours`** (Business Hours) | **`<= 24 hours`** | - Log ticket in Tier-2 Enterprise IT / CoE Triage Queue. - Notify Departmental Knowledge Curator or Connector Admin to remediate source document or ACL sync. |
| **`SEV-4` (Low / Informational)** | - User feedback reporting unhelpful response, formatting defect, or false-positive Runtime AI Guardrail Service prompt block on benign domain terminology. | **`<= 2 business days`** | **Next Sprint / Release** | - Route through Tier-1 CoE Champion triage. - Tune Runtime AI Guardrail allowlist or prompt template in bi-weekly GenAIOps review. |

## 3. Five-Layer 15-Minute Containment & Kill-Switch Architecture

When an AI incident occurs, SOC Analysts and Cloud Platform Engineers do not need to shut down the entire **Enterprise AI Platform** environment if the issue is isolated to a single user account, a single source document, or a single custom agent. Containment is structured across **five precision kill-switch layers**:

```
+-----------------------------------------------------------------------+
|    ENTERPRISE 5-LAYER AI CONTAINMENT & KILL-SWITCH HIERARCHY          |
+-----------------------------------------------------------------------+
|                                                                       |
|  LAYER 1: USER / IDENTITY KILL SWITCH (Target SLA: <= 5 Mins)         |
|  Action : Remove user from IdP group SG-AI-Enterprise-Wave*           |
|           AND reset platform identity session cookies + IdP           |
|           refresh tokens immediately.                                 |
|  Scope  : Isolates a single compromised account or B2B guest leak.    |
|                                                                       |
|  LAYER 2: DOCUMENT / CONNECTOR KILL SWITCH (Target SLA: <= 10 Mins)   |
|  Action : Remove file ACL in source repository, delete source from    |
|           shared Knowledge Workspace (CAT-*), or pause connector.     |
|  Scope  : Stops overshared D4/D5 file from surfacing in answers.      |
|                                                                       |
|  LAYER 3: AGENT SERVICE PRINCIPAL KILL SWITCH (Target SLA: <= 5 Mins) |
|  Action : Disable non-human actor principal (sa-agent-*)              |
|           in Cloud IAM or unpublish No-Code Agent Builder workflow.   |
|  Scope  : Immediately halts runaway custom agent or MCP tool call.    |
|                                                                       |
|  LAYER 4: SAFETY FILTER & PROMPT BLOCKADE (Target SLA: <= 15 Mins)    |
|  Action : Update Runtime AI Guardrail policy to block specific        |
|           adversarial regex, URL domain, or prompt signature fleetwide|
|  Scope  : Neutralizes active prompt injection campaign fleet-wide.    |
|                                                                       |
|  LAYER 5: TENANT / PRIVATE PERIMETER LOCKDOWN (Target SLA: <= 15 Mins)|
|  Action : Disable Enterprise AI Assistant Web App endpoint OR enforce |
|           Private Network Perimeter (VPC / Private Link) lockdown.    |
|  Scope  : Full emergency stop for global SEV-1 security incident.     |
+-----------------------------------------------------------------------+
```

## 4. Step-by-Step Emergency Execution Runbooks (SOC & Platform Ops)

### 4.1 Runbook A: Layer 1 - Emergency User or External Guest Revocation (`<= 5 Minutes`)

**Trigger:** A corporate user account is compromised, an employee leaves a sensitive role, or an external B2B partner guest account is accidentally added to an AI access group.

1. **Identity Provider (IdP) Security Group Removal & Session Revocation:**
   - In the corporate **Identity Provider Admin Center -> Groups**, remove the user from `SG-AI-Enterprise-Users` (or `SG-AI-Enterprise-Champions`, `SG-AI-Finance-Controllers`), and revoke active sessions / refresh tokens on the user profile.
   - Verify the SCIM scoping filter on the Enterprise Directory Connector enforces `userType EQUALS "Member" AND accountEnabled EQUALS "True"` so external guest accounts are blocked at the directory boundary.
2. **Immediate Platform Identity Session Termination (Do Not Wait for SCIM Sync Cycle):**
   - In the **Enterprise Identity Admin Console -> Directory -> Users**, select the user and reset active sign-in cookies / sessions (or click **Suspend user**). This terminates active Enterprise AI Platform web and mobile sessions immediately.
3. **Verification:**
   - Confirm in Immutable Audit Logs (`service="enterprise-ai-gateway"`) that subsequent requests from the principal return `401/403 PERMISSION_DENIED`.

### 4.2 Runbook B: Layer 2 - Emergency Document Purge or Connector Suspension (`<= 10 Minutes`)

**Trigger:** A `D4 Restricted` or `D5 Regulated / Critical` file (such as an unredacted legal agreement, M&A packet, or executive board paper) was accidentally placed in a broad `D2/D3` document folder or shared Knowledge Workspace (`CAT-*`).

1. **Immediate Source Lockdown (Document Repository / Grounded Knowledge Notebook):**
   - Restrict permissions or quarantine the file in the **source document repository** immediately (for Federated Search connectors, revoking source read access blocks retrieval on the very next query because federated search evaluates live per-user OAuth tokens).
   - If the file was uploaded into a **Curated Departmental Knowledge Workspace (`CAT-001` to `CAT-008`)**, open the workspace as Curator and delete the source file immediately.
2. **Immediate Ingested Data Store Purge (If Indexed in Cloud Object Storage / Managed Search Index):**
   - In **Platform Admin Console -> Enterprise AI -> Data Stores**, select the target ingested data store and execute **Purge Documents** for the document URI, or toggle the connector status to **`PAUSED / DISABLED`**.
3. **Verification:**
   - Run the exact test query that surfaced the sensitive snippet using a non-privileged test account; verify zero citations or snippets from the purged document are returned.

### 4.3 Runbook C: Layer 3 - Runaway Agent or Non-Human Actor (`NHA-02` to `NHA-05`) Kill Switch (`<= 5 Minutes`)

**Trigger:** A Code-First Custom Agent (`UC-004` Finance Agent or `UC-006` Analytics Agent) or No-Code Agent Builder workflow (`UC-005` Helpdesk Agent) enters an infinite loop, exceeds its token budget, or returns ungrounded outputs.

1. **Disable Dedicated Agent Service Principal (`Code-First Agent on Enterprise Agent Runtime`):**
   - Because every Code-First Custom Agent runs under a dedicated, least-privilege Cloud Service Principal (per [AIAF-DOC-02](02_EnterpriseAIPolicyAndDataClassification.md), Section 4), disabling that single principal halts the agent immediately without affecting any other agent or human user:

```sh
# Disable dedicated agent service principal in cloud IAM / IdP
iam-cli service-principal disable sa-agent-<agent-id>-prod
```

2. **Unpublish No-Code Agent Builder Workflow (`Gateway 2`):**
   - For a shared Agent Builder workflow, open **Enterprise AI Platform -> Agent Builder**, select the agent, and toggle sharing from **Shared Group** back to **Private / Disabled**.
3. **Verification:**
   - Confirm in Platform Observability & Telemetry that outbound MCP/SQL tool invocations and LLM token consumption for the disabled agent drop to `0` within 60 seconds.

## 5. Mandatory 90-Day Kill-Switch Drill Schedule & Log Template

To satisfy the Pilot-to-Production Gate ([AIAF-DOC-11](11_PilotToProductionGatePackage.md)) and AI Impact Assessment ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)), the AI CoE and SOC run a quarterly live verification drill in the staging environment and record the measured time-to-contain below:

| Drill ID | Scenario Tested | Target SLA | Measured Time (Template) | Last Drill Date | Verified By (Role) | Pass / Fail & Remediation Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`KSD-001`** | **Layer 1 Identity Kill Switch:** Attempt simulated external guest sync + reset active platform identity session cookies for a test user in `SG-AI-Enterprise-Users`. | `<= 5 mins` | `<Measured Time>` | `<Drill Date>` | SOC Lead & Identity Admin | `<PASS / FAIL>` - Verify SCIM filter blocks guest account and cookie reset terminates active session in `<5` mins. |
| **`KSD-002`** | **Layer 2 Overshared Document Purge:** Place simulated `D4 Restricted` watermarked file in staging folder & Knowledge Workspace; revoke ACL and purge source. | `<= 10 mins` | `<Measured Time>` | `<Drill Date>` | Cloud Platform Admin & Workspace Curator | `<PASS / FAIL>` - Verify document is removed and unreachable via grounded prompt within `<10` mins. |
| **`KSD-003`** | **Layer 3 Runaway Custom Agent Shutdown:** Trigger simulated loop on staging custom agent (`UC-004`); fire budget alert and disable agent service principal. | `<= 5 mins` | `<Measured Time>` | `<Drill Date>` | AI CoE Engineer | `<PASS / FAIL>` - Verify event-driven budget webhook triggers and service principal disables via IAM CLI in `<5` mins. |
| **`KSD-004`** | **Layer 4 Indirect Prompt Injection Block:** Upload vendor PDF containing hidden adversarial instruction (`LLM01`); verify Runtime AI Guardrail block and SIEM alert routing. | `<= 15 mins` | `<Measured Time>` | `<Drill Date>` | InfoSec Analyst | `<PASS / FAIL>` - Verify Runtime AI Guardrail blocks payload pre-inference and Immutable Audit Log routes to SIEM. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): AI Security & Trust Perspective (incident response, agentic action boundaries, kill-switch verification freshness) and Non-Human Actors.
- [References](../References.md): Maintained catalog of regulatory and security standards.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Manage Function (incident response, containment, and recovery).
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/): Controls for `LLM01` (Prompt Injection), `LLM06` (Excessive Agency), and `LLM10` (Unbounded Consumption).
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final): Dynamic identity revocation, least-privilege session enforcement, and micro-segmentation.
