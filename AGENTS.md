# MolI repository instructions

When writing or revising human-facing prose, use `MolI` for the platform and
`Moli` for the agent. Preserve exact technical identifiers and historical
quotations; follow `devguide/policies/naming_policy.md` for the standard and
examples.

Read `MOLI_GUIDE.md` before changing platform governance or a contract shared by
components. Use `moli.toml` to find accepted policies and their normative documents;
read the relevant decisions in `architecture_1.0/` for architectural work. Route
bugs and proposals to the owning GitHub issue as the guide requires.

During development, testing, scientific exploration and human conversations,
surface actionable suspected defects, inconsistencies, missing capabilities
and improvements, even uncertain or nonblocking ones. At a natural pause,
explicitly offer the owning issue or an update to an existing one; distinguish
observation from hypothesis. Use reporting authority already granted without
repeated permission. Respect declined or deferred human disclosure and protect
confidential material; otherwise authorized technical reporting remains due.
Deliver an accepted report through an observable issue/update or explain the
private route or maintainer handoff. Follow
`devguide/governance/reporting_protocol.md#human-facing-issue-feedback`.

When MOLI changes a platform rule that may affect MolSysSuite or its members,
record the required adoption and evidence in an existing or new
`uibcdf/molsyssuite` issue, linked to the MOLI decision. Leave changes to the
MolSysSuite repository and its member repositories to the MolSysSuite
development team. Keep cross-platform contracts and MOLI's own implementation
in `uibcdf/moli`; follow the ownership boundary in `MOLI_GUIDE.md`.

When a change to a shared auxiliary library or UIBCDF development action may
affect other packages, link its provider issue from an impact issue in MOLI,
MolSysSuite, or both according to the affected consumers. Follow
`devguide/governance/cross_component_feedback.md` before publishing the provider
change or starting consumer rollout when the impact is known in advance.

For authorized direct-push development, group short local commits when possible
and choose local checks and remote CI according to the change. Consider
`[skip ci]` only for a locally checked push permitted by the repository's CI
policy, with any deferred code tests recovered before claiming completion or
release. Verify the applicable gates on the exact head through an ordinary
unskipped run or an explicitly authorized manual run. A skipped run is not
passing evidence. Follow
`devguide/policies/python_ci_policy.md#validation-during-direct-push-development`.

For a needed fix in another repository, use its issue when there is no ready
fix, or propose a ready fix through a pull request for owner review. If urgent
work is being done by or directly with Diego or Liliana, ask them whether to
use a direct push, pull request or issue; direct push needs explicit permission.
Follow `devguide/governance/cross_component_feedback.md` and keep shared-provider
impact notices separate from the provider review route.

At task or release closeout, review temporary resources created by the work.
Remove owned disposable paths after their last needed use; retain useful
evidence with an owner and review trigger. Protect other sessions, active
worktrees and caller outputs, and report cleanup failures. Follow
`devguide/governance/temporary_resource_lifecycle.md`.

Before creating or editing a public component GitHub Release, verify that its
visible title is exactly the canonical `X.Y.Z` version and matches its tag and
project/package version; put descriptive text in the release notes. Follow
`devguide/policies/release_version_policy.md#github-release-title`.

Report and fix defects through their owning issues, code, tests and technical
documentation. Do not turn a source-specific fact, edge case or workaround
into an `AGENTS.md` rule. Only a lasting instruction about how agents or
contributors work across future tasks belongs in the correctly scoped root
or nested `AGENTS.md`, after normal owner review. Follow
`devguide/governance/agent_instruction_lifecycle.md`; propose cross-component
adoption only for an accepted working instruction with shared evidence. For
work under `devguide/`, also read `devguide/AGENTS.md`.

Validate this governance repository with
`python devtools/scripts/validate_governance.py`.
`devtools/scripts/check_repository.py` checks MOLI component repositories; it is
not the validator for this repository.
