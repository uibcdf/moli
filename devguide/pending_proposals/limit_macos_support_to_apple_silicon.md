---
summary: Restrict macOS support claims for MOLI direct components to Apple Silicon.
issue: uibcdf/moli#31
status: open
opened: 2026-09-27
closed:
verification: inspected
area: [governance, compatibility]
blocked_by: []
supersedes: []
---

# Limit macOS support to Apple Silicon in MOLI direct components

## What

MOLI should adopt this common support statement for applicable direct components:

> macOS support is currently limited to Apple Silicon (arm64). Intel-based
> macOS (x86_64) is not part of the supported platform matrix. Support may be
> reconsidered if there is demonstrated user demand.

This does not certify macOS arm64 in a component that has not earned that
claim. MolSysSuite owns its member rollout separately in
`uibcdf/molsyssuite#59`.

## How / evidence

Inspect each direct component's supported-platform declarations, build and
test matrices, publication paths, and developer guidance. Remove prospective
Intel macOS targets and add accurate user-facing wording only where a macOS
support claim exists. Preserve dated release artifacts and historical evidence.

The direct-component inventory on 2026-10-02 found one public Python package
with a macOS claim: Sabueso. Its prior 0.5.0 installed-package matrix ran on
arm64 according to the owner evidence in this issue. The prospective routine
and staged matrices now use the documented arm64 `macos-26` runner and check
`uname -m`; the noarch Conda build already has `platform_osx-64: false`.
Sabueso's README and two user installation pages carry the support boundary.
Praxis, Nextia and MOLI Agent are architectural scaffolds with no public
Python-package or OS support claim. MOLI itself is a governance repository,
not a public Python package. MolSysSuite completed its member-owned rollout
under `uibcdf/molsyssuite#59` without transferring member rows into MOLI.

This is an explicit maintainer support-scope decision on 2026-09-27, not a
finding that Intel binaries can no longer be built or used.

## Why

The initial user base is expected to be small. Avoiding an extra native
architecture lets maintainers focus on the platforms they can test and
support; demonstrated demand can reopen the decision.

## Alternatives

Keeping Intel macOS as a default release gate was rejected for now. Removing
existing artifacts or related fork repositories is unnecessary and not
authorized by this policy change.

## Acceptance criteria

- MOLI's direct-component platform policy clearly names arm64 as the only
  macOS support target, with the demand-based reconsideration clause.
- Applicable direct components expose accurate support messages and exclude
  Intel targets from prospective validation and publication gates.
- The MOLI and MolSysSuite records link to one another without transferring
  implementation ownership between their registries.

## Resolution

Pending rollout across MOLI direct components.
