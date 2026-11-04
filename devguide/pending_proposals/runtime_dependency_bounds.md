---
summary: Evaluate minimum-only runtime requirements with justified exceptions and separate compatibility evidence.
issue: uibcdf/moli#76
status: partial
opened: 2026-10-24
closed:
verification: inspected
area: [governance, distribution, compatibility]
blocked_by: []
supersedes: []
---

# Runtime dependency bounds: central evaluation

## Outcome for maintainer review — 2026-11-04

**Recommendation:** use `provider>=X` as the general runtime declaration, where
`X` is the evidenced consumed-API floor. Require a concrete compatibility reason
for a ceiling, exclusion or narrower range. Keep exact qualification pins and
separate public-provider monitoring. Apply the same reasoning to optional runtime
features without making them mandatory.

This is a **completed evaluation and proposed decision**, not an accepted MolI
rule or a command to remove component bounds. [MolI #76](https://github.com/uibcdf/moli/issues/76)
owns the principal-maintainer decision. MolI's current distribution/CI policies,
canonical guide and registry remain unchanged by this review. Component teams
own metadata, recipes, provider contracts, CI and publication; Nextia runtime
remains deferred. MolSysSuite independently owns its member rule and adoption.

## Evidence and its limits

The [inspection receipt](../evidence/runtime_dependency_bounds_76_20261104.json)
binds exact source/file identities and records what was inspected. No dependency
solve, provider matrix, consumer test, package installation or scientific
validation is newly executed for this documentation task.

| Direct Python component | Fixed source inspected | Current declarations and conclusion |
| --- | --- | --- |
| Sabueso | `ca9e0f376f4f2f62ac817de82a8da3886efae16a` | Required `smonitor>=0.17.0`, `pyunitwizard>=0.27.0`, `argdigest>=0.13.0`, `depdigest>=0.11.0`, `ackredit>=0.9.0`; recipe required names/ranges agree. Already minimum-only in shape; this does not verify every advertised floor or optional feature. |
| Praxis | `17e1856fa45a50b26097b19be28accb7ab88f689` | Required ArgDigest `>=0.15,<0.18`, DepDigest `>=0.13,<0.16`, SMonitor `>=0.19,<0.23`, PyUnitWizard `>=0.28.1,<0.30`; recipe agrees. Optional recording is `recorda>=0.3,<0.4`, attribution `ackredit>=0.12,<0.13`. Owner review must establish reasons/exit conditions before retaining or changing bounds. |
| Recorda | `ff52fa5d8628d796f413b833c8abe73907990cf9` | Required `argdigest>=0.15.0`, `smonitor>=0.19.0`; recipe agrees. Its accepted local policy and public 0.3.3 provide a concrete minimum-only example, not proof of a universal platform rule. |

Nextia and Moli have no registered `python-package` capability in the inspected
MolI registry. This review prescribes no artificial runtime requirements or
compatibility lane for those scaffolds. MolSysSuite member declarations are not
inventoried or modified here.

### Recorda's measured local experience

[Recorda #35](https://github.com/uibcdf/recorda/issues/35) removed automatic
next-minor caps after the previous bounds rejected a later provider cohort even
though a bounded receiving exercise passed. Its
[maintained policy](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/devguide/DEPENDENCY_POLICY.md)
preserves exact qualification coordinates while adding a weekly/manual
latest-public installed lane. The source-bound
[hosted receipt](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/devguide/evidence/dependency_policy_35_hosted.json)
reports 14 source jobs and two latest-public jobs; the latter ran 408 tests per
Linux/macOS arm64 Python 3.14 cell. The
[0.3.3 release receipt](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/devguide/evidence/release_0_3_3.json)
and [MolI #78](https://github.com/uibcdf/moli/issues/78) retain later public-file
and release evidence. Those are owner-reported, inspected historical results;
their runs, archives and scientific scope are not requalified here.

The current latest workflow selects stable public coordinates, verifies installed
file/import identities and dependency closure, tests the installed consumer,
retains evidence on failure and does not tolerate a failed test lane. The fixed
cohort and latest-public cohort remain distinct. Neither proves every declared
minimum, every combination of admitted versions or future compatibility.

### Independent MolSysSuite decision

[MolSysSuite #137](https://github.com/uibcdf/molsyssuite/issues/137) already accepts
the general `provider>=X` rule at
[`3feec0e6534200820a53fd4b131609ce38b653f9`](https://github.com/uibcdf/molsyssuite/blob/3feec0e6534200820a53fd4b131609ce38b653f9/devguide/python_distribution_policy.md#runtime-dependency-version-bounds),
with justified API/ABI/scientific exceptions and member-owned floor/exception
review still partial. This is relevant alignment evidence, not adoption by MolI
or authority to change member repositories.

## Proposed normative text

On acceptance, incorporate this section into MolI's single
[distribution policy](../policies/python_distribution_policy.md), register it
and link onboarding/CI guidance. It is not a second dependency manifest.

### General runtime interval and exceptions

Declare a required runtime provider as `provider>=X`, with an evidenced minimum
for the contracts actually consumed. Apply this default to required dependencies
and optional runtime features, keeping features optional. Newer published siblings
are the intended compatible direction; admitting selection does not certify that
an unexecuted version works.

Add a ceiling, exclusion or narrower interval only for a concrete incompatible
API, ABI, scientific, runtime or supported-engine contract. A provider's documented
breaking boundary may justify a prospective restriction without waiting for a
production failure. A new version number, pre-1.0 status or absence of tests alone
does not justify a mechanical next-minor cap. Retain real native ABI/run-export,
platform and qualified optional-engine restrictions while necessary.

Record provider/affected versions, the consumed contract, evidence or documented
boundary, owning issue, responsible owner, interim interval and review/removal
condition. Report incompatibilities through the owning feedback route; external
publication follows its separate approval rule. Do not remove an existing cap
until its owner has reviewed the reason and applicable receiving evidence.

### Minimum support, parity and reproducibility

Derive `X` from the minimum published version providing the consumed API and test
that boundary. The lowest declared number or the latest version that happened to
pass is not an API-floor proof. Retain the actual tested cohort, installed origin,
platform/Python scope and unresolved gaps. Where all minima cannot form one valid
closure, distinguish a per-provider minimum test with compatible peers from a
combined-minima claim. This does not demand an exhaustive Cartesian product.

Keep `pyproject.toml` and recipe runtime intervals consistent. Preserve dependency
optionality, explicit name translations and scoped route constraints. Exact
version/build/digest or full-source pins remain appropriate for reproducible
development/build environments, CI and release qualification; they serve a
different purpose from the public runtime interval. Python support and existing
candidate/installed-artifact gates remain separately governed.

### Observe current public compatibility separately

Use applicable scheduled/manual compatibility checks for newer public providers,
separate from a fixed-cohort verifier. An initial useful route uses routine Python
3.14 on Linux and the additional claimed platforms where affected contracts need
coverage; retain the existing supported-minor/OS and exact-release requirements.
The component records cadence, scope and justified gaps. This does not add a full
scientific suite to every internal push or resume deferred scientific work.

Retain selected stable public version/build/file identities, index/source basis,
installed origins, clean dependency closure, consumer source/artifact, meaningful
consumed-contract results and actual exclusions. A constrained older selection
must not be called the newest public provider; surface the excluded newer version
and its reason. Distinguish a public installed lane from source co-development.
Neither solver success nor synthetic version-metadata fixtures prove runtime or
scientific compatibility.

A failed or incomplete selection/installation/test remains visible with its
identities and an owning report. Do not silently rewrite the qualified-cohort
verifier, hide the failure or relabel its selected closure as qualified. Preserve
old releases/files and their original receipts. Changes to minimums, caps or
compatibility claims follow component review and applicable release gates.

## Alternatives considered

| Approach | Benefit | Cost / disposition |
| --- | --- | --- |
| Automatic next-minor caps | Restricts resolver choices to previously considered intervals | Repeated consumer metadata releases even without a provider defect; a broad interval still does not prove every admitted combination. Reject as the general rule. |
| Exact pins in public runtime requirements | Selects a narrowly repeatable declaration | Conflates user compatibility with a qualification environment, restricts co-installation and still does not preserve a complete transitive closure. Keep exact pins for qualification, not as the universal runtime default. |
| Minimum-only plus owner-reviewed exceptions and separate monitoring | Reduces purely numerical solver blocks; preserves explicit compatibility limits and reproducible evidence | Requires maintained floor/contract review and visible failure handling. Recommended. |
| Scope the default only to UIBCDF siblings | Addresses the demonstrated receiving problem narrowly | Leaves arbitrary third-party caps unreviewed. Prefer a general declaration principle with actual third-party/native/scientific restrictions preserved by evidence. |

## Owner actions after a decision

1. Principal maintainer accepts the text above or records a justified alternative
   in #76. Until then this remains a proposal; accepted registry/guide bytes stay
   unchanged.
2. MolI publishes the central rule and a linked rollout inventory. Its central
   policy decision may then close with component work explicitly assigned and
   tracked separately, rather than claiming all metadata is migrated.
3. Sabueso's team reviews actual floors, optional contracts and monitoring in its
   existing distribution/ecosystem routes; its minimum-only metadata needs no
   mechanical rewrite. Recorda's team retains its existing local rule/evidence and
   reviews any remaining minimum/monitoring coverage without reopening a resolved
   release as an unverified defect.
4. Praxis's team inventories the four required and two optional intervals,
   establishes reasons/exit conditions and chooses tested retention or changes.
   Existing #14 receiving stays historical; central review does not extend it.
5. MolI returns its accepted boundary through suite #137, leaving all member
   changes to MolSysSuite. Concrete owner notices require their normal reporting
   and publication authority; none is sent by this evaluation step.

## Acceptance state

- [x] Inspect current direct Python declarations, recipe parity and the original
  Recorda/MolSysSuite decisions at fixed source identities.
- [x] Compare alternatives, failure modes, scope and meaningful minimum/latest
  qualification without inventing compatible provider versions.
- [x] Prepare concrete normative text and separate central/team responsibilities.
- [ ] Record the principal-maintainer decision in #76.
- [ ] If accepted, publish policy/registry/guide links and explicit owner handoffs;
  retain actual component adoption and public release evidence separately.

No runtime code, requirements, recipe, workflow, guide copy, environment, package,
tag or existing scientific contract changes in this evaluation. The receipt and
proposal support a decision, not an installed compatibility claim.

Local review checks pass: `validate_governance.py`, 59 Markdown targets/anchors,
all eleven public-file Git-blob/content identities, the five unchanged local
policy/registry/guide hashes and whitespace. This documentation-only evaluation
does not defer a changed-code test or claim a new remote/component qualification.
