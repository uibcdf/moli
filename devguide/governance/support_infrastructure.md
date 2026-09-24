# UIBCDF development infrastructure supporting MOLI

`moli.toml` lists UIBCDF-owned tools used to develop, verify and publish MOLI
components. This is a support-infrastructure category, not another architectural
MOLI component layer. The tool repositories own implementation, releases and their
own defects. MOLI owns platform-wide usage guidance; MolSysSuite governs adoption
by its members. Pytest Receptor and GH Run Receptor keep their existing MolSysSuite
auxiliary membership while also appearing in this cross-platform catalog.

| Resource | Use when applicable | Provider issue board |
| --- | --- | --- |
| [Pytest Receptor](https://github.com/uibcdf/pytest-receptor) | Human or agent pytest runs and Python CI reporting, following the [developer-tools policy](../policies/python_developer_tools_policy.md). | [pytest-receptor issues](https://github.com/uibcdf/pytest-receptor/issues) |
| [GH Run Receptor](https://github.com/uibcdf/gh-run-receptor) | Inspect GitHub Actions runs; GitHub conclusions remain authoritative. | [gh-run-receptor issues](https://github.com/uibcdf/gh-run-receptor/issues) |
| [Conda build/upload action](https://github.com/uibcdf/action-build-and-upload-conda-packages) | Build and publish component Conda packages through a reviewed action release, following the [distribution policy](../policies/python_distribution_policy.md). | [Conda action issues](https://github.com/uibcdf/action-build-and-upload-conda-packages/issues) |
| [Sphinx-to-Pages action](https://github.com/uibcdf/action-sphinx-docs-to-gh-pages) | Build Sphinx documentation and publish it to GitHub Pages. Use a reviewed action release when this is the component's documentation route; document an equivalent route or exception if the action is unsuitable. | [Sphinx action issues](https://github.com/uibcdf/action-sphinx-docs-to-gh-pages/issues) |

These resources are development and publication infrastructure, not scientific
runtime dependencies. A component without a Conda release does not need an upload
workflow yet; a component without Sphinx-to-Pages documentation does not need that
action. Use the supported resource where its boundary applies, with the repository
owning its workflow, action version and verification. Channel credential access is
a separate unresolved platform decision in [MOLI #8](https://github.com/uibcdf/moli/issues/8);
this catalog does not claim any repository already has the secret.

The [MOLI issue-feedback commitment](reporting_protocol.md#universal-issue-feedback-commitment)
applies to all four providers and to their consumers. Report a tool bug, improvement
or feature proposal on its provider issue board, or add evidence to an existing
issue. Link any consumer-side blocker or workaround. Use a MOLI issue for a shared
platform usage contract and a MolSysSuite issue for a suite-specific adoption or
integration decision. Do not hide provider feedback in a consumer repository.
Private security reporting takes precedence for exploitable findings.
