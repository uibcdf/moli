# Object Identity and Portability

MOLI Platform Architecture 1.0 should avoid coupling scientific objects to a particular Python process, filesystem, database, machine, or deployment topology.

Even when the initial implementation is entirely local:

> **Important scientific objects should be serializable and referencable.**

This principle allows the platform to evolve from local Python objects toward shared or remote services without changing the scientific meaning of those objects.

## Important scientific objects

The principle applies especially to objects such as:

```text
Sabueso
────────
Card
SourceAssertion
resolved knowledge objects

Praxis
──────
Capability
Protocol
validation records

Nextia
──────
DiscoveryProject
Question
Hypothesis
Strategy
Campaign
Run
Artifact
Result
Observation
Evidence
Candidate
Decision
```

Additional objects may adopt the same model when justified.

## Stable identity

Important persistent objects should have stable identities that are independent of their current in-memory representation or storage location.

Conceptually:

```text
object
  │
  ├── stable identity
  ├── type
  ├── version / revision where relevant
  ├── provenance
  └── content / state
```

A stable identifier should continue to identify the same scientific object whether it is:

```text
in memory
serialized to disk
stored in a database
referenced from another project
served remotely
replicated
archived
```

The exact identifier syntax is intentionally not frozen in Architecture 1.0.

Possible future forms could resemble:

```text
sabueso:<object-type>:<id>
praxis:<object-type>:<id>
nextia:<object-type>:<id>
```

or URI-like references, UUID-backed identities, content-addressed identities, database identifiers, or another scheme.

Architecture 1.0 freezes the **requirement for stable referencability**, not the concrete identifier format.

## Serialization

Important objects should have a defined serializable representation.

Serialization should preserve the information required to reconstruct or meaningfully inspect the object, including where relevant:

```text
identity
type
schema version
scientific content
relations
status
provenance
references
timestamps
version/revision information
```

The concrete serialization technology is implementation-open.

Possible representations include:

```text
JSON
YAML
MessagePack
database records
domain-specific formats
```

No specific format is mandated by Architecture 1.0.

## References rather than duplication

When possible, components should reference authoritative objects rather than silently copying their content.

For example:

```text
Nextia Evidence
      │
      └── references
              │
              ▼
      Sabueso SourceAssertion
```

rather than creating an indistinguishable duplicate.

Similarly:

```text
DiscoveryProject
      │
      ├── Protocol reference ───► Praxis
      │
      ├── knowledge reference ──► Sabueso
      │
      └── Artifact reference ───► external storage
```

This preserves ownership and provenance.

## References must survive location changes

A reference should conceptually remain meaningful if the underlying object moves from:

```text
local file
    ↓
local database
    ↓
shared database
    ↓
remote service
```

This does not mean every reference must always be globally resolvable.

It means scientific identity should not be defined solely by a transient storage path.

For example, this is fragile as identity:

```text
/home/user/project/results/run17.json
```

whereas a stable scientific reference can remain meaningful even if storage changes.

## Identity is not necessarily content identity

Not every object should necessarily be content-addressed.

For example, a DiscoveryProject may evolve over time while preserving project identity.

Architecture 1.0 therefore distinguishes conceptually between:

```text
object identity
version / revision
content
```

The exact versioning semantics remain implementation-open.

## Versioned references

Some scientific operations require reproducibility against a specific historical state.

A reference may therefore need to distinguish:

```text
current object
```

from:

```text
specific version / snapshot
```

This is especially important for:

* Sabueso knowledge that changes as external sources evolve;
* Praxis Protocols that acquire new versions;
* DiscoveryProjects with evolving state;
* software/environment definitions;
* external databases.

A historical Run should remain interpretable even after current knowledge or methodology has changed.

## Provenance travels with the object graph

Serialization and remote execution must not sever provenance.

Conceptually:

```text
Protocol
   │
   ▼
Run
   │
   ▼
Result
   │
   ▼
Observation
   │
   ▼
Evidence
```

should remain traceable even when the objects are stored by different components or services.

Stable references provide the edges of this distributed scientific graph.

## Artifacts may be referenced externally

Large Artifacts should not be forced into the same storage mechanism as structured scientific objects.

For example:

```text
Artifact
  │
  ├── stable identity
  ├── metadata
  ├── provenance
  ├── checksum
  └── content location
          │
          ▼
     object storage
     filesystem
     HPC storage
     archive
```

The Artifact remains part of the scientific graph even when its bytes are stored elsewhere.

## Local and remote interfaces

A desirable long-term property is that scientific semantics remain similar across local and remote use.

Conceptually:

```python
project = nextia.get_project(project_ref)
```

should not require the scientist to care whether the authoritative project is stored:

```text
in the same Python process
in a local database
on a laboratory server
in a remote service
```

The exact API is not frozen; the architectural goal is **location transparency where scientifically appropriate**.

Location transparency must not hide information relevant to provenance, performance, confidentiality, or reproducibility.

## Interoperability without circular dependencies

Stable references also help preserve package boundaries.

MolSysMT can consume information originating from a Sabueso Card without requiring Sabueso and MolSysMT to become mutually dependent packages.

Nextia can refer to a Praxis Protocol without owning the Protocol.

MolSysSuite can produce an Artifact consumed by Nextia without owning the DiscoveryProject.

Thus:

> **Referencability enables interoperability without collapsing semantic ownership.**

## Security and authorization

Referencability does not imply accessibility.

A valid reference may identify an object that the current user, agent, or service is not authorized to read.

Future remote implementations should therefore separate:

```text
identity
resolution
authorization
```

An object may be identifiable without being resolvable under the current credentials.

This is particularly important for proprietary scientific knowledge and molecular assets.

## Architectural invariant

The scientific identity of important objects should survive changes in:

```text
process
machine
filesystem
database
service
compute provider
deployment topology
```

Architecture 1.0 therefore adopts the principle:

> **Serializable objects + stable references + explicit provenance are prerequisites for a local-first, remote-ready MOLI Platform.**

