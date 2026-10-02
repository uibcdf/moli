---
summary: Restore verified live Codecov percentages in applicable MOLI READMEs.
issue: uibcdf/moli#35
status: resolved
opened: 2026-10-01
closed: 2026-10-02
verification: measured
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

MOLI adopted the coverage policy, owner-local registry review and future-repo
check in [`3a81276`](https://github.com/uibcdf/moli/commit/3a81276).
Its administrative tests publish coverage on each `main` push, and the README
shows a live Codecov badge. [Run 36986025418](https://github.com/uibcdf/moli/actions/runs/36986025418)
published the `43060e5` report; Codecov returned `state=complete`, 55.38%
and `updatestamp=2026-10-02T08:47:43Z`, while the public SVG showed 55%.

Sabueso adopted the measured Linux/Python 3.13 offline pytest producer in
[`ef40ba8`](https://github.com/uibcdf/sabueso/commit/ef40ba8) and the
README badge in [`28485b2`](https://github.com/uibcdf/sabueso/commit/28485b2).
[Run 36985932505](https://github.com/uibcdf/sabueso/actions/runs/36985932505)
passed all nine cells, retained `coverage.xml` and published the `3bef1bc`
report. Codecov returned `state=complete`, 85.86% and
`updatestamp=2026-10-02T08:52:34Z`; its public SVG showed 86%.
The badges themselves remain dynamic; these figures are dated verification
evidence, not README values or coverage thresholds.

The direct scaffolds have no meaningful tested runtime yet and will be
reassessed at package admission. MolSysSuite retains its own suite/member
adoption in [#69](https://github.com/uibcdf/molsyssuite/issues/69).
