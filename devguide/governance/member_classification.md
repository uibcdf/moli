# Governance Classification

MOLI components may differ in how their internal governance is organized.

## Direct components without delegated internal ecosystem governance

- Sabueso — Knowledge context.
- Praxis — Methodological / Know-how context.
- Nextia — Discovery context.
- MOLI Agent — scientific reasoning/agency.

Their cross-component/platform contracts are governed directly by MOLI; their local implementation remains locally owned.

## Component with delegated internal governance

- **MolSysSuite** — molecular modeling ecosystem.

MolSysSuite is a first-class MOLI component. MOLI governs its platform-level relationship with Sabueso, Praxis, Nextia, MOLI Agent, and other future MOLI components. Because its internal governance is delegated, MolSysSuite is **not** a consumer of the vendored `MOLI_GUIDE.md`; its root governance documents reference MOLI directly and it distributes `MOLSYSSUITE_GUIDE.md` to its own members.

MolSysSuite delegates governance of its internal members and shared modeling-ecosystem policies to `uibcdf/molsyssuite`.

This is hierarchical governance, not exclusion from MOLI membership.

## Conceptual groupings

Scientific Context groups Sabueso, Praxis, and Nextia conceptually. It is not currently a separate repository or governance layer.

## Future changes

Admission of another MOLI component or a change in internal-governance delegation is a MOLI governance decision and must be reflected in `moli.toml`.
