# MOLI Agent

MOLI Agent is the optional scientist-facing reasoning and agency component of the MOLI Platform.

It operates across:

- **Scientific Context:** Sabueso, Praxis, and Nextia;
- **MolSysSuite:** molecular modeling components;
- authorized external scientific engines exposed through platform interfaces.

MOLI Agent may interpret scientific intent, query Sabueso, inspect DiscoveryProjects, propose Questions/Hypotheses/Strategies, identify uncertainty or conflict, invoke DiscoveryEngine, use Praxis Capabilities/Protocols, call modeling APIs, and interpret Results, Observations, and Evidence.

## Multi-level access

`Discovery operation ↔ Capability ↔ Protocol ↔ Modeling API`

Semantic abstractions must not prevent expert-level access to underlying scientific APIs.

## Authority

MOLI Agent does not own scientific truth, certify methodology, or silently mutate project state beyond configured authority. Execution and mutation rights are governed by explicit policy and approval gates.

A human scientist can operate the same Scientific Context and MolSysSuite infrastructure without MOLI Agent.

> **MOLI proposal ≠ scientific certification.**
