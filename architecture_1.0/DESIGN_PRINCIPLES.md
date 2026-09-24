# Design Principles

1. Scientific Context provides structured persistent context; it is not synonymous with AI.
2. MolSysSuite provides molecular modeling and may consume Scientific Context directly.
3. Molecular Intelligence emerges from Scientific Context + Molecular Modeling + Scientific Reasoning.
4. MOLI Agent is optional; reproducible science works without it.
5. MolSys-AI is the specialist agent for MolSysSuite and remains distinct from MOLI Agent.
6. Context Assembly ≠ document retrieval; structured scientific semantics and references must be preserved.
7. MOLI may use semantic Capabilities, specialist-agent delegation, or direct expert APIs.
8. Ownership does not imply isolation.
9. Conceptual interoperability does not require circular package dependencies.
10. Sabueso, Praxis, and Nextia retain distinct epistemic ownership.
11. SourceAssertion ≠ Evidence ≠ Provenance.
12. Capabilities do not hide expert APIs.
13. Capability promotion requires validation.
14. Discovery is graph-shaped.
15. DiscoveryProject state/history ≠ DiscoveryEngine action.
16. Strategy ≠ Protocol; Campaign ≠ Protocol.
17. Artifact ≠ Result ≠ Observation ≠ Evidence.
18. External knowledge does not automatically become project Evidence.
19. Candidate is optional/type-agnostic.
20. Stable references/provenance are first-class.
21. Failure, contradiction, inconclusive, rejected, and superseded states are meaningful.
22. Human agency/approval gates are first-class.
23. Compose external scientific engines where appropriate.
24. LEARN is explicit: project experience becomes shared Knowledge or Know-how only through curation/validation gates.
25. Discovery improves knowledge and methodology.
26. Avoid pharmacology-specific core assumptions.
27. AI-generated methodology is not automatically validated methodology.
28. Scientific architecture and deployment topology are independent concerns; Architecture 1.0 is local-first and remote-ready without prescribing microservices.
29. Important persistent scientific objects should be serializable and referencable, with stable identity independent of transient process, filesystem, database, machine, or service location.
30. Object identity, version/revision, content location, resolution, and authorization are distinct concerns where scientifically relevant.
31. Remote or distributed execution must preserve scientific semantics, provenance, reproducibility information, and auditable references.
32. Infrastructure should evolve around the scientific model rather than forcing deployment-specific concepts into scientific semantics.
33. Semantic ownership, visibility, authorization, and publication status are independent concerns.
34. Public/open-source frameworks may operate on private, proprietary, embargoed, or otherwise controlled scientific content.
35. LEARN and promotion into Sabueso/Praxis do not imply publication; `promotion ≠ publication`.
36. Context Assembly and remote execution must respect disclosure policy and trust boundaries.

37. A MOLI project distinguishes ProjectWorkspace, Nextia ProjectGraph, MOLI ProjectRecord, and ProjectStore; these concerns must not be collapsed.
38. Nextia ProjectGraph owns structured scientific continuity of a DiscoveryProject; it is graph-shaped, extensible, and preserves rejected, superseded, reopened, and historical scientific states.
39. MOLI ProjectRecord provides cross-platform provenance continuity for audit, trace, replay, integrity, and release without duplicating component-owned scientific objects.
40. Components own their scientific objects; MOLI provides project-scoped organization, stable cross-component references, provenance infrastructure, and portability.
41. Participating components should satisfy a common provenance contract appropriate to their persistent objects and consequential events.
42. A shared mutable scientific megastore is not the integration model; use component ownership + stable references + typed ProjectGraph relationships + composed ProjectRecord.
43. ProjectWorkspace is a logical contract independent of ProjectStore physical topology.
44. Notebooks are human orchestration documents, not the authoritative ProjectRecord.
45. Scientific Communication is derived from the ProjectGraph and ProjectRecord; reports, slides, and videos are not the source of truth.
46. Replay follows the recorded trajectory without new scientific reasoning; rerun creates a new trajectory and may make different decisions.

47. Project scope/reference to shared Sabueso/Praxis objects does not imply project ownership or physical duplication.
48. Nextia owns ProjectGraph Discovery semantics; EventLedger records consequential changes but is not the semantic source of Discovery meaning.
49. Cross-component workflows must preserve explicit partial/failure/cancellation states and correlation identity; MOLI requires auditable consistency rather than fictitious distributed atomicity.
50. Stable historical references remain meaningful when current targets are unavailable, unauthorized, archived, or externally removed; resolution state must not be confused with historical nonexistence.

51. Project architecture has three conceptual levels: component-owned records, MOLI provenance infrastructure, and composed project-level views/operations; this does not prescribe three physical services.
52. A human-browsable local filesystem Workspace is the preferred initial materialization when practical, without coupling scientific identity to paths.
53. Small structured project material may be version-controlled while large scientific Artifacts may remain in ProjectStore; authoritative identity/location is expressed through manifests/references.
54. The project descriptor is the bootstrap contract for resolving project-scoped context; components should not invent independent project paths.
55. Historical ProjectGraph views, state/graph diffs, and chronological project timelines are required conceptual inspection capabilities; exact APIs remain open.
56. ProjectRecord/project-wide graph views may be virtual, materialized, cached, or computed; architecture does not require a duplicated persistent global graph.
57. Project portability distinguishes reference export from self-contained archival export, with unavailable/non-embeddable dependencies remaining explicit.
58. Nextia provides scientific continuity through Discovery semantics, not hierarchical control over Sabueso, Praxis, or MolSysSuite.

59. Execution is portable: scientific intent and ResourceRequirements are expressed independently of execution location/provider.
60. Local hardware is preferred capacity, not the architectural ceiling; eligible institutional, partner, cloud, or rented resources may satisfy an ExecutionPlan without changing its scientific meaning.
61. Provider-specific execution APIs belong behind replaceable ExecutionBackend adapters; scientific components and Protocols must not be coupled to a commercial compute provider.
62. Remote/rented compute is normally ephemeral; ProjectStore/ProjectRecord remain durable authorities and required outputs/provenance must be committed before ephemeral resource loss.
63. Remote execution stages the minimum required and authorized dependency set rather than the entire ProjectWorkspace.
64. Environment identity/portability is part of reproducibility; containers are a strong direction but no single container technology is architecturally required.
65. Resource selection is governed by explicit policy including compatibility, availability, confidentiality, cost/budget, data locality, and authorization; MOLI Agent does not improvise spending/provider policy.
66. Recorda/Run provenance records actual execution resources and environment, not only planned ResourceRequirements.
