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

## 22. Design principles

> **ProjectGraph is the evolving scientific graph of a DiscoveryProject and is owned by Nextia.**

> **ProjectRecord is the cross-platform provenance record required for audit and reproducibility and is composed by MOLI infrastructure.**

> **ProjectWorkspace provides project-scoped organization and reference/storage context; ProjectStore provides physical storage.**

> **ProjectGraph scientific continuity and ProjectRecord provenance continuity are distinct and complementary.**

> **Components own their scientific objects; MOLI provides stable cross-component references, provenance infrastructure, project organization, portability, and project-level views.**

> **No component should need to duplicate another component's authoritative object to participate in a project.**

> **The ProjectGraph may continue to grow after Conclusions; new Knowledge/Evidence can open new branches without rewriting history.**

> **The scientific project must remain auditable and replayable without the LLM that helped orchestrate it.**
