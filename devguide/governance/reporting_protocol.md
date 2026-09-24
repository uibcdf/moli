# Reporting Protocol

The issue-feedback commitment below applies to everyone using, developing,
maintaining or operating a MOLI component or UIBCDF support tool, including
MolSysSuite members, pytest-receptor, gh-run-receptor, the Conda build/upload
action and the Sphinx-to-Pages action. The
devguide queue and archive mechanics in this document are normative for repositories
directly governed by MOLI; MolSysSuite maintains its compatible member lifecycle.

## Universal issue-feedback commitment

When you find a bug, a missing or limiting capability, an improvement opportunity,
or a proposed new feature, communicate it through the GitHub issue in the repository
that owns the behavior or shared contract. Open an issue or add the concrete finding
to an existing one. This applies to users, collaborators, developers, maintainers and
agents, whether the finding concerns their own repository or another component.
If you cannot open an issue, ask the responsible maintainer to record it and provide
the evidence needed for triage.

Do not leave an actionable finding only in a private chat, a local workaround, a code
comment or a downstream repository. Describe what was observed or needed, why it
matters, and a reproduction or concrete use case when available. Cross-link consumer
and provider issues where both have work to do. Reporting creates a durable feedback
record; maintainers decide priority and scope, so an issue is not a promise of
immediate implementation.

Keep confidential data out of public issues. Report exploitable security findings
through the repository's private security channel first; create or link a public
issue only when disclosure is safe.

## Universal lifecycle

For bugs and proposals that require durable devguide analysis:

```text
GitHub issue
    ↓
pending devguide report
    ↓
analysis / implementation / verification
    ↓
resolution
    ↓
archive
```

**Every queued report must have an issue in the repository that owns the work.**
Small findings may need only an issue or an update to an existing issue.

GitHub issue references are the stable cross-repository identity. Do not use a path into a sibling repository's `devguide/` as an external identifier.

## Ownership

- one-component work → owning component issue;
- provider limitation → provider issue, cross-linked from consumer work;
- shared contract between MOLI components → `uibcdf/moli` issue;
- MolSysSuite-internal work → MolSysSuite governance;
- cross-boundary MolSysSuite ↔ other MOLI component contract → `uibcdf/moli`.

A platform issue may link local implementation issues; it does not absorb their local code/test analysis.

## Queues

Directly governed repositories provide:

- `devguide/pending_bugs/`;
- `devguide/pending_proposals/`;
- `devguide/archive/`;
- `devguide/templates/report.md`.

Not every small issue requires a report. Create a report when durable analysis, alternatives, measurements, migration reasoning, or multi-session context is useful.

## Front matter

Queued and archived reports use:

```yaml
---
summary: One-line theme.
issue: uibcdf/<owning-repository>#1
status: open
opened: YYYY-MM-DD
closed:
verification: asserted
area: [governance]
blocked_by: []
supersedes: []
---
```

For bugs, add:

```yaml
severity: medium
```

Allowed statuses:

- open: `open`, `active`, `blocked`, `partial`;
- closed: `resolved`, `withdrawn`, `superseded`.

Verification vocabulary:

- `reproduced` — executed and observed;
- `measured` — supported by recorded measurements;
- `inspected` — verified by source/configuration inspection;
- `upstream` — confirmed outside the owning repository;
- `asserted` — believed but not yet independently checked.

Domain-specific scientific evidence vocabulary remains local and must not be confused with this development-report verification field.

## Filing

1. Decide ownership.
2. Open the owning GitHub issue.
3. If durable analysis is needed, create a report from the shared template in the appropriate queue.
4. Record What / How / Why, alternatives, and acceptance criteria.
5. Cross-link provider/consumer or platform issues where applicable.

## Resolution

When resolved, withdrawn, or superseded:

1. update the report status and `closed` date;
2. record the decision/fix and verification;
3. move the report to `devguide/archive/`;
4. close/synchronize the GitHub issue with the durable outcome.

**Archive, never silently delete meaningful decision history.**

## Confidentiality

Public reporting must not expose confidential DiscoveryProjects, proprietary Protocols, molecular Candidates, unpublished Evidence, credentials, or restricted data. Use sanitized reproductions and controlled references.

## Exceptions

A repository may use stricter local reporting machinery if the common meanings above remain intact. Any intentional incompatibility requires a MOLI issue documenting rationale and an exit condition.
