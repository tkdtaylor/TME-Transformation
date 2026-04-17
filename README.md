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
- **Technology CoE operating model evolution** from gatekeeper through advisor, platform, and federated stages
- **RACI template** for ten core roles across adoption phases
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
- **AI CoE operating model evolution** from gatekeeper through advisor, platform, and federated stages as maturity increases
- **RACI template** for 14 core roles including Chief Data Officer, Data Steward, and Knowledge / Prompt Librarian
- **20+ KPIs** spanning business value, adoption, quality, operational, and data & knowledge outcomes

**Starting point:** The [Business Readiness Assessment](Workshops/BusinessReadinessAssessment.md) is a facilitated workshop that feeds into and speeds up Phase 1 of both frameworks. It produces a capability inventory, a Wardley Map, an AI disruption analysis, and a scored maturity baseline, giving teams the concrete starting point the frameworks require before moving into planning and pilots.

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
