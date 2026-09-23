# MOLI

**MOLI is a platform for Molecular Intelligence.**

Molecular Intelligence emerges from combining **scientific context**, **molecular modeling**, and **scientific reasoning** to understand, investigate, learn about, and create molecular systems.

MOLI is not an LLM and does not require an AI agent to perform reproducible science. Human scientists can operate the same scientific infrastructure directly, while **MOLI Agent** may augment reasoning and agency where useful.

The platform is designed to be **local-first and remote-ready**: scientific semantics remain independent of deployment topology so the same architecture can evolve from local workflows to shared, distributed, or hybrid infrastructure.

## Platform composition

```text
                         MOLI
                    platform / umbrella
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Scientific Context     MolSysSuite        MOLI Agent
        │                  │
   ┌────┼────┐             ├── MolSysMT
   ▼    ▼    ▼             ├── MolSysViewer
Sabueso Praxis Nextia      ├── TopoMT
                           ├── ...
                           └── MolSys-AI
```

The diagram shows **composition**, not mandatory execution flow.

### Scientific Context

Scientific Context is the conceptual grouping of three complementary forms of persistent scientific context:

- **[Sabueso](https://github.com/uibcdf/sabueso) — Knowledge:** what is known about molecular entities, systems, properties, relationships, and observations, preserving traceable source assertions.
- **[Praxis](https://github.com/uibcdf/praxis) — Know-how:** what scientific tasks we know how to perform reproducibly, through reusable Capabilities and Protocols.
- **[Nextia](https://github.com/uibcdf/nextia) — Discovery:** what we are trying to discover, what we have tried, observed, learned, rejected, and decided.

Scientific Context is an architectural concept, not a requirement for a separate package or governance repository.

### MolSysSuite

**[MolSysSuite](https://github.com/uibcdf/molsyssuite)** is MOLI's molecular modeling ecosystem. Its components provide molecular-system representation, interoperability, computation, simulation, analysis, and visualization.

MolSysSuite is a first-class MOLI component with its own delegated internal governance. MOLI governs MolSysSuite at the platform boundary; MolSysSuite governs its internal components and shared modeling-ecosystem policies.

**MolSys-AI** belongs to the MolSysSuite domain as the AI subsystem specialized in understanding and operating MolSysSuite.

### MOLI Agent

**[MOLI Agent](https://github.com/uibcdf/moli-agent)** is the optional scientific reasoning and agency component operating across Scientific Context and MolSysSuite.

It may help interpret scientific intent, assemble relevant context, reason over DiscoveryProjects, use methodological Capabilities, delegate modeling-specialist work to MolSys-AI Agent, invoke authorized scientific tools, and interpret results while preserving explicit authority and approval boundaries.

MOLI Agent is not the MOLI platform itself.

## Architectural interaction

Composition does not imply isolation. Scientific Context and MolSysSuite may interoperate directly where appropriate, while MOLI Agent may reason and act across both.

```text
                     MOLI Agent
                         │
                  reasoning / agency
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
     Scientific Context  ◄──────►  MolSysSuite
             │
        ┌────┼────┐
        ▼    ▼    ▼
     Sabueso Praxis Nextia
```

Ownership of a scientific concept does not imply isolation, and conceptual interoperability does not require circular package dependencies.

## Three complementary views

MOLI can be understood through three compatible architectural views:

- **Structural:** Scientific Context ↔ MolSysSuite, with optional MOLI Agent across both.
- **Functional:** Knowledge | Modeling | Capabilities | Discovery.
- **Dynamic:** KNOW → MODEL → DO → DISCOVER → LEARN → KNOW.

```text
Knowledge     Modeling      Capabilities     Discovery
   │             │               │               │
Sabueso      MolSysSuite        Praxis          Nextia
```

The dynamic view makes learning explicit: discovery experience may improve Knowledge and Know-how through controlled curation and validation. **Promotion does not imply publication.**

## Molecular Intelligence

Molecular Intelligence is a property of the integrated scientific system, not the name of a subsystem and not a synonym for AI:

> **Molecular Intelligence = Scientific Context + Molecular Modeling + Scientific Reasoning**

Reasoning may be human, agent-assisted, or a combination of both.

## Architecture 1.0

The frozen conceptual baseline is documented in [`architecture_1.0/`](architecture_1.0/README.md).

It defines component boundaries, Scientific Context Assembly, the learning loop, epistemic distinctions, agent specialization, object identity and portability, visibility/confidentiality, deployment independence, examples, diagrams, and scientific/operational stress tests.

Architecture and implementation evolve at different rates: implementation repositories may mature without silently changing the frozen conceptual meanings.

## Governance

MOLI also acts as the governance and coordination repository for platform-level contracts.

- [`moli.toml`](moli.toml) is the machine-readable registry of MOLI components and governance relationships.
- [`MOLI_GUIDE.md`](MOLI_GUIDE.md) is the concise component-facing governance guide.
- [`devguide/`](devguide/README.md) contains durable governance and development knowledge.

The governing rule is:

> **A concern is governed at the lowest level that owns the shared contract it affects.**

Sabueso, Praxis, Nextia, and MOLI Agent are directly coordinated through MOLI for shared platform contracts. MolSysSuite is also a MOLI component, while governance of its internal ecosystem is delegated to the MolSysSuite repository.

## Repositories

```text
MOLI
├── uibcdf/moli
├── uibcdf/sabueso
├── uibcdf/praxis
├── uibcdf/nextia
├── uibcdf/moli-agent
└── uibcdf/molsyssuite
      └── modeling components and MolSys-AI
```

Real discovery programs may remain private while using the public MOLI infrastructure. Open-source software does not imply publication of DiscoveryProjects, proprietary Know-how, Evidence, Candidates, or molecular assets.
