# MOLI development checkpoint

**Paused on:** 2026-10-20 (23:07 UTC). **MOLI `main`:**
[`5584382`](https://github.com/uibcdf/moli/commit/558438240173aff42f24ee585cd1e52f235d8c94)
was synchronized with `origin/main` and clean when this checkpoint was prepared.
This page is a dated navigation aid. Recheck the live [MOLI issue board](https://github.com/uibcdf/moli/issues),
the relevant owner issues and current repository heads before acting. Do not use a
historical issue count or this page to infer that an adoption or CI run still has
the same state.

## Where authority and current evidence live

- [`moli.toml`](../moli.toml) registers direct components and accepted policies;
  [`MOLI_GUIDE.md`](../MOLI_GUIDE.md) is the concise component-facing rule.
  [`README.md`](README.md) indexes the normative devguide documents, and
  [`INFRASTRUCTURE_CENSUS.md`](INFRASTRUCTURE_CENSUS.md) records pinned
  implementation snapshots rather than a live issue queue.
- MOLI owns platform contracts and its directly governed components. The
  [MolSysSuite issue board](https://github.com/uibcdf/molsyssuite/issues) and
  its own registry/guide own member policy and rollout. Route owner-local fixes
  and shared-provider changes through their owning issues; link impact issues
  where needed.
- The open MOLI board had **18 issues** at the snapshot time. The lists below
  indicate where to resume reading, not a new priority order or acceptance
  decision. Issue comments and linked evidence are the current work record.

## Last completed MOLI work

- [#68](https://github.com/uibcdf/moli/issues/68): public GitHub Release titles
  use the exact version. The MOLI rule and direct-component guide copies were
  delivered; the [full guide audit](https://github.com/uibcdf/moli/actions/runs/39468857387)
  passed. MolSysSuite handled its own member rollout in
  [#119](https://github.com/uibcdf/molsyssuite/issues/119).
- [#61](https://github.com/uibcdf/moli/issues/61): owner-scoped retirement of
  temporary development resources. The [normative rule](governance/temporary_resource_lifecycle.md),
  [adoption record](governance/temporary_resource_adoption.md), and five direct
  component guide/instruction deliveries are published. The final
  [governance run](https://github.com/uibcdf/moli/actions/runs/39490747547)
  and [full guide audit](https://github.com/uibcdf/moli/actions/runs/39490330174)
  passed. The separate MolSysSuite member rollout remains in
  [suite #104](https://github.com/uibcdf/molsyssuite/issues/104); the Conda
  action's provider decision remains in
  [action #51](https://github.com/uibcdf/action-build-and-upload-conda-packages/issues/51).
- [#60](https://github.com/uibcdf/moli/issues/60),
  [#41](https://github.com/uibcdf/moli/issues/41),
  [#44](https://github.com/uibcdf/moli/issues/44), and
  [#45](https://github.com/uibcdf/moli/issues/45) were also closed after their
  recorded evidence was checked. Read each issue for its exact accepted scope.

## Open coordination that was active at the pause

| MOLI issue | Current boundary and next evidence |
| --- | --- |
| [#40](https://github.com/uibcdf/moli/issues/40) | Python 3.14 editable co-development is documented; Recorda/Praxis source and development compatibility with recent public providers has been received. The combined workspace remains partial: [suite #82](https://github.com/uibcdf/molsyssuite/issues/82) still has TopoMT authorization and broader integration, and [Recorda #26](https://github.com/uibcdf/recorda/issues/26) owns a future public release for the latest-provider cohort. A fourteen-member suite receipt plus two direct consumers does not establish a sixteen-component qualification. |
| [#62](https://github.com/uibcdf/moli/issues/62) | Shared diagnostic-provider work has public provider evidence and specific consumer handoffs, but application-owned policy, scoped-capture adoption and receiving decisions remain issue-bound. Check the latest provider and consumer comments before selecting a MOLI action; availability of a provider release does not itself approve adoption. |

## Other open MOLI issues

- **Scientific and interoperability contracts:** [#3](https://github.com/uibcdf/moli/issues/3),
  [#17](https://github.com/uibcdf/moli/issues/17),
  [#22](https://github.com/uibcdf/moli/issues/22),
  [#28](https://github.com/uibcdf/moli/issues/28),
  [#33](https://github.com/uibcdf/moli/issues/33),
  [#36](https://github.com/uibcdf/moli/issues/36), and
  [#46](https://github.com/uibcdf/moli/issues/46). Several require a real
  consumer, implementation or owner decision; read the issue before treating
  the design as ready for closure.
- **Operations and governance decisions:** [#8](https://github.com/uibcdf/moli/issues/8)
  (Conda upload credential access), [#23](https://github.com/uibcdf/moli/issues/23)
  (Discussions), and [#47](https://github.com/uibcdf/moli/issues/47)
  (reserved archive tags).
- **Longer-horizon or explicitly deferred scope:** [#12](https://github.com/uibcdf/moli/issues/12)
  (cross-component quantity canary), [#18](https://github.com/uibcdf/moli/issues/18)
  and [#19](https://github.com/uibcdf/moli/issues/19) (project telemetry and
  effort annotations), [#34](https://github.com/uibcdf/moli/issues/34)
  (scientist-facing issue feedback), [#42](https://github.com/uibcdf/moli/issues/42)
  (deferred Conda-provider adoption), and [#43](https://github.com/uibcdf/moli/issues/43)
  (release overhead). In particular, the user asked to leave the quantity
  canary for later. An open issue here is an intentionally tracked objective,
  not proof that work should start immediately.

## When development resumes

1. Synchronize this clone with `origin/main`; check for local work before
   changing branches or files. Read this checkpoint, then refresh the live
   MOLI and relevant owner issue states and their latest evidence.
2. Select one issue with the maintainer. Resolve its ownership boundary using
   [`MOLI_GUIDE.md`](../MOLI_GUIDE.md), applicable `moli.toml` policy entries and
   the relevant architecture decision. For MolSysSuite member work, notify its
   team through a linked suite issue rather than editing member repositories.
3. Update the owning issue with the decision, exact evidence and remaining
   limits. For MOLI governance edits, run
   `python devtools/scripts/validate_governance.py`; verify applicable hosted
   gates on the delivered head. Refresh this checkpoint when the pause state
   or next resumption path materially changes.

No further MOLI issue implementation is in progress as part of this pause.
