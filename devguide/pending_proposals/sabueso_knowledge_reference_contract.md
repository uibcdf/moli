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

State of Sabueso, inspected on `main` on 2026-09-23:

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
   - Entity-level references (`sabueso:<type>:<entity-id>`). They require the
     EntityResolver from uibcdf/sabueso#6.
   - Source-record-level references, as today, with the entity as a separate object.
2. **Pinning**
   - Content-addressed snapshots, which are immutable and reproducible by construction.
   - Monotonic revisions or timestamps, which are simpler to read but need a registry
     to resolve.
   - Both at once: revision for humans, hash for integrity.
3. **What a snapshot captures:** at minimum the card state, its SourceAssertionStore, the
   selection-rules version and the source versions.
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
  uibcdf/sabueso#7 and uibcdf/sabueso#6.
- The architecture examples are consistent with the chosen grammar, or the difference is
  explained.

## Resolution

Pending.
