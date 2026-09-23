# Deployment Model

MOLI Platform Architecture 1.0 is **deployment-independent**.

The scientific architecture defines responsibilities, semantics, ownership, provenance, and interactions between Scientific Context, MolSysSuite, MOLI Agent, MolSys-AI, and external scientific engines. It does not prescribe where these components must run.

> **Scientific architecture and deployment topology are independent concerns.**

The same scientific concepts should remain valid whether the platform runs on a single workstation, a laboratory cluster, institutional HPC infrastructure, commercial cloud infrastructure, specialized GPU providers, or a hybrid combination of these resources.

## Local-first, remote-ready

Architecture 1.0 does not require remote services or microservices.

An initial deployment may consist simply of:

```text
Python packages
+
local databases / files
+
workstations
+
laboratory CPU/GPU servers
```

This is expected to be a natural starting point for a small scientific team.

The architecture should nevertheless avoid assumptions that would prevent components from later becoming remotely accessible services.

A useful principle is:

> **Local objects today should be able to become remotely addressable objects tomorrow without changing their scientific semantics.**

## Possible deployment evolution

A plausible evolution is:

```text
Stage 1
────────────────────────
local Python packages
local Scientific Context
workstations / laboratory GPUs


Stage 2
────────────────────────
shared Scientific Context
central Nextia projects
shared Sabueso / Praxis
remote or shared MOLI
local compute workers


Stage 3
────────────────────────
distributed computation
local GPUs
+
institutional HPC
+
rented CPU/GPU infrastructure


Stage 4
────────────────────────
hybrid infrastructure
dynamic resource allocation
multiple compute backends
```

These stages are illustrative, not normative.

Architecture 1.0 does not require the platform to pass through them in this order.

## Control plane and compute plane

A future deployment may benefit from separating relatively persistent scientific state and orchestration from computationally intensive workloads.

Conceptually:

```text
                     CONTROL PLANE

              Sabueso   Praxis   Nextia
                  \       │       /
                   \      ▼      /
                      MOLI
                       │
                DiscoveryEngine
                       │
                      Run
                       │
───────────────────────┼────────────────────────
                       │
                   COMPUTE PLANE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        local         HPC         rented
       compute      cluster       compute
          │            │            │
          └────────────┼────────────┘
                       ▼
                   MolSysSuite
               + external engines
```

This is a deployment pattern, not a new scientific boundary.

Scientific Context and MolSysSuite retain the same semantics regardless of where their implementations execute.

## Runs are location-independent scientific objects

A `Run` should represent a scientific execution independently of where that execution occurs.

The same conceptual Run may execute on:

```text
workstation
laboratory server
institutional HPC
commercial cloud
specialized GPU provider
partner infrastructure
```

The execution location becomes part of provenance rather than part of the scientific identity of the Run.

A Run may therefore record information such as:

```yaml
run:
  id: stable-id
  protocol_ref: stable-ref

  inputs:
    ...

  execution:
    backend: ...
    environment: ...
    hardware: ...
    software_versions: ...
    container_or_environment_ref: ...
    random_seed: ...

  outputs:
    ...

  provenance:
    ...
```

The exact schema remains implementation-open.

The architectural requirement is that sufficient execution information can be preserved to support traceability, reproducibility, comparison, and auditing.

## Compute backends are replaceable

Scientific workflows should avoid unnecessary dependence on a particular infrastructure provider.

A Protocol may require resources such as:

```text
CPU
GPU
memory
storage
wall time
specialized software
```

without requiring that those resources come from a specific provider.

Where practical, execution policy may select among:

```text
local
laboratory cluster
institutional HPC
commercial cloud
specialized compute provider
```

according to scientific requirements, availability, confidentiality, cost, and resource constraints.

This allows computational capacity to grow without making infrastructure topology part of scientific methodology.

## Remote Scientific Context

Sabueso, Praxis, and Nextia are natural candidates for shared or remote deployment because they contain persistent scientific context.

For example:

```text
Sabueso
    shared molecular knowledge

Praxis
    shared methodological know-how

Nextia
    shared DiscoveryProjects
```

Central deployment may eventually allow multiple scientists, agents, and compute workers to operate against authoritative shared state.

This does not require these systems to begin as network services.

## MOLI as a remote service

MOLI Agent may eventually run as a shared or remote service.

Clients may include:

```text
web interfaces
Jupyter
CLI
desktop applications
APIs
other scientific applications
```

MOLI should obtain only the Scientific Context required and permitted for the current reasoning operation.

The agent does not need direct access to every stored object.

## Context Assembly and confidentiality

Scientific Context Assembly provides a natural boundary for controlling what information is sent to a reasoning backend.

For example:

```text
Public Scientific Context
          │
          ├────► external model/backend permitted
          │
Proprietary Scientific Context
          │
          └────► trusted/private backend only
```

Context policy may consider:

* project permissions;
* intellectual-property sensitivity;
* unpublished molecular structures;
* proprietary Candidates;
* internal assay data;
* confidential Protocols;
* model/provider trust;
* organizational policy.

The architectural principle is:

> **Context availability does not imply unrestricted context disclosure.**

Context Assembly should be able to select the information appropriate for a particular reasoning backend while preserving references to authoritative internal objects.

## Data and Artifact locality

Large scientific Artifacts do not necessarily need to move with the control plane.

For example:

```text
Nextia
  Artifact reference
        │
        ▼
object storage / filesystem / HPC storage
```

Trajectories, molecular ensembles, docking poses, simulation checkpoints, model weights, and other large outputs may remain close to the compute resource while Nextia preserves stable references and provenance.

This allows the platform to scale without requiring all scientific data to reside in one database.

## Architecture 1.0 does not prescribe microservices

The existence of clear architectural components does not imply that each component should become an independent network service.

Premature decomposition into:

```text
sabueso-service
praxis-service
nextia-service
molsysmt-service
topomt-service
docking-service
...
```

would introduce operational complexity without necessarily improving scientific capability.

The preferred early strategy is:

```text
clear Python interfaces
+
serializable objects
+
stable identities
+
explicit provenance
+
clean component boundaries
```

Remote services should be introduced when real operational requirements justify them.

## Architectural invariant

Deployment may evolve substantially while the scientific architecture remains stable.

A transition such as:

```text
local
  ↓
shared
  ↓
remote
  ↓
distributed
  ↓
hybrid
```

should not require redefining what a Card, Capability, Protocol, DiscoveryProject, Run, Result, Evidence, or Decision means.

> **Infrastructure should move around the scientific model, not force the scientific model to move around the infrastructure.**

