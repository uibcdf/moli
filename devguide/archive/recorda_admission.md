---
summary: Register the directly governed Recorda recording component.
issue: uibcdf/moli#50
status: resolved
opened: 2026-10-05
closed: 2026-10-06
verification: measured
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

## Historical verification and remaining delivery (2026-10-05)

The reconciled MOLI registry validates on Python 3.14, and all 44 administrative contract tests pass. The local Recorda checkout passes the current component governance checker with the canonical guide. Recorda Lab's local checkout still lacks the nested developer-guide instructions and has guide/instruction drift; the laboratory owner must reconcile those files before calling that surface complete.

Recorda's published main at a007b65cbcc606871667c28ddaa36eb8fb44c3b2 still contains only README and development guidance at the repository root. Its local implementation and governance surface have not yet been published. The registry addition therefore does not certify completed hosted guide delivery, runtime maturity, public OS support, coverage, or release readiness. Recorda implementation and delivery remain under uibcdf/recorda#1; coverage is under #6. Keep this admission report active until published delivery and the applicable hosted audit are verified.

The workspace-wide local guide audit also reports stale or missing surfaces in MOLI Agent, Nextia and Praxis. That result describes the local checkouts, not independently verified current remote delivery. Those repositories retain ownership of their changes.


## Admission outcome and published governance review — 2026-10-06

Recorda is registered as a directly governed MOLI recording substrate and has
published its experimental implementation. The associated laboratory is test
infrastructure; neither repository becomes a MolSysSuite member. Earlier
unpublished-delivery and laboratory-guide findings above are historical.

Current reviewed guard commits are Recorda
`bb2da676824a68728e8bee1ec160b038832eb8f7` and Recorda Lab
`0ca1943baeb2551489eaa821fb414b95892e0952`. Root/nested instructions,
canonical byte-identical guides, issue/report/template/archive surfaces and
local validators pass. Existing owner publication of the experimental 0.2.0
source checkpoint at `4e3d422fef1b0927fe63422323dc6d941c061bfb` and the
laboratory's updated manual source default were preserved.

The review reproduced a missing regression gate: each old local validator
accepted an isolated copy without `devguide/AGENTS.md`. MOLI's existing shared
checker rejected it. Recorda #10 and Recorda Lab #7 now invoke that checker
and canonical guide at immutable MOLI
`4316867722f259fdf77f4d7d5e6e2c093ff95d04` from their existing CI governance
routes. No duplicate validator or new Action was introduced. Existing
`tests/test_component_guides.py::ComponentGuideTests::test_missing_nested_instructions_are_reported`
protects the mechanism; all 41 MOLI administrative tests pass locally.

Exact-head Recorda CI 37425033040 succeeds in all seven jobs, including the
executed shared-core step. Recorda Lab push 37425032314 succeeds in its four
dummy/governance jobs; manual integration/scientific jobs are intentionally
skipped and are not newly certified. Historical manual 37422250513 remains a
separate seven-job success. GH Run Receptor independently reads these jobs.

Actual full platform-guide audit 37423854461 checks published Recorda without
a finding but fails on guide drift in MOLI Agent, Nextia and Praxis. Its failure
is preserved and independently tracked by uibcdf/moli#60; registration does
not claim that global audit passes. No affected rule was removed or filtered.

This resolves the bounded registration/published-governance delivery theme.
Recorda #2/#3 remain partial for ecosystem/distribution adoption, #4 remains
pending for installed-candidate OS support and #6 for coverage. Public package,
OS, stable API, complete recording, replay and cross-component runtime evidence
remain owner work. Canonical guide and shared normative policy are unchanged.

Primary receipt: `devguide/evidence/recorda_governance_50_20261006.json`.
Normative onboarding: `devguide/governance/new_component_onboarding.md`.
