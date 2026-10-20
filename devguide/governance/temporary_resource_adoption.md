# Temporary-resource rule adoption

This record accompanies [MOLI #61](https://github.com/uibcdf/moli/issues/61).
The [normative rule](temporary_resource_lifecycle.md) is in MOLI; a component
owns its local task, test, build and release resources. Guide delivery and
contributor instructions do not prove that historical scratch trees are safe
to delete. MolSysSuite owns its member rollout in
[MolSysSuite #104](https://github.com/uibcdf/molsyssuite/issues/104).

| Direct repository | Instruction delivery on main | Applicable local route and checked evidence |
| --- | --- | --- |
| MOLI | [bc75c4a](https://github.com/uibcdf/moli/commit/bc75c4a4f4a9b1ae1d1bf30a8cb379a0bd0ba9d7): registry, policy, guide, root instruction, onboarding and starter | [Governance](https://github.com/uibcdf/moli/actions/runs/39490197597) and post-delivery [complete guide audit](https://github.com/uibcdf/moli/actions/runs/39490330174) passed. |
| Sabueso | [784ae70](https://github.com/uibcdf/sabueso/commit/784ae70a1ee6d3b99c40580527d9dc65e9e773dc): root instruction, exact guide and developer-guide entry | Local test and Conda release routes remain in devguide/TESTS.md and devtools/conda-build/README.md; [governance](https://github.com/uibcdf/sabueso/actions/runs/39490318193) passed. |
| Praxis | [c83e592](https://github.com/uibcdf/praxis/commit/c83e5920a316130836c6bc2d9b0a7bcb4cdf8d49): root instruction, exact guide and developer-guide entry | Test, build and candidate routes remain in its workflows and devguide; [governance](https://github.com/uibcdf/praxis/actions/runs/39490312982) passed. |
| Nextia | [62618bb](https://github.com/uibcdf/nextia/commit/62618bb6640dc505be8fb6c6ee4cfac0cd3c7782): root instruction and exact guide | Design-stage repository has no Python test/build or public release route; [governance](https://github.com/uibcdf/nextia/actions/runs/39490304334) passed. |
| MOLI Agent | [ff3fabe](https://github.com/uibcdf/moli-agent/commit/ff3fabe32dd85eafa2a8cd244767e1c8dcea9c68): root instruction and exact guide | Design-stage repository has no Python test/build or public release route; [governance](https://github.com/uibcdf/moli-agent/actions/runs/39490307567) passed. |
| Recorda | [f156a14](https://github.com/uibcdf/recorda/commit/f156a1423d669f27b00703f5ce18fed3d6d2c275): root instruction, exact guide, developer-guide entry and current MOLI policy pin | Local environment and release routes remain in devtools/conda-envs/README.md and devguide/RELEASING.md; the quality job in [tests and governance](https://github.com/uibcdf/recorda/actions/runs/39490323245) passed. |

The five published direct-component copies passed the full hosted guide audit,
which checks current component main branches. Governance and guide evidence
does not certify scientific suites, installed artifacts or cleanup of
unidentified historical resources. Broader component test runs triggered by
the documentation pushes retain their own conclusions.

## Shared support infrastructure

- Pytest Receptor's owned benchmark cleanup defect was repaired and guarded
  in [provider #40](https://github.com/uibcdf/pytest-receptor/issues/40).
- GH Run Receptor has an [owner review #63](https://github.com/uibcdf/gh-run-receptor/issues/63)
  and a maintained resource-lifecycle report; no duplicate issue was opened.
- The Conda build/upload action exposes a temporary build-output tree to
  downstream steps. [Provider #51](https://github.com/uibcdf/action-build-and-upload-conda-packages/issues/51)
  asks its owner to define retention and safe cleanup after final use.
- Source review of the Sphinx-to-Pages action found caller-workspace build
  output rather than a tool-created /tmp tree. No unverified cleanup defect
  was inferred from that alone.

These provider reviews do not transfer their implementation ownership to MOLI
or assert that MolSysSuite's separate member adoption is complete.
