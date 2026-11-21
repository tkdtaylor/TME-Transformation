<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-02` (Enterprise AI Policy, Data Classification [D1-D5] & Non-Human Actor Standard) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Chief Information Security Officer (CISO) / InfoSec, Enterprise IT Architecture, Data Stewards, and Legal & Compliance |
| **Primary Internal Owner** | CISO / Head of Information Security, Head of Enterprise IT & AI Center of Excellence (CoE) Lead |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE), Information Security, Data Governance, and Legal teams establish a unified Enterprise AI Policy, 5-Tier Data Classification (`D1` to `D5`), and Non-Human Actor Standard. It is **not** prescriptive. Sections include pre-structured tables for data classification, domain readiness scoring, the 7 classes of AI knowledge assets (`KNA-01` to `KNA-07`), Shadow AI safe channeling, and the 5 Non-Human Actor personas (`NHA-01` to `NHA-05`) so teams do not have to start from a blank page.

## 1. How the AI CoE Can Create, Customize & Run an Internal Working Session for This Document

### 1.1 Purpose & Why This Document Exists

A primary cause of stalled enterprise AI rollouts is "Governance Theater" or policy ambiguity: employees either upload sensitive corporate documents into unsanctioned public AI tools (**Shadow AI**), or Information Security teams block high-value internal deployments because **inference-time grounding (RAG)** is conflated with **model weight training**.

This document provides the canonical **AIAF Enterprise AI Policy, Data Classification (`D1` to `D5`), and Non-Human Actor Standard**. It exists to establish four enforceable technical and legal standards:

1. **5-Tier AI Data Classification (`D1` to `D5`)**: Defines exactly which classes of enterprise data may enter which AI tools and under what security controls (Corporate IdP SSO, source ACL inheritance, Private Network Perimeter, CMEK).
2. **Mandatory Inference-Time Grounding Standard**: Codifies that corporate and business unit documents enter the **Enterprise AI Platform** strictly at inference time via access-controlled Grounding (never via foundation model weight training).
3. **7 Classes of AI Knowledge Assets & Shadow AI Channeling**: Treats reusable prompts, curated workspaces, retrieval indexes, and Golden Evaluation Datasets as governed enterprise assets, while channeling employee demand away from public consumer bots into the organization's sanctioned tenant.
4. **Non-Human Actor Governance (5 Agent Personas)**: Establishes identity, least-privilege scoping, Human-in-the-Loop (`HITL`) write gates, and 90-day kill-switch drills for every AI assistant and agent operating across the enterprise estate.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Primary Internal Authors**: Information Security (CISO Office), Enterprise Data Architecture Lead, and AI CoE Lead.
- **Required Internal Contributors**:
  - **Legal & Data Protection Officer (DPO)**: Validates `D4 Restricted` (confidential contracts, M&A, PII) and `D5 Regulated / Critical` boundaries.
  - **Identity & Collaboration Administrators**: Validate Identity Provider (IdP) SAML 2.0 / SCIM 2.0 group scoping, external B2B guest filtering, and source document ACL inheritance.
  - **Business Unit Data Stewards**: Validate domain data quality and pre-grounding remediation steps.
- **Accountable Sign-Off**: Head of Enterprise IT and CISO prior to production cutover and Gateway 2 agent promotion.

### 1.3 Recommended Approach: Running a CoE & InfoSec Policy Alignment Working Session

The fastest way for the AI CoE to finalize and ratify this policy is to convene an internal working session with Information Security (CISO), Enterprise Data Architecture, Identity/Collaboration Admins, and Legal:

1. **Part 1 - Map Internal Data Labels & Domain Readiness (Sections 2.1 & 2.2)**: Align the organization's existing corporate security classification labels (e.g., *Public, Internal, Confidential, Restricted, Secret*) to the 5-Tier `D1` to `D5` table below, and confirm pre-grounding remediation steps for document repositories, ERP, and lakehouse platforms.
2. **Part 2 - Assign Custodians for the 7 AI Knowledge Asset Classes & Shadow AI Rules (Sections 2.3 & 3)**: Confirm which internal teams in Enterprise IT, Digital Transformation, or Business Units own the central catalog for Role-Based Prompts, Departmental Knowledge Workspaces, and Golden Evaluation Datasets, and ratify the Shadow AI channeling policy.
3. **Part 3 - Ratify the Non-Human Actor Policy (Section 4)**: Confirm the service principal naming convention, mandatory Human-in-the-Loop (`HITL`) gates, and 90-day kill-switch verification owner for Tier 2 and Tier 3 agents deployed via the **Enterprise Agent Runtime (Code-First Agent SDK)** and **No-Code Agent Builder**.

## 2. 5-Tier AI Data Classification (`D1`-`D5`) & Knowledge Asset Inventory (Template Baseline)

### 2.1 Enterprise 5-Tier AI Data Classification & Grounding Rules

> **Companion Operational Deep-Dives:** This section defines the overarching 5-tier policy taxonomy (`D1` to `D5`). For the granular 10-surface **`D1-D5 x AI Tool` Permission Matrix** and the **12-Repository Enterprise Data Source Control Register (`SRC-001` to `SRC-012`)**, see [03 AI Data Classification Matrix & Enterprise Data Source Control Register](03_DataClassificationMatrixAndSourceRegister.md) (`AIAF-DOC-03`). For the 1-page visual employee guide, see [04 Employee AI Acceptable Use Policy (AUP) & Traffic-Light Guide](04_EmployeeAcceptableUseGuide.md) (`AIAF-DOC-04`).

| Data Tier | Classification Label | Representative Enterprise Data Assets | Allowed AI Usage & Grounding Policy | Mandatory Technical & Security Controls |
| :---: | :--- | :--- | :--- | :--- |
| **`D1`** | **Public** | Published annual reports, public product/service catalogs, press releases, published sustainability reports, public industry news. | **Permitted across all approved tools**: Enterprise AI Assistant Web Chat, Public Web Search Grounding, Enterprise Deep Research, and safe personal learning. | Standard enterprise authentication; zero confidential data inclusion. |
| **`D2`** | **Internal** | General corporate HR policies, IT helpdesk FAQs, onboarding guides, corporate communications templates on internal portals. | **Permitted for all licensed users**: Enterprise AI Assistant Chat, File Upload, Grounded Knowledge Notebooks, and Gateway 1 No-Code Agent Builder assistants. | Corporate IdP SAML 2.0 SSO; external B2B guests blocked (`userType EQUALS 'Member'`); zero model training. |
| **`D3`** | **Confidential** | Departmental operational SOPs, engineering/technical maintenance manuals, internal ITSM tickets, vendor RFPs, non-public operational KPIs. | **Permitted via ACL-Enforced Grounding Only**: Federated Enterprise Repository Connectors, Departmental Knowledge Workspaces, or scoped Gateway 2 agents. | Per-user IdP OAuth 2.0 source ACL inheritance; network egress allowlisting; Immutable Audit Logs enabled. |
| **`D4`** | **Restricted** | Business unit financial statements (ERP), master service agreements (MSAs), strategic commercial contracts, customer pricing schedules, employee PII, M&A packets. | **Restricted to Scoped Enclaves & Approved Tier 2/3 Agents**: Permitted only in strictly ACL-isolated Knowledge Workspaces or Gateway 2 agents with completed `AIIA`. | Strict per-entity ACL isolation; Private Network Perimeter (VPC / Private Link); Customer-Managed Encryption Keys (CMEK); named human `Decision Owner` in `AIDecisionRegister`. |
| **`D5`** | **Regulated / Critical Infrastructure** | Live industrial/operational control commands (`OT`), statutory secrets, regulated security telemetry, cryptographic keys, unredacted sensitive PII. | **Prohibited from Cloud LLM Prompts**: Must remain within isolated boundaries unless explicitly anonymized via Enterprise Data Loss Prevention (DLP) / PII Redaction and approved by CISO and Legal. | Network segmentation / air-gap separation; Enterprise DLP / PII Redaction; formal Security & Legal sign-off. |

### 2.2 Core Enterprise Data Domain Readiness Scorecard (`1 = Poor` to `5 = AI-Ready`)

| Data Domain / Repository | Tier (`D1`-`D5`) | Primary Storage Platform | Grounding or Training? | Completeness (1-5) | Accuracy (1-5) | Consistency (1-5) | Freshness (1-5) | Accessibility (1-5) | AI Readiness Avg | Required Pre-Ground Remediation |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Corporate HR, IT & Procurement Policies** | `D2 / D3` | `<Enterprise Collaboration & Document Suite>` | Grounding Only | 4 | 4 | 4 | 4 | 4 | **4.0 / 5.0** | Curate authoritative PDF/document versions into Departmental Knowledge Workspaces to avoid stale draft retrieval. |
| **Operations & Engineering Manuals** | `D3` | `<Document Libraries / Cloud Object Storage>` | Grounding Only | 4 | 5 | 3 | 4 | 3 | **3.8 / 5.0** | Use Layout-Aware Document Parser / Grounded Knowledge Notebooks for complex multi-column PDF schematics and tables. |
| **Financial Exports & Trial Balances** | `D4` | `<Enterprise ERP & Data Lakehouse>` | Grounding / Code Exec | 5 | 5 | 3 | 4 | 3 | **4.0 / 5.0** | Standardize chart-of-accounts mapping across entities; route large tabular math (`>500,000` words) via Code-First Agent / Lakehouse MCP rather than text RAG. |
| **Commercial & Legal Contract Vaults** | `D4` | `<Restricted Legal Document Enclaves>` | Grounding Only | 5 | 5 | 3 | 5 | 2 | **4.0 / 5.0** | Enforce strict per-entity security group isolation before indexing. |
| **ITSM & Employee Support Ticket History** | `D2 / D3` | `<ITSM Platform>` | Grounding Only | 4 | 4 | 3 | 5 | 4 | **4.0 / 5.0** | Redact personal identifiers before curating common resolved ticket patterns into Tier-1 Helpdesk knowledge bases. |

### 2.3 Inventory of the 7 Classes of AI Knowledge Assets

> **Companion Curation Playbook:** For the 5-stage curation SOP, `R-C-T-V` prompt template, 90-day freshness review cycle, and pre-populated asset catalog (`CAT-001` to `CAT-008`) governing `KNA-01` through `KNA-03`, see [05 Departmental Knowledge Notebook & Prompt Library Curation Playbook & Asset Catalog](05_KnowledgeNotebookAndPromptPlaybook.md) (`AIAF-DOC-05`).

| Asset Class ID | AI Knowledge Asset Class | Baseline Pilot State (Typical) | Designated Owner | Target Governance & Architecture Standard |
| :--- | :--- | :--- | :--- | :--- |
| `KNA-01` | **Prompt Libraries** (reusable role-based system and task prompts) | Ad-hoc individual prompts created during pilot (export saved prompts prior to pilot decommission). | AI CoE Champions & Enablement Lead | Publish curated **Role-Based Prompt Starter Kit** (Finance, Legal, HR, IT, Operations) ahead of initial launch. |
| `KNA-02` | **Retrieval Indexes & Grounding Stores** | Ad-hoc file uploads; transitioning to governed production instance. | Cloud Platform Team & Departmental Knowledge Curators | Hybrid Grounding: (1) Departmental Knowledge Workspaces, (2) Federated Enterprise Repository Connectors, (3) Lakehouse MCP, (4) Network Egress Controls. |
| `KNA-03` | **Evaluation / Golden Datasets** (curated Q&A test sets and grading rubrics) | Absent during initial pilot (relied on manual spot-checks). | AI CoE + Business Unit Domain Owners | Curate **25 to 50 Q&A Golden Dataset** for authoritative SOPs and 100-sample Golden Datasets for Code-First Custom Agents. |
| `KNA-04` | **Embeddings & Vector Stores** | Managed internally per workspace. | Cloud Platform Team | Managed within Enterprise Grounded Search / Vector Platform with tenant-isolated namespaces and CMEK encryption. |
| `KNA-05` | **Fine-Tuned / Distilled Models** | Used only in specialized predictive/operational ML systems. | Data Science / ML Engineering | **Enterprise GenAI is 100% Grounding-First**: zero LLM weight fine-tuning on `D3/D4` corporate documents; use Prompt / Context Caching (`>32k` tokens) instead. |
| `KNA-06` | **Synthetic Test Datasets** | Emerging in non-production environments. | Enterprise IT & Technical Builders | Mandatory synthetic financial and operational datasets for all `L300` developer bootcamps and non-production sandboxes. |
| `KNA-07` | **AI-Generated Downstream Artifacts** (reports, code, SOP summaries) | Ungoverned ad-hoc sharing. | Document / Process Owners | Require inline source citation verification and human owner review before saving AI-generated summaries into authoritative folders. |

## 3. Enterprise Grounding Policy, Shadow AI Channeling & Build-vs.-Buy Standard

### 3.1 Mandatory Inference-Time Grounding vs. Model Training Policy

1. **Zero Foundation Model Training on Enterprise Data**: Under the organization's enterprise AI platform contractual terms, corporate prompts, uploaded files, retrieval queries, and grounding corpora are **never** used to train external foundation models or shared across customer tenants.
2. **Inference-Time Grounding Only**: All corporate knowledge must be supplied at inference time via **Enterprise Grounded Search**, **Grounded Knowledge Notebooks**, or read-only **Model Context Protocol (MCP)** connectors. This ensures real-time enforcement of Identity Provider permissions and immediate revocation whenever a document is updated or deleted.
3. **Context Caching Standard**: For recurring queries against large static reference manuals, tariff books, or technical specifications exceeding `32,768` tokens, technical builders should enable **Prompt / Context Caching** to reduce input token costs by up to 75% while preserving strict tenant isolation.

### 3.2 Shadow AI Safe Channeling Policy

| Usage Scenario | Policy Status | Allowed Data Tiers | Channeling & Enforcement Rule |
| :--- | :---: | :---: | :--- |
| **Unsanctioned Public Consumer AI Tools** (free consumer web bots, unverified browser extensions, personal accounts) | **PROHIBITED for Corporate Data** | `D1 Public` Only (personal learning off corporate network) | Never authenticate with corporate SSO, never invite external recording bots into virtual meetings, and never paste `D2`-`D5` corporate data. Channel all productivity demand into the sanctioned **Enterprise AI Assistant**. |
| **Gateway 1: Self-Service Personal & Departmental Productivity** (Enterprise AI Assistant Web App, Grounded Knowledge Notebooks, Personal No-Code Agent Builder) | **APPROVED (Default)** | `D1` to `D3` (`D4` only in ACL-isolated Knowledge Workspaces) | Bounded strictly by the signed-in user's own IdP OAuth 2.0 identity; zero shared service principals or external write actions. |
| **Gateway 2: Enterprise Shared Agents & System Integrations** (Org-wide Agent Builder publishes, Code-First Custom Agents, Lakehouse/ERP MCP) | **APPROVED (Gated by 4-Stage HITL Review)** | `D1` to `D4` (per approved `AIIA`) | Requires AI CoE intake approval (`AIUseCaseCard`), security/ACL verification, Golden Dataset evaluation (`>= 85%` groundedness), and `AIDecisionRegister` sign-off. |

### 3.3 Build vs. Buy Reassessment ("The Vendor Bypass Pattern")

> **Companion Procurement Checklist:** For the operational two-stage procurement gate (Stage 1 Core Platform Bypass Check + Stage 2 10-Point Vendor Security & Legal Checklist `VND-001` to `VND-010`), see [14 Third-Party SaaS & Vendor AI Procurement Assessment Checklist](14_VendorAIProcurementChecklist.md) (`AIAF-DOC-14`).

| Software / Workflow Category | Traditional SaaS Approach | AI Adoption Framework Decision (`Keep / Evaluate / Build`) | Rationale & Target Architecture |
| :--- | :--- | :---: | :--- |
| **Core ERP, ITSM & Cloud Productivity** (`<Enterprise ERP, ITSM Platform, Enterprise Collaboration Suite, Cloud Data Lakehouse>`) | Core transactional systems of record | **KEEP (Core Systems of Record)** | Authoritative transactional engines and data stores remain in place ("Zero Data Movement"). |
| **Siloed Point-Solution SaaS AI Add-Ons** (separate per-seat AI copilot add-ons inside every individual SaaS tool) | High per-seat markups restricted to a single vendor's data silo | **EVALUATE / BYPASS via Enterprise AI Platform** | Deploy our **Enterprise AI Platform** across knowledge workers as the unified cross-platform reasoning layer spanning workspace docs, PDFs, web, and enterprise data. |
| **Cross-System Multi-Step Workflows** (Multi-entity financial variance commentary, cross-system operational analytics) | Expensive bespoke system integrator custom portals | **BUILD on Code-First Agent SDK & No-Code Agent Builder** | Use Code-First Custom Agents and `L200` Departmental Champions to compose lightweight agents over existing APIs at a fraction of legacy custom software cost. |

## 4. Non-Human Actor Governance Policy (5 Agent & System Personas)

> **Companion Incident & Kill-Switch Runbook:** For the step-by-step 5-layer 15-minute emergency containment procedures and quarterly 90-day kill-switch drill log (`KSD-001` to `KSD-004`), see [06 AI Security Incident Response & 90-Day Kill-Switch Drill Runbook](06_AISecurityIncidentAndKillSwitchRunbook.md) (`AIAF-DOC-06`).

**Important: The Golden Accountability Rule**: An AI model, agent, or cloud service principal can **never** be listed as the accountable owner of a business decision. Every non-human actor must have a named human **`Decision Owner`** and **`Human Accountable`** recorded in `AIDecisionRegister` ([AIAF-DOC-13](13_OperationalGovernanceRegistersAndGenAIOps.md)).

| Persona ID | Non-Human Actor Persona | Enterprise Deployment Pattern | Machine Principal / Identity Standard | Max Risk Tier | Mandatory Governance, HITL & Kill-Switch Cadence |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `NHA-01` | **1. Interactive AI Assistant** | **Enterprise AI Assistant Chat, Deep Research & Grounded Knowledge Notebooks** (All licensed users) | Executes strictly under the **human user's IdP OAuth 2.0 token** (`On-Behalf-Of` ACLs). | Tier 1-2 | Governed by Platform Admin Console policies; mandatory inline citations for grounded responses. |
| `NHA-02` | **2. Scoped Agent** | **IT & HR Helpdesk Agents** or Departmental SOP Assistants in **No-Code Agent Builder** | Scoped to explicit document folders or Knowledge Workspace corpora; inherits caller's IdP permissions. | Tier 2 | Registered in `AIDecisionRegister` with a named departmental owner; strictly read-only by default. |
| `NHA-03` | **3. Service Agent** | **Automated Document Ingestion & Layout Parsing Pipelines** | Dedicated least-privilege Cloud Service Principal (`sa-agent-ingest-<env>`); zero shared user keys. | Tier 2-3 | Federated Workload Identity / 90-day rotation; token budget alerts to prevent runaway batch consumption. |
| `NHA-04` | **4. Tool-Using Agent** | **Code-First Finance Consolidation Agent** & **Enterprise Analytics Agent** | Dedicated agent identity + per-user OAuth 2.0 token pass-through for read-only SQL/ERP queries. | Tier 3 | Requires approved `AIIA` ([AIAF-DOC-12](12_AIImpactAssessmentAndOWASPControls.md)), **mandatory HITL approval** before any write action, and a **90-day tested kill-switch**. |
| `NHA-05` | **5. Multi-Agent System** | **Cross-Domain Operations & Supply Chain Coordinator** (Coordinated Sub-Agents) | Distinct sub-agent service principals with hard recursion caps (`max_steps <= 10`) and Runtime AI Guardrail Service screening. | Tier 3-4 | Full distributed execution tracing; automated circuit-breaker and **90-day tested kill-switch drill**. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Data & Knowledge Perspective (grounding vs. training data), Non-Human Actors, and Risk Tier Classification.
- [References](../References.md): Maintained catalog of regulatory and security references.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1): Controls for data governance, privacy, and risk management.
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/): Risk mapping for prompt injection, sensitive data disclosure, and excessive agency.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Auditable AI management system controls and lifecycle governance.
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final): Identity-based perimeter and least-privilege non-human actor isolation.
