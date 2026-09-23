# MOLI Python CI Policy

Normative for MOLI components carrying the `python-package` capability.

## Routine gate

Every push and pull request has a gating Linux test lane on the routine development Python version (currently 3.13).

## Full supported matrix

At least weekly, and before a public release, the complete required test suite runs on every supported Python minor (currently 3.11, 3.12, 3.13). Manual dispatch should also be available for candidate verification.

A skipped, cancelled, tolerated-failure, or merely configured lane is not passing evidence.

## Local freedom

Repositories choose workflow structure, environment solver, specialized tests, and additional platforms according to their risks. The shared contract concerns observable support, not identical YAML.

Platform-specific claims beyond Linux require representative evidence or a documented exception.
