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
| `uibcdf/recorda` | Adopted contributor instructions | [bb2da676824a68728e8bee1ec160b038832eb8f7](https://github.com/uibcdf/recorda/commit/bb2da676824a68728e8bee1ec160b038832eb8f7): root/nested routes, exact guide and executed immutable shared-core CI; bounded registration review [MOLI #50](https://github.com/uibcdf/moli/issues/50). Runtime/ecosystem and public support remain owner reviews. |
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


Associated Recorda Lab infrastructure is separately verified at
`0ca1943baeb2551489eaa821fb414b95892e0952`, including its root/nested routes,
exact guide and four executed shared-core CI steps under Recorda Lab #7.
It is not an independently admitted scientific component or suite member.
The full platform-guide audit still fails on three other guide copies under
MOLI #60; these current source checks do not certify a global pass.
