# MOLI Agent

MOLI Agent is the optional scientist-facing reasoning and agency component of the MOLI Platform.

It operates across Scientific Context, MolSysSuite, optional MolSys-AI specialist delegation, and authorized external scientific engines.

## Scientific Context Assembly

MOLI does not need to rely only on document RAG. It can assemble structured context from Sabueso knowledge/SourceAssertions/conflicts/provenance, Praxis Capabilities/Protocols/validation/limitations, and Nextia project state/history/Results/Observations/Evidence/Decisions.

See `CONTEXT_ASSEMBLY.md`.

## Multi-level access

`Discovery operation ↔ Capability ↔ Protocol ↔ specialist agent ↔ Modeling API`

MOLI may use semantic Praxis Capabilities, delegate MolSysSuite-specific operations to MolSys-AI, or access expert APIs directly.

## Scientific role and authority

MOLI may interpret intent, inspect DiscoveryProjects, propose Questions/Hypotheses/Strategies, identify uncertainty/conflict, invoke DiscoveryEngine, interpret Results/Observations/Evidence, and help plan next actions.

MOLI does not own scientific truth, certify methodology, or silently mutate project state beyond configured authority. A human scientist can operate the same infrastructure without MOLI Agent.

> **MOLI proposal ≠ scientific certification.**
