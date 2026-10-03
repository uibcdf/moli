# MOLI repository instructions

Read `MOLI_GUIDE.md` before changing platform governance or a contract shared by
components. Use `moli.toml` to find accepted policies and their normative documents;
read the relevant decisions in `architecture_1.0/` for architectural work. Route
bugs and proposals to the owning GitHub issue as the guide requires.

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
