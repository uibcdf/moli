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

## Exceptions and history

Historical nonconforming tags are not rewritten. New deviations require a MOLI issue, rationale, and exit condition.

Schema versions, API versions, policy versions, Conda build numbers, and third-party action refs are separate namespaces.
