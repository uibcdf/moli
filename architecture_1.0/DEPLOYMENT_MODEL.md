# Deployment Model

MOLI Platform Architecture 1.0 is **deployment-independent**.

The scientific architecture defines responsibilities, semantics, ownership, provenance, and interactions between Scientific Context, MolSysSuite, MOLI Agent, MolSys-AI, and external scientific engines. It does not prescribe where these components must run.

> **Scientific architecture and deployment topology are independent concerns.**

The same scientific concepts should remain valid whether the platform runs on a single workstation, a laboratory cluster, institutional HPC infrastructure, commercial cloud infrastructure, specialized GPU providers, or a hybrid combination of these resources.

## No owned-compute requirement

A valid MOLI deployment must be able to operate **without founder-owned, laboratory-owned, or institution-owned compute infrastructure**.

Persistent platform services, storage, reasoning backends, and scientific compute may all be hosted on contracted infrastructure when necessary.

Conceptually:

    researchers / clients
            |
            v
    contracted persistent infrastructure
        MOLI / Scientific Context / databases
        ProjectRecord / ProjectStore
            |
            v
    contracted elastic compute
        CPU / GPU / HPC / specialized resources

Owned/local resources, when available, are an optimization for cost, latency, privacy, resilience, or throughput. They are not an operational prerequisite for the platform.

This supports startup and small-team deployments in which scientists work remotely or from home while persistent services and computational resources run in datacenters or other contracted infrastructure.

> **MOLI must be capable of operating entirely on contracted infrastructure; owned compute is an optional optimization, not an architectural dependency.**

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



## Execution portability as an architectural goal

MOLI should be **local-first but execution-location agnostic**.

Scientific intent must be expressible independently of the machine or provider that eventually executes it.

Conceptually:

    Decision
        ↓
    ExecutionPlan
        ├── scientific inputs
        ├── Capability / Protocol
        ├── parameters
        ├── EnvironmentSpec
        └── ResourceRequirements
                ↓
        execution policy / broker
          ┌─────┼───────────┐
          ▼     ▼           ▼
        local  HPC      rented/cloud
          └─────┼───────────┘
                ↓
               Run

Changing the execution backend must not silently change the scientific meaning of the ExecutionPlan.

> **Execution is portable. Scientific intent is expressed independently of execution location; MOLI may satisfy an ExecutionPlan using local, institutional, partner, cloud, or rented resources without changing its scientific meaning or provenance requirements.**

## ResourceRequirements

An ExecutionPlan should be able to express resource requirements without naming a provider.

Examples may include:

    CPU count / architecture constraints
    RAM
    GPU required
    minimum GPU VRAM
    accelerator capabilities
    precision requirements
    scratch/storage
    expected wall time
    network/data-locality constraints
    specialized software/license requirements

The exact schema is implementation-open.

A requirement such as:

    gpu = required
    min_vram = 40 GB

should allow MOLI to determine that no local worker is compatible and consider an eligible remote/rented backend without rewriting the scientific plan.

## Execution backends and resource brokering

MOLI should expose a provider-independent execution contract.

Conceptually:

    ExecutionBackend
        ├── local process / workstation
        ├── local scheduler / Slurm
        ├── SSH / partner infrastructure
        ├── institutional HPC
        ├── cloud VM / batch
        └── rented specialized GPU

Provider-specific APIs belong behind adapters rather than inside scientific components or Protocols.

A future Resource Broker may match:

    ResourceRequirements
          +
    EnvironmentSpec
          +
    execution policy
          ↓
    eligible ExecutionBackend

The broker is infrastructure/orchestration, not a scientific reasoning component.

## Execution policy and cost

When several compatible resources exist, infrastructure policy may consider:

    prefer local resources
    queue/wait time
    expected runtime
    monetary cost
    project budget
    deadline / priority
    confidentiality
    data locality
    energy/operational policy
    provider trust

MOLI Agent may request scientific work, but provider selection and spending limits should be governed by explicit execution policy/authorization rather than improvised model reasoning.

The exact scheduling/optimization algorithm is not part of Architecture 1.0.

## Environment portability

Portable execution requires more than portable inputs.

ExecutionPlans/Runs should be able to reference an environment specification sufficient to identify or reconstruct the required software environment.

Where appropriate this may include:

    container image
    immutable image digest
    Python/environment lock
    CUDA/runtime requirements
    scientific engine versions
    driver/hardware compatibility constraints

Containers are a strong implementation direction for remote/rented execution but are not mandated for every Capability.

The invariant is reproducible environment identity, not one container technology.

## Ephemeral remote compute and persistent ProjectStore

A rented/cloud compute instance should normally be treated as **ephemeral compute**, not as the authoritative ProjectStore.

Conceptually:

    ProjectStore
        |
        | stage required inputs
        v
    ephemeral ExecutionBackend
        |
        | execute Run
        v
    Results / Artifacts
        |
        | retrieve / verify
        v
    ProjectStore
        |
        v
    backend may be destroyed

The Run is not complete from a durability perspective merely because remote computation finished. Required outputs/provenance must be retrieved or durably committed according to policy.

Large Artifacts may remain in an approved remote store when policy permits, but their stable identity, location, integrity, retention, and authorization state must remain represented in the ProjectRecord.

## Minimal execution bundles

Remote execution should not require copying an entire ProjectWorkspace.

MOLI should be able to derive a minimal execution bundle or equivalent staged dependency set from the ExecutionPlan and provenance graph.

Conceptually:

    RunBundle
        ├── execution manifest
        ├── required inputs
        ├── parameters
        ├── environment specification
        ├── required Protocol/Capability references
        └── scoped ephemeral credentials when unavoidable

Only the information required and authorized for that Run should leave the trusted project environment.

Secrets must not be persisted in Recorda/ProjectRecord or embedded permanently in execution bundles.

## Confidentiality and remote execution

Eligibility for remote/rented execution depends on more than hardware compatibility.

Execution policy must consider:

    project visibility
    proprietary inputs
    unpublished structures
    patient/sensitive data where applicable
    provider trust
    geographic/organizational constraints
    license restrictions
    credential scope

A scientifically compatible provider may therefore be operationally ineligible.

Context/data availability never implies permission to transmit it to an external compute backend.

## Recorda and actual execution provenance

The ExecutionPlan records intended requirements; the Run/Recorda record must capture what was actually used.

For remote or local execution, provenance should be able to identify as applicable:

    backend class
    provider / infrastructure identity
    instance / worker identity
    hardware model
    GPU VRAM / relevant accelerator properties
    CPU / RAM
    driver
    CUDA/runtime
    container/environment identity
    scientific software versions
    input identities
    output identities
    seeds / precision
    lifecycle timestamps
    provisioning / execution / retrieval status

This allows the same ExecutionPlan to be compared across different eligible backends.

## Failure and lifecycle of ephemeral resources

Remote execution introduces lifecycle states beyond scientific success/failure.

A Run may need to distinguish:

    backend requested
    resource provisioned
    inputs staged
    execution started
    execution completed
    outputs retrieved
    integrity verified
    record committed
    resource destroyed

Failures at any stage must remain auditable.

Destroying an ephemeral instance must not erase the evidence required to explain a failed or partial Run.

## Local capacity is not the platform ceiling

MOLI should not be designed around the largest resource physically owned by the laboratory.

Local infrastructure is the preferred everyday capacity when appropriate; external resources extend the execution envelope.

Therefore a Capability requiring, for example, substantially more single-GPU VRAM than the local cluster provides should be representable and schedulable rather than architecturally unsupported.

This lets local hardware optimize routine throughput while exceptional workloads use institutional or rented resources.


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

