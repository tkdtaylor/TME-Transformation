<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 03 AI Data Classification Matrix & Enterprise Data Source Control Register

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-03` (AI Data Classification Matrix & Enterprise Data Source Control Register) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | Chief Information Security Officer (CISO) / InfoSec, Enterprise Data Architects, Data Stewards, AI Center of Excellence (CoE), and Enterprise IT |
| **Primary Internal Owner** | Information Security (CISO Office), Enterprise Data Governance Lead & AI Center of Excellence (CoE) Lead |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE), Information Security, and Data Governance teams operationalize data classification rules (`D1` to `D5`) across AI tools and enterprise data repositories. It is **not** prescriptive. Sections include a **10-Surface `D1-D5 x AI Tool` Permission Matrix** and a **12-Repository Enterprise Data Source Control Register (`SRC-001` to `SRC-012`)** covering universal corporate platforms (Intranet/Docs, Engineering Manuals, Commercial Folders, Email/Calendar, ITSM, Procurement, ERP Financials, Data Lakehouse, Legal Vaults, Customer Support, Compliance Manuals, and Critical Operational Systems) so teams do not have to start from a blank page.

## 1. How the AI CoE & InfoSec Can Create, Customize & Evolve This Document

### 1.1 Purpose & Why This Document Exists

A mature AI data governance program evolves through two stages:

- **Stage 1 (Day-1 Clarity - High-Level Data Classification & Tool Permission Matrix)**: Every employee, champion, and administrator needs a single, unambiguous table that defines the organization's data sensitivity tiers (`D1` through `D5`) and shows exactly which AI tools each tier can and cannot be used with.
- **Stage 2 (Longer-Term Operational Control - Enterprise Data Source & Technical Control Register)**: As AI adoption scales across business units and regions, high-level policy rules must be mapped down to **specific enterprise repositories and data sources** (such as *Cloud Document Repositories*, *ERP Ledgers*, *Cloud Data Lakehouses*, *ITSM Systems*, *Legal Vaults*, and *Critical Operational Control Systems*), recording the highest data classification each source holds, whether it is permitted for inference-time grounding or code execution, who the named Data Steward is, and what technical controls enforce that boundary at runtime.

While [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`) establishes the overarching policy rules and [13 Operational Governance Registers (Decision, Tool & Data Dictionary) & GenAIOps Guide](13_OperationalGovernanceRegistersAndGenAIOps.md) (`AIAF-DOC-13`) tracks the tool catalog, this standalone document unites **both** the **High-Level `D1`-`D5` x AI Tool Permission Matrix** (`Section 2`) and the **Granular Enterprise Data Source Control Register** (`Section 3`) in one place for InfoSec and Data Stewards.

### 1.2 Who Normally Produces & Maintains This Document Internally

- **Primary Custodians**: Information Security (CISO Office) and Enterprise Data Governance / Architecture Lead, in partnership with the AI Center of Excellence (CoE).
- **Required Internal Contributors**:
  - **System & Repository Owners (Enterprise Collaboration Suite, ERP, Data Lakehouse, ITSM, Operational Systems)**: Confirm the highest data tier held in each repository and the active technical controls.
  - **Legal & Data Protection Officer (DPO)**: Confirm cross-border data residency (`global`, `us`, or `eu` multi-region) and statutory retention/deletion rules under applicable privacy and critical infrastructure mandates.

### 1.3 Recommended Two-Phase Implementation Approach for the AI CoE

1. **Phase A (Pre-Launch Quick Win - InfoSec & CoE Alignment)**: Review and ratify **Section 2** (`Tables 2.1 & 2.2`) so the CoE and Champions have a single `D1`-`D5` x Tool matrix ahead of initial rollout.
2. **Phase B (Rolling Repository Inventory)**: Use **Table 3.1** (`SRC-001` through `SRC-012`) as your living **Enterprise Data Source Control Register**. Start with the 12 core repository archetypes pre-populated below, and require any Business Unit proposing a new **Gateway 2** connector or agent to register their target data source in Table 3.1 before connector activation.

## 2. Stage 1: High-Level Data Classification Definitions & AI Tool Permission Matrix

### 2.1 The 5-Tier AI Data Classification Standard (`D1` to `D5`)

| Tier | Classification Name | Clear Operational Definition | Representative Enterprise Examples | Default AI Handling Rule |
| :---: | :--- | :--- | :--- | :--- |
| **`D1`** | **Public** | Information officially approved for public release where disclosure carries zero commercial, legal, or safety risk. | Published Annual & Sustainability Reports, press releases, public product catalogs, published whitepapers, public industry news. | **Open for All Approved AI Tools** (and safe personal learning off-network). |
| **`D2`** | **Internal** | Routine corporate and operational information accessible to broad internal staff where sensitivity is low. | Corporate HR/IT FAQs, general onboarding guides, internal newsletters, standard blank templates, non-confidential training decks. | **Permitted in Sanctioned Enterprise AI Only** (Enterprise AI Assistant, Grounded Knowledge Notebooks); prohibited in public consumer bots. |
| **`D3`** | **Confidential** | Business-sensitive operational, engineering, or commercial information restricted to specific teams or functions. | Engineering/operations maintenance SOPs, internal project plans, vendor RFP responses, ITSM ticket histories, operational KPI dashboards. | **Permitted via ACL-Enforced Grounding Only**: Must inherit per-user Identity Provider (IdP) permissions; zero model weight training. |
| **`D4`** | **Restricted (Need-to-Know)** | Highly sensitive strategic, financial, legal, or personal data where cross-entity or external disclosure causes severe harm. | Master service agreements (MSAs), strategic commercial contracts, business unit financial trial balances (ERP), customer pricing schedules, M&A files, employee PII/compensation. | **Restricted to Scoped Enclaves & Approved Gateway 2 Agents**: Requires explicit per-entity ACL isolation, Private Network Perimeter (VPC / Private Link), CMEK, and approved `AIIA`. |
| **`D5`** | **Regulated / Critical Infrastructure** | Data governed by strict national security, Critical Information Infrastructure (`CII`), operational technology (`OT`), or statutory mandates. | Live industrial/operational control commands, regulated trade/health/banking secrets, security telemetry, cryptographic keys/secrets. | **Prohibited from Cloud LLM Prompts**: Remains strictly inside isolated boundaries unless formally anonymized via DLP and cleared by CISO/Legal. |

### 2.2 The `D1`-`D5` x AI Tool Permission Matrix (Where Data Can and Cannot Be Used)

| AI Tool / Platform Surface | `D1 Public` | `D2 Internal` | `D3 Confidential` | `D4 Restricted (NTK)` | `D5 Regulated / Critical` | Mandatory Runtime Condition |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Enterprise AI Assistant Web Chat & File Upload (`Gateway 1`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *CONDITIONAL* (Only by authorized user; do not re-share output broadly) | **PROHIBITED** | Corporate IdP SAML 2.0 SSO login; zero model training. |
| **2. Enterprise Federated Repository & Collaboration Search** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *CONDITIONAL* (Strictly bounded by caller's own IdP OAuth 2.0 ACL) | **PROHIBITED** | Per-user delegated OAuth 2.0 token + network egress allowlisting. |
| **3. Enterprise Deep Research (`Web + Enterprise Grounding`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *PROHIBITED* in outbound web search strings (keep `D4` local to tenant) | **PROHIBITED** | Never include confidential customer or M&A names in public web search queries. |
| **4. Grounded Knowledge Notebooks (`Departmental Workspaces`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *CONDITIONAL* (Permitted ONLY in security-group-locked enclave workspaces) | **PROHIBITED** | Share notebooks strictly with synchronized Enterprise IdP security groups ([AIAF-DOC-05](05_KnowledgeNotebookAndPromptPlaybook.md)). |
| **5. No-Code Agent Builder - Personal Assistant (`Gateway 1`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *PROHIBITED* for shared publishing (use Gateway 2) | **PROHIBITED** | Scoped to creator's own corporate identity; read-only retrieval. |
| **6. No-Code Agent Builder - Departmental Shared (`Gateway 2`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *CONDITIONAL* (Requires approved `AIIA` & CISO/Legal sign-off) | **PROHIBITED** | 4-Stage Gateway 2 HITL approval + 25-50 Q&A Golden Dataset (`>= 85%`). |
| **7. Code-First Custom Agent on Enterprise Agent Runtime (`Gateway 2`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | **PERMITTED (With Controls)** (Read-only SQL/MCP + mandatory human HITL) | **PROHIBITED** | Approved `AIIA` ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)), Private Network Perimeter, CMEK, Inline Prompt & Output Guardrail API callback, 100-sample Golden Eval, 90-day kill-switch. |
| **8. Productivity Suite In-App Assistants (`<Enterprise Collaboration Suite>`)** | **PERMITTED** | **PERMITTED** | **PERMITTED** | *CONDITIONAL* (Subject to folder permissions & sensitivity labels) | **PROHIBITED** | Restricted to licensed cohort; corporate IdP and DLP controls. |
| **9. Internal Domain-Specific Operational / Predictive ML** | **PERMITTED** | **PERMITTED** | **PERMITTED** | **PERMITTED** (Within domain boundary) | **PERMITTED (In Isolated Enclave Only)** | Strictly isolated within regulated/OT network segmentation. |
| **10. Unsanctioned Public Consumer AI Web Bots & Extensions** | **PERMITTED** (Off-network personal learning only) | **PROHIBITED** | **PROHIBITED** | **PROHIBITED** | **PROHIBITED** | Never log in with corporate SSO or paste any non-public corporate text/code. |

## 3. Stage 2 (Longer-Term Living Register): Enterprise Data Source & Technical Control Inventory

```
+-----------------------------------------------------------------------+
|     ENTERPRISE DATA SOURCE TO AI GROUNDING CONTROL FLOW (D1 - D5)     |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 1: IDENTIFY REPOSITORY & HIGHEST DATA CLASSIFICATION (D1 - D5)  |
|  * Record system platform, named Data Steward, and regulatory regime. |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 2: ENFORCE IDENTITY, NETWORK & PERIMETER CONTROLS               |
|  * Corporate IdP SAML/SCIM + External B2B Guest Filter + OAuth ACLs   |
|  * Network Egress + Private Network Perimeter + CMEK + Guardrail API  |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STEP 3: BIND TO APPROVED AI CONSUMPTION PATTERN                      |
|  * D1-D3: Federated Search or Curated Departmental Knowledge Spaces   |
|  * D4: Scoped Enclave Workspace or Gateway 2 Read-Only Custom Agent   |
|  * D5: Isolated Operational Boundary (Zero Cloud LLM Prompt Input)    |
+-----------------------------------------------------------------------+
```

### 3.1 Enterprise Data Source & Control Register (`Pre-Structured Template Baseline`)

| Source ID | Data Source / Repository Name | Platform / Host Environment | Highest Data Tier Held | Regulatory / Policy Regime | Permitted AI Consumption Mode | Technical & Access Controls in Place | Named Data Steward (Role) | Audit & Review Cadence |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| `SRC-001` | **Global Corporate Intranet, HR & IT Policy Portals** | `<Enterprise Intranet & Document Management Suite>` | **`D2 Internal`** | Corporate IT & Privacy Baseline | Federated Search (`Gateway 1`), Departmental Knowledge Workspaces, `UC-005` Helpdesk Agent. | Corporate IdP SAML 2.0 SSO; External B2B Guest Filter (`userType EQUALS 'Member'`); read-only OAuth ACLs. | HR & IT Portal Stewards | Quarterly |
| `SRC-002` | **Operations, Engineering & Preventive Maintenance Manuals** | `<Engineering Document Libraries / Cloud Object Storage>` | **`D3 Confidential`** | Workplace Safety & Vendor IP | Curated Departmental Knowledge Workspaces (`1M-2M` context) or Ingested RAG with Layout-Aware Document Parser. | Synchronized Enterprise IdP engineering security groups; mandatory inline citation links to source PDF tables. | Head of Engineering / Operations | Quarterly (90-Day Freshness Check) |
| `SRC-003` | **Corporate Communications, Commercial Proposals & Marketing Assets** | `<Cloud Document Repositories>` | **`D2` / `D3`** | Commercial Confidentiality | Enterprise AI Assistant Chat, Collaborative Drafting Canvas, and Federated Document Search. | Per-user delegated OAuth 2.0 permissions; network egress allowlisting. | Commercial & Corporate Comms Leads | Semi-Annual |
| `SRC-004` | **Employee Individual Email & Calendar Workspaces** | `<Enterprise Email & Calendar System>` | **`D3`** (Contains occasional `D4`) | Global Data Privacy | Federated Mail/Calendar Connector (`Gateway 1` personal user session only; never indexed into shared group stores). | Strictly scoped to the authenticated individual user's OAuth token; zero cross-user visibility. | Enterprise Messaging & Identity Lead | Semi-Annual |
| `SRC-005` | **ITSM & Employee Support Ticket Repository** | `<ITSM Platform>` | **`D3 Confidential`** | Corporate IT & Employee Privacy | Sanitized common resolution articles curated into `UC-005` IT/HR Helpdesk Agent (`Gateway 2`). | PII redaction prior to workspace curation; read-only grounding; one-click human specialist escalation. | Head of IT Service Management (ITSM) | Quarterly |
| `SRC-006` | **Procurement Vendor RFPs & Standard Contract Templates** | `<Procurement Folders / Enterprise Procurement Portal>` | **`D3`** (`D4` for active sealed bids) | Commercial & Procurement Governance | Scoped Departmental Workspaces and `UC-008` RFP Comparison Workflow (`Gateway 1/2`). | Restricted to Procurement security groups; Runtime AI Guardrail Service prompt-injection screening on external vendor PDFs (`LLM01`). | Head of Corporate Procurement | Quarterly |
| `SRC-007` | **Multi-Entity Financial Trial Balances & Monthly Variance Exports** | `<Enterprise Financial ERP Exports>` | **`D4 Restricted`** | Financial Audit, Tax & Board Reporting | **Gateway 2 Code-First Financial Consolidation Agent (`UC-004`)**: Deterministic Python/SQL code execution + grounded narrative synthesis. | Strict per-entity RBAC (`SG-AI-Finance-Controllers`); **read-only credentials** (zero ERP write access); Private Network Perimeter; CMEK; mandatory human controller sign-off. | Corporate Financial Controller / CFO Steward | Monthly |
| `SRC-008` | **Enterprise Operational & Commercial Analytics Lakehouse** | `<Enterprise Data Warehouse / Cloud Data Lakehouse>` | **`D3` / `D4`** | Multi-Entity Data Governance | **Gateway 2 Code-First Analytics Agent (`UC-006`)** via read-only Model Context Protocol (`MCP`) server. | Per-user OAuth 2.0 identity passthrough enforcing catalog row/column ACLs; read-only SQL execution; query cost/timeout caps. | Head of Enterprise Data & Analytics | Quarterly |
| `SRC-009` | **Master Service Agreements, Strategic Commercial Contracts & M&A Legal Vaults** | `<Restricted Legal Document Enclaves>` | **`D4 Restricted`** | Legal Privilege, Confidentiality, GDPR | **Scoped Legal Enclave Knowledge Workspaces (`UC-007`)** (and regional `eu`/`us` multi-region instances where required). | Entity-specific security group isolation (`0%` cross-entity leakage verified in UAT); CMEK encryption; mandatory Legal Counsel review. | General Counsel & Legal Operations Stewards | Quarterly |
| `SRC-010` | **Customer Operations Incident Feeds & Advisory Knowledge Base** | `<CRM / Customer Operations Portals>` | **`D3 Confidential`** | Customer Contract Confidentiality | `UC-009` Customer Advisory Drafter (`Gateway 2`) combining approved incident summaries with Enterprise Deep Research. | Customer PII minimization; human operations coordinator review before sending advisories to customers. | Head of Customer Operations | Quarterly |
| `SRC-011` | **Regulatory Compliance & Statutory Reference Manuals** | `<Compliance & Regulatory Document Libraries>` | **`D1` to `D3`** (`D5` for live statutory filings) | Sector Regulatory & Compliance Laws | Reference compliance manuals grounded in Knowledge Workspaces; **live statutory filings remain in core transactional systems**. | Separation of reference compliance manuals (`D1-D3`) from live statutory submissions (`D5`). | Chief Compliance Officer / Regulatory Steward | Semi-Annual |
| `SRC-012` | **Live Critical Infrastructure, Industrial OT & Core Control Systems** | `<Core Operational Technology (OT) / Industrial Control Systems>` | **`D5 Regulated / Critical`** | Critical Infrastructure & Sector Security Mandates | **PROHIBITED from Corporate Cloud LLM Prompts**: Handled exclusively by internal domain models within the isolated boundary. | Air-gapped / segmented network perimeter; only de-identified equipment maintenance manuals (`SRC-002`) enter corporate Grounded Knowledge Notebooks. | CISO & Head of Critical Operations | Continuous / Annual Audit |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Data & Knowledge Perspective, grounding vs. training governance, and retrieval access scoping.
- [References](../References.md): Maintained catalog of regulatory, security, and architectural standards.
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final): Fine-grained access control, per-session authorization, and data perimeter isolation.
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/): Controls for `LLM02` (Sensitive Information Disclosure) and `LLM08` (Vector and Embedding Weaknesses).
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Auditable data governance and lifecycle inventory controls.
