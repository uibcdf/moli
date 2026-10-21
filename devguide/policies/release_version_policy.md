# MOLI Release Version Policy

Normative for public releases of MOLI repositories unless an explicit exception applies.

## Public identity

Public releases use exactly `X.Y.Z`: three non-negative decimal integers without
leading zeroes except for zero itself, no `v` prefix and no alpha, beta, rc,
dev, post, or local suffix. The accepted pattern is recorded in `moli.toml`.

The project/package version, Git tag, and GitHub Release tag use the same public version.

Development checkouts may carry truthful derived/local identities; these are provenance, not public release versions.

## GitHub Release title

For every public component GitHub Release, the visible title (`name`) is exactly
the canonical `X.Y.Z` version, identical to the release `tag_name` and the
project/package version. For example, a `0.14.0` release has `name = "0.14.0"`;
do not prepend the project name or append a subtitle, comment or other text.
Put descriptive content in the release body or notes instead.

Before creating or editing a public release, verify the intended title and tag.
Use `gh release create 0.14.0 --title 0.14.0` or set both `name` and
`tag_name` to `0.14.0` through the GitHub API. Verify the resulting release
metadata after publication. This title rule applies to component public
releases; separately governed policy-release namespaces and `archive/` tags
retain their own meanings. It does not require rewriting historical release
metadata, moving a tag, rebuilding a package or changing an artifact.

A proposed deviation follows the existing exception route: record the owner,
owning issue, rationale and review expiry or exit condition, with a MOLI issue
for a direct-component policy exception. Do not infer an exception from a
previously published title. [MOLI #68](https://github.com/uibcdf/moli/issues/68)
tracks adoption of this convention; MolSysSuite owns member adoption in its
separate governance domain.

## Archive tags

Accepted through [MOLI #47](https://github.com/uibcdf/moli/issues/47), the reserved
`archive/<description>` namespace may preserve a historical or experimental
**commit** without declaring a public release. The suffix is nonempty and the
whole ref must be a valid Git tag. Record the purpose, owner, preserved commit
and immutable tag-object identity in an annotation or linked owning issue.
Keep the reference stable. Do not move, delete or recreate an existing tag to
satisfy this prospective rule; record historical metadata without changing it.

Archive names cannot be project/package versions, GitHub Release identities,
or publication candidates. They supply no source, artifact, installation or
archive/DOI qualification. A later canonical release may use the preserved
commit only through its separate exact-candidate gates. Public component
versions remain exactly `X.Y.Z`; other invalid public versions do not acquire
an exception merely because this namespace exists. Separately governed policy
tags and Action version/major aliases retain their own meanings.

### Applicability and activation

This is an **owner-reviewed opt-in capability** for MOLI and its directly
governed components. Before first use, the repository owner records its
decision and evidence in an owning issue linked to #47:

1. Inspect every maintained publication route, including tag/release events,
   manual dispatch, reusable workflows and other package indexes. An archive
   push must not publish. A mistakenly supplied archive release/candidate name
   must be rejected before release-gate acquisition, credentials or registry
   mutation; the publishing guard also checks canonical tag/package identity.
   Prove this with owner-local negative cases and canonical controls, without
   performing an upload or manufacturing a release.
2. Provide an unconditional, failure-gating conformance route on **all** tag
   pushes. Normally use `tags: ["**"]`; `"*"` excludes `/`. Reject tag
   exclusions and conditional/tolerated/missing gates. GitHub's path filters
   do not run on tag pushes. See the [GitHub filter reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#filter-pattern-cheat-sheet).
3. Record the capable enforcement source: a reviewed full-commit pin for a
   central/reusable caller, or the immutable component revision of an equivalent
   native gate. A mutable branch/tag or a guide copy is not enforcement evidence.
   Record actual native workflow/job/step evidence separately from static
   configuration. An older compatible caller need not migrate until the
   repository chooses this capability.
   For an older target, inspect the workflow/caller selected at that historical
   ref: changing `main` does not retrofit its workflow. A missing historical
   gate needs a separately reviewed owner enforcement route, not a rewritten
   target or a claim that default-branch configuration proves tag execution.
4. Record preservation metadata and review any version-from-Git matcher so an
   archive ref cannot accidentally become package metadata. Preserve current
   public tags, bytes and original release evidence. A configuration audit or
   temporary Git fixture is not proof of an actual hosted archive-tag event.

Repositories not using this namespace need no new tag, package, caller migration
or capability rollout. The existing canonical component guide already links to
this policy; no byte-copy change is required by #47. A future activation remains
owner-local and is not inferred from receiving this decision.

MolSysSuite retains its independent rule, enforcement and member rollout under
[suite #84](https://github.com/uibcdf/molsyssuite/issues/84). MOLI does not change
those member rules. The separately registered UIBCDF support providers may
review this capability through their own governance; notice alone does not
change an Action's release namespace or activate a receptor's suite caller.

### Executable checks and limits

MOLI's own read-only gate is
`python devtools/scripts/check_archive_tags.py .`. It uses PyYAML 6.0.3, preserves
the string `on` key, rejects ambiguous YAML and checks the actual all-tag job and
command. It inspects available archive refs without writing them, requires a
commit target, inspects that target's historical workflow and native script,
and rejects archive names in literal project versions. An unqualified old
workflow is reported even when the current checkout has a capable gate. Fetch all
tags before using it. Its reusable workflow helper accepts only the exact
reviewed full-commit caller supplied by the owner; matching a pin does not prove
that the named implementation is capable.

The reference gate accepts annotated tags with nonempty `Owner:` and `Purpose:`
lines. For lightweight or historical annotations, retain an owning-issue record
without changing the original tag. Its optional `devguide/archive_tags.toml`
adapter is illustrated below; equivalent native gates may use their own record
format. Reviewers verify the substantive owner/purpose and linked decision.

```toml
[tags."archive/example"]
owner = "responsible maintainer"
purpose = "preserve the reviewed experiment"
issue = "uibcdf/component#123"
commit = "<full preserved commit>"
tag_object = "<full original ref object>"
```

`--release-version X.Y.Z` provides an early shape check only. It never qualifies
a publisher, acquires credentials or authorizes a release. The
[regressions](../../tests/test_archive_tags_policy.py) exercise an unchanged
annotated temporary Git tag, non-release/public-version separation, pinned
preservation records, incapable callers and missing/filtered/conditional gates.
They do not certify another repository's publisher. MOLI has no package publisher;
its all-tag workflow performs read-only administrative checks and tests.

An activation exception follows the existing owning-issue/MOLI exception route
with rationale, owner and an exit condition. A deferred or excepted enforcement
route is not a qualified archive capability and cannot authorize publication.

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

A `[skip ci]` marker on the original producer commit neither proves nor
disqualifies a candidate. An authorized manual route may qualify it only when
every mandatory gate actually executes and passes for that exact source commit,
resolved closure and, where applicable, the recorded artifact bytes and digest.
Keep the original producer identity and file; a later workflow repair does not
permit rebuilding it or presenting a different file as the recorded candidate.
Manual dispatch alone is not a passing result. The
[Python CI policy](python_ci_policy.md#validation-during-direct-push-development)
also governs ordinary direct-push checkpoints.

The pre-publication decision records which gates were reused, which became stale,
and the new evidence that replaced each stale result. A passing status applies
only to the identity and scope actually observed. Repositories keep their own
gate implementations and may impose stricter invalidation rules. [MOLI #24](https://github.com/uibcdf/moli/issues/24)
tracks this direct-component rule; MolSysSuite owns its own member release policy
and coordinated release refinements.

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
correctness or safety gates may be declared non-waivable. MolSysSuite sets its
own member release decisions while remaining accountable for any platform
contract at the suite boundary. The [reference evaluator](../../devtools/scripts/release_evidence.py)
and [negative fixtures](../../tests/test_release_evidence_policy.py) illustrate
result fidelity and per-candidate decisions. [MOLI #27](https://github.com/uibcdf/moli/issues/27)
tracks this rule.

## Exceptions and history

Historical nonconforming tags are not rewritten. New deviations require a MOLI issue, rationale, and exit condition.

Schema versions, API versions, policy versions, Conda build numbers, and third-party action refs are separate namespaces.
