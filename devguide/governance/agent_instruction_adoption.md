# Agent-instruction adoption inventory

This inventory tracks MOLI #20 for repositories directly governed by MOLI.
The normative rule is [agent_instruction_lifecycle.md](agent_instruction_lifecycle.md).
The listed evidence must be verified against each repository's current `main`
before marking it adopted. A pending entry is a tracked migration, not an
exception. MolSysSuite owns instructions for its member repositories.

| Repository | Root and `devguide/` instructions | Evidence or next step |
| --- | --- | --- |
| `uibcdf/moli` | Adopted | [012fca3](https://github.com/uibcdf/moli/commit/012fca3): root and nested instructions, governance validator and onboarding guide. |
| `uibcdf/sabueso` | Adopted | [9191bae](https://github.com/uibcdf/sabueso/commit/9191bae): preserved Sabueso-specific guidance, clarified the technical-finding boundary in root and nested instructions; local gate retained. |
| `uibcdf/praxis` | Adopted | [6850b7e](https://github.com/uibcdf/praxis/commit/6850b7e): root and scoped developer-guide instructions clarify the boundary; local gate retained. |
| `uibcdf/nextia` | Adopted | [2bd000f](https://github.com/uibcdf/nextia/commit/2bd000f): root and scoped developer-guide instructions clarify the boundary; local gate retained. |
| `uibcdf/moli-agent` | Adopted | [6263508](https://github.com/uibcdf/moli-agent/commit/6263508): root and scoped developer-guide instructions clarify the boundary; local gate retained. |
| `uibcdf/molsyssuite` | Delegated | MOLI platform-boundary feedback applies; [MolSysSuite #66](https://github.com/uibcdf/molsyssuite/issues/66) owns member adoption and the new-member starter kit. |

Acceptance requires an owner-local root rule, a scoped developer-guide rule,
and a passing mechanical check for each direct, non-delegated repository.
Local repository-specific exceptions must name their owning issue and exit
condition here; none is assumed from an incubating status alone.

## Placement example

The paired MolSysMT/MolSysViewer release exposed a recurring agent handoff
problem: working instructions were lost between sessions. That workflow
problem, rather than the release defects themselves, justified a shared
instruction. [MOLI #20](https://github.com/uibcdf/moli/issues/20)
owns the rule for direct components, while [MolSysSuite #66](https://github.com/uibcdf/molsyssuite/issues/66)
owns any member-wide adoption. A directory-specific instruction to consult
active report queues before relying on archived analyses belongs in
`devguide/AGENTS.md`; a general obligation to report upstream limitations
belongs in the root `AGENTS.md`. Neither placement substitutes for the issue
or a regression guard for the original defect.
