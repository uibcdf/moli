---
summary: Define the first Praxis–Nextia integration slice without freezing component internals.
issue: uibcdf/moli#28
status: active
opened: 2026-09-26
closed:
verification: inspected
area: [architecture, methodology, discovery, integration]
blocked_by: []
supersedes: []
---

# First Praxis–Nextia integration slice

## Purpose and authority

This is a **shared-contract proposal**, not a revision to frozen Architecture 1.0 or
an accepted wire format. [MOLI #28](https://github.com/uibcdf/moli/issues/28)
owns its decisions. [Nextia #1](https://github.com/uibcdf/nextia/issues/1) and
[Praxis #1](https://github.com/uibcdf/praxis/issues/1) own component-local design
and implementation. The boundaries here follow the [architecture decisions](../../architecture_1.0/DECISIONS.md),
[project architecture](../../architecture_1.0/PROJECT_ARCHITECTURE.md),
[identity and portability](../../architecture_1.0/OBJECT_IDENTITY_AND_PORTABILITY.md),
and [visibility rules](../../architecture_1.0/VISIBILITY_AND_CONFIDENTIALITY.md).

The first implementation must be useful in a local, human-operated project without
an LLM, network service, or complete MOLI runtime. A public test fixture uses only
fictional scientific objects. Real project content may remain private.

## What is already decided

| Concern | Authority | Consequence for the first slice |
| --- | --- | --- |
| Reusable methodology | Praxis | Capability describes scientific intent; Protocol describes a reproducible way to fulfill it, with applicability, limitations, version, and validation state. |
| Project scientific meaning | Nextia | ProjectGraph owns Questions, Hypotheses, Observations, Evidence, Decisions, typed relations, and their history. A Result or SourceAssertion acquires project meaning only through an explicit interpretation. |
| External knowledge | Sabueso | Sabueso issues and resolves its references; Nextia retains the issued historical reference and adds its own Evidence meaning. |
| Computation and domain outputs | Executing component | MolSysSuite or another engine retains its authoritative modeling Results/Artifacts and local provenance. |
| Cross-platform provenance | MOLI/Recorda | ProjectRecord and EventLedger record what happened; they do not become the semantic owner of the ProjectGraph or of a component's scientific objects. |
| Project organization | MOLI Workspace | A component receives project-scoped context; it does not invent a project path or make the path an object identity. |

These are ownership boundaries, not requirements for separate services or mutual
Python imports. See [Recorda's MOLI integration](../RECORDA.md).

## Two acceptance journeys

### A. Knowledge and manual interpretation

1. A scientist opens project `P` with Focus and Goal, then records Question `Q`.
2. An external provider issues an immutable, versioned reference `K1` to one
   statement about fictional protein `X`. Nextia stores the full provider-issued
   reference and its owner/kind; it does not parse or copy the authoritative item.
3. The scientist explicitly creates project Evidence `E1`, states why `K1`
   **informs** Question `Q`, identifies limitations, and records actor and basis.
   A citation alone does not create `E1` and does not establish support. A
   Hypothesis may be added later.
4. A Decision `D1` may cite `E1` with rationale and authority. If the provider
   later changes its current view, `E1` and `D1` still cite `K1`.
5. If `K1` later cannot resolve, the project retains the citation and its own
   historical interpretation. Resolution reports an honest outcome; it never
   substitutes a newer state.

This route requires no Campaign, Protocol, Run, Candidate, or Hypothesis. A
Hypothesis is one possible later branch, not the project's required starting
state.

### B. Exploratory computation and methodological use

1. A scientist starts an exploratory Campaign to compare two fictional protein
   structures. Praxis offers an **experimental** Capability and an explicitly
   selected Protocol version `M1`; applicability and limitations remain visible.
2. The project records the selection and frozen execution intent before an
   attempt. One attempt fails; its identity, status, reason, and correlation
   remain in history. A retry is a separate attempt, not a rewrite.
3. The successful attempt produces Result reference `R1` and perhaps Artifact
   references. Their authoritative objects remain with the producing component.
4. A scientist explicitly creates Observation `O1` from `R1`; `O1` opens new
   Question `Q2`. A later Evidence item may relate the Observation to a
   Hypothesis, including contradiction or uncertainty.
5. If Praxis later publishes Protocol version `M2`, the historical attempt
   still points to `M1`. One successful attempt does not validate the
   Capability or promote the project workflow into shared know-how.

This route tests Observation-before-Hypothesis and non-success as scientific
history. It does not assume a pharmacology-specific Candidate.

## Proposed minimum seam between components

The names below describe fields and responsibilities, **not Python classes or
serialized keys**.

| Exchange | Minimum meaning |
| --- | --- |
| External scientific reference | Provider/owner, object kind, complete provider-issued opaque reference, and pinned version/snapshot when a historical dependency is required. Identity, location, resolution, authorization, and availability stay distinct. |
| Project context | Project identity, logical scope, actor/authority, visibility policy, resolver/storage context, and optional provenance/correlation context supplied by the Workspace. No component hard-codes another component's project path. |
| Method request/selection | Scientific Capability sought, input references and constraints, explicit selected Protocol version or a non-selection outcome. Deterministic policy may select; scientific judgment is recorded as a human/agent Decision. |
| Frozen execution intent | Selected method version, inputs, parameters, required environment/resources, expected outputs/checks, and authority. Physical quantities retain value, unit, and meaning under the [quantity integrity policy](../policies/quantity_integrity_policy.md). Changes after freezing create a new version/amendment. |
| Attempt and outputs | Distinct attempt/correlation identity, lifecycle and failure/partial state, actual environment/inputs, and owner-issued Result/Artifact references. No success is inferred from the existence of a request. |
| Project interpretation | Explicit Nextia operation, actor, statement, admissible basis references, subject relation (`supports`, `contradicts`, or `informs` where applicable), limitations, rationale/review state, and graph revision. Recording an operation never infers its scientific meaning. |
| Provenance event | References the authoritative object and before/after state where relevant; records actor, time, correlation, and status without becoming a second semantic store. Required recording failure remains visible. |

All historically consequential references are pinned to what was used. A resolver
may later report unavailable, unauthorized, offline/archived, removed, or unknown
according to the provider and disclosure policy; a consumer must not silently
fall back to the latest object. [MOLI #3](https://github.com/uibcdf/moli/issues/3)
still owns the exact Sabueso consumer reference guarantee.

## Decisions to settle before the execution bridge

1. **ExecutionPlan, Run, Result, Artifact ownership.** Architecture requires the
   Decision → frozen intent → attempt → output → interpretation chain, but leaves
   exact ownership and representation open. Propose that the first Nextia graph
   records project relations and owner-issued execution/output references; do not
   copy a producer's Result into a Nextia-owned object. Agree where the plan and
   attempt are authoritative before implementing their creation.
2. **Experimental methodology.** Architecture distinguishes Protocol from
   Capability and requires gated validation. Decide whether an experimental
   Protocol must refer to a provisional Capability, or whether a candidate
   workflow can exist before Capability association. Neither state may imply
   validation from a successful Run.
3. **Graph revisions and recording.** Nextia must expose historical state and
   typed relations. EventLedger may record changes but need not be the graph's
   storage engine. Choose a local persistence scheme only after it passes
   reopen, history, contradiction, and failed-update exercises.
4. **Reference and failure vocabulary.** Keep provider-specific identifier
   syntax opaque to consumers. Agree the minimum cross-component resolution
   outcomes and confidentiality behavior without exposing private existence to
   unauthorized callers.

## Acceptance tests for the shared boundary

- Journey A survives provider revision and an unavailable/unauthorized target;
  the original reference and Nextia interpretation remain inspectable.
- Journey B preserves a failed attempt, a separate retry, a later Protocol
  version, and an Observation that opens a Question without a Hypothesis.
- Two contradictory Evidence items can coexist; a later Decision can supersede
  an earlier one without erasure.
- No source citation, Result creation, or Recorda event alone creates Nextia
  Evidence or certifies a Praxis Capability.
- Praxis and Nextia each work independently outside a MOLI Agent session, with
  no circular package dependency and no shared mutable scientific megastore.
- A private project can use public framework code and remain absent from public
  fixtures, issue bodies, and test artifacts.
- A separate controlled exercise with a real scientific workflow checks that
  the design is usable beyond synthetic fixtures. Only generalized findings
  leave the controlled workspace.

## Resolution

Pending agreement at MOLI #28 and the linked component issues. This proposal
does not accept a cross-component API, identifier grammar, retention promise, or
execution ownership before the acceptance journeys are exercised.
