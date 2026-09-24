---
summary: Define how consumers reference versioned Sabueso knowledge (Cards, SourceAssertions, snapshots).
issue: uibcdf/moli#3
status: open
opened: 2026-09-23
closed:
verification: inspected
area: [contracts, identity, knowledge, discovery]
blocked_by: []
supersedes: []
---

# Reference contract for versioned Sabueso knowledge

## What

This record defines the shared contract by which Nextia, and other consumers such as
MOLI Agent Context Assembly or MolSysSuite components, reference Sabueso knowledge:

- the reference syntax for Sabueso Cards and SourceAssertions;
- how a reference pins a specific version or snapshot;
- the guarantees a consumer gets when it resolves a pinned reference.

Architecture 1.0 freezes the requirement and leaves the contract open:

- Frozen: stable referencability, versioned references, and identity ≠ version ≠
  location ≠ resolution ≠ authorization (`OBJECT_IDENTITY_AND_PORTABILITY.md`, stress
  test 12, `DECISIONS.md` "Object identity and portability").
- Open: `OPEN_QUESTIONS.md` "SourceAssertion / Evidence bridge" and the Sabueso item
  "Card snapshot/version semantics".

This record defines an implementation contract beneath the architecture. It does not
change it.

## How / evidence

Historical state of Sabueso, inspected on `main` on 2026-09-23. The next section
supersedes observations that have since changed:

- **Card identity:** `meta.card_id = sabueso:<entity_type>:<subject_ref>`, for example
  `sabueso:protein:uniprot:P52789`, together with `meta.schema_version = 0.2.0`. It was
  introduced as provisional in commit `3408f7c`.
- **SourceAssertion identity:** `id = SA_<source>_<record>_<sha256-16>`, computed
  deterministically from source, record, `field_path` and `asserted_value`. The
  identifier does not include `source.version`. Each assertion also carries
  `subject_ref = <namespace>:<record_id>`, for example `uniprot:P52789` or `pdb:2NZT`.
- **Mismatch with the architecture examples:**
  - The examples (`examples/tctim_discovery_project.md`) use entity-level references
    such as `sabueso:protein:TcTIM`. The current `card_id` names a *source record*, not
    an entity.
  - Entity resolution is not implemented yet (uibcdf/sabueso#6).
  - Cards built from annotation sources (GO, InterPro, CATH, SCOPe, TED) receive
    `entity_type = "protein"`.
- **Versions and snapshots:**
  - No reference can express a version or snapshot.
  - SQLite persistence appends one row per `card_id` and loads the latest.
  - No mapping fills `source.version`, although UniProt exposes `entryVersion` and
    `sequenceVersion`.
- **Nextia:** no implementation exists yet, so this is the moment to fix the contract
  before any consumer hard-codes the provisional forms.

## New evidence: minimal Sabueso workflow (2026-09-24)

Sabueso now has the live
[`knowledge_baseline.ipynb`](https://github.com/uibcdf/sabueso/blob/main/docs/content/showcase/knowledge_baseline.ipynb)
and a corresponding frozen-response
[`test_knowledge_baseline_offline.py`](https://github.com/uibcdf/sabueso/blob/main/tests/core/test_knowledge_baseline_offline.py).
The workflow resolves two proteins, creates cards and SourceAssertions, adds a curated
literature assertion, and stores and reloads cards. This satisfies the scheduling
condition recorded in [MOLI #3](https://github.com/uibcdf/moli/issues/3); the
cross-component reference decision can now be reviewed against an actual workflow.
The observations below were checked against Sabueso `8bdb80d`.

- `meta.card_id` is now an entity-level anchor: UniProt accession for a protein and
  standard InChIKey for a small molecule. The string form remains explicitly
  provisional. Neither a card revision nor a snapshot id exists.
- A SourceAssertion id hashes source, record, field path and asserted value, but
  omits `source.version`. Several mappings now record source releases. Therefore the
  id identifies a stated claim across releases, while an exact historical
  observation also needs its source version or a containing snapshot. Sources
  without a stated release require another observation locator. The current
  16-hex-character suffix and string representation have not been reviewed as a
  platform-wide external identifier format; consumers must treat the id as opaque.
- Curated assertions survive card rebuilds with stable ids, while their comparison
  outcome can change as database statements change. A snapshot of a resolved card
  must therefore preserve its selected values, conflicts and curation outcomes,
  not only the assertion ids.
- The stored card includes its SourceAssertionStore, relationships, selection rules,
  quality and source metadata. The quantity seal verifies quantity fields on read;
  it is not a whole-card snapshot id or digest. SQLite appends rows but its public
  read path selects the latest row for a `card_id`. No pinned resolver exists.
- Nextia is still at the architecture/documentation stage and has no consumer
  implementation that would force a provisional syntax into production.

## Contract candidate for review

Separate the stable object identity from its historical state. A cross-component
reference should carry the owning component, object kind, opaque object id and,
when historical reproducibility is required, an immutable snapshot id. A consumer
may request the current card without a pin for live exploration; Nextia Evidence,
Decisions and recorded Runs must pin the state they used. Resolution of a missing
pin must fail explicitly rather than silently returning the latest card. This is
a candidate contract, not an accepted reference grammar.

For the first Sabueso implementation, a SourceAssertion citation could be scoped
to the pinned card snapshot that contains it: card id, snapshot id and assertion
id. The assertion id plus `source.version` remains useful as an additional
source-release locator, but cannot by itself reconstruct the card's selected
value and conflicts. An independent assertion snapshot may be defined later if a
consumer needs to cite assertions without a containing card.

The snapshot must preserve the card payload and its interpretation context:
schema version, SourceAssertionStore, relationships, selected values, selection
rules or profile version, quality and curation outcomes, source versions and
retrieval metadata. A portable snapshot id cannot be the local SQLite row number.
If the public id is content-addressed, canonicalization and digest versioning must
be specified first; an opaque immutable id may instead carry a separate integrity
digest. Retention, resolution and error states need explicit guarantees before
this candidate becomes a platform contract.

## Why

- A Nextia Evidence or Decision must stay interpretable against the exact external
  knowledge it used, even after the sources evolve (stress test 12).
- Context Assembly must preserve references to the authoritative objects
  (`CONTEXT_ASSEMBLY.md`).
- The reference format is shared by two or more components, so under the `MOLI_GUIDE.md`
  ownership rule it belongs to `uibcdf/moli`, not to Sabueso alone.

## Alternatives

Nothing is decided yet. These are the options to evaluate:

1. **Card identity**
   - Keep the current entity-level anchor and define its public namespace and
     resolution guarantees. Sabueso's EntityResolver is now implemented; source
     records remain provenance rather than the card's identity.
   - Decide how to represent aliases and entity merges without changing what an
     existing reference means.
2. **Pinning**
   - Content-addressed snapshots, which are immutable and reproducible by construction.
   - Monotonic revisions or timestamps, which are simpler to read but need a registry
     to resolve.
   - Both at once: revision for humans, hash for integrity.
3. **What a snapshot captures:** the card state and interpretation context listed in
   the contract candidate, including curation outcomes and source versions.
4. **SourceAssertion ids across source releases**
   - Keep them stable while the asserted content is unchanged, with the source versions
     recorded as observations, as today.
   - Or include `source.version` in the identity.
5. **Scope:** storage backends, remote services and authorization are out of scope
   (Architecture 1.0 keeps them implementation-open).

## Acceptance criteria

- A documented reference grammar for Sabueso Cards and SourceAssertions, with the
  pinning syntax and semantics, in the MOLI devguide or as a MOLI policy.
- Explicit guarantees for resolving pinned references (immutability, retention
  expectations).
- Sabueso's provisional forms are either confirmed or scheduled for migration in
  uibcdf/sabueso#7.
- The architecture examples are consistent with the chosen grammar, or the difference is
  explained.

## Resolution

Pending.
