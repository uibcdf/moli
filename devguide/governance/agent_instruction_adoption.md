# Agent-instruction adoption inventory

This inventory tracks MOLI #20 for repositories directly governed by MOLI.
The normative rule is [agent_instruction_lifecycle.md](agent_instruction_lifecycle.md).
The listed evidence must be verified against each repository's current `main`
before marking it adopted. A pending entry is a tracked migration, not an
exception. MolSysSuite owns instructions for its member repositories.

| Repository | Root and `devguide/` instructions | Evidence or next step |
| --- | --- | --- |
| `uibcdf/moli` | In progress | Pilot: root `AGENTS.md`, `devguide/AGENTS.md`, governance validator. |
| `uibcdf/sabueso` | Pending | Adapt the root lesson rule and add `devguide/AGENTS.md` without losing Sabueso-specific guidance. |
| `uibcdf/praxis` | Pending | Add root lesson rule and `devguide/AGENTS.md`. |
| `uibcdf/nextia` | Pending | Add root lesson rule and `devguide/AGENTS.md`. |
| `uibcdf/moli-agent` | Pending | Add root lesson rule and `devguide/AGENTS.md`. |
| `uibcdf/molsyssuite` | Delegated | MOLI platform-boundary feedback applies; [MolSysSuite #66](https://github.com/uibcdf/molsyssuite/issues/66) owns member adoption and the new-member starter kit. |

Acceptance requires an owner-local root rule, a scoped developer-guide rule,
and a passing mechanical check for each direct, non-delegated repository.
Local repository-specific exceptions must name their owning issue and exit
condition here; none is assumed from an incubating status alone.

## Placement example

The paired MolSysMT/MolSysViewer release exposed a reusable lesson about
preserving agent development instructions. [MOLI #20](https://github.com/uibcdf/moli/issues/20)
owns the rule for direct components, while [MolSysSuite #66](https://github.com/uibcdf/molsyssuite/issues/66)
owns any member-wide adoption. A directory-specific instruction to consult
active report queues before relying on archived analyses belongs in
`devguide/AGENTS.md`; a general obligation to report upstream limitations
belongs in the root `AGENTS.md`. Neither placement substitutes for the issue
or a regression guard for the original defect.
