# Completeness of remote inventories

Accepted working instruction under [MolI #85](https://github.com/uibcdf/moli/issues/85).
Applies to MolI and direct-component development, reporting and administrative
audits. MolSysSuite owns member adoption through
[suite #171](https://github.com/uibcdf/molsyssuite/issues/171).

## Match the conclusion to the acquired scope

Before declaring a remote object absent, an inventory exhaustive, an audit clean,
or an issue safe to create without duplication, establish complete acquisition
for the declared repository, endpoint, state/filter, permissions and observation
time. A bounded exploration is valid when reported as bounded. A compact display
may summarize a complete inventory; it must not silently become its source.

A list limit, first page, search-result sample, local queue or previously saved
snapshot alone cannot prove absence. Search has its own scope/index semantics;
traversing its results does not automatically establish a complete repository
inventory. State whether PRs are included when using an issues endpoint, and
preserve endpoint distinctions such as open-only versus all-state acquisition.
Follow every required continuation and check successful completion before using
the result. Record the repository/resource, filters, page/record counts, endpoint,
observation time, acquisition outcome and known access limitations.

A failed request, inaccessible repository, missing page, timeout, malformed body,
ambiguous duplicate identity or reached safety bound yields partial/unknown
coverage. Do not turn any of these into an empty result, missing object, clean
audit or permission to create a duplicate. A successfully acquired, valid empty
inventory is a different result. A 404 under limited credentials is not by itself
a universal nonexistence claim. An independent direct lookup can settle a named
object within its accessible scope; it does not qualify the entire inventory.

## Apply the evidence before a mutation

Keep acquisition separate from presentation, reconciliation and writes. If complete
acquisition required for a decision is unavailable, retain the bounded finding and
its owner/recovery route, and defer the absence-dependent mutation. Preserve
human dispositions and genuine drift; no automatic issue reopening, deletion or
label mutation follows from this policy. Remote changes during traversal can
still matter: a completed pagination is an observation, not a transactional frozen
board or a claim about inaccessible data. Revalidate the relevant identity before
an authorized write and stop if the decision is no longer supported.

A reusable inventory reader belongs to its provider. Review the existing
[suite reader and transport contract](https://github.com/uibcdf/molsyssuite/blob/ea14a4115e132ae6e89531a53b12c9cea360e284/devguide/github_inventories.md)
before duplicating it; adoption needs the consumer's own dependency/API review.
MolI's current local governance validators do not acquire remote issue/label
inventories, so this instruction creates no new network CI gate or reader runtime.

When implementing an inventory-dependent tool, test records beyond the old cap,
multiple pages, valid empty data, failed/missing/malformed acquisition, duplicate
identities and the endpoint's issue/PR semantics. A reader safety bound refuses a
completeness claim rather than returning a truncated success. Report defects to
the owning tool issue; do not convert the original 500-issue incident into a
universal numeric limit.

## Delivery and limits

The reproduced source defect is [MolSysMT #587](https://github.com/uibcdf/molsysmt/issues/587).
Its owner fix and suite delivery are inputs, not proof of direct-component
adoption. Root instructions, the shared guide and starter carry the action;
[platform adoption](platform_guidance_adoption.md) records receiving separately.
No fixed worker count, new shared service or scientific/release qualification is
introduced by this administrative working instruction.
