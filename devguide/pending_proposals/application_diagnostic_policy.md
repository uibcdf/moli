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

The original receipt fixes full identities for the initial inspection; later
owner receiving is recorded below with its own implementation and evidence.

| Component | Observed boundary | Owner-local follow-up |
| --- | --- | --- |
| [Sabueso `f392844`](https://github.com/uibcdf/sabueso/tree/f392844ec48fd8364d83c72a9521808daf1c598a) | Import calls `ensure_configured`; provider recommendations include warning/logging capture. Its catalog emitter constructs a `DiagnosticBundle` with compatibility defaults. Metadata permits SMonitor >=0.17.0 / ArgDigest >=0.13.0, before the new capabilities. | [#150](https://github.com/uibcdf/sabueso/issues/150): decide setup/scoped-capture applicability and qualify import/first use/emission on selected installed providers. #31's basic adoption stays accepted. Source inspection does not prove a regression. |
| [Praxis `eb3b0c8`](https://github.com/uibcdf/praxis/tree/eb3b0c829b6466aa2080ce24e823bb749bb48ace) | Both real advice sites now enter a restrictive scope before registration and emission. Request first-use configuration remains explicit and preserves selected application/project policy. | [#13](https://github.com/uibcdf/praxis/issues/13): scoped advice adopted with installed receiving; pure registration-only behavior deferred with a concrete embedding trigger; audience maps/identity export not applicable to the current slice. See the dated receiving below. #10 compatibility remains separate. |
| [Recorda `b455ff5`](https://github.com/uibcdf/recorda/tree/b455ff5ec6fee206f8c077cbac45712f0b6c704b) | Argument pipelines use metadata-only diagnostics with an explicit safe baseline; recovery emits safe IDs. The completed inspection adapter resolves count-only facts without emitting or importing ArgDigest, with fresh-process guards. | [#29](https://github.com/uibcdf/recorda/issues/29): decide whether registration-only behavior enables another useful slice. Completed #21 presentation / #24 compatibility do not select a new argument path, per-call audience or nonbootstrap emission contract. |
| [Nextia `32d12e2`](https://github.com/uibcdf/nextia/tree/32d12e20fae26f00a523d0ed4812e46def8a64e9) | Tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration. Implementation remains deferred by Diego. |
| [Moli `08d0e2b`](https://github.com/uibcdf/moli-agent/tree/08d0e2b809e7e5c46add5ee554ae9528831f7454) | Agent tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration; no scaffold implementation is requested. |
| MolSysSuite | Delegated member governance, outside the direct runtime inventory. | [Suite #106](https://github.com/uibcdf/molsyssuite/issues/106) owns its independent dispositions: two settled and nine pending at this review. Do not translate that count into MolI adoption or edit members. |

## Praxis receiving — 2026-10-22 UTC

[Praxis #13](https://github.com/uibcdf/praxis/issues/13) implements the bounded fix
in `eb3b0c829b6466aa2080ce24e823bb749bb48ace`. The earlier source-only suspicion
was reproduced: both checker and recording-gap advice attached enclosing
scientific argument summaries, tags and ordinary extras across all four
audiences (eight expected failures before the fix). The local scope excludes
that context before event construction, keeps fixed safe messages/hints and
caller-approved primitive facts, and restores capture state. Imports are also
inside the presentation-failure guard. Retained findings, failed attempts and
native recording-error identity survive filtering and diagnostic failures.

Fresh disposable Linux x86_64/Python 3.14.9 environments installed the changed
Praxis wheel and original public provider files. The legacy cohort passes
199 tests with one explicit absent-MolSysMT skip; the latest cohort passes 196
with that skip and three absent-Recorda skips. All 43 diagnostic tests pass
without skips in each cohort. Public Recorda 0.3.0 remains incompatible with the
latest mandatory-provider cohort; its optional integration executes in the
legacy cohort. Both environments pass `pip check`. Provider archives and installed
Python files are verified against their Conda hashes. The
[owner receipt](https://github.com/uibcdf/praxis/blob/eb3b0c829b6466aa2080ce24e823bb749bb48ace/devguide/evidence/diagnostics_13_20261022.json)
and compressed closures retain identities, integrity-checked receptor summaries,
exclusions and the local wheel digest. This does not qualify a public Praxis
release or repeat #40's scientific MolSysMT receiving.

The ordinary exact-head [Python workflow](https://github.com/uibcdf/praxis/actions/runs/39827135703)
builds an unpublished candidate and runs installed Linux/macOS Python 3.11–3.14,
the routine Linux 3.14 wheel and latest-public-provider lane, quality and measured
coverage. [Local governance CI](https://github.com/uibcdf/praxis/actions/runs/39827135424)
is separate. Final native conclusions and the published GH Run Receptor capture
are recorded in #13; skipped optional steps are not passing test evidence.

The [owner decision](https://github.com/uibcdf/praxis/blob/eb3b0c829b6466aa2080ce24e823bb749bb48ace/devguide/DIAGNOSTICS.md)
retains the safe first-request baseline and compatibility console for direct
advice in an unconfigured process. Pure registration-only execution is deferred
until a concrete host requires no implicit handler or configuration; revisit
request setup and real emission together. This also leaves SMonitor's existing
empty-handler console fallback in place; the configured-application receiving
uses an application-owned sink and makes no handlerless-host claim.
Per-audience safe template maps and
identity export have no current local use case. No provider floor, application
policy, scientific contract, registry state or shared platform rule changes.

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

#62 stays `partial` until the remaining Sabueso #150 and Recorda #29 decisions
settle its receiving scope; Praxis #13 has its bounded owner disposition above.
The providers' original publication blocker is gone. No platform runtime,
shared correlation/routing/reliability contract, automatic diagnostic attachment
or Nextia interpretation is accepted here. Recorda's completed #14/#15 analyses
and [Lab #13](https://github.com/uibcdf/recorda-lab/issues/13)/[#14](https://github.com/uibcdf/recorda-lab/issues/14)
retain their bounded experimental scope; future shared contracts require their
own substantive MolI review.
