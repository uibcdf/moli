---
summary: Reconcile qualified core adoption and inventory optional diagnostic receiving.
issue: uibcdf/moli#62
status: partial
opened: 2026-10-06
closed:
verification: inspected
area: [diagnostics, support-libraries, receiving]
blocked_by: []
supersedes: []
---

# Application-owned diagnostics and scoped capture

## Current outcome — 2026-10-22 UTC

The original advance notice in [MolI #62](https://github.com/uibcdf/moli/issues/62)
predates the implemented and published provider capabilities. This review
reconciles Recorda's completed core adoption and inventories every direct
component. Optional receiving decisions stay with their owners. The
[dated receipt](../evidence/diagnostic_receiving_62_20261022.json) records pinned
files, metadata and independently rechecked original Recorda CI. It is source
inspection and CI verification, not new component execution or qualification.

The existing [support-library policy](../policies/python_support_libraries_policy.md)
applies. Recorda's ecosystem state changes from `partial` to `adopted` for its
completed current-core review in [Recorda #2](https://github.com/uibcdf/recorda/issues/2).
Applicable ArgDigest and SMonitor paths have implementation and test evidence.
DepDigest has no Recorda-owned optional/backend loader; PyUnitWizard has no
current quantity parsing/conversion/validation boundary. Their documented
reassessment triggers remain. Scientific target arguments stay producer-owned.
This covers the core reviewed in #2, not every later optional feature.
Distribution, OS, coverage and a new public release retain separate reviews;
in particular [Recorda #26](https://github.com/uibcdf/recorda/issues/26) remains open.

## Provider capability versus consumer adoption

| Capability | Public provider contract | Receiving implication |
| --- | --- | --- |
| Restrictive collection, explicit argument pipelines and preservation of selected application policy | SMonitor 0.19.0; ArgDigest 0.15.0 for its scoped instrumentation and pipeline selection. Provider issues: SMonitor #37/#38, ArgDigest #29/#30. | Recorda's core qualifies these paths. A scope must begin before payload collection; explicit safe fields do not sanitize previously constructed text or inherited context. |
| Registration without bootstrap, including real emissions | SMonitor 0.20.0 adds `bootstrap_policy=False` to bundles/emission; default remains `True`. ArgDigest 0.16.0 supplies registration-only initialization when this capability exists, public registration/setup APIs and explicit refusal when unavailable. | ArgDigest 0.16.0 alone is insufficient with an older SMonitor. A consumer's explicit `ensure_configured` still selects a first-use baseline. Registration and restricted collection do not prove absence of bootstrap during emission. |
| Safe audience-specific templates and bounded identity export | SMonitor 0.21.0: [capture contract](https://github.com/uibcdf/smonitor/blob/066b69cad8896cdc126d5586fd53268af4ea6490/docs/content/user/library-integrators/scoped-capture.md), [export contract](https://github.com/uibcdf/smonitor/blob/066b69cad8896cdc126d5586fd53268af4ea6490/docs/content/user/bundles-and-export.md). | Optional owner-selected use. Bounded primitive facts are caller-approved, not automatically secret-free. Identity bundles have omissions and are neither a complete history nor Recorda's journal. |

Publication has provider and independent MolSysSuite receipts linked in #62,
[ArgDigest #32](https://github.com/uibcdf/argdigest/issues/32) and
[suite #106](https://github.com/uibcdf/molsyssuite/issues/106). This review checks
their recorded status and pinned public source contracts; it does not repeat
provider matrices or download/requalify Conda archives. No common dependency-floor
upgrade or rich-default change is selected. New releases do not reopen completed
local reviews automatically. No shared rule is added to the normative policy.

## Direct-component inventory

The receipt fixes full identities; links select the inspected main snapshots.

| Component | Observed boundary | Owner-local follow-up |
| --- | --- | --- |
| [Sabueso `f392844`](https://github.com/uibcdf/sabueso/tree/f392844ec48fd8364d83c72a9521808daf1c598a) | Import calls `ensure_configured`; provider recommendations include warning/logging capture. Its catalog emitter constructs a `DiagnosticBundle` with compatibility defaults. Metadata permits SMonitor >=0.17.0 / ArgDigest >=0.13.0, before the new capabilities. | [#150](https://github.com/uibcdf/sabueso/issues/150): decide setup/scoped-capture applicability and qualify import/first use/emission on selected installed providers. #31's basic adoption stays accepted. Source inspection does not prove a regression. |
| [Praxis `55b7d6d`](https://github.com/uibcdf/praxis/tree/55b7d6d2f9f7495a148ebe4d6bbc7acbffd9a512) | Request digestion bootstraps a safe first-use baseline inside a metadata-only scope. Lazy catalog advice registers and emits without a local restrictive scope or nonbootstrap option. Recommendations disable global capture. | [#13](https://github.com/uibcdf/praxis/issues/13): decide inherited-context treatment and behavior in unconfigured applications at request/advice boundaries. #10's latest-provider compatibility stays accepted separately. No leak or policy corruption was reproduced here. |
| [Recorda `b455ff5`](https://github.com/uibcdf/recorda/tree/b455ff5ec6fee206f8c077cbac45712f0b6c704b) | Argument pipelines use metadata-only diagnostics with an explicit safe baseline; recovery emits safe IDs. The completed inspection adapter resolves count-only facts without emitting or importing ArgDigest, with fresh-process guards. | [#29](https://github.com/uibcdf/recorda/issues/29): decide whether registration-only behavior enables another useful slice. Completed #21 presentation / #24 compatibility do not select a new argument path, per-call audience or nonbootstrap emission contract. |
| [Nextia `32d12e2`](https://github.com/uibcdf/nextia/tree/32d12e20fae26f00a523d0ed4812e46def8a64e9) | Tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration. Implementation remains deferred by Diego. |
| [Moli `08d0e2b`](https://github.com/uibcdf/moli-agent/tree/08d0e2b809e7e5c46add5ee554ae9528831f7454) | Agent tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration; no scaffold implementation is requested. |
| MolSysSuite | Delegated member governance, outside the direct runtime inventory. | [Suite #106](https://github.com/uibcdf/molsyssuite/issues/106) owns its independent dispositions: two settled and nine pending at this review. Do not translate that count into MolI adoption or edit members. |

## Registry acceptance evidence

Recorda's accepted implementation is
`c6248686815bd405a08955565e4fdc232bcef906`, with resolved documentation at
`b3a53770e3b9917e5ff399dbfc00a9c53f2a37ac`. Owner receipts report 221
source/installed tests, or 209 plus 12 explicit recovery skips in the ordinary
lane. These are historical owner counts, not tests executed here.

Published GH Run Receptor 1.2.0 independently recaptures
[original run 37534456487](https://github.com/uibcdf/recorda/actions/runs/37534456487),
attempt 1: the exact implementation above, successful ordinary push on main.
All six captured members verify size and SHA-256. Native jobs and required
steps pass: quality, six installed-package Linux/macOS lanes and four explicit
published-SMonitor recovery lanes across Python 3.11–3.14. Installation,
dependency consistency, provider verification and installed tests actually ran.
The receipt retains native steps and test-log excerpts separately from owner
local counts. No skipped run is used as passing evidence.

Current pinned source retains the applicable adapters, metadata and regressions.
Its wider ranges from #24 do not retroactively qualify another public Recorda
package. This correction changes neither those ranges nor its empty registered
OS claims or other review states.

## Remaining decisions and closure

Each relevant optional boundary needs an adoption with receiving evidence,
deferral with reason/revisit trigger, or reasoned non-applicability in its owner
issue. Review fresh configured/unconfigured processes, import/first use/repeated
registration and real emissions. Preserve native errors, application hooks and
handlers, scientific results, safe-field boundaries and fallback behavior.
Capability refusal must fail selected-feature qualification rather than become
an unnoticed passing skip.

#62 stays `partial` until the three direct-owner decisions settle its receiving
scope. The providers' original publication blocker is gone. No platform runtime,
shared correlation/routing/reliability contract, automatic diagnostic attachment
or Nextia interpretation is accepted here. Recorda's completed #14/#15 analyses
and [Lab #13](https://github.com/uibcdf/recorda-lab/issues/13)/[#14](https://github.com/uibcdf/recorda-lab/issues/14)
retain their bounded experimental scope; future shared contracts require their
own substantive MolI review.
