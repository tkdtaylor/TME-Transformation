<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Contributing to TME Transformation Frameworks

Thank you for contributing to TME Transformation Frameworks. Improvements to the core frameworks, facilitated workshops, foundational CoE baselines, blank templates, worked examples, and regulatory references are welcome.

## Repository Architecture & Where Changes Belong

| Directory / File | Scope & What Belongs Here |
| :--- | :--- |
| [TechAdoptionFramework.md](TechAdoptionFramework.md) | Base Technology Adoption Framework (TAF) across six perspectives and six lifecycle phases |
| [AIAdoptionFramework.md](AIAdoptionFramework.md) | AI Adoption Framework (AIAF) specialization across seven perspectives, six phases, maturity model, Responsible AI, and OWASP LLM controls |
| [AIFoundationalSuite/](AIFoundationalSuite/README.md) | 15-document Center of Excellence (CoE) governance and operations starter kit (`00` through `14` plus `README.md`) |
| [Templates/](Templates/README.md) + [Templates/DataDictionary.md](Templates/DataDictionary.md) | Standalone blank Markdown judgment forms, CSV operational registers, and controlled vocabularies |
| [Examples/](Examples/InternalEmployeeLifecycleAssistant/README.md) | Complete worked single-use-case reference artifacts illustrating end-to-end AIAF application |
| [Workshops/](Workshops/BusinessReadinessAssessment.md) | Facilitated Business Readiness Assessment workshop and Facilitator Guide |
| [References.md](References.md) | Authoritative regulatory, standards, security, and framework references with review cadences |

## Authoring & Style Guidelines

1. **Vendor neutrality**: Keep guidance, templates, and architectures vendor-neutral across cloud providers, foundation models, identity providers, and SaaS platforms. Official vendor frameworks may be cited in [References.md](References.md) and attribution notes.
2. **Modern punctuation (no em-dashes)**: Do not use em-dashes, spaced double-hyphens, or spaced en-dashes in prose. Use colons, parentheses, periods, or explicit conjunctions instead.
3. **Deterministic formatting & anchor stability**: Format dates as `YYYY-MM-DD`, zero-pad sequential identifiers (`UC-001`, `ADR-001`, `TOOL-001`, `AIAF-DOC-01`), preserve Markdown heading slugs targeted by Table of Contents `#anchor` links, and keep [Templates/DataDictionary.md](Templates/DataDictionary.md) synchronized whenever CSV register columns change.
4. **Evidence-backed regulatory references**: Prefer primary regulator and standards-body URLs in [References.md](References.md), and include a `last reviewed` date whenever timelines or obligations are staged.

## License & Attribution

All contributions to this repository are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) license (`SPDX-License-Identifier: CC-BY-4.0`), attributed to `The TME-Transformation Authors`. Submissions must reflect independent, vendor-neutral guidance without proprietary, customer-specific, or employer-confidential material.
