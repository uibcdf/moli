---
summary: Accept bounded public Ackredit promises for optional direct-component use.
issue: uibcdf/moli#46
status: resolved
opened: 2026-10-04
closed: 2026-10-21
verification: inspected
area: [attribution, interoperability, governance]
blocked_by: []
supersedes: []
---

# Ackredit optional-contract review

## Decision

The principal developer selected this bounded MOLI review on 2026-10-21,
keeping Nextia development deferred. Accept the provider-owned public promises
in the [direct-consumer policy](../policies/ackredit_client_policy.md): portable
attribution from 0.9.0, function providers/prepared credit from 0.11.0, bounded
recorder evidence and standalone validation from 0.12.0. General public 1.x
remains a separate delivery decision. Earlier provisional releases retain
their original classifications; green tests do not retroactively promote them.

The original #46 proposal predates these decisions and public deliveries.
Ackredit owns the APIs and guide; MOLI records its direct-consumer acceptance.
MolSysSuite's independent [#97 review](https://github.com/uibcdf/molsyssuite/issues/97)
is complete and does not substitute for this decision or for direct receiving.
No mandatory dependency, upgrade, host schema or implementation is introduced.

## Provider evidence and limits

The [review receipt](../evidence/ackredit_optional_contract_review_46_20261021.json)
records pinned source/receipt digests, original public-file checks and native
receiving evidence. In particular:

| Public delivery | Original producer | Original file SHA-256 |
| --- | --- | --- |
| 0.11.0, `ackredit-0.11.0-py_0.tar.bz2` | `85deae594e65b2fd443d6ca9a7347eb2bda537e1` | `df8963ca2d286f50b19eb778e95c54c5ebb79c12fb55a6504e7c23daf5717d4f` |
| 0.12.0, `ackredit-0.12.0-py_0.tar.bz2` | `6f4dbf39996a7185b8aaff7c52b9daeb167a100a` | `160b452c2b9de3b44bc6c6e2f4bd8c47e44b1d2779b620f63048231708a1d4aa` |

Both original public files were downloaded read-only and their bytes and
Conda identity checked; no package was installed, rebuilt or published.
Provider source acceptance, exact-file public delivery, guide copies and
runtime adoption remain distinct. The canonical guide's current pinned source
`315e0da41f0b7ec5f343984a297c98b94be40b53` still matches the owner-delivered
SHA-256 `6353892d552eab79973cecec5f8e3c8c31e146416e1cb481786e21cd3fcbf99d`.

The original [0.12.0 receiving run](https://github.com/uibcdf/ackredit/actions/runs/37588186298),
attempt 1, is bound to that producer. All ten native jobs and their required
steps were rechecked through published GH Run Receptor 1.2.0; its complete
capture's six member hashes verify. The earlier
[independent suite review](https://github.com/uibcdf/molsyssuite/blob/ca96503f1049fcf7b16c8dd364510e8f1468a891/devguide/rollouts/ackredit_public_contract_review_97_20261008.json)
reconstructed eight Linux x86-64/macOS arm64 × Python 3.11–3.14 cells, 72
mandatory tests, no skips/deselections and all ten original artifact digests.
This review reuses that recorded reconstruction; it does not re-download or
reconstruct the original artifact ZIPs, rerun those tests or certify a current
Sabueso/Praxis release. Its real producer is pinned PyUnitWizard
`0e422d06b0af56e4dd2b43cafd00f059221eb405`, not a direct MOLI client.

## Direct-consumer inventory and ownership

These are source-inspected profiles, not new installed qualifications.

| Direct component | Inspected source and disposition |
| --- | --- |
| Sabueso | `7d1354753d3486a5e32e0a1fd830ac043c779c1d`: required `ackredit>=0.9.0`; application-owned sessions and detached host attribution. [Sabueso #108](https://github.com/uibcdf/sabueso/issues/108) retains actual bibliography/receiving, failures and release claims. Choose later optional APIs only for a concrete need and qualify that path; keep the portable route and existing product dependency. |
| Praxis | `55b7d6d2f9f7495a148ebe4d6bbc7acbffd9a512`: optional attribution extra `ackredit>=0.12,<0.13`; the inspected lazy adapter borrows the current application session and calls portable `capture`. Preserve that tested range. [Praxis #9](https://github.com/uibcdf/praxis/issues/9) retains installed/dependency evidence; this does not infer observer/evidence adoption from the extra's floor. |
| Recorda | `b455ff5ec6fee206f8c077cbac45712f0b6c704b`: no Ackredit dependency or extra in its metadata. Carrying original detached records in a bounded MOLI example does not create a provider-observer integration obligation. Shared exchange remains #36. |
| Nextia and MOLI Agent | Registered design-stage components without Python-package capability. No receiving rollout or implementation is opened here; Nextia remains deferred by the maintainer. Reassess only when an owner selects an actual attribution boundary. |
| MolSysSuite | Delegated member policy and the six registered guide copies remain owned by [suite #97](https://github.com/uibcdf/molsyssuite/issues/97), not this direct-component inventory. |

Sabueso #108 and Praxis #9 receive the optional capability/receiving handoff;
their existing unrelated acceptance states and scientific debt remain intact.
No component, suite or member source is edited. `MOLI_GUIDE.md` is unchanged;
the new policy is discoverable through `moli.toml` and the devguide index, so
this review requires no five-repository canonical-guide delivery.

## Related correction and remaining work

The #36 [knowledge-attribution report](../pending_proposals/knowledge_pipeline_attribution_boundary.md)
still called the portable API provisional and public delivery pending. Its
availability paragraph is corrected using the owned public evidence. The
original composition-only pilot remains historical; later acquisition/results
need their own source/release receipts. #36 stays open for its actual shared
exchange/project acceptance, with Nextia implementation still deferred.

This completes #46's bounded central review. Runtime use is owner-selected;
optional future adoption is not an outstanding requirement for closing this
review. Provider fixes belong to Ackredit; concrete consumer work belongs to
its owning issue. General future 1.x and project interpretation remain separate.

## Validation and resource lifecycle

Run MOLI's governance/archive-tag checks, document links, JSON/TOML consistency
and whitespace checks before direct publication. The owning #46 closeout records
the ordinary unskipped final-head native governance/coverage result. This is
administrative evidence, not scientific or consumer-package qualification.

Owned temporary downloads, source snapshots, inspection tool/caches and captures
are retired after final verification and handoffs. Retain only the normalized
repository receipt, owned by MOLI #46 with review when provider promises,
canonical guide or a selected consumer boundary changes.
