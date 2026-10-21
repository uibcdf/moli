# GitHub Discussions

This policy is accepted under [MOLI #23](https://github.com/uibcdf/moli/issues/23)
for MOLI and its directly governed components, including the MolSysSuite
repository. MolSysSuite's team implements the common baseline for its member
repositories through its own versioned policy and adoption process. This
document does not change the platform architecture or establish a scientist-facing
agent runtime.

## Purpose and ownership

Use Discussions for usage questions, announcements and early design conversation
that has not yet identified actionable work. Use the lowest repository that owns
the subject. Cross-component MOLI questions belong in MOLI; suite-internal
questions belong in MolSysSuite. Link an existing conversation instead of opening
parallel threads. Organization-wide centralization is not required.

An actionable suspected bug, missing capability or concrete improvement belongs
in an owning issue even when uncertain or nonblocking. Follow the
[reporting protocol](reporting_protocol.md), including its human-facing review
and disclosure authority. Ideas is not a holding queue that bypasses that duty.

Every MOLI repository must have Discussions enabled, including component
repositories that are still scaffolds or have little activity. The common
structure below is a platform baseline; an individual component does not opt
out because it has no discussions yet. New directly governed repositories
enable it during onboarding; existing repositories track adoption under #23.

Each repository records:

- a useful purpose for each category;
- a named maintainer or maintained team responsible for triage;
- the destination for actionable work and durable decisions.

The repository maintainers are accountable for triage until they name a
specific maintainer or maintained team; missing assignment is work to resolve,
not permission to disable the channel. There is no response-time promise.
Recheck ownership when repository maintainers change. Before retiring an
additional category, inspect its threads and preserve useful content, decisions
and links in an appropriate destination.

## Categories

All repositories keep the same three baseline categories, names/slugs and
formats. Adapt descriptions, examples and forms to the repository's subject;
the names alone do not configure GitHub's format.

| Category | GitHub format | Purpose and triage destination |
| --- | --- | --- |
| Announcements / `announcements` | Announcement | Maintainers announce an already recorded release, contract or policy update, linking its authoritative record. GitHub restricts new announcement threads to maintain/admin roles. |
| Q&A / `q-a` | Question and answer | Usage and interpretation questions. Mark a useful answer; route any actionable finding to its owning issue and any lasting clarification to maintained documentation. |
| Ideas / `ideas` | Open-ended discussion | Early questions without concrete actionable work. Triage to an owning issue when work becomes concrete; record a decision in that issue or a named versioned record. |

Components may add their own categories and discussions on top of that baseline.
An additional intake category requires a category form, a triage owner and a
named durable registry or issue destination. Document its disposition states
and conversion rule locally. Other additional categories also need a purpose,
owner and destination. They complement the common categories rather than
renaming, replacing or removing them.

Remove unused default categories such as General, Polls and Show and tell.
For these additional categories, a default name or an empty channel is not a
reason to retain it. The three baseline categories remain even when empty.
Inspect content before moving threads when removing a category. Do not delete
discussion history just to make the configuration match.

Sabueso's Data sources is an existing intake case: its owner maintains the form,
source registry, statuses and generated page. MOLI does not take over those
implementation details. Keep that intake and its useful links when aligning
the other categories.

## From conversation to a durable outcome

At triage or when a thread reaches a conclusion:

1. Search for the owning issue or existing versioned record. Open/update the
   issue for actionable work, including the observation, uncertainty, use case
   and acceptance scope. Conversion through GitHub is optional.
2. Record an accepted, deferred or rejected decision with its date and reason
   in that issue or a named versioned record. For deferral, include a concrete
   revisit trigger; a later change must preserve the previous disposition.
3. Link the original discussion URL from the durable record and link the
   destination back from the discussion. Close or mark the discussion as
   answered when appropriate, explaining the destination or disposition.

A discussion answer, poll, closure or announcement does not by itself accept a
platform contract or prove an implemented fix. Apply the normal owner decision,
review, tests and publication requirements. Do not leave the only decision in
a thread; a short usage answer needs no new issue unless actionable work or a
lasting change is identified.

Public discussions have the same confidentiality limits as public issues.
Use sanitized examples; do not publish confidential pilot projects, unpublished
scientific results, credentials or restricted material. Use the private security
or maintainer route where required.

Agents may read discussions and cite their URLs. Summaries preserve the source
link and distinguish observations, suggestions and accepted decisions. Reading
or summarizing a thread does not authorize posting, subscriptions, external
disclosure or implementation. Act within the task's existing authority and the
reporting protocol; no automatic notifications or runtime integration follows.

## MOLI configuration

MOLI enables Discussions for platform questions, policy interpretation and
maintainer announcements. Diego Prada (`dprada`) owns triage, with delegation
through the repository's maintainers. The intended categories are:

| Name / slug | Format | Description |
| --- | --- | --- |
| Announcements / `announcements` | Announcement | Maintainer updates on MOLI architecture, policies and cross-component contracts; link the authoritative record. |
| Q&A / `q-a` | Question and answer | Questions about MOLI policies and component boundaries; actionable findings go to owning issues. |
| Ideas / `ideas` | Open-ended discussion | Early cross-component design questions; concrete work goes to owning issues and decisions to versioned records. |

Q&A and Ideas have forms under `.github/DISCUSSION_TEMPLATE/`, named after
their category slugs. The MOLI issue board is the destination for platform work;
accepted rules live in `moli.toml` and their linked normative documents.
Component-local work is handed to its owning issue. This written table declares
the desired configuration; it does not claim to enforce the remote settings.

The repository keeps a dated observed inventory and adoption state in the
[issue-backed implementation record](../pending_proposals/github_discussions.md).
Review the live enabled flag, category names/slugs, descriptions, Q&A
answerability, announcement format/access and form rendering before claiming
configuration complete. Record the observer and date. GitHub's category editor
is needed for settings not exposed through its public API.

No network-dependent CI check or new manifest schema for remote categories is
introduced. The written declaration, checked-in forms and explicit readback
record the initial configuration without claiming automatic enforcement.
Reconsider an automated read-only drift check after the multi-repository
baseline rollout provides operational evidence, or when actual drift warrants it;
such a check must distinguish desired settings from observed evidence.

See GitHub's documentation for [category formats and management](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions)
and [category forms](https://docs.github.com/en/discussions/managing-discussions-for-your-community/creating-discussion-category-forms).
