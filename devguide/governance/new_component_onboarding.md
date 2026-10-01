# Starting a directly governed MOLI component

Apply this checklist when creating a new component repository directly
governed by MOLI. The authoritative component registry is `moli.toml`; a
MolSysSuite member follows MolSysSuite's own admission and starter kit instead.

1. Register the component and its governance/guide delivery mode in
   `moli.toml`. Record capabilities and owner-local review issues as required
   by applicable policies. Do not claim support or publication without
   evidence.
2. Create a root `AGENTS.md` at repository inception. Link the vendored
   `MOLI_GUIDE.md`, state the issue-feedback duty and the
   [durable-instruction lifecycle](agent_instruction_lifecycle.md), and route
   developer-guide work to `devguide/AGENTS.md`. Adapt the
   [starter snippets](../templates/component_agent_instructions.md) to the
   component's actual ownership and local work.
3. Start `devguide/AGENTS.md` with the root-instruction link, current guidance,
   active `pending_bugs/` and `pending_proposals/` queues, historical
   `archive/`, and the reporting route. Keep the queue README files and
   `devguide/templates/report.md` present. A nested rule applies only within
   its subtree; put repository-wide rules in the root file.
4. Install the canonical `MOLI_GUIDE.md` byte-identically and provide the
   component's governance validation path. From the MOLI checkout, run
   `python devtools/scripts/check_repository.py <component-checkout> --canonical-guide MOLI_GUIDE.md`
   before declaring onboarding complete. Wire the same check into the new
   repository's CI or its existing governance gate. New repositories start
   with these files; they do not wait for a later policy rollout.
5. For a Python package, complete the extra registry reviews, CI, developer
   receptors, support-library applicability, distribution and OS-support
   evidence required by the applicable policies. The [component guide](../../MOLI_GUIDE.md)
   and `moli.toml` identify those rules.

The component still owns its implementation, tests, local API, release
decisions, and additional scoped instructions. A shared contract or reusable
cross-component lesson is reported to `uibcdf/moli` through the owning issue.
