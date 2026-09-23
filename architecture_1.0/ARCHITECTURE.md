# Platform Architecture

## Structural view

```text
                         MOLI PLATFORM

                     ┌────────────────┐
                     │   MOLI Agent   │
                     │ scientific     │
                     │ reasoning /    │
                     │ agency         │
                     └───────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼

       SCIENTIFIC CONTEXT  ◄──────────►  MolSysSuite
              │                       molecular modeling
      ┌───────┼───────┐                     │
      ▼       ▼       ▼                 MolSys-AI
   Sabueso  Praxis  Nextia          specialist agent
  Knowledge Know-how Discovery
```

A human scientist can operate Scientific Context and MolSysSuite directly. MOLI Agent and MolSys-AI are optional.

Scientific Context groups Sabueso, Praxis, and Nextia conceptually; it need not be a monolithic package. MolSysSuite is the molecular modeling ecosystem. MolSys-AI is its specialized software/modeling agent and is distinct from MOLI Agent.

## Interoperability

Ownership does not imply isolation. MolSysSuite components may consume Sabueso knowledge; Praxis Protocols may orchestrate MolSysSuite components; MolSysSuite Results may update Nextia projects. Conceptual bidirectionality does not require circular package dependencies.

MOLI may assemble Scientific Context, invoke Praxis/DiscoveryEngine, delegate modeling tasks to MolSys-AI, or access MolSysSuite/external APIs directly.

## Molecular Intelligence

`Scientific Context + Molecular Modeling + Scientific Reasoning → Molecular Intelligence`

## Dynamic view

```text
KNOW → MODEL → DO → DISCOVER → LEARN
 ▲                              │
 └──────────────────────────────┘
```

`LEARN` represents controlled accumulation of project experience, curated knowledge, and validated know-how.
