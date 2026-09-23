# MOLI infrastructure census

**Snapshot:** 2026-09-23. This census records implementation evidence visible in the
published UIBCDF repositories and distinguishes a repository's existence from a usable
implementation. It is an implementation-status record, not a change to the frozen
[Architecture 1.0](../architecture_1.0/README.md) or a second membership registry.
The authoritative direct-component registry is [`moli.toml`](../moli.toml);
MolSysSuite and MolSys-AI maintain their own member/subsystem registries.

## Status vocabulary

- **Implemented (bounded):** working code and a validation path exist for the scope
  stated in the row. It does not assert a stable API or a live deployment.
- **In development:** implementation code exists, while the described architectural
  responsibility is only partly covered.
- **Incubating:** a repository and design/governance material exist, but the intended
  package or runtime is not implemented there yet.
- **Specified:** architecture or development guidance defines a required capability;
  no corresponding platform implementation was verified. This does not imply that a
  separate repository should be created.

The links below point to the commits inspected for this snapshot. A README's future
tense and an illustrative code example are design evidence, not implementation
evidence. Service availability, release maturity, and private deployments were not
verified.

## Direct MOLI components and platform governance

| Scope and owner | Repository | State and observed evidence | Next verifiable step |
| --- | --- | --- | --- |
| MOLI architecture and engineering governance | [`uibcdf/moli`](https://github.com/uibcdf/moli/tree/888902eb2ccc482c62c6f75da9d8f0bf9bb56442) | **Implemented (bounded):** component/policy registry, guide delivery checks, governance validation and hosted CI. This is coordination infrastructure, not a ProjectWorkspace runtime. | Keep the registry, delivered guides and hosted checks current as components are added. |
| Sabueso — Knowledge, Cards, SourceAssertions and resolution | [`uibcdf/sabueso`](https://github.com/uibcdf/sabueso/tree/4e89944a79e9177f829e4945c51a1bee63519fc1) | **In development:** Python package, mappings, storage, schemas, offline tests and CI exist; the [README](https://github.com/uibcdf/sabueso/blob/4e89944a79e9177f829e4945c51a1bee63519fc1/README.md) calls it early-stage. | Complete and verify the minimum Knowledge contract and repository-local adoption work. |
| Praxis — Capabilities and Protocols | [`uibcdf/praxis`](https://github.com/uibcdf/praxis/tree/3a59f6f89755b3db7d3fa6c459c5cbed0bae1763) | **Incubating:** repository, architecture and governance skeleton exist; its [README](https://github.com/uibcdf/praxis/blob/3a59f6f89755b3db7d3fa6c459c5cbed0bae1763/README.md) says APIs and storage are not frozen, and no Praxis runtime package was found. | Implement a small inspectable Capability/Protocol path with tests. |
| Nextia — DiscoveryProject, ProjectGraph and DiscoveryEngine | [`uibcdf/nextia`](https://github.com/uibcdf/nextia/tree/c9568128d80274aae3176c687e37507a355814b9) | **Incubating:** repository and Discovery design exist; its [README](https://github.com/uibcdf/nextia/blob/c9568128d80274aae3176c687e37507a355814b9/README.md) establishes the implementation home, with no Nextia runtime package yet. | Build a minimal persistent project graph and deterministic operation against it. |
| MolSysSuite — modeling ecosystem | [`uibcdf/molsyssuite`](https://github.com/uibcdf/molsyssuite/tree/4012f75e16298d7e04a72d21a97e898cf8c4c7bc) | **Implemented (bounded):** delegated member registry, policies and validation exist; modeling code lives in member repositories. This row makes no claim that every member has the same maturity. | Use [`suite.toml`](https://github.com/uibcdf/molsyssuite/blob/4012f75e16298d7e04a72d21a97e898cf8c4c7bc/suite.toml) and the suite's adoption records for member-level status. |
| MOLI Agent — optional cross-domain scientific agency | [`uibcdf/moli-agent`](https://github.com/uibcdf/moli-agent/tree/d784745462ec2b18a8be9a34321900e487d9fc61) | **Incubating:** the repository **does exist**; its [README](https://github.com/uibcdf/moli-agent/blob/d784745462ec2b18a8be9a34321900e487d9fc61/README.md) and development guide define the boundary, but no agent runtime code was found. | Specify the contracts needed for a first controlled scientific-context action, then implement and test it. |

## Delegated MolSys-AI subsystem

MolSys-AI belongs to MolSysSuite. Its internal [registry](https://github.com/uibcdf/molsys-ai/blob/c1b67196f5b2f1e3de8a8b2ec5bf752afc5b0462/molsys-ai.toml)
is authoritative for Server, Client and Agent membership. MOLI records only the
platform-relevant maturity and boundary with MOLI Agent.

| Scope | Repository | State and observed evidence | Next verifiable step |
| --- | --- | --- | --- |
| MolSys-AI umbrella and internal governance | [`uibcdf/molsys-ai`](https://github.com/uibcdf/molsys-ai/tree/c1b67196f5b2f1e3de8a8b2ec5bf752afc5b0462) | **Implemented (bounded) governance; incubating runtime:** architecture, guides and internal registry exist; the specialist runtime belongs in the child repositories. | Maintain the migration and member evidence in MolSys-AI. |
| Server — inference and Software Knowledge | [`uibcdf/molsys-ai-server`](https://github.com/uibcdf/molsys-ai-server/tree/a71c091401ec45e04a76270e196cc614ae3758f3) | **In development:** chat API, retrieval/indexing, model server, widget, tests and deployment material exist. Its [README](https://github.com/uibcdf/molsys-ai-server/blob/a71c091401ec45e04a76270e196cc614ae3758f3/README.md) describes the documentation chatbot; this census did not verify a live endpoint. Legacy client/agent prototypes still reside here. | Preserve the working documentation surface while extracting only responsibility-appropriate code to Client and Agent. |
| Client — typed SDK for remote services | [`uibcdf/molsys-ai-client`](https://github.com/uibcdf/molsys-ai-client/tree/a0b98299ba028799888f7c508d1de378251ca7ee) | **Incubating:** API/configuration/compatibility design exists, with no SDK package or tests in the inspected tree. | Implement the roadmap's minimal typed transport and test it against Server. |
| Agent — MolSysSuite specialist | [`uibcdf/molsys-ai-agent`](https://github.com/uibcdf/molsys-ai-agent/tree/9cc97fae9d4fedb55e2e1044836ac48ef8271a6d) | **Incubating:** architecture and migration maps exist, with no agent runtime in this repository. Legacy prototypes remain in Server. | Extract a tested, bounded MolSysSuite operation without requiring Server for every action. |

## Recording and project-level infrastructure

These are capabilities of the platform design, not an instruction to create one
repository per concept. [Project Architecture](../architecture_1.0/PROJECT_ARCHITECTURE.md)
separates component-owned scientific objects, MOLI provenance infrastructure and
composed project views.

| Capability and owner | Implementation home / repository | State and observed evidence | Next verifiable step |
| --- | --- | --- | --- |
| Recorda — standalone scientific recording substrate; MOLI integration is platform-owned | [`uibcdf/recorda`](https://github.com/uibcdf/recorda/tree/401c4d4928c603885e6fa9179f3ef2232b9cb95d) | **Incubating:** repository exists with a [design-stage README](https://github.com/uibcdf/recorda/blob/401c4d4928c603885e6fa9179f3ef2232b9cb95d/README.md) and development guidance, but no package code, tests or release metadata. Recorda is an independent library, not a new top-level MOLI scientific component. | Prototype RecordingSession and one safe semantic instrumentation boundary, first with Sabueso as proposed in [MOLI's integration design](RECORDA.md#minimal-first-experiment). |
| Scientific Context Assembly | MOLI platform and future MOLI Agent consumers; no separate repository prescribed | **Specified:** [structured context contract](../architecture_1.0/CONTEXT_ASSEMBLY.md) exists; no implementation verified. | Assemble a small, reference-preserving context from real Sabueso/Praxis/Nextia objects when their minimum contracts exist. |
| ProjectWorkspace, ProjectStore and project descriptor | MOLI platform; repository boundary open | **Specified:** logical organization, access/storage context and preferred initial local materialization are in [Project Architecture](../architecture_1.0/PROJECT_ARCHITECTURE.md). No runtime implementation verified. | Prove a human-browsable local Workspace with stable project-scoped references and a descriptor. |
| Cross-component identity and reference resolution | MOLI platform with component-owned identities | **Specified at platform level:** [identity/portability contract](../architecture_1.0/OBJECT_IDENTITY_AND_PORTABILITY.md) exists; Sabueso has local object IDs, but no cross-component resolver was verified. | Resolve at least one stable reference across independently owned component records without copying semantic ownership. |
| ProjectRecord, EventLedger, manifests and Recorda routing | MOLI platform, fed by component records | **Specified:** [Project Architecture](../architecture_1.0/PROJECT_ARCHITECTURE.md) and [Recorda integration](RECORDA.md) define distinct provenance and Discovery responsibilities; no composed MOLI runtime was verified. | Record and reconstruct one cross-component project operation after a minimal Recorda substrate exists. |
| ExecutionPlan/Run, audit, trace, replay and export | MOLI project infrastructure, with component and Nextia records | **Specified:** [reproducibility design](REPRODUCIBILITY_AUDIT_AND_REPLAY.md) defines the evidence and explicitly leaves several representations open. No end-to-end project replay was verified. | Exercise a human-driven Decision → ExecutionPlan → Run pilot with manifests before adding agent orchestration. |
| Scientific communication | MOLI composition of Nextia, component and ProjectRecord data | **Specified:** [ProjectBriefing, ProgressBrief and ProjectReport](SCIENTIFIC_COMMUNICATION.md) are designed; no renderer or structured artifact implementation was verified. | Produce a traceable structured report from a real project record before adding presentation formats. |
| Project visibility and authorization | MOLI project infrastructure plus component-owned policy | **Specified:** [visibility](../architecture_1.0/VISIBILITY_AND_CONFIDENTIALITY.md) and [deployment](../architecture_1.0/DEPLOYMENT_MODEL.md) rules exist; no platform-wide enforcement was verified. | Demonstrate a local access decision and redacted context/record export in a project pilot. |

The provenance and replay rows group the pending KnowledgeSnapshot, DecisionRecord,
RunRecord, ProjectStateSnapshot, ProjectManifest, IntegrityManifest, ReplayPreflight,
ProjectRelease, agent/human action, amendment and approval semantics listed in the
[reproducibility design](REPRODUCIBILITY_AUDIT_AND_REPLAY.md#concepts-to-formalize-before-implementation).
They are not counted as separate products or presumed Python classes.

## Boundaries and maintenance

Scientific Context is a conceptual grouping, Molecular Intelligence is a property of
the integrated system, and LEARN is a controlled process. None requires a separate
repository by name. The modeling methods and physical-loop ideas in
[Future Directions](../architecture_1.0/FUTURE_DIRECTIONS.md) are horizons, not
unimplemented commitments in this census.

Update a row when a repository is created, implementation code lands, a tested
end-to-end path becomes available, or a repository boundary changes. Record the date,
the exact repository commit or hosted evidence, the scope that works, and the next
unverified capability. The owning repository tracks implementation issues; this
census points to maturity evidence without becoming a duplicate issue backlog.
Recheck delegated summaries against MolSysSuite and MolSys-AI registries rather than
copying their complete member inventories into MOLI.
