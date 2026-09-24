# MOLI Python distribution policy

Normative for MOLI components with the `python-package` capability. MOLI owns the
shared user-installation and distribution contract. MolSysSuite inherits this baseline
and owns member-specific release routes, coupled-package staging, promotion and
rollout evidence. A repository owns its package recipe, environments, CI, release
workflow and publication decision.

## Public installation and truthful claims

The official user-installation route for a public UIBCDF Python component is a
published package on the `uibcdf` Conda channel, with third-party dependencies from
`conda-forge`. Document `conda install -c uibcdf -c conda-forge <package>` only after
the package exists in the public channel and a clean installation has been verified.
Before the first publication, document source installation as a development route;
do not claim the Conda package already exists. A `noarch: python` recipe is appropriate
for a genuinely pure-Python package; packages with compiled artifacts use their
applicable platform/build profile.

PyPI is an optional *additional* public route, adopted for a documented component
need rather than by default. Claim or recommend `pip install <package>` for users
only after the matching version is published on PyPI and a clean installation of
its declared runtime dependency closure succeeds on the claimed Python versions
and platforms. A Conda-only required dependency makes a PyPI route incomplete
until that dependency is available through the package index or the component
changes its dependency contract. A Git repository or editable checkout is not
evidence of PyPI availability. Distribution badges and README instructions follow
the independently observed publication state.

`pytest-receptor` has a specific reason for PyPI publication: pytest's generated
plugin catalog discovers projects through PyPI naming. This does not make PyPI
publication mandatory for other MOLI packages, and catalog inclusion is distinct
from joining the `pytest-dev` GitHub organization. Its own
[PyPI release runbook](https://github.com/uibcdf/pytest-receptor/blob/main/devguide/pypi_release.md)
records the discovery and release checks.

## Development and CI

Install the local checkout for development with `pip install --no-deps --editable .`
after creating the component's declared Conda development environment. The Conda
environment supplies dependencies; `--no-deps` prevents pip from resolving them
again. This local, editable installation is not a publication and does not imply
that a PyPI distribution exists. The equivalent short option is `-e`; pip has no
`--development` install option. Build scripts may use `pip install --no-deps .`
for a non-editable local installation. A component with an entirely PyPI-available
development dependency closure may document a virtual-environment alternative.

Keep committed environment specifications under `devtools/conda-envs/`. Use
`development_env.yaml` for the development route and `test_env.yaml` for required
tests; add `build_env.yaml` and `docs_env.yaml` when those jobs exist. Additional
files may describe platform-specific or reduced-dependency lanes. These environment
files declare tool and test dependencies as well as the runtime packages needed by
their jobs. A required CI lane that needs Conda-only third-party dependencies must
acquire them through a resolvable Conda environment, using micromamba or an
equivalent solver;
install the local component with `--no-deps` only after its required dependencies
are present. If a required sibling version cannot be resolved from the configured
Conda channels, a tracked temporary CI route may install that sibling from a
reviewed full commit SHA and verify its installed import. That source route is
development/test evidence, not evidence for a public user-installation claim.
A component with a verified all-PyPI dependency closure may use a pip test lane,
but a public Conda release still needs installed-artifact evidence.
MOLI's [Python CI policy](python_ci_policy.md) governs events, supported minors and
passing evidence; this policy does not prescribe identical workflow YAML.

Declare required runtime dependencies and supported Python bounds in
`pyproject.toml` (`project.dependencies` and `requires-python`); keep optional
features in `project.optional-dependencies` when they are truly optional. The Conda
recipe's `requirements: run` must express the same required runtime closure and
compatible version floors/ceilings. Conda and Python distribution names can differ;
record intentional mappings, such as `mmcif` to `py-mmcif`, and verify both resolved
installations. Environment files may add development tools and optional-feature
packages, but must not silently substitute for missing runtime metadata. Recheck
recipe and CI environments whenever a required dependency or Python bound changes.

For normal Conda environments, list `uibcdf` before `conda-forge` and record the
channel-priority mode. Strict priority is the normal starting point, not a universal
proof of package origin: a staging label or overlapping names may require a different
solver setting. Such a route must select exact package coordinates and verify the
installed source channel and artifact identity. A solver success alone is not
publication or provenance evidence.

## Recipe and publication

Before a component's first public Conda release, maintain a recipe under
`devtools/conda-build/` (`meta.yaml` and a build script if needed) and a
`.github/workflows/build_and_upload_conda_packages.yaml` workflow invoking a
reviewed release of `uibcdf/action-build-and-upload-conda-packages`. A repository
may use a different workflow name with a documented reason and equivalent gates.
Build the package from
the exact release candidate and derive its public version from the `X.Y.Z` Git tag
required by [MOLI release-version policy](release_version_policy.md); Conda build
numbers are separate. Test the built artifact's installation, import/version and
required runtime behavior before publication. Verify the public channel state after
upload before claiming the version is available.

Use `uibcdf/action-build-and-upload-conda-packages` as the shared publication
mechanism unless a tracked exception explains an equivalent route. Keep channel
credentials in CI secrets, never in the repository or retained evidence. A first
release needs a reviewed publication route and exact-candidate evidence. Mandatory
staging, promotion ordering, rollback and coupled-package gates are not declared
platform-wide here; MolSysSuite's [coordinated release proposal](https://github.com/uibcdf/molsyssuite/issues/27)
owns that domain-specific decision. Direct components choose a suitable route with
their own release evidence.

The build/upload action is UIBCDF-owned
[support infrastructure](../governance/support_infrastructure.md). Report action
defects to its provider repository; report platform-wide usage changes to MOLI.
Credential access and communication are tracked separately in
[MOLI #8](https://github.com/uibcdf/moli/issues/8).

## Onboarding and adoption

Direct Python components register a `python_distribution_review` issue and state in
`moli.toml`. States are `pending`, `partial`, `adopted` and `excepted`. The issue records
the intended user channels, dependency closure, environment/recipe paths, CI route,
release readiness and any bounded exception. `adopted` requires evidence for the
routes the component actually claims; it does not assert that an incubating package
has already published a release. The registry validator prevents a new direct Python
component from entering without this review. Delegated governance tracks member
adoption in its own registry and may impose stricter domain requirements.
