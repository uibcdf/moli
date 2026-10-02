---
summary: Restore verified live Codecov percentages in applicable MOLI READMEs.
issue: uibcdf/moli#35
status: active
opened: 2026-10-01
closed:
verification: inspected
area: [governance, ci]
blocked_by: []
supersedes: []
---

# Live coverage badges for directly governed MOLI repositories

## What

Make the main README show a repository-specific Codecov percentage when its
meaningful test selection has a recent accepted default-branch report. This is
MOLI's direct-component decision. MolSysSuite owns its member rollout in
`uibcdf/molsyssuite#69`.

## Initial inventory, 2026-10-02

| Repository | Meaningful executable code today | Initial Codecov evidence | Owner route |
| --- | --- | --- | --- |
| `uibcdf/moli` | Governance scripts with administrative tests | No report or badge; coverage producer to be added to the existing governance workflow | `uibcdf/moli#35` |
| `uibcdf/sabueso` | Python knowledge package with offline tests | Public `main` badge rendered `unknown`; existing CI did not upload coverage | `uibcdf/sabueso#107` |
| `uibcdf/praxis` | Architectural scaffold; no tested runtime package | No meaningful runtime coverage to advertise | Reassess when a tested runtime is introduced |
| `uibcdf/nextia` | Architectural scaffold; no tested runtime package | No meaningful runtime coverage to advertise | Reassess when a tested runtime is introduced |
| `uibcdf/moli-agent` | Architectural scaffold; no tested agent runtime | No meaningful runtime coverage to advertise | Reassess when a tested runtime is introduced |
| `uibcdf/molsyssuite` | Delegated ecosystem | Member and suite-root inventory is owned by MolSysSuite | `uibcdf/molsyssuite#69` |

The governance percentage measures only `devtools/scripts` under the existing
administrative `unittest` selection. Sabueso's percentage measures its Python
package under the offline pytest selection on Linux/Python 3.13. Neither is a
scientific correctness score or a full operating-system matrix result.

## How / evidence

Retain XML from the actual test job. Upload from a separate trusted-main job
with OIDC, no README token and no PR publication authority. Check the accepted
source SHA, report status, upload timestamp and numeric SVG through Codecov
before adding a badge. Weekly or push-triggered reports may lag the latest
commit; state the measured scope and cadence.

The registry requires a component-owned `coverage_review` for future direct
Python components. The central component checker verifies an adopted badge's
repository, branch and public image shape; it cannot establish live service
freshness. New-component guidance requires the review at inception.

## Why

A visible percentage helps readers assess which code is exercised, but an
`unknown` image or a number copied by hand makes an unsupported claim.

## Alternatives

A static coverage number is rejected because it drifts from Codecov. A badge
before the service accepts the report is rejected because configured upload
steps are not publication evidence. Requiring one percentage across all
architectural scaffolds would imply runtime code that does not exist.

## Acceptance criteria

- MOLI and Sabueso have a recent accepted report for their measured code and a
  live numeric badge in the main README, with scope and cadence described.
- Incubating direct repositories and the delegated suite have explicit
  inventory outcomes and reassessment routes.
- The canonical policy, registry, onboarding guide, component guides and
  mechanical badge-shape guard agree.

## Resolution

Pending Codecov producer verification and README adoption.
