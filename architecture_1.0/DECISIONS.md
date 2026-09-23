# Architecture Decision Log

## Structural view
Scientific Context groups Sabueso/Praxis/Nextia conceptually. MolSysSuite is molecular modeling. They interoperate conceptually in both directions. MOLI Agent is optional across both.

## Functional view
Knowledge→Sabueso; Modeling→MolSysSuite; Capabilities→Praxis; Discovery→Nextia.

## Dynamic view
`KNOW → MODEL → DO → DISCOVER → LEARN → KNOW`.

LEARN is explicit. Project experience remains in Nextia; reusable knowledge or know-how reaches Sabueso/Praxis only through explicit curation/validation gates.

## Molecular Intelligence
Reserved for `Scientific Context + Molecular Modeling + Scientific Reasoning`.

## Scientific Context Assembly
MOLI context is not defined as document RAG. Structured context may be assembled from Sabueso, Praxis, and Nextia while preserving semantics, provenance, conflicts, validation, and history.

`Context Assembly ≠ document retrieval`.

## MolSys-AI
MolSys-AI remains in the MolSysSuite domain as its specialist agent. It may combine RAG-based software knowledge with authorized tool execution.

`MolSys-AI ≠ MOLI Agent`.

MOLI may delegate to MolSys-AI or access MolSysSuite APIs directly.

## Interoperability
Ownership does not imply isolation. Conceptual bidirectionality does not imply circular package dependencies.

## Epistemic vocabulary
Sabueso: SourceAssertion. Nextia: Evidence. Cross-cutting: Provenance.

`SourceAssertion ≠ Evidence ≠ Provenance`.

Other frozen boundaries remain: Capability≠Protocol; Project≠Engine; Strategy≠Protocol; Campaign≠Protocol; Artifact≠Result≠Observation≠Evidence; graph-shaped Discovery; Focus+Goal; contextual roles; stable references; auditable history.
