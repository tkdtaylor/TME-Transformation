# Changelog

All notable changes to this project are recorded here.

The format is inspired by Keep a Changelog, using `YYYY-MM-DD` release dates and semantic versioning starting with `v1.0.0`.

## [1.0.0] - 2026-11-21

### Added

- Added the vendor-neutral [AI Foundational Suite](AIFoundationalSuite) (`00` through `14`): a 15-document Center of Excellence (CoE) governance and operations starter kit ordered chronologically across four execution tiers (Day-0 Guardrails, Wave-1 Enablement and Kill-Switch Safety, FinOps Seat Governance and Maturity, and Custom Agent Production Gates, OWASP LLM Controls, GenAIOps, and Vendor AI Procurement).
- Added a FinOps Foundation (`FinOps for AI`) reference entry in [References.md](References.md) for cloud AI financial governance and license reclamation.
- Added a `License & Disclaimer` section to [README.md](README.md).
- Added [CONTRIBUTING.md](CONTRIBUTING.md) covering repository scope, vendor-neutrality rules, modern punctuation, anchor stability, and CC BY 4.0 licensing, plus a standard [.gitignore](.gitignore).
- Added workshop-to-suite handoff mappings in [FacilitatorGuide.md](Workshops/FacilitatorGuide.md) and [BusinessReadinessAssessment.md](Workshops/BusinessReadinessAssessment.md), and linked pre-populated baselines and worked examples from [Templates/README.md](Templates/README.md).
- Added the [Program Delivery Kit](ProgramDelivery/README.md) (`01` through `04`) covering the executive kickoff outline, Day-0 readiness gates (`RDY-01` to `RDY-07`), `M0`-`M5` progression, bi-weekly health checks (`HC-01` to `HC-08`), 3-part Agent PRD template, and closeout / BAU warm handoff charter.
- Added a second worked example at [Examples/ApprovalGatedFinancialVarianceAgent](Examples/ApprovalGatedFinancialVarianceAgent/README.md) illustrating a Tier 3 read-only tool-using scoped agent with deterministic Python/SQL math, inline guardrail hooks, OWASP `LLM01`-`LLM10` controls, a tested kill switch, and completed CSV registers.
- Added standalone [Technology Adoption Framework](TechAdoptionFramework.md) templates: [WorkloadPortfolio7Rs.csv](Templates/WorkloadPortfolio7Rs.csv), [ArchitectureDecisionRecord.md](Templates/ArchitectureDecisionRecord.md), and [MigrationWaveReadinessGate.md](Templates/MigrationWaveReadinessGate.md), with schema definitions in [DataDictionary.md](Templates/DataDictionary.md).
- Added zero-dependency repository validation ([scripts/validate_repo.py](scripts/validate_repo.py)), MkDocs Material documentation staging and site configuration ([scripts/build_docs_src.py](scripts/build_docs_src.py) and [mkdocs.yml](mkdocs.yml)), GitHub community health files ([CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), issue template, PR template), and CI validation plus GitHub Pages deployment workflows (`.github/workflows/validate.yml` and `.github/workflows/docs.yml`).

### Changed

- Replaced the short summary deed in [LICENSE](LICENSE) with the full verbatim Creative Commons Attribution 4.0 International (`CC-BY-4.0`) legalcode so repository tooling detects the SPDX license identifier cleanly.
- Linked the [AI Foundational Suite](AIFoundationalSuite) from [README.md](README.md) and across Phases 1 through 6 and the Pilot-to-Production Gate in [AIAdoptionFramework.md](AIAdoptionFramework.md).
- Updated the EU AI Act staged implementation timeline (reflecting Aug 2026 Article 50 enforcement and Digital Omnibus on AI Regulation (EU) 2026/1744 high-risk compliance dates) and refreshed the `last reviewed` date in [AIAdoptionFramework.md](AIAdoptionFramework.md) and [References.md](References.md) to `2026-11-21`.
- Linked the new base TAF templates across Phases 2, 3, and Portfolio Rationalization in [TechAdoptionFramework.md](TechAdoptionFramework.md), and expanded [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md) with `ProgramDelivery/` and both Tier 2 and Tier 3 worked examples.
- Adopted semantic versioning (`v1.0.0`) in [CHANGELOG.md](CHANGELOG.md) and linked [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and local validation instructions from [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## 2026-05-15

### Added

- Added vendor-neutral templates for AI impact assessments, use case cards, pilot-to-production gates, decision registers, use case backlogs, and approved AI tool registries.
- Added a template data dictionary with CSV column definitions, conventions, and recommended controlled values.
- Added a worked example for an internal employee lifecycle assistant covering onboarding, role changes, and offboarding.
- Added source reference tracking with review cadences for regulatory, standards, security, and adoption-framework sources.
- Added a facilitator guide for running the AIAF-grounded Business Readiness Assessment workshop.

### Changed

- Reframed the Business Readiness Assessment as an AIAF-first workshop with optional TAF context, rather than a shared workshop for both frameworks.
- Updated EU AI Act wording to reflect staged obligations and mark implementation guidance as last reviewed on 2026-05-15.
- Refined Tier 4 risk language for external-facing agents with elevated action authority.
- Renamed the use case maturity progression to `Task Automation -> Human Augmentation -> Agentic Autonomy`.
- Clarified README descriptions of CoE evolution and RACI scope.
- Fixed fragile Markdown TOC anchors in the AIAF and TAF phase sections.

### Fixed

- Cleaned regulated-data examples in the workshop so examples describe data types rather than mixing laws, standards, and data categories.
