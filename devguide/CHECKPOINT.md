# MolI development checkpoint

**Refreshed on:** 2026-10-22 UTC for the bounded retrieval/archive contract
review in [#33](https://github.com/uibcdf/moli/issues/33) and reconciliation of
the obsolete open-coordination entry for closed #62. Earlier workspace receiving,
credential guidance, Discussions, optional-provider reviews and contributor-rule
deliveries retain their scoped evidence below.
Each owning issue records the exact final published source, native gates and
temporary-resource disposition; receipt links below identify their scoped evidence.
This page is a dated navigation aid. Recheck the live [MolI issue board](https://github.com/uibcdf/moli/issues),
the relevant owner issues and current repository heads before acting. Do not use a
historical issue count or this page to infer that an adoption or CI run still has
the same state.

## Where authority and current evidence live

- [`moli.toml`](../moli.toml) registers direct components and accepted policies;
  [`MOLI_GUIDE.md`](../MOLI_GUIDE.md) is the concise component-facing rule.
  [`README.md`](README.md) indexes the normative devguide documents, and
  [`INFRASTRUCTURE_CENSUS.md`](INFRASTRUCTURE_CENSUS.md) records pinned
  implementation snapshots rather than a live issue queue.
- MolI owns platform contracts and its directly governed components. The
  [MolSysSuite issue board](https://github.com/uibcdf/molsyssuite/issues) and
  its own registry/guide own member policy and rollout. Route owner-local fixes
  and shared-provider changes through their owning issues; link impact issues
  where needed.
- Consult the live board for current open work. The lists below indicate where
  to resume reading, not a new priority order or acceptance decision. Issue
  comments and linked evidence are the current work record.

## Last completed MolI work

- **Actual joint receiving in [#40](https://github.com/uibcdf/moli/issues/40):**
  a fresh Linux/Python 3.14.8 Conda environment installs fourteen eligible suite
  sources plus Sabueso/Praxis/Recorda from fixed clean snapshots. Joint dependency
  closure, all seventeen editable/import origins and official Qt 6.11.2 pass.
  Published pytest-receptor runs 19 handoff, seven Praxis integration/real-MolSysMT/
  quantity and 345 Recorda cases: **371 passed, zero skips**. The
  [resolved review](archive/python_314_workspace.md) and
  [receipt](evidence/python_314_workspace_40_20261022.json) keep this exact cohort
  distinct from public packages, other OS/minors and full scientific/GUI admission.
  TopoMT stays suite-owned/excluded; Recorda #26 stays the release owner. The
  caller's environment retains its twelve prior findings; unrelated/concurrent
  owner work is preserved. Known receptor #4 warning and optional absent beartype
  are explicit. Final CI, issue closure and temporary-prefix/cache retirement
  are recorded in #40's closeout.

- **Administrative decision in [#8](https://github.com/uibcdf/moli/issues/8):**
  Diego Prada confirmed the canonical `ANACONDA_UIBCDF_TOKEN` organization
  secret, his administration/rotation responsibility and selected-repository
  grants requested through an owning issue. The
  [distribution contract](policies/python_distribution_policy.md#conda-publication-credential-access),
  onboarding and release checklist record this once, with a presence-only
  readiness example. Actual repository grants, execution and successful
  authorized delivery remain separate evidence; the current API context cannot
  inspect organization-secret metadata (403). No credential value, grant,
  rotation, workflow dispatch or publication was accessed/performed here.

- **Earlier documentary reconciliation of [#40](https://github.com/uibcdf/moli/issues/40):**
  the [workspace review](archive/python_314_workspace.md) replaces the
  obsolete eight-member/Praxis-scaffold description with received fourteen-member
  suite integration and separate Recorda/Praxis compatibility. Central guidance
  is delivered. Joint receiving with direct components, suite-owned TopoMT
  authorization/qualification and Recorda #26's public release remain distinct;
  #40 stayed partial at that earlier checkpoint. The receiving above now
  resolves its direct integration criterion. No primary environment, component
  source or guide was changed by the documentary reconciliation.

- **Bounded central review in [#62](https://github.com/uibcdf/moli/issues/62):**
  Recorda's current-core ecosystem review #2 is accepted as `adopted` in
  `moli.toml`, after independent published-receptor inspection of all eleven
  native jobs and required steps in original CI 37534456487. Distribution,
  OS, coverage and public release remain separate. The
  [receiving inventory](archive/application_diagnostic_policy.md) and
  [receipt](evidence/diagnostic_receiving_62_20261022.json) fix all five direct
  initial source identities. Sabueso #150, Praxis #13 and Recorda #29 now
  settle the direct receiving scope through qualified fixes, retained baselines
  and explicit optional deferrals; #62 is resolved. Provider publication is available,
  not a remaining blocker or automatic adoption. Nextia/Moli scaffolds have no
  present receiving runtime; Nextia development remains deferred. Suite #106
  retains independent member decisions. Final source/gates/cleanup are recorded
  in #62's delivery comment.

- **[#23](https://github.com/uibcdf/moli/issues/23), Discussions:** required
  Announcements/Q&A/Ideas and local extensions are accepted; all seven registered
  platform/root repositories are enabled and configured. API readback and
  Diego's reported UI checks are distinct evidence in the
  [archived decision](archive/github_discussions.md) and
  [receipt](evidence/github_discussions_23_20261021.json). Five component owner
  issues are closed; Sabueso preserves Data sources and both existing welcome
  threads survive. Suite [#120](https://github.com/uibcdf/molsyssuite/issues/120)
  stays open for its own versioned member rule and rollout. Root setup does
  not claim member adoption or Nextia runtime development. Final documentary
  source/CI/cleanup are recorded in #23's closeout.

- **[#46](https://github.com/uibcdf/moli/issues/46), bounded optional Ackredit review:**
  the [direct-consumer policy](policies/ackredit_client_policy.md), registered
  in `moli.toml`, accepts portable >=0.9.0, function providers/prepared credit
  >=0.11.0 and bounded recorder evidence/standalone validation >=0.12.0 as
  provider capability floors. Original public 0.11.0/0.12.0 bytes and metadata
  verify; all ten native original 0.12.0 receiving jobs/required steps pass.
  The recorded eight-cell/72-test reconstruction is reused with its original
  pinned PyUnitWizard scope, not claimed as new direct-consumer qualification.
  See the [archived review](archive/review_ackredit_optional_contracts.md) and
  [receipt](evidence/ackredit_optional_contract_review_46_20261021.json).
  Sabueso #108 and Praxis #9 retain their own required/optional profiles,
  tested ranges and owner-selected receiving. No dependency, component code,
  guide-copy rollout or general public 1.x acceptance is required. #36's
  obsolete pending-provider-delivery paragraph is corrected; its semantic
  exchange remains open. Nextia implementation remains deferred by the maintainer.
- **Contributor-instruction portion of [#34](https://github.com/uibcdf/moli/issues/34):**
  central reporting policy, root/starter/onboarding routes and all five direct
  component guide/root deliveries are on main under Diego's explicit direct-push
  authorization. The five bounded owner issues are closed with exact-head
  administrative evidence. Central [governance/coverage](https://github.com/uibcdf/moli/actions/runs/39663979062)
  passes all 54 tests and the [full guide audit](https://github.com/uibcdf/moli/actions/runs/39663979006)
  passes against actual component default branches. See the
  [partial issue record](pending_proposals/human_facing_issue_feedback.md) and
  [delivery receipt](evidence/human_facing_feedback_34_20261021.json).
  GitHub automatically recognized PR #72 as integrated after the direct push;
  no component PRs were needed. The scientist-facing pilot, project linkage,
  coding-agent handoff and opt-in verified-fix return remain open in #34 and
  suite #65. Final documentation-head CI and resource retirement are recorded
  in #34's closing work comment, not inferred from this implementation checkpoint.
- [#47](https://github.com/uibcdf/moli/issues/47), delivered through
  [PR #70](https://github.com/uibcdf/moli/pull/70): optional `archive/` refs preserve
  reviewed commits without public-release meaning. The native gate checks both
  current and historical-target enforcement; the regression fails before its
  correction and preserves the fixture tag. All 54 administrative tests,
  [merged-head governance/coverage](https://github.com/uibcdf/moli/actions/runs/39658459426)
  and [full guide audit](https://github.com/uibcdf/moli/actions/runs/39658459615)
  pass. The [archived decision](archive/archive_tags.md) and
  [nine-repository receipt](evidence/archive_tags_47_20261021.json) distinguish
  advance owner notices from future activation. Canonical guide copies are
  unchanged; no actual archive-tag push or package qualification is claimed.
- [PR #65](https://github.com/uibcdf/moli/pull/65) synchronizes the published
  Sabueso pinned-item integrity evidence. The maintained report and #3 now record
  the #79 fix and public 0.5.0 receipt; reference grammar, retention, resolution
  and Nextia interpretation remain open.
- [PR #66](https://github.com/uibcdf/moli/pull/66) accepts Praxis's four
  owner-reviewed engineering states and Linux/macOS arm64 claims in `moli.toml`.
  Distribution adoption covers its reviewed pre-publication route, not a public
  package claim. The [exact-head full guide audit](https://github.com/uibcdf/moli/actions/runs/39653313900)
  passed against fresh component default branches.
- [PR #67](https://github.com/uibcdf/moli/pull/67) integrates the bounded
  Sabueso–Recorda receiving example. On `06bc5ac`,
  [governance and default-branch coverage](https://github.com/uibcdf/moli/actions/runs/39653589638)
  and the [manually dispatched receiving workflow](https://github.com/uibcdf/moli/actions/runs/39653601505)
  passed with their mandatory native steps inspected. Local Python 3.14.7
  verification with published pytest-receptor 1.2.0 passed all 60 baseline and
  receiving cases; Ruff, formatting, governance and the fresh-copy guide audit
  also passed. Local source integration and the hosted pinned-public-provider
  lane are separate evidence. #36/#18 remain open for project context, retention,
  routing, telemetry and explicit Nextia interpretation.
- [#68](https://github.com/uibcdf/moli/issues/68): public GitHub Release titles
  use the exact version. The MolI rule and direct-component guide copies were
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

## Selected coordination at resumption

| MolI issue | Current boundary and next evidence |
| --- | --- |
| [#33](https://github.com/uibcdf/moli/issues/33) | Review the retrieval/archive/mirror boundary against pinned Sabueso source. The [candidate contract](pending_proposals/retrieval_archive_contract.md) separates existing local behavior from proposed project retention, sharing, storage and replay guarantees. Owner review and consumer acceptance remain open; no Nextia runtime or shared service is selected. |

The former #62 coordination is closed/completed; its accepted dispositions and
owner-local revisit triggers are recorded above and in the archived review.
Sabueso #150, Praxis #13 and Recorda #29 are completed receiving records, not
outstanding direct-component blockers. Suite #106 retains its independent scope.

## Other open MolI issues

- **Scientific and interoperability contracts:** [#3](https://github.com/uibcdf/moli/issues/3),
  [#17](https://github.com/uibcdf/moli/issues/17),
  [#22](https://github.com/uibcdf/moli/issues/22),
  [#28](https://github.com/uibcdf/moli/issues/28),
  [#33](https://github.com/uibcdf/moli/issues/33),
  and [#36](https://github.com/uibcdf/moli/issues/36). Several require a real
  consumer, implementation or owner decision; read the issue before treating
  the design as ready for closure.
- **Operations and governance follow-up:** [#8](https://github.com/uibcdf/moli/issues/8)
  has its administrative model settled; per-repository readiness/adoption and
  actual publication evidence remain owner-local, with suite #45 delegated.
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
   MolI and relevant owner issue states and their latest evidence.
2. Select one issue with the maintainer. Resolve its ownership boundary using
   [`MOLI_GUIDE.md`](../MOLI_GUIDE.md), applicable `moli.toml` policy entries and
   the relevant architecture decision. For MolSysSuite member work, notify its
   team through a linked suite issue rather than editing member repositories.
3. Update the owning issue with the decision, exact evidence and remaining
   limits. For MolI governance edits, run
   `python devtools/scripts/validate_governance.py`; verify applicable hosted
   gates on the delivered head. Refresh this checkpoint when the pause state
   or next resumption path materially changes.

The three-PR review and #47 policy decision are complete. Archive-tag activation
remains an owner-local future choice, with the separate Action applicability
notices and independent MolSysSuite rule retained. #34's contributor-instruction
step is complete; its scientist-facing pilot and notifications remain pending.
The bounded #46 provider-contract review is complete; owner-selected consumer
adoption is separate. Nextia runtime work remains deferred; #28/Nextia #1 must
not be taken as selected implementation work from this checkpoint.
The #23 platform policy/root configuration scope is complete; suite #120
retains delegated member policy and rollout. Recheck that owning issue before
claiming member adoption.
