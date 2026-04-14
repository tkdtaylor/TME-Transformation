# Comprehensive Technology Adoption Framework (TAF)

> Synthesized from AWS Cloud Adoption Framework, Google Cloud Adoption Framework, and Microsoft Azure Cloud Adoption Framework. Not affiliated or endorsed in any way with any of the parent companies.

---

## Table of Contents

1. [Overview](#overview)
2. [Guiding Principles](#guiding-principles)
3. [Six Core Perspectives](#six-core-perspectives)
   - [Business Perspective](#1-business-perspective)
   - [People & Culture Perspective](#2-people--culture-perspective)
   - [Governance & Risk Perspective](#3-governance--risk-perspective)
   - [Platform & Technology Perspective](#4-platform--technology-perspective)
   - [Security & Compliance Perspective](#5-security--compliance-perspective)
   - [Operations & Management Perspective](#6-operations--management-perspective)
4. [Adoption Lifecycle Phases](#adoption-lifecycle-phases)
   - [Phase 1: Assess & Strategize](#phase-1----assess--strategize)
   - [Phase 2: Plan & Prepare](#phase-2----plan--prepare)
   - [Phase 3: Implement & Migrate](#phase-3----implement--migrate)
   - [Phase 4: Govern & Secure](#phase-4----govern--secure)
   - [Phase 5: Optimize & Manage](#phase-5----optimize--manage)
   - [Phase 6: Modernize & Innovate](#phase-6----modernize--innovate)
5. [Maturity Model](#maturity-model)
   - [Maturity by Perspective](#maturity-by-perspective)
   - [Technology Center of Excellence: Operating Model Evolution](#technology-center-of-excellence-operating-model-evolution)
6. [Workload Strategy](#workload-strategy)
7. [Governance & Security Model](#governance--security-model)
8. [Roles & Responsibilities](#roles--responsibilities)
9. [Success Metrics & KPIs](#success-metrics--kpis)
   - [Business Outcomes](#business-outcomes)
   - [Operational Outcomes](#operational-outcomes)
   - [Security Outcomes](#security-outcomes)
   - [People Outcomes](#people-outcomes)
10. [Quick Reference Summary](#quick-reference-summary)

---

## Overview

The **Technology Adoption Framework (TAF)** is a vendor-agnostic, structured approach for organizations planning, executing, and sustaining technology transformations (including cloud adoption, platform modernization, and AI/data initiatives).

It draws on the structural strengths of three industry-leading frameworks:

| Source Framework | Primary Contribution |
|---|---|
| **AWS CAF** | Six organizational perspectives covering 47 capabilities |
| **Google Cloud AF** | Phased adoption lifecycle with maturity measurement |
| **Microsoft Azure CAF** | End-to-end methodology from strategy through operations |

The TAF is organized around two complementary dimensions:
- **Horizontal axis**: Six core perspectives that span the organization (who is involved and what they own)
- **Vertical axis**: Six lifecycle phases (when work happens and in what order)

### Specializations

The TAF is designed to be extended for specific adoption contexts. The current specialization is:

- **[AI Adoption Framework (AIAF)](AIAdoptionFramework.md)** — expands the TAF with a seventh perspective (Data & Knowledge) and AI-specific governance, security, and operations concerns (Responsible AI, OWASP LLM Top 10, agent personas, GenAIOps, measurable RAI goals). Use the AIAF when the transformation involves LLMs, AI assistants, AI coding tools, AI-embedded products, or autonomous agents.

---

## Guiding Principles

These principles underpin every phase and perspective of the framework:

1. **Business outcomes first**: Every technology decision must trace back to a measurable business objective.
2. **People over tools**: Organizational readiness, culture, and skills determine adoption success more than technology selection.
3. **Iterative progress**: Adopt incrementally; avoid big-bang transformations. Deliver value early and often.
4. **Security by design**: Security and compliance are built in, not bolted on.
5. **Shared responsibility**: Technology teams, business units, and leadership each own distinct parts of adoption.
6. **Measure what matters**: Establish baselines before transformation and track outcomes, not just outputs.
7. **Continuous improvement**: Adoption is never "done." Optimize, modernize, and innovate as a steady-state practice.

---

## Six Core Perspectives

Each perspective represents a capability domain with distinct stakeholders, concerns, and deliverables. All six must be addressed in every phase.

---

### 1. Business Perspective

**Purpose:** Align technology investments to business strategy and ensure measurable return on investment.

**Key Stakeholders:** CEO, CFO, COO, Board, Business Unit Leaders, Product Owners

**Core Capabilities:**
- Business case development and financial modeling (TCO, ROI, NPV)
- Strategy alignment: connecting technology initiatives to corporate objectives
- Value realization tracking: measuring whether expected benefits are delivered
- Partner and vendor ecosystem management
- Digital product and service portfolio management

**Key Questions to Answer:**
- What business outcomes are we funding?
- What is the cost of inaction?
- How will we measure success in 6, 12, and 24 months?

---

### 2. People & Culture Perspective

**Purpose:** Build the organizational capacity, culture, and skills required to sustain continuous technology change.

**Key Stakeholders:** Head of HR, CIO, Transformation Officers, Team Leads, Learning & Development

**Core Capabilities:**
- Skills gap analysis and workforce planning
- Training curricula and certification pathways
- Change management and communication planning
- Organizational design: restructuring teams around products, platforms, or value streams
- Leadership development for technology-fluent management
- Culture building toward psychological safety, experimentation, and continuous learning

**Key Questions to Answer:**
- Do we have the skills we need? Where are the gaps?
- How will we prepare people for new ways of working?
- How do we sustain momentum through change fatigue?

---

### 3. Governance & Risk Perspective

**Purpose:** Establish controls, policies, and oversight mechanisms that maximize benefits while minimizing transformation risk.

**Key Stakeholders:** CIO, CFO, Chief Risk Officer, Chief Compliance Officer, Legal, Audit

**Core Capabilities:**
- Technology governance frameworks (policies, standards, guardrails)
- Portfolio and program management (prioritization, funding gates, stage reviews)
- Risk identification, assessment, and mitigation
- Regulatory and compliance mapping: e.g., GDPR, CCPA/CPRA and the US state privacy patchwork, HIPAA, SOC 2, ISO 27001, PCI DSS 4.0, DORA (EU financial services operational resilience), and sector-specific rules
- Vendor and third-party risk management
- FinOps policy and cost governance (budgets, tagging policies, chargeback models, spend approval thresholds). Execution and optimization live in the Operations & Management perspective
- Audit and accountability mechanisms

**Key Questions to Answer:**
- What guardrails prevent ungoverned sprawl or shadow IT?
- How do we manage compliance across multiple environments?
- Who approves technology spend, and against what criteria?

---

### 4. Platform & Technology Perspective

**Purpose:** Design, build, and maintain enterprise-grade technology platforms that are scalable, resilient, and fit for workload requirements.

**Key Stakeholders:** CTO, Enterprise Architects, Platform Engineers, Data Engineers, Site Reliability Engineers

**Core Capabilities:**
- Current-state architecture assessment (applications, data, infrastructure)
- Target architecture design (on-premises, cloud, hybrid, multi-cloud, edge)
- Platform foundation design: network topology, identity, tenancy boundaries (e.g., subscriptions, accounts, or projects in cloud; organizational units in on-premises)
- Infrastructure-as-Code (IaC) and platform automation
- Data platform strategy (mesh, lakes, warehouses, streaming, ML infrastructure)
- Application portfolio rationalization (the "7 Rs": Retain, Retire, Rehost, Replatform, Repurchase, Refactor, Rearchitect)
- Developer experience: internal developer platforms, CI/CD, toolchains

**Key Questions to Answer:**
- What is our target architecture, and what are the stepping stones to get there?
- Which workloads move when, and by which migration strategy?
- How do we enable development teams to move fast without creating risk?

---

### 5. Security & Compliance Perspective

**Purpose:** Protect confidentiality, integrity, and availability of data and systems throughout the adoption lifecycle.

**Key Stakeholders:** CISO, Security Architects, Compliance Officers, Platform Security Teams

**Core Capabilities:**
- Identity and Access Management (IAM): Zero Trust architecture, least-privilege, MFA/SSO
- Data protection: classification, encryption at rest and in transit, DLP
- Network security: segmentation, perimeter controls, private connectivity
- Threat detection, monitoring, and incident response (SIEM, SOAR, XDR)
- Vulnerability management and secure software supply chain
- Compliance-as-Code: automated policy enforcement and drift detection
- Business continuity and disaster recovery planning

**Key Questions to Answer:**
- What is our shared responsibility model, and what do we own?
- How do we maintain a consistent security posture across all our environments?
- How do we detect and respond to incidents faster than attackers can move?

---

### 6. Operations & Management Perspective

**Purpose:** Ensure technology services reliably meet agreed service levels and that operational practices scale with the organization.

**Key Stakeholders:** VP of Infrastructure/Operations, Site Reliability Engineers (SRE), IT Service Managers, FinOps Teams

**Core Capabilities:**
- Observability: logging, metrics, tracing, alerting, and dashboards
- Incident management and on-call operations (runbooks, playbooks, post-mortems)
- Change and release management
- Capacity planning and performance management
- FinOps execution: cost visibility, rightsizing, capacity commitment management (reservations, savings plans, committed-use discounts), TCO tracking. Policy and guardrails are set in the Governance & Risk perspective
- Service catalog and configuration management (CMDB)
- Automation of toil: reducing manual operational burden

**Key Questions to Answer:**
- How will we know when something is broken before users do?
- How do we manage operational complexity as the environment scales?
- How do we control and optimize spend continuously?

---

## Adoption Lifecycle Phases

The framework progresses through six sequential-but-iterative phases. Organizations may be in different phases for different workloads or business units simultaneously.

---

### Phase 1: Assess & Strategize

**Goal:** Establish baseline understanding of current state and define the transformation vision, business case, and priorities.

**Key Activities:**
- Technology landscape and portfolio inventory
- Business driver and stakeholder interviews
- Technology readiness assessment across all six perspectives
- Gap analysis: skills, architecture, governance, security posture
- Business case development: TCO/ROI modeling, risk quantification
- Define transformation goals, success criteria, and KPIs
- Establish executive sponsorship and program governance structure

**Outputs:**
- Current-state assessment report
- Approved business case
- High-level transformation roadmap (6–12 month horizon)
- Governance structure and RACI
- Quick-win candidates identified

---

### Phase 2: Plan & Prepare

**Goal:** Develop detailed plans for the transformation and build the foundational capabilities required to execute.

**Key Activities:**
- Detailed roadmap with workstreams, milestones, and resource requirements
- Platform foundation design and build
- Identity, access, and network baseline configuration
- Security baseline and compliance controls framework
- Workforce readiness plan: training, hiring, and organizational design
- Change management and communication plan
- FinOps model and cost governance policies established
- Pilot workload(s) selected for proof-of-concept

**Outputs:**
- Detailed project/program plan
- Deployed platform foundation: the baseline environment in which all subsequent workloads will run, including network topology, identity baseline, tenancy structure, core security controls, observability wiring, and policy guardrails. In cloud contexts this is often called the "landing zone"; in on-premises or hybrid contexts the equivalents are the reference environment, platform baseline, or core infrastructure pattern
- Workforce training program launched
- Pilot scope defined and approved

---

### Phase 3: Implement & Migrate

**Goal:** Execute migrations, new deployments, and workload onboarding in a structured, repeatable manner.

**Key Activities:**
- Wave-based migration execution (starting with low-risk, iterating to complex)
- Application rationalization decisions (7 Rs) made per workload
- CI/CD pipelines and deployment automation established
- Data migration and validation
- Integration testing and cutover planning
- User acceptance testing (UAT) and stakeholder sign-off
- Hypercare / stabilization period post-migration

**Migration Strategies (7 Rs):**

| Strategy | Description | Typical Use Case |
|---|---|---|
| **Retain** | Keep as-is, not migrating now | Legacy, decommission candidate |
| **Retire** | Decommission the workload | Redundant or end-of-life systems |
| **Rehost** | "Lift and shift" to new platform | Quick migration, minimal change |
| **Replatform** | Migrate with minor optimizations | Take advantage of managed services |
| **Repurchase** | Replace with SaaS alternative | CRM, ERP, collaboration tools |
| **Refactor** | Re-architect to utilize modern patterns | Performance, scalability needs |
| **Rearchitect** | Rebuild from scratch | Strategic differentiation workloads |

**Outputs:**
- Migrated/deployed workloads by wave
- Updated runbooks and operational documentation
- Hypercare completion sign-off per workload

---

### Phase 4: Govern & Secure

**Goal:** Operationalize governance, security, and compliance controls across the transformed environment at scale.

**Key Activities:**
- Policy-as-Code deployment (guardrails enforced automatically)
- Continuous compliance scanning and drift detection
- Privileged access reviews and Zero Trust maturity advancement
- Cost governance dashboards and chargeback/showback models
- Formal risk register review and remediation tracking
- Vendor and third-party access controls review
- Incident response tabletop exercises and playbook validation

**Outputs:**
- Automated governance and compliance dashboard
- Risk register with remediation status
- Security posture improvement metrics
- FinOps cost allocation and accountability model

---

### Phase 5: Optimize & Manage

**Goal:** Improve performance, reliability, and cost-efficiency of the operating environment while building operational excellence.

**Key Activities:**
- Performance benchmarking against target KPIs
- Cost optimization: rightsizing, reserved instances, spot/preemptible usage, hardware purchase
- Reliability engineering: SLOs, SLAs, error budgets
- Observability maturity improvements
- Operational runbook automation and AIOps adoption
- Platform consolidation and rationalization
- Well-Architected and design review assessments for key workloads (see [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/), [Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/), or [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) for vendor-specific pillar guidance)

**Outputs:**
- Cost reduction and performance improvement reports
- Updated architecture decision records (ADRs)
- Automation coverage metrics
- SLO/SLA compliance reports

---

### Phase 6: Modernize & Innovate

**Goal:** Leverage the transformed platform to drive competitive differentiation through modernization, AI, and net-new modern application development (cloud-native, container-based, serverless, or event-driven patterns as appropriate).

**Key Activities:**
- Application modernization (containers, serverless, microservices)
- Data platform maturation: real-time analytics, data mesh, ML/AI pipelines
- AI and generative AI adoption: model deployment, RAG pipelines, AI agents
- Modern technology product development with product teams
- Developer experience investment: internal developer platforms, self-service
- Innovation experiments and rapid prototyping cycles
- Contribution back to platform capabilities based on learnings

**Outputs:**
- Modernized application portfolio
- Active AI/ML use cases in production
- Internal developer platform in operation
- Innovation pipeline and experimentation metrics

---

## Maturity Model

Organizations progress through four maturity levels. Each level applies across all six perspectives.

| Level | Name | Description |
|---|---|---|
| **1: Tactical** | Ad-hoc | Reactive, manual processes. No formal standards. Individual heroics. High risk and inconsistency. |
| **2: Defined** | Repeatable | Basic processes documented. Standards exist but inconsistently applied. Some automation. Governance emerging. |
| **3: Managed** | Scalable | Consistent processes enforced. Governance automated. Teams operate with defined SLOs and cost visibility. Security controls systematic. |
| **4: Optimizing** | Strategic | Continuous improvement embedded. Platform-as-a-product mindset. AI-augmented operations. Business and technology strategy fully aligned. |

### Maturity by Perspective

Use this grid to assess current state and set targets per perspective. It is common and expected to be at Level 3 in one perspective while still at Level 1 in another; balanced progress across perspectives is more valuable than pushing any single perspective to Level 4 in isolation.

| Perspective | Level 1: Tactical | Level 2: Defined | Level 3: Managed | Level 4: Optimizing |
|---|---|---|---|---|
| **Business** | No formal business case; project-led funding; value unmeasured | Business cases developed per initiative; basic ROI tracking | Portfolio managed against business outcomes; value realization tracked | Technology strategy directly shapes business strategy; continuous outcome measurement |
| **People & Culture** | Ad-hoc training; skills gaps undocumented; change management reactive | Training curricula in place; some role-based paths; change plans per initiative | Role-based learning with certification targets; org design aligned to platforms or products; change as a steady practice | Continuous learning culture; leadership development continuous; org design evolves with strategy |
| **Governance & Risk** | Informal guardrails; shadow IT prevalent; compliance reactive | Basic policies documented; manual compliance checks; risk register exists | Policy-as-Code enforced; automated compliance scanning; portfolio governance active | Predictive governance; risk posture proactively managed; controls continuously tuned |
| **Platform & Technology** | Siloed infrastructure; manual provisioning; inconsistent architecture | Platform foundation built; some IaC; target architecture defined but not enforced | Consistent platform with self-service; IaC as standard; architecture governance active | Platform-as-a-product; internal developer platform; architecture continuously refreshed |
| **Security & Compliance** | Perimeter-based; reactive; manual audits | Basic Zero Trust principles; some automation; compliance evidence gathered per audit | Zero Trust broadly applied; continuous compliance monitoring; automated policy enforcement | Threat intelligence integrated; compliance-as-Code; security embedded in dev and ops |
| **Operations & Management** | Manual operations; firefighting culture; limited visibility | Runbooks documented; basic monitoring; change management process | SLOs defined; observability integrated; FinOps governance active; incident response drilled | Self-healing systems; automation-first operations; continuous cost and performance optimization |

### Technology Center of Excellence: Operating Model Evolution

As maturity increases, the central Technology CoE's role must shift. A CoE stuck in gatekeeper mode at Level 3+ becomes a bottleneck that teams will route around, recreating the shadow-IT problem the CoE was stood up to solve. A CoE that jumps to self-service before guardrails are automated leaves policy enforcement to goodwill. Plan the evolution deliberately:

| Stage | Maturity Range | CoE Role | Primary Activities | Failure Signal |
|---|---|---|---|---|
| **Gatekeeper** | Levels 1 → 2 | Central approval authority | Review architectures by hand, source tools, publish standards, block unsanctioned usage, execute first migration waves | High friction is acceptable here; if teams are not waiting on you, unsanctioned work is routing around |
| **Enabler / Advisor** | Level 3 | Consultant and accelerator | Provide reference architectures, reusable IaC modules, design review services, embedded advisors; curate the approved tool registry | Advisor queue depth is the bottleneck; teams stall waiting for consultation |
| **Platform / Self-service** | Level 4 | Platform owner | Operate the platform foundation, automated guardrails, internal developer platform, service catalog; teams self-serve within policy | Platform usage is high but policy or quality incidents rise: guardrails are not keeping up with what teams can do |

**Design implication:** Every control the gatekeeper enforces by hand in Stage 1 is a candidate to be codified into platform automation by Stage 3. Anything that cannot be automated must be designed as a lightweight self-attestation with sample-audit, not synchronous review. A CoE whose Stage 3 controls still require a human reviewer for every change is not actually at Stage 3.

**Naming note:** This pattern is often called "CCoE" (Cloud Center of Excellence) in cloud-specific contexts, "Platform CoE" in platform-engineering contexts, and simply "CoE" in technology-agnostic contexts. The same operating-model evolution applies regardless of the domain label.

**How to use the maturity model:**
- Assess current level per perspective at the start of each phase
- Set target maturity levels that are appropriate to organizational size, risk, and ambition; not every organization needs Level 4 in every perspective
- Use maturity gaps to prioritize roadmap items and investments
- Align the CoE operating mode to your dominant maturity level; mismatches (gatekeeper at Level 4, self-service at Level 1) create predictable failures

---

## Workload Strategy

Not all workloads are equal. Classify every workload before making migration or modernization decisions.

### Workload Classification

| Tier | Criticality | RTO / RPO | Typical Strategy |
|---|---|---|---|
| **Tier 0: Mission Critical** | Business stops without it | Minutes / Zero | Rearchitect or Replatform with HA/DR |
| **Tier 1: Business Critical** | Significant impact if down | Hours / Minutes | Replatform or Refactor |
| **Tier 2: Business Important** | Operational impact | Hours / Hours | Rehost or Replatform |
| **Tier 3: Supporting** | Low impact | Days / Hours | Rehost, Repurchase, or Retire |
| **Tier 4: Legacy / Candidate** | Marginal value | N/A | Retain short-term; plan Retirement |

### Portfolio Rationalization Process

1. **Inventory**: Catalog all applications with owner, business function, tech stack, hosting, cost
2. **Classify**: Assign tier and identify dependencies
3. **Decide**: Apply 7 Rs per workload
4. **Sequence**: Build migration waves (low risk → high complexity)
5. **Execute**: Migrate per wave with gates between waves
6. **Validate**: Confirm outcomes against targets post-migration

---

## Governance & Security Model

### Governance Layers

| Layer | Scope | Mechanism |
|---|---|---|
| **Enterprise Policies** | All environments | Policy-as-Code, guardrails, top-level standards |
| **Platform Controls** | Platform baseline | Platform wide controls, network rules, IAM baselines |
| **Workload Controls** | Per application | Application-level access, secrets management, compliance tags |
| **FinOps Controls** | Cost management | Budgets, alerts, tagging policies, chargeback |

### Zero Trust Security Principles

1. **Verify explicitly**: Authenticate and authorize every request based on all available data points
2. **Use least privilege**: Limit access with just-in-time, just-enough-access (JIT/JEA)
3. **Assume breach**: Minimize blast radius, segment access, encrypt everything, use analytics to detect threats

### Shared Responsibility Model

The boundary between provider and consumer responsibility varies by service model:

| Responsibility | IaaS | PaaS | SaaS |
|---|---|---|---|
| Data | Customer | Customer | Customer |
| Identity & Access | Customer | Customer | Customer |
| Application | Customer | Customer | Provider |
| Runtime/Middleware | Customer | Provider | Provider |
| OS | Customer | Provider | Provider |
| Infrastructure | Provider | Provider | Provider |
| Physical | Provider | Provider | Provider |

---

## Roles & Responsibilities

### Core Program Roles

| Role | Perspective Owner | Primary Responsibilities |
|---|---|---|
| **Executive Sponsor** | Business | Champions program, removes blockers, owns business case |
| **Program Director** | Governance | End-to-end program accountability, budget, stakeholder reporting |
| **Enterprise Architect** | Platform | Target architecture ownership, design authority |
| **Platform Lead** | Platform | Platform foundation build, shared platform services, IaC ownership |
| **Security Architect** | Security | Security baseline design, compliance mapping, threat modeling |
| **Change Manager** | People | Change impact assessments, communications, training coordination |
| **FinOps Lead** | Operations | Cost governance, optimization, chargeback modeling |
| **Operations Lead** | Operations | Observability, incident response, SRE practices |
| **HR / L&D Lead** | People | Skills gap plans, training programs, hiring pipelines |
| **Workload Owner** | Business | Application SME, migration decision authority per workload |

### RACI Template (per Phase)

| Activity | Executive Sponsor | Program Director | Architect | Security | Operations | Workload Owner |
|---|---|---|---|---|---|---|
| Business case approval | **A** | R | C | C | C | I |
| Architecture design | I | I | **A/R** | C | C | C |
| Security baseline | I | I | C | **A/R** | C | I |
| Migration execution | I | C | C | C | **A/R** | R |
| Cost governance | C | **A** | I | I | R | I |
| Training delivery | I | C | I | I | I | **A/R** |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## Success Metrics & KPIs

Track metrics across four outcome categories aligned to the business case.

### Business Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Technology ROI | Return on transformation investment | Positive within 24 months |
| Time-to-market | Speed of new feature/product delivery | 30% reduction |
| Business agility | Ability to respond to market changes | Qualitative + deployment frequency |
| ESG impact | Energy and carbon footprint reduction from efficiency gains | Measurable reduction in energy use, carbon intensity, or data-center PUE |

### Operational Outcomes

| KPI | Description | Target Example |
|---|---|---|
| System availability | Uptime against SLAs | 99.9%+ for Tier 0/1 |
| Deployment frequency | How often code ships to production | Daily or on-demand |
| Lead time for changes | Time from code commit to production | Hours to a day (high maturity) |
| MTTR | Mean time to resolve incidents | < 1 hour for P1 |
| Change failure rate | % of changes causing incidents | < 5% |
| Cost per workload | Total cost of ownership per application | Tracked and trending down |

*Deployment frequency, lead time for changes, MTTR, and change failure rate are the [DORA Four Keys](https://dora.dev/) and serve as the industry baseline for software delivery performance. Use them to benchmark against published DORA annual research.*

### Security Outcomes

| KPI | Description | Target Example |
|---|---|---|
| MTTD | Mean time to detect threats | < 24 hours |
| Policy compliance rate | % of resources in compliant state | > 95% |
| Critical vulnerability age | Time from detection to remediation | < 7 days |
| Access reviews completed | % of privileged access reviewed on schedule | 100% quarterly |

### People Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Certification attainment | % of target staff certified against role-relevant standards | 80% of platform and engineering staff |
| Change readiness score | Survey-based change readiness | > 70/100 |
| Adoption rate | % of teams using new platform/tools | > 85% |
| Attrition rate | Staff lost during transformation | Within normal range |

---

## Quick Reference Summary

```
COMPREHENSIVE TECHNOLOGY ADOPTION FRAMEWORK

  SIX PERSPECTIVES (What we manage)
  ┌────────────┬──────────────┬─────────────┬──────────────┬────────────┬────────────┐
  │  Business  │   People &   │ Governance  │  Platform &  │ Security & │ Operations │
  │            │   Culture    │   & Risk    │  Technology  │ Compliance │ & Mgmt     │
  └────────────┴──────────────┴─────────────┴──────────────┴────────────┴────────────┘

  SIX PHASES (How we progress)
  ┌───────────┐  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │  ASSESS   │→ │   PLAN   │→ │ IMPLEMENT │→ │  GOVERN  │→ │ OPTIMIZE │→ │ INNOVATE │
  │ Strategize│  │ Prepare  │  │ & MIGRATE │  │ & SECURE │  │ & MANAGE │  │ & SCALE  │
  └───────────┘  └──────────┘  └───────────┘  └──────────┘  └──────────┘  └──────────┘

  FOUR MATURITY LEVELS
  1. Tactical (Ad-hoc) → 2. Defined (Repeatable) → 3. Managed (Scalable) → 4. Optimizing (Strategic)

  COE OPERATING MODEL EVOLUTION (tracks maturity)
  Gatekeeper (L1-L2) → Enabler/Advisor (L3) → Platform/Self-service (L4)

  SEVEN MIGRATION STRATEGIES (7 Rs)
  Retain | Retire | Rehost | Replatform | Repurchase | Refactor | Rearchitect

  FIVE WORKLOAD CRITICALITY TIERS
  Tier 0 Mission-Critical | Tier 1 Business-Critical | Tier 2 Business-Important |
  Tier 3 Supporting | Tier 4 Legacy/Candidate

  FOUR GOVERNANCE LAYERS
  Enterprise Policies | Platform Controls | Workload Controls | FinOps Controls

  THREE ZERO TRUST PRINCIPLES
  Verify Explicitly | Use Least Privilege | Assume Breach

  THREE SERVICE MODELS (for Shared Responsibility)
  IaaS | PaaS | SaaS

  KEY OUTCOME CATEGORIES
  Business | Operational (incl. DORA Four Keys) | Security | People

  SPECIALIZATIONS
  AI Adoption Framework (AIAF) — seven perspectives, AI-specific controls
```

---

*Synthesized from three industry-leading cloud adoption frameworks: [AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/) (six-perspective structure, 47 foundational capabilities), [Google Cloud Adoption Framework](https://cloud.google.com/adoption-framework) (phased adoption lifecycle with maturity measurement), and [Microsoft Azure Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) (end-to-end methodology from strategy through operations). Software delivery performance metrics reference the [DORA Four Keys](https://dora.dev/). Architectural quality pillars reference the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/), and [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework). Zero Trust principles align with [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final). For AI, ML, or generative-AI-specific adoption, see the specialized [AI Adoption Framework (AIAF)](AIAdoptionFramework.md), which expands this base framework with a seventh perspective (Data & Knowledge) and AI-specific controls (Responsible AI, OWASP LLM Top 10, agent personas, GenAIOps). Not affiliated or endorsed in any way with any of the referenced companies or authors.*
