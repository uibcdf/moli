# Scribe — MOLI Provenance Instrumentation

## Status

**Scribe** is the working name for the low-friction provenance/instrumentation mechanism that may implement important parts of the MOLI Provenance Contract.

Scribe is an **implementation direction**, not a new scientific component alongside Sabueso, Praxis, Nextia, or MolSysSuite, and this document does not yet freeze a package/repository boundary or exact Python API.

The name evokes a scribe whose role is to observe and faithfully record what happens without deciding what the science means.

## Purpose

MOLI requires distributed components to preserve enough structured provenance for ProjectRecord, EventLedger, Audit, Trace, Replay, ProjectRelease, and Scientific Communication.

Requiring every scientific function to hand-write this infrastructure would create duplicated boilerplate and inconsistent records.

Scribe should provide a common, low-friction way to instrument **scientifically meaningful operations** across MOLI components.

Conceptually:

    Sabueso --------┐
    Praxis ---------|
    Nextia ---------|
    MolSysMT -------|
    TopoMT ---------|
    DockingMT ------|
    ...             |
                    v
                 Scribe
       context + instrumentation
       profiles + safe capture
       routing + event emission
                    |
                    v
        MOLI Provenance Contract
                    |
          +---------+---------+
          v                   v
      EventLedger        ProjectRecord

Component-owned scientific objects remain owned by their components.

## Scribe records; it does not interpret

Scribe's central boundary is:

    AUTOMATIC / STRUCTURED RECORDING

    what happened
    where it happened
    who/what executed it
    with what inputs/parameters
    with what software/environment
    what it produced
    whether it failed
    how it relates operationally to parent work

versus:

    EXPLICIT DISCOVERY SEMANTICS

    what a Result means scientifically
    which Hypothesis it bears on
    whether it supports/contradicts
    what Decision should follow

The second category belongs to Nextia Discovery semantics and must not be inferred merely because Scribe observed a computation.

For example, TopoMT may produce Result R71 and Scribe may record the complete operation. Only an explicit Nextia operation should create an Observation or Evidence relationship saying what R71 means for a Hypothesis.

> **Components own scientific meaning; Scribe records consequential operations and semantic changes.**

> **Nextia owns Discovery meaning; Scribe records the provenance and evolution of that meaning in the ProjectGraph.**

Scribe therefore remains active when work enters Nextia. It can instrument the explicit operation that creates an Observation, links Evidence to a Hypothesis, records a Decision, rejects/supersedes a Hypothesis, or otherwise mutates the ProjectGraph. What Scribe must not do is invent that Discovery meaning merely because it observed an upstream computation.

## Instrumentation mechanisms

Scribe should support more than one instrumentation mechanism because not all scientific work has the same shape.

### Decorators

A natural Python mechanism for stable semantic API boundaries:

    @scribe.record(profile="scientific_analysis")
    def detect_pockets(...):
        ...

The decorator may capture invocation metadata before/after execution.

### Context managers

Useful for establishing inherited project/execution scope:

    with scribe.context(...):
        ...

or conceptually:

    with project.run(execution_plan):
        ...

Operations executed inside inherit the active context.

### Explicit recording API

Manual scientific actions, external processes, notebooks, or operations that cannot be cleanly decorated need an explicit API.

The final syntax is open. Decorators are an important convenience mechanism, not the only provenance mechanism.

## Instrument semantic boundaries, not every function

Scribe should not decorate every private helper.

Avoid producing provenance noise for implementation details such as internal string normalization or trivial utility calls.

Prefer instrumentation at semantic boundaries such as:

- knowledge retrieval;
- entity resolution;
- knowledge derivation;
- molecular-system transformation;
- model construction;
- scientific analysis;
- comparison;
- simulation;
- Capability execution;
- Protocol execution;
- Result/Artifact production;
- ProjectGraph mutation;
- manual scientific action;
- communication generation where relevant.

The exact catalog should remain small enough to preserve meaning.

## Recording profiles

Scribe should use **semantic recording profiles**.

A profile answers:

> What kind of operation is this, and what provenance fields/behaviors are expected?

Candidate profiles include:

    knowledge_retrieval
    entity_resolution
    knowledge_derivation

    transformation
    scientific_analysis
    comparison
    simulation

    capability_execution
    protocol_execution

    project_graph_mutation
    decision
    manual_action

    communication

These names are provisional.

Profiles should not be one-per-function. They should describe reusable semantic categories.

### Example: knowledge retrieval

May expect:

- external source;
- query/request;
- source/service version when available;
- retrieval timestamp;
- response/snapshot/hash;
- produced SourceAssertions/objects;
- licensing/retention constraints.

### Example: scientific analysis

May expect:

- scientific inputs/references;
- parameters;
- implementation/version;
- environment;
- random seeds where relevant;
- Results/Artifacts;
- timing/status/failure.

### Example: transformation

May expect:

- input object references;
- transformation identity;
- parameters;
- output object references;
- lineage.

### Example: ProjectGraph mutation

May expect:

- Nextia semantic object type;
- previous graph state/version where relevant;
- created/updated node/relationship;
- actor;
- rationale/approval where semantically required.

The profile does not transfer semantic ownership to Scribe.

## Component detection and explicit ownership metadata

Scribe may automatically detect implementation metadata such as:

    package
    module
    function
    package version
    Git commit

For example, instrumentation inside TopoMT may normally infer that the executing implementation belongs to TopoMT.

However, automatic detection must not be the final authority for semantic ownership.

Prefer the precedence:

    explicit metadata
        ↓
    registered package/component metadata
        ↓
    automatic detection fallback

This allows instrumentation to remain convenient while preserving correctness in wrappers, plugins, delegated execution, tests, or unusual packaging.

## Safe automatic capture of function inputs

Decorators can use Python signatures to bind arguments and capture scientifically relevant invocation state.

For example:

    detect_pockets(
        molecular_system,
        probe_radius=...,
        threshold=...
    )

may record:

    molecular_system:
        stable reference / content identity

    probe_radius:
        value + unit where available

    threshold:
        value

Scribe must not blindly serialize arbitrary Python arguments.

Inputs may include:

- secrets/API keys;
- huge NumPy arrays;
- trajectories;
- file handles;
- GPU/runtime objects;
- callbacks;
- database/service clients;
- objects with sensitive fields.

Scribe therefore requires pluggable **serializers/reference adapters** and **redaction policies**.

Large/persistent scientific objects should normally be represented by stable reference/version/hash rather than bulk serialization.

Secrets must never be persisted merely because they were function arguments.

## Output capture

Instrumentation may observe return values and created objects.

A recorded operation may capture/reference:

- Result objects;
- Artifact objects;
- transformed scientific objects;
- stable references;
- content hashes;
- status;
- exceptions/failures.

The component remains responsible for creating the authoritative domain object. Scribe records its provenance and routing relationships.

## Project context propagation

Scribe should understand the currently active MOLI project scope without requiring every scientific API to add project-specific arguments.

A propagated context may include:

    Project
    Workspace
    Campaign
    Experiment / scientific work unit
    ExecutionPlan
    Run
    actor
    correlation identity
    authorization scope
    record/event destinations

The exact vocabulary must align with final Nextia/project semantics; for example, an `Experiment` object should not be introduced solely by Scribe if Nextia does not define it.

Python `contextvars` or equivalent mechanisms may be appropriate for local propagation, but implementation is open.

## Nested execution and correlation

Scientific operations are frequently nested:

    Campaign
        ↓
    ExecutionPlan
        ↓
    Run
        ├── MolSysMT prepare
        ├── TopoMT detect
        ├── TopoMT characterize
        └── MolSysViewer scene

Nested instrumented operations should inherit project/run/correlation context while preserving their own:

- component;
- operation identity;
- parent operation;
- inputs;
- outputs;
- status.

This can produce a reproducible execution DAG without forcing one component to own all nested operations.

Correlation identity is particularly important for partial failure and distributed execution.

## Semantic routing

Scribe should know **where different parts of a record belong**, based on active context, semantic profile, component ownership, and routing policy.

Routing is distinct from capture.

### TopoMT scientific analysis

Conceptually:

    component = TopoMT
    profile = scientific_analysis
    project = TcTIM
    campaign = C3
    work scope = E7

may route to:

    TopoMT local provenance / authoritative Result
    MOLI EventLedger
    MOLI ProjectRecord
    current Run / correlation scope

It does **not** automatically create Nextia Observation/Evidence.

### Nextia ProjectGraph mutation

Conceptually:

    component = Nextia
    profile = project_graph_mutation

may result in:

    authoritative Nextia ProjectGraph mutation
    EventLedger event
    ProjectRecord provenance

### Sabueso knowledge retrieval

Conceptually:

    component = Sabueso
    profile = knowledge_retrieval

may result in:

    authoritative Sabueso retrieval/SourceAssertions
    EventLedger event
    ProjectRecord provenance

A later Nextia operation may explicitly connect a Sabueso SourceAssertion to project Evidence.

## End-to-end example: execution to Discovery meaning

Consider a TopoMT analysis whose Result is later interpreted inside Nextia.

    TopoMT.detect_pockets(...)
            |
            | Scribe: scientific_analysis
            v
        Result R71
            |
            +--> TopoMT authoritative Result/provenance
            +--> EventLedger: ResultCreated
            +--> ProjectRecord: execution provenance
            |
            v
    human / MOLI Agent interprets R71
            |
            v
    Nextia.add_observation(...)
            |
            | Scribe: project_graph_mutation
            v
        Observation O17
        ProjectGraph v17 -> v18
        EventLedger: ObservationCreated
        ProjectRecord: GraphMutation provenance
            |
            v
    Nextia.add_evidence(...)
            |
            | Scribe: project_graph_mutation
            v
        Evidence E21
        E21 --supports--> H3
        ProjectGraph v18 -> v19
        EventLedger: EvidenceCreated / EvidenceLinked
        ProjectRecord: GraphMutation provenance

The first Scribe record does not infer that R71 supports H3.

The later Scribe records state that **Nextia authoritatively created** O17, E21, and the `supports` relationship. Scribe records those semantic changes because they occurred; Nextia defines and owns their Discovery meaning.

### ProjectGraph mutation provenance

For a consequential Nextia mutation, Scribe should be able to capture/reference, as applicable:

    actor
    Nextia operation
    Project / Campaign / active work scope
    graph version/snapshot before mutation
    created / modified semantic objects
    created / modified typed relationships
    graph version/snapshot after mutation
    explicit rationale where supplied/required
    approval where required
    timestamp
    correlation identity
    referenced upstream objects

For example, Scribe may record that Nextia created:

    Evidence E21
        --supports--> Hypothesis H3

but Scribe does not independently define what `supports` means, decide that the relation should exist, or infer it from R71. Those semantics and validation rules belong to Nextia.

The same principle applies to other ProjectGraph changes:

    Hypothesis rejected
    Hypothesis superseded
    Decision created / approved
    Campaign stopped
    Conclusion created
    Conclusion challenged / superseded
    new Question opened

Scribe should make the evolution of Discovery meaning auditable without becoming the owner or interpreter of that meaning.

## Routing policy must preserve ownership

Scribe is not permission to write arbitrary objects into every destination.

Routing must respect the architecture:

    Sabueso owns Knowledge semantics
    Praxis owns Know-how semantics
    Nextia owns Discovery semantics
    MolSysSuite components own modeling/execution-specific domain outputs
    MOLI owns cross-platform provenance composition

Scribe may coordinate/event-record these actions but must not silently cross semantic ownership boundaries.

## Structured records before human language

Scribe should emit structured records/events, not final human-facing prose.

Avoid making provenance depend on phrases such as:

    "TopoMT identified a pocket..."

Instead record structured facts and references.

Scientific Communication may later transform the same ProjectGraph/ProjectRecord into:

- scientist-facing explanation;
- technical report;
- ProgressBrief;
- audit view;
- slides;
- narrated video.

> **Recording and communication are separate concerns.**

## Operation lifecycle

Instrumentation should preserve lifecycle states and failures, including:

    requested
    accepted
    started
    partial
    completed
    failed
    cancelled
    superseded / abandoned

A decorator/context should record exceptions and failed attempts rather than emitting only successful completion.

Retries remain separate Runs/operations linked through correlation/provenance.

## ExecutionPlan and Run integration

Scribe should integrate naturally with the Architecture 1.0 boundary:

    Decision
        ↓
    ExecutionPlan
        ↓
    Run
        ↓
    Result / Artifact
        ↓
    Observation / Evidence

Within a Run, Scribe can capture the actual API/CLI operations that implement the ExecutionPlan.

This makes replay independent of re-running agent reasoning.

Scribe does not itself decide the scientific Decision or interpret the resulting Evidence.

## Event emission

Scribe may provide the common mechanism through which participating components emit consequential events such as:

    RetrievalStarted
    RetrievalCompleted
    SourceAssertionCreated

    RunStarted
    RunCompleted
    RunFailed

    ResultCreated
    ArtifactCreated

    ObservationCreated
    EvidenceLinked
    DecisionApproved

Event names/schema remain open and should be governed centrally enough to avoid incompatible vocabularies.

Events should reference authoritative objects rather than duplicate their complete content.

## Operation outside a MOLI project

MOLI must not become a mandatory gateway to component APIs.

For example:

    topomt.detect_pockets(system)

should remain scientifically usable outside an active MOLI Workspace.

Possible behavior:

    no active MOLI project
        ↓
    function executes normally
        ↓
    optional local provenance / no project routing

versus:

    active MOLI project context
        ↓
    same function executes
        +
    project provenance/events automatically captured

> **Instrumentation must not make MOLI a mandatory gateway to component APIs.**

## Manual actions

Not all scientific work is a decorated Python call.

Scribe should support explicit recording of:

- manual inspection;
- manual curation;
- manual selection/exclusion;
- human approval;
- external GUI/CLI work;
- imported experimental results.

Manual records must preserve actor, timestamp, referenced objects, rationale/context, and relevant outputs/relationships.

## Notebooks

Phase 1 notebooks are a primary environment in which Scribe should prove useful.

A notebook should be able to call normal Sabueso/Praxis/Nextia/MolSysSuite APIs while Scribe captures the underlying scientifically meaningful operations.

The notebook remains a human-readable orchestration document; Scribe helps ensure it is not the only provenance record.

## Profiles and routing are configuration, not prose

Scribe may maintain centrally governed profile definitions and routing rules.

These definitions should specify:

- expected semantic fields;
- capture behavior;
- serializer/reference behavior;
- redaction;
- event type(s);
- allowed/required destinations;
- ownership constraints;
- lifecycle behavior.

Human-facing phrases belong to Scientific Communication templates/renderers, not Scribe recording profiles.

## Extensibility

A future component such as a quantum-chemistry package should be able to participate by:

1. registering component identity/ownership metadata;
2. satisfying the MOLI Provenance Contract;
3. instrumenting its semantic boundaries;
4. using common profiles or defining governed extensions;
5. emitting references/events into active project context.

MOLI should not need intimate knowledge of the component's internal storage implementation.

## Minimal first experiment

Do not implement all Scribe capabilities before testing the design.

Sabueso is a good first proving ground.

For example, instrument one real knowledge-retrieval boundary and one entity-resolution boundary.

The experiment should test whether Scribe can capture:

- component/function/version;
- active project context;
- input references/parameters;
- external source/query;
- retrieval time;
- response hash/snapshot reference;
- produced authoritative Sabueso objects;
- status/failure;
- EventLedger routing;
- ProjectRecord linkage;
- secret redaction.

Then use the TcTIM Phase 1 notebook to expose missing semantics.

A similar later experiment in TopoMT should test scientific-analysis capture, nested MolSysSuite execution, Results/Artifacts, and Run correlation.





## Scoped ProjectRecord views

Project context and correlation metadata should make it possible to reconstruct the complete record associated with a meaningful scientific scope without requiring each component to know how that record will later be presented.

Conceptually, MOLI should be able to derive views such as:

    ProjectRecord for Project
    ProjectRecord for Campaign
    ProjectRecord for Run
    ProjectRecord for ExecutionPlan
    ProjectRecord for an active scientific work scope

If Nextia eventually defines an `Experiment` or equivalent semantic object, the same mechanism may provide an experiment-scoped record. Scribe must not invent that Discovery concept solely for reporting convenience.

A scoped record may cross component boundaries:

    work scope E7
        |
        +-- MolSysMT
        |     prepare(...)
        |
        +-- TopoMT
        |     detect_pockets(...)
        |     characterize(...)
        |
        +-- MolSysViewer
        |     create_scene(...)
        |
        +-- Nextia
              Observation O17
              Evidence E21

This is possible because the relevant operations/objects carry sufficient project scope, parent/correlation identity, and stable references.

Conceptually, future APIs might resemble:

    project.record.for_campaign(C1)
    project.record.for_run(R2)
    project.record.for_scope(E7)

The exact API is not frozen.

### Scoped record is not a report

Scribe does not generate a human-facing report merely because it can reconstruct a scoped record.

The separation is:

    Scribe + ProjectContext
            ↓
    scope/correlation-aware records
            ↓
    Scoped ProjectRecord view
            ↓
    Scientific Communication / Audit / Trace
            ↓
    optional human-facing view

Possible future renderings might include a Campaign report, Run report, experiment/work-scope report, Protocol-execution report, or audit view.

Those are communication/view concerns, not new Scribe semantic ownership.

> **Scribe should preserve enough scope and correlation metadata that MOLI can reconstruct the complete cross-component record of a meaningful scientific work unit after the fact.**


## Routing is resolved from context, not hard-coded destinations

Instrumentation should not normally encode project-specific destinations inside decorators.

Prefer the separation:

    recording profile
        says WHAT kind of operation is being recorded

    active ProjectContext
        says WHERE in the current project scope it belongs

    ownership / routing policy
        says WHAT Scribe may record, reference, or route

For example, avoid coupling a reusable TopoMT function to a specific project path such as:

    @scribe.record(destination="TcTIM/C3/E7")

The same instrumented function should be reusable in another project without modification.

Project/campaign/run/work-scope destinations are resolved from propagated context and Workspace configuration.

Explicit destination overrides may exist for exceptional cases, but should not become the normal integration mechanism.

## Operation identity versus scientific-object identity

A recorded operation has an identity independent of the scientific objects it may create.

For example:

    Operation OP17
        TopoMT.detect_pockets(...)
        status = failed

        Result = none

The failed operation remains part of provenance even though no Result exists.

Likewise, nested execution may contain:

    Run R1
        ├── Operation OP1 — MolSysMT.prepare
        ├── Operation OP2 — TopoMT.detect
        └── Operation OP3 — MolSysViewer.scene

Each operation may reference parent operation, Run, ExecutionPlan, correlation identity, inputs, outputs, lifecycle, and implementation metadata.

Scientific objects such as Result R71 or Artifact A12 retain their own component-owned identities.

> **Operation identity records that an action occurred or was attempted; scientific-object identity records the domain objects created or referenced by that action.**

## Semantic consumption provenance

Reproducibility and audit may require recording not only what an operation created, but also which existing scientific objects it **meaningfully consumed**.

This must not become instrumentation of every Python read/access.

Record semantic consumption when an object's use materially contributes to a consequential scientific operation, decision, interpretation, context assembly, or generated output.

Examples include a Decision or AgentAction consuming:

    KnowledgeSnapshot KS7
    Evidence E3
    Evidence E4
    Protocol P2
    Result R19

or a Scientific Communication operation consuming a particular ProjectStateSnapshot and Conclusions.

This is especially important for reconstructing ContextAssembly:

    what information was available
        ↓
    what subset was selected
        ↓
    what consequential operation consumed it

Consumption references should preserve stable object/version/snapshot identity where appropriate.

> **Scribe records meaningful scientific dependencies, not incidental implementation-level reads.**

## Recording reliability policy

Not every provenance event has the same tolerance for recording failure.

Scribe should support a governed reliability policy, conceptually including at least:

### Strict recording

The consequential operation must not be considered committed/successful if required provenance cannot be durably recorded.

Likely candidates include operations such as:

    DecisionApproved
    ProjectGraph mutation
    ProjectRelease
    irreversible/external consequential action

The exact catalog is policy-driven and not frozen here.

### Best-effort / buffered recording

The scientific operation may proceed when immediate provenance persistence is temporarily unavailable, provided Scribe can safely buffer and later reconcile the record.

Potential examples include selected local/HPC execution telemetry where blocking the scientific calculation would be disproportionate.

Buffered records must preserve ordering/correlation/integrity sufficiently for reconciliation, and the ProjectRecord must expose unresolved provenance gaps rather than silently treating them as complete.

### Policy resolution

Recording reliability may depend on:

    profile
    operation type
    active project policy
    authorization
    destination availability
    deployment mode

The decorator should not independently decide whether an operation is strict.

> **A provenance failure must never be silently indistinguishable from successful complete recording.**


## What Scribe should not become

Scribe should not become:

- a scientific reasoning agent;
- a replacement for Nextia;
- a generic logging framework with no scientific semantics;
- a shared mutable scientific megastore;
- the owner of Sabueso/Praxis/Nextia/MolSysSuite objects;
- a report-writing system;
- a requirement that all component APIs be invoked through MOLI;
- a mechanism that serializes every argument indiscriminately;
- instrumentation on every internal helper function.

## Open implementation questions

Before freezing an API/package, Phase 1 pilots should help determine:

- package/repository boundary: embedded MOLI infrastructure, `scribe`, `moli-scribe`, or another distribution;
- decorator/context-manager/explicit API balance;
- exact profile catalog;
- component registration/discovery;
- context propagation across processes/jobs/remote execution;
- event schema/versioning;
- serializer/reference adapter protocol;
- secret/sensitive-data redaction;
- routing configuration and authorization;
- integration with ExecutionPlan/Run;
- integration with notebooks;
- async/distributed/nested execution;
- performance/overhead;
- failure behavior when provenance storage is temporarily unavailable;
- strict versus best-effort recording policy and which semantic operations require each;
- buffering, ordering, integrity, and reconciliation of offline/distributed records;
- testing strategy for provenance completeness.

## Guiding principles

> **Components own meaning; Scribe records consequential operations and semantic changes.**

> **Nextia owns Discovery meaning; Scribe records the provenance and evolution of that meaning in the ProjectGraph.**

> **Capture and routing are distinct: profiles describe semantic operation types; routing decides where records/events belong under current project context and ownership rules.**

> **Prefer stable references over bulk serialization of scientific objects.**

> **Instrumentation should be low-friction but never silently violate semantic ownership, authorization, or confidentiality.**

> **Scribe should make provenance easier to do correctly than to omit, while keeping component APIs independently usable outside MOLI.**

> **Structured records come before human-readable reporting.**

> **Profiles describe what is recorded; active context and ownership/routing policy determine where it belongs.**

> **Operation identity is distinct from the identities of scientific objects produced or consumed by the operation.**

> **Record meaningful scientific consumption/dependencies, not incidental implementation reads.**

> **Recording reliability is policy-driven; provenance failure must never masquerade as a complete successful record.**

> **Scope and correlation metadata must be sufficient to derive complete cross-component ProjectRecord views for meaningful scientific work units without coupling component code to future report formats.**
