---
summary: Deliver human-facing contributor issue feedback separately from the runtime pilot.
issue: uibcdf/moli#34
status: partial
opened: 2026-10-01
closed:
verification: inspected
area: [governance, issue-feedback]
blocked_by: []
supersedes: []
---

# Human-facing issue feedback

## Accepted contributor instruction

The maintainer selected the contributor-instruction portion of #34 on
2026-10-21. The [reporting protocol](../governance/reporting_protocol.md#human-facing-issue-feedback)
owns the rule; root `AGENTS.md`, the canonical `MOLI_GUIDE.md`, registry,
component starter and onboarding checklist carry its actionable route.

Surface actionable suspected defects, inconsistencies, missing capabilities
and improvements, including uncertain and nonblocking findings. Explicitly
offer their owning issue at a natural pause, preserve existing reporting
authority without repeated permission, respect declined/deferred human
disclosure and protect confidential material. Deliver accepted reports through
an observable issue/update or explain the private route or maintainer handoff.
Ordinary technical reporting whose disclosure is otherwise authorized remains
due. The rule is a lasting contributor action under
[the instruction lifecycle](../governance/agent_instruction_lifecycle.md).

MolSysSuite's independently accepted antecedent is
[suite #65](https://github.com/uibcdf/molsyssuite/issues/65), with
[central and sixteen-member evidence](https://github.com/uibcdf/molsyssuite/blob/37401257a501b2ea09cc5482988d2468781a950f/devguide/rollouts/human_facing_feedback_65_20261010.json).
MOLI records the platform decision there; MolSysSuite owns any further member
work. No suite or member file is edited by this task.

## Direct-component delivery

The registry identifies five direct repositories with vendored guide delivery:
Sabueso, Praxis, Nextia, MOLI Agent and Recorda. Each owner-local issue records
the byte-identical guide and a short root action. Recorda also
pins its shared-core CI checkout to the reviewed MOLI source supplying that
guide, so its exact-copy gate remains consistent. Preserve
local instructions and existing nested routing; no nested rule is needed for
a repository-wide action. Diego, the principal developer, explicitly accepted
direct pushes of these prepared changes on 2026-10-21 instead of component PRs.
That authorization resolves the earlier automatic-approval publication block;
the [owning issue records the route](https://github.com/uibcdf/moli/issues/34#issuecomment-6324906858).
A passing candidate check alone is not evidence of default-branch adoption.

The [delivery receipt](../evidence/human_facing_feedback_34_20261021.json)
records immutable bases/heads, guide and patch digests, owner-local issues and
applicable checks. [MOLI PR #72](https://github.com/uibcdf/moli/pull/72) was the
initial review surface, with canonical source
`1131e16c42b339b28ef8feb987bca40b9f71e681`; its implementation commits are now
on MOLI main at `80e7e00396321cd578e2be30e4a68fb2948f3468`, and GitHub
automatically recognized the PR as integrated. All five component commits
below were pushed normally to main and pass their native administrative
gates. The five owner issues are closed/completed. Sabueso was rebased onto a separately published
documentation advance without changing that work or the prepared guide/rule.

| Repository | Owner-local issue | Delivery state |
| --- | --- | --- |
| Sabueso | [#147](https://github.com/uibcdf/sabueso/issues/147) | Main [e6c1cff](https://github.com/uibcdf/sabueso/commit/e6c1cff640887c9cf7d3b459a68bb68233292e95); [native governance passes](https://github.com/uibcdf/sabueso/actions/runs/39663832691). |
| Praxis | [#11](https://github.com/uibcdf/praxis/issues/11) | Main [55b7d6d](https://github.com/uibcdf/praxis/commit/55b7d6d2f9f7495a148ebe4d6bbc7acbffd9a512); [native governance passes](https://github.com/uibcdf/praxis/actions/runs/39663837727). |
| Nextia | [#3](https://github.com/uibcdf/nextia/issues/3) | Main [32d12e2](https://github.com/uibcdf/nextia/commit/32d12e20fae26f00a523d0ed4812e46def8a64e9); [native governance passes](https://github.com/uibcdf/nextia/actions/runs/39663842957). |
| MOLI Agent | [#2](https://github.com/uibcdf/moli-agent/issues/2) | Main [08d0e2b](https://github.com/uibcdf/moli-agent/commit/08d0e2b809e7e5c46add5ee554ae9528831f7454); [native governance passes](https://github.com/uibcdf/moli-agent/actions/runs/39663849172). |
| Recorda | [#27](https://github.com/uibcdf/recorda/issues/27) | Main [b455ff5](https://github.com/uibcdf/recorda/commit/b455ff5ec6fee206f8c077cbac45712f0b6c704b), including matching CI pin; [native quality passes](https://github.com/uibcdf/recorda/actions/runs/39663852969/job/119443576809). |

The source-head [governance run](https://github.com/uibcdf/moli/actions/runs/39661670803)
passes all 54 administrative tests and its executed governance/archive-tag
steps. Default-branch coverage publication is inapplicable to that PR event.
The initial [hosted guide audit](https://github.com/uibcdf/moli/actions/runs/39661609436)
failed specifically on the five previous default-branch guide copies before
delivery; the combined local candidate audit passed. After delivery, freshly
fetched main branches have the exact canonical guide and preserved original
root/nested instructions. The implementation-head
[main governance and coverage](https://github.com/uibcdf/moli/actions/runs/39663979062)
passes all 54 tests and its mandatory executed steps. The final
[full hosted guide audit](https://github.com/uibcdf/moli/actions/runs/39663979006)
passes against all five actual component default branches. All complete
captures have their member digests checked. Recorda's whole-workflow capture
is incomplete while separate runtime jobs await execution; its completed
administrative job and logs were checked through native GitHub APIs, including
the reviewed-core checkout and exact-guide check. Other component runtime CI
retains its own scope and conclusions. The instruction rollout is complete;
no scientific or installed-package qualification is inferred.

The final documentation-head governance and temporary-resource retirement
are recorded in the owning #34 closeout comment after this receipt is committed.
Associated infrastructure is outside this five-component rollout; separately
assess any linked guide obligation without claiming it adopted here.

## Review cases for the instruction

These are policy review cases, not demonstrations of a scientist-facing agent.

| Situation | Required contributor action |
| --- | --- |
| Missing capability while the task can continue | Explain the need and useful outcome, offer the owning issue at a natural pause. |
| Uncertain scientific discrepancy | Preserve observation versus hypothesis; offer investigation without certifying a software defect or Evidence. |
| Existing authorized reporting scope | Surface the finding and file/update under that authority without another permission request. |
| Person declines or defers project disclosure | Respect the decision and retain only an authorized sanitized disposition; do not publish the material elsewhere. |
| Confidential or exploitable finding | Use the private route or safe minimal reproduction; explain a required maintainer handoff. |
| Existing owner issue | Add concrete evidence there and provide its observable reference; avoid a duplicate. |
| Issue closed without project-compatible fix | Do not infer usability or trigger a scientific retry from closure alone. |

## Remaining #34 acceptance

Keep #34 open for the scientist-facing pilot: editable proposals for missing capability and
suspected defect, uncertain/nonblocking findings, declined disclosure,
deduplication, safe project linkage, coding-agent handoff and opt-in return
only after verified availability in a compatible environment. MOLI Agent
remains optional; neither an instruction rollout nor issue closure implements
subscriptions, notification, automatic retry or scientific certification.

## Alternatives

Waiting for a runtime implementation would leave a useful contributor action
undelivered. Reusing suite adoption as MOLI acceptance would cross the
delegation boundary. Copying full policy into every `AGENTS.md` would create
divergent instructions. This bounded change accepts the central rule and
offers concise component adoption under the principal developer's accepted
direct-push route, with explicit residual work.
