# MOLI Platform Architecture 1.0

**Final conceptual baseline. Supersedes all previous Architecture 1.0 packages.**

Three complementary views define the architecture:

1. **Structural:** `Scientific Context ↔ MolSysSuite`, with optional MOLI Agent across both.
2. **Functional:** Knowledge | Modeling | Capabilities | Discovery.
3. **Dynamic:** KNOW → MODEL → DO → DISCOVER → LEARN.

**Scientific Context** conceptually groups Sabueso (Knowledge), Praxis (Know-how), and Nextia (Discovery). It is not necessarily a package.

**MolSysSuite** is the molecular modeling ecosystem and interoperates directly with Scientific Context where appropriate.

**MOLI Agent** provides optional reasoning/agency. Humans can operate the same infrastructure directly.

**Molecular Intelligence** is not a subsystem name or synonym for an LLM:
`Scientific Context + Molecular Modeling + Scientific Reasoning → Molecular Intelligence`.

Conceptual interoperability does not imply circular package dependencies.

## Additional Architecture 1.0 documents

- `CONTEXT_ASSEMBLY.md` — structured Scientific Context Assembly for MOLI and its distinction from document RAG.
- `LEARNING_LOOP.md` — meaning of LEARN and controlled promotion of experience into reusable Knowledge/Know-how.
- `MOLSYS_AI.md` — MolSys-AI as the MolSysSuite specialist agent and its boundary with MOLI Agent.
- `DEPLOYMENT_MODEL.md` — deployment-independent, local-first/remote-ready evolution from local resources to shared, remote, distributed, or hybrid infrastructure.
- `OBJECT_IDENTITY_AND_PORTABILITY.md` — serialization, stable identity, referencability, versioning, provenance, and location-independent scientific objects.
- `VISIBILITY_AND_CONFIDENTIALITY.md` — separation of semantic ownership from visibility/publication, enabling open infrastructure with private or controlled scientific context and discovery programs.
- `PROJECT_ARCHITECTURE.md` — project-level organization: MOLI Project Workspace, Nextia ProjectGraph, MOLI ProjectRecord, ProjectStore, provenance contract, and their relationship to audit/replay/communication.

These documents refine consequences of the frozen architecture; they do not introduce a new top-level structural boundary.

Architecture 1.0 deliberately separates scientific semantics from deployment topology and from visibility/publication policy. Important scientific objects should be serializable and referencable so local implementations can evolve toward shared or remote services without redefining their scientific meaning, while authorization and confidentiality remain independently enforceable.
