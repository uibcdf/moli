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
   shared-provider impact-notice and cross-repository contribution routes, and follow the
   [durable-instruction lifecycle](agent_instruction_lifecycle.md), including
   its distinction between technical findings and agent working instructions.
   Route developer-guide work to `devguide/AGENTS.md`. Adapt the
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
   and `moli.toml` identify those rules. Start local development and routine
   push/PR tests on Python 3.14; retain full tests on every supported minor.
   Create the declared Conda development environment; run local pytest under
   Python 3.14 and install the checkout with
   `python -m pip install --no-deps --editable .`. For integrated work, install
   each participating installable component checkout into a compatible Conda
   environment, verify its import path and track any compatibility or packaging
   gap. Coordinate suite members through MolSysSuite rather than declaring its
   environment complete from this checklist.
   If macOS is claimed, register only
   `supported_macos_architectures = ["arm64"]`, verify the runner architecture
   and installed candidate, and use the required Apple Silicon wording in the
   README. Do not claim macOS from a noarch recipe or a successful solve alone.
   Also register an owner-local `coverage_review` issue. Once meaningful code
   and tests exist, measure coverage in CI and add a live Codecov percentage
   only after Codecov accepts a recent report for this repository and branch;
   otherwise record a scoped, reviewable non-applicability or pending state.

The component still owns its implementation, tests, local API, release
decisions, and additional scoped instructions. Report a shared contract to
`uibcdf/moli` through its owning issue; propose an agent working instruction
there only after local acceptance and evidence of cross-component need.
