# MOLI Python Quality Tooling Policy

Normative for MOLI components carrying the `python-package` capability.

## Baseline

Ruff is the common formatter, import sorter, and linter. Pytest is the common test runner.

Required checks:

```bash
ruff format --check .
ruff check .
pytest
```

Every Python repository enables at least Ruff rule families `E4`, `E7`, `E9`, `F`, and `I`, with target version `py311` while Python 3.11 remains supported.

Repositories may add stricter rules and local exclusions. They may not silently disable the shared baseline.

Black, isort, and Flake8 should not remain active after migration to the common Ruff baseline.

## Versioning

MOLI governance records the tested Ruff version used by its conformance policy. Upgrades are coordinated rather than independently discovered by every component.
