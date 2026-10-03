---
summary: Coordinate knowledge support, resource attribution, source terms, and project interpretation.
issue: uibcdf/moli#36
status: active
opened: 2026-10-03
closed:
verification: inspected
area: [architecture, attribution, interoperability]
blocked_by: []
supersedes: []
---

# Knowledge pipeline attribution across MOLI components

## Authority and status

This is the shared-boundary review for [MOLI #36](https://github.com/uibcdf/moli/issues/36),
not an accepted wire schema or a revision to frozen Architecture 1.0. It follows
the [architecture decisions](../../architecture_1.0/DECISIONS.md),
[project architecture](../../architecture_1.0/PROJECT_ARCHITECTURE.md), and
[object identity rules](../../architecture_1.0/OBJECT_IDENTITY_AND_PORTABILITY.md).
Sabueso owns its knowledge and packet implementation; Ackredit and its clients
are governed within MolSysSuite; Nextia owns project interpretation; MOLI/Recorda
owns cross-platform execution history. A release claim requires owner-local
installed-package evidence, separately from this semantic review.

## Distinct records and authorities

| Question | Authoritative record | Boundary |
| --- | --- | --- |
| What did a source state, and which exact statements support returned knowledge? | Sabueso SourceAssertions, relationships, and pinned knowledge | Source support does not assert that a resource was accessed in the current operation or that the project accepts a claim as Evidence. |
| Which resource, reference work, or software was actually used for this result? | Executing component's result attribution, with Ackredit's detached bibliography and contextual uses where adopted | Credit follows observed use, not installed packages, whole-card source lists, or inferred database releases. Ackredit owns its provider API and payload. |
| What obligations, restrictions, or unknowns did the source state for an intended use? | Sabueso terms report and source records | A citation does not grant permission. Source-stated terms are an input to the application's disclosure decision, not an authorization decision by Ackredit. |
| What happened during execution, including attempts, failures, retries, and meaningful consumption? | Component records plus MOLI/Recorda ProjectRecord and EventLedger | Execution provenance does not create bibliographic credit, source support, or Nextia Evidence by itself. |
| What did the knowledge or result mean for a project? | Explicit Nextia ProjectGraph interpretation and Evidence | Nextia cites owner-issued historical references; a citation or attribution record never silently creates Evidence or validates a Praxis Protocol. |

Praxis owns Capability and Protocol meaning, including stated method references,
limitations, and validation state. A Protocol's declared dependencies are not
proof that a particular Run executed every branch. The executing component and
the project record preserve what actually ran.

## Proposed minimum exchange behavior

These are semantic requirements for review, not prescribed Python classes, JSON
keys, or a common replacement for component-owned records.

1. **Acquisition and reuse are different events.** Preserve an acquisition
   attempt's outcome: acquired, evaluated empty, replayed/cached, failed, or
   unknown where observation is unavailable. A stored SourceAssertion can support
   a new result without implying a new download. An unqueried source receives no
   current acquisition credit; a failed request cannot masquerade as a completed
   acquisition. Do not infer a global database release from a source-record
   version.
2. **Bind records to the exact result.** A result can expose its own detached
   attribution and exact selected support, including conflicts and relationship
   dependencies. Keep the result's owner-issued identity/version or immutable
   snapshot reference with those records. Whole-card provenance and a workflow's
   deduplicated bibliography cannot replace a result's own scope. An enclosing
   application session may aggregate uses while each result retains resources
   reused by other results.
3. **Preserve original meaning on export and read.** Retain provider-issued pins,
   original source-record and executing-software versions, full observed
   bibliographic records, contextual roles, and explicit unknowns/gaps. A saved
   reader inspects those original records without new acquisition, attribution
   credit, silent current-head resolution, or metadata enrichment. Reference
   identity, availability, resolution, and authorization remain separate.
4. **Carry status and correlation without fabricating completeness.** Link a
   result, its support/attribution records, an execution attempt, and any later
   project interpretation using owner-issued references and correlation context.
   Report absent, failed, or partial attribution distinctly from complete
   attribution. A component may preserve a completed scientific result when an
   attribution provider fails, but the host exposes a diagnostic and the project
   must not present its provenance as complete. Project policy may require a
   stricter commit gate for consequential operations.
5. **Keep permission decisions explicit.** Terms reports name a use and what
   sources actually state, including unknowns. The authorized application or
   project decides whether content may be disclosed or reused. Bibliography
   alone, or permission to cite an article, does not authorize copying its text.

## Existing consumer evidence and limits

[Sabueso #108](https://github.com/uibcdf/sabueso/issues/108) has an automatic
packet-composition adapter and an application-owned Ackredit session. Its local
`sabueso.packet_attribution@1` sidecar remains separate from packet/card/store
payloads and terms. The public offline two-result pilot retains reused
references, original versions, and saved-reader behavior. It observes
composition of stored knowledge; source acquisition, further result types,
complete bibliography, and public provider delivery remain open. Sabueso's
choice of a required Ackredit dependency is its own product decision; it does
not change the optional-client policy for MolSysSuite members.

[Ackredit #75](https://github.com/uibcdf/ackredit/issues/75) owns the
provisional `ackredit.attribution@1` capture/export/import contract, including
detached bibliography, contextual uses, and workflow capture. Its first stable
API release and public package remain pending under Ackredit #75 and #22.
Source-installed Python 3.14 validation does not establish public Conda closure.
MolSysSuite coordinates its provider/member review; MOLI does not edit those
repositories.

## Decisions and evidence still needed

- Review the semantic seam with one Sabueso result, one Ackredit provider record,
  and prospective Nextia/Praxis and Recorda consumers. Determine the minimum
  links and status vocabulary they actually need without standardizing local
  sidecar schemas prematurely.
- Coordinate the exact historical knowledge-reference and resolution guarantees
  with [MOLI #3](https://github.com/uibcdf/moli/issues/3), and execution
  correlation/telemetry with [MOLI #18](https://github.com/uibcdf/moli/issues/18).
  Packet details remain in [MOLI #22](https://github.com/uibcdf/moli/issues/22).
- Ask MolSysSuite to review how Ackredit and its member clients expose detached
  result/workflow records, gaps, original versions, and saved-reader behavior.
  Ackredit's API, bibliographic registry, delivery, and member adoption stay
  with their owning issues.
- Exercise a public, synthetic two-result workflow that includes a reused
  resource, an evaluated-empty or failed acquisition, a saved read, and an
  explicit project interpretation. Demonstrate that neither citation nor
  recording alone creates Evidence or permission.

## Resolution

Pending cross-component review and the acceptance exercise. No shared wire
format, universal dependency rule, or release is accepted by this report.
