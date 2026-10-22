---
summary: Complete direct diagnostic receiving with bounded fixes and explicit deferrals.
issue: uibcdf/moli#62
status: resolved
opened: 2026-10-06
closed: 2026-10-22
verification: measured
area: [diagnostics, support-libraries, receiving]
blocked_by: []
supersedes: []
---

# Application-owned diagnostics and scoped capture

## Current outcome — 2026-10-22 UTC

The original advance notice in [MolI #62](https://github.com/uibcdf/moli/issues/62)
predates the implemented and published provider capabilities. This review
reconciles Recorda's completed core adoption and closes the direct receiving
scope through bounded Sabueso, Praxis and Recorda owner decisions. Optional
capabilities have explicit deferral/non-applicability and revisit triggers. The
[dated receipt](../evidence/diagnostic_receiving_62_20261022.json) records pinned
files, metadata and independently rechecked original Recorda CI. That initial receipt is source
inspection and original CI verification; later executed receiving is recorded
separately in the component sections below. No common provider upgrade or new
shared runtime contract is selected.

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
| [Sabueso `c31e8c9`](https://github.com/uibcdf/sabueso/tree/c31e8c9815cb8d08b495fe83dbc04e367771f361) | Reviewed argument-error paths now check caller capture permissions before repr/str. Existing import/bundle bootstrap is retained; effective unconfigured policy depends on provider import order. | [#150](https://github.com/uibcdf/sabueso/issues/150): scoped argument receiving adopted on capable public cohorts, application/project precedence and real emission qualified, registration-only setup deferred with an embedding trigger; safe audience maps/identity export not applicable. Older declared floors do not imply newer semantics. See the dated receiving below. |
| [Praxis `eb3b0c8`](https://github.com/uibcdf/praxis/tree/eb3b0c829b6466aa2080ce24e823bb749bb48ace) | Both real advice sites now enter a restrictive scope before registration and emission. Request first-use configuration remains explicit and preserves selected application/project policy. | [#13](https://github.com/uibcdf/praxis/issues/13): scoped advice adopted with installed receiving; pure registration-only behavior deferred with a concrete embedding trigger; audience maps/identity export not applicable to the current slice. See the dated receiving below. #10 compatibility remains separate. |
| [Recorda `ebe95dc`](https://github.com/uibcdf/recorda/tree/ebe95dcc8528cfa4760951a87c818b812c4ebbba) | Safe first-use argument setup and the completed nonemitting inspection adapter are retained. Recovery catalog registration preserves setup; actual emission retains the compatibility empty-handler console fallback. | [#29](https://github.com/uibcdf/recorda/issues/29): baseline retained with fresh-process installed receiving on both public cohorts; registration-only execution and per-call audience deferred with concrete triggers; safe audience maps/identity export not applicable to this slice. See the dated receiving below. #26's release decision stays separate. |
| [Nextia `32d12e2`](https://github.com/uibcdf/nextia/tree/32d12e20fae26f00a523d0ed4812e46def8a64e9) | Tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration. Implementation remains deferred by Diego. |
| [Moli `08d0e2b`](https://github.com/uibcdf/moli-agent/tree/08d0e2b809e7e5c46add5ee554ae9528831f7454) | Agent tree has no installable Python package or current diagnostic runtime to receive these APIs. | No present receiving boundary. Reassess at its first runtime/provider integration; no scaffold implementation is requested. |
| MolSysSuite | Delegated member governance, outside the direct runtime inventory. | [Suite #106](https://github.com/uibcdf/molsyssuite/issues/106) owns its independent dispositions: two settled and nine pending at this review. Do not translate that count into MolI adoption or edit members. |

## Sabueso receiving — 2026-10-22 UTC

[Sabueso #150](https://github.com/uibcdf/sabueso/issues/150) fixes diagnostic
construction in `c31e8c9815cb8d08b495fe83dbc04e367771f361`. Seven reproduced
cases on the original source evaluated rejected-value repr or native-error str
before SMonitor and replaced the intended `ArgumentError`. The bounded fix
consults the provider's capture permissions before formatting those payloads,
including shared option/field-path, structures, knowledge-query and threshold
errors. Detailed defaults, validation, units, schema and runtime floors remain.
The legacy capability-absence branch keeps detailed behavior; it does not
pretend an older provider offers scoped collection or application ownership.

Both selected public cohorts (SMonitor 0.19 / ArgDigest 0.15 and SMonitor 0.21 /
ArgDigest 0.16) pass 178 source and 178 installed-wheel cases each in disposable
Linux x86_64/Python 3.14.9 environments. All 21 new receiving cases pass without
skips. The public repository-input checkpoint passes 5,031 cases with ten
explicit unshared-original exclusions; those originals were not copied from the
caller checkout. Published pytest-receptor 1.2.1 artifacts are complete and
integrity-valid, with matching JUnit/native results. The
[owner receipt and compressed inputs](https://github.com/uibcdf/sabueso/blob/c31e8c9815cb8d08b495fe83dbc04e367771f361/devguide/evidence/diagnostic_receiving_150_20261022.json)
retain exact public archives, all 549 installed runtime-file hashes, dependency
closures, failed-harness/quota attempts and their successful recovery. The
Sphinx build with fatal warnings, fixture/dependency/governance and Ruff gates
pass. The [exact-head ordinary CI](https://github.com/uibcdf/sabueso/actions/runs/39842639454)
and [governance run](https://github.com/uibcdf/sabueso/actions/runs/39842643795)
have their final native gate/capture verification in #150.

Fresh processes qualify configured/project setup, reload and real emission,
including the compatibility empty-handler console fallback. With no explicit
setup, the original cohort selects ArgDigest's logging-on/warning-capture-off
baseline; the latest selects Sabueso's logging/warning-capture-on baseline.
This review preserves both rather than forcing a global reconfiguration.
The [owner decision](https://github.com/uibcdf/sabueso/blob/c31e8c9815cb8d08b495fe83dbc04e367771f361/devguide/DIAGNOSTIC_RECEIVING.md)
defers pure registration-only setup until a named host needs no implicit capture;
all imports and actual emission need review together. Safe audience maps/export
have no selected current boundary. No scientific/source operation bridge is added.

Real fixture-backed Card resolution retains source/status facts and its ordinary
Python warning through filtered or failed delivery. Rendered enrichment `detail`
can vary across capture policies because it uses catalog exception prose;
delivery tests compare within the same policy. No universal redaction or
byte-identical cross-policy detail is claimed. Independent `HTTPError` resource
warnings are reported in [Sabueso #151](https://github.com/uibcdf/sabueso/issues/151),
with ownership/allocation still to investigate. They are not suppressed or
translated into a platform receiving blocker, a release or scientific acceptance.

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

## Recorda setup decision — 2026-10-22 UTC

[Recorda #29](https://github.com/uibcdf/recorda/issues/29) records the bounded
decision and receiving in `ebe95dcc8528cfa4760951a87c818b812c4ebbba`. Runtime
implementation, dependency ranges, schema and application contracts are
unchanged. The explicit safe first-use argument baseline is retained; application
and project configuration take precedence. The completed #21 count-only
inspection path already resolves without emission, bootstrap or ArgDigest import.

Fresh processes distinguish repeated recovery-adapter registration from actual
emission and session recovery. Registration is nonconfiguring; real emission
keeps SMonitor's compatibility console fallback when handlers are empty, including
explicit application `handlers=[]`. Restrictive capture does not prevent that
bootstrap. Existing application sinks, hooks, native error identity/cause, fixed
recovery notes and incomplete work are preserved. This is qualification of the
retained behavior, not a reproduced Recorda runtime defect or a new setup API.

Two disposable Linux x86_64/Python 3.14.9 environments install the Recorda wheel
with verified original public legacy/latest provider files. Each passes all
357 tests without skips, explicitly enabling recovery, including twelve new
fresh-process setup cases. Both pass `pip check`; installed runtime bytes match
the unchanged source. The
[dated owner receipt](https://github.com/uibcdf/recorda/blob/ebe95dcc8528cfa4760951a87c818b812c4ebbba/devguide/evidence/diagnostic_setup_29_20261022.json)
and compressed dependency closures retain exact identities and integrity-checked
published pytest-receptor 1.2.1 results. The
[ordinary exact-head CI](https://github.com/uibcdf/recorda/actions/runs/39833860794)
and native gate verification are recorded in #29. This does not qualify another
public Recorda package; #26 remains independent.

The [owner decision](https://github.com/uibcdf/recorda/blob/ebe95dcc8528cfa4760951a87c818b812c4ebbba/devguide/DIAGNOSTIC_SETUP.md)
defers registration-only setup until a named embedding host needs no implicit
configuration/handlers; argument first use and real recovery emission must be
reviewed together. Per-call audience awaits a real need for different audiences
in one process. Safe audience maps and identity export have no selected current
boundary. No new dependency floor, provider rollout or shared rule is introduced.

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

## Closure and future receiving

All direct-owner decisions in this review now have an adoption with bounded
receiving, deferral with a reason/revisit trigger, or reasoned non-applicability.
Praxis #13, Recorda #29 and Sabueso #150 settle this scope. #62 is resolved and
this report is archived. Future optional adoption still needs its own exact
consumer/provider evidence; capability refusal or skipped cases cannot be
counted as passing selected-feature qualification. MolSysSuite #106 retains its
independent member decisions. Recorda #26, Sabueso #151 and consumer scientific
acceptance retain their separate owners and gates.

The providers' original publication blocker is gone. No platform runtime,
shared correlation/routing/reliability contract, automatic diagnostic attachment
or Nextia interpretation is accepted here. Recorda's completed #14/#15 analyses
and [Lab #13](https://github.com/uibcdf/recorda-lab/issues/13)/[#14](https://github.com/uibcdf/recorda-lab/issues/14)
retain their bounded experimental scope; future shared contracts require their
own substantive MolI review.
