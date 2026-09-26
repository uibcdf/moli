---
summary: Agree on consumer-facing guarantees for versioned Sabueso knowledge references.
issue: uibcdf/moli#3
status: active
opened: 2026-09-23
closed:
verification: inspected
area: [contracts, identity, knowledge, discovery]
blocked_by: []
supersedes: []
---

# Reference contract for versioned Sabueso knowledge

## Purpose and ownership

This is a proposal for the references another MOLI component may retain when it
uses Sabueso knowledge. Sabueso owns Cards, SourceAssertions, relationship
records, snapshot serialization, hashing, storage, APIs and local migrations.
MOLI owns only the shared meaning of a reference crossing into Nextia, Context
Assembly, MolSysSuite or a ProjectRecord. Sabueso's provisional implementation
is tracked by [Sabueso #7](https://github.com/uibcdf/sabueso/issues/7);
adoption of the agreed form belongs to
[Sabueso #53](https://github.com/uibcdf/sabueso/issues/53).

Architecture 1.0 requires stable referencability and distinguishes object
identity, version, location, resolution and authorization
([Object identity and portability](../../architecture_1.0/OBJECT_IDENTITY_AND_PORTABILITY.md),
[decisions](../../architecture_1.0/DECISIONS.md)). Nextia owns project Evidence
and Decisions; a Sabueso SourceAssertion is a possible basis for Evidence, never
Evidence by virtue of being cited
([Sabueso](../../architecture_1.0/SABUESO.md),
[Nextia](../../architecture_1.0/NEXTIA.md)). Context Assembly may select or
summarize knowledge while preserving its authoritative references and applying
disclosure policy
([Context Assembly](../../architecture_1.0/CONTEXT_ASSEMBLY.md),
[visibility](../../architecture_1.0/VISIBILITY_AND_CONFIDENTIALITY.md)).

Historical references remain part of the ProjectGraph and ProjectRecord even
when their target is unavailable. A hash proves identity, not continued
availability; reference export and self-contained archival export have different
guarantees
([Project architecture](../../architecture_1.0/PROJECT_ARCHITECTURE.md),
[audit and replay](../REPRODUCIBILITY_AUDIT_AND_REPLAY.md)).

## Current implementation evidence (2026-09-26)

Inspected Sabueso at commit
985e1b83f3ad766a7d006b6fa75614c533caa49f, including
its snapshot code, KnowledgeStore and offline tests. This supersedes the
2026-09-23/24 observations in the earlier version of this report.

- A Card has an entity-level card id. Its snapshot id is a SHA-256 content
  address over the stored Card in canonical JSON. The quantity seal is omitted
  from that hash because it is derived; the quantity values and units in the
  Card remain in the hashed content. Full Card reads verify the snapshot and
  quantity seal.
- Sabueso issues a pinned Card reference: a Card id followed by
  `@sha256:` and 64 hexadecimal digits.
  KnowledgeStore returns that exact historical state or raises StorageError.
  An absent, malformed or foreign pin never falls back to the latest Card.
  Offline tests cover a later Card whose curation outcome changed.
- A SourceAssertion or relationship is addressed within a pinned Card state
  by appending #SA_... or #REL_... to that Card reference. A bare item id is
  insufficient: the same SourceAssertion id can occur in different source
  releases, while the snapshot records the release and retrieval context.
- A bare Card id resolves the latest state in a store. It is useful for live
  exploration but cannot preserve what a historical Run, Evidence or Decision
  used. Sabueso also implements pinned Decks; their cross-component meaning
  can be considered with the packet/query work in
  [MOLI #22](https://github.com/uibcdf/moli/issues/22).
- The local KnowledgeStore does not prune snapshots today and has no
  authorization layer. Its StorageError does not provide the platform's full
  unavailable/unauthorized/offline outcome vocabulary. Those facts do not by
  themselves establish indefinite retention or a remote resolver contract.

One implementation gap was reproduced during this review: a modified
SourceAssertion row is rejected by a pinned full-Card read but returned by a
direct pinned item read. The common item path also serves relationships. This
belongs to [Sabueso #79](https://github.com/uibcdf/sabueso/issues/79); the
cross-component item guarantee should not be declared implemented until that
path is guarded.

## Provisional meaning for consumers

The smallest shared reference has an owner, object kind, opaque object id and
an immutable snapshot id when historical state matters. An optional item kind
and item id identify an item inside that snapshot. These are conceptual fields;
Sabueso proposes the serialized string form and owns its parser. Consumers
should preserve the complete issued reference, rather than reconstructing it
from pieces or treating a database path as identity.

| Reference | Proposed consumer meaning | Limit |
| --- | --- | --- |
| Bare Card id | Current state at the chosen Sabueso store | Not a historical citation; store choice matters |
| Pinned Card | One exact resolved Card state, including selections, conflicts, curation outcomes, source metadata and rules | Does not assert that the selected value is scientific truth |
| Pinned Card plus #SA item | The SourceAssertion as held in that state, with its recorded source and observation context | The assertion is distinct from the Card's selected interpretation and from Nextia Evidence |
| Pinned Card plus #REL item | The relationship as held in that state, including its recorded support or derivation | Does not automatically become a Nextia Observation or Evidence |

Nextia Evidence, Decisions and recorded Runs should retain pinned references
to the knowledge they used. Nextia supplies the project-contextual
supports/contradicts/informs interpretation. Context Assembly may present the
same knowledge under an authorized disclosure policy, while retaining the
reference and provenance. Neither use transfers semantic ownership of the
Sabueso object to Nextia or MOLI.

For example, a Nextia Evidence record may cite a pinned #SA statement and
explain why it informs a project Hypothesis. A later Decision may cite that
Evidence. The #SA reference preserves the external statement as observed;
the Evidence carries the project's interpretation of its relevance.

Resolution of a pin must yield the named state or an explicit non-resolution
outcome; returning the latest state under that pin is forbidden. The
ProjectGraph/ProjectRecord keeps the reference even when resolution fails.
This is the proposed invariant, not yet an accepted cross-component API.

## Small acceptance exercise

Use fictional objects in public records: one protein Card `C`, one
SourceAssertion `A`, two stored Card states `S1` and `S2`, and a project
Hypothesis `H`. The provider issues all references; the consumer stores the
issued text unchanged. `C@S1#A` below is symbolic notation, not a proposed
serialized grammar. No scientific project or real protein is needed to
exercise the boundary.

1. **Historical citation.** Save `S1` with `A` and its source observation
   context. Save `S2` after changing the Card's resolved state or observing
   the same assertion in another source release. `C@S1` and `C@S1#A` still
   return exactly the state and observation first cited. `C@S2` may differ;
   it never changes what the `S1` references mean. A malformed, missing or
   foreign pin fails explicitly and never selects the latest Card.
2. **Item integrity.** Change an item row outside Sabueso without changing
   the issued pin. Both a full-Card read and a direct `#A` read reject the
   altered state. The direct item check is pending Sabueso #79.
3. **Project interpretation.** A conceptual Nextia Evidence object cites
   `C@S1#A` and records why `A` informs `H`. Its interpretation and status
   belong to Nextia; the Sabueso assertion remains unchanged. The same
   assertion may inform another project differently. This case becomes an
   integration test when Nextia has the minimum persistent Evidence slice;
   a citation alone does not create Evidence.
4. **Unavailable target.** Resolve the citation through a store that lacks
   `S1`. Resolution reports failure without using `S2`, while the project
   retains the original reference and its own Evidence history. A
   reference-only export makes no claim that `S1` is available offline.

These cases test consumer meaning, not a frozen parser or Nextia schema.
Whether a self-contained export also guarantees independent digest
verification needs a separate test vector and an explicit decision about
canonicalization and archival responsibility.

## Decisions before acceptance

1. **External form and hash promise.** Sabueso proposes its current
   card-id@sha256:snapshot#item grammar. The minimal MOLI contract can treat
   this as a provider-issued opaque reference. If consumers are promised
   independent digest recomputation from exported JSON, the canonicalization
   rules and their evolution become part of the public contract. Decide that
   promise explicitly; do not infer it from the SHA-256 prefix alone. A later
   alias or entity merge must not silently retarget an old pinned citation.
2. **Retention and availability.** Sabueso currently keeps every snapshot,
   but perpetual online resolution has not been agreed. State a retention or
   archival expectation for externally cited pins, and record availability
   and retention in project manifests. A reference-only export must not claim
   to be a self-contained archive. Future pruning requires an explicit
   policy, a migration/archival route where applicable, and honest
   non-resolution rather than fallback.
3. **Resolution outcomes and confidentiality.** Architecture 1.0 calls for
   distinguishing resolvable, unavailable, unauthorized, offline/archived,
   externally removed, unknown and never-existed states. The local store only
   raises StorageError and cannot speak for future remote authorization.
   Decide the cross-component outcome semantics without forcing a local
   exception class or leaking a private object's existence to an
   unauthorized caller. An undisclosed/unknown outcome may be required at
   that trust boundary.
4. **Pinned items.** Sabueso #79 must establish that direct #SA and #REL
   reads verify the cited snapshot or otherwise reject altered content.
   Until then, full-Card pinned reads provide stronger checked evidence than
   direct item reads.

## Route to resolution

Review the proposed consumer meanings with Sabueso and a prospective Nextia
consumer, using one pinned Card and one pinned SourceAssertion in a
project Evidence/Decision example. Agree the external form and availability
semantics at [MOLI #3](https://github.com/uibcdf/moli/issues/3), then have
Sabueso #53 adopt or migrate it. After that, update Architecture 1.0 examples
that currently use conceptual unpinned Sabueso ids, or label them explicitly
as live examples. Do not make a provisional form stable by copying it into a
consumer first.

## Resolution

Pending. No cross-component reference grammar or retention guarantee has
been accepted yet.
