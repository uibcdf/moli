---
summary: Accept optional archive refs without public-release meaning or automatic consumer rollout.
issue: uibcdf/moli#47
status: active
opened: 2026-10-21
closed:
verification: reproduced
area: [governance, release, history]
blocked_by: []
supersedes: []
---

# Optional archive tags — MOLI decision and receiving boundary

## Decision and authority

The maintainer authorized proceeding with #47 after the prior three-PR review.
Accept the reserved `archive/<description>` namespace as an owner-reviewed
opt-in capability. It preserves a commit and owner/purpose metadata, never a
package version, GitHub Release or publication qualification. The normative
rule is [release-version policy](../policies/release_version_policy.md#archive-tags),
registered separately in `moli.toml`. The public version parser is unchanged.

MOLI owns this rule for its own repository and direct components. MolSysSuite
retains its independent member decision under suite #84. Shared support providers
receive notice through their own governance; neither their release namespaces
nor their implementations change through this decision.

## What was inspected and executed

The [dated receipt](../evidence/archive_tags_47_20261021.json) retains nine exact
source heads, every observed workflow's hash/event filters, empty remote
`refs/tags/archive/` responses and three bounded publication-guard probes.
Its owner is MOLI #47; recheck before first activation or a changed caller or
publication route. Empty remote observations are dated facts, not a future ban.

| Owner | Observed route and disposition |
| --- | --- |
| Sabueso | Branch-only local governance; Conda release/manual/staging/promotion/withdrawal routes. `check_route` rejects an archive candidate before gate/registry access; its canonical parser control passes. Native all-tag enforcement still needs owner qualification before use. |
| Praxis | Branch-only local governance; manual/reusable unpublished builder and manual exact-file publisher. `identity` rejects the archive version; current source/canonical version passes the non-tagging identity control. Activation remains owner-local. |
| Nextia | Branch-only local governance; no package publisher in the inspected workflow inventory. No runtime or publication maturity inferred. |
| MOLI Agent | Branch-only local governance; no package publisher in the inspected workflow inventory. No agent runtime or publication maturity inferred. |
| Recorda | Unfiltered push quality route with a reviewed MOLI-core pin; manual candidate/publication routes use fixed 0.3.0 identity. Temporary archive-valued project metadata fails before archive access; the canonical control reaches an intercepted archive reader. This does not inspect or publish an artifact. |
| Pytest Receptor | Separately suite-governed receptor; current policy caller remains `policy-v1.5.4` with `tags: ["*"]`. Conda and PyPI publication remain owner-qualified routes. Suite #84 owns any later activation. |
| GH Run Receptor | Separately suite-governed receptor; current policy caller remains `policy-v1.5.4` with `tags: ["*"]`. GitHub and Conda publication remain owner-qualified routes. Suite #84 owns any later activation. |
| Conda action | Shared provider has Action-specific version refs and simulation/qualification workflows. No provider implementation, version alias or registry operation is changed; optional archival use belongs to its owner. |
| Sphinx action | Shared Action provider; no `.github/workflows` directory in the inspected source. No automatic activation, new conformance claim or change to its Action release namespace. |

The provider probes import only their recorded source into an owned scratch
process and intercept consequential calls. They prove the stated guard behavior,
not complete publication safety, user installation, artifact closure or source
CI. No scientific functions, private content, package builds or registry writes
were used. Full workflow hashes let owners inspect the other maintained routes
before any future activation.

## MOLI implementation

`check_archive_tags.py` supplies a read-only native gate and reusable workflow
configuration helper. PyYAML's BaseLoader preserves string event keys, while a
duplicate-key rejection prevents ambiguous configuration. All-tag coverage and
an unconditional failure-gating exact command/caller are checked separately from
the actual implementation and native run evidence. Equivalent native owner gates
remain permitted; existing component checkers do not import a new dependency.

MOLI's governance workflow now includes `tags: ["**"]`, full tag acquisition,
the explicit archive check and pinned PyYAML 6.0.3. MOLI has no package publisher.
The regression suite preserves an annotated tag's object/commit in a temporary
real Git repository, rejects archive public/project versions and noncommit
targets, checks optional pinned issue records, and rejects incomplete, filtered,
conditional, tolerated or mismatched caller routes. A CLI negative rejects an
archive release candidate before even reading a repository.

This configured/native branch verification does not manufacture an archive-tag
event. Historical targets require review of the workflow actually selected at
that ref; changing current `main` cannot retrofit an older workflow. Keep those
original refs intact and select a reviewed owner enforcement route before use.

## Delivery and closeout

The canonical `MOLI_GUIDE.md` already routes component readers to the normative
release policy. Its bytes and all five delivered copies remain unchanged.
There is no mandatory caller upgrade, source-tag change or consumer activation.
Owner notices must precede provider publication and remain distinct from any
later adoption. Record those notice URLs and the immutable published MOLI source
with exact-head CI in the final closeout of #47.

Advance notices for prepared implementation `e093b13df7fe2cc1c84b5be676ff008ed55cdd04`
were delivered before pushing its branch:

- [MOLI #47](https://github.com/uibcdf/moli/issues/47#issuecomment-6324036981);
- [Sabueso #34](https://github.com/uibcdf/sabueso/issues/34#issuecomment-6324037910),
  [Praxis #9](https://github.com/uibcdf/praxis/issues/9#issuecomment-6324038873),
  [Nextia #2](https://github.com/uibcdf/nextia/pull/2#issuecomment-6324039898),
  [MOLI Agent #1](https://github.com/uibcdf/moli-agent/pull/1#issuecomment-6324040839)
  and [Recorda #3](https://github.com/uibcdf/recorda/issues/3#issuecomment-6324041590);
- [MolSysSuite #84](https://github.com/uibcdf/molsyssuite/issues/84#issuecomment-6324042428)
  for its independent member boundary and both receptors;
- [Conda action #52](https://github.com/uibcdf/action-build-and-upload-conda-packages/issues/52)
  and [Sphinx action #11](https://github.com/uibcdf/action-sphinx-docs-to-gh-pages/issues/11)
  for separately owned optional applicability reviews.

The notices preserve existing completed issue dispositions and introduce no
immediate consumer migration or release. The two Action owner reviews remain
independent follow-ups; no Action implementation is part of this MOLI decision.

The implementation/decision is complete only after its local checks, current
guide audit and exact-head hosted governance pass and the notices are recorded.
Future consumer activation is explicitly deferred to its owner and is not an
uncompleted general rollout promised by this decision.
