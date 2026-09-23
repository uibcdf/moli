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

The current core deliberately does **not** impose MolSysSuite-specific Python, Ruff, CI-matrix, release, packaging, Zenodo, or badge policies.

Cross-repository byte-level guide synchronization is currently a checked convention and manual synchronization step; automation may be added when the coordination load justifies it.

## Structure

- `governance/` — ownership, reporting, cross-component coordination, and membership/delegation rules.
- `policies/` — shared policies accepted for directly governed MOLI repositories.
- `pending_bugs/` — durable analyses of active platform bugs when needed.
- `pending_proposals/` — durable analyses of active platform proposals when needed.
- `archive/` — permanent historical records.
- `templates/` — shared reporting templates.

GitHub issues are the stable identity for reported work. The concise component-facing summary is the root `MOLI_GUIDE.md`.
