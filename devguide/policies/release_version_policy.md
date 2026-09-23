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

## Exceptions and history

Historical nonconforming tags are not rewritten. New deviations require a MOLI issue, rationale, and exit condition.

Schema versions, API versions, policy versions, Conda build numbers, and third-party action refs are separate namespaces.
