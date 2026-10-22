---
summary: Review retrieval references, archives and shared mirrors at the MolI project boundary.
issue: uibcdf/moli#33
status: partial
opened: 2026-09-30
closed:
verification: inspected
area: [contracts, provenance, storage, reproducibility]
blocked_by: []
supersedes: []
---

# Retrieval records, project archives and shared mirrors

## Status and ownership

This is a **candidate contract for review**, prepared on 2026-10-22. It does not
accept a schema, change a platform policy, select a storage service, require a
provider migration or resume Nextia development. [MolI #33](https://github.com/uibcdf/moli/issues/33)
owns the shared decision. [Sabueso #100](https://github.com/uibcdf/sabueso/issues/100)
owns its archive, mirror adapters, access modes, APIs, tests and local changes.
MolSysSuite owns implementation/adoption within its members; any later accepted
platform obligation affecting it needs a linked suite-owned adoption decision.

The existing [identity](../../architecture_1.0/OBJECT_IDENTITY_AND_PORTABILITY.md),
[project ownership](../../architecture_1.0/PROJECT_ARCHITECTURE.md),
[visibility](../../architecture_1.0/VISIBILITY_AND_CONFIDENTIALITY.md) and
[architecture decisions](../../architecture_1.0/DECISIONS.md) remain authoritative.
The [external-source requirement](../REPRODUCIBILITY_AUDIT_AND_REPLAY.md#external-services-and-mutable-sources)
already distinguishes preserving a response from merely naming a database record.

## Inspected implementation and limits

Source inspection uses Sabueso main at
[`4ae60603371fa8afa173d4d24cdff9a2b7121012`](https://github.com/uibcdf/sabueso/tree/4ae60603371fa8afa173d4d24cdff9a2b7121012),
in an isolated, clean, read-only-for-this-review clone. The
[inspection receipt](../evidence/retrieval_contract_33_20261022.json) records exact
file digests and scope. No component test, source query, mirror download, package
installation, public release or project-level integration is qualified here.
Test names below are inspected assertions, not newly executed results.

The initial #33 description predates the implementation. Current source and
[`CACHE_POLICY.md`](https://github.com/uibcdf/sabueso/blob/4ae60603371fa8afa173d4d24cdff9a2b7121012/devguide/CACHE_POLICY.md#direction-adopted-2026-09-30-100)
show the following bounded behavior:

| Boundary | Existing Sabueso behavior | What this does not establish |
| --- | --- | --- |
| Retrieval storage | `_archive.py` uses an explicit SQLite archive, deduplicated compressed response bodies and separate retrieval metadata. The body has SHA-256 identity; `get` checks the decompressed body against that digest. | A portable project resolver, independent verification of every metadata binding, source authenticity or complete wire capture. |
| Issued identity | `record` hashes method, stored URL, request-body hash, status, selected headers, acquisition time and response digest. `source` is stored separately and is outside that reference hash. | A universal reference grammar, a globally unique execution-attempt identity or authentication of the source label. Same-second identical records can deduplicate. |
| Request and response scope | `_http.py` archives responses at its shared transport boundary, including final HTTP errors, and keeps a header allowlist. Request bodies are represented by a digest. | Every component I/O route, every retry attempt, the original request body or every response header. A request hash alone cannot reconstruct its parameters. |
| Record, reuse and replay | Explicit recording/reuse/replay contexts retain original response times; `replaying(of=card)` takes a build manifest. Replay without a build manifest looks up the latest matching archived request. | Exact historical project replay from an unpinned lookup; replaying stored answers is not a fresh source validation. |
| Scientific lineage | `quality.retrievals` lists the records used by a build. `Card.explain` groups retrieval references by source with `basis: source_in_build`. | Exact response-to-field or response-to-SourceAssertion lineage. The proposed per-assertion `provenance_ref` is not supplied by that grouping. |
| Retention report | `retention_from_licence@2` derives the current report when read, including a separate raw-response `retention_licence`. Europe PMC raw responses report internal retention/sharing unknown. | A frozen acquisition-time terms decision or an automatic authorization/retention/export gate. `record` stores its supplied body; it has no metadata-only non-retention branch. |
| Local mirrors | `mirrors.py` registers BindingDB only. Its adapter checks the release ZIP against a published or caller-supplied MD5, builds a SQLite index and removes its own downloaded ZIP. Installed releases can be explicitly pinned. | ChEMBL or every proposed database having an adapter, an archive of the original ZIP, universal SHA-256 verification or a qualified shared service. |
| Storage and lifecycle | Paths are explicit; archives use SQLite sessions and a per-instance thread lock. Mirror updates support manual/notify/auto and `keep` pruning. | Cross-process/distributed writer coordination, quotas, project leases, backup/export completeness or protection of another project's pinned releases from removal. |

Inspected tests in `test_retrieval_archive_offline.py` cover build replay,
unarchived/unqueried distinction, freshness reuse, original timestamps and
source-in-build links. `test_mirrors_offline.py` covers checksum refusal, local
BindingDB rows, missing pins, offline transport refusal and update policies.
These are useful owner-local acceptance inputs; their existence does not prove
the remaining platform guarantees.

## Candidate shared meaning

### References, content and acquisition history

Keep the complete owner-issued retrieval reference opaque, together with its
provider/format identity and separately identified response digest. Coordinate
external syntax and verification promises with [#3](https://github.com/uibcdf/moli/issues/3).
Do not parse a local SQLite row number or archive basename as a global identity.
Moving an archive changes location, not the reference retained by a project.

A response digest identifies bytes under a stated representation; it does not
authenticate a server, establish a scientific release or identify a unique Run.
State whether the digest covers downloaded bytes, decompressed content or a
derived index, and retain the transformation link when several exist. Preserve
the provider's checksum algorithm and basis instead of relabeling an MD5 as a
SHA-256 verification. Equal response bytes do not imply equal acquisition context.

Retain the requested source/endpoint and non-secret request identity, original
acquisition time, native release when actually stated, response status and scope,
and any gaps needed to interpret the result. A route/software version is not a
source release. Preserve the distinction between captured request parameters and
parameters represented only by a digest. Credentials must not enter public or
portable records; hashing a request does not make its other metadata safe to share.

An application may reference retrievals from an InputManifest or KnowledgeSnapshot
without turning them into scientific assertions or Nextia Evidence. Preserve the
declared lineage basis: source-in-build is useful but cannot stand in for exact
field-level support. Scientific assertions, execution events, attribution and
permission remain separate under [#22](https://github.com/uibcdf/moli/issues/22)
and [#36](https://github.com/uibcdf/moli/issues/36).

### Retention, authorization and availability

Describe actual payload custody separately from the reviewed permission to keep,
share or export it. A Boolean `retained` alone cannot describe all relevant states:
content can be present, never retained, deliberately removed or currently
unavailable. Keep the reason, decision owner, applicable terms/version or evidence
and assessment time where available. Distinguish the original assessment from a
later policy assessment; do not silently rewrite historical permission claims.

An unknown or per-record rights report is not a grant for a shared mirror or
export. The project/operator reviews the intended action and recipient before
retaining or disclosing content. Do not infer authorization from the existence of
an archived copy, its hash, a service's general licence or a bibliography entry.
Even request metadata, record identifiers and hashes can disclose private research.
This proposal sets no new legal interpretation of a source's terms.

Where a response cannot be kept, retain only permitted metadata with an explicit
payload gap; where metadata itself is restricted, keep the permitted private
reference/disposition instead. A current source query is a new acquisition,
never an invisible repair to an unavailable historical record. Reference export
and a self-contained archive must state different replay guarantees.

### Project storage and shared mirror operation

The Workspace supplies project storage/resolution context; Sabueso remains
independently usable with explicit local paths. No directory name, cloud backend
or new shared mutable scientific store is selected here. A project archive is
project-scoped by default in this candidate; sharing needs its own authorization
and retention decision. A mirror may be shared only for a qualified source,
release, user scope and operational route.

Before claiming a platform-managed mirror, name the operator and test writer
coordination, interrupted installation/publication, immutable release selection,
reader consistency and recovery. A possible first route is a single managed
writer with read-only consumers, but that route is not implemented or accepted by
this review. The existing per-instance lock and `.part` index are not evidence of
a multi-process or distributed contract.

Record storage budget, retained releases, backup/restore responsibility and
project dependencies before enabling automatic pruning. Updating a mirror must
not silently switch a pinned project; cleanup must account for retained project
pins/archives or explicitly record the loss and its consequence. A local `keep`
count alone is not project-aware retention. Follow the existing
[temporary-resource lifecycle](../governance/temporary_resource_lifecycle.md)
for task scratch; durable scientific archives need their own owner and retention
decision rather than being treated as disposable scratch.

### Replay and observation

Exact historical replay selects the original recorded request/response references
and their required order, checks the promised integrity and refuses missing or
foreign targets. It must not substitute the latest answer, another release or a
live network response. Reuse under a freshness policy is a different operation.
Record later consumption separately while retaining the original acquisition
time; acquisition and replay coverage/gaps remain inspectable.

Preserved response bytes alone do not guarantee identical derived Cards: parser,
mapping/rule versions, required inputs and environment can matter. State the
replay scope and closure. A recorded 404/empty result differs from unqueried,
unauthorized, unavailable, malformed and failed acquisition. Neither reading a
mirror nor replaying an archive certifies current external-source health.

## Review and acceptance still required

These are **planned exercises**, not executed receiving or an accepted schema:

| Exercise | Required observable distinction | Owning follow-up |
| --- | --- | --- |
| Same bytes, different acquisitions; later reuse | Payload identity versus acquisition/consumption context and original time | Sabueso #100; MolI #18/#36 for project recording |
| Two responses to the same request; one historical target absent | Manifest-bound replay versus latest lookup; missing target stays missing without network fallback | Sabueso #100; shared references in MolI #3 |
| Source-in-build support | Honest coarse lineage versus an exact per-assertion claim | Sabueso #100; MolI #22/#36 |
| Restricted/per-record payload and a metadata-only export | Actual custody, permission, disclosure and replay gap remain separate | Project/operator review; provider changes in Sabueso #100 |
| Relocated archive; reference-only and self-contained exports | Identity survives location changes; available content/closure is verified separately | MolI #3/#33; future Workspace consumer |
| Shared pinned mirror with update, concurrent reader and failed writer | No silent pin switch, partial release exposure or unrecorded deletion | MolI #33; Sabueso #100; affected consumer owners |
| Quota/pruning and restore | Project dependencies and availability survive or expose explicit loss | Future project/operator implementation; delegated suite adoption if applicable |

Next: ask the Sabueso owner to review the inspected limits and candidate seam;
settle the minimum semantic contract in #33 with affected consumer owners.
Only then select an implementation/adoption slice and its exact tests. Keep the
broader issue open for project storage, shared operation and consumer evidence.
No Nextia runtime, new database download or provider change is needed to review
this document. A frozen wire format, project-wide ACL service, exact per-field
lineage, automatic mirror rollout and a full replay engine remain outside this
documentation step.
