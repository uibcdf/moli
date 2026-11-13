# MOLI Shared Policies

MOLI owns the engineering baseline for its directly governed components, alongside platform and scientific governance.

Current engineering policies cover Python support, Python CI, Ruff/pytest quality tooling, applicable support libraries, developer receptors, distribution, public release-version semantics, repository badge evidence, and Zenodo/DOI archival claims.

Applicability is recorded in `moli.toml` for directly registered components. Policies do not pass automatically through MolSysSuite to its members; `suite.toml` and MolSysSuite's policy documents govern those members.

Several practices were developed first in MolSysSuite and later adopted independently for directly governed MOLI components. Similarity does not change each repository's authority to decide and version its own rules.

Shared policy should answer a demonstrated cross-repository need rather than being added for symmetry.

The [resource-aware execution rule](resource_aware_execution.md) covers general
contributor conduct on shared compute. Infrastructure owners keep enforcement
and site configuration; the [integration proposal](../pending_proposals/execution_infrastructure_contract.md)
is separately pending executable review and receiving.
