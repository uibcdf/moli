---
summary: Review a portable workload request and infrastructure policy-discovery boundary.
issue: uibcdf/moli#96
status: partial
opened: 2026-11-08
closed:
verification: inspected
area: [architecture, execution, infrastructure]
blocked_by: []
supersedes: []
---

# Execution and external infrastructure

## Decision and open implementation

MolI defines computational needs and general safety obligations; infrastructure
providers determine where and how to execute them safely. The accepted
[resource working rule](../policies/resource_aware_execution.md) applies now.
The minimum integration below is **design review material**, not a frozen API or
implemented execution service. It elaborates the existing
[deployment-independent architecture](../../architecture_1.0/DEPLOYMENT_MODEL.md)
without changing Architecture 1.0. #95 is superseded by #96 and the separately
owned [UIBCDF infrastructure #1](https://github.com/uibcdf/uibcdf-infrastructure/issues/1).

| Concern | Owner |
| --- | --- |
| Scientific Capability/Protocol, selected method and applicability | Praxis and scientific component owners |
| Project meaning, authoritative scientific state and interpretation | Nextia; implementation remains deferred |
| General workload requirements and cross-platform integration contract | MolI #96 |
| Site configuration, scheduler/admission, containment and operational recovery | Replaceable infrastructure provider |
| Execution recording and project provenance composition | Recorda/platform; #18/#28/#36 remain separate |
| Suite/member adoption, profiles and tests | MolSysSuite and member owners |

An administrative workload attempt or admission receipt is not a second
ExecutionPlan/Run, scientific Result or Evidence. Correlate with owner-issued
identities where they exist; do not invent project semantics for a development
test process. Moli remains optional and grants no independent execution authority.

## Proposed minimum exchange

These are semantic information groups, not prescribed JSON keys:

- **Request:** caller/task/correlation and intended operation; immutable code,
  inputs and environment identity where available; estimated versus required
  CPU/RAM/accelerator/scratch/duration; child concurrency; locality/network and
  confidentiality constraints; authorized budget and bounded waiting policy.
- **Discovery/capabilities:** explicit operator-configured policy location,
  revision/digest and scope; supported admission, monitoring, cancellation and
  whole-workload limits; authentication/access via the operator's existing route,
  never embedded credentials. Missing/stale/unreadable required policy stays
  unavailable. Passive discovery must not execute arbitrary policy code.
- **Admission:** admitted with explicit allocation/lease and expiry if supported,
  deferred with reason/revisit condition, rejected with reason, or unavailable.
  An estimate or preflight observation is not an exclusive allocation. Do not
  accept a silent fallback that violates required confidentiality or protection.
- **Execution observation:** stable provider attempt/correlation, lifecycle times,
  queued/running/terminal status, actual limits, available measured usage, exit or
  interruption reason, output identity/completeness and explicit gaps. Backend
  status never supplies scientific acceptance.
- **Cancellation/retirement:** identify the owned attempt and its children,
  acknowledge cancellation separately from confirmed termination, release owned
  leases and retain uncertain/orphan cleanup for the provider. Retry creates a
  related attempt; an uncertain write/start is not permission to duplicate it.

A backend switch must preserve the scientific/environment requirements or be
reported incompatible. No hostname, queue partition, fixed memory budget or
mandatory Linux mechanism enters the platform request. External services require
their separate access, disclosure and spending authorization.

## Planned receiving; none executed by this design

Before accepting a versioned runtime contract, the owners should demonstrate:

1. Two offline providers or deterministic stubs accepting the same bounded request,
   with distinct capabilities and honest unavailable-policy/unsupported-limit
   outcomes. Substitution needs no scientific component change.
2. Admission, bounded deferral/rejection and cancellation before/after start;
   failed/partial output, retry correlation and uncertain termination remain visible.
3. Concurrent attempts, stale leases and a nonparticipating workload cannot be
   ignored by a claimed coordination guarantee. Provider tests own containment,
   full child-family limits, graceful escalation and recovery in a safe sandbox.
4. Missing external integration preserves permitted local/lightweight operation
   and defers unsafe expensive work. No UIBCDF repository is imported by default.
5. A separately authorized reference integration with UIBCDF infrastructure, plus
   a receiving record from the delegated suite. Host/SSH availability, production
   deployment and scientific qualification are distinct evidence.

No stress test, model job, prefix migration, provisioning or site access change
is authorized by writing this proposal. #96 remains partial for provider review,
policy discovery implementation, executable contract and actual receiving. The
[adoption record](../governance/platform_guidance_adoption.md) retains these limits.
