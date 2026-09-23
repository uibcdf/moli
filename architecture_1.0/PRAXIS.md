# Praxis — Methodological Context

Praxis is the **Methodological-context / Know-how component** of the MOLI Platform.

Its responsibility is to encode reusable scientific know-how independently of any single DiscoveryProject or modeling implementation.

## Capability — WHAT

A `Capability` represents a semantic scientific ability: **what we know how to do**.

A Capability should be able to describe:
- identity/version;
- scientific intent;
- semantic input/output contracts;
- applicability and preconditions;
- available Protocols;
- validation status and supporting validation records;
- limitations;
- maturity/deprecation state.

Examples include comparing binding sites, identifying selective intervention sites, characterizing allosteric networks, evaluating mutations, screening compounds, or analyzing assays.

## Protocol — HOW

A `Protocol` represents a reproducible implementation of a Capability: **how the task is performed**.

A Protocol may specify inputs, prerequisites, exact tool/engine versions, parameters, steps, outputs, checks, provenance requirements, and cost/fidelity/resource characteristics.

Multiple Protocols may implement one Capability.

## Relationship with MolSysSuite and external engines

Praxis does not replace scientific APIs. Protocols may orchestrate MolSysSuite components and external engines. Capabilities provide a semantic level above those implementations without hiding expert access to lower-level APIs.

## Selection and composition

Protocol selection may depend on applicability, validation status, resources, cost/time, requested fidelity, and project policy. Deterministic policy may be executed by DiscoveryEngine; open-ended scientific judgment belongs to human scientists and/or MOLI Agent.

Capabilities may eventually compose other Capabilities; exact composition/recursion rules remain implementation-open and must preserve provenance and avoid hidden recursion.

## Methodological learning

`scientific need → APIs/tools → ad-hoc workflow → formalized Protocol → validation/generalization → Capability`

MOLI Agent may help compose or formalize methodology. It does not certify it.
