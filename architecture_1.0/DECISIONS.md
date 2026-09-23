# Architecture Decision Log

## Structural view
Scientific Context groups Sabueso/Praxis/Nextia conceptually. MolSysSuite is molecular modeling. They interoperate conceptually in both directions. MOLI Agent is optional across both. Scientific Context is not necessarily a package.

## Functional view
Knowledge→Sabueso; Modeling→MolSysSuite; Capabilities→Praxis; Discovery→Nextia.

## Dynamic view
`KNOW → MODEL → DO → DISCOVER → LEARN`. Learning may yield curated Sabueso knowledge, validated Praxis know-how, and retained Nextia experience.

## Molecular Intelligence
Reserved for the emergent capability:
`Scientific Context + Molecular Modeling + Scientific Reasoning`.

## Interoperability
Ownership does not imply isolation. Conceptual bidirectionality does not imply circular package dependencies; use stable interfaces/adapters.

## Epistemic vocabulary
Sabueso: SourceAssertion. Nextia: Evidence. Cross-cutting: Provenance.
`SourceAssertion ≠ Evidence ≠ Provenance`.

Other frozen boundaries: Capability≠Protocol; Project≠Engine; Strategy≠Protocol; Campaign≠Protocol; Artifact≠Result≠Observation≠Evidence; graph-shaped Discovery; Focus+Goal; contextual roles; stable references; auditable history.
