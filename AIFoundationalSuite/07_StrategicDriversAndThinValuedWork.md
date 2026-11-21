<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# 07 Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment

| Document Metadata | Details |
| :---- | :---- |
| **Document ID** | `AIAF-DOC-07` (Strategic Drivers, Capability Inventory & Thin-vs.-Valued Work Assessment) |
| **Document Version** | `v1.0 (Reusable Baseline)` |
| **Target Audience** | AI Center of Excellence (CoE), Executive Sponsors, Business Unit Leaders, Enterprise IT Architecture, and HR / Change Management Leads |
| **Primary Internal Owner** | AI Center of Excellence (CoE) Lead & Strategy / Digital Transformation Lead |
| **Document Status** | Reusable Reference Template & Implementation Baseline (Industry- and Organization-Agnostic) |

**Note: Reference Template & Non-Prescriptive Accelerator Notice:** This document is provided as an illustrative template and optional starting baseline to help an organization's AI Center of Excellence (CoE) and internal teams build and scale their own AI governance and operational capabilities. It is **not** prescriptive. Sections have been pre-populated with representative enterprise patterns across corporate functions and core operations so your teams do not have to start from a blank page, and so internal teams can adapt, consolidate, or replace any section to fit their governance model.

## 1. How the AI CoE Can Create, Customize & Run an Internal Workshop for This Document

### 1.1 Purpose & Why This Document Exists

Organizations frequently begin artificial intelligence initiatives with a "tool-first" mindset, debating model features or building isolated proofs of concept before defining which business outcomes matter or which operational workflows contain the highest friction. This document is the business discovery anchor in the [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md) governance suite.

It exists to establish three executive guardrails before scaling licenses or custom agents:

1. **Strategic Anchor**: Connects every AI investment directly to boardroom priorities and codifies non-negotiable regulatory, sovereignty, and architectural constraints.
2. **Capability-Centric Mapping**: Inventories what the organization actually does as durable *business capabilities* (nouns and gerunds such as *Core operational planning* or *Multi-entity financial consolidation*), rather than temporary org-chart departments or software vendor names.
3. **Thin Work vs. Valued Work Decomposition**: Separates repetitive, rules-bound information compilation (**Thin Work**, targeted for Stage 1 Task Automation) from high-judgment human expertise (**Valued Work**, targeted for Stage 2 Human Augmentation), ensuring saved hours are systematically reinvested into higher-value outcomes.

### 1.2 Who Normally Produces & Signs Off on This Document Internally

- **Internal Lead / Facilitator**: AI Center of Excellence (CoE) Lead and Strategy / Digital Transformation Lead.
- **Required Internal Contributors**:
  - **Executive Sponsor / Operations & Technology Leadership**: Confirms the top strategic drivers and hard constraints.
  - **Business Unit & Functional Leads (Core Operations, Customer Operations, Finance, Legal, HR, Procurement)**: Validate the core business capabilities and estimate the current balance of Thin Work versus Valued Work.
  - **Human Resources / Learning & Development (L&D) Lead**: Validates role transition paths and manager enablement requirements.
- **Accountable Sign-Off**: Executive Sponsor and Head of Enterprise IT before locking the prioritized use-case backlog.

### 1.3 Recommended Approach: Running a CoE-Led Internal Alignment Session

The most effective way for the AI CoE to produce or ratify this document is to run a focused internal alignment session with the roles above, using the pre-populated tables in **Sections 2 through 4** below as a read-ahead strawman rather than starting from a blank page:

1. **Pre-Work (Sent Ahead of the Session)**: Share Sections 2, 3, and 4 with participating Business Unit Leads and ask each lead to identify core capabilities where teams spend excessive hours on repetitive compilation or manual search (**Thin Work**).
2. **Segment 1 - Strategic Drivers & Hard Constraints**: Walk through the 14 canonical drivers in **Table 2.2** (`DRV-01` to `DRV-14`) and the hard constraints in **Table 2.3** (`CON-01` to `CON-06`) with the Executive Sponsor and Head of Enterprise IT. Adjust the `1` to `5` urgency scores and lock the **Top 3 Strategic Drivers** for the upcoming rollout.
3. **Segment 2 - Business Capability Inventory & Concentration Risk**: Review the 10 baseline capabilities in **Table 3.1** (`CAP-01` to `CAP-10`) with Business Unit Leads. Add or refine capabilities specific to regional business units or product lines, and verify the **Concentration Risk** column (identifying where critical processes depend on a single key person or a single rigid software vendor).
4. **Segment 3 - Thin vs. Valued Work & Manager Transition Plan**: Adjust the `Thin Work Share` vs. `Valued Work Share` estimates in **Table 4.1**, confirm placement in the **2x2 Disruption Priority Matrix (`Section 4.2`)**, and align with HR / L&D on the **Manager Readiness Actions (`Table 4.3`)** so time saved from Thin Work is actively redirected toward Valued Work.

## 2. Business Context, Strategic Drivers & Hard Constraints (Template Baseline)

> **Companion Strategy Charter:** For the board-level Enterprise AI Vision Statement, 8 Guiding Decision Principles (`STR-01` to `STR-08`), and external Public AI Trust Statement derived from these drivers, see [AIAF-DOC-01: Enterprise AI Strategy Charter & Public AI Trust Statement](01_EnterpriseAIStrategyCharter.md). For ongoing monthly ROI telemetry (`VAL-01` to `VAL-04`) and 60-day license governance, see [AIAF-DOC-09: AI Value Realization, FinOps & 60-Day License Governance SOP](09_ValueRealizationAndSeatGovernanceSOP.md).

### 2.1 Organization Profile & Value Proposition Baseline

| Profile Dimension | Enterprise Template Baseline (Customize per Organization) |
| :--- | :--- |
| **Organization Name & Ownership** | `[Organization Legal Name]` (`[Publicly Traded / Privately Held / Sovereign-Backed]`; headquartered in `[Primary Headquarters Location]`) |
| **Industry & Core Business Model** | `[Primary Industry Sector & Core Business Lines]`; `[B2B / B2C / B2G Operating Model]` |
| **Global Scale & Footprint** | `[Annual Revenue]`; `[Primary Operational Volume Metric]`; `[Total Employee Headcount]` across operating regions and locations |
| **Key Regulatory Regimes** | Sector-specific critical infrastructure and safety mandates, data privacy regulations (such as GDPR, CCPA, HIPAA, and ISO/IEC 27701), EU AI Act, and financial/operational compliance across operating jurisdictions |
| **1. What problem do you solve for customers?** | `[Describe the core customer problem solved. For example: Delivering reliable, high-velocity products and end-to-end services across global markets while minimizing cycle time, risk, and operational disruption.]` |
| **2. What differentiates your solution?** | `[Describe core differentiators. For example: Proprietary operational platforms, domain-specific physical or digital infrastructure, integrated multi-region network reach, and deep institutional expertise.]` |
| **3. What would customers lose without the organization?** | `[Describe customer switching cost and value moat. For example: Customers would lose integrated multi-region execution, compliance assurance, and resilient service continuity.]` |

### 2.2 The 14 Canonical Strategic Drivers Scorecard (`1 = Low` to `5 = Critical`)

| Driver ID | Canonical Strategic Driver | Applies? | Urgency (1-5) | Illustrative Enterprise Strategic Context & Value Rationale |
| :--- | :--- | :---: | :---: | :--- |
| `DRV-01` | **Reduce operational costs** | Yes | **5** | Offloading repetitive manual information compilation across knowledge workers delivers measurable annual productivity capacity. |
| `DRV-02` | **Improve product / service quality** | Yes | **4** | Improving accuracy, consistency, and citation traceability across technical SOPs, regulatory filings, and customer communications. |
| `DRV-03` | **Accelerate time to market** | Yes | **4** | Compressing turnaround time for new product launches, commercial tenders, and customer onboarding workflows. |
| `DRV-04` | **Scale without proportional headcount growth** | Yes | **5** | Scaling transaction and service volume across global business units without linear growth in corporate or administrative overhead. |
| `DRV-05` | **Respond to competitive pressure** | Yes | **4** | Embedding artificial intelligence and automation into core workflows to maintain cost, speed, and service leadership against industry peers. |
| `DRV-06` | **Comply with new regulations** | Yes | **5** | Enforcing critical infrastructure security, multi-jurisdiction data privacy laws, AI governance standards, and ESG sustainability disclosures. |
| `DRV-07` | **Attract or retain talent** | Yes | **4** | Equipping corporate and regional staff with modern AI assistants to eliminate repetitive administrative drudgery and focus on high-impact work. |
| `DRV-08` | **Enter new markets** | Yes | **3** | Supporting geographic and product line expansion with scalable localization, regulatory research, and commercial readiness. |
| `DRV-09` | **Improve customer experience** | Yes | **4** | Enhancing customer visibility, proactive exception advisories, and faster commercial and support response times. |
| `DRV-10` | **Reduce key-person dependency / knowledge risk** | Yes | **5** | Capturing decades of specialized engineering, operations, and legal/commercial expertise into governed, searchable knowledge bases. |
| `DRV-11` | **Deliver value from proprietary data assets** | Yes | **5** | Activating high-value operational, financial, and contract repositories across enterprise document stores, ERPs, and data lakehouses without data duplication. |
| `DRV-12` | **Increase speed of executive decision-making** | Yes | **5** | Compressing multi-entity financial variance analysis, market intelligence, and competitor benchmarking from days to hours. |
| `DRV-13` | **Reduce software vendor dependency by building with AI** | Yes | **4** | Using horizontal **Enterprise AI Platform**, **No-Code Agent Builder**, and **Code-First Custom Agents** across existing systems instead of paying per-silo SaaS AI add-on markups. |
| `DRV-14` | **Protect core services from customer self-build** | No | **2** | Core physical/regulated assets maintain high structural moats, while digital service interfaces require continuous AI innovation. |

- **Illustrative Top 3 Strategic Drivers for an Enterprise AI Program**:
  1. **`DRV-01 / DRV-04` - Scale Operations & Knowledge Productivity Without Linear Overhead Growth**
  2. **`DRV-11 / DRV-12` - Activate Multi-Entity Proprietary Knowledge & Accelerate Executive Decision-Making**
  3. **`DRV-06 / DRV-10` - Enforce Multi-Jurisdiction Governance, Security & Institutional Knowledge Continuity**

### 2.3 Hard Constraints & Non-Negotiables

| Constraint ID | Constraint Category | Illustrative Enterprise Boundary / Mandate |
| :--- | :--- | :--- |
| `CON-01` | **Critical Infrastructure & OT Air-Gap Boundary** | Live operational technology (OT), safety-critical control systems, and regulated national secrets (`D5 Regulated / Critical Infrastructure`) must remain strictly isolated from external or corporate cloud LLM prompts. |
| `CON-02` | **Multi-Entity & Customer Confidentiality** | Customer contracts, pricing schedules, and subsidiary financial statements (`D4 Restricted`) must never leak across business units or unauthorized roles; source ACL inheritance is mandatory. |
| `CON-03` | **Multi-Cloud "Zero Data Movement" Mandate** | Grounding must query enterprise document repositories, collaboration suites, and analytical lakehouses in place or via governed connectors without forced platform migration. |
| `CON-04` | **Directory & External Guest Isolation** | External B2B partner, contractor, or vendor guest accounts in the corporate identity provider must be strictly filtered out (`userType EQUALS 'Member'`) so they never sync or consume enterprise AI licenses without explicit authorization. |
| `CON-05` | **Regional Data Residency** | Regulated regional subsidiaries require alignment with approved regional or multi-region cloud boundaries (such as `us`, `eu`, or `global`) to satisfy applicable data residency obligations. |
| `CON-06` | **Human-in-the-Loop (HITL) Financial & Legal Gate** | No AI agent is permitted to autonomously post journal entries in the ERP, execute binding procurement commitments, or sign off on legal obligations without a named human approver. |

## 3. Business Capability Inventory & Classification (Template Baseline)

**Note: Capability Naming Rule**: Capabilities describe *what* the business does (e.g., *Enterprise document retrieval & SOP synthesis*), never an org-chart department (*"IT Department"*) or a software tool (*"Document Repository Software"*).

| Cap ID | Business Capability Name | Owning Function / BU | Strategic Importance (`Core / Strategic / Supporting / Commodity`) | Current Execution Quality (`Leading / Competitive / Lagging / Absent`) | Key System Dependencies | Concentration Risk (Key-Person or Single-Vendor Bottleneck) |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `CAP-01` | **Enterprise Document Retrieval & Technical SOP Synthesis** | All BUs / Enterprise IT & Operations | **Supporting** | **Lagging** (Siloed across regional document sites) | `<Enterprise Collaboration & Document Suite>`, PDF Manuals | **High Key-Person Risk**: Senior engineers and specialists hold unwritten troubleshooting knowledge. |
| `CAP-02` | **Multi-ERP Financial Consolidation & Variance Analysis** | Corporate Finance / CFO Office | **Strategic** | **Lagging** (Manual spreadsheet reconciliation across entities) | `<Enterprise ERP Platform>`, Spreadsheets, Data Lakehouse | **High Key-Person Risk**: Month-end close depends on manual analyst spreadsheet macros. |
| `CAP-03` | **Enterprise Contract & Legal Obligation Management** | Legal & Commercial Operations | **Strategic** | **Competitive** (High legal rigor, manual contract review) | Contract Lifecycle Management (CLM), Legal Document Vaults | **High Key-Person Risk**: Complex long-term agreements require specialist counsel review. |
| `CAP-04` | **Market, Competitor & ESG Sustainability Research** | Strategy, Commercial & Sustainability | **Strategic** | **Competitive** (manual analyst synthesis) | Industry Reports, Market Databases, Public Web | **Medium Bottleneck**: Manual compilation limits frequency of executive scenario briefings. |
| `CAP-05` | **Internal IT & HR Employee Service Desk Triage** | Enterprise IT & HR | **Commodity** | **Competitive** (ITSM platform + manual Tier-1 triage) | `<ITSM Platform>`, HRIS & IT Policy Portals | **Medium Operational Load**: High volume of repetitive policy, access, and benefits queries. |
| `CAP-06` | **Conversational Enterprise Operational & Commercial Analytics** | Enterprise Data, BI & Commercial Teams | **Strategic** | **Lagging** (Queued behind BI & SQL specialists) | `<Enterprise Data Warehouse / Cloud Data Lakehouse>`, BI Tools | **High Bottleneck**: Business leaders wait days for ad-hoc cross-functional SQL queries. |
| `CAP-07` | **Operational Disruption Monitoring & Customer Advisory** | Customer Operations & Service Delivery | **Core** | **Leading** (Real-time event monitoring + manual advisory drafting) | Operational Risk Monitors, CRM, Customer Portals | **Low-Medium Risk**: Opportunity to accelerate tailored customer impact advisories. |
| `CAP-08` | **Core Real-Time Operational Control & Predictive Optimization** | Core Operations & Engineering | **Core** | **Leading** (Dedicated deterministic control & domain ML models) | Core Operational Control Systems, Digital Twins, Telemetry | **Protected Core Moat**: Keep deterministic/OT MLOps separate; use GenAI only for maintenance/safety SOPs. |
| `CAP-09` | **Global Procurement & Multi-Vendor RFP Evaluation** | Procurement & Supply Chain | **Supporting** | **Competitive** (Manual multi-vendor bid comparison) | `<Enterprise Procurement Portal>`, Tender Repositories | **Medium Bottleneck**: Slow side-by-side technical and commercial bid scoring. |
| `CAP-10` | **Enterprise GenAIOps, Golden Evaluation & AI Governance** | Enterprise IT & AI CoE | **Strategic** | **Absent / Nascent** (Transitioning from initial pilot) | Enterprise AI Platform Admin, Lakehouse Telemetry, Automated AI Evaluation Pipeline | **Critical Scaling Dependency**: Required to govern enterprise-wide seats and custom agents safely. |

## 4. Thin vs. Valued Work Split, 2x2 Disruption Matrix & Workforce Transition

### 4.1 Thin Work vs. Valued Work & 5-Type AI Disruption Scoring Table

- **Thin Work:** Repetitive, rules-bound compilation tasks (searching across document folders, reformatting status updates, extracting table rows from PDFs, answering Tier-1 FAQ tickets). **Target: Stage 1 Task Automation.**
- **Valued Work:** High-judgment, strategic, creative, or relationship-driven human work (negotiating commercial agreements, resolving complex operational exceptions, signing off on audited financial statements, leading operational safety). **Target: Stage 2 Human Augmentation (HITL).**

| Cap ID | Business Capability Name | Thin Work Share | Valued Work Share | Primary AI Disruption Type (`Automate / Augment / Accelerate / Displace / Create`) | Likelihood (1-5) | Business Impact (1-5) | 2x2 Matrix Quadrant | Target Progression Stage & Value Case Pattern |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| `CAP-01` | **Enterprise Document Retrieval & SOP Synthesis** | **High** | Low-Moderate | **Accelerate & Automate** | 5 | 5 | **EXPLOIT / PRIORITIZE** | **Stage 1 -> Stage 2**: Enterprise Grounded Search & Grounded Knowledge Notebooks across knowledge workers |
| `CAP-02` | **Multi-ERP Financial Consolidation & Variance** | **High** | Moderate | **Augment & Automate** | 4 | 5 | **PRIORITIZE** | **Stage 2 (Strict HITL)**: Code-First Financial Consolidation Agent + ERP/Lakehouse exports |
| `CAP-03` | **Enterprise Contract & Legal Obligation Review** | **Moderate-High** | Moderate-High | **Augment** | 4 | 5 | **PRIORITIZE** | **Stage 2 (Strict HITL)**: Scoped Legal Knowledge Workspace / No-Code Agent Builder with mandatory counsel sign-off |
| `CAP-04` | **Market, Competitor & ESG Research** | **High** | Moderate | **Accelerate & Augment** | 5 | 4 | **EXPLOIT** | **Stage 1/2**: Enterprise Deep Research for managers, strategists, and analysts |
| `CAP-05` | **Internal IT & HR Employee Service Desk Triage** | **High** | Low-Moderate | **Automate & Displace** | 5 | 4 | **EXPLOIT** | **Stage 2**: No-Code Agent Builder IT/HR Helpdesk Agents for Tier-1 ticket deflection |
| `CAP-06` | **Conversational Enterprise Data Analytics** | **Moderate** | Moderate | **Create & Accelerate** | 4 | 5 | **PRIORITIZE** | **Stage 2**: Read-only Data Warehouse MCP / Code-First Analytics Agent |
| `CAP-07` | **Operational Disruption & Customer Advisory** | Low-Moderate | **High** | **Augment & Create** | 4 | 4 | **PRIORITIZE** | **Stage 2**: Augment account and operations advisors with multi-source customer impact synthesis |
| `CAP-08` | **Core Real-Time Operational Control Systems** | Low | **High** | **Augment** (SOPs only) | 3 | 5 | **MONITOR** | **Stage 1/2**: Preserve deterministic/OT ML; ground engineering maintenance manuals in Knowledge Notebooks |
| `CAP-09` | **Global Procurement & Vendor RFP Evaluation** | **High** | Moderate | **Accelerate & Augment** | 4 | 3 | **EXPLOIT** | **Stage 2**: L200 Champion No-Code Agent Builder RFP comparison workflow |
| `CAP-10` | **Enterprise GenAIOps & AI Governance (CoE)** | Low-Moderate | **High** | **Create** | 5 | 5 | **PRIORITIZE** | **Foundation**: Establish 3-Tier CoE, Golden Datasets, and P2P Gate governance |

### 4.2 The 2x2 AI Disruption Priority Matrix

```
+-----------------------------------------------------------------------+
|             ENTERPRISE 2x2 AI DISRUPTION PRIORITY MATRIX              |
+-----------------------------------------------------------------------+
| HIGH IMPACT | MONITOR (Selective GenAI)   | PRIORITIZE (Strategic)    |
| (Score 4-5) | * CAP-08: Core Real-Time    | * CAP-02: Multi-ERP       |
|             |   Operational Control & OT  |   Finance Consolidation   |
|             |   (Preserve deterministic   | * CAP-03: Enterprise      |
|             |   ML; use GenAI strictly    |   Contract & Legal Review |
|             |   for maintenance & safety  | * CAP-06: Conversational  |
|             |   SOP search)               |   Enterprise Analytics    |
|             |                             | * CAP-10: Enterprise      |
|             |                             |   GenAIOps & CoE Gov      |
+-------------+-----------------------------+---------------------------+
| MODERATE    | WATCH (Review Annually)     | EXPLOIT (Fast Wave 1 Wins)|
| IMPACT      | * Long-cycle physical       | * CAP-01: Enterprise Doc  |
| (Score 1-3) |   capital infrastructure &  |   & SOP Synthesis         |
|             |   civil engineering cycles  | * CAP-04: Deep Research   |
|             |                             |   Market & ESG Analysis   |
|             |                             | * CAP-05: IT & HR Service |
|             |                             |   Desk Triage             |
|             |                             | * CAP-09: Procurement RFP |
+-------------+-----------------------------+---------------------------+
                  LOWER LIKELIHOOD (1-3)        HIGHER LIKELIHOOD (4-5)
                   OF GENAI DISRUPTION            OF GENAI DISRUPTION
```

### 4.3 Workforce Impact & People Leader Transition Plan

| Capability Group | Affected Roles & Cohort Pattern | Nature of Impact (`Changed / Expanded`) | Target Time Reallocated (`Thin -> Valued`) | Transition Path & Enablement Track | Manager Readiness Action Required |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`CAP-01`, `CAP-05` - Corporate & Operational Knowledge Workers** | **All Licensed Enterprise Knowledge Workers** across phased rollout cohorts | **Changed**: Less manual searching, drafting, and formatting; more exception resolution. | **Routine search & drafting** shifted from Thin Work to Valued Work | **Track 3 (L100 Mass Enablement)**: Day-1 Onboarding, workspace connectors, and safe prompting. | Department Heads nominate active users and review 60-day seat utilization. |
| **`CAP-04`, `CAP-09` - Business Champions, Analysts & Functional Leads** | **Early-Access Power Users / CoE Champions** + **Departmental Champions** | **Expanded**: Become departmental Knowledge Workspace curators and no-code workflow builders. | **Manual compilation** shifted to cross-source analysis & process redesign | **Track 1 (L200 Champion Enablement)**: Enterprise Deep Research, Grounded Knowledge Workspace curation, and No-Code Agent Builder. | Managers shift from reviewing manual drafts to auditing source citations and Golden Dataset accuracy. |
| **`CAP-02`, `CAP-06`, `CAP-10` - AI Engineers, Data Architects & IT Leads** | **Technical Builders** in Enterprise IT, Digital Transformation & Data Teams | **Expanded**: Transition from ad-hoc ticket support to building governed Custom/MCP agents and GenAIOps pipelines. | **Ad-hoc report pulls** shifted to governed custom agent development | **Track 1 Advanced (L300 Technical Track)**: Code-First Agent SDK, Gateway 2 governance, and Automated AI Evaluation Pipeline. | IT & CoE leadership enforce the 2-Gateway approval model and 10-Dimension P2P Gate. |

## References & Standards

- [AI Adoption Framework (AIAF)](../AIAdoptionFramework.md): Business Value Perspective, People & Workforce Perspective (thin work vs. valued work classification, manager transition), and Use Case Maturity Progression.
- [Business Readiness Assessment Workshop](../Workshops/BusinessReadinessAssessment.md): Modules 1, 2, and 6 for capability inventory, strategic drivers, and AI disruption analysis.
- [References](../References.md): Maintained catalog of adoption, operational, and governance references.
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Organizational risk framing and human accountability principles.
- [ISO/IEC 42001: AI Management System](https://www.iso.org/standard/42001): Alignment of AI objectives with organizational strategy and workforce competence.
