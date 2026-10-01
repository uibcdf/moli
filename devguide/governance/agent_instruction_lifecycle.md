# Durable instructions for development agents

This policy applies to MOLI's directly governed repositories. MolSysSuite
remains responsible for instructions and rollout within its member repositories;
its platform-facing work follows MOLI's shared-contract and feedback boundary.

## From a finding to a working instruction

An incident does not require an `AGENTS.md` change merely because it taught us
something. First report an actionable defect or need in its owning issue and
put the correction in code, a regression test, and the relevant technical or
user documentation as applicable. Source behavior, scientific facts, API
contracts, edge cases, and local workarounds belong there, not in agent
instructions. For example, a UniProt search returning inactive entries and
causing an OMA error
is a connector defect to fix and test; the fact about those entries is not an
`AGENTS.md` rule.

Consider `AGENTS.md` only when the incident exposes a **lasting instruction
about how contributors or agents should work** across future tasks in the
file's scope, and existing policy, tests, and technical documentation do not
already provide a sufficient instruction. It must be expressible as an action
with a trigger and a link to authoritative detail. The repository owner
adopts it through the normal review process; routine triage does not require
asking a human whether every bug should become an `AGENTS.md` rule. If such a
working instruction is accepted, place it in the correctly scoped `AGENTS.md`
with the fix or governance decision. Open an owned adoption follow-up only if
that *accepted instruction* cannot be placed in the same change. An issue
comment, chat, or agent memory is not its final home. `AGENTS.md` complements
tests and technical documentation; it does not replace them.

This classification concerns `AGENTS.md` only. It does not waive the
issue-feedback obligation or any human review required before publishing a
project-derived report.

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

For example, if agent handoffs repeatedly lose provider limitations in chat,
the repository-wide instruction to report them in the owning issue belongs in
the root file and links to `MOLI_GUIDE.md`. An instruction to consult active
report queues before interpreting an old archived analysis belongs in
`devguide/AGENTS.md` and links to that repository's reporting protocol and
indexes. Neither file is a catalog of provider-specific bugs or scientific
facts.

## Feedback beyond one repository

Report every actionable defect or proposal to its owning issue under the
[reporting protocol](reporting_protocol.md). Raise an instruction-adoption
proposal only after a local **agent working instruction** has been accepted
and there is evidence that the same working problem could affect another
component. Route that proposal to the lowest governance owner:
`uibcdf/moli` for direct components or a cross-MolSysSuite boundary,
`uibcdf/molsyssuite` for rules shared only among suite members.
Link the incident, the local rule, evidence, candidate adopters, and known
exceptions. Link issues at both levels only if each level has distinct work.
The owner decides whether to adopt; do not spread a rule by copying it first.
An ordinary provider-specific defect needs its provider issue, not a parallel
governance issue about agent instructions.

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
checks do not judge whether a candidate working instruction is sound,
correctly scoped, or well written; review remains with the owning repository.

Adoption evidence and justified exceptions are recorded in
[the adoption inventory](agent_instruction_adoption.md).
