# AI Adoption Framework (AIAF)

> An organization-level framework for responsibly adopting AI tools (including large language models, AI assistants, AI coding tools, and autonomous AI agents), derived from the [Comprehensive Technology Adoption Framework](TechAdoptionFramework.md).

---

## Table of Contents

1. [Overview](#overview)
2. [Guiding Principles](#guiding-principles)
3. [Seven Core Perspectives](#seven-core-perspectives)
   - [Business Value Perspective](#1-business-value-perspective)
   - [People & Workforce Perspective](#2-people--workforce-perspective)
   - [AI Governance & Risk Perspective](#3-ai-governance--risk-perspective)
   - [Data & Knowledge Perspective](#4-data--knowledge-perspective)
   - [AI Platform & Integration Perspective](#5-ai-platform--integration-perspective)
   - [AI Security & Trust Perspective](#6-ai-security--trust-perspective)
   - [AI Operations & Quality Perspective](#7-ai-operations--quality-perspective)
4. [Adoption Lifecycle Phases](#adoption-lifecycle-phases)
   - [Phase 1: Discover & Assess](#phase-1----discover--assess)
   - [Phase 2: Pilot & Validate](#phase-2----pilot--validate)
   - [Pilot-to-Production Gate](#pilot-to-production-gate)
   - [Phase 3: Deploy & Integrate](#phase-3----deploy--integrate)
   - [Phase 4: Govern & Control](#phase-4----govern--control)
   - [Phase 5: Optimize & Measure](#phase-5----optimize--measure)
   - [Phase 6: Scale & Innovate](#phase-6----scale--innovate)
5. [AI Maturity Model](#ai-maturity-model)
6. [Use Case Classification](#use-case-classification)
7. [Responsible AI Model](#responsible-ai-model)
8. [AI Shared Responsibility Model](#ai-shared-responsibility-model)
9. [Roles & Responsibilities](#roles--responsibilities)
10. [Non-Human Actors: Agent and System Personas](#non-human-actors-agent-and-system-personas)
11. [Success Metrics & KPIs](#success-metrics--kpis)
    - [Business Outcomes](#business-outcomes)
    - [Adoption Outcomes](#adoption-outcomes)
    - [Quality & Safety Outcomes](#quality--safety-outcomes)
    - [Operational Outcomes](#operational-outcomes)
    - [Data & Knowledge Outcomes](#data--knowledge-outcomes)
    - [GenAIOps & Agent Outcomes](#genaiops--agent-outcomes)
12. [Applying the Framework at Different Scales](#applying-the-framework-at-different-scales)
13. [Quick Reference Summary](#quick-reference-summary)

---

## Overview

The **AI Adoption Framework (AIAF)** is a structured, vendor-agnostic approach for organizations planning, governing, and scaling the adoption of AI tools across their workforce and products. It applies specifically to:

- **AI assistants**: conversational AI for search, writing, analysis, and Q&A
- **AI coding tools**: AI-powered developer assistants operating in IDEs and terminals
- **AI agents**: autonomous or semi-autonomous systems that use tools, browse, write code, or take multi-step actions
- **AI-embedded products**: internal or customer-facing products that integrate AI model APIs
- **Generative AI pipelines**: retrieval-augmented generation (RAG), summarization, classification, and structured output systems

### Relationship to the Base Framework

The AIAF is a specialization of the [Technology Adoption Framework (TAF)](TechAdoptionFramework.md). It inherits the same structural DNA (six lifecycle phases and a four-level maturity model) but adapts every element to the unique characteristics of AI adoption, and expands TAF's six perspectives to **seven** by elevating Data & Knowledge to first-class status (reflecting Google Cloud's treatment of data as a peer dimension to People, Process, and Technology):

| TAF Concept | AIAF Adaptation |
|---|---|
| Six perspectives | Seven perspectives (adds Data & Knowledge as a standalone perspective) |
| Workload Strategy (7 Rs) | Use Case Classification (5 categories + risk tiers) |
| Platform Landing Zone | AI Platform Foundation (APIs, gateways, data boundaries) |
| Security Posture | AI Trust & Safety (prompt security, output integrity, data privacy) |
| FinOps | AI Cost Management (token economics, usage governance) |
| Change Management | Workforce Transformation (augmentation anxiety, skill building) |
| Compliance Controls | Responsible AI Controls (AI Act, bias audits, impact assessments) |
| Data governance (cross-cutting) | Data & Knowledge perspective (grounding vs training data, prompt/eval/index reuse) |

### The AIAF as Part of a Stack

The AIAF is one layer in a stack of guidance an organization needs to adopt AI responsibly. The layers are complementary, not competing. Mixing them (compliance questions answered as adoption questions, or runtime changes justified by revisiting principles) is a common source of confusion:

| Layer | Question it answers | Artifacts |
|---|---|---|
| **Responsible AI foundation** | What principles and regulatory obligations must hold regardless of technology? | RAI principles (Fairness, Reliability, Privacy, Transparency, Accountability, Inclusiveness); regulatory scope (EU AI Act, sector-specific rules); organizational risk appetite |
| **Adoption framework (this AIAF)** | How do we govern, roll out, and scale AI across the organization, end to end? | Seven perspectives; six phases; maturity model; AIIA process; RACI; Decision Register |
| **Implementation patterns** | For a given use case pattern, what is the reference architecture, prompt library, eval set, and control set? | Reference scenario entries; prompt and eval libraries; platform templates |
| **Runtime operations** | What runs where, with what controls, monitored how? | AI gateway, observability, policy enforcement, incident response runbooks |

**Design implication:** Changes at one layer should not force changes at others. Switching model providers is a runtime change and should not invalidate your RAI principles or require rewriting the adoption framework. A new EU AI Act obligation enters at the foundation layer and propagates down, but should not require reinventing the adoption phases.

**When to consult which layer:**

- Compliance or ethics question: start at the foundation, then consult the AIAF for operationalization.
- New use case triage: AIAF (classify, prioritize, AIIA), then implementation patterns, then runtime.
- Architecture decision: implementation patterns and runtime; the AIAF should rarely need to change.
- "Should we even do this?" decision: foundation, not framework.

### Why AI Adoption Is Different

AI tools introduce challenges that traditional IT governance was not designed for:

- **Non-deterministic outputs**: the same prompt can produce different results; quality must be measured statistically, not by unit tests
- **Shadow AI**: employees often adopt AI tools personally before organizational policy exists, creating ungoverned data exposure
- **Prompt as attack surface**: prompt injection, jailbreaking, and data exfiltration via model APIs are novel threat vectors
- **Workforce anxiety**: AI adoption touches job security in ways other technology migrations typically do not
- **Regulatory landscape in motion with concrete deadlines**: the EU AI Act is partially in force (prohibited-practice provisions applied Feb 2025, general-purpose AI model obligations Aug 2025, high-risk system obligations apply Aug 2026, Annex I regulated-product systems Aug 2027). Alongside the Act, **NIST AI RMF** is the US voluntary reference increasingly cited in contracts, and **ISO/IEC 42001** (the AI management system standard) is being adopted for certification. Sector-specific AI rules (financial services, healthcare, employment, education) continue to layer on top. Deadlines are now concrete, not theoretical
- **Data boundary blurring**: sending internal content to external model APIs requires explicit data governance decisions
- **Build/buy economics reset**: AI-assisted development dramatically lowers the cost and time to build custom software. Capabilities that previously required vendor products or large development teams are now within reach of small teams. This creates a strategic opportunity (reassessing current vendor spend as potential build candidates) and a competitive risk (customers, partners, or new entrants can build alternatives to products and services you provide)

---

## Guiding Principles

1. **Outcomes before models**: Select AI tools based on the specific outcomes you need, not on which model is most popular. Avoid vendor lock-in by abstracting model choice behind internal interfaces where possible.
2. **Humans remain accountable**: AI augments human judgment; it does not replace human accountability. Every AI output that influences a consequential decision must have a named human owner.
3. **Responsible by design**: Fairness, transparency, and privacy considerations are designed into AI use cases from the start, not evaluated after deployment.
4. **Govern shadow AI, don't just prohibit it**: Employees are already using AI. A prohibition-only approach drives usage underground. Provide sanctioned tools and clear policies instead.
5. **Start narrow, expand with evidence**: Begin with well-scoped, low-risk use cases. Expand scope and automation level only when quality and safety thresholds are demonstrably met.
6. **Measure quality, not just usage**: Adoption metrics (seats, sessions) are vanity metrics. Track whether AI outputs are accurate, trusted, and delivering business value.
7. **Preserve the right to intervene**: Every AI-driven process must have a defined mechanism for humans to override, pause, or roll back AI behavior.
8. **Continuous evaluation**: AI model capabilities, risks, and costs change rapidly. Treat AI tool selection and configuration as a continuously reviewed decision, not a one-time purchase.

---

## Seven Core Perspectives

Each perspective defines who is responsible for what throughout the AI adoption lifecycle. All seven must be engaged in every phase.

---

### 1. Business Value Perspective

**Purpose:** Ensure AI investments are directed toward use cases with clear business value, and that realized value is tracked and reported.

**Key Stakeholders:** CEO, CFO, COO, Business Unit Leaders, Product Owners, Strategy Teams

**Core Capabilities:**
- AI opportunity identification: systematic scanning of workflows for high-value AI use cases
- Business case development: quantifying productivity gains, cost reduction, revenue uplift, and risk reduction
- Use case prioritization: scoring opportunities by value, feasibility, and risk
- Value realization tracking: measuring actual vs. projected outcomes post-deployment
- AI vendor and partner management: licensing, contracts, SLAs, and strategic alignment
- AI portfolio management: visibility across all active AI initiatives to avoid duplication and manage spend
- Build vs. buy reassessment: evaluating current SaaS and enterprise software spend against AI-assisted build alternatives; identifying where custom-built solutions now deliver better value, differentiation, or strategic control than purchased software

**Key Questions to Answer:**
- Which business problems are we solving, and why is AI the right solution for each?
- What does success look like in 90 days, 12 months, and 3 years?
- How do we ensure AI spend is producing measurable returns, not just activity?
- Which capabilities are we currently paying vendors for that AI-assisted development has made economically viable to build and own? And conversely, which products or services we provide are now at risk from customers or competitors building their own alternatives?

---

### 2. People & Workforce Perspective

**Purpose:** Prepare the workforce for AI-augmented ways of working, address displacement anxiety, and build the skills needed to use AI effectively and responsibly.

**Key Stakeholders:** Head of HR, L&D Leaders, Team Managers, Union Representatives (where applicable), Internal Communications

**Core Capabilities:**
- Workforce impact assessment: identifying roles and tasks most affected by AI adoption
- Skills gap analysis: mapping required AI literacy, prompt engineering, and critical evaluation skills against current workforce capabilities
- Tiered training programs: role-specific learning paths (executive awareness, practitioner proficiency, builder/developer depth)
- Change management: communication strategies that address both the opportunity and the fear of AI adoption
- Augmentation mindset: cultivating the expectation that AI handles routine work, freeing humans for higher-value judgment and creativity
- Thin work / valued work classification: systematically categorizing tasks within each role as either **thin work** (repetitive, low-value, machine-ready tasks that AI should absorb) or **valued work** (creative, strategic, judgment-intensive tasks that humans should be freed to focus on). This classification drives both AI use case prioritization and workforce transition planning
- AI acceptable use policy communication: ensuring every employee understands what is and isn't permitted
- Feedback culture: creating mechanisms for employees to report when AI tools are underperforming or producing harmful outputs

**Key Questions to Answer:**
- What tasks are being automated, and how do affected employees transition to higher-value work?
- How do we build AI literacy across all roles, not just technical teams?
- How do we address the fear that AI will replace jobs while being honest about changing role requirements?
- As workflows progress from human-performed to AI-augmented to AI-automated, leaders shift from managing people who *do the work* to managing people who *direct AI that does the work*. Have our leaders been prepared for this transition?

---

### 3. AI Governance & Risk Perspective

**Purpose:** Establish the policies, processes, and controls required to manage AI-specific risks: including ethical risks, regulatory compliance, and ungoverned usage.

**Key Stakeholders:** CIO, Chief Risk Officer, Chief Compliance Officer, Legal, Privacy Officer, Internal Audit, AI Ethics Officer

**Core Capabilities:**
- AI policy framework: acceptable use policies, data handling rules, approved tool registry, prohibition list
- AI risk taxonomy: classifying AI risks by type: accuracy, bias, privacy, security, legal, reputational, operational
- AI Impact Assessment (AIIA) process: mandatory evaluation before deploying AI to consequential use cases
- Regulatory compliance mapping: **EU AI Act** (applicability by system risk class with obligations staggered from Feb 2025 through Aug 2027); **NIST AI Risk Management Framework** (US voluntary reference widely adopted and increasingly contract-cited); **ISO/IEC 42001** (AI management system standard, available for certification and analogous to ISO 27001 for infosec); **GDPR and CCPA** as they intersect with AI training data, inference data, and automated decision-making; **HIPAA**; and sector-specific rules (financial services, healthcare, employment, education, safety-critical systems)
- Shadow AI governance: detection, remediation, and channeling of unsanctioned AI tool usage. Governance should define safe experimentation boundaries rather than blanket prohibition: personal exploration with unsanctioned tools is acceptable when those tools are not connected to company data, not invited into meetings or internal systems, and not authenticated with organizational credentials
- AI Decision Register: a maintained record of where AI is making, shaping, or influencing decisions inside the organization, who owns those decisions, what guardrails apply, and how exceptions are handled. Distinct from audit logging (which captures interactions); the decision register captures the *design* of AI's role in decision-making
- AI audit and accountability: logging AI interactions for regulated use cases, maintaining evidence of human oversight
- Third-party AI vendor risk: due diligence on AI providers' data handling, model training practices, and security posture
- AI cost governance: token usage budgets, cost allocation, and FinOps for AI APIs

**Key Questions to Answer:**
- What data can and cannot be sent to external AI APIs, and how is this enforced?
- Which of our AI use cases fall into the EU AI Act's high-risk categories, and are we on track for the Aug 2026 obligations? Are we aligning controls with NIST AI RMF? Is ISO/IEC 42001 certification a customer, partner, or procurement requirement we need to plan for?
- How do we detect and govern AI tools that employees are using outside of sanctioned channels?
- Which of our current software vendors operate in categories now at risk of AI-driven displacement, and what is our contingency if those vendors' products or businesses are disrupted?

---

### 4. Data & Knowledge Perspective

**Purpose:** Treat data and knowledge assets as the foundation that determines what AI can and cannot do. Govern, organize, and make discoverable the data sources, retrieval indexes, embeddings, prompt libraries, and evaluation datasets that AI systems depend on. A capable model on weak or ungoverned data produces weak or ungoverned outcomes.

**Key Stakeholders:** Chief Data Officer, Data Stewards, Knowledge Managers, Information Architects, Data Engineering Leads, Records Management

**Core Capabilities:**
- Data classification for AI: maintaining authoritative classification (public, internal, confidential, restricted, regulated) with explicit rules for which classes may be used in prompts, retrieval, training, or fine-tuning
- Grounding data design: managing the corpora that AI retrieves from at inference time, including knowledge bases, document indexes, and vector stores. Concerns include freshness, source-of-truth designation, retrieval-time access scoping, and redaction
- Training and fine-tuning data design: separately governing the datasets used to train, fine-tune, or distill models. Concerns include consent, provenance, IP rights, opt-out handling, and contamination prevention
- Data lineage and provenance: tracking where AI inputs came from and where AI-generated outputs flow, including synthetic data lineage and attribution for retrieved context
- Prompt library management: centralized, versioned, discoverable prompt assets reusable across teams, with documented ownership, evaluation results, and intended use
- Evaluation dataset catalog: shared "golden" eval sets and benchmark datasets owned, versioned, and discoverable across teams so evaluation is not rebuilt per project
- Knowledge asset reuse: feature stores, embedding stores, retrieval indexes, and processed knowledge artifacts published as reusable assets rather than silently rebuilt in each initiative
- Data retention and lifecycle: retention rules for prompts, completions, retrieved context, and AI-generated artifacts, including legal hold, export, and deletion considerations
- Synthetic data governance: rules for generating, labeling, and using AI-produced synthetic data in downstream systems, preventing unmarked synthetic data from contaminating future training

#### Grounding Data vs Training Data: Why the Distinction Matters

Grounding data (retrieved at inference time, as in RAG) and training data (baked into model weights during training or fine-tuning) share the word "data" but require different governance because they enter the AI system at different times with different blast radius:

| Property | Grounding Data (RAG / retrieval) | Training / Fine-tuning Data |
|---|---|---|
| Where it enters | Inference time, per query | Training time, baked into weights |
| Who can change it | Index owner, often near-real-time | Model team, infrequent releases |
| Access control | Can be enforced per-user, per-query | Cannot be enforced once trained |
| Rights and consent | Required at retrieval time; can be revoked | Required at training time; hard to revoke |
| Contamination blast radius | Affects one response | Affects every future response |
| Removal mechanism | Re-index | Retrain or unlearn (often impractical) |

Treating these as the same concern leads to one of two failures: applying training-grade governance to grounding data (creating friction that kills RAG use cases), or applying retrieval-grade governance to training data (creating compliance gaps that surface years later).

**Access & Reuse Principle:** Assume every AI artifact your organization produces (prompts, eval sets, retrieval indexes, embeddings, fine-tuned models) will be useful to more than one team. If it cannot be discovered, attributed, and reused, it will be silently rebuilt, resulting in duplicate spend, inconsistent quality, and divergent governance. Discoverability is a governance control, not a nice-to-have.

**Key Questions to Answer:**
- For each AI use case, which data sources are grounding (retrieved at inference time) and which are training (baked into the model)? Are they governed accordingly?
- Where are our prompt libraries, eval datasets, and retrieval indexes published so other teams can discover and reuse them rather than rebuild?
- What is our retention policy for prompts, completions, and AI-generated artifacts, and how is it enforced technically?
- If a data subject exercises a deletion right, can we remove their data from grounding indexes? From training data? What is the timeline for each, and who owns it?
- Which AI-generated artifacts are flowing back into future training data (our own or third-party), and is that flow intentional and governed?

---

### 5. AI Platform & Integration Perspective

**Purpose:** Build and maintain the technical foundation that enables AI tools to be integrated securely, consistently, and at scale across the organization.

**Key Stakeholders:** CTO, AI/ML Platform Engineers, Enterprise Architects, Data Engineers, Developer Experience Teams

**Core Capabilities:**
- AI gateway / API management: centralized routing, rate limiting, logging, and model-switching without application changes
- RAG infrastructure: vector databases, embedding pipelines, document ingestion services, and retrieval runtime (the *technology platform* for grounding; corpus ownership, classification, and reuse belong to the Data & Knowledge perspective)
- Identity and access for AI: ensuring AI agents and APIs use scoped, auditable credentials with least-privilege access
- AI tool integration patterns: IDE plugins, chat platform integrations, workflow automation hooks, API-first design
- Prompt deployment infrastructure: centralized prompt versioning, testing, and deployment runtime (the *runtime platform*; prompt-as-asset curation and cross-team reuse belong to the Data & Knowledge perspective)
- Evaluation infrastructure: automated evals, golden dataset management, regression testing for AI output quality
- Model abstraction: designing systems so the underlying model can be swapped without full rewrites
- Developer platform for AI: self-service tooling that lets teams build AI features safely within guardrails

**Key Questions to Answer:**
- How do we prevent every team from independently integrating the same AI APIs with no shared governance?
- How do we ensure that when a model provider changes their API or pricing, we can respond quickly?
- How do teams evaluate whether their AI integration is actually working well?

---

### 6. AI Security & Trust Perspective

**Purpose:** Protect the organization from AI-specific threats and ensure that AI systems behave in ways that can be trusted by users, customers, and regulators.

**Key Stakeholders:** CISO, AI Security Engineers, Privacy Engineers, Red Team / Offensive Security, Compliance

**Core Capabilities:**
- Data classification for AI: determining what data classes (PII, confidential, IP) can be processed by which AI tools
- Prompt injection defense: detecting and preventing adversarial inputs that attempt to hijack AI behavior or exfiltrate data
- Output filtering and content safety: post-processing AI outputs to detect harmful, sensitive, or policy-violating content before surfacing to users
- AI supply chain security: vetting model providers, third-party fine-tuning, open-source models, and AI plugins
- Agentic action boundaries: defining and enforcing the scope of actions that AI agents are permitted to take (read vs. write vs. execute)
- Audit logging for AI: immutable logs of prompts, retrieved context, and AI outputs for regulated use cases
- Incident response for AI: playbooks for handling AI-related incidents: data leakage via prompts, hallucinations in critical decisions, agent actions that cause harm
- Model reliability and availability: ensuring AI dependencies have fallback behavior and do not create single points of failure

**Key Questions to Answer:**
- What happens if a user or attacker crafts a prompt that causes the AI to leak confidential data?
- How do we detect when an AI agent is about to take an action outside its intended scope?
- What is our incident response process when an AI system produces harmful or incorrect outputs at scale?

#### OWASP LLM Top 10 Mapping (2025)

The [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) is the de facto industry taxonomy for LLM-specific security risks. Every Tier 2+ use case should be assessed against each risk and record its mitigations. Map each risk to the capability that owns it:

| OWASP Risk | Description | Primary Owner |
|---|---|---|
| **LLM01: Prompt Injection** | Adversarial input that manipulates model behavior or bypasses instructions (direct or via retrieved content) | Security & Trust (prompt injection defense) |
| **LLM02: Sensitive Information Disclosure** | Model reveals PII, credentials, or confidential data via training data, context, or prompts | Data & Knowledge + Security & Trust |
| **LLM03: Supply Chain** | Compromised models, fine-tunes, plugins, datasets, or inference services | Security & Trust (AI supply chain security) |
| **LLM04: Data and Model Poisoning** | Training data or fine-tune corpus deliberately corrupted to introduce backdoors or bias | Data & Knowledge (training data governance) |
| **LLM05: Improper Output Handling** | Downstream systems blindly execute or render AI output, enabling XSS, SSRF, code execution, data exfiltration | Platform & Integration + Security & Trust |
| **LLM06: Excessive Agency** | Agent granted more permissions, tools, or autonomy than the use case justifies, enabling unintended real-world actions | Security & Trust (agentic action boundaries) |
| **LLM07: System Prompt Leakage** | System prompts containing secrets, policies, or access patterns are extracted by users or adversaries | Platform & Integration (prompt design) + Data & Knowledge |
| **LLM08: Vector and Embedding Weaknesses** | Attacks on RAG: poisoned embeddings, cross-tenant leakage, unauthorized retrieval | Data & Knowledge (grounding data) + Platform & Integration |
| **LLM09: Misinformation** | Confident but false output accepted by humans or downstream systems without verification (overreliance) | Operations & Quality (evals) + People & Workforce (AI literacy) |
| **LLM10: Unbounded Consumption** | Resource exhaustion, runaway cost, or denial of wallet from unconstrained prompts, context, or agent loops | Operations & Quality (cost controls) + Platform & Integration (rate limiting) |

**Applying the mapping:** The AIIA for Tier 2+ use cases must explicitly enumerate which of the ten risks apply, what technical and procedural controls are in place, and who owns each. Risks that do not apply to a given use case should be marked explicitly (e.g., "LLM04 not applicable: we do not fine-tune"). Unmitigated risks escalate to the AI governance body.

---

### 7. AI Operations & Quality Perspective

**Purpose:** Ensure AI tools and systems operate reliably, that their output quality is continuously measured, and that they remain cost-effective over time.

**Key Stakeholders:** AI Operations Teams, SRE, FinOps, Product Managers, Quality Assurance

**Core Capabilities:**
- AI observability: monitoring latency, error rates, token usage, and model availability across all AI integrations
- Output quality measurement: evaluation frameworks (LLM-as-judge, human review panels, task-specific evals) to measure accuracy, relevance, and safety
- Feedback loops: structured collection of user ratings and corrections to identify quality drift and improvement opportunities
- GenAIOps discipline: the operational practice for systems built on pre-trained models, distinct from classical MLOps (see subsection below)
- Token cost management: tracking spend per use case, team, and model; rightsizing context windows; optimizing prompt efficiency
- Model version management: tracking which model version is in use where, and managing upgrades without quality regressions
- Capacity and rate limit management: handling API rate limits gracefully, planning for usage growth
- AI service catalog: internal directory of approved AI tools, their data handling properties, approved use cases, and owners
- Continuous improvement cycles: regular review of AI use cases to retire underperforming ones, improve prompts, and upgrade to better models

#### GenAIOps vs MLOps

Classical MLOps centers on the training pipeline: feature engineering, experiment tracking, training orchestration, model registry, and serving infrastructure for models you built. Most generative-AI use cases do not train models; they compose pre-trained models with prompts, retrieval, and tools. The operational unit of change shifts from the model to the *prompt*, the *retrieval index*, and the *agent configuration*. This is **GenAIOps**:

| Dimension | MLOps (classical) | GenAIOps (pre-trained models) |
|---|---|---|
| Primary artifact | Trained model | Prompt, index, agent config, tool set |
| Change cadence | Weeks to months | Hours to days |
| Quality gate | Model eval on held-out set | Prompt/agent eval against golden set, LLM-as-judge, red-team |
| Rollout unit | Model version | Prompt version, index version, model version |
| Registry | Model registry | Prompt registry, eval set registry, retrieval index registry (plus model registry) |
| Primary failure mode | Drift in input distribution | Prompt regression, retrieval staleness, model-provider update, tool misuse |

Both disciplines coexist: an organization fine-tuning a model and serving it via RAG runs both. Treat them as peers, not as one replacing the other. Own each with clear capabilities, pipelines, and promotion gates.

**Key Questions to Answer:**
- How do we know when an AI tool's output quality has degraded?
- How do we track and control AI API costs as usage scales across the organization?
- How do we manage the operational impact of a model provider's deprecation or pricing change?
- What is our promotion path for a new prompt or retrieval index, and what eval thresholds gate it?

---

## Adoption Lifecycle Phases

The framework progresses through six phases. Different use cases and teams may be at different phases simultaneously. Each gate requires evidence before proceeding.

---

### Phase 1: Discover & Assess

**Goal:** Build a shared understanding of the AI landscape, identify high-value opportunities, assess organizational readiness, and establish the governance foundation before any deployment.

**Key Activities:**
- AI opportunity workshops with business units: systematic identification of use cases by workflow. Match candidates to the [Reference Scenarios](#reference-scenarios-canonical-patterns) library to inherit classification as a starting point
- Backlog ranking: apply the [Use Case Prioritization Rubric](#use-case-prioritization-rubric) to rank candidates reproducibly rather than by stakeholder enthusiasm
- Workforce readiness survey: AI literacy, awareness, and sentiment baseline
- Shadow AI audit: inventory of AI tools already in use across the organization
- Data readiness assessment: classify data assets; identify which can and cannot be used with AI tools. See the [Data & Knowledge Perspective](#4-data--knowledge-perspective) for grounding-vs-training data treatment
- Regulatory mapping: identify applicable AI regulations and standards (EU AI Act, sector rules, NIST AI RMF, ISO/IEC 42001) and their requirements for your sector and location
- AI vendor landscape review: evaluate available tools by capability, data handling, pricing, and security posture
- Vendor displacement analysis: map current software vendor spend against the new build/buy calculus; identify where AI-assisted development makes custom builds viable, and assess which of your own products or services are exposed to the same dynamic from your customers
- Risk appetite definition: establish organizational thresholds for AI risk tolerance by use case category
- Establish AI governance body: steering committee, working groups, accountability structure. Record the initial operating mode per the [CoE Operating Model Evolution](#ai-center-of-excellence-operating-model-evolution)

**Gate Criteria to Proceed:**
- Approved AI Policy Framework (v1) published
- Approved tool registry established (even if small)
- Executive sponsor named
- At least one high-value, low-risk pilot use case selected

**Outputs:**
- AI opportunity map with prioritized use case backlog
- Shadow AI inventory and remediation plan
- Organizational AI readiness assessment
- AI Policy Framework v1
- Approved AI governance structure

---

### Phase 2: Pilot & Validate

**Goal:** Run structured, time-boxed pilots of selected AI use cases to validate value, test governance controls, and build organizational confidence before broad rollout.

**Key Activities:**
- Define pilot scope: specific use case, target user group, success criteria, and time boundary
- Document target workflow as SOP: before any AI tool is applied, the target process must be documented with its steps, decision points, exceptions, and handoffs. If the process is not documented, it is not ready to automate or augment. Classify each step as thin work (repetitive, machine-ready) or valued work (judgment-intensive, human-required)
- Stand up AI platform foundation: API gateway, logging, access controls, data boundary enforcement
- Conduct AI Impact Assessment (AIIA) for each pilot use case, enumerating the applicable [Measurable RAI Goals](#measurable-rai-goals-evidence-requirements) and the evidence artifact for each
- Deploy AI tools to pilot group with onboarding, training, and feedback mechanisms
- Establish evaluation baseline: measure pre-AI performance of the target task
- Run pilot with structured feedback collection (quantitative + qualitative)
- Red-team the pilot: systematically exercise each applicable risk in the [OWASP LLM Top 10 Mapping](#owasp-llm-top-10-mapping-2025) (prompt injection, sensitive info disclosure, excessive agency, etc.)
- Measure outcomes against baseline: quality, speed, user satisfaction, cost
- Document learnings: what worked, what failed, what needs governance adjustment

**Gate Criteria to Proceed:**
- Target workflow documented as SOP with decision points, exceptions, and handoffs identified
- Pilot outcomes meet or exceed pre-defined success thresholds
- No unresolved critical security or compliance findings
- Governance controls validated under realistic usage
- Rollout plan approved by AI governance body

**Outputs:**
- Pilot evaluation report with go/no-go recommendation
- Updated AI Impact Assessment for the use case
- Refined prompts, configurations, and integration patterns
- Rollout plan for Phase 3

---

### Pilot-to-Production Gate

Between Phase 2 and Phase 3, a specific class of failure deserves its own gate: **pilots that pass their success criteria and still fail to reach durable production use**. Industry surveys consistently estimate that a large majority of AI pilots (commonly cited around 80–90%) do not transition from successful pilot to steady-state production, despite meeting pilot-phase targets. The cause is rarely the AI itself; it is the absence of production-grade ownership, operations, and budget that the pilot did not require. Pilots run on volunteers, goodwill, and temporary credits. Production does not.

Before a pilot progresses to Phase 3, confirm each of the following is in place and funded, not merely named:

| Readiness Dimension | Question | Evidence |
|---|---|---|
| **Production owner** | Who is accountable for this use case in production, as part of their day job (not as a pilot volunteer)? | Named individual with this responsibility in their objectives and time allocation |
| **Operational ownership** | Who is paged when quality degrades, costs spike, or the provider has an outage? | On-call rotation with documented runbook |
| **Funded operating budget** | Is operating spend funded for at least 12 months beyond pilot, covering expected growth? | Approved line in business unit or central platform budget, not trial credits |
| **Eval infrastructure** | How will quality be measured continuously, not just during the pilot window? | Golden eval set, automated eval pipeline, dashboard, alert thresholds |
| **Platform integration** | Is the use case running on the approved AI gateway with logging, rate limits, and data boundary enforcement? | Gateway configuration reviewed, audit log sample verified |
| **User support** | Who do users contact with problems? What is the response SLA? | Documented support channel and SLA, resourced |
| **Change management beyond pilot cohort** | How will the next 100, 1,000, or 10,000 users be onboarded? | Training content, rollout communications, acceptable use acknowledgment flow |
| **Decommission / provider-change plan** | If the model provider deprecates, changes pricing materially, or changes terms, what is our move? | Documented alternative model, migration path, or sunset criteria |

**Rule:** A pilot that meets all functional success criteria but has no production owner, no eval infrastructure, and no operating budget is not ready to deploy. Send it back to Phase 2 to secure these, or decide not to proceed. "We will figure that out later" is the single most reliable predictor of a pilot that will quietly die six months after its celebratory all-hands demo.

---

### Phase 3: Deploy & Integrate

**Goal:** Roll out validated AI use cases to broader populations in a structured, wave-based approach with active monitoring and user support.

**Key Activities:**
- Wave-based rollout: pilot group → department → organization (gated by adoption and quality metrics)
- Integration with existing tools and workflows (chat platforms, IDEs, ticketing systems, document management)
- Employee onboarding: role-specific training, acceptable use policy acknowledgment, feedback channels
- Enable AI service catalog entry: published documentation, owner, data handling classification
- Activate production monitoring: token usage, error rates, latency, quality sampling
- Establish support channel for AI-related questions and issues
- Communicate proactively: what the tool does, what it doesn't do, and how employees should use it
- Data boundary enforcement: technical controls preventing unauthorized data from reaching AI APIs
- For any deployment involving agents, classify and register each non-human actor per [Agent and System Personas](#non-human-actors-agent-and-system-personas) with its identity, scope, and named human owner before go-live

**Rollout Decision Matrix:**

| Use Case Category | Deployment Approach | Required Sign-offs |
|---|---|---|
| Internal productivity (low risk) | Standard wave rollout | AI Lead + IT |
| Customer-facing (medium risk) | Limited beta → full rollout | AI Lead + Legal + Security |
| Consequential decisions (high risk) | Controlled rollout with mandatory human review | AI Ethics Officer + Legal + Executive |
| Autonomous/agentic actions (critical) | Narrow scope, sandboxed, manual escalation | CISO + Legal + Board-level awareness |

**Outputs:**
- Deployed AI use case with active monitoring
- Training completion records
- AI service catalog entry
- Baseline quality and usage metrics established

---

### Phase 4: Govern & Control

**Goal:** Operationalize AI governance at scale, ensuring policies are enforced, risks are tracked, and accountability is maintained across all active AI use cases.

**Key Activities:**
- Activate centralized AI audit logging for regulated use cases
- Establish and maintain the AI Decision Register: a living record of every point where AI is making, shaping, or influencing decisions; who owns each decision; what guardrails apply; and how exceptions are escalated. Review the register quarterly with the governance body
- Enforce data classification rules via AI gateway (block, redact, or alert on policy violations)
- Conduct first AI use case review cycle: reassess risk ratings and quality thresholds; re-run the [OWASP LLM Top 10](#owasp-llm-top-10-mapping-2025) assessment for Tier 2+ use cases and document mitigations or residual risk
- Audit measurable RAI evidence: confirm each applicable [Measurable RAI Goal](#measurable-rai-goals-evidence-requirements) still has current evidence; remediate gaps
- Vendor risk reviews for all AI API providers
- Establish AI cost governance: budgets by team/use case, alerts, chargeback model
- Formalize AI incident response process and run tabletop exercise
- Review and update AI Policy Framework based on operational learnings
- Compliance evidence package for relevant regulations (EU AI Act, sector rules)
- Address any shadow AI surfaced in production monitoring

**Key Governance Controls:**

| Control | Mechanism | Frequency |
|---|---|---|
| Data boundary enforcement | AI gateway policy rules | Continuous |
| Usage and cost visibility | Token usage dashboards | Weekly |
| Output quality sampling | Automated evals + human review | Per use case cadence |
| Incident detection | Anomaly detection on logs | Continuous |
| Policy acknowledgment | Annual employee re-acknowledgment | Annual |
| Vendor risk review | Third-party AI provider assessments | Annual / at contract renewal |
| AI use case registry review | Governance body review of active use cases | Quarterly |

**Outputs:**
- AI governance dashboard (policy compliance, incidents, cost, quality)
- Updated risk register with AI-specific entries
- Regulatory compliance evidence package
- Incident response playbooks tested and validated

---

### Phase 5: Optimize & Measure

**Goal:** Improve the quality, efficiency, and business impact of AI use cases based on operational data, user feedback, and evolving model capabilities.

**Key Activities:**
- Analyze quality metrics: identify use cases with high error rates, low satisfaction, or drift from baseline
- Prompt optimization: systematic improvement of prompts based on evaluation data; all prompt changes flow through the [GenAIOps](#genaiops-vs-mlops) promotion pipeline (eval-gated, versioned, rollback-capable)
- Cost optimization: apply the detailed [Cost Optimization Levers](#cost-optimization-levers-detailed), prioritizing prompt caching, model tier routing, and agent workflow cost controls
- Model upgrade evaluation: assess newer or alternative models against established evals before switching
- Retire underperforming use cases: apply a structured review to discontinue AI integrations that are not delivering value
- A/B testing infrastructure: compare prompt variants, model versions, or integration patterns
- Expand feedback loops: increase coverage of structured user feedback and human evaluation
- Benchmark against external standards: compare quality and safety metrics to industry benchmarks where available

**Optimization Levers:**

| Dimension | Optimization Action |
|---|---|
| Output quality | Prompt refinement, retrieval improvement, fine-tuning consideration |
| Latency | Model tier selection, streaming, caching, async patterns |
| Cost | See detailed cost optimization levers below |
| Safety | Tighten output filtering, add input validation, reduce agent action scope |
| Adoption | UX improvements, workflow integration, friction reduction |

#### Cost Optimization Levers (Detailed)

AI costs behave unlike traditional cloud costs: they scale with *content* (tokens in and out) rather than compute time, they compound in agent workflows (a single user request can fan out to dozens of model calls), and they change materially with prompt design and model selection. Surface-level "use a cheaper model" advice leaves most savings on the table. Apply these levers in order of leverage:

| Lever | Action | When It Applies |
|---|---|---|
| **Prompt cost engineering** | Shorten system prompts, remove redundant few-shot examples, compress or summarize context before it enters the prompt | Any production use case; high leverage when prompts are verbose or shared across many calls |
| **Prompt caching** | Use provider prompt cache for stable prefixes (system prompts, reusable context); structure prompts so cacheable content is prefix-stable | Any use case with a shared system prompt or repeated large context |
| **Semantic response caching** | Cache final responses keyed by semantically similar inputs for deterministic, non-personal queries | FAQ, doc-lookup, and similar patterns with repetitive user intent |
| **Model tier routing** | Route simple tasks to smaller/cheaper models; reserve flagship models for hard tasks; use a classifier or router to decide | Mixed-difficulty workloads; high leverage when most traffic is easy |
| **Context window management** | Retrieve only what is needed; trim or re-rank before inclusion; bound max context length | RAG use cases where retrieval is unconstrained |
| **Retrieval-k tuning** | Tune the number of retrieved chunks against eval outcomes; more is not better and costs linearly | Every RAG use case |
| **Vector store cost tuning** | Dimension reduction, index pruning, cold-tier storage for rarely-queried corpora | Large or growing knowledge bases |
| **Batch and async APIs** | Move non-latency-sensitive work (overnight summarization, backfills, evals) to batch APIs at provider discount | Any non-interactive workload |
| **Agent workflow cost controls** | Set step limits, per-task token ceilings, self-evaluation gates, and early-exit conditions. Agent cost amplification is the largest single risk: a loop or poor tool choice can 10–100× the cost of a direct call | Every agentic use case; non-negotiable for Tier 3/4 |
| **Streaming for abandonment recovery** | Stream output so users can cancel long generations they no longer need | Interactive UI use cases |
| **Budget guardrails** | Per-user, per-team, and per-use-case token ceilings enforced at the gateway with throttle or alert behavior before spend incidents become cost incidents | All production deployments |

**Agent cost amplification, specifically:** An autonomous agent making five reasoning steps, each with retrieval and tool use, can cost 20–50× a single direct call to the same model for the same user intent. This is the most common source of unexpected AI cost blowouts. Every agentic use case must have a per-task cost budget enforced technically, not just monitored in dashboards after the fact.

**Outputs:**
- AI use case performance reports (quality, cost, adoption, business impact)
- Updated prompt library with versioned improvements
- Model selection decisions with supporting evidence
- Retired use case list with rationale

---

### Phase 6: Scale & Innovate

**Goal:** Extend AI adoption across the organization, enable teams to build new AI capabilities with guardrails, and explore next-generation patterns like autonomous agents and AI-native workflows.

**Key Activities:**
- Self-service AI platform: enable teams to build and deploy AI integrations within pre-approved guardrails without central team bottlenecks. By this phase, the CoE should be operating at the Platform / Self-service stage of the [CoE Evolution model](#ai-center-of-excellence-operating-model-evolution)
- Agent framework adoption: structured approach to deploying AI agents with defined action scopes, escalation paths, and audit trails. Every agent is registered as an [Agent or System Persona](#non-human-actors-agent-and-system-personas) with its own principal, scope, and named human owner. Agentic deployment is a *graduation*, not a starting point: a use case must have demonstrated reliability at the Automate or Augment stage before progressing to Agentic (see Use Case Maturity Progression)
- AI-native workflow design: redesigning processes around AI capabilities, not just adding AI to existing processes
- Cross-functional AI communities of practice: knowledge sharing, prompt libraries, eval frameworks shared across teams (see [Access & Reuse](#4-data--knowledge-perspective))
- Innovation pipeline: structured process for teams to propose, prototype, and validate new AI use cases
- External AI product features: embedding AI into customer-facing products with appropriate transparency and consent
- AI strategy refresh: periodic review of the AI opportunity landscape, competitive positioning, and framework evolution

**Agentic AI Adoption Criteria:**

Before deploying AI agents that take autonomous actions, the following must be true:

- [ ] Use case has operated successfully at the Automate or Augment stage with documented reliability evidence
- [ ] Target workflow is documented as an SOP with decision points, exceptions, and handoffs mapped
- [ ] Scope of permitted actions explicitly defined and technically enforced
- [ ] All agent actions logged with full audit trail
- [ ] Human escalation trigger defined (confidence threshold, action type, cost threshold)
- [ ] Rollback or undo mechanism exists for reversible actions
- [ ] Blast radius of worst-case failure is understood and acceptable
- [ ] Red-team exercise completed against the agent's action surface
- [ ] Named human owner accountable for agent behavior

**Outputs:**
- Self-service AI platform available to development teams
- Active AI community of practice
- Innovation pipeline with quarterly review
- Agentic AI use cases deployed with full governance artifacts

---

## AI Maturity Model

Organizations progress through four maturity levels. Assess each of the seven perspectives independently; it is common to be at Level 3 in Platform while still at Level 1 in Governance.

| Level | Name | Characteristics |
|---|---|---|
| **1: Exploring** | Uncoordinated | Individual employees using personal or trial AI accounts. No organizational policy. No data governance for AI. Value is anecdotal. Shadow AI prevalent. |
| **2: Piloting** | Emerging | Sanctioned pilots underway. Basic AI policy published. A small team owns AI governance. Use cases are internal and low-risk. Quality measured informally. |
| **3: Scaling** | Governed | AI governance body active. Approved tool registry maintained. Data boundaries enforced. Quality measured systematically. Use cases span multiple business units. Cost tracked and allocated. |
| **4: Transforming** | AI-native | AI embedded in core workflows and products. Self-service platform for teams. Autonomous agents deployed with full governance. AI strategy directly tied to business strategy. Continuous evaluation and improvement as steady state. |

### Maturity by Perspective

Use this grid to assess your current state and set targets per perspective:

| Perspective | Level 1: Exploring | Level 2: Piloting | Level 3: Scaling | Level 4: Transforming |
|---|---|---|---|---|
| **Business Value** | No use case tracking | Pilot ROI tracked informally | Use case portfolio managed | AI drives strategic differentiation |
| **People & Workforce** | No AI training | Ad-hoc training for power users | Role-based training programs | AI fluency is a hiring and performance standard |
| **Governance & Risk** | No AI policy | Basic acceptable use policy | Full AIIA process, vendor risk reviews | Automated compliance, regulatory proactive engagement |
| **Data & Knowledge** | No classification for AI; ad-hoc grounding sources | Basic data classification; pilot RAG indexes owned per team | Governed grounding/training split; shared prompt, eval, and index catalogs | Knowledge assets versioned and reused as strategic capability; lineage end-to-end |
| **Platform & Integration** | Direct API usage, no gateway | Shared API key management | Centralized AI gateway with logging | Self-service platform with guardrails |
| **Security & Trust** | No AI-specific controls | Data handling guidelines | Prompt security, output filtering | Red-teaming cadence, agent action enforcement |
| **Operations & Quality** | No quality measurement | Manual quality spot-checks | Automated evals, feedback loops | Continuous improvement as a core process |

### AI Center of Excellence: Operating Model Evolution

As maturity increases, the central AI team's role *must change*. A team that remains in gatekeeper mode at Level 4 becomes a bottleneck that the organization will route around, recreating the shadow-AI problem the CoE was stood up to solve. A team that jumps to self-service before guardrails are platformized leaves policy enforcement to goodwill. Plan the evolution deliberately:

| Stage | Maturity Range | CoE Role | Primary Activities | Failure Signal |
|---|---|---|---|---|
| **Gatekeeper** | Levels 1 → 2 | Central approval authority | Review each use case by hand, source tools, publish policy, block unsanctioned usage, stand up first pilots | High friction is acceptable here; if teams are not waiting on you, it means unsanctioned work is routing around |
| **Enabler / Advisor** | Level 3 | Consultant and accelerator | Provide templates (AIIA, prompts, evals), run clinics, embed advisors into high-value programs, publish reusable patterns, curate the approved tool registry | Queue depth growing; the central team's advisory hours are the bottleneck |
| **Platform / Self-service** | Level 4 | Platform owner | Operate the AI gateway, eval infra, prompt/eval/index catalog, and automated policy enforcement. Teams self-serve within guardrails; central team focuses on platform evolution, ecosystem curation, and horizon-scanning | Platform usage is high but quality or policy incidents are rising: guardrails are not keeping up with what teams can do |

**Design implication:** Every control the gatekeeper enforces by hand in Stage 1 is a candidate to be codified into platform automation by Stage 3. Anything that cannot be automated must be designed as a lightweight self-attestation with sample-audit, not a synchronous review. If your Stage 3 controls still require a human-in-the-loop for every use case, you are not at Stage 3.

**Warning:** Governance maturity is the strongest predictor of overall AI readiness. Organizations consistently over-invest in Platform while under-investing in Governance, then discover they cannot safely use what they built. Advance Governance & Risk at least in lockstep with Platform & Integration; if anything, lead with Governance.

---

## Use Case Classification

Not all AI use cases carry the same value or risk. Classify every use case before deployment to determine the appropriate level of governance, testing, and oversight.

### Five Use Case Categories

| Category | Description | Examples |
|---|---|---|
| **Augmentation** | AI enhances a human's own work; human produces and owns the output | Writing assistance, summarization, research support, code completion |
| **Analysis** | AI processes large volumes of data to surface insights; human interprets and acts | Contract review, sentiment analysis, log analysis, document classification |
| **Generation** | AI creates new artifacts that humans review and approve before use | Code generation, report drafting, image/asset creation, test case writing |
| **Automation** | AI handles a defined, repeatable task end-to-end with human oversight of outcomes | Ticket routing, data extraction, email triage, scheduled reporting |
| **Agency** | AI agents take multi-step actions using tools, with defined autonomy boundaries | Autonomous coding agents, research agents, workflow orchestration, customer-facing AI |

### Risk Tier Classification

Every AI use case must be assigned a risk tier before deployment. The tier determines required governance controls.

| Tier | Risk Level | Trigger Criteria | Required Controls |
|---|---|---|---|
| **Tier 1: Low** | Minimal | Internal use only. No sensitive data. Human reviews all outputs before any action. Easily reversible. | Acceptable use policy. Basic training. |
| **Tier 2: Medium** | Moderate | Involves confidential or sensitive internal data. Outputs influence (but don't drive) decisions. Customer-facing with human review. | AI Impact Assessment. Data classification review. Prompt security review. Logging enabled. |
| **Tier 3: High** | Significant | Consequential decisions affecting people (HR, finance, legal, clinical). Regulated data. Outputs drive automated actions. | Full AIIA. Legal review. Executive approval. Bias audit. Mandatory human review before action. Quarterly review cycle. |
| **Tier 4: Critical** | Severe | Fully autonomous actions with real-world consequences. Irreversible or high-blast-radius outcomes. External-facing agents. | Extensive red-teaming. Narrow action scope enforced technically. Board-level awareness. Continuous monitoring. Incident response plan specific to use case. |

### Use Case Classification Matrix

Plot use cases on this 2x2 to guide initial tier assignment:

```
High Value │  Tier 2 / Tier 3        │  Tier 3 / Tier 4
           │  (Govern carefully,     │  (Highest scrutiny --
           │   automate with review) │   strategic and risky)
           │─────────────────────────│────────────────────────
Low Value  │  Tier 1                 │  Tier 2 / Tier 3
           │  (Start here, build     │  (Reconsider if the
           │   confidence)           │   value justifies risk)
           └─────────────────────────┴────────────────────────
                    Low Risk                 High Risk
```

### Reference Scenarios (Canonical Patterns)

Most AI initiatives in most organizations resolve to a small number of recurring patterns. Starting from a canonical pattern beats starting from a blank page: the category, tier, and dominant concerns are predictable. Use this library as a shortcut during Phase 1 use-case triage. Adapt from the nearest pattern rather than classifying from first principles, and document deviations in the AIIA.

| Scenario | Typical Category | Typical Tier | Dominant Perspectives | Common Pitfalls |
|---|---|---|---|---|
| **Knowledge Assistant (internal RAG)** — employees ask natural-language questions over corporate docs, policies, and wikis | Augmentation / Analysis | Tier 2 | Data & Knowledge (grounding corpus), Security & Trust (access scoping), Operations & Quality (retrieval evals) | Corpus drift; cross-user data leaks when retrieval ignores source permissions; confident answers from low-confidence retrieval |
| **Developer Coding Assistant** — IDE-embedded AI for completion, refactoring, test generation, shell actions | Augmentation / Generation | Tier 2 (escalates to Tier 3 when given repo-wide agentic actions) | People & Workforce (skills, review practice), Security & Trust (IP and secrets leakage, supply chain), Data & Knowledge (prompt library, eval set) | Secrets in prompts; hallucinated APIs; over-reliance without review; license contamination from generated code |
| **Document Analysis & Extraction** — batch summarization, extraction, classification over long documents (contracts, claims, forms) | Analysis | Tier 2–3 (rises with decision consequence) | Data & Knowledge (provenance, lineage), Governance & Risk (AIIA, bias), Operations & Quality (structured-output evals) | Silent extraction errors at scale; drift when document formats change; no human sampling plan for downstream validation |
| **Customer Support Copilot** — AI assists a human support agent with suggested replies, policy lookup, case summarization | Augmentation | Tier 2 | People & Workforce (agent workflow redesign), Operations & Quality (customer-outcome metrics), Security & Trust (PII handling) | Measuring AI output quality instead of resolved-customer outcomes; suggestions subtly overriding agent judgment over time |
| **Customer-Facing Conversational AI** — external chatbot or assistant for prospects and customers | Generation / Analysis | Tier 3 | Governance & Risk (disclosure, liability), Security & Trust (prompt injection, jailbreak), Data & Knowledge (grounding scope) | Hallucinated commitments creating legal exposure; attackers using the bot as an exfiltration channel; absent kill switch |
| **Meeting Intelligence** — transcription, summarization, action-item extraction, retrieval across meeting archives | Automation / Analysis | Tier 2 (Tier 3 when content is sensitive: legal, clinical, M&A, HR) | Governance & Risk (consent, recording law), Data & Knowledge (retention), Security & Trust (cross-meeting search permissions) | Consent gaps across jurisdictions; indexing privileged conversations; default-public transcripts |
| **Agentic Workflow Automation** — AI agent takes multi-step actions using tools (ticket triage, incident triage, data ops) | Agency / Automation | Tier 3–4 | All seven, especially Security & Trust (excessive agency), Operations & Quality (cost amplification), Governance & Risk (Decision Register) | Starting here before Automate/Augment graduation; unbounded step loops; missing rollback; audit-trail gaps |
| **AI-Embedded Product Feature** — customer-facing AI inside an existing product (generation, personalization, smart search) | Generation / Analysis | Tier 2–3 | Business Value (strategic fit), Governance & Risk (disclosure, regulated outputs), Operations & Quality (product-grade SLAs) | Treated as a feature launch rather than a governed AI use case; no rollback path; provider outages become product outages |

**Using the library:**
- In Phase 1, match each candidate use case to the nearest pattern and inherit its classification as a starting point.
- Adjust the tier upward based on data sensitivity, decision consequence, or external exposure; adjust downward only with justification documented in the AIIA.
- The list is non-exhaustive. When your organization deploys a pattern not listed, capture it here so the next team inherits the learnings rather than rediscovering them.

### Use Case Prioritization Rubric

The 2x2 Matrix above is adequate for rough triage but insufficient for ranking a backlog of 30 candidate use cases or defending investment decisions to a steering committee. When rigor is needed, score each candidate along six weighted dimensions. The weights below are defaults; adjust to reflect your organization's priorities (regulated industries may weight risk higher; growth-stage companies may weight time-to-value higher).

| Dimension | Weight | Score 1 | Score 3 | Score 5 |
|---|---|---|---|---|
| **Business value** | 25% | Marginal or hard-to-quantify impact | Measurable productivity gain or cost avoidance for a defined group | Material revenue uplift, cost reduction, or strategic capability with executive sponsorship |
| **Data readiness** | 20% | Data is scattered, unclassified, or missing; heavy prep required | Data exists but needs classification, cleansing, or access work | Classified, governed, accessible data already flows to the right place |
| **Risk inverted** | 20% | Tier 3/4: regulated, consequential, or external-facing | Tier 2: internal sensitive data; human review mandatory | Tier 1: internal, non-sensitive, reversible |
| **Technical feasibility** | 15% | Capability gap; research required; integration complexity high | Proven pattern exists; modest integration work | Off-the-shelf tools solve this; integration is days, not months |
| **Strategic fit** | 10% | Tactical; does not advance stated AI strategy or differentiators | Aligned with a strategic theme | Advances a named strategic differentiator or builds a reusable capability |
| **Time to value** | 10% | 6+ months to realized value | 3–6 months | Under 90 days |

**How to use:**

1. Score each dimension 1–5 using the anchors above; anchors reduce inter-rater variance.
2. Multiply by weight, sum for a composite score (max 5.0).
3. Rank the backlog. Discuss the top decile and the cut line, not the absolute numbers.
4. Rescore annually or when material facts change (data becomes available, risk tier changes, strategy shifts).

**Why risk is inverted in this rubric:** Lower risk scores higher because this tool favors execution speed and confidence-building early in maturity. A Tier 3 use case with very high business value may still rank lower than a Tier 1 quick win, which is often *correct* at Levels 1–2. This rubric is a *prioritization* tool, not a risk tool; it does not replace the AIIA process or excuse high-risk use cases from full governance. As maturity increases, strategic use cases that score lower here should still be pursued with eyes open, funded as multi-year investments rather than quick wins.

**Common failure modes:**

- **Scoring on enthusiasm, not evidence.** Anchor scores to observable facts (data exists, users identified, model available), not stakeholder excitement.
- **Mistaking activity for value.** "AI-powered" is not a value proposition; the business outcome is.
- **Under-scoring data readiness.** The most common single reason pilots stall; do not round up because the team is confident.
- **Rescoring to fit a preferred answer.** If a pet project does not rank, the answer is to improve the project, not to rewrite the weights.

### Use Case Maturity Progression

The five categories above classify *what AI does*. The maturity progression below guides *how a use case should evolve over time*. The sequence matters.

**Stage 1, Automate:** Start here. Identify workflows (or steps within workflows) where AI can handle the task end-to-end without human judgment. These are typically thin work (repetitive, rule-based, low-ambiguity tasks). Automating thin work first delivers quick wins and builds organizational confidence.

**Stage 2, Augment:** Where full automation is not possible because the workflow requires human judgment at decision points, augment instead. AI handles the heavy lifting (research, drafting, analysis, preparation); the human makes the judgment call. The human's role shifts from *doing the work* to *overseeing the work*.

**Stage 3, Agentic:** When an automated or augmented workflow has proven reliable over time and the human decision point is no longer adding value, the workflow may graduate to agentic. AI operates independently within defined governance boundaries. **Do not start here.** Agentic deployment requires demonstrated automation reliability, established governance, and the full checklist in Phase 6.

**Why the sequence matters:** Each stage builds the evidence, governance muscle, and organizational trust required for the next. An organization that jumps to agentic without first proving automation reliability will lack the monitoring, override mechanisms, and cultural readiness to manage autonomous AI safely. Courts, regulators, insurers, and boards will still look for accountable people, not autonomous software.

**The leadership transition:** As workflows progress through these stages, people leaders must be prepared for a fundamental shift. Managing a team that *does work* is different from managing a team that *directs AI that does work*. If leaders have not been developed for this transition, the progression from augmented to agentic will fail, not because the technology isn't ready, but because the management layer isn't.

---

## Responsible AI Model

Responsible AI is not a checklist; it is an ongoing practice embedded in how the organization designs, deploys, and reviews AI systems.

### Six Responsible AI Principles

| Principle | Definition | Operationalized By |
|---|---|---|
| **Fairness** | AI systems do not produce systematically biased outcomes against identifiable groups | Bias audits, diverse evaluation datasets, outcome monitoring by demographic |
| **Reliability** | AI systems behave consistently and safely within their defined scope | Eval frameworks, regression testing, confidence thresholds |
| **Privacy** | AI systems handle personal data in compliance with applicable law and user expectations | Data classification enforcement, PII detection in prompts and outputs, minimization |
| **Transparency** | Users know when they are interacting with AI and understand its limitations | AI disclosure labels, uncertainty communication, explainability where required |
| **Accountability** | Every AI output that influences a decision has a named human owner | RACI per use case, audit trails, human-in-the-loop for high-risk tiers |
| **Inclusiveness** | AI tools are accessible and useful to all relevant employees, not just technical staff | Accessibility standards, multilingual support, UX design for diverse users |

### Measurable RAI Goals (Evidence Requirements)

Principles alone are not auditable. Each principle decomposes into concrete goals with required evidence artifacts. For Tier 2+ use cases, the AIIA must show that each applicable goal is met before approval, and the governance body audits the evidence on the review cadence.

| Principle | Measurable Goal | Required Evidence |
|---|---|---|
| **Fairness** | Evaluation datasets represent affected populations | Documented eval set composition with demographic coverage rationale |
| **Fairness** | Outcome disparities are monitored for use cases affecting people | Disaggregated metrics dashboard (or documented rationale if not applicable) |
| **Fairness** | Disparities trigger remediation, not just reporting | Bias remediation playbook with defined thresholds and owners |
| **Reliability** | Quality thresholds are defined *before* deployment | Quantitative acceptance criteria in the AIIA, signed off by the use case owner |
| **Reliability** | Changes cannot silently regress quality | Regression test suite against a golden eval set, gating model and prompt changes |
| **Reliability** | Quality degradation in production is detected and resolved | Incident runbook for quality incidents with MTTD/MTTR targets |
| **Privacy** | Data classification is enforced, not just declared | AI gateway policies blocking or redacting disallowed data classes, with logged events |
| **Privacy** | PII is detected in both prompts and outputs | PII detection results logged, alerted on, and reviewed |
| **Privacy** | Retention and deletion are governed | Documented retention schedule for prompts, completions, and retrieved context, with technical enforcement |
| **Transparency** | Users know when they are interacting with AI | Disclosure standard applied to every AI surface (UI label, API header, document footer) |
| **Transparency** | Users understand the system's identity and limits | Model card or use case card published: model/version, intended use, known limitations, contact |
| **Transparency** | Uncertainty is communicated where it matters | Confidence or caveat signaling on Tier 2+ outputs that influence decisions |
| **Accountability** | Every consequential AI output has a named human owner | Entry in the AI Decision Register with owner, scope, and guardrails |
| **Accountability** | Actions are auditable end-to-end | Audit trail capturing prompts, retrieved context, outputs, and human decisions for Tier 2+ |
| **Accountability** | Humans can intervene | Documented escalation, override, and kill-switch procedure, tested at deployment and annually (Tier 3/4) |
| **Inclusiveness** | AI surfaces are accessible | WCAG 2.2 AA conformance (or sector equivalent) evidenced for AI-touched UI |
| **Inclusiveness** | AI works for the user population | Language, locale, and accessibility coverage matches the user base, with gaps documented |
| **Inclusiveness** | Feedback reaches the team | Accessible feedback channel with published response SLA and surfaced response rate |

**Applying the goals:** Not every goal applies to every use case; the AIIA captures applicability and justifies exclusions. The goals replace generic "we care about fairness" statements with specific artifacts a reviewer can check. If an applicable goal has no evidence, the use case is not ready to deploy.

### AI Impact Assessment (AIIA) Process

An AIIA is required for all Tier 2, 3, and 4 use cases before deployment.

**Step 1: Use Case Description**
- What problem is being solved?
- Who are the users and who is affected by outputs?
- What data is processed?
- What actions or decisions does the output influence?

**Step 2: Risk Identification**
- Accuracy risks: What happens if the AI is wrong?
- Bias risks: Are there identifiable groups who could be unfairly affected?
- Privacy risks: What sensitive data is involved, and how is it handled?
- Security risks: What attack vectors exist?
- Operational risks: What happens if the AI is unavailable?

**Step 3: Mitigation Design**
- What controls reduce each identified risk to acceptable levels?
- What is the human review or override mechanism?
- What monitoring will detect if risks materialize post-deployment?

**Step 4: Approval**
- Risk tier confirmed
- Required approvers sign off (per tier)
- Review cadence scheduled

**Step 5: Ongoing Review**
- Scheduled reassessment (quarterly for Tier 3/4, annually for Tier 2)
- Triggered reassessment if: use case scope changes, model is upgraded, incident occurs, or regulation changes

### Human-in-the-Loop Requirements

| Risk Tier | Human Review Requirement |
|---|---|
| Tier 1 | User reviews output before acting; no system requirement |
| Tier 2 | Process design must include human review step; outputs are advisory |
| Tier 3 | Mandatory human approval before any consequential action; human identity and decision logged |
| Tier 4 | Human operator must explicitly authorize each autonomous action sequence; kill switch accessible |

---

## AI Shared Responsibility Model

Unlike traditional software, AI systems involve a three-party responsibility model: the **AI model provider**, the **AI platform layer** (which may be your organization or a middleware vendor), and the **AI application consumer** (your organization's team or product).

| Responsibility Area | Model Provider | Platform / Gateway Layer | Application Consumer |
|---|---|---|---|
| Model safety and alignment | Owner | - |: |
| Model accuracy and capability | Owner | - | Prompt design influence |
| API availability and uptime | Owner | Partially | Fallback design |
| Data sent in prompts | - | Policy enforcement | Owner |
| Output filtering (post-processing) | Partially | Can implement | Can implement |
| Identity and access to AI APIs | - | Owner | User-level controls |
| Audit logging of interactions | - | Owner | Owner (for regulated use) |
| Prompt injection defense | Partially | Can implement | Owner |
| Data residency and sovereignty | Owner (by region) | Routing policy | Configuration |
| Regulatory compliance for use | - |: | Owner |
| User disclosure (AI transparency) | - |: | Owner |
| Business outcomes of AI use | - |: | Owner |

**Key implication:** The AI provider is responsible for the model; your organization is responsible for what you do with it.

---

## Roles & Responsibilities

### Core AI Program Roles

| Role | Perspective Owner | Primary Responsibilities |
|---|---|---|
| **AI Executive Sponsor** | Business Value | Champions AI program, removes blockers, owns business case, represents AI at board level |
| **AI Program Lead** | Governance & Risk | End-to-end program accountability, use case portfolio management, stakeholder reporting |
| **AI Ethics / Responsible AI Officer** | Governance & Risk | AIIA process ownership, bias review, regulatory compliance, policy governance |
| **Chief Data Officer (or equivalent)** | Data & Knowledge | Executive accountability for grounding and training data governance, classification policy, and knowledge asset strategy |
| **Data Steward (AI)** | Data & Knowledge | Data classification for AI, PII governance, approved data set management, grounding corpus ownership |
| **Knowledge / Prompt Librarian** | Data & Knowledge | Prompt library curation, eval dataset catalog, retrieval index registry, cross-team reuse enablement |
| **AI Platform Engineer** | Platform & Integration | AI gateway, API management, RAG runtime infrastructure, eval infrastructure, developer platform |
| **AI Security Engineer** | Security & Trust | Prompt security controls, output filtering, AI incident response, vendor security reviews |
| **AI Quality / Eval Engineer** | Operations & Quality | Evaluation frameworks, quality metrics, feedback loop infrastructure, regression testing |
| **AI Operations Lead** | Operations & Quality | Token cost management, observability, model version management, AI service catalog |
| **Prompt Engineer / AI Practitioner** | Platform & Integration | Prompt design, optimization, testing, and documentation for production use cases |
| **Business AI Champion** | Business Value | Use case identification and advocacy within a business unit, user adoption enablement |
| **Change Manager** | People & Workforce | Workforce impact assessments, communication planning, training coordination |
| **L&D Lead** | People & Workforce | AI literacy curriculum, role-specific training programs, skill gap closure |

### RACI Template (per Use Case Deployment)

| Activity | AI Exec Sponsor | AI Program Lead | AI Ethics Officer | Data Steward | AI Platform Eng | AI Security Eng | Business AI Champion |
|---|---|---|---|---|---|---|---|
| Business case approval | **A** | R | C | I | I | I | R |
| AI Impact Assessment | I | C | **A/R** | C | C | C | R |
| Data classification & grounding corpus approval | I | C | C | **A/R** | R | C | C |
| Training / fine-tuning data approval | I | C | R | **A/R** | C | C | I |
| Prompt / eval asset publication | I | C | I | **A** | R | I | R |
| Platform / integration build | I | I | I | C | **A/R** | C | I |
| Security review | I | C | C | C | C | **A/R** | I |
| User training & rollout | I | C | I | I | I | I | **A/R** |
| Quality monitoring | I | **A** | C | C | R | C | C |
| Cost governance | C | **A** | I | I | R | I | I |
| Incident response | I | **A** | C | C | R | R | C |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## Non-Human Actors: Agent and System Personas

Traditional IAM assumes every identity in the system belongs to a human. Agentic AI breaks that assumption. An AI agent that reads tickets, calls APIs, commits code, and emails customers is an *actor* in your systems with its own identity, scope, audit trail, and accountability chain. Treating an agent as an extension of the human who launched it (a prompt in a form field) collapses at the first audit, the first incident, and the first regulated environment.

Define each non-human persona with the same rigor as a human role:

| Persona | Description | Identity & Access | Audit & Accountability |
|---|---|---|---|
| **Interactive AI Assistant** | AI that responds to a human user in real time; actions are attributed to the human in session | User identity propagates to all downstream calls; AI inherits the user's permissions, nothing more | Log records human identity, prompt, and AI response; AI is not a principal |
| **Scoped Agent** | AI operating within a bounded task on behalf of a human (e.g., "triage this ticket", "draft this brief") | Human-delegated, time-bound, least-privilege credential, separate from the human's general identity | Log records delegating human + agent principal ID + each action; kill switch accessible to the delegating human |
| **Service Agent** | AI running on schedule or in response to events, no human in session (e.g., nightly report generator, queue processor) | Dedicated service principal with explicit allowed actions, resources, and data scope | Log records the agent principal; named human owner is accountable; alerts route to that owner |
| **Multi-Agent System** | Multiple cooperating agents, each with a distinct role and scope | Each agent has its own principal and permissions; inter-agent calls are logged as peer-to-peer, not collapsed into a single "AI" identity | Audit trail captures the full agent graph; escalation path defined per agent; single named human owner for the system |
| **Tool-Using Agent** | Agent calls external tools or APIs (search, email, code execution, ticket creation) | Each tool connector is explicitly allow-listed with per-tool scope; destructive tools require higher authorization or per-action human confirmation | Per-tool logging of inputs, outputs, and effects; per-invocation cost budget enforced |

**Design implications:**

- **Every non-human persona has a named human owner.** The human does not perform the action but is accountable for the agent's behavior. The Decision Register captures this mapping.
- **Agents do not share identities.** Resist the temptation to give "the AI" one God-account. Each persona gets its own principal so audit logs remain legible.
- **Permissions are explicit, not inherited for convenience.** A scoped agent launched by an admin should have its own narrow scope, not the admin's full permissions.
- **Destructive actions require graduated authorization.** Read-only is default; writes require scope; destructive actions require per-action confirmation or a narrow allow-list.
- **Persona lifecycle is governed.** Agents are created, reviewed, updated, and retired with the same discipline as user accounts. Orphaned agent identities are a security and compliance risk.
- **Inherited user consent does not extend to agents.** If a human consented to AI-assisted summarization, that is not consent for an autonomous agent to email their contacts on their behalf.

---

## Success Metrics & KPIs

Track metrics across four outcome categories. Establish baselines before deployment so you can measure change.

### Business Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Productivity uplift | Time saved per user per week on AI-assisted tasks | 2–5 hours/week/user (use-case dependent) |
| Time-to-output | Speed improvement on targeted workflows | 30–60% reduction |
| Use case ROI | Return on investment per active use case | Positive within 6 months for Tier 1/2 |
| AI-influenced revenue | Revenue attributable to AI-enabled products or decisions | Tracked and growing |
| Cost avoidance | Reduction in outsourced or manual processing costs | Tracked per use case |

### Adoption Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Active user rate | % of target users actively using AI tools (weekly) | > 70% within 6 months of rollout |
| Use case activation rate | % of planned use cases live vs. in backlog | > 60% of backlog active within 12 months |
| Shadow AI reduction | % reduction in unsanctioned AI tool usage | Trending toward zero |
| Training completion | % of target employees completing role-appropriate AI training | > 90% |
| Net Promoter Score (AI) | User satisfaction with AI tools | > 30 NPS |

### Quality & Safety Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Output accuracy rate | % of AI outputs rated correct/useful by users or evals | > 85% (use-case dependent) |
| Hallucination / error rate | % of AI outputs containing factual errors in monitored samples | < 5% for Tier 2+; < 1% for Tier 3/4 |
| Policy violation rate | AI interactions that triggered data or content policy violations | Trending toward zero |
| AIIA completion rate | % of Tier 2+ use cases with a completed and current AIIA | 100% |
| Incident rate | AI-related security or quality incidents per quarter | Zero critical incidents |
| Human override rate | % of AI outputs where human exercised override (Tier 3/4) | Tracked; sustained high rate may indicate poor AI quality |

### Operational Outcomes

| KPI | Description | Target Example |
|---|---|---|
| AI API availability | Uptime of AI services in production | > 99.5% |
| Mean time to detect (AI) | Time to detect AI quality degradation or security incident | < 24 hours |
| Token cost per task | Average token spend to complete a unit of AI-assisted work | Tracked and optimizing |
| Cost per active user | Monthly AI API cost per active user | Tracked against budget |
| Eval coverage | % of production AI use cases with automated quality evals | 100% for Tier 2+; 100% for all Tier 3/4 |

### Data & Knowledge Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Grounding corpus freshness | Median and P95 age of the top-N queried grounding sources | Within use-case SLO (e.g., policy docs < 30 days; legal < 7 days) |
| Prompt / eval / index reuse rate | % of new production use cases reusing at least one existing asset (prompt, eval set, retrieval index) rather than rebuilding | Trending up; > 50% at Level 3, > 75% at Level 4 |
| Data classification coverage for AI | % of data sources used in grounding or training with an authoritative classification | 100% of in-use sources |
| Retention policy adherence | % of AI interaction data (prompts, completions, retrieved context) meeting its retention policy | 100% |
| Cross-tenant retrieval leakage events | Count of events where retrieval returned data the requesting user should not see | Zero |

### GenAIOps & Agent Outcomes

| KPI | Description | Target Example |
|---|---|---|
| Prompt change lead time | Time from prompt PR opened to production rollout | Hours (high maturity); days (early) |
| Eval pass rate at promotion | % of prompt/model changes passing the golden-set eval threshold on first submission | > 80% (indicates good dev-time evaluation) |
| Index staleness SLO adherence | % of retrieval indexes refreshed within their defined SLO | > 95% |
| Model rollout cycle time | Time from new model availability to completed evaluation and rollout decision | < 30 days |
| Orphaned agent identities | Non-human principals with no active named human owner | Zero; any non-zero is an incident |
| Agent scope drift | Agents with permissions granted but not exercised in 90 days (candidates for scope reduction) | Reviewed quarterly; trend toward zero |
| Kill-switch verification freshness | % of Tier 3/4 agents with a verified kill-switch exercise in the last 90 days | 100% |
| Per-task agent cost ceiling breaches | Count of agentic tasks exceeding their per-task token budget | Near zero; each breach is a signal |

---

## Applying the Framework at Different Scales

The framework is written in enterprise voice: named committees, mandatory AIIAs, dedicated platform engineering. A 20-person startup cannot and should not staff that operating model. But the *risks* AI introduces do not shrink with headcount. The goal at small scale is not to skip governance; it is to execute the same controls at lower cost by collapsing roles, simplifying artifacts, and leaning on off-the-shelf tooling rather than building.

The dividing line is not headcount, it is whether dedicated people exist for each role. When one person wears ten hats, keep the hats but shorten the meetings.

### Startup / Small Team Overlay

| Element | Enterprise Default | Startup Overlay |
|---|---|---|
| **Governance body** | AI steering committee, working groups, separate AI Ethics Officer | One recurring 30-minute leadership review; CEO or CTO plays the Ethics Officer role explicitly |
| **AI Impact Assessment (AIIA)** | Multi-section document, formal legal review, quarterly reassessment | One-page AIIA with the same risk/mitigation questions; re-read on material change |
| **Approved tool registry** | Centrally curated catalog with vendor risk reviews | Short list (5–10 tools) in a shared doc, updated when something is added |
| **AI gateway** | Self-operated gateway with policy enforcement, logging, rate limiting | Hosted gateway or a provider with built-in policy controls; do not build your own |
| **RAG infrastructure** | Internal vector store, embedding pipelines, retrieval services | Managed vector DB and an off-the-shelf framework; avoid custom pipelines until scale forces them |
| **Prompt / eval / index registry** | Separate platformed registries with promotion gates | A shared repo with reviewed PRs and a golden-set spreadsheet; same discipline, lighter tooling |
| **Audit logging** | Immutable logs for all regulated use cases | Provider-native logging plus export to durable storage; same retention policy |
| **Red-teaming** | Dedicated red team on a scheduled cadence | Structured self-red-team checklist per use case; external pen test at Tier 3+ |
| **AI CoE** | Full CoE team evolving through gatekeeper → advisor → platform | One designated owner wearing the CoE hat; external advisor optional |
| **Training program** | Tiered role-based curriculum | A single onboarding module plus acceptable-use acknowledgment |
| **RACI** | Per-activity RACI across 7+ roles | Name the Accountable for each activity; Responsible is often the same person |

**What does NOT change at startup scale:**

- **Risk tiers.** Data sensitivity and decision consequence determine tier, not headcount.
- **Named human owner per use case.** The AI Decision Register is as important at 10 people as at 10,000.
- **Data classification enforcement.** Even if enforcement is manual, define what can and cannot go to external APIs and check.
- **Kill-switch and rollback for Tier 3/4.** An agent that can take destructive action must be stoppable regardless of company size.
- **Pilot-to-production gate.** A small team is *more* vulnerable to pilot death because operational slack is scarcer, not less.
- **OWASP LLM Top 10 assessment.** The threats do not know you are small.

**Graduation triggers.** Move each element from overlay to full framework mode when any of these occur: first regulated use case, first customer-facing AI surface, first agent with external write access, first AI-related incident, first material enterprise customer contract, or headcount crossing roughly 100–200. Each trigger applies to the specific element it touches, not to the whole framework at once.

---

## Quick Reference Summary

```
AI ADOPTION FRAMEWORK (AIAF)

  FOUR-LAYER STACK (Where does this question belong?)
  Responsible AI Foundation → Adoption Framework (AIAF) →
  Implementation Patterns → Runtime Operations

  SEVEN PERSPECTIVES (What we govern)
  ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
  │ Business │ People & │    AI    │  Data &  │    AI    │    AI    │    AI    │
  │  Value   │Workforce │Governance│Knowledge │ Platform │ Security │Operations│
  │          │          │  & Risk  │          │& Integr. │ & Trust  │ & Quality│
  └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

  SIX PHASES (How we progress) with pilot-to-production gate
  ┌──────────┐ ┌──────────┐ ╔══════╗ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
  │ DISCOVER │→│  PILOT   │→║ P2P  ║→│  DEPLOY  │→│  GOVERN  │→│ OPTIMIZE │→│  SCALE   │
  │  ASSESS  │ │ VALIDATE │ ║ GATE ║ │INTEGRATE │ │ CONTROL  │ │ MEASURE  │ │ INNOVATE │
  └──────────┘ └──────────┘ ╚══════╝ └──────────┘ └──────────┘ └──────────┘ └──────────┘

  FOUR MATURITY LEVELS
  1. Exploring → 2. Piloting → 3. Scaling → 4. Transforming

  COE OPERATING MODEL EVOLUTION (tracks maturity)
  Gatekeeper (L1-L2) → Enabler/Advisor (L3) → Platform/Self-service (L4)

  FIVE USE CASE CATEGORIES
  Augmentation | Analysis | Generation | Automation | Agency

  USE CASE MATURITY PROGRESSION (a graduation, not a starting point)
  Automate → Augment → Agentic

  FOUR RISK TIERS
  Tier 1 (Low) → Tier 2 (Medium) → Tier 3 (High) → Tier 4 (Critical)

  EIGHT REFERENCE SCENARIOS (canonical patterns for triage)
  Knowledge Assistant | Coding Assistant | Document Analysis |
  Support Copilot | Customer-Facing Chat | Meeting Intelligence |
  Agentic Workflow | Embedded Product AI

  SIX-DIMENSION PRIORITIZATION RUBRIC (default weights)
  Business Value (25%) | Data Readiness (20%) | Risk inverted (20%) |
  Feasibility (15%) | Strategic Fit (10%) | Time to Value (10%)

  SIX RESPONSIBLE AI PRINCIPLES → ~18 measurable, evidence-backed goals
  Fairness | Reliability | Privacy | Transparency | Accountability | Inclusiveness

  OWASP LLM TOP 10 (assessed at Tier 2+)
  Prompt Injection | Sensitive Info Disclosure | Supply Chain |
  Data/Model Poisoning | Improper Output Handling | Excessive Agency |
  System Prompt Leakage | Vector/Embedding Weaknesses |
  Misinformation | Unbounded Consumption

  FIVE AGENT & SYSTEM PERSONAS (non-human actors)
  Interactive Assistant | Scoped Agent | Service Agent |
  Multi-Agent System | Tool-Using Agent

  REGULATORY BASELINE
  EU AI Act (staged 2025-2027) | NIST AI RMF | ISO/IEC 42001 |
  GDPR/CCPA | HIPAA | Sector rules (FS, HC, HR, education, safety-critical)

  TWO SCALES OF APPLICATION
  Enterprise Default ↔ Startup Overlay (same risks, lighter artifacts)

  SIX OUTCOME CATEGORIES
  Business | Adoption | Quality & Safety | Operational |
  Data & Knowledge | GenAIOps & Agent
```

---

*Derived from the [Comprehensive Technology Adoption Framework (TAF)](TechAdoptionFramework.md), which is based on [AWS CAF](https://aws.amazon.com/cloud-adoption-framework/), [Google Cloud Adoption Framework](https://cloud.google.com/adoption-framework), and [Microsoft Azure CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/). AI-specific adaptations draw from the [Google Cloud AI Adoption Framework](https://services.google.com/fh/files/misc/ai_adoption_framework_whitepaper.pdf) (Data as a first-class dimension, Access & Reuse theme, CoE evolution), the [AWS CAF for AI](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html), [AWS GenAI Maturity Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/introduction.html), and [AWS Well-Architected GenAI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) (cost optimization depth, excessive-agency framing), the [Microsoft Cloud Adoption Framework for AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/) and [Responsible AI Standard v2](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf) (measurable RAI goals, grounding-vs-training data split, GenAIOps). Security risk taxonomy mapped to the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Elements of the Use Case Maturity Progression, thin work/valued work classification, AI Decision Register, and process documentation prerequisites were informed by the [GEM Blueprint](https://www.gemblueprint.com/) by Timothy J. Hitchens / Techshin Partners. Not affiliated or endorsed in any way with any of the referenced companies or authors.*
