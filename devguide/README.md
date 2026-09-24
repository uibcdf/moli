# MOLI Development Guide

This directory contains durable development/governance knowledge for repositories directly governed by MOLI.

It is distinct from `architecture_1.0/`:

- `architecture_1.0/` defines **what MOLI is**;
- `devguide/` defines **how MOLI repositories coordinate and evolve**.

## Governance v0.1

The initial executable governance core provides:

- an authoritative component/policy registry in `moli.toml`;
- canonical component guidance in `MOLI_GUIDE.md`;
- repository ownership and cross-component feedback rules;
- an issue-backed report lifecycle with pending queues and permanent archive;
- a common report template and status vocabulary;
- a local governance validator for this repository;
- a reusable component checker;
- local governance-surface CI gates in Sabueso, Praxis, Nextia, and MOLI Agent.

[`INFRASTRUCTURE_CENSUS.md`](INFRASTRUCTURE_CENSUS.md) records which platform and
component capabilities have verified implementation, which repositories are still
incubating, and which project-level infrastructure remains specified only in the
architecture. It does not replace the component registry or delegated inventories.

Shared engineering policies (Python support and CI, Ruff/pytest quality tooling, applicable support libraries, developer receptors, distribution, release versions, repository badges, and Zenodo/DOI archival) are documented in `policies/`; `moli.toml` records which repositories or capabilities each one applies to. MolSysSuite-specific extensions for its internally governed members remain in MolSysSuite.

The [quantity integrity policy](policies/quantity_integrity_policy.md) applies wherever
physical quantities cross an API, storage, process or component boundary. PyUnitWizard
owns the shared serialization design and codec; the component owns its scientific
meaning, source vocabulary, schema migration and adoption evidence.

The scheduled component-guide audit checks byte-identical copies and Python-package classification in directly governed repositories. Guide updates are synchronized to those repositories when the canonical guide changes.

The [UIBCDF support-infrastructure catalog](governance/support_infrastructure.md)
records the developer receptors and publication actions used by MOLI repositories.
These resources have their own provider repositories and issue boards; they are not
new scientific MOLI components.

## Structure

- `governance/` — ownership, reporting, cross-component coordination, and membership/delegation rules.
- `governance/policy_inheritance.md` — single-source MOLI engineering policy and delegated adoption.
- `policies/` — shared policies accepted for directly governed MOLI repositories.
- `pending_bugs/` — durable analyses of active platform bugs when needed.
- `pending_proposals/` — durable analyses of active platform proposals when needed.
- `archive/` — permanent historical records.
- `templates/` — shared reporting templates.

GitHub issues are the stable identity for reported work. The concise component-facing summary is the root `MOLI_GUIDE.md`.


## Cross-platform scientific communication

[`SCIENTIFIC_COMMUNICATION.md`](SCIENTIFIC_COMMUNICATION.md) records the long-term MOLI capability for producing traceable ProjectBriefings, ProgressBriefs, and ProjectReports from Scientific Context, modeling, and Discovery state, with multiple renderings such as written dossiers, slides, interactive reports, and future narrated video.


## Reproducibility, audit, trace, and replay

[`REPRODUCIBILITY_AUDIT_AND_REPLAY.md`](REPRODUCIBILITY_AUDIT_AND_REPLAY.md) records the cross-platform requirement that completed MOLI projects remain independently auditable and that their recorded computational trajectories can be replayed without requiring an LLM/agent to reason again. It distinguishes Decision, ExecutionPlan, Run, scientific interpretation, snapshots/manifests, and the separate operations Audit, Trace, Replay, and Rerun.


## Recorda provenance instrumentation (formerly Scribe)

[`RECORDA.md`](RECORDA.md) is intentionally retained as MOLI's integration specification for **Recorda** (originally designed under the working name Scribe). It explains how Recorda instrumentation, project-context propagation, safe capture, semantic profiles, event emission, and ownership-aware routing contribute to ProjectRecord/EventLedger and Nextia ProjectGraph evolution. The standalone/general design is maintained in `uibcdf/recorda`.
