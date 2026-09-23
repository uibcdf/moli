# Repository Ownership Contract

## Principle

Each repository owns its implementation. MOLI owns only shared platform contracts and directly governed cross-component policy.

> **A concern is governed at the lowest level that owns the shared contract it affects.**

## Local ownership

Sabueso, Praxis, Nextia, and MOLI Agent own their local code, tests, APIs, scientific behavior, release decisions, and component-specific documentation.

A local implementation detail does not become a MOLI platform decision merely because the repository belongs to MOLI.

## Platform ownership

`uibcdf/moli` owns decisions that define or change relationships shared across directly governed components or the wider platform boundary.

Examples include stable cross-component reference semantics, SourceAssertion/Evidence boundaries, Capability invocation contracts, Context Assembly contracts, visibility/disclosure principles, and Scientific Context ↔ MolSysSuite interoperability.

## Delegated domains

MolSysSuite is a delegated governance domain. Its internal policies and component contracts are owned by `uibcdf/molsyssuite`.

MOLI governs only contracts that cross between MolSysSuite and the rest of the platform.

## Exceptions

If ownership is ambiguous, open the issue at the lowest plausible owner and cross-link/escalate to MOLI when evidence shows a shared contract is involved. Do not solve ambiguity by duplicating implementation or authoritative issues.
