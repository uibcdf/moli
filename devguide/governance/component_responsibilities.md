# Current component responsibilities

This maintained platform map supplements the frozen
[Architecture 1.0](../../architecture_1.0/README.md). It is a selected responsibility
map, not an exhaustive MolSysSuite roster or scientific capability inventory.
`moli.toml` owns direct membership; MolSysSuite owns its member registry and
qualification. Moli remains optional; scientists can use components directly.

| Concern | Owner |
| --- | --- |
| SourceAssertions, knowledge and reference-preserving retrieval | Sabueso |
| Capability/Protocol methodology, applicability and implementation selection | Praxis |
| DiscoveryProject, project interpretation, Evidence and Decisions | Nextia |
| Molecular modeling ecosystem and internal member governance | MolSysSuite |
| Cross-platform optional scientific agency | Moli |
| Execution observations and recording substrate | Recorda; platform provenance composition remains separately owned |
| Actual resource/software attribution | Ackredit under its provider and consumer contracts |

## BindingMT receiving — 2026-11-12

[MolI #97](https://github.com/uibcdf/moli/issues/97) receives the continuing suite
component **BindingMT**, formerly DockingMT, for **modeling and characterizing
molecular binding**. [BindingMT #108](https://github.com/uibcdf/bindingmt/issues/108)
and [MolSysSuite #190](https://github.com/uibcdf/molsyssuite/issues/190) own component
and member receiving. Repository ID **1380446251** and issue/Git history continue.
The current distribution/import is `bindingmt`, viewer package
`molsysviewer_bindingmt` and addon/workspace `bindingmt`. No deprecated aliases or
compatibility packages are selected by its owner. Original source tag/artifacts
stay immutable; renaming creates no new package publication.

| Binding operation | Owner-reported scope at source `95b69df` |
| --- | --- |
| Molecular docking | Existing bounded Vina/Vinardo profiles; not every partner/chemistry. |
| Fixed-identity complex prediction | Accepted domain; Boltz-2 #110 is proposed, no received runtime/API. |
| Complex refinement | Accepted domain; provider design/qualification, including HADDOCK3 #109, remains pending. |
| Absolute/relative binding free-energy calculation | Accepted future capability; no qualified provider/implementation. |
| Binding free-energy prediction | Accepted future endpoint-specific capability; no qualified provider/implementation. |
| Binding-interface characterization | Accepted future capability; current pose-interaction association/viewing is narrower. |

The [pinned scientific scope](https://github.com/uibcdf/bindingmt/blob/95b69dfb573e40073b5f2b182c4c6043aed98db3/devguide/SCIENTIFIC_SCOPE.md)
and [owner receiving receipt](https://github.com/uibcdf/bindingmt/blob/95b69dfb573e40073b5f2b182c4c6043aed98db3/devguide/validation/data/bindingmt_identity_scope_receiving_2026-11-11.json)
are source/owner evidence. Reported selected installed/admin/DOM checks are not
new central executions; the owner's full ordinary gate remains incomplete after
its memory interruption. No general scientific-accuracy, live browser, public
package or new engine qualification follows from this map.

MolSysMT keeps generic molecular identity, preparation, conversion, maps and
analysis; TopoMT/specialized owners keep numerical/topographic kernels; MolSysViewer
keeps generic visualization. BindingMT owns binding-specific operations, engine
adaptation, association and interpretation within qualified profiles. PeptideMT
keeps peptide generation/design intent and evaluation, reusing appropriate public
binding operations. Single-molecule folding and sequence generation are not
assigned wholesale to BindingMT.

## Scientific engines and historical references

Apply this map to the provider-neutral study in [MolI #84](https://github.com/uibcdf/moli/issues/84)
and Praxis #18. Preserve distinct scientific results for structure prediction,
sequence design, complex prediction/refinement and binding endpoints; a common
technical invocation must not merge their meaning. Praxis selects methodology;
Nextia, Recorda, Ackredit and Sabueso keep their project, recording, attribution
and knowledge responsibilities. No compulsory model, agent or new adapter runtime
is introduced by receiving the component identity.

Frozen architecture and original receipts retain DockingMT where it identifies
historical source, artifact or examples. Use BindingMT in current maintained
maps; do not rewrite immutable technical identifiers or qualification history.
Suite registry, labels, dependency/profile migration and generated guides stay
suite-owned. No consumer source, package, engine or caller environment changes
are performed by this central receiving.
