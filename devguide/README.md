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

Shared engineering policies (Python support, Python CI, Ruff/pytest quality tooling, release versions, repository badges, Zenodo/DOI archival) are documented in `policies/`; `moli.toml` records which repositories or capabilities each one applies to. MolSysSuite-specific extensions for its internally governed members remain in MolSysSuite.

Cross-repository byte-level guide synchronization is currently a checked convention and manual synchronization step; automation may be added when the coordination load justifies it.

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
