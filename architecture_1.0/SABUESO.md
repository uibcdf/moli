# Sabueso — Knowledge Context

Sabueso is the **Knowledge-context component** of the MOLI Platform.

Its responsibility is to transform heterogeneous external and curated information into structured, traceable, resolved molecular knowledge that can be consumed by scientists, MOLI Agent, and modeling components.

## Core flow

`Source → SourceAssertion → normalization/resolution → Resolved Knowledge → Card / Deck / relationships`

A `SourceAssertion` records what a source asserts about an entity or property. It preserves source identity, source record/version, asserted value, normalized value where appropriate, retrieval information, and provenance.

Its acquisition provenance records how Sabueso obtained the assertion
(database import, human curation, rule extraction, or model extraction),
separately from the source's identity and any upstream origin the source
reports. A human-validated extraction remains identifiable as an extraction.
Historical assertions without this provenance are `not_recorded`; their
acquisition route must not be inferred. The [conceptual schema](schemas/sabueso_source_assertion_conceptual_schema.md)
defines this shared meaning, while Sabueso owns its concrete representation.

The former Sabueso term `Evidence` is deprecated for this role. Conceptually:

- `Evidence` → `SourceAssertion`
- `EvidenceStore` → `SourceAssertionStore`
- `evidence_ids` → `source_assertion_ids`

This migration prevents collision with Nextia `Evidence`.

## Relationship with Nextia

A SourceAssertion may be referenced as part of the basis for Nextia Evidence after project-contextual scientific interpretation, but it does not automatically become Evidence.

`SourceAssertion ≠ Evidence ≠ Provenance`

## Relationship with MolSysSuite

Sabueso knowledge is not isolated from modeling. MolSysMT, TopoMT, or other MolSysSuite components may consume Cards, entity mappings, annotations, relationships, or other resolved knowledge through stable interfaces/adapters.

Sabueso retains semantic ownership of that knowledge.

> **Sabueso knows; it does not discover.**
