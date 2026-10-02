# MOLI Python Support Policy

Normative for MOLI components carrying the `python-package` capability.

## Baseline

Python packages declare `requires-python = ">=3.11,<3.15"` and support Python
3.11, 3.12, 3.13 and 3.14. Python 3.14 is the routine local development and
test version. A shared development environment must use Python 3.14; a
component may use another supported interpreter to investigate a version-specific
failure or run its required compatibility matrix.

Supporting a minor means package metadata admits it and the repository's required tests run on it.

## Ownership

Changing the common range is a MOLI engineering-governance decision. A component does not change it unilaterally.

A component may carry a documented, time-bounded exception with reason, tracking issue, and exit condition.

## Evolution

Transitions to new Python minors should be evidence-driven and phased. Component-specific feasibility may precede platform-wide baseline changes.

MolSysSuite sets and versions the Python range and routine development version
for its members. A MOLI revision does not automatically change the suite's rule.
