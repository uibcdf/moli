# Resource-aware execution

Accepted general contributor working rule under
[MolI #96](https://github.com/uibcdf/moli/issues/96), preserving the incident and
coordination history in [#95](https://github.com/uibcdf/moli/issues/95).
Applies to MolI development and directly governed components. MolSysSuite owns
member instructions and receiving. Infrastructure providers own site-specific
admission, coordination, limits, deployment and recovery.

## Before expensive execution

Apply this rule to tests, builds, benchmarks, simulations, model inference and
other operations that can materially affect a shared environment. Lightweight
reads and edits need no resource reservation ceremony. Before an expensive job:

1. Identify the active environment, its owner-supplied execution policy and any
   available scheduler/admission route. Load the relevant policy before execution;
   recording its URL without applying it is insufficient. If required policy is
   unavailable or conflicting, report the gap and defer the affected job.
2. Estimate the whole job's peak RAM, CPU/process/thread concurrency, accelerator
   memory, scratch/I/O and expected duration where relevant. Include worker and
   native-library fan-out, not just the launcher. Label unknown estimates.
3. Inspect current resource availability/pressure, existing workloads and known
   reservations using authorized read-only mechanisms. Respect the site's safety
   reserve for the OS, access/interactive sessions and other users. A point-in-time
   check does not reserve those resources or exclude another agent.
4. Select bounded concurrency and an admissible execution scope. Unknown demand
   calls for a small bounded probe, reduced scope or deferral; it never justifies
   using every reported CPU. State the budget, estimate basis, monitoring and stop
   conditions. No universal RAM percentage or pytest worker count is prescribed.

The local repository may document expensive suites and measured profiles, keeping
measurements tied to inputs/environment. Those facts belong in its technical
notes and tests. A generic instruction does not invent a profile for every host.
Use published receptors under the existing developer-tool policy; their reporting
or worker defaults do not override resource limits or required test scope.

## Managed and direct routes

Where a scheduler or approved admission mechanism manages substantial work, use
it and respect its allocation, queue and whole-job controls. Do not bypass a
required scheduler because direct execution appears idle. Site-specific Slurm
partitions, cgroups/systemd settings, hostnames and numeric limits belong to the
infrastructure provider, not MolI's project defaults.

On direct-execution machines, follow the active site's policy, explicit limits
and coordination mechanism when available. Distinguish a resource observation,
a cooperative reservation and enforceable containment; one does not prove the
others. Report which protections are actually available for the full child
process family. If the required protections are absent, reduce or defer the
workload and identify the missing capability. Do not silently claim safe
multi-agent admission from independent preflight checks.

Without an external integration, MolI remains usable for eligible local work.
Use conservative bounded execution only when permitted by the active policy;
otherwise defer expensive work. No UIBCDF-specific repository, new scheduler,
remote service or agent is a mandatory scientific dependency.

## During execution and recovery

Monitor pressure and the agreed budget at an appropriate cadence. Bound waiting;
if admission cannot be obtained within the chosen window, return a deferred
status with reason, owner and retry trigger. On pressure or budget breach, reduce
work when supported or cancel the owned workload through its approved route.
Do not terminate unrelated processes, clear another task's scratch or change host
configuration to rescue a test. Prefer graceful interruption and retain useful
outputs/logs when permitted; escalation and orphan handling remain provider-owned.

Record completed, deferred, rejected, interrupted, cancelled and failed outcomes
honestly. An OOM/interruption or incomplete output is not a passing test or a
scientific result. Preserve the original attempt, actual limits/measurements,
partial-output state and recovery gap; do not automatically retry into the same
pressure. Release owned reservations only after confirming termination or record
uncertain cleanup for the operator. Follow the
[temporary-resource lifecycle](../governance/temporary_resource_lifecycle.md).

## Policy discovery and authority

Use an explicit trusted operator/project configuration to locate the active
infrastructure policy; record its revision or digest, applicable scope and
available capabilities. Loading policy text does not authorize executing remote
code, changing system settings, spending money, sending private data or reading
credentials. Combine legitimate repository and environment constraints, apply the
more restrictive compatible requirement, and ask the owner to settle conflicts
before the affected job. This policy cannot override higher-priority instructions
or expand the task's existing authority.

The [integration proposal](../pending_proposals/execution_infrastructure_contract.md)
defines review material for request/status/cancellation boundaries and planned
receiving. It is not an implemented adapter, wire schema, reservation service or
host-protection guarantee. [UIBCDF infrastructure #1](https://github.com/uibcdf/uibcdf-infrastructure/issues/1)
owns the reference implementation; MolSysSuite independently owns member adoption.
