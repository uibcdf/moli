# Scientific Context Assembly

MOLI Agent should not be understood as a conventional chatbot whose scientific context is assembled only by retrieving documents into a prompt.

```text
documents → retrieval / RAG → prompt → LLM
```

MOLI can instead assemble **structured Scientific Context**:

```text
                    SCIENTIFIC CONTEXT
          Knowledge     Methodology      Discovery
              │             │               │
           Sabueso        Praxis          Nextia
              └─────────────┼───────────────┘
                            ▼
                     Context Assembly
                            │
                            ▼
                        MOLI Agent
```

## Context sources

**Sabueso** may contribute resolved knowledge, SourceAssertions, provenance, conflicts, uncertainty, entity relationships, and versioned external knowledge.

**Praxis** may contribute Capabilities, Protocols, applicability, validation status, limitations, and resource/fidelity characteristics.

**Nextia** may contribute Focus, Goal, Questions, Hypotheses, Strategies, Campaigns, previous Runs/failures, Results, Observations, Evidence, Candidates, Decisions, and relevant history.

## Context Assembly is not just retrieval

`Context Assembly ≠ document retrieval`.

RAG remains useful for unstructured information and especially for software documentation, but MOLI's scientific context should preserve semantics, identities, provenance, conflicts, validation status, and project relationships. Context may be selected, summarized, ranked, or compressed while preserving references to authoritative objects.

## Relationship with MolSys-AI

MolSys-AI may use RAG over MolSysSuite documentation, APIs, tutorials, examples, devguides, tool schemas, and source context to understand and operate MolSysSuite.

MOLI uses Scientific Context Assembly to reason about the scientific investigation. It may delegate MolSysSuite-specialist tasks to MolSys-AI, invoke Praxis/DiscoveryEngine, or access modeling APIs directly.

> **MolSys-AI knows how to use MolSysSuite. MOLI reasons about why, when, and what for.**
