# MOLI — Reproducibility, Audit, Trace, and Replay

## Purpose

A completed MOLI project must preserve enough structured scientific history for an authorized third party who did not participate in the work to determine what was known, asked, decided, considered, approved, executed, produced, observed, interpreted, concluded, rejected, left uncertain, or stopped — and to execute the recorded computational trajectory again.

> **A completed MOLI project must be independently auditable from persistent scientific records, and its recorded computational trajectory must be replayable without requiring an LLM or agent to reason again.**

This is a cross-platform design direction. Exact Python classes, serialization formats, storage engines, and APIs are not frozen here.

## Reproducibility must not depend on agent reasoning

During discovery, a human or MOLI Agent may choose the scientific path. Once chosen, that trajectory must become persistent platform state.

    DISCOVERY

    Human / MOLI Agent
            ↓
         Decision
            ↓
      ExecutionPlan
            ↓
           Run
            ↓
      Result / Artifact
            ↓
        Observation
            ↓
         Evidence
            ↓
         Decision ...

    REPLAY

    recorded Decision
            ↓
    recorded ExecutionPlan
            ↓
    recorded inputs / parameters
            ↓
    recorded environment / versions
            ↓
         execute again

No new scientific decision is required for replay.

## Five layers of the project record

1. **Knowledge state** — what was known, asserted, conflicting, missing, or unknown.
2. **Discovery state** — what was asked, hypothesized, interpreted, decided, rejected, or concluded.
3. **Execution state** — what was planned and what was actually executed.
4. **Interpretation state** — how Results became Observations, Evidence, and Conclusions.
5. **Communication state** — how a scientific state was rendered as briefing, report, slides, web, or video.

## Components record; Nextia connects; MOLI explains

The platform writes its own history while work happens.

- **Sabueso** records external SourceAssertions, relationships, provenance, conflicts, unknowns, and knowledge snapshots.
- **Praxis** records reusable Capability/Protocol identity, versions, requirements, and methodological semantics.
- **MolSysSuite** records scientific execution and produced Results/Artifacts.
- **Nextia** records DiscoveryProject meaning: Questions, Hypotheses, Campaigns, Observations, Evidence, Decisions, Conclusions.
- **MOLI Agent** records scientifically relevant proposals, explicit rationales, context identities, and tool actions.
- **Humans** record consequential approvals/decisions where required.

These distributed records form the authoritative **Scientific Record**. MOLI/LLMs later read and communicate it; they do not reconstruct it from chat history.

## KnowledgeSnapshot

A consequential decision should reference the knowledge state available when it was made.

A `KnowledgeSnapshot` may reference Sabueso Cards, Decks, Relationships, SourceAssertions, conflicts, unknowns, source versions/retrieval dates, and content identities/hashes.

It need not duplicate an entire store. It may be a manifest of immutable/versioned references.

Its question is:

> **What did MOLI/the scientists know when this decision was made?**

## DecisionRecord

A consequential Decision should persist:

- decision and timestamp/state;
- proposer;
- approver/authority when applicable;
- alternatives considered;
- selected alternative;
- explicit human-auditable rationale;
- supporting and contradicting Evidence;
- KnowledgeSnapshot / ProjectState;
- ContextAssembly when an agent participated.

Private chain-of-thought is not the scientific record. An explicit rationale sufficient for audit is.

## ExecutionPlan

A Decision such as “run dynamics” is not reproducible. It must become a deterministic-enough execution specification.

    Decision
        ↓
    ExecutionPlan
        ├── Capability
        ├── Protocol
        ├── inputs
        ├── parameters
        ├── software/environment requirements
        ├── random seeds
        ├── resource requirements
        └── expected outputs
        ↓
       Run

The `ExecutionPlan` is the **frozen executable intent** between scientific decision and execution. The name is provisional; the concept is required.

## RunRecord

A Run records what actually happened, including:

- referenced ExecutionPlan;
- start/end;
- executor;
- machine/environment;
- actual software versions;
- actual inputs/parameters;
- commands/API invocations;
- exit status;
- logs;
- produced Results/Artifacts.

Actual execution may differ from the plan through failures, retries, environment resolution, or explicitly recorded amendments; those differences must remain visible.

## Commands and API invocations

Scientifically consequential operations must be reproducible beyond prose.

For CLI execution preserve command, arguments, working directory, relevant non-secret configuration, and executable/version identity.

For API execution preserve equivalent serialized invocation: callable/Capability identity, arguments, referenced inputs, and implementation/version identity.

For notebooks preserve at least notebook content/version/hash, environment, referenced inputs, and executed scientific operations/results.

MOLI need not record every human keystroke; it must record every operation needed to reconstruct consequential computation.

## EnvironmentManifest

A Run should reference enough environment information to reconstruct execution when feasible:

- Python/packages/Git SHAs;
- OS/architecture;
- external scientific engines;
- CUDA/GPU/driver when relevant;
- container image/digest;
- Conda/environment lock;
- relevant non-secret configuration.

**Secrets must never be stored.** The record may state that a credential was required without storing its value.

## InputManifest and transformation lineage

An identifier alone may not be a reproducible input. Preserve content identity, retrieval context, and hashes where appropriate.

Transformations must remain traceable:

    raw structure
        ↓
    normalization
        ↓
    repair
        ↓
    protonation
        ↓
    model/simulation system

Each meaningful transformation references input, operation/Protocol, parameters, and output.

## Result and Artifact

A Run may produce both.

**Artifacts** are files/data objects such as trajectories, structures, tables, plots, pocket files, or viewer scenes. Preserve content hash, format, size/location, creating Run, and semantic role as appropriate.

**Results** are structured scientific outputs such as pocket populations, RMSD, scores, confidence intervals, or other measurements.

Do not collapse Result and Artifact merely because both originate from the same Run.

## Observation

A Result is not automatically an Observation.

An Observation is an interpretation of Results and should reference its source Results/Artifacts, proposer, review/acceptance state, and relevant context.

This preserves the boundary between computation and interpretation.

## Evidence

Evidence records how an admissible project object — commonly an Observation — bears on a Question/Hypothesis, including supports/contradicts/informs semantics, context, and limitations.

A SourceAssertion does not become Evidence merely because it exists; project interpretation establishes the relationship.

## Conclusion

Important Conclusions should be persistent objects rather than prose existing only in a final report.

A Conclusion may reference supporting and contradicting Evidence, scope, uncertainty/limitations, and approval state.

It should be possible to trace a Conclusion back through Evidence, Observations, Results, Runs, ExecutionPlans, Protocols, inputs, and relevant SourceAssertions.

## AgentActionRecord

Scientifically relevant agent behavior should record:

- MOLI Agent version;
- model/provider/version when available;
- ContextAssembly identity;
- available tool/Capability registry snapshot;
- requested action;
- proposal and explicit rationale;
- tools invoked and outputs;
- resulting Decision;
- approval requirement/outcome.

Operational transcripts may be retained according to policy, but reproducibility must not depend on obtaining identical model text.

## HumanAction / ApprovalRecord

Human intervention is scientific provenance.

Record authorized actor, action/approval, referenced object/version/hash, timestamp, and optional rationale/comment for consequential approvals.

## ContextAssembly

When MOLI Agent participates, preserve the identity of the context supplied to it:

- Sabueso KnowledgeSnapshot;
- applicable Praxis Capability/Protocol snapshot;
- Nextia ProjectState;
- relevant MolSysSuite state/Results;
- selection policy;
- assembly time/version.

The goal is not to make a future LLM answer identically. It is to know **what information the original agent had available**.


## ProjectStateSnapshot

At meaningful boundaries, a DiscoveryProject should expose an immutable/versioned state snapshot referencing, as applicable:

- KnowledgeSnapshot;
- Questions, Hypotheses, Strategies, Campaigns;
- Decisions and approvals;
- ExecutionPlans and Runs;
- Results and Artifacts;
- Observations, Evidence, Conclusions;
- Candidates;
- relevant AgentActions.

Snapshots support historical inspection and state diffs such as `PS17 → PS18`, which can also ground ProgressBrief generation.

## Append-only EventLedger

Beneath mutable/current views, MOLI should preserve an append-only or equivalently immutable history of consequential events, for example:

    CardCreated
    SourceAssertionAdded
    HypothesisCreated
    DecisionProposed
    DecisionApproved
    ExecutionPlanFrozen
    RunStarted
    RunCompleted
    ResultCreated
    ObservationRecorded
    EvidenceLinked
    ConclusionApproved

Objects may acquire new states; meaningful historical sequence must not be silently rewritten.

The exact event-sourcing implementation is open. The invariant is reconstructable history.

## ProjectManifest

A completed or snapshotted project should expose a manifest/index describing its reproducible scientific record.

Conceptually it references:

- project identity and MOLI architecture/schema versions;
- KnowledgeSnapshots;
- Questions/Hypotheses;
- Decisions/approvals;
- ExecutionPlans/Runs;
- Capability/Protocol versions;
- environments and inputs;
- Results/Artifacts;
- Observations/Evidence/Conclusions;
- AgentActions/HumanActions;
- ProjectStateSnapshots;
- timeline/EventLedger;
- communication artifacts.

The manifest need not embed all data. It may index immutable/content-addressed objects owned by their proper components.

The name and exact serialization remain open.

## IntegrityManifest

Names and paths are insufficient to prove identity.

Where practical use cryptographic content hashes or equivalent immutable identities for external input snapshots, transformed inputs, Protocol definitions, ExecutionPlans, environments/containers, code snapshots, Artifacts, and important manifests.

Audit should answer:

> **Is this actually the object that was used?**

not merely whether a similarly named file still exists.

## Audit, Trace, Replay, and Rerun are different

### Audit

`project.audit()`

Question:

> What happened, in what order, under whose authority, and why?

Audit executes nothing.

### Trace

`project.trace(conclusion)`

Question:

> Why do we believe this specific statement?

Conceptually:

    Conclusion
        ↑
    Evidence
        ↑
    Observation
        ↑
    Result
        ↑
    Run
        ↑
    ExecutionPlan
        ↑
    Protocol / Capability
        ↑
    Inputs / SourceAssertions

### Replay

`project.replay()`

Question:

> Can we execute the recorded historical trajectory again?

Replay uses recorded Decisions, ExecutionPlans, inputs, versions, environments, and seeds.

**Replay must not require an LLM or agent to reason again.**

### Rerun

`project.rerun()`

Question:

> If MOLI investigates this starting state again, what trajectory does it choose now?

Rerun invokes new agent/scientific decision-making and may produce a different path.

> **Replay reproduces an executed scientific trajectory; rerun creates a new discovery trajectory.**

## Replay granularity

A project is graph-shaped. Future replay may target:

- a single Run;
- an ExecutionPlan;
- a Campaign;
- a project branch;
- the complete recorded computational trajectory.

Trace should likewise work from an individual Conclusion, Evidence item, Result, or Artifact.

## Verification of reproduction

Reproducibility does not always mean bitwise-identical output.

Useful verification categories are:

- **Recorded** — complete historical specification/provenance is available.
- **Executable** — the recorded computation can be reconstructed and launched.
- **Computationally reproducible** — outputs reproduce exactly or within method-appropriate numerical/statistical tolerances.
- **Scientifically reproducible** — the scientifically relevant interpretation remains supported under defined reproduction criteria.

These are verification categories, not platform scores.

For stochastic simulations, meaningful distributional equivalence may matter more than an identical trajectory.



## Execution lifecycle, failures, cancellations, and retries

An ExecutionPlan and a Run must not imply successful completion.

The scientific record should distinguish states such as:

    ExecutionPlan
        ├── planned / frozen
        ├── never started
        └── attempted
              ├── failed
              ├── cancelled
              ├── partial
              └── completed

Retries must remain separate historical executions rather than overwriting failed attempts:

    EP17
      ├── Run17a — failed
      ├── Run17b — failed
      └── Run17c — completed

Failure, cancellation, partial output, and retry history may themselves be scientifically or operationally informative.

## Immutable amendments

Frozen executable intent must not be silently edited after approval or execution begins.

When a scientifically meaningful change is required, preserve the previous plan and create explicit amendment provenance or a new version/plan:

    EP17 — frozen
       ↓
    Amendment A1
       rationale / actor / approval
       ↓
    EP18
       ↓
    Run

> **Frozen execution intent is immutable; changes create new provenance.**

The exact amendment/versioning mechanism remains open.

## Manual scientific actions, observations, and curation

Not all consequential scientific work occurs through an API.

Human inspection, manual curation, exclusion, annotation, or interpretation must be representable when it affects project state.

Examples include:

- a scientist rejecting a pocket as likely crystal-packing artifact after visual inspection;
- manual reconciliation of an ambiguous molecular identity;
- human curation of a literature statement;
- manual annotation of a structure or experimental condition.

The record should preserve actor, timestamp, inspected/referenced objects, statement/action, rationale, and resulting project relationship as appropriate.

Manual work must not become invisible merely because it is not computationally replayable.

## Selection and exclusion provenance

Selection of data is itself a scientific decision.

If 17 structures are available and 4 are used, the record should preserve the candidate set, selected set, excluded set, criteria, rationale, actor/process, and relevant state.

The same applies to:

- structures;
- ligands;
- papers;
- trajectories;
- replicates;
- outliers;
- Candidates;
- training/reference subsets;
- any other scientifically consequential filtering.

A final input set without its selection history is incomplete provenance.

## General data lineage

Transformation lineage applies to all scientific data, not only molecular structures.

Derived datasets, Decks/cohorts, rankings, clusters, vulnerability families, statistical summaries, and other aggregate objects should preserve their dependency graph:

    A + B + C
        ↓
      filter
        ↓
     normalize
        ↓
     aggregate
        ↓
     Result X

Where derived knowledge is produced, lineage should connect the derivation to its inputs, operation, parameters, software/version, and underlying SourceAssertions/Results as appropriate.

## Predeclared acceptance and decision criteria

When scientific criteria can be specified before observing an outcome, their identity and temporal ordering should be preserved.

Examples may include convergence requirements, replicate counts, statistical tolerances, pocket-population criteria, selectivity gates, or stopping rules.

The record should make it possible to distinguish:

    criterion defined before result

from:

    criterion introduced after inspecting result

Not every exploratory analysis requires predeclared thresholds. The requirement is to preserve predeclaration when it exists and avoid retrospective ambiguity.

## External services and mutable sources

External scientific services and databases may change or disappear.

For an external retrieval or computation, preserve as applicable:

- service/source identity;
- endpoint/tool identity;
- version/release when available;
- query/request identity;
- retrieval/execution timestamp;
- returned content or materialized snapshot when legally/technically allowed;
- content hash;
- licensing/retention constraint when the response cannot be preserved.

A reference such as “ChEMBL record X” is weaker than preserving the actual content state used by the project.

When content cannot be retained, the manifest should say so explicitly rather than implying full replayability.

## Artifact availability and retention

Integrity and availability are different.

A content hash can prove identity but cannot replay a project if the referenced data no longer exist.

Artifacts and inputs should therefore be able to expose, where relevant:

- content identity/hash;
- current storage location/reference;
- availability state;
- archival state;
- retention policy;
- reconstructability;
- reason for non-retention.

For example:

    Artifact A17
    hash: ...
    storage: cold archive
    retention: ...
    reconstructable: yes

or:

    raw trajectory
    retained: no
    reconstructable_from:
        ExecutionPlan + inputs + environment + seeds

Large scientific data may require explicit retention tradeoffs. The project record must make those tradeoffs visible.

## ReplayPreflight

Before replay, MOLI should be able to assess whether the recorded trajectory is currently executable.

Conceptually:

    ReplayPreflight

    inputs available                 ✓
    environment reconstructable      ✓
    Protocol available               ✓
    external engine available        ✗
    required license available       ✗
    archived Artifact available      ✓

Preflight does not change the historical record. It reports present-day replay feasibility and blockers.

## Historical replay and migrated replay

Exact historical software stacks may eventually become unavailable or impractical.

Distinguish:

### Historical replay

Attempts to reconstruct the original implementation/environment as faithfully as possible.

### Migrated replay

Executes the same scientific intent using an explicitly substituted compatible implementation/environment.

A migrated replay must record the substitution, rationale, compatibility claim, and verification criteria. It must never be presented as an exact historical replay.

## ReplayComparisonRecord

A replay should itself produce provenance.

Conceptually:

    ReplayComparison

    original_run:
        R17

    replay_run:
        RR17

    comparison:
        exact
        numerical tolerance
        statistical equivalence
        scientifically equivalent
        divergent

    criteria:
        ...

    result / limitations:
        ...

This makes reproducibility claims auditable rather than anecdotal.

## Project release / frozen scientific record

A live DiscoveryProject evolves. Publications, regulatory-like records, collaborations, or long-term audit may need a frozen project state.

A future `ProjectRelease` or equivalent concept may bind:

- project identity;
- release/version;
- ProjectManifest;
- IntegrityManifest;
- ProjectStateSnapshot;
- closure/release timestamp;
- responsible authority;
- communication/publication references.

Conceptually:

    live DiscoveryProject
           ↓
    ProjectRelease TcTIM-1.0
           ↓
    paper / report / archive

A later project release may contain additional knowledge without rewriting what release 1.0 contained.

## Four audit questions

A complete project record should be able to answer:

### WHAT?

What happened?

### WHY?

Why was this path chosen and how were Results interpreted?

### WITH WHAT?

With exactly what knowledge, data, code, software, environment, parameters, seeds, and resources did it happen?

### WHO OR WHAT AUTHORIZED IT?

Who/what proposed, approved, executed, reviewed, or changed each consequential step?


## Scientific Communication consumes the record

ProjectBriefings, ProgressBriefs, ProjectReports, slides, web reports, and videos should derive from the structured Scientific Record.

    ProjectManifest
          +
    ProjectStateSnapshot
          +
    scientific object graph
          +
    Results / Artifacts
             ↓
            MOLI
             ↓
         LLM / renderer
             ↓
    ScientificCommunicationArtifact
             ↓
       PDF / HTML / Slides / Video

Communication is a derived view.

If a report contains a narrative error, correct the report; do not rewrite scientific history to match it.

## Claims in reports should be traceable

Where feasible, substantive report claims should reference the scientific objects supporting them:

    report claim
         ↓
    Conclusion
         ↓
      Evidence
         ↓
    Observation
         ↓
       Result
         ↓
        Run

Reports may cite Sabueso SourceAssertions directly when communicating external knowledge rather than project conclusions.

## LLM independence

If all LLM services disappeared after project completion, MOLI should still retain:

- Questions and Hypotheses;
- Decisions and explicit rationales;
- alternatives and approvals;
- ExecutionPlans;
- commands/API invocations;
- inputs and transformations;
- Protocol/Capability identities;
- software/environment versions;
- seeds;
- Runs and logs;
- Results and Artifacts;
- Observations;
- Evidence;
- Conclusions;
- Knowledge/Project snapshots;
- integrity hashes;
- event history.

The project remains auditable and its recorded computational work remains replayable to the extent allowed by preserved software/data/resources.

A different future LLM may generate a new narrative from the same Scientific Record without becoming a dependency of the science.

## Relationship to Phase 1 and Phase 2 pilots

The provenance model should be the same regardless of who orchestrates the work.

### Phase 1

    Human
       ↓
    Decision
       ↓
    ExecutionPlan
       ↓
    Run

### Phase 2

    MOLI Agent
       ↓ proposes
    Decision
       ↓ approved as required
    ExecutionPlan
       ↓
    Run

After the Decision is materialized, the reproducible execution path is the same kind of platform record.

This is essential: agentic automation changes who proposes/orchestrates scientific work, not the provenance standard.

## Ownership summary

The design should preserve distributed semantic ownership:

- Sabueso owns external knowledge objects and knowledge snapshots.
- Praxis owns reusable methodological semantics.
- MolSysSuite components own their execution-specific Results/Artifacts and local provenance.
- Nextia owns DiscoveryProject interpretation/history and stable references connecting those objects.
- MOLI Agent owns its action/proposal records.
- humans/policy authority own recorded approvals where applicable.
- MOLI composes cross-platform manifests/views and scientific communication.

Nextia may act as the central Discovery graph/ledger without copying all underlying objects.

## Design constraint

The Scientific Record must not be a chat transcript.

Conversation may be useful operational context, but the authoritative project history consists of structured platform objects and their immutable/versioned relationships.

## Concepts to formalize before implementation

This document identifies several concepts whose exact representation still requires design:

- ExecutionPlan / RunManifest boundary;
- DecisionRecord richness and approval semantics;
- KnowledgeSnapshot;
- ContextAssembly identity;
- AgentActionRecord;
- HumanAction / ApprovalRecord;
- ProjectStateSnapshot;
- EventLedger;
- ProjectManifest;
- IntegrityManifest;
- replay verification criteria;
- execution lifecycle and retry semantics;
- immutable amendment/versioning semantics;
- manual scientific action/curation provenance;
- selection/exclusion provenance;
- general data-lineage representation;
- predeclared acceptance-criteria representation;
- external-service snapshot/retention semantics;
- Artifact availability/retention policy;
- ReplayPreflight;
- historical versus migrated replay;
- ReplayComparisonRecord;
- ProjectRelease / frozen-record semantics.

Not every concept must become an independent Python class. Some may be manifests, events, views, or cross-component references.

The requirement is semantic coverage, not class proliferation.

## Guiding principles

> **Agent reasoning may choose a scientific path, but once a path is chosen, the chosen decision, execution plan, inputs, parameters, environment, outputs, observations, evidence, and subsequent decisions must become persistent platform objects. Reproducing the historical path must not require the agent to reason again.**

> **Replay reproduces an executed scientific trajectory; rerun creates a new discovery trajectory. They are not the same operation.**

> **Components record; Nextia connects; MOLI explains.**

> **The science must survive the disappearance of the LLM that helped produce it.**
