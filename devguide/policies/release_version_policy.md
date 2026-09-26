# MOLI Release Version Policy

Normative for public releases of MOLI repositories unless an explicit exception applies.

## Public identity

Public releases use exactly `X.Y.Z`: three non-negative decimal integers without
leading zeroes except for zero itself, no `v` prefix and no alpha, beta, rc,
dev, post, or local suffix. The accepted pattern is recorded in `moli.toml`.

The project/package version, Git tag, and GitHub Release tag use the same public version.

Development checkouts may carry truthful derived/local identities; these are provenance, not public release versions.

## Candidates

Candidate evaluation belongs in staging and exact commit evidence rather than public prerelease tags.

## Candidate evidence lifecycle

Before tagging or publishing, compare every required gate's evidence with the
candidate it is meant to certify. A reviewable receipt or release checklist
records, for each gate:

- the repository or component whose result is claimed, the exact source commit,
  intended public version and build or distribution route where applicable;
- the gate name, result, run or evidence link, and tested scope such as operating
  system, Python minor, or paired components;
- immutable identities of the inputs the gate observed: applicable dependency
  metadata and resolved closure, recipe/build inputs, generated runtime resources,
  and the candidate artifact coordinate and content digest once built.

A receipt names every component and artifact consumed by a combined gate. The
identity can be recorded in a machine-readable manifest or an inspectable release
record; this policy does not prescribe a file format or workflow layout. Missing or
ambiguous input identity cannot establish that old evidence still applies.
For a Python distribution route carrying generated or vendored runtime resources,
the receipt includes that route's archive inspection and installed-runtime result
under the [distribution policy](python_distribution_policy.md#generated-resources-in-release-artifacts).
Evidence from a different route does not certify the resource bytes in this one.

If a source commit, dependency contract or resolved closure, recipe/build input,
generated resource, candidate artifact, or tested scope changes, mark each gate
that consumed it **stale** and rerun that gate against the new candidate. Keep its
old result as historical or diagnostic evidence; do not relabel it as a pass for
a new commit or artifact. A source-commit change requires fresh exact-commit
source gates even if a previous run passed. An unchanged artifact or component
gate may be reused only when its own recorded inputs and scope, including an
artifact digest when the gate consumed an artifact, are demonstrably unchanged.
A combined installed-package gate must be rerun if any participant or dependency
closure it observed changes; another participant's unchanged artifact does not
need to be rebuilt for that reason alone.

The pre-publication decision records which gates were reused, which became stale,
and the new evidence that replaced each stale result. A passing status applies
only to the identity and scope actually observed. Repositories keep their own
gate implementations and may impose stricter invalidation rules. [MOLI #24](https://github.com/uibcdf/moli/issues/24)
tracks this platform rule; MolSysSuite owns member adoption and its coordinated
release refinements.

The [reference evaluator](../../devtools/scripts/release_evidence.py) and
[mutation fixtures](../../tests/test_release_evidence_policy.py) illustrate
input-bound evidence and selective reuse. Their data format is illustrative;
the rules above are the contract.

## Bounded release-gate exceptions

A required gate keeps its observed status and evidence: `failed`, `skipped`,
`cancelled` or tolerated failure is never reported as `passed`. If the repository's
release authority permits publication with an unmet gate, record a separate
**release decision with exception** before tagging or publishing. The minimum
reviewable record identifies:

- the exact repository, source commit, intended release version and candidate
  artifact identity where the gate consumed an artifact;
- the gate, affected capability, platform and other tested scope, its authoritative
  result, observed failure or reason for no result, and run/evidence link;
- compensating evidence and its limits, the decision owner and dated decision link;
- the owner-local remediation issue, the limitation communicated with the release,
  and an expiry or explicit re-decision condition.

The exception authorizes only the named release candidate and gate scope. It does
not change the gate result, certify an untested platform or capability, or satisfy
a later candidate, later public version, or 1.0 readiness gate. Before any such
later decision, rerun or re-evaluate the gate under the candidate evidence
lifecycle and explicitly accept a new bounded exception or remove the old one.
An expired exception blocks the claim until a new decision is recorded. Preserve
the unresolved remediation issue and truthful release/status wording while the
gate remains unmet; do not weaken, skip or relabel the test to make a green result.

Each repository defines its specialized release gates, decision authority and
which gates, if any, may receive an exception. The decision cannot override a
non-waivable gate or a separate platform support requirement. Scientific
correctness or safety gates may be declared non-waivable. MolSysSuite may impose
member-specific approval and admission requirements; this platform rule governs
the meaning and traceability of the evidence. The [reference evaluator](../../devtools/scripts/release_evidence.py)
and [negative fixtures](../../tests/test_release_evidence_policy.py) illustrate
result fidelity and per-candidate decisions. [MOLI #27](https://github.com/uibcdf/moli/issues/27)
tracks this rule.

## Exceptions and history

Historical nonconforming tags are not rewritten. New deviations require a MOLI issue, rationale, and exit condition.

Schema versions, API versions, policy versions, Conda build numbers, and third-party action refs are separate namespaces.
