# MOLI Python developer tools policy

Normative for MOLI components carrying the `python-package` capability. These tools
support development and CI inspection; they are not runtime dependencies of the
component.

## Pytest Receptor

When an agent runs pytest, use the published pytest-receptor release and its
`--receptor=llm` profile. Use `--receptor=ci` for the component's pytest CI logs.
The receptor changes reporting, not the repository's required tests, markers, exit
status, or MOLI Python CI coverage. Pin the exact published release used by CI.
If a receptor version cannot run on a supported Python minor, record a bounded
exception and continue to run the required tests with native pytest.

## GH Run Receptor

Use a published gh-run-receptor release as the preferred first inspection of GitHub
Actions runs during development. It is an inspection tool, not a step that must run
inside each CI job. GitHub's run, job, and step conclusions remain authoritative.
Inspect with native `gh run view` when receptor evidence is incomplete, fails, omits a
needed fact, or disagrees with GitHub. Do not use the receptor as the sole approval
source for a release or publication. Pin an exact reviewed commit for experiments with
unreleased capabilities; report limitations to the provider with sanitized run evidence.

## Adoption

Direct Python components track adoption or a bounded exception through their
`python_ecosystem_review` issue and state in `moli.toml`. MolSysSuite coordinates
member-level rollout under its delegated governance while inheriting this MOLI rule.
