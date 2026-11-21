<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Security Policy

## Scope of This Repository

**TME Transformation Frameworks** provides vendor-neutral adoption frameworks, workshops, Center of Excellence (CoE) governance baselines, and operational templates for technology and AI transformation. It does not ship hosted services, runtime credentials, or production infrastructure.

In addition to documentation and CSV templates, the repository maintains small Python build and validation scripts under `scripts/` and automation workflows under `.github/workflows/`.

## Supported Versions

Security and control-guidance fixes are applied to the active `main` branch and included in subsequent tagged releases.

| Version / Branch | Supported | Notes |
| :--- | :---: | :--- |
| `1.0.x` (`main`) | Yes | Active maintenance and control updates |
| Older snapshots | No | Upgrade to the latest tagged release |

## What to Report

Please report either of the following issues:

1. **Security-control guidance defects**: Technical inaccuracies, unsafe defaults, or omissions in documented AI and cloud security guidance (for example, OWASP `LLM01`-`LLM10` mitigations, Zero Trust identity controls, data classification rules, or kill-switch containment runbooks).
2. **Tooling or CI workflow vulnerabilities**: Unsafe input handling, command injection, overly broad token permissions, or supply-chain risks in `scripts/` or `.github/workflows/`.

## How to Report

### Sensitive Workflow or Script Vulnerabilities (Private)

If you discover a vulnerability in `scripts/`, `mkdocs.yml`, or `.github/workflows/` that could expose repository automation or build integrity, do **not** open a public issue. Submit a confidential report via [GitHub Private Vulnerability Reporting](https://github.com/tkdtaylor/TME-Transformation/security/advisories/new) or contact the repository maintainer [@tkdtaylor](https://github.com/tkdtaylor) through GitHub.

### Security-Control Guidance Improvements (Public)

For non-sensitive improvements, regulatory alignment updates, or clarifications to documented security controls and runbooks, open an issue using the [Framework or Suite Improvement](https://github.com/tkdtaylor/TME-Transformation/issues/new?template=framework_improvement.md) template or submit a pull request.

## Response Expectations

Maintainers review private reports and control-guidance issues on a best-effort open-source basis, confirm scope with the reporter, and document validated fixes in [CHANGELOG.md](CHANGELOG.md).
