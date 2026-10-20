# Temporary development resource lifecycle

This working rule applies to MOLI and its directly governed components. It
covers resources created for development, tests, builds, documentation and
qualification, including resources in /tmp. MolSysSuite governs adoption inside
its member repositories through
[its own issue](https://github.com/uibcdf/molsyssuite/issues/104). Shared UIBCDF
tools own their implementation and report lifecycle gaps in their provider
repositories.

## Ownership and useful retention

Use /tmp when appropriate. An owned temporary resource may remain there while
it is needed for active work, failure investigation, handoff or later
verification. Evidence does not have to be moved elsewhere solely because it
is in /tmp. Preserve original candidate packages, digests and receipts for as
long as their release or audit route requires; deleting an exact artifact
before qualification finishes can destroy the evidence.

The task or tool that creates a resource owns its lifecycle unless ownership
is explicitly handed to a caller or another maintainer. At creation or handoff,
identify its purpose, path, owner and next review or retirement trigger. A
prefix, age, size or location does not establish that a path is disposable.
Keep caller output separate from private tool scratch.

## At completion and on failure

After the last required use, remove owned disposable test results, temporary
Conda or virtual environments, build and extraction trees, downloaded copies,
temporary wheels, documentation builds and task-specific caches. Make the
closeout review part of both successful and failed tasks or releases. Retain
resources still needed for investigation, follow-up or exact-artifact custody,
with an owner and a concrete review trigger. Record a cleanup failure or an
uncertain owner instead of silently claiming removal.

Code that creates private scratch should use a managed lifetime or a
finally/trap path where feasible. Tests for a changed executable tool should
cover success, failure and interruption or cleanup failure as applicable.
Do not let a cleanup error erase the primary failure; keep both visible.
Caller-owned outputs need an explicit retention/cleanup contract rather than
surprise deletion by a reusable tool.

## Safe scope

Remove only explicit paths that the current task owns after checking that no
active process, human edit or other session needs them. Do not use a broad
prefix, age-based or machine-wide cleaner. Do not delete system-private paths,
another task's cache, a primary checkout or an uncertain artifact. Registered
Git worktrees use Git's worktree lifecycle: inspect their status and owner,
then remove a retired clean worktree with git worktree remove; do not erase its
directory directly.

At task or release closeout, review task-owned roots, artifacts and retained
resources. Record the disposition of nontrivial resources: removed after final
use, retained with owner/review trigger, or unresolved with an owning issue.
Small scratch automatically removed by a managed lifetime needs no separate
inventory entry. Report a reusable
tool's lifecycle defect to its provider issue and link any shared-consumer
impact under [cross-component feedback](cross_component_feedback.md).

This rule is tracked in [MOLI #61](https://github.com/uibcdf/moli/issues/61).
