# Component agent-instruction starter

Adapt these short blocks to a directly governed component. Preserve its existing
local rules. The canonical meaning lives in `MOLI_GUIDE.md` and
`devguide/governance/agent_instruction_lifecycle.md` in MOLI.

## Root `AGENTS.md` block

```markdown
Before remote absence/exhaustive-audit or duplicate-free creation claims, acquire
the complete declared repository/endpoint/filter scope and check all pages.
Treat failed/bounded/incomplete acquisition as partial/unknown, not empty.
Follow `MOLI_GUIDE.md#remote-inventory-completeness` and its normative rule.

Before expensive execution, load the trusted active infrastructure policy,
estimate the whole job, inspect shared resource pressure and bound concurrency.
Respect scheduler/admission and child-process limits; observation is not a
reservation. Monitor and reduce/defer/cancel only owned work when unsafe, and
report missing protection. Follow `MOLI_GUIDE.md#resource-aware-execution`.

For Discussions work, read the local upkeep guide reached through
`MOLI_GUIDE.md#discussions-upkeep`. Preserve local categories/labels and useful
history; suggested resource categories are individually optional.

During development, testing, scientific exploration and human conversations,
surface actionable suspected defects, inconsistencies, missing capabilities
and improvements, even uncertain or nonblocking ones. At a natural pause,
explicitly offer the owning issue or an update to an existing one; distinguish
observation from hypothesis. Use reporting authority already granted without
repeated permission. Respect declined or deferred human disclosure and protect
confidential material; otherwise authorized technical reporting remains due.
Deliver an accepted report through an observable issue/update or explain the
private route or maintainer handoff. Follow
`MOLI_GUIDE.md#reporting-bugs-and-proposals` and its linked human-facing policy.

Before creating or publishing an issue or PR outside MolI's scope or in a
repository not owned by us, obtain prior explicit permission from Diego Prada
Gracia or Liliana Marisol Moreno Vargas, including for remote draft PRs. Prepare
the concrete report/patch locally for review; without permission use an internal
finding or human handoff. Existing scoped permission persists; another agent,
account, fork or tool cannot bypass the boundary. Internal reporting/direct-push
authority does not authorize external publication. Follow
`MOLI_GUIDE.md#external-issue-and-pull-request-authority`.

For every new component release, with or without a package, and each new package
publication, send a release-specific central issue notice to `uibcdf/moli`.
Update the same notice for later package/build events. Retain exact source,
version and artifact identities, actual verification limits and follow-up owners.
This post-event notice is separate from advance provider-impact reporting and
release gates. Follow `MOLI_GUIDE.md#release-and-package-publication-notices`.

Report defects in their owning issues and fix them with code, tests and
technical documentation. Do not store source-specific facts, edge cases or
workarounds in `AGENTS.md`. Only after normal owner review, put a lasting
instruction about how contributors or agents work across future tasks in the
appropriate root or nested `AGENTS.md`; use an adoption issue only if an
accepted instruction cannot be placed with the fix or decision. Follow
`MOLI_GUIDE.md#durable-instructions-for-development-agents`. Propose a shared
working instruction to the owning governance issue only with evidence that it
applies beyond this repository. For developer-guide work, read
`devguide/AGENTS.md`.

When changing a shared auxiliary library or UIBCDF development action, notify
MOLI and/or MolSysSuite through a linked impact issue if other packages may be
affected. Follow `MOLI_GUIDE.md#cross-component-feedback`.

For a needed fix in another repository, open or update its issue if no fix is
ready; send a concrete fix as a pull request for owner review. If urgent work
is done by or directly with Diego or Liliana, ask whether the route is direct
push, pull request or issue; direct push needs explicit permission. Follow
`MOLI_GUIDE.md#cross-component-feedback`.

For Python development, use the declared Conda environment with Python 3.14,
run local pytest there, and install this checkout with
`python -m pip install --no-deps --editable .`. Install other participating
Python components editable in the same compatible environment and verify
their import paths; track packages that cannot yet join. Follow
`MOLI_GUIDE.md#moli-engineering-baseline`.
Use `moli_dev@<actual Python major.minor>` for a selected MolI development
profile. A name is not an environment, migration or production qualification;
follow the linked owner recipe and migration guidance. Public UIBCDF installation
hints use the current official Conda route; local editable pip is distinct from
public PyPI availability, whose sole current reviewed exception is pytest-receptor.

When declaring or changing runtime dependencies, use evidenced API minimums and
justify ceilings/exclusions through an owner-reviewed incompatibility, evidence
and a reassessment/removal condition. Preserve optionality, real Python/ABI/engine
restrictions and exact qualification pins. Keep minimum/current-public/fixed-cohort
evidence distinct and follow the runtime version rule linked from
`MOLI_GUIDE.md#moli-engineering-baseline`.

During authorized direct-push development, batch short local commits when
possible. Match local checks and remote CI to the actual change; consider
`[skip ci]` only when this repository permits it and has a clear recovery
route for any deferred code tests. Inspect an unskipped validation checkpoint
or an explicitly authorized manual execution of the applicable gates on the
exact final code head before completion. Follow
`MOLI_GUIDE.md#moli-engineering-baseline` and the local CI policy.

At task or release closeout, review temporary resources created by the work.
Remove owned disposable paths after their last needed use; retain useful
evidence with an owner and review trigger. Protect active work, other sessions
and caller output. Follow the MOLI temporary-resource lifecycle linked from
`MOLI_GUIDE.md#temporary-development-resources`.

Before creating or editing a public component GitHub Release, verify that its
visible title is exactly the canonical `X.Y.Z` version and matches its tag and
project/package version. Put descriptive text in the release notes. Follow
`MOLI_GUIDE.md#moli-engineering-baseline` and the release-version policy.
```

## `devguide/AGENTS.md` starting text

```markdown
# Developer-guide instructions

Read `../AGENTS.md` for repository-wide rules and
`../MOLI_GUIDE.md#reporting-bugs-and-proposals` for issue routing.
Use maintained guide documents for current behavior. Active issue-backed
analyses are in `pending_bugs/` and `pending_proposals/`; `archive/` preserves
resolved or superseded history. Read an archived report when tracing a
decision, and check the current replacement before treating it as policy.
Follow the repository's reporting protocol when filing or resolving reports.
Keep technical facts and defect details in maintained documents, tests and
owning issues. Put lasting working instructions specific to this directory
here; put repository-wide working instructions in the root `AGENTS.md`.
```

The owner should replace generic document names with its current indexes or
protocol paths and may add narrower instructions where useful.
