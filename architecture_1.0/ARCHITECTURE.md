# Platform Architecture

```text
                         MOLI PLATFORM

                     ┌────────────────┐
                     │   MOLI Agent   │
                     │ optional       │
                     │ reasoning/     │
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

A human scientist can operate Scientific Context and MolSysSuite directly.

`Scientific Context` is a conceptual grouping, not necessarily a monolithic package.

## Interoperability
Ownership does not imply isolation. MolSysMT may consume Sabueso Cards/entity information; TopoMT may use Sabueso annotations; Praxis Protocols may orchestrate MolSysSuite components; MolSysSuite Results may update Nextia projects.

Conceptual bidirectionality does not require circular code dependencies. Prefer stable interfaces/adapters.

## Molecular Intelligence
Molecular Intelligence is an emergent capability:
`Scientific Context + Molecular Modeling + Scientific Reasoning → Molecular Intelligence`.
