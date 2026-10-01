# Durable instructions for development agents

This policy applies to MOLI's directly governed repositories. MolSysSuite
remains responsible for instructions and rollout within its member repositories;
its platform-facing work follows MOLI's shared-contract and feedback boundary.

## From a lesson to an instruction

After a defect, failed workflow, or difficult investigation, ask whether the
lesson is a reusable rule for future contributors and agents. A one-off symptom
still needs its owning issue, fix, and appropriate regression guard. Put an
accepted, lasting behavior rule in the correctly scoped `AGENTS.md` in the same
change as the fix or governance decision. If adoption cannot happen in that
change, open an owned follow-up issue and link it; a chat, issue comment, or
agent memory is not the final instruction. `AGENTS.md` complements tests and
technical documentation; it does not replace them.

Keep instructions short and actionable. State the action, its trigger, and the
authoritative policy or local evidence. Revisit a rule when its underlying
decision changes, and remove or revise obsolete instructions explicitly.

## Scope and placement

- MOLI policy and `MOLI_GUIDE.md` own shared contracts and development rules.
- A repository's root `AGENTS.md` states repository-wide actions and points to
  authoritative detail, including the guide and issue-reporting rule.
- A nested `AGENTS.md` refines behavior only for its directory subtree. Put a
  `devguide/`-specific rule in `devguide/AGENTS.md`; put a rule governing all
  development in the root file. Do not copy entire policies into either file.
- Apply this placement test to *any* nested `AGENTS.md`, not only `devguide/`.
  A more local instruction must not silently contradict its parent or MOLI.

For example, a reusable rule to report a provider limitation belongs in the
root file and links to `MOLI_GUIDE.md`. A rule to consult active report queues
before interpreting an old archived analysis belongs in `devguide/AGENTS.md`
and links to that repository's reporting protocol and indexes.

## Feedback beyond one repository

Report every actionable defect or proposal to its owning issue under the
[reporting protocol](reporting_protocol.md). When a *local instruction* might
help another component, raise a separate adoption proposal at the lowest
governance owner: `uibcdf/moli` for direct components or a cross-MolSysSuite
boundary, `uibcdf/molsyssuite` for rules shared only among suite members.
Link the incident, the local rule, evidence, candidate adopters, and known
exceptions. Link issues at both levels only if each level has distinct work.
The owner decides whether to adopt; do not spread a rule by copying it first.

## Adoption and checks

Each direct repository with a `devguide/` keeps a root `AGENTS.md` and a
`devguide/AGENTS.md`. The root points to its guide and this lifecycle. The
nested file points back to the root, identifies active guidance/queues and
archive/history, and routes findings to the repository's reporting protocol.
The [templates](../templates/README.md) provide concise starting text.
The [new-component onboarding guide](new_component_onboarding.md) requires
these files from the first commit of a directly governed repository.

`devtools/scripts/check_repository.py` checks file presence and stable links
for components. MOLI uses `validate_governance.py` for its own files. These
checks do not judge whether a lesson is sound, correctly scoped, or well
written; review of those decisions remains with the owning repository.

Adoption evidence and justified exceptions are recorded in
[the adoption inventory](agent_instruction_adoption.md).
