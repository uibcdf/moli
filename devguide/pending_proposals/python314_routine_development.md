---
summary: Make Python 3.14 the routine development and CI interpreter across MOLI and MolSysSuite.
issue: uibcdf/moli#37
status: active
opened: 2026-10-02
closed:
verification: inspected
area: [governance, ci]
blocked_by: []
supersedes: []
---

# Python 3.14 as routine development interpreter

## What

The maintainer decided on 2026-10-02 that local development and the routine
CI test lane for MOLI and MolSysSuite Python tools use Python 3.14. A lane that
previously tested only 3.13 moves to 3.14. Python 3.13 remains in the full
compatibility matrix where the package still supports it. This is a working
interpreter decision, not a finding that every member has already passed its
3.14 scientific or installed-package gates.

## Ownership and route

MOLI sets the direct-component Python baseline and validates this repository on
3.14. Sabueso is the current directly governed public Python package and must
move its routine macOS test, coverage producer and local development recipe.
MolSysSuite independently sets the corresponding member policy, starter kit,
shared development recipe and rollout under `uibcdf/molsyssuite#39` and
`uibcdf/molsyssuite#51`. The suite owns each member's adoption and any bounded
exception. A Python package that cannot yet install or test on 3.14 retains an
owner-local blocker with an exit condition; a 3.13 result cannot be counted as
passing the new routine gate.

## Why

An older routine interpreter can miss failures that affect the development
environment and the newest supported minor. The weekly/full matrix still
protects users on older supported minors.

## Acceptance

- Direct MOLI policy, registry, CI and guide identify 3.14 as the routine
  version; the direct-component starter guidance and Sabueso's active workflow
  and development environment agree.
- MolSysSuite's policy, registry, shared environment, starter kit and central
  administrative tests use 3.14; its member rollout and blockers are tracked
  under suite authority without false compatibility claims.
- Hosted runs show the actual interpreter and tests. Installed-package and
  platform claims continue to need their separate evidence.

## Resolution

Pending hosted and component rollout evidence.
