# MolI

[![Governance tests](https://github.com/uibcdf/moli/actions/workflows/validate_governance.yml/badge.svg?branch=main)](https://github.com/uibcdf/moli/actions/workflows/validate_governance.yml)
[![Codecov](https://codecov.io/gh/uibcdf/moli/branch/main/graph/badge.svg)](https://app.codecov.io/gh/uibcdf/moli)

**MolI is the Molecular Intelligence platform. Moli is its scientific agent.**

The name **MolI** combines **Mol** from Molecular and **I** from Intelligence.
**Moli** is the proper name of the platform's optional scientific agent. See the
[naming policy](devguide/policies/naming_policy.md) for the conceptual basis and
standard spelling.

The coverage badge measures `devtools/scripts` with MolI's governance tests on
pushes to `main`. It describes that administrative test selection, not scientific
coverage across the platform.

Molecular Intelligence emerges from combining **scientific context**, **molecular modeling**, and **scientific reasoning** to understand, investigate, learn about, and create molecular systems.

Human scientists can operate MolI's scientific infrastructure directly to perform reproducible science. **Moli** may augment reasoning and agency where useful; the platform can operate without an LLM or AI agent.

The platform is designed to be **local-first and remote-ready**: scientific semantics remain independent of deployment topology so the same architecture can evolve from local workflows to shared, distributed, or hybrid infrastructure.

## Platform composition

```text
                         MolI
                    platform / umbrella
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Scientific Context     MolSysSuite           Moli
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

**[MolSysSuite](https://github.com/uibcdf/molsyssuite)** is MolI's molecular modeling ecosystem. Its components provide molecular-system representation, interoperability, computation, simulation, analysis, and visualization.

MolSysSuite is a first-class MolI component with its own delegated internal governance. MolI governs MolSysSuite at the platform boundary; MolSysSuite governs its internal components and shared modeling-ecosystem policies.

**MolSys-AI** belongs to the MolSysSuite domain as the AI subsystem specialized in understanding and operating MolSysSuite.

### Moli

**[Moli](https://github.com/uibcdf/moli-agent)** is MolI's optional scientific reasoning and agency component operating across Scientific Context and MolSysSuite.

It may help interpret scientific intent, assemble relevant context, reason over DiscoveryProjects, use methodological Capabilities, delegate modeling-specialist work to MolSys-AI Agent, invoke authorized scientific tools, and interpret results while preserving explicit authority and approval boundaries.

Moli is an agent within the MolI platform.

## Architectural interaction

Composition does not imply isolation. Scientific Context and MolSysSuite may interoperate directly where appropriate, while Moli may reason and act across both.

```text
                        Moli
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

MolI can be understood through three compatible architectural views:

- **Structural:** Scientific Context ↔ MolSysSuite, with optional Moli across both.
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

## Scientific communication

MolI may eventually compose the scientific state held across Sabueso, Praxis, Nextia, and MolSysSuite into traceable **ProjectBriefings**, **ProgressBriefs**, and **ProjectReports**. These structured communication artifacts may then be rendered as written dossiers, interactive reports, slides, or narrated video while preserving provenance, uncertainty, confidentiality, and the ownership of the underlying scientific objects.

See [`devguide/SCIENTIFIC_COMMUNICATION.md`](devguide/SCIENTIFIC_COMMUNICATION.md).

## Architecture 1.0

The frozen conceptual baseline is documented in [`architecture_1.0/`](architecture_1.0/README.md).

It defines component boundaries, Scientific Context Assembly, the learning loop, epistemic distinctions, agent specialization, object identity and portability, visibility/confidentiality, deployment independence, examples, diagrams, and scientific/operational stress tests.

Architecture and implementation evolve at different rates: implementation repositories may mature without silently changing the frozen conceptual meanings.

## Governance

This repository coordinates governance and platform-level contracts for MolI.

- [`moli.toml`](moli.toml) is the machine-readable registry of MolI components and governance relationships.
- [`MOLI_GUIDE.md`](MOLI_GUIDE.md) is the concise component-facing governance guide.
- [`devguide/`](devguide/README.md) contains durable governance and development knowledge.
- [`devguide/CHECKPOINT.md`](devguide/CHECKPOINT.md) is the dated pause and resumption checkpoint; verify live issues before acting on it.
- [`devguide/INFRASTRUCTURE_CENSUS.md`](devguide/INFRASTRUCTURE_CENSUS.md) records observed implementation maturity and pending platform infrastructure.
- [MolI Development Observatory](https://github.com/uibcdf/moli-dev-observatory) provides the platform's development-health dashboards from the authoritative registries.
- [`devguide/governance/policy_inheritance.md`](devguide/governance/policy_inheritance.md) defines how delegated ecosystems inherit MolI engineering policy.

The governing rule is:

> **A concern is governed at the lowest level that owns the shared contract it affects.**

Sabueso, Praxis, Nextia, and Moli are directly coordinated through MolI for shared platform contracts. MolSysSuite is also a MolI component, while governance of its internal ecosystem is delegated to the MolSysSuite repository.

## Repositories

```text
MolI
├── uibcdf/moli
├── uibcdf/sabueso
├── uibcdf/praxis
├── uibcdf/nextia
├── uibcdf/moli-agent
└── uibcdf/molsyssuite
      └── modeling components and MolSys-AI
```

Real discovery programs may remain private while using the public MolI infrastructure. Open-source software does not imply publication of DiscoveryProjects, proprietary Know-how, Evidence, Candidates, or molecular assets.
