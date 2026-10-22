---
summary: Reconcile Python 3.14 workspace evidence and remaining joint integration.
issue: uibcdf/moli#40
status: partial
opened: 2026-10-03
closed:
verification: inspected
area: [development-environment, interoperability]
blocked_by: []
supersedes: []
---

# Python 3.14 shared development workspace

## Current assessment — 2026-10-22 UTC

The accepted [distribution policy](../policies/python_distribution_policy.md#development-and-ci),
[component guide](../../MOLI_GUIDE.md#moli-engineering-baseline),
[onboarding checklist](../governance/new_component_onboarding.md) and
[contributor starter](../templates/component_agent_instructions.md) already
specify Python 3.14, a compatible Conda dependency closure, per-checkout
`python -m pip install --no-deps --editable .`, verified import origins and
tracked exclusions. Supported older minors remain in compatibility CI.
This review corrects the issue's obsolete cohort description; it adds no
installation rule or environment recipe.

Sabueso, Praxis and Recorda are directly governed installable Python components
in `moli.toml`. Nextia and Moli have no current Python-package capability and
need no editable installation. Nextia implementation remains deferred.
MolSysSuite owns its members, named environment, registry-derived installer and
integration authorization in [suite #82](https://github.com/uibcdf/molsyssuite/issues/82).
Use its [workspace contract](https://github.com/uibcdf/molsyssuite/blob/83ae9925ce2133fea5f4eb586316c7d3c9f99709/devguide/development_workspace.md)
and maintained [environment instructions](https://github.com/uibcdf/molsyssuite/blob/main/devtools/conda-envs/README.md);
do not copy its recipe into MolI or add direct components to the suite registry.

## Evidence already received

The pinned [2026-10-20 cross-domain receipt](https://github.com/uibcdf/molsyssuite/blob/83ae9925ce2133fea5f4eb586316c7d3c9f99709/devguide/rollouts/latest_public_workspace_cohort_82_20261020.json)
and the owning issues distinguish these scopes:

| Scope | Recorded outcome | Limit |
| --- | --- | --- |
| Fourteen eligible suite members | Fresh Linux/Python 3.14 public-channel solve, editable installation, dependency closure and actual source/official-Qt imports in [39472963178](https://github.com/uibcdf/molsyssuite/actions/runs/39472963178), suite source `05126c54d45a118db966070d1c42b2198713820c`. The receipt retains each participant revision. | Suite-only integration; not a scientific test campaign or direct-component admission. The original eight-member description is historical. |
| Recorda source/development receiving | [#24](https://github.com/uibcdf/recorda/issues/24) closed at `4a94b5dc0a783160335b0e9c18aab7f85e81ab70`; [39471202391](https://github.com/uibcdf/recorda/actions/runs/39471202391) has fourteen accepted jobs, including eight installed Linux/macOS arm64 minor cells and four recovery cells. | Source/development compatibility does not rewrite public Recorda 0.3.0. |
| Praxis source/development receiving | [#10](https://github.com/uibcdf/praxis/issues/10) closed at `6d092a991ab3fd05fdfab4206094cd48d423b1b2`; [39471277865](https://github.com/uibcdf/praxis/actions/runs/39471277865) has nineteen accepted jobs, including eight latest-provider and eight legacy installed cells. | Latest-provider cells explicitly omit incompatible public Recorda 0.3.0 and real MolSysMT; legacy recording and joint editable recording are separate evidence. |
| Joint editable Recorda/Praxis, exact public providers | The disposable Linux/Python 3.14.8 receiving passed 345 Recorda / 154 Praxis tests with clean dependency closure. Selected providers were ArgDigest 0.16.0, SMonitor 0.21.0 and DepDigest 0.15.1; original file digests/import provenance are in the receipt. | Optional real-MolSysMT scenario omitted. No full MolSysMT scientific qualification or new consumer Conda release. |
| Existing named workspace | After deliberate consumer source updates/reinstallation, five newer consumer metadata conflicts were removed; local tests passed 345 Recorda / 156 Praxis cases with the real-MolSysMT module excluded. | Seven previously accepted external dependency findings remain. A host's existing environment is not the clean disposable receiving environment. |

These are existing owner-executed results and retained native receipts inspected
here. They were not rerun by this documentary review. The receipt's early
`selected_completed_native_jobs` section preserves then-pending macOS jobs;
its final `hosted_full_matrix_state` and owning issue closeouts record their
eventual success. Do not mistake the earlier observation for current debt.

The previous MolI head's [full fresh guide audit](https://github.com/uibcdf/moli/actions/runs/39705085710)
already passes for all five direct repositories at
`4b086ef4c7bbbaa2539bc9e4c768340feb118841`. This review changes no guide bytes,
registry, installer or environment. Final documentary-head validation is
recorded in #40's delivery comment.

## Outstanding work and owners

1. **Joint direct-component receiving — MolI #40, coordinated with suite #82.**
   Select the participating suite and Sabueso/Praxis/Recorda revisions and
   demonstrate their combined dependency closure, editable origins and relevant
   cross-component operations in one compatible environment. Record exclusions
   and their owners explicitly. Fourteen-member suite evidence plus separately
   tested consumers does not establish a sixteen- or seventeen-component result.
   [Sabueso #109](https://github.com/uibcdf/sabueso/issues/109) is closed for
   guidance adoption and bounded local checks, not joint workspace receiving;
   do not present it as an open implementation ticket or proof of integration.
2. **TopoMT cohort authorization/integration — MolSysSuite team.**
   [Suite #51](https://github.com/uibcdf/molsyssuite/issues/51) and
   [TopoMT #16](https://github.com/uibcdf/topomt/issues/16) retain component-owned
   qualification and scientific debt. Exclusion from the authorized profile
   does not mean its metadata lacks Python 3.14. MolI does not edit member sources
   or waive their gates.
3. **New public Recorda package — Recorda team, [#26](https://github.com/uibcdf/recorda/issues/26).**
   Version/timing, exact candidate, tested artifact and public receiving belong
   there. Original 0.3.0 stays immutable. A new public release is needed for
   public-only latest-provider recording in Praxis; it is not a prerequisite
   invented for the already completed editable-source receiving.

Keep #40 `partial` for its broader joint integration scope. Central contributor
guidance is delivered; public publication and delegated cohort expansion retain
their own owners. Do not infer scientific, GUI, additional-OS or public-package
qualification from a guide, solver or import check. Optional diagnostic-capability
decisions remain independently tracked in [#62](https://github.com/uibcdf/moli/issues/62).
