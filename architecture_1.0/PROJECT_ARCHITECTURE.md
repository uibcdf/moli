# MOLI Project Architecture

## Status

This document refines consequences of the frozen MOLI Platform Architecture 1.0. It does not add a new top-level scientific component or change the structural view.

It defines how a real scientific project is organized, how its scientific continuity grows, how distributed component-owned objects become a complete auditable record, and how that record supports audit, trace, replay, and scientific communication.

## Core distinction

A MOLI project needs four complementary concepts:

- **MOLI Project Workspace** — the logical project-scoped organization and access context.
- **Nextia ProjectGraph** — the evolving scientific graph of the DiscoveryProject.
- **MOLI ProjectRecord** — the complete cross-platform provenance/history required for audit and reproducibility.
- **MOLI ProjectStore** — the physical storage backend(s) holding project data and artifacts.

These concepts are related but not interchangeable.

    ProjectWorkspace
           |
      +----+-------------+
      |                  |
      v                  v
  ProjectGraph      ProjectRecord
     Nextia              MOLI
      |                  |
      +--------+---------+
               |
               v
          ProjectStore
    local / NAS / HPC / cloud /
    databases / object storage

Scientific Communication consumes the graph and record but is not the authoritative project history.

## 1. MOLI Project Workspace

The Project Workspace is the logical place in which a scientific project operates.

It provides project-scoped organization, identity, references, storage resolution, and access context to participating components.

Components should not independently invent where project records live.

> **Components do not choose where project records live; the MOLI Project Workspace provides their project-scoped storage and reference context.**

A local implementation may eventually resemble:

    project/
    ├── moli.project.toml
    ├── knowledge/
    ├── methodology/
    ├── discovery/
    ├── modeling/
    ├── record/
    ├── artifacts/
    ├── notebooks/
    └── communication/

This directory layout is illustrative, not frozen.

The logical contract is more important than a particular filesystem representation.

A future remote/distributed implementation may expose the same logical scopes while storing objects in databases, object storage, HPC filesystems, or services.

## 2. Component namespaces and ownership

The Workspace does not create shared semantic ownership.

Conceptually:

    knowledge/
        Sabueso-owned objects

    methodology/
        Praxis-owned objects

    discovery/
        Nextia-owned objects

    modeling/
        MolSysSuite-owned objects

    record/
        MOLI cross-platform provenance infrastructure

Components write the objects whose semantics they own.

A component must not silently rewrite another component's authoritative object.

> **Components own the semantics of the objects they create; MOLI owns project-level organization, cross-component identity/reference infrastructure, provenance composition, and portability.**

## 3. Nextia ProjectGraph

A DiscoveryProject is graph-shaped. Nextia owns the persistent scientific continuity of that graph.

The **ProjectGraph** is the evolving, structured scientific graph connecting concepts such as:

    Question
        ↓
    Hypothesis
        ↓
    Decision
        ↓
    Campaign
        ↓
    Execution reference
        ↓
    Result reference
        ↓
    Observation
        ↓
    Evidence
        ↓
    Decision / Conclusion / new Question
        ↓
       ...

The graph may branch, converge, revisit previous questions, reject hypotheses, preserve failed work, reopen conclusions, and grow indefinitely.

A Conclusion does not necessarily close the graph. New Knowledge or Evidence may motivate new Questions and branches later.

### ProjectGraph is not prose

Nextia does not primarily preserve project continuity by writing a narrative document.

It preserves explicit scientific objects and typed relationships among them.

Human-readable narrative is later produced by MOLI Scientific Communication.

### ProjectGraph references external objects

The ProjectGraph should not copy all data owned by other components.

For example:

    Evidence E17
        based_on / informed_by
            Sabueso SourceAssertion SA42

    Observation O31
        derived_from
            TopoMT Result R71

    Campaign C4
        uses
            Praxis Protocol P12

Stable cross-component references preserve ownership while allowing scientific meaning to remain connected.

## 4. Scientific continuity versus provenance continuity

Two complementary forms of continuity exist.

### Nextia scientific continuity

Answers:

- What were we asking?
- What did we hypothesize?
- What did a Result mean in project context?
- What Evidence changed our view?
- Why did we choose the next scientific branch?
- What did we conclude?
- What remains unresolved?

This continuity lives in the ProjectGraph.

### MOLI provenance continuity

Answers:

- What exactly happened?
- In what order?
- Who or what acted?
- What was executed?
- With which inputs, parameters, versions, environment, and resources?
- What failed or was retried?
- Which immutable objects and hashes were involved?
- Can the recorded computation be replayed?

This continuity lives in the ProjectRecord.

The two are linked but should not be collapsed.

## 5. MOLI ProjectRecord

The **ProjectRecord** is the complete cross-platform record required for audit, traceability, reproducibility, and replay.

It is composed from distributed component-owned records plus MOLI-level provenance infrastructure.

It may include/reference:

- KnowledgeSnapshots;
- ProjectGraph states;
- Decisions and approvals;
- ExecutionPlans;
- Runs and retries;
- commands/API invocations;
- environments;
- inputs and transformation lineage;
- Results and Artifacts;
- manual actions/curation;
- AgentActions;
- EventLedger;
- ProjectStateSnapshots;
- ProjectManifest;
- IntegrityManifest;
- ReplayComparison records;
- ProjectReleases;
- ScientificCommunicationArtifacts.

The ProjectRecord is not a second copy of every scientific object. It is a federated/composed record based on stable references, manifests, events, and integrity information.

## 6. MOLI ProjectStore

The ProjectStore is the physical storage layer.

It may be:

- local filesystem;
- NAS;
- HPC filesystem;
- object storage;
- database;
- remote service;
- cold archive;
- hybrid combinations.

The Workspace and scientific object identities must not depend on one particular storage topology.

Large Artifacts may live outside the visible Workspace directory while being referenced through stable identity, hash, availability, retention, and storage metadata.

Therefore:

    ProjectWorkspace ≠ ProjectStore

and:

    object identity ≠ filesystem path

## 7. Project entry point

A project should eventually expose a small authoritative project descriptor, conceptually similar to:

    moli.project.toml

It may identify:

- project identity;
- schema/architecture version;
- logical scopes;
- participating components;
- storage resolution;
- visibility/authorization policy;
- record/manifests;
- active/frozen release state.

The exact filename/schema is not frozen.

All components should receive project context through MOLI rather than hard-coding independent paths.

Conceptually:

    project = moli.open_project(...)

    project.knowledge
    project.methodology
    project.discovery
    project.modeling
    project.record
    project.artifacts

The final API is open.

## 8. MOLI Provenance Infrastructure

Provenance is cross-cutting infrastructure, not a new scientific component analogous to Sabueso, Praxis, or Nextia.

Its conceptual responsibilities are:

### Identity and references

Stable, resolvable cross-component references to persistent scientific objects.

### Event ledger

An append-only or equivalently immutable history of consequential project events.

### Manifest and integrity

Project-level manifests, hashes/content identities, snapshots, availability/retention metadata, and release records.

### Replay and verification

Preflight, historical/migrated replay, replay execution, and comparison against recorded Results.

This infrastructure belongs to MOLI platform architecture.

A separate implementation repository is not implied by this document.

## 9. Provenance Contract

Every participating component should satisfy a small common project/provenance contract appropriate to its objects.

Conceptually, persistent objects should be able to expose or resolve:

    stable reference
    owner/component
    object type
    version/revision
    content identity/hash where applicable
    provenance
    dependencies / parents
    created-by / created-at
    project scope
    visibility/authorization metadata where applicable

Execution-producing components additionally expose execution-specific provenance.

Components may emit consequential events into the MOLI EventLedger.

The exact interface is not frozen.

A current implementation direction is **Scribe**, documented in [`../devguide/SCRIBE.md`](../devguide/SCRIBE.md): low-friction semantic instrumentation using decorators, propagated project context, explicit recording APIs, safe serializers/redaction, recording profiles, event emission, and ownership-aware routing. Scribe is not a new scientific component, and its package/repository boundary remains open.

The goal is that MOLI can ask of an object:

> What are you?

> Who owns/created you?

> Which version/content are you?

> What do you depend on?

> What did you produce?

without understanding every component's internal storage implementation.

## 10. No shared mutable megastore

MOLI should not solve provenance by allowing every component to mutate one undifferentiated project database.

Avoid:

    Sabueso ----┐
    Praxis -----┤
    Nextia -----┼── arbitrary writes ──> shared scientific megastore
    MolSysSuite ┤
    Agent ------┘

Prefer:

    component-owned objects
             +
    stable cross-component references
             +
    typed ProjectGraph relationships
             +
    shared provenance/event contract
             ↓
       composed ProjectRecord

This preserves semantic ownership and extensibility.

## 11. EventLedger

A component creates its authoritative object locally/within its owned scope and emits a project event referencing that object.

For example:

    TopoMT
        creates Result R17

    EventLedger
        ResultCreated
        object_ref = R17
        project = TcTIM
        actor = TopoMT
        timestamp
        version/hash

The event does not need to duplicate the Result.

Sabueso may emit SourceAssertionAdded or KnowledgeSnapshotCreated.

Nextia may emit HypothesisCreated, EvidenceLinked, DecisionApproved, or ConclusionCreated.

MOLI Agent may emit AgentActionProposed or ToolInvocationRequested.

Human approvals may likewise enter the ledger.

## 12. Decision → ExecutionPlan → Run

This boundary is cross-platform and central to reproducibility.

    Nextia scientific Decision
              ↓
        ExecutionPlan
              ↓
            Run
              ↓
       Result / Artifact
              ↓
    Nextia Observation/Evidence

The Decision explains **why**.

The ExecutionPlan freezes **what should be executed**.

The Run records **what actually happened**.

The exact ownership/implementation of ExecutionPlan remains to be formalized, but it belongs to project/execution orchestration rather than to a domain algorithm such as TopoMT.

## 13. Human and agent orchestration share the same record

Phase 1:

    Human
       ↓
    Decision
       ↓
    ExecutionPlan
       ↓
    Run

Phase 2:

    MOLI Agent
       ↓ proposes
    Decision
       ↓ approved as required
    ExecutionPlan
       ↓
    Run

Agentic automation changes who proposes/orchestrates work; it does not create a second provenance model.

## 14. ProjectGraph evolution

The ProjectGraph is appendable/evolvable.

New work may add:

- Questions;
- Hypotheses;
- Strategies;
- Campaigns;
- Decisions;
- Results references;
- Observations;
- Evidence;
- Conclusions;
- contradictions;
- supersession;
- reopened questions.

Historical scientific states must remain reconstructable.

For example, a Conclusion in ProjectRelease 1.0 may later be challenged without rewriting what release 1.0 concluded.

## 15. ProjectGraph snapshots and ProgressBriefs

A ProjectStateSnapshot may capture/reference a version of the ProjectGraph plus relevant Knowledge/modeling/provenance state.

Comparing snapshots can answer:

> What changed since the previous checkpoint?

This provides a structured basis for ProgressBrief generation.

Scientific Communication should not need to infer project change from conversational memory.

## 16. Audit, Trace, Replay, and Communication

MOLI composes the ProjectGraph and ProjectRecord to provide project-level operations.

### Audit

What happened, in what order, under whose authority, and why?

### Trace

Why do we believe this Conclusion/Evidence/Result?

### Replay

Re-execute recorded scientific work using frozen historical decisions/plans without new LLM reasoning.

### Rerun

Start a new discovery trajectory in which human/agent reasoning may choose a different path.

### Communication

Explain the scientific state/history to humans through structured communication artifacts and renderings.

Conceptually:

                         MOLI

        +-----------------+------------------+
        |                 |                  |
        v                 v                  v
      Audit             Replay         Communication
        |                 |                  |
        v                 v                  v
  What happened?      Do it again       Explain it

All consume the same authoritative project infrastructure.

## 17. Notebooks

Jupyter notebooks are first-class human orchestration documents, especially in Phase 1 pilots.

They should be stored/versioned or referenced through the Workspace and recorded sufficiently for reproducibility.

However:

> **Notebooks are not the authoritative ProjectRecord.**

The authoritative scientific objects and execution provenance exist below/alongside the notebook.

A notebook should contain scientific composition, not become the only location of identity, provenance, Evidence, or execution semantics.

## 18. Scientific Communication

MOLI Scientific Communication consumes:

    ProjectGraph
        +
    ProjectRecord
        +
    Knowledge / Results / Artifacts
        ↓
    ScientificCommunicationArtifact
        ↓
    PDF / HTML / Slides / Video

The ProjectGraph provides scientific continuity.

The ProjectRecord provides provenance continuity.

The resulting report/video is a derived human-facing view, not the source of truth.

## 19. Portability and export

Because Workspace semantics are independent of storage topology, a project should eventually be exportable/archivable.

A project bundle may contain:

- project descriptor;
- ProjectManifest / IntegrityManifest;
- ProjectGraph snapshot/release;
- EventLedger;
- notebooks;
- environment specifications;
- small Artifacts;
- stable references to large/external Artifacts;
- checksums;
- communication artifacts.

A self-contained export may include all legally/technically retainable Artifacts.

Exact packaging/CLI is not frozen.

## 20. Local-first and remote-ready

The same conceptual project model must work when everything is local and when infrastructure later becomes distributed.

Today:

    local Workspace
    local notebooks
    local scientific components

Future:

    remote Knowledge store
    remote ProjectStore
    HPC/cloud execution
    shared databases
    object storage

The scientific semantics, stable references, ProjectGraph, and ProjectRecord remain unchanged.

## 21. Architecture summary

The complete project-level architecture is:

    Sabueso
        MEMORY OF EXTERNAL KNOWLEDGE

    Praxis
        MEMORY OF HOW TO DO SCIENCE

    MolSysSuite
        MEMORY OF COMPUTATION

    Nextia ProjectGraph
        MEMORY OF DISCOVERY

    MOLI ProjectRecord
        MEMORY OF WHAT HAPPENED

    MOLI Agent
        REASONING / ORCHESTRATION

    MOLI Scientific Communication
        EXPLANATION TO HUMANS

These are complementary responsibilities, not competing stores.



## 23. Project-scoped references to shared objects

Not every object referenced by a project is owned by or physically contained inside that project.

Sabueso Knowledge and Praxis Know-how may be shared across many projects.

The Workspace therefore provides **project scope and references**, not forced duplication or project ownership.

For example:

    TcTIM ProjectGraph
        |
        +--> Sabueso SourceAssertion SA42
        +--> Praxis Protocol P12

SA42 and P12 may remain globally/shared owned objects while the project records which version/snapshot it relied on.

A project-specific snapshot/reference must preserve enough identity/version information to reconstruct the historical dependency without converting shared Knowledge/Know-how into project-owned copies.

> **Project membership/reference does not imply semantic ownership or physical containment.**

## 24. ProjectGraph semantic ownership

Nextia owns the semantic Discovery objects that give the ProjectGraph scientific meaning, including Questions, Hypotheses, Strategies, Campaigns, project Decisions, Observations, Evidence, and Conclusions.

The ProjectGraph may contain typed references to externally owned objects such as SourceAssertions, Protocols, ExecutionPlans, Runs, Results, Artifacts, molecular systems, and Candidates when those objects are owned elsewhere.

A technical event or Run does not become a Nextia semantic object merely because it is referenced by the graph.

Conversely, the ProjectRecord does not become the owner of a Decision or Conclusion merely because it records its creation/version/integrity.

## 25. EventLedger versus ProjectGraph

The EventLedger and ProjectGraph have different authority.

- **ProjectGraph** is the semantic scientific state/history of Discovery.
- **EventLedger** is chronological provenance that records consequential changes/actions across the project.

For example:

    Nextia creates Decision D17
            |
            +--> ProjectGraph gains/versions D17
            |
            +--> EventLedger records DecisionCreated(D17)

The event records that a semantic change occurred; it does not define the scientific meaning of D17.

Rebuilding a ProjectGraph view from events may be technically possible in a future implementation, but Architecture 1.0 does not require event sourcing as the semantic storage model.

> **EventLedger records change; ProjectGraph owns Discovery meaning.**

## 26. Cross-component consistency and incomplete operations

A scientific operation may span several components:

    Decision
       ↓
    ExecutionPlan
       ↓
    Run
       ↓
    Result
       ↓
    Observation

Failures may occur between any two steps.

MOLI must not hide partial cross-component state or falsely imply atomic scientific completion.

Cross-component orchestration should therefore support explicit lifecycle/status and correlation identity sufficient to distinguish:

- requested;
- accepted;
- started;
- partially completed;
- completed;
- failed;
- cancelled;
- superseded/abandoned.

Where one logical action produces objects in several components, those records should share a correlation/operation identity or equivalent linkage.

Compensation/recovery must create new provenance rather than deleting evidence of the failed partial operation.

A ProjectGraph relationship that depends on an external Result should not be treated as satisfied until the referenced Result exists in an admissible state.

The exact transaction/distributed-consistency mechanism is implementation-open.

> **MOLI requires auditable consistency, not fictitious distributed atomicity.**

## 27. Reference resolution and unavailable objects

Stable references may temporarily or permanently fail to resolve because of authorization, retention, remote-service failure, archival state, or deleted/unavailable external content.

The ProjectGraph and ProjectRecord must preserve the reference and its historical identity even when current content cannot be resolved.

Consumers should distinguish:

    resolvable
    unavailable
    unauthorized
    archived/offline
    externally removed
    unknown

from:

    object never existed

This is necessary for long-lived audit and honest replay preflight.




## 28. Three-level project integration model

The project architecture can be understood through three levels:

### Level 1 — Component records

    Sabueso
    Praxis
    Nextia
    MolSysSuite
    ...

Each component owns and records the objects whose scientific semantics belong to it.

### Level 2 — MOLI provenance infrastructure

    stable identity and references
    EventLedger
    integrity
    snapshots / manifests
    cross-component lineage
    replay / verification

This level connects distributed records without taking semantic ownership from their components.

### Level 3 — MOLI project views and operations

    ProjectManifest
    Audit
    Trace
    Replay
    Timeline
    Scientific Communication

These are project-level compositions over the lower levels.

The three-level model is explanatory, not a requirement for three physical services or databases.

## 29. Preferred initial Workspace materialization

Architecture remains storage/deployment independent, but an initial local implementation should prefer a **human-browsable filesystem Workspace** when practical.

This supports Phase 1 scientific work in Jupyter and makes the project inspectable without requiring remote infrastructure.

A local Workspace may materialize the logical scopes described earlier while using references/manifests for data that live elsewhere.

This preference does not freeze the directory layout and does not make filesystem paths scientific identities.

## 30. Version-control guidance

The Workspace should distinguish material that is naturally version-controlled from large or externally managed scientific data.

Typically suitable for Git or equivalent source version control:

    project descriptor
    notebooks
    manifests
    small structured records
    schemas/configuration
    selected communication artifacts

Typically referenced through ProjectStore rather than committed directly:

    trajectories
    large datasets
    large molecular ensembles
    model weights
    large generated Artifacts

This is operational guidance rather than an absolute rule. ProjectManifest/Artifact metadata should identify the authoritative location and content identity regardless of version-control choice.

## 31. Workspace descriptor as bootstrap contract

A project descriptor such as the conceptual `moli.project.toml` is not merely descriptive metadata.

It is the bootstrap entry point through which MOLI and participating components discover the project-scoped logical context:

    project identity
    architecture/schema version
    logical scopes
    component participation
    ProjectRecord entry points
    ProjectStore resolution
    authorization/visibility context
    release state

Components should receive resolved project context rather than inventing independent project paths.

The exact filename and schema remain open.

## 32. Historical ProjectGraph views, diffs, and timeline

Because ProjectGraph is versioned/evolvable and the ProjectRecord preserves chronological provenance, MOLI should eventually support three distinct inspection capabilities:

### Historical graph view

Inspect/reconstruct the scientific graph at a prior snapshot, release, or time boundary.

Conceptually:

    project.graph.at(snapshot_or_time)

### Graph/state diff

Inspect what scientific state changed between two checkpoints.

Conceptually:

    project.graph.diff(T1, T2)

This can ground ProgressBrief generation.

### Project timeline

Present a chronological view composed from Nextia scientific changes and relevant EventLedger events.

Conceptually:

    project.timeline()

The API names are illustrative, not frozen.

A timeline is a view over semantic/project provenance; it is not a replacement for ProjectGraph or EventLedger.

## 33. ProjectRecord views may be virtual

MOLI may compose project-wide views from:

    Sabueso records
        +
    Praxis records
        +
    Nextia ProjectGraph
        +
    MolSysSuite execution records
        +
    EventLedger / manifests
        ↓
    project-wide view

Architecture does **not** require MOLI to persist a second global database/graph containing copies of all component objects.

A ProjectRecord view may be materialized, cached, indexed, or computed on demand.

> **Federated/composed ProjectRecord does not imply duplicated persistent global graph.**

This preserves the no-megastore ownership principle while allowing complete project-level Audit/Trace/Replay views.

## 34. Portable export modes

Project portability should support at least two conceptual export modes.

### Reference export

Packages the portable project record while allowing large or externally controlled data to remain referenced:

    project descriptor
    ProjectManifest / IntegrityManifest
    ProjectGraph snapshot/release
    EventLedger
    notebooks
    environment specifications
    small Artifacts
    stable references to external/large Artifacts
    checksums

### Self-contained archival export

Attempts to include all legally and technically retainable inputs/Artifacts required for independent archival/replay.

Objects that cannot be embedded because of size, licensing, authorization, or external-service constraints remain explicit unresolved/external dependencies rather than disappearing from the manifest.

Exact archive format and CLI are implementation-open.

## 35. Why Nextia provides scientific continuity

Nextia does not provide ProjectGraph continuity because it governs or owns Sabueso, Praxis, or MolSysSuite.

It provides continuity because **Discovery is the domain in which previous Knowledge, actions, Results, and Evidence acquire project-specific scientific meaning and motivate subsequent Questions, Hypotheses, Decisions, and work**.

Thus:

    Sabueso
        what external sources assert

    Praxis
        how scientific work can be performed

    MolSysSuite
        what was computed / produced

    Nextia ProjectGraph
        what those things mean for this DiscoveryProject
        and how that meaning leads to subsequent work

This is semantic continuity, not hierarchical control.

## 36. Design principles

> **ProjectGraph is the evolving scientific graph of a DiscoveryProject and is owned by Nextia.**

> **ProjectRecord is the cross-platform provenance record required for audit and reproducibility and is composed by MOLI infrastructure.**

> **ProjectWorkspace provides project-scoped organization and reference/storage context; ProjectStore provides physical storage.**

> **ProjectGraph scientific continuity and ProjectRecord provenance continuity are distinct and complementary.**

> **Components own their scientific objects; MOLI provides stable cross-component references, provenance infrastructure, project organization, portability, and project-level views.**

> **No component should need to duplicate another component's authoritative object to participate in a project.**

> **The ProjectGraph may continue to grow after Conclusions; new Knowledge/Evidence can open new branches without rewriting history.**

> **The scientific project must remain auditable and replayable without the LLM that helped orchestrate it.**

> **Project membership/reference does not imply semantic ownership or physical containment.**

> **EventLedger records change; ProjectGraph owns Discovery meaning.**

> **MOLI requires auditable cross-component consistency and explicit partial/failure states rather than fictitious distributed atomicity.**

> **Stable historical references remain meaningful even when their current targets are unavailable or unauthorized.**

> **The project architecture has three conceptual levels: component-owned records, MOLI provenance infrastructure, and composed project-level views/operations.**

> **A human-browsable local Workspace is the preferred initial materialization when practical, while scientific identity remains independent of filesystem layout.**

> **ProjectRecord views may be federated or virtual; MOLI does not require a duplicated persistent global graph.**

> **Project portability distinguishes reference exports from self-contained archival exports.**

> **Nextia provides scientific continuity through Discovery semantics, not hierarchical control over other components.**
