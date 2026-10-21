---
summary: Require Discussions with common categories and local extensions; track repository adoption.
issue: uibcdf/moli#23
status: partial
opened: 2026-09-26
closed:
verification: inspected
area: [governance, collaboration]
blocked_by: []
supersedes: []
---

# GitHub Discussions — decision and implementation

## Decision

Diego authorized proceeding with #23 on 2026-10-21. The accepted
[normative policy](../governance/github_discussions.md), registered in
`moli.toml`, keeps actionable work in owning issues and promotes discussion
outcomes to an issue or named versioned record with reciprocal links.

Diego subsequently clarified that **every MOLI repository must have Discussions
enabled**, with a common structure and component-specific additions. This
supersedes the optional-enablement decision in initial source `d7162f4` and its
early issue comments. Announcements, Q&A and Ideas are now the mandatory common
categories, with their specified formats/slugs; locally owned intake and other
purposeful categories extend them. Empty common categories remain. Each
repository records purpose, triage owner and destination. Confidentiality and
existing human-facing reporting authority apply. The registry and new-component
onboarding carry this corrected baseline.

MOLI enables Announcements, Q&A and Ideas for platform-level conversation;
Diego Prada owns triage through the maintainers. Component-local topics stay
with their owners. Organization-wide centralization was not selected because
repository ownership already provides routing. Network-dependent configuration
CI and a new remote-settings manifest schema were deferred until demonstrated
rollout evidence or actual drift justifies them. Desired configuration is written explicitly;
dated observed configuration remains separate.

This changes collaboration governance, not architecture or Nextia runtime.
The canonical `MOLI_GUIDE.md` already points contributors to `moli.toml` and
the reporting protocol; its bytes and component copies are unchanged.

## Observed inventory and owner adoption

The [normalized receipt](../evidence/github_discussions_23_20261021.json)
records read-only GitHub API observations before and after MOLI enablement,
including categories and existing discussion URLs. Owner: MOLI maintainers
under #23. Recheck on configuration or triage-owner change and before closure;
the receipt is a dated observation, not a continuously enforced claim.

| Repository | Observed state / disposition |
| --- | --- |
| MOLI | Initially disabled with no threads. Enabled by this task; GitHub created six defaults and no thread. Only the desired three categories and their forms are intended for use; browser configuration and rendered-form verification remain pending. |
| Sabueso | Enabled; six defaults plus Data sources, one existing welcome announcement (#63). [Sabueso #149](https://github.com/uibcdf/sabueso/issues/149) owns alignment, triage declaration and preservation of its source intake. |
| MolSysSuite | Enabled; six defaults, one welcome announcement (#2). [Suite #120](https://github.com/uibcdf/molsyssuite/issues/120) owns a compatible policy, settings and member adoption. MOLI changes no suite/member files or settings. |
| Praxis, Nextia, MOLI Agent, Recorda | Observed disabled in the initial inventory. This is now pending adoption, not compatible non-applicability: enable Discussions and establish the common three categories, local triage and any useful extensions. Nextia runtime implementation remains deferred; repository collaboration setup is separate. |

The two owner issues received advance notice before initial publication and
are updated with the maintainer's corrected requirement. MolSysSuite's own
repository participates as a direct component; its team owns the compatible
member rule and rollout. The original dated inventory is preserved as observed
history, not evidence of adoption or a continuing opt-out.

## MOLI configuration handoff

The authenticated GitHub public API permits enabling Discussions and reading
categories. Its inspected GraphQL mutation schema exposes no category CRUD;
the available GitHub connector has no category administration operation.
The computer-use inventory has no connected browsers, and requesting the
built-in browser reports `Browser is not available: iab`. This is a tool-access
block, not a missing repository permission: the API reports ADMIN access.

To finish through the repository's Discussions category editor:

1. Retain Announcements, Q&A and Ideas. Set their descriptions and formats to
   the [MOLI table](../governance/github_discussions.md#moli-configuration).
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

## Remaining acceptance / closeout

Local policy/registry/forms checks and exact-head hosted governance gates must
pass on delivery. Record their immutable source and native runs in #23.
Keep #23 open until MOLI's category editor and rendered forms have been checked
and the required direct-component adoption has evidence or an explicit linked
owner handoff. Update the receipt and track the four initially disabled direct
repositories as pending until their enabled state and baseline are verified.
Independent Sabueso and suite adoption retain their owning issues. Archive this
report and close the platform issue only when its stated rollout scope is
accounted for. Do not mark GitHub's unused defaults as already removed.

Task-owned raw API responses, downloaded inspection tooling and CI captures are
disposable after normalized evidence and issue handoff. Retain this receipt
under MOLI ownership with the review triggers above; protect unrelated sessions.
