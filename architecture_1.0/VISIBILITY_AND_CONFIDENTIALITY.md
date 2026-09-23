# Visibility, Confidentiality, and Publication Boundaries

MOLI separates **scientific semantics and ownership** from **visibility, confidentiality, and publication policy**.

A concept belonging semantically to Sabueso, Praxis, Nextia, MolSysSuite, or another component does not determine whether its concrete content must be public or private.

> **Semantic ownership ≠ visibility ≠ publication status.**

## Open infrastructure, private discovery

A natural deployment and development model is:

```text
PUBLIC / OPEN
────────────────────────────
MOLI architecture
Sabueso framework
Praxis framework
Nextia framework
MolSysSuite
MolSys-AI
reusable generic methodology


PRIVATE / CONTROLLED
────────────────────────────
real DiscoveryProjects
unpublished Questions/Hypotheses
proprietary SourceAssertions/curation
internal Protocols
experimental/computational Results
Evidence and Decisions
Candidates and molecular designs
confidential Artifacts
project-specific learning
```

This is a useful default pattern, not a requirement that every framework artifact be public or every discovery artifact be private.

## Code and content are different layers

A public software component may operate on private scientific content.

Examples:

```text
Sabueso code       PUBLIC      private curated knowledge      CONTROLLED
Praxis code        PUBLIC      proprietary Protocols          CONTROLLED
Nextia code        PUBLIC      DiscoveryProjects              CONTROLLED
MOLI Agent code    PUBLIC      project context                CONTROLLED
MolSysSuite code   PUBLIC      molecular Results/Artifacts    CONTROLLED
```

Open-source licensing of software does not imply publication of the data, knowledge, methodology, projects, or molecular assets processed by that software.

## Visibility is orthogonal to semantic ownership

Sabueso may own both public and private Knowledge.

Praxis may own both public and private Know-how.

Nextia may own both public and private Discovery context.

Therefore future implementations should be able to distinguish visibility scopes such as:

- public;
- organization/internal;
- project-private;
- explicitly shared;
- embargoed/unpublished;

without changing the scientific type of the underlying object.

The exact access-control model is not frozen in Architecture 1.0.

## LEARN does not imply publication

The learning loop:

`KNOW → MODEL → DO → DISCOVER → LEARN → KNOW`

describes scientific accumulation, not disclosure.

For example, experience from a private DiscoveryProject may produce:

- private curated Knowledge in Sabueso;
- private validated Know-how in Praxis;
- a public generalized Protocol;
- a public framework improvement;
- a publication;
- a patentable molecular asset;
- or no external disclosure at all.

Promotion from Nextia into Sabueso/Praxis and publication are separate decisions.

> **Promotion ≠ publication.**

## Vertical pilots

Real discovery programs may be maintained in controlled/private workspaces while using public MOLI infrastructure.

A repository such as `moli-vertical-pilots` can contain project-specific material including Questions, Hypotheses, Campaigns, Results, Evidence, Candidates, Decisions, and unpublished learning.

Generalizable improvements discovered through a vertical pilot may flow back into public frameworks without requiring disclosure of confidential project content.

```text
private vertical pilot
        │
        ├── framework/general improvement ──► public repositories
        │
        ├── generic publishable methodology ─► public Praxis content
        │
        └── proprietary scientific learning ─► controlled context
```

## Context Assembly and disclosure

MOLI Context Assembly must respect visibility and authorization boundaries.

The fact that an agent can resolve a scientific object does not imply that its content may be sent to every model or service.

Future policy may distinguish, for example:

```text
public context       → approved external backend
private context      → trusted/private backend
restricted context   → no model disclosure without authorization
```

Identity, resolution, authorization, visibility, and disclosure policy remain distinct concerns.

## Artifacts and compute

Private scientific content may be processed using local, institutional, or rented compute resources. Deployment choice must not silently change confidentiality policy.

When data or context crosses a trust boundary, authorization and disclosure policy must be explicit.

## Publication is a deliberate scientific/governance action

MOLI Architecture does not decide when scientific results should be published, patented, shared, embargoed, or retained internally.

Those are project/organizational governance decisions.

The architectural requirement is that provenance, ownership, visibility, and authorization can be preserved well enough for those decisions to be made deliberately.

## Architectural invariant

> **MOLI may be open infrastructure for private science.**

Open architecture and open-source software are compatible with proprietary DiscoveryProjects, confidential Scientific Context, private methodological know-how, and protected molecular assets.
