# Component agent-instruction starter

Adapt these short blocks to a directly governed component. Preserve its existing
local rules. The canonical meaning lives in `MOLI_GUIDE.md` and
`devguide/governance/agent_instruction_lifecycle.md` in MOLI.

## Root `AGENTS.md` block

```markdown
Report defects in their owning issues and fix them with code, tests and
technical documentation. Do not store source-specific facts, edge cases or
workarounds in `AGENTS.md`. Only after normal owner review, put a lasting
instruction about how contributors or agents work across future tasks in the
appropriate root or nested `AGENTS.md`; use an adoption issue only if an
accepted instruction cannot be placed with the fix or decision. Follow
`MOLI_GUIDE.md#durable-instructions-for-development-agents`. Propose a shared
working instruction to the owning governance issue only with evidence that it
applies beyond this repository. For developer-guide work, read
`devguide/AGENTS.md`.
```

## `devguide/AGENTS.md` starting text

```markdown
# Developer-guide instructions

Read `../AGENTS.md` for repository-wide rules and
`../MOLI_GUIDE.md#reporting-bugs-and-proposals` for issue routing.
Use maintained guide documents for current behavior. Active issue-backed
analyses are in `pending_bugs/` and `pending_proposals/`; `archive/` preserves
resolved or superseded history. Read an archived report when tracing a
decision, and check the current replacement before treating it as policy.
Follow the repository's reporting protocol when filing or resolving reports.
Keep technical facts and defect details in maintained documents, tests and
owning issues. Put lasting working instructions specific to this directory
here; put repository-wide working instructions in the root `AGENTS.md`.
```

The owner should replace generic document names with its current indexes or
protocol paths and may add narrower instructions where useful.
