# Component agent-instruction starter

Adapt these short blocks to a directly governed component. Preserve its existing
local rules. The canonical meaning lives in `MOLI_GUIDE.md` and
`devguide/governance/agent_instruction_lifecycle.md` in MOLI.

## Root `AGENTS.md` block

```markdown
When an incident reveals a reusable development rule, assess its scope. Put
an accepted repository-wide rule here and a directory-specific rule in the
appropriate nested `AGENTS.md` in the same change; otherwise track adoption
in an owned issue. Follow `MOLI_GUIDE.md#durable-instructions-for-development-agents`.
Report a potentially shared lesson to the owning governance issue.
For work in the developer guide, also read `devguide/AGENTS.md`.
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
Put rules specific to this directory here; put repository-wide rules in the
root `AGENTS.md`.
```

The owner should replace generic document names with its current indexes or
protocol paths and may add narrower instructions where useful.
