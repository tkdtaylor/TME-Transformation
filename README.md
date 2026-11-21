# TME Transformation Frameworks

A library of vendor-agnostic adoption frameworks for technology and AI transformation initiatives. These documents are distilled from leading cloud and AI guidance (AWS CAF, Google Cloud AF, Microsoft Azure CAF) augmented and adapted with my personal experience for practical organizational use.

---

## Frameworks

### [Technology Adoption Framework (TAF)](TechAdoptionFramework.md)

A comprehensive guide for technology transformations (cloud adoption, platform modernization, and data initiatives). It organizes work across **six perspectives** (Business, People & Culture, Governance & Risk, Platform & Technology, Security & Compliance, Operations & Management) and a **six-phase lifecycle** from initial assessment through continuous innovation.

Key elements:
- **Maturity model** with four levels: Tactical → Defined → Managed → Optimizing
- **Workload classification** across five tiers (Mission Critical through Legacy/Candidate) with corresponding migration strategies using the 7 Rs
- **Governance layers** covering enterprise policy, platform controls, workload controls, and FinOps
- **Zero Trust security** model and shared responsibility matrix (IaaS / PaaS / SaaS)
- **Technology CoE operating model evolution** from gatekeeper through advisor to platform / self-service stages
- **Core role definitions and a sample RACI template** across adoption phases
- **Success metrics** across business, operational, security, and people outcome categories

TAF is the base framework. The AI Adoption Framework below inherits its structure and extends it for AI-specific challenges.

---

### [AI Adoption Framework (AIAF)](AIAdoptionFramework.md)

A specialization of TAF for AI initiatives: LLMs, AI assistants, AI coding tools, autonomous agents, and AI-embedded products. It inherits TAF's six-phase lifecycle and four-level maturity model but expands to **seven perspectives** by elevating Data & Knowledge to first-class status, and adapts every element for AI-specific governance, responsible use, and operational quality.

Key elements:
- **Eight guiding principles** including governing shadow AI rather than prohibiting it, human accountability for consequential outputs, and continuous evaluation
- **AI-specific perspective content**: prompt management, RAG infrastructure, grounding vs training data governance, AI Impact Assessments, prompt injection defense, agentic action boundaries, token cost management
- **AI maturity model**: Exploring → Piloting → Scaling → Transforming, assessed independently per perspective
- **Pilot-to-Production Gate**: explicit criteria use cases must clear before leaving pilot, to prevent indefinite pilot sprawl
- **Use case classification** across five capability types (Augmentation, Analysis, Generation, Automation, Agency) and four risk tiers
- **Responsible AI model** covering Fairness, Reliability, Privacy, Transparency, Accountability, and Inclusiveness with an AI Impact Assessment (AIIA) process
- **AI Shared Responsibility Model** across model provider, platform layer, and application consumer
- **Non-human actor personas** (interactive assistants, scoped agents, service agents, multi-agent systems, tool-using agents) with identity, audit, and accountability patterns for agentic AI
- **AI CoE operating model evolution** from gatekeeper through advisor to platform / self-service stages as maturity increases
- **Core AI role definitions and a sample RACI template** including Chief Data Officer, Data Steward, and Knowledge / Prompt Librarian
- **20+ KPIs** spanning business value, adoption, quality, operational, and data & knowledge outcomes

**Starting point for AI adoption:** The [Business Readiness Assessment](Workshops/BusinessReadinessAssessment.md) is a facilitated workshop grounded in the AIAF. It feeds into and speeds up AIAF Phase 1 by producing a capability inventory, a Wardley Map, an AI disruption analysis, an initial AI Decision Register, and a scored AI maturity baseline. It uses TAF concepts where they help explain the underlying business and technology landscape, but a dedicated TAF workshop should be run separately for broader non-AI transformation programs.

---

## AI Foundational Suite

The [AI Foundational Suite](AIFoundationalSuite) contains a 15-document (`00` through `14`), vendor-neutral governance and operations starter kit for an organization's AI Center of Excellence (CoE). While [Templates](Templates) provides blank per-use-case forms and CSV register schemas, this suite provides pre-populated program-level baselines ordered chronologically across four execution tiers so internal teams do not start from a blank page:

| Tier | Documents | Focus |
|---|---|---|
| **Master Guide** | [00_CoEProductionGuide.md](AIFoundationalSuite/00_CoEProductionGuide.md) | Priority sequencing (`01` to `14`), internal ownership, and CoE facilitation patterns |
| **Tier 1: Day-0 Guardrails** | `01` to `04` ([Strategy Charter](AIFoundationalSuite/01_EnterpriseAIStrategyCharter.md), [Enterprise AI Policy](AIFoundationalSuite/02_EnterpriseAIPolicyAndDataClassification.md), [Data Matrix & Source Register](AIFoundationalSuite/03_DataClassificationMatrixAndSourceRegister.md), [Employee Traffic-Light AUP](AIFoundationalSuite/04_EmployeeAcceptableUseGuide.md)) | Executive trade-off rules, `D1`-`D5` data boundaries, Non-Human Actor standards, and Day-1 workforce guidance |
| **Tier 2: Wave-1 Enablement & Safety** | `05` to `08` ([Knowledge & Prompt Playbook](AIFoundationalSuite/05_KnowledgeNotebookAndPromptPlaybook.md), [Incident & Kill-Switch Runbook](AIFoundationalSuite/06_AISecurityIncidentAndKillSwitchRunbook.md), [Drivers & Thin-vs.-Valued Work](AIFoundationalSuite/07_StrategicDriversAndThinValuedWork.md), [Intake & Scored Backlog](AIFoundationalSuite/08_AIUseCaseIntakeAndPortfolioBacklog.md)) | Curated departmental workspaces, `<15-minute` 5-layer kill switches, work decomposition, and portfolio scoring |
| **Tier 3: Seat FinOps & Maturity** | `09` to `10` ([Value & 60-Day Seat SOP](AIFoundationalSuite/09_ValueRealizationAndSeatGovernanceSOP.md), [Maturity Scorecard & Roadmap](AIFoundationalSuite/10_AIMaturityScorecardAndReadinessRoadmap.md)) | Verified ROI formulas, 30/45/60-day inactive license reclamation, and 7-perspective readiness scoring |
| **Tier 4: Custom Agents & GenAIOps** | `11` to `14` ([P2P Gate Package](AIFoundationalSuite/11_PilotToProductionGatePackage.md), [AIIA & OWASP Controls](AIFoundationalSuite/12_AIImpactAssessmentAndOWASPControls.md), [Governance Registers & GenAIOps](AIFoundationalSuite/13_OperationalGovernanceRegistersAndGenAIOps.md), [Vendor AI Procurement Checklist](AIFoundationalSuite/14_VendorAIProcurementChecklist.md)) | 10-dimension production gates, measurable RAI and OWASP `LLM01`-`LLM10` controls, Golden Dataset evaluation, and SaaS AI TPRM |

---

## Templates

The [Templates](Templates) folder contains vendor-neutral source templates intended to be converted into your preferred working format: documents, spreadsheets, forms, tickets, GRC records, or workflow tools. Markdown is used for judgment artifacts; CSV is used for operational registers.

| Template | Use For |
|---|---|
| [AIImpactAssessment.md](Templates/AIImpactAssessment.md) | Tier 2+ AI Impact Assessments, risk review, mitigation evidence, and approval history |
| [AIUseCaseCard.md](Templates/AIUseCaseCard.md) | Use case intake, prioritization, value framing, and pilot selection |
| [PilotToProductionGate.md](Templates/PilotToProductionGate.md) | Production readiness review before a successful pilot moves to rollout |
| [AIDecisionRegister.csv](Templates/AIDecisionRegister.csv) | Living register of where AI influences decisions, owners, guardrails, and review cadence |
| [AIUseCaseBacklog.csv](Templates/AIUseCaseBacklog.csv) | Scored and sortable portfolio backlog of candidate AI use cases |
| [ApprovedAIToolRegistry.csv](Templates/ApprovedAIToolRegistry.csv) | Approved, conditional, and prohibited AI tools with data handling and review metadata |
| [DataDictionary.md](Templates/DataDictionary.md) | Column definitions and recommended values for CSV registers |

---

## Worked Example

The [Internal Employee Lifecycle Assistant](Examples/InternalEmployeeLifecycleAssistant) example shows how to apply the AIAF to a common internal use case covering onboarding, role changes, and offboarding. It demonstrates a Tier 2, internal-only pattern that starts with Human Augmentation and narrow Task Automation rather than customer-facing or agentic autonomy.

---

## Supporting Docs

| Document | Use For |
|---|---|
| [References.md](References.md) | External source links, review cadences, and maintenance notes |
| [CHANGELOG.md](CHANGELOG.md) | Project change history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Scope, vendor-neutrality rules, formatting conventions, and licensing |
| [FacilitatorGuide.md](Workshops/FacilitatorGuide.md) | Running the AIAF-grounded Business Readiness Assessment workshop |

---

## How the Frameworks Relate

```
TAF  ────────────────────────────────────────────────────────────
     6 perspectives: Business · People · Governance · Platform · Security · Ops
     6 phases: Assess → Plan → Implement → Govern → Optimize → Modernize

AIAF ────────────────────────────────────────────────────────────
     7 perspectives: adds Data & Knowledge as a peer dimension
     Same 6 phases + Pilot-to-Production Gate
     Shadow AI · Responsible AI · Prompt security · Agent personas · CoE evolution
```

Both frameworks are designed to be used together. An organization running a cloud modernization program would use TAF as the primary guide, while a parallel or subsequent AI initiative would layer in AIAF across the same organizational perspectives.

---

## License & Disclaimer

Copyright (c) 2026 TME Transformation ([@tkdtaylor](https://github.com/tkdtaylor)). Released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) license.

*Disclaimer: This is an independent personal open-source project. The views, frameworks, and templates expressed here are my own and do not represent those of my current or past employers.*
