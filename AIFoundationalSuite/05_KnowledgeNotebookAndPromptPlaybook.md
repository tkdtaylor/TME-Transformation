<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 05 Departmental Knowledge Notebook & Prompt Library Curation Playbook & Asset Catalog

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-05` (Departmental Knowledge Notebook & Prompt Library Curation Playbook & Shared Asset Catalog) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | Early-Access Power Users / CoE Champions, L200 Departmental Champions, Digital Transformation Leads, and Enterprise IT |
| **Primary Internal Owner** | AI Center of Excellence (CoE) Enablement Lead & Departmental Knowledge Curators |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reusable Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as a reusable, industry-agnostic reference template and optional starting baseline to help an organization's AI Center of Excellence (CoE) and Departmental Champions (`L200`) curate, benchmark, and govern shared **Grounded Knowledge Notebooks (Departmental Knowledge Workspaces)** and reusable prompt libraries. It is **not** prescriptive. Sections include a **5-Stage Curation Lifecycle SOP**, the **4-Part Role-Based Prompt Structure (`R-C-T-V`)**, and a pre-structured **Shared AI Knowledge Asset Catalog (`CAT-001` to `CAT-008`)** so teams do not have to start from a blank page. Organizations can share this playbook directly or customize the bracketed fields to fit their internal governance standards.

## 1. How the AI CoE & Champions Can Use This Playbook

### 1.1 Purpose & Why This Document Exists

In [02 Enterprise AI Policy, Data Classification (D1-D5) & Non-Human Actor Standard](02_EnterpriseAIPolicyAndDataClassification.md) (`AIAF-DOC-02`, Section 2.3), an organization's **Prompt Libraries (`KNA-01`)**, **Departmental Knowledge Workspaces / Grounding Stores (`KNA-02`)**, and **Golden Evaluation Datasets (`KNA-03`)** are defined as core enterprise knowledge assets. However, as **Early-Access Power Users / CoE Champions** and **Departmental Champions (`L200`)** begin curating shared workspaces across business units, two operational failure modes commonly occur:

1. **"Corpus Rot" & Data Poisoning (`OWASP LLM04`)**: Well-meaning users upload unapproved draft documents, superseded policy versions, or conflicting spreadsheets into a shared workspace, causing the AI to cite outdated procedures.
2. **Siloed Duplication Across Business Units**: Multiple regional or functional teams independently spend hours building identical prompt templates for financial variance commentary, incident summaries, or procurement RFP comparisons because no central catalog exists.

This playbook provides the **5-Stage Curation Lifecycle SOP** (`Section 2`), **Naming & ACL Standards** (`Section 3`), and a **Reusable Shared AI Knowledge Asset Catalog (`Section 4`)** so CoE Champions can build once, verify quality, and share safely across the enterprise.

### 1.2 Who Normally Produces & Maintains This Catalog Internally

- **Catalog Custodian**: AI Center of Excellence (CoE) Enablement Lead.
- **Asset Curators (`Knowledge Workspace & Prompt Owners`)**: Designated **CoE Champions (`Power Users`)** and **Departmental Champions (`L200`)** within Operations, Engineering, Finance, Legal, HR, IT, Procurement, and Commercial teams.
- **Recommended Operating Rhythm**: Introduce this playbook during the **Track 1 (`L200`) Champion Enablement Workshop** prior to initial launch and review catalog freshness once every **90 days**.

## 2. The 5-Stage Departmental Knowledge Notebook & Prompt Curation Lifecycle SOP

```
+-----------------------------------------------------------------------+
|   AI CoE: 5-STAGE KNOWLEDGE NOTEBOOK & PROMPT CURATION LIFECYCLE SOP  |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 1: AUTHORITATIVE SOURCE SELECTION & CLEANUP                    |
|  * Select signed-off PDFs/docs only; exclude drafts & personal        |
|    scratch sheets; verify D1-D4 classification in AIAF-DOC-03.        |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 2: STRUCTURAL PREPARATION & CHUNKING CHECK                     |
|  * Ensure clear section headings & table titles; route >500k-word     |
|    tabular ledgers to Code Execution / Custom Agents over text RAG.   |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 3: NAMING CONVENTION & SECURITY GROUP ACL BINDING              |
|  * Name: [<ORG>-<BU>] <Domain> - <Workspace Name> (vX.Y)              |
|  * Share as 'Viewer' ONLY with synchronized IdP security groups.      |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 4: PRE-PUBLISH GOLDEN DATASET BENCHMARK (25-50 Q&A PAIRS)      |
|  * Test 25-50 real departmental questions; verify >= 85% groundedness |
|    and accurate inline citations before announcing to the department. |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  STAGE 5: CATALOG REGISTRATION & 90-DAY FRESHNESS ATTESTATION         |
|  * Register in Table 4.1 below; every 90 days, the named Curator      |
|    replaces superseded SOPs and archives obsolete workspaces.         |
+-----------------------------------------------------------------------+
```

### 2.1 Detailed Curation Rules for CoE Champions

| Curation Rule | Standard for Departmental Curators | Why This Matters in Enterprise AI |
| :--- | :--- | :--- |
| **1. Authoritative Final Versions Only (`Zero Drafts`)** | Never upload documents marked `DRAFT`, `WIP`, or `Track Changes` into a shared Departmental Knowledge Workspace. Upload only signed-off, dated PDFs or formatted enterprise documents. | Prevents the model from blending an unapproved draft clause with an official corporate policy (`OWASP LLM04`). |
| **2. Explicit Metadata Header on Every Source File** | Ensure the filename and first page of each uploaded SOP state the **Document Title, Effective Date (`YYYY-MM-DD`), Version, and Applicable Business Unit/Region**. | Enables Enterprise Grounded Search and Grounded Knowledge Notebooks to distinguish between *prior-year vs. current-year policies* or *Region A vs. Region B rules*. |
| **3. Respect the `500,000-Word` Per-File Limit & Tabular Routing** | Keep individual source documents under **500,000 words** (and under the **100-source / 200 MB** per-workspace threshold). Do not upload massive raw ERP transaction dumps into text notebooks. | Full-context synthesis excels on policy, legal, and technical manuals (`1M-2M` tokens), whereas large tabular calculations belong in **Python Code Execution / Code-First Agent Runtime**. |
| **4. Viewer-Only Group Sharing (`Least Privilege`)** | Grant Editor (Curator) rights to designated CoE Champions (such as a primary curator and backup) per workspace; grant **Viewer** rights to the target department's synchronized Enterprise IdP security group (e.g., `SG-AI-Engineering-Ops`). | Prevents accidental source deletion or unreviewed file uploads by general users while guaranteeing continuity if one curator is on leave. |
| **5. Mandatory 90-Day Freshness Attestation** | Every registered knowledge workspace and prompt pack has a `Next Review Date` (**90 days** from publish). If an underlying SOP changes, the Curator swaps the file within **5 business days**. | Eliminates "corpus rot" and ensures employees always query the latest effective procedure. |

## 3. Standard Naming & Role-Based Prompt Structure

### 3.1 Naming Standard for Shared Knowledge Workspaces & Agents

Use a consistent prefix so employees can immediately recognize official CoE-curated assets in the **Enterprise AI Platform**:

- **Global Corporate Knowledge Workspaces**: `[<ORG>-GLOBAL] <Function> - <Topic Name> (v<X.Y>)`
  - *Example*: `[CORP-GLOBAL] HR - Global Mobility, Leave & Business Travel Policies (v1.0)`
- **Business Unit / Regional Knowledge Workspaces**: `[<ORG>-<BU/REGION>] <Function> - <Topic Name> (v<X.Y>)`
  - *Example*: `[CORP-OPS] Engineering - Preventive Maintenance & Reliability Manuals (v1.0)`
  - *Example*: `[CORP-CS] Customer Operations - Incident Response & Customer Advisory Templates (v1.0)`

### 3.2 The 4-Part Role-Based Prompt Template (`R-C-T-V` Pattern)

When publishing reusable prompts into the Enterprise Prompt Library (`KNA-01`), structure every prompt using **Role, Context, Task, and Verification (`R-C-T-V`)**:

1. **Role**: *"Act as a senior `<Operations Reliability Engineer / Financial Planning Analyst / Commercial Proposals Manager>`..."*
2. **Context & Source Constraint**: *"Using ONLY the attached `<Workspace Name / uploaded files>`, analyze `<specific topic>`. Do not extrapolate beyond the provided sources; if a specification is missing, state 'Not found in provided SOPs'."*
3. **Task & Output Format**: *"Produce a structured table containing `<Column A, Column B, Column C>` followed by a 3-bullet executive summary in plain business English."*
4. **Verification & Citation Mandate**: *"Include a clickable inline citation (`[Source Name, Section/Page]`) after every numerical specification, policy rule, or contractual obligation."*

## 4. Shared AI Knowledge Asset Catalog Template (`KNA-01` to `KNA-03` Baseline)

| Catalog ID | Asset Type (`Workspace / Prompt Pack / Golden Eval`) | Standardized Asset Title | Owning BU / Function | Data Tier (`D1`-`D4`) | Authorized Security Group | Primary Lead Curator & Backup | Golden Eval Score (`>= 85%`) | Last Verified | Next 90-Day Review |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| `CAT-001` | **Departmental Knowledge Workspace + Golden Eval** | `[<ORG>-OPS] Engineering - Equipment, Platform & Preventive Maintenance SOPs (v1.0)` | Operations & Engineering (`UC-001`) | `D3` | `SG-AI-Engineering-Ops` | Lead: `<Eng Champion #1>` Backup: `<Eng Champion #2>` | `Target >= 90%` (`25-50 Q&A`) | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-002` | **Departmental Knowledge Workspace + Golden Eval** | `[<ORG>-GLOBAL] HR & IT - Employee Onboarding, Leave, Travel & Service Desk Policies (v1.0)` | Human Resources & IT (`UC-001 / UC-005`) | `D2 / D3` | `SG-AI-Enterprise-Users (All Licensed Users)` | Lead: `<HR Champion>` Backup: `<ITSM Champion>` | `Target >= 90%` (`25-50 Q&A`) | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-003` | **Departmental Knowledge Workspace** | `[<ORG>-GLOBAL] HSSE & Compliance - Workplace Safety, Incident Reporting & Continuity SOPs (v1.0)` | Health, Safety, Security & Compliance | `D2 / D3` | `SG-AI-Enterprise-Users` | Lead: `<HSSE Champion>` Backup: `<Compliance Lead>` | `Target >= 90%` (`25-50 Q&A`) | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-004` | **Prompt Library + Golden Eval** | `[<ORG>-GLOBAL] Finance - Monthly Multi-Entity Variance Commentary & Executive Summary Prompt Pack (v1.0)` | Finance / FP&A (`UC-004`) | `D3 / D4` | `SG-AI-Finance-Controllers` | Lead: `<Finance Champion>` Backup: `<FP&A Lead>` | `100-Sample Financial Eval Set` | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-005` | **Prompt Library + Deep Research Guide** | `[<ORG>-GLOBAL] Strategy & ESG - Market Intelligence, Competitor & Sustainability Research Prompts (v1.0)` | Strategy, Commercial & Sustainability (`UC-003`) | `D1 / D2` | `SG-AI-Strategy-Commercial` | Lead: `<Strategy Champion>` Backup: `<ESG Lead>` | `Verified in Pilot` | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-006` | **Departmental Knowledge Workspace + Agent Template** | `[<ORG>-CS] Customer Operations - Service Disruption & Customer Advisory Playbook (v1.0)` | Customer Operations & Support (`UC-009`) | `D3` | `SG-AI-Customer-Ops` | Lead: `<Ops Champion>` Backup: `<Support Lead>` | `Target >= 85%` | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-007` | **Departmental Knowledge Workspace + Prompt Pack** | `[<ORG>-GLOBAL] Procurement - Multi-Vendor RFP Technical & Commercial Comparison Kit (v1.0)` | Corporate Procurement (`UC-008`) | `D3` | `SG-AI-Procurement` | Lead: `<Procurement Champion>` Backup: `<Category Manager>` | `Target >= 85%` | `<Verified>` | `Quarterly (90-Day)` |
| `CAT-008` | **Restricted Enclave Workspace** | `[<ORG>-LEGAL-<ENTITY>] Commercial Contract Obligation & Renewal Clause Reference Enclave (v1.0)` | Legal & Compliance (`UC-007`) | `D4 Restricted` | Entity-Specific Legal Security Group (`Strict Isolation`) | Lead: `<Legal Counsel>` Backup: `<Legal Ops Lead>` | `Target >= 90%` (`0%` Cross-Entity Leakage) | `<Verified>` | `Quarterly (90-Day)` |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Data & Knowledge Perspective (Access & Reuse Principle, grounding corpus freshness, prompt library management, and evaluation dataset catalog).
- [References](../References.md): Maintained catalog of regulatory, security, and operational references.
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/): Controls for `LLM04` (Data and Model Poisoning) and `LLM08` (Vector and Embedding Weaknesses).
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Data quality, provenance, and lifecycle governance guidance.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Documented information control and ongoing review cadences.
