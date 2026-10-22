---
summary: Require common Discussions categories; verify seven roots and hand off suite member adoption.
issue: uibcdf/moli#23
status: resolved
opened: 2026-09-26
closed: 2026-10-22
verification: inspected
area: [governance, collaboration]
blocked_by: []
supersedes: []
---

# GitHub Discussions — decision and implementation

## Final resolution and verified scope

Final authenticated API inventory on **2026-10-22 UTC** (2026-10-21 in
America/Mexico_City) verifies all seven registered platform/root repositories
with Discussions enabled and the common Announcements, Q&A and Ideas
names/slugs, expected descriptions and answerable Q&A. General, Polls and
Show and tell are absent. Sabueso additionally retains Data sources. The
[normalized receipt](../evidence/github_discussions_23_20261021.json) preserves
both initial observations and this final state with exact source heads,
category IDs/timestamps, template trees and owner-issue state.

| Repository | Final configuration and ownership |
| --- | --- |
| MolI | Three common categories; Q&A/Ideas forms present. Diego owns triage and reports the format/form-preview checklist completed. |
| Sabueso | Common three plus original Data sources; its form/registry blob identities and welcome announcement #63 survive. [#149](https://github.com/uibcdf/sabueso/issues/149) closed with its receipt. |
| Praxis | Common three; [#12](https://github.com/uibcdf/praxis/issues/12) closed. |
| Nextia | Common three; [#4](https://github.com/uibcdf/nextia/issues/4) closed. Runtime implementation remains deferred. |
| Moli | Common three; [#3](https://github.com/uibcdf/moli-agent/issues/3) closed. Repository identifier remains `uibcdf/moli-agent`. |
| Recorda | Common three; [#28](https://github.com/uibcdf/recorda/issues/28) closed. |
| MolSysSuite root | Common three; original welcome announcement #2 survives. Diego reports the format checklist completed. [#120](https://github.com/uibcdf/molsyssuite/issues/120) stays open for suite-owned policy and member rollout. |

Repository maintainers retain triage accountability until explicit named
assignment under the accepted policy. Each category's description defines
its purpose; actionable work goes to the owning issue and durable decisions
to issues or named versioned records with reciprocal links. Sabueso keeps its
existing source-registry disposition route. No extra component category or
runtime capability is invented to fill an empty forum.

### Evidence boundaries

Diego performed the browser work and replied with each repository's completion
after the supplied checklists. These are **maintainer-reported UI checks** of
actual formats and, where present, form previews. The CLI independently
verified API-visible settings. `isAnswerable` proves Q&A answerability; a
category name or false boolean does not prove Announcement format. No
independent browser inspection by the CLI is claimed.

The final template inventory contains MolI's Q&A/Ideas forms and Sabueso's
Data sources form; the other inspected roots have no local discussion-template
directory. No test/welcome thread was created. Only the two original welcome
announcements remain. Settings changes do not qualify ingestion, a generated
page, scientific execution, package releases or notification/runtime features.

### Delegated work and completion

The platform rule, MolI implementation, five component adoption issues and
MolSysSuite's root configuration are complete. MolSysSuite's team owns its
versioned policy, future-repository route and member inventory/rollout/evidence
through **suite #120**, which remains open. The central task changes no
suite/member source or settings; Diego made the root changes manually. Root
adoption is not a claim that suite members are configured.

This explicit handoff satisfies #23's platform-boundary coordination scope;
member implementation is not absorbed into the MolI task. The earlier
optional/disabled-compatible decision is superseded by the maintainer's
required baseline, as retained in the history below. Final documentary
source, applicable exact-head native CI and temporary-resource retirement
are recorded in #23's closeout comment. No canonical guide bytes changed.

The receipt and archived decision remain under MolI ownership. Review them
when category, triage owner, form or policy changes, and before extending an
adoption claim. Raw API replies and published CI inspection tooling are
retired after final verification and issue handoff; unrelated work is protected.

## Decision and initial implementation history

The sections below retain the initial plan, observations and acceptance
criteria. They describe the earlier checkpoints; the final resolution above
supersedes their pending browser/configuration statements.

### Accepted decision

Diego authorized proceeding with #23 on 2026-10-21. The accepted
[normative policy](../governance/github_discussions.md), registered in
`moli.toml`, keeps actionable work in owning issues and promotes discussion
outcomes to an issue or named versioned record with reciprocal links.

Diego subsequently clarified that **every MolI repository must have Discussions
enabled**, with a common structure and component-specific additions. This
supersedes the optional-enablement decision in initial source `d7162f4` and its
early issue comments. Announcements, Q&A and Ideas are now the mandatory common
categories, with their specified formats/slugs; locally owned intake and other
purposeful categories extend them. Empty common categories remain. Each
repository records purpose, triage owner and destination. Confidentiality and
existing human-facing reporting authority apply. The registry and new-component
onboarding carry this corrected baseline.

MolI enables Announcements, Q&A and Ideas for platform-level conversation;
Diego Prada owns triage through the maintainers. Component-local topics stay
with their owners. Organization-wide centralization was not selected because
repository ownership already provides routing. Network-dependent configuration
CI and a new remote-settings manifest schema were deferred until demonstrated
rollout evidence or actual drift justifies them. Desired configuration is written explicitly;
dated observed configuration remains separate.

This changes collaboration governance, not architecture or Nextia runtime.
The canonical `MOLI_GUIDE.md` already points contributors to `moli.toml` and
the reporting protocol; its bytes and component copies are unchanged.

## Initial observed inventory and owner adoption — historical

The [normalized receipt](../evidence/github_discussions_23_20261021.json)
records read-only GitHub API observations before and after MolI enablement,
including categories and existing discussion URLs. Owner: MolI maintainers
under #23. Recheck on configuration or triage-owner change and before closure;
the receipt is a dated observation, not a continuously enforced claim.

| Repository | Observed state / disposition |
| --- | --- |
| MolI | Initially disabled with no threads. Enabled by this task; GitHub created six defaults and no thread. Only the desired three categories and their forms are intended for use; browser configuration and rendered-form verification remain pending. |
| Sabueso | Enabled; six defaults plus Data sources, one existing welcome announcement (#63). [Sabueso #149](https://github.com/uibcdf/sabueso/issues/149) owns alignment, triage declaration and preservation of its source intake. |
| MolSysSuite | Enabled; six defaults, one welcome announcement (#2). [Suite #120](https://github.com/uibcdf/molsyssuite/issues/120) owns a compatible policy, settings and member adoption. MolI changes no suite/member files or settings. |
| Praxis, Nextia, Moli, Recorda | Observed disabled in the initial inventory. This is now pending adoption, not compatible non-applicability: enable Discussions and establish the common three categories, local triage and any useful extensions. Nextia runtime implementation remains deferred; repository collaboration setup is separate. |

The two owner issues received advance notice before initial publication and
are updated with the maintainer's corrected requirement. MolSysSuite's own
repository participates as a direct component; its team owns the compatible
member rule and rollout. The original dated inventory is preserved as observed
history, not evidence of adoption or a continuing opt-out.

## Initial browser handoff — completed

The authenticated GitHub public API permits enabling Discussions and reading
categories. Its inspected GraphQL mutation schema exposes no category CRUD;
the available GitHub connector has no category administration operation.
The computer-use inventory has no connected browsers, and requesting the
built-in browser reports `Browser is not available: iab`. This is a tool-access
block, not a missing repository permission: the API reports ADMIN access.

To finish through the repository's Discussions category editor:

1. Retain Announcements, Q&A and Ideas. Set their descriptions and formats to
   the [MolI table](../governance/github_discussions.md#moli-configuration).
   Verify Announcements actually uses Announcement format and Q&A uses
   Question and answer; the names do not prove these settings.
2. Recheck live thread counts, then remove unused General, Polls and Show and
   tell. If content has arrived, move it to an appropriate retained category
   using GitHub's category-retirement flow; preserve thread URLs/history.
3. Open the new Q&A and Ideas forms on the delivered default branch; check
   required fields, routing links and confidentiality text. No public test
   thread or welcome announcement is needed.
4. Read back enabled state, exact categories/slugs/descriptions and Q&A
   answerability through the API; record the human/UI observation of actual
   announcement format/access and form rendering with its date.

## Initial acceptance / closeout criteria — satisfied or handed off

Local policy/registry/forms checks and exact-head hosted governance gates must
pass on delivery. Record their immutable source and native runs in #23.
Keep #23 open until MolI's category editor and rendered forms have been checked
and the required direct-component adoption has evidence or an explicit linked
owner handoff. Update the receipt and track the four initially disabled direct
repositories as pending until their enabled state and baseline are verified.
Independent Sabueso and suite adoption retain their owning issues. Archive this
report and close the platform issue only when its stated rollout scope is
accounted for. Do not mark GitHub's unused defaults as already removed.

Task-owned raw API responses, downloaded inspection tooling and CI captures are
disposable after normalized evidence and issue handoff. Retain this receipt
under MolI ownership with the review triggers above; protect unrelated sessions.
