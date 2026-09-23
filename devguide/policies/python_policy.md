# MOLI Python Support Policy

Normative for MOLI components carrying the `python-package` capability.

## Baseline

Python packages declare `requires-python = ">=3.11,<3.14"` and support Python 3.11, 3.12 and 3.13. Python 3.13 is the routine development version.

Supporting a minor means package metadata admits it and the repository's required tests run on it.

## Ownership

Changing the common range is a MOLI engineering-governance decision. A component does not change it unilaterally.

A component may carry a documented, time-bounded exception with reason, tracking issue, and exit condition.

## Evolution

Transitions to new Python minors should be evidence-driven and phased. Component-specific feasibility may precede platform-wide baseline changes.

MolSysSuite may maintain additional rollout machinery for its internally governed members, but its stable engineering baseline inherits this MOLI policy.
