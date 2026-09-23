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

## Naming convention

The following names have distinct architectural meanings and should be used consistently in repositories, documentation, APIs, and team communication:

- **MOLI** — the Molecular Intelligence platform and umbrella project. Repository: `uibcdf/moli`.
- **MOLI Agent** — the scientific reasoning and agency component operating across Scientific Context and MolSysSuite. Repository: `uibcdf/moli-agent`.
- **MolSys-AI** — the MolSysSuite-specialized AI subsystem and umbrella project. Repository: `uibcdf/molsys-ai`.
- **MolSys-AI Agent** — the specialist agent that understands and operates MolSysSuite. Repository: `uibcdf/molsys-ai-agent`.
- **MolSys-AI Server** — remote inference, MolSysSuite software-knowledge, retrieval/RAG, and documentation-assistant services. Repository: `uibcdf/molsys-ai-server`.
- **MolSys-AI Client** — lightweight typed SDK for MolSys-AI remote services. Repository: `uibcdf/molsys-ai-client`.

Thus `MOLI` should not be used as shorthand for `MOLI Agent`, and `MolSys-AI` should not be used as shorthand for `MolSys-AI Agent` when the distinction matters.

MOLI Agent may delegate MolSysSuite-specialist work to MolSys-AI Agent, but neither agent is a mandatory gateway to the underlying scientific components.

## Deployment model
Architecture 1.0 is deployment-independent and local-first/remote-ready.

Scientific semantics must remain stable across local, shared, remote, distributed, and hybrid deployments. Architecture 1.0 does not prescribe microservices, cloud providers, schedulers, container systems, or a specific control-plane/compute-plane implementation.

A Run remains the same kind of scientific object regardless of execution location; backend, hardware, software environment, seed, and other execution details belong to provenance/reproducibility metadata.

## Object identity and portability
Important persistent scientific objects should be serializable and referencable.

Stable scientific identity should not depend solely on an in-memory object, transient filesystem path, database location, machine, or service endpoint. References should preserve semantic ownership and support movement from local to remote storage/services without redefining the object.

Architecture 1.0 freezes the requirement for stable referencability and explicit provenance, but leaves identifier syntax, serialization format, storage backend, versioning implementation, and resolution mechanism open.

Identity, version/revision, content location, resolution, and authorization are distinct concerns where relevant.

## Interoperability
Ownership does not imply isolation. Conceptual bidirectionality does not imply circular package dependencies.

## Epistemic vocabulary
Sabueso: SourceAssertion. Nextia: Evidence. Cross-cutting: Provenance.

`SourceAssertion ≠ Evidence ≠ Provenance`.

Other frozen boundaries remain: Capability≠Protocol; Project≠Engine; Strategy≠Protocol; Campaign≠Protocol; Artifact≠Result≠Observation≠Evidence; graph-shaped Discovery; Focus+Goal; contextual roles; stable references; auditable history.
