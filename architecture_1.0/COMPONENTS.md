# Component Responsibilities

## Scientific Context
**Sabueso — Knowledge context:** owns structured external/curated molecular knowledge, SourceAssertions, resolution, conflicts, Cards/Decks, and knowledge relationships.

**Praxis — Methodological context:** owns reusable Capabilities, reproducible Protocols, applicability, validation, and limitations.

**Nextia — Discovery context:** owns DiscoveryProject state/history and deterministic DiscoveryEngine orchestration.

## MolSysSuite
Owns molecular representation, interoperability, computation, simulation, analysis, and visualization through MolSysMT, MolSysViewer, TopoMT, ElastNetMT, PharmacophoreMT, DockingMT, and future modeling components.

MolSysSuite may consume Scientific Context and produce Results/Artifacts used by it.

## MOLI Agent
Optional reasoning/agency across Scientific Context and MolSysSuite.

**Ownership does not imply isolation.**
