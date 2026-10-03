# Cross-Component Feedback

MOLI components share responsibility for improving the platform while preserving provider ownership.

The [universal issue-feedback commitment](reporting_protocol.md#universal-issue-feedback-commitment)
also covers defects and improvements within the component someone is using. This
document adds the provider/consumer handoff for findings that cross repositories.

When one component reveals a limitation in another:

1. identify the provider that owns the missing capability;
2. report the need there with a minimal reproduction or concrete scientific/integration use case;
3. explain impact and required outcome without prescribing an unnecessary implementation;
4. cross-link consumer workarounds or blocked work;
5. open/escalate a MOLI issue if the resolution changes a shared platform contract.

A local workaround is temporary evidence, not a replacement for provider feedback.

For private discovery programs, sanitize the report so the provider can reproduce the platform need without exposing confidential project content.

## Contributing a fix across repositories

When work on one component requires a change in another repository, route the
change through the repository that owns the behavior:

1. If the need is not urgent and there is no ready fix, open or update a provider
   issue with the evidence and required outcome so its developers can prioritize it.
2. If a concrete fix is ready, propose it as a pull request to the provider for
   owner review. Link the owning issue (or open one for an otherwise unreported
   actionable finding) and any consumer work it unblocks.
3. If the change is urgent **and** Diego or Liliana are doing or directly
   supervising that development, ask them whether to use a direct commit and
   push, a pull request, or an issue. Direct push needs their explicit permission
   for that change. Urgency alone does not grant write authority.

These routes concern contributions **to another repository**. They do not
replace the owning team's normal local commit and review practice. A pull
request or approved direct push does not remove the issue-feedback duty for
the underlying bug or improvement. A change to a shared auxiliary provider
also follows the consumer-impact notice below; provider approval does not
substitute for coordination with affected consumers.

## Changes to shared auxiliary providers

When a developer or agent changes a UIBCDF auxiliary library or development
action that other components consume, assess the effect on those consumers.
This includes SMonitor, PyUnitWizard, ArgDigest, DepDigest, Pytest Receptor,
GH Run Receptor, the Conda build/upload action and the Sphinx-to-Pages action;
the trigger is plausible cross-package impact, not membership in this list.
Public behavior, APIs, serialized records, defaults, dependency or Python
requirements, diagnostics, workflow inputs/outputs and release behavior can
all create such impact. A private refactor with no plausible consumer effect
does not need a platform impact issue.

The provider owns the change, its tests and release, with an issue in its own
repository. Also open or update a **consumer-impact issue** in the governance
domain that must coordinate adoption:

| Affected consumers or contract | Impact issue |
| --- | --- |
| Direct MOLI components or a platform contract | `uibcdf/moli` |
| MolSysSuite members only | `uibcdf/molsyssuite` |
| Both domains, with distinct work in each | One issue in each, cross-linked |

Link the provider issue and identify affected or candidate consumers, the old
and proposed observable behavior, compatibility/version implications, migration
or fallback, available evidence and unknowns, and owners of follow-up work.
Notify as soon as the wider impact is recognized, before publishing the
provider change or starting consumer rollout when known in advance; report a
later discovery promptly. Use an existing impact issue when it already covers
the change. A change affecting
one consumer locally still belongs in provider and consumer issues; escalate
when wider impact becomes plausible. Notification coordinates work; it neither
transfers provider ownership nor automatically approves the change.

MolSysSuite decides its member policy and implementation. MOLI records its own
direct-component or platform implications and passes suite work through an
issue there, without editing suite or member repositories. Confidential or
exploitable details follow the private reporting route before public notice.
