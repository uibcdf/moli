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

- **MOLI** — platform/umbrella: `uibcdf/moli`.
- **MOLI Agent** — scientific agent: `uibcdf/moli-agent`.
- **MolSys-AI** — MolSysSuite-specialized AI subsystem/umbrella: `uibcdf/molsys-ai`.
- **MolSys-AI Agent** — MolSysSuite specialist agent: `uibcdf/molsys-ai-agent`.
- **MolSys-AI Server** — remote inference/Software Knowledge/docs-assistant services: `uibcdf/molsys-ai-server`.
- **MolSys-AI Client** — lightweight typed SDK: `uibcdf/molsys-ai-client`.

MOLI Agent may delegate to MolSys-AI Agent, but neither agent is a mandatory gateway.

## Deployment model
Architecture 1.0 is deployment-independent and local-first/remote-ready. Scientific semantics remain stable across local, shared, remote, distributed, and hybrid deployments. Architecture 1.0 does not prescribe microservices or providers.

A Run remains the same kind of scientific object regardless of execution location; execution details belong to provenance/reproducibility metadata.

## Object identity and portability
Important persistent scientific objects should be serializable and referencable. Stable scientific identity should not depend solely on process, path, database location, machine, or service endpoint.

Architecture 1.0 freezes stable referencability and explicit provenance while leaving identifier syntax, serialization, storage, versioning implementation, and resolution open.

Identity, version/revision, content location, resolution, and authorization are distinct concerns.

## Visibility, confidentiality, and publication

Semantic ownership does not determine visibility.

Sabueso may contain public or private Knowledge; Praxis may contain public or private Know-how; Nextia may contain public or private Discovery context. Public/open-source implementations do not imply public scientific content.

`semantic ownership ≠ visibility ≠ publication status`.

`promotion ≠ publication`.

A private DiscoveryProject may promote curated Knowledge or validated Know-how into controlled/private Sabueso or Praxis context. Publication, patenting, embargo, sharing, and internal retention are separate governance decisions.

MOLI may therefore operate as open infrastructure for private science. Context Assembly and remote execution must respect authorization, disclosure policy, and trust boundaries.

## Interoperability
Ownership does not imply isolation. Conceptual bidirectionality does not imply circular package dependencies.

## Epistemic vocabulary
Sabueso: SourceAssertion. Nextia: Evidence. Cross-cutting: Provenance.

`SourceAssertion ≠ Evidence ≠ Provenance`.

Other frozen boundaries remain: Capability≠Protocol; Project≠Engine; Strategy≠Protocol; Campaign≠Protocol; Artifact≠Result≠Observation≠Evidence; graph-shaped Discovery; Focus+Goal; contextual roles; stable references; auditable history.


## Project-level architecture

A real MOLI project distinguishes four complementary concepts:

- **MOLI Project Workspace** — logical project-scoped organization/access context.
- **Nextia ProjectGraph** — evolving structured scientific graph and continuity of the DiscoveryProject.
- **MOLI ProjectRecord** — complete cross-platform provenance/history required for audit, traceability and replay.
- **MOLI ProjectStore** — physical storage backend(s).

`ProjectGraph ≠ ProjectRecord ≠ ProjectWorkspace ≠ ProjectStore`.

Nextia owns scientific continuity; MOLI provenance infrastructure composes provenance continuity. Components retain semantic ownership of their objects and participate through stable references and a common provenance contract rather than arbitrary writes into a shared scientific megastore.

The ProjectGraph may continue to grow after Conclusions. Historical states/releases remain reconstructable.

Replay uses recorded Decisions/ExecutionPlans and does not require new LLM reasoning; rerun creates a new discovery trajectory.

Scientific Communication is a derived view over the ProjectGraph/ProjectRecord and is not the authoritative scientific record.


## Project graph, shared references, and consistency

Nextia owns the semantic Discovery objects of the ProjectGraph. EventLedger records consequential change but does not replace ProjectGraph semantic authority.

Project-scoped references to shared Sabueso/Praxis objects do not imply project ownership or physical duplication.

Cross-component scientific operations preserve explicit lifecycle/partial/failure/cancellation states and correlation identity. Architecture 1.0 requires auditable consistency rather than pretending distributed operations are atomically completed.

Stable historical references remain part of the record even when their current targets are unavailable, unauthorized, archived, or externally removed.


## Project architecture implementation consequences

Project integration is understood at three conceptual levels: component-owned records, MOLI provenance infrastructure, and composed project-level views/operations. These levels do not imply separate physical services.

A human-browsable local filesystem Workspace is the preferred initial materialization when practical. The project descriptor acts as the bootstrap contract; participating components receive project-scoped context instead of inventing paths.

Small structured records/notebooks/manifests may be version-controlled while large Artifacts remain in ProjectStore and are referenced by stable identity/content metadata.

ProjectGraph must support historical inspection, state/graph diffs, and chronological timeline views conceptually; exact APIs are not frozen.

ProjectRecord/project-wide views may be virtual/materialized/cached/computed. MOLI does not require a duplicated persistent global graph.

Portability distinguishes reference export from self-contained archival export.

Nextia provides scientific continuity because Discovery gives project-specific meaning to Knowledge, Results, Evidence, and subsequent Decisions; this does not make Nextia the hierarchical owner of other components.


## Portable execution and rented resources

MOLI is local-first but execution-location agnostic.

ExecutionPlan expresses scientific intent, EnvironmentSpec, and provider-independent ResourceRequirements. Infrastructure selects an eligible ExecutionBackend among local workers/schedulers, institutional or partner HPC, cloud, or rented specialized compute according to explicit compatibility, confidentiality, authorization, locality, availability, and cost/budget policy.

Provider-specific APIs remain behind replaceable backend adapters and must not leak into scientific Protocol semantics.

Remote/rented instances are normally ephemeral compute. Required inputs are staged minimally; required Results/Artifacts and provenance are durably committed to an approved ProjectStore/ProjectRecord before ephemeral resources disappear.

Recorda records the actual backend, hardware, environment, software, lifecycle, inputs, and outputs used by the Run.

Local hardware capacity is not the architectural ceiling of MOLI.
