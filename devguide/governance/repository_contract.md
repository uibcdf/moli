# Repository Ownership Contract

## Principle

Each repository owns its implementation. MOLI owns contracts shared between MOLI components and platform-wide governance.

> **A concern is governed at the lowest level that owns the shared contract it affects.**

## MOLI component ownership

Sabueso, Praxis, Nextia, MolSysSuite, and MOLI Agent are components of MOLI.

Each component owns its local implementation and component-specific behavior.

## Platform ownership

`uibcdf/moli` owns decisions that define or change relationships between MOLI components or the wider platform contract.

Examples include SourceAssertion/Evidence boundaries, Capability invocation contracts, Context Assembly, visibility/disclosure principles, and Scientific Context ↔ MolSysSuite interoperability.

## Components with internal governance

MolSysSuite is both:

1. a component of MOLI; and
2. a governed ecosystem with its own members.

MOLI governs the contract of MolSysSuite **as a MOLI component**.

`uibcdf/molsyssuite` governs MolSysSuite's internal repositories, policies, tooling, membership, and shared component contracts.

Thus:

```text
MolSysSuite ↔ Nextia contract   → MOLI
MolSysMT ↔ TopoMT contract      → MolSysSuite
TopoMT implementation          → TopoMT
```

Internal governance delegation does not remove MolSysSuite from MOLI's component model.

## Scientific Context

Scientific Context is a conceptual grouping of Sabueso, Praxis, and Nextia, not a separate governance repository.

## Exceptions

If ownership is ambiguous, begin at the lowest plausible owner and escalate/cross-link when evidence shows that a higher-level shared contract is involved. Do not duplicate implementation or authoritative issues.
