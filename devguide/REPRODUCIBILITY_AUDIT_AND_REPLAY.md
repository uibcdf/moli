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
