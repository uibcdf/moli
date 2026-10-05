---
summary: Register the directly governed Recorda recording component.
issue: uibcdf/moli#50
status: active
opened: 2026-10-05
closed:
verification: reproduced
area: [governance, recording]
blocked_by: []
supersedes: []
---

## Purpose and ownership

Register Recorda as directly governed MOLI recording/provenance infrastructure. Its local implementation remains in uibcdf/recorda, without a MOLI runtime dependency; it is not a MolSysSuite member or a new Knowledge/Know-how/Discovery pillar. The maintainer selected uibcdf/recorda-lab as associated controlled test infrastructure.

## Prepared changes

Add components.recorda to moli.toml with python-package capability, vendored MOLI guide, component-owned ecosystem/distribution/OS/coverage reviews, partial packaging/ecosystem states and an empty public supported_os list pending evidence. Coverage review is pending under uibcdf/recorda#6; no accepted Codecov report or percentage is claimed. Clarify direct governance classification and align RECORDA.md with the controlled laboratory followed by real-library, Sabueso and platform experiments.

Earlier preparation established local contributor instructions, guide copies, issue/report queues, templates, archive, package metadata and experimental CI. Recheck those surfaces against the current guide after upstream changes; local tests do not constitute public support or release qualification. Keep the census's published-commit observations historical until published implementation evidence exists.

## Acceptance

MOLI registry validation and classification tests pass; guide delivery remains exact. Local implementation/scenario work stays with its owner, referenced by uibcdf/recorda#1. Reconcile remaining published documentation/census evidence after implementation is pushed. No suite member admission or suite policy inheritance is introduced.

## Reconciliation with the current Python baseline

The prepared local changes assumed an active component-specific Python 3.14 transition. Upstream has since adopted Python 3.11–3.14 with routine development and push/PR tests on 3.14 under uibcdf/moli#37; the platform transition is completed. Recorda follows that accepted baseline directly and needs no separate 3.14 admission or development-default exception. Python 3.13 remains in the full compatibility matrix alongside the other supported minors. Recorda Lab follows as associated infrastructure. Earlier transition notes in uibcdf/moli#50 and uibcdf/recorda#4 are historical and superseded by this reconciliation; public OS and installed-candidate qualification remain pending under the component's review.

## Verification and remaining delivery (2026-10-05)

The reconciled MOLI registry validates on Python 3.14, and all 44 administrative contract tests pass. The local Recorda checkout passes the current component governance checker with the canonical guide. Recorda Lab's local checkout still lacks the nested developer-guide instructions and has guide/instruction drift; the laboratory owner must reconcile those files before calling that surface complete.

Recorda's published main at a007b65cbcc606871667c28ddaa36eb8fb44c3b2 still contains only README and development guidance at the repository root. Its local implementation and governance surface have not yet been published. The registry addition therefore does not certify completed hosted guide delivery, runtime maturity, public OS support, coverage, or release readiness. Recorda implementation and delivery remain under uibcdf/recorda#1; coverage is under #6. Keep this admission report active until published delivery and the applicable hosted audit are verified.

The workspace-wide local guide audit also reports stale or missing surfaces in MOLI Agent, Nextia and Praxis. That result describes the local checkouts, not independently verified current remote delivery. Those repositories retain ownership of their changes.
