<!-- Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0). -->

# Migration Wave Readiness Gate

> Source template for [Technology Adoption Framework](../TechAdoptionFramework.md) Phase 3 wave cutover reviews. Pair with [WorkloadPortfolio7Rs.csv](WorkloadPortfolio7Rs.csv) and [DataDictionary.md](DataDictionary.md). Do not approve cutover until blocking evidence links point to verified artifacts.

## Wave Summary

| Field | Response |
| :--- | :--- |
| Wave ID | `Wave X` |
| Wave Name / Scope | |
| Target Cutover Window | `YYYY-MM-DD` to `YYYY-MM-DD` |
| Program / Wave Owner | |
| Technical / Migration Lead | |
| Security Reviewer | |
| Operations / SRE Owner | |
| Workloads Included | Reference `WKL-*` IDs from [WorkloadPortfolio7Rs.csv](WorkloadPortfolio7Rs.csv) |

## Readiness Checklist

| Readiness Area | Required Evidence | Status | Evidence / Link |
| :--- | :--- | :--- | :--- |
| Landing Zone & IaC | Target platform foundation, network topology, tenancy boundaries, and IaC drift checks verified | Not started / In progress / Ready | |
| Zero Trust IAM & Network Segmentation | Explicit identity auth, least-privilege / JIT roles, network segmentation, and encryption verified | Not started / In progress / Ready | |
| Data Backup & RTO/RPO Rollback Tested | Pre-cutover snapshot verified; restore drill and rollback steps tested against workload Tier RTO/RPO | Not started / In progress / Ready | |
| Observability & DORA Metrics Baseline | Centralized logging, metrics, alerting thresholds, and DORA delivery metrics wired before cutover | Not started / In progress / Ready | |
| FinOps Tagging & Budget Alerts | Mandatory cost-allocation tags enforced; budget thresholds and commitment/rightsizing rules active | Not started / In progress / Ready | |
| Operations Runbook & On-Call Handover | Runbooks, CMDB entries, hypercare on-call rotation, and incident escalation SLAs confirmed | Not started / In progress / Ready | |
| Cutover Communications | Change-freeze/holiday check passed; user outage notices and UAT/smoke testers scheduled | Not started / In progress / Ready | |

## Gate Decision

| Role | Name | Decision | Date | Conditions |
| :--- | :--- | :--- | :--- | :--- |
| Wave Owner | | Approve / Conditional / Reject | | |
| Platform / Enterprise Architect | | Approve / Conditional / Reject | | |
| Security Reviewer | | Approve / Conditional / Reject | | |
| Operations / SRE Lead | | Approve / Conditional / Reject | | |
| FinOps Lead | | Approve / Conditional / Reject | | |

**Final Gate Decision:** Approve / Conditional / Reject  
**Conditions to Resolve Before Cutover:**  
**Post-Cutover Hypercare Review Date:**  
