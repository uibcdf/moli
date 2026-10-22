# MolI Development Guide

This directory contains durable development/governance knowledge for repositories directly governed by MolI.

**Resume work here:** [`CHECKPOINT.md`](CHECKPOINT.md) records the dated state of
the current pause, recent completions, live work to recheck, and a short
resumption procedure. GitHub issues and `moli.toml` remain authoritative; the
checkpoint is a navigation aid, not a second backlog or policy source.

It is distinct from `architecture_1.0/`:

- `architecture_1.0/` defines **what MolI is**;
- `devguide/` defines **how MolI repositories coordinate and evolve**.

**MolI** combines **Mol** from Molecular and **I** from Intelligence: it names
the platform supporting Molecular Intelligence. **Moli** is the proper name of
its optional scientific agent. The [naming policy](policies/naming_policy.md)
records the conceptual basis and standard for future documentation and
communication, including the older spellings and preservation of exact
technical identifiers and historical quotations.

## Governance

The initial executable governance core provides:

- an authoritative component/policy registry in `moli.toml`;
- canonical component guidance in `MOLI_GUIDE.md`;
- repository ownership and cross-component feedback rules;
- an issue-backed report lifecycle with pending queues and permanent archive;
- a common report template and status vocabulary;
- a local governance validator for this repository;
- a reusable component checker;
- local governance-surface CI gates in Sabueso, Praxis, Nextia, Moli,
  and Recorda.

[`INFRASTRUCTURE_CENSUS.md`](INFRASTRUCTURE_CENSUS.md) records which platform and
component capabilities have verified implementation, which repositories are still
incubating, and which project-level infrastructure remains specified only in the
architecture. It does not replace the component registry or delegated inventories.

Engineering policies for directly governed components (Python support and CI, Ruff/pytest quality tooling, applicable support libraries, developer receptors, distribution, release versions, repository badges, and Zenodo/DOI archival) are documented in `policies/`; `moli.toml` records their applicability. MolSysSuite defines and versions the engineering policies for its own members. MolI governs the suite's platform boundary and shared scientific contracts.

The [Ackredit client policy](policies/ackredit_client_policy.md) records bounded
public attribution, function-provider and recording-evidence promises for
owner-selected direct-component use. Capability floors, required/optional host
profiles and actual receiving evidence remain separate. Its
[review inventory](archive/review_ackredit_optional_contracts.md) identifies the
accepted scope and component-owned follow-ups without requiring an upgrade.

The [quantity integrity policy](policies/quantity_integrity_policy.md) applies wherever
physical quantities cross an API, storage, process or component boundary. PyUnitWizard
owns the shared serialization design and codec; the component owns its scientific
meaning, source vocabulary, schema migration and adoption evidence.

The scheduled component-guide audit checks byte-identical copies and Python-package classification in directly governed repositories. Guide updates are synchronized to those repositories when the canonical guide changes.

The [agent-instruction lifecycle](governance/agent_instruction_lifecycle.md)
defines when an accepted development lesson becomes a root or nested
`AGENTS.md` rule. Its [adoption inventory](governance/agent_instruction_adoption.md)
tracks directly governed repositories without taking over MolSysSuite members.

The [human-facing feedback rule](governance/reporting_protocol.md#human-facing-issue-feedback)
requires surfacing actionable uncertain or nonblocking findings and offering
their owning issue under the applicable reporting and disclosure authority.
Its [adoption record](pending_proposals/human_facing_issue_feedback.md) tracks the
bounded contributor instruction separately from the scientist-facing runtime
pilot and verified-fix notifications in #34.

The [GitHub Discussions policy](governance/github_discussions.md) requires
Discussions across MolI repositories with common Announcements, Q&A and Ideas
categories, plus component-specific extensions. It defines triage ownership
and promotion to owning issues or versioned decisions. The
[archived implementation record](archive/github_discussions.md) and
[dated receipt](evidence/github_discussions_23_20261021.json) record the seven
configured platform/root repositories. MolSysSuite
[#120](https://github.com/uibcdf/molsyssuite/issues/120) retains its own member
policy and rollout; the root configuration does not establish member adoption.

The [temporary-resource lifecycle](governance/temporary_resource_lifecycle.md)
requires owner-scoped cleanup after the last useful use while preserving active
work and evidence still needed for verification. Its
[adoption record](governance/temporary_resource_adoption.md) separates direct
component instructions from shared-provider and MolSysSuite follow-ups.

The [UIBCDF support-infrastructure catalog](governance/support_infrastructure.md)
records the developer receptors and publication actions used by MolI repositories.
These resources have their own provider repositories and issue boards; they are not
new scientific MolI components.

## Structure

- `governance/` — ownership, reporting, cross-component coordination, and membership/delegation rules.
- `governance/policy_inheritance.md` — direct-component policy scope and delegated member-governance boundary.
- `policies/` — shared policies accepted for directly governed MolI repositories.
- `pending_bugs/` — durable analyses of active platform bugs when needed.
- `pending_proposals/` — durable analyses of active platform proposals when needed.
- `archive/` — permanent historical records.
- `templates/` — shared reporting templates.

GitHub issues are the stable identity for reported work. The concise component-facing summary is the root `MOLI_GUIDE.md`.

The review-only [Sabueso/Recorda receiving exercise](pending_proposals/sabueso_recorda_handoff.md)
supplies public acceptance material for #36: original scientific/credit artifacts,
explicit application consumption, independent read and failed/unavailable delivery.
Its bounded example is not an accepted ProjectRecord schema or routing runtime.


## Cross-platform scientific communication

[`SCIENTIFIC_COMMUNICATION.md`](SCIENTIFIC_COMMUNICATION.md) records the long-term MolI capability for producing traceable ProjectBriefings, ProgressBriefs, and ProjectReports from Scientific Context, modeling, and Discovery state, with multiple renderings such as written dossiers, slides, interactive reports, and future narrated video.


## Reproducibility, audit, trace, and replay

[`REPRODUCIBILITY_AUDIT_AND_REPLAY.md`](REPRODUCIBILITY_AUDIT_AND_REPLAY.md) records the cross-platform requirement that completed MolI projects remain independently auditable and that their recorded computational trajectories can be replayed without requiring an LLM/agent to reason again. It distinguishes Decision, ExecutionPlan, Run, scientific interpretation, snapshots/manifests, and the separate operations Audit, Trace, Replay, and Rerun.


## Recorda provenance instrumentation (formerly Scribe)

[`RECORDA.md`](RECORDA.md) is intentionally retained as MolI's integration specification for **Recorda** (originally designed under the working name Scribe). It explains how Recorda instrumentation, project-context propagation, safe capture, semantic profiles, event emission, and ownership-aware routing contribute to ProjectRecord/EventLedger and Nextia ProjectGraph evolution. The standalone/general design is maintained in `uibcdf/recorda`.

## Development observability

The operational [MolI Development Observatory](https://github.com/uibcdf/moli-dev-observatory)
is maintained in its dedicated repository. This repository retains only the
[platform-side migration pointer](DEVELOPMENT_OBSERVATORY.md) and historical
decision record; `moli.toml` remains an authoritative input to the Observatory.

