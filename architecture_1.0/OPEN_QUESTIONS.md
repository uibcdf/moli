# Open Questions

These are intentionally not frozen implementation details.

## Scientific Context organization
- Exact repositories/package ownership for Sabueso, Praxis, and Nextia.
- Shared stable-reference and provenance primitives without creating tight coupling.
- Cross-project/private knowledge governance.

## Sabueso
- SourceAssertion schema/versioning details.
- SourceAssertionStore persistence.
- EntityResolver vs FieldResolver contracts.
- Relationship model and semantic KnowledgeQuery API.
- Card snapshot/version semantics.
- Literature/patent ingestion and curation gates.
- Confidence/uncertainty and conflicting SourceAssertion representation.

## Praxis
- Exact Capability/Protocol schemas and registry.
- Validation/maturity lifecycle.
- Public vs proprietary/project-local Capabilities.
- Composition/recursion semantics.
- External-engine/environment references.

## Nextia
- Exact DiscoveryProject graph representation/serialization.
- Result/Experiment/Run details.
- Campaign/run/task hierarchy.
- Resumability and approval-gate semantics.
- Artifact lifecycle/content addressing.
- Project lineage/forks and cross-project references.
- Candidate-collection abstraction.

## SourceAssertion / Evidence bridge
- Exact reference mechanism from Nextia Evidence to Sabueso SourceAssertions/resolved knowledge.
- How external knowledge snapshots are pinned for historical reproducibility.
- Confidence/uncertainty propagation across the boundary.

## MOLI Agent
- Sandbox/testing model for composed workflows.
- Agent proposal vs deterministic Engine behavior.
- Model/backend independence.
- Authority and approval policy.

## Experimental integration
- Laboratory data ingestion.
- Assay/protocol representation.
- Instrument/robotics integration.
