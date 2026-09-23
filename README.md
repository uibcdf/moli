# MOLI

**MOLI is a platform for Molecular Intelligence.**

Molecular Intelligence emerges from combining **structured scientific context**, **molecular modeling**, and **scientific reasoning** to understand, investigate, learn about, and create molecular systems.

Scientific reasoning may be performed by human scientists alone or augmented by **MOLI Agent**. The scientific platform is therefore not dependent on an LLM or any particular AI technology.

MOLI is designed to be **local-first and remote-ready**: its scientific semantics are independent of deployment topology, allowing the same architecture to evolve from local scientific workflows to shared, distributed, or hybrid infrastructure.

## Architecture

```text
                         MOLI PLATFORM

                     ┌────────────────┐
                     │   MOLI Agent   │
                     │ optional       │
                     │ reasoning /    │
                     │ agency         │
                     └───────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼

       SCIENTIFIC CONTEXT  ◄──────────►  MolSysSuite
              │                       molecular modeling
      ┌───────┼───────┐
      ▼       ▼       ▼
   Sabueso  Praxis  Nextia
  Knowledge Know-how Discovery
```

### Scientific Context

Scientific Context brings together three complementary forms of persistent context:

- **Sabueso — Knowledge:** what is known about molecular entities, systems, properties, relationships, and observations, with traceable source assertions.
- **Praxis — Know-how:** what scientific tasks we know how to perform reproducibly, through reusable Capabilities and Protocols.
- **Nextia — Discovery:** what we are trying to discover, what we have tried, observed, learned, rejected, and decided.

### MolSysSuite

**MolSysSuite** is the molecular modeling ecosystem. It provides molecular-system representation, interoperability, computation, simulation, analysis, and visualization through components such as MolSysMT, MolSysViewer, TopoMT, ElastNetMT, PharmacophoreMT, and DockingMT.

Scientific Context and MolSysSuite are designed to interoperate directly where appropriate. Ownership of a scientific concept does not imply isolation, and conceptual interoperability does not require circular package dependencies.

### MOLI Agent

MOLI Agent is the optional scientist-facing reasoning and agency layer operating across Scientific Context and MolSysSuite. It can help interpret scientific intent, query knowledge, reason over discovery projects, use validated methodological capabilities, invoke modeling tools, and interpret results while preserving explicit authority and approval boundaries.

## Three complementary views

The platform can be understood through three compatible views:

- **Structural:** Scientific Context ↔ MolSysSuite, with optional MOLI Agent across both.
- **Functional:** Knowledge | Modeling | Capabilities | Discovery.
- **Dynamic:** KNOW → MODEL → DO → DISCOVER → LEARN.

These views describe organization, scientific responsibility, and learning over time respectively.

## Architecture 1.0

The frozen conceptual baseline, including design principles, component boundaries, schemas, examples, diagrams, scientific stress tests, and operational/epistemic stress tests, is documented in [`architecture_1.0/`](architecture_1.0/README.md).

Architecture 1.0 also defines Scientific Context Assembly, the learning loop, agent specialization, stable object identity and portability, and a deployment-independent path from local workflows to remote and distributed infrastructure.

## Ecosystem

Current related projects include:

- [MolSysSuite](https://github.com/uibcdf/molsyssuite) — molecular modeling ecosystem.
- [Sabueso](https://github.com/uibcdf/sabueso) — structured molecular knowledge context.

Praxis, Nextia, and MOLI Agent are defined by Architecture 1.0; their implementation status and repository boundaries will evolve independently from the frozen conceptual architecture.

---

**Molecular Intelligence = Scientific Context + Molecular Modeling + Scientific Reasoning**
