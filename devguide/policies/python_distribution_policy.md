# MOLI Python distribution policy

Normative for directly governed MOLI components with the `python-package`
capability. MolSysSuite owns distribution rules for its members, including
member-specific release routes, coupled-package staging, promotion and rollout
evidence. A repository owns its package recipe, environments, CI, release
workflow and publication decision.

## Public installation and truthful claims

The official user-installation route for a public UIBCDF Python component is a
published package on the `uibcdf` Conda channel, with third-party dependencies from
`conda-forge`. Document `conda install -c uibcdf -c conda-forge <package>` only after
the package exists in the public channel and a clean installation has been verified.
Before the first publication, document source installation as a development route;
do not claim the Conda package already exists. A `noarch: python` recipe is appropriate
for a genuinely pure-Python package; packages with compiled artifacts use their
applicable platform/build profile. `noarch` describes one build artifact, not an
operating-system support claim. Declare supported systems and verify the installed
artifact on them as required by [MOLI's Python CI policy](python_ci_policy.md):
Linux and macOS are the baseline; Windows is optional and claimed only with evidence.

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

For a co-development workspace spanning components, first solve a compatible
Conda environment for their runtime, test and build requirements. Install each
participating **installable Python package** from its local checkout into that
environment with `python -m pip install --no-deps --editable .` (run once per
checkout), then verify the installed distribution and import path resolve to
the intended checkout. Run local pytest under Python 3.14 in that environment;
the routine CI lane also uses Python 3.14 under the
[Python CI policy](python_ci_policy.md). Editable source changes are then visible
to other packages using that environment. Dependency metadata changes or native
builds may still require reinstalling or rebuilding; an editable installation
alone does not prove cross-component compatibility. Track an unavailable or
incompatible package as a concrete adoption gap rather than claiming a complete
workspace. Repositories without a Python package are outside this installation
step.

MolSysSuite owns the named `molsyssuite@uibcdf_3.14` development environment,
its eligible member inventory and expansion to the full suite. Follow its
[Conda environment instructions](https://github.com/uibcdf/molsyssuite/blob/main/devtools/conda-envs/README.md)
for the actual recipe and any build options required by its members. A shared
workspace that also includes directly governed MOLI packages must verify their
dependency compatibility and install them from their own checkouts; the suite
environment name alone does not certify that wider workspace. The suite rollout
is tracked in [MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82)
and the platform target in [MOLI #40](https://github.com/uibcdf/moli/issues/40).

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

## Early dependency-contract preflight

Before an expensive candidate build, each applicable Python component runs a cheap,
read-only dependency-contract preflight. `pyproject.toml` remains authoritative for
required runtime names, version constraints, and `requires-python`; an audit
inventory identifies secondary routes, not a second dependency list. Inventory
every maintained Conda recipe, runtime-bearing development or CI environment,
and exact sibling-source route used by a required lane. Classify a route that does
not install the component runtime with a reason. A newly added or unclassified
runtime route fails the preflight until it is reviewed.

The check compares each applicable recipe and environment with the public runtime
closure and Python bounds. It must detect a missing required Conda dependency, a
weaker or stale version floor or ceiling, and a missing or incompatible Python
constraint. Record intentional Conda/Python name translations and justified
route-specific constraints explicitly; they must not hide a public requirement.
For a `--no-deps` lane that supplies a sibling from source, verify a reviewed full
commit SHA, the route that installs it, and the installed distribution version
against the public requirement. A source checkout below the declared floor fails
even when its Git commit is exact.

Run this preflight early in CI when dependency metadata, recipes, environments,
or source-install routes change, and again for the exact release candidate before
costly builds where practical. Keep a negative fixture or equivalent conformance
test that rejects at least a missing recipe runtime dependency, an environment
with a stale floor, and a source candidate below its public floor. Report the
offending route and constraint; do not silently rewrite hand-maintained recipes
or weaken package metadata to make the audit pass. Repositories may choose their
own parser, inventory format, exclusions, and CI layout. A static audit proves
contract consistency, not that the minimum version provides the required API:
clean installed compatibility tests and built-artifact checks remain release
gates.

Direct components record their preflight route, negative evidence, and any
bounded exception in their `python_distribution_review` issue or an issue linked
from it. MolSysSuite independently governs member distribution and tracks
adoption and exceptions in its own inventory. A policy pin, an earlier adopted review, or another member's passing
audit does not by itself prove adoption of this requirement. The platform change
is tracked in [MOLI #21](https://github.com/uibcdf/moli/issues/21).

For normal Conda environments, list `uibcdf` before `conda-forge` and record the
channel-priority mode. Strict priority is the normal starting point, not a universal
proof of package origin: a staging label or overlapping names may require a different
solver setting. Such a route must select exact package coordinates and verify the
installed source channel and artifact identity. A solver success alone is not
publication or provenance evidence.

## Generated resources in release artifacts

For each claimed public distribution route, inventory package-critical generated
or vendored runtime resources and version-bearing payloads delivered to users.
Examples include compiled extensions, generated schemas, embedded data and
browser bundles. Record the expected path or identity in that route's archive,
the applicable release-version check, and a representative installed runtime
path. A repository with no such resources records non-applicability and its
reason in its distribution review; it does not need a JavaScript or npm build.

Run cheap checks of committed sources and generated files before expensive
packaging. Then build **each claimed route from the exact release candidate**,
inspect that route's resulting archive for every required resource, and check
embedded version identities against the intended `X.Y.Z` tag where applicable.
Install that artifact in a clean environment and exercise a representative path
that loads or uses the resource. Record the artifact coordinate and content digest
with the route-specific result in the candidate evidence described by
[MOLI release-version policy](release_version_policy.md). A missing resource,
stale version, failed installed path or uninspected claimed artifact blocks the
claim for that route. A source checkout, or a Conda/npm build that regenerates a
resource, cannot certify an ordinary wheel carrying committed bytes; evidence
from one route does not certify another route's delivered content.

Keep a negative fixture or equivalent conformance test that rejects a stale
embedded version and a missing required resource in one claimed artifact even
when another route passes. Repositories choose their own build and archive
inspection mechanisms, including any extraction required for Conda artifacts.
The [reference archive checker](../../devtools/scripts/distribution_artifact_evidence.py)
and its [fixtures](../../tests/test_distribution_artifact_evidence.py) illustrate
the per-route boundary for ZIP and TAR archives; they do not replace a
repository's exact-candidate build or installed-runtime test. Direct components
record route/resource inventory, verification evidence and bounded exceptions
in their `python_distribution_review` issue or a linked issue. MolSysSuite owns
its member policy, adoption and exceptions. [MOLI #26](https://github.com/uibcdf/moli/issues/26)
tracks this platform rule.

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
required runtime behavior before publication. Follow the immutable-coordinate and
public-registry verification rule below before claiming the version is available.

### Immutable Conda coordinates and public poststate

Treat the owner/package/version/subdir/filename tuple as one immutable Conda file
coordinate across all labels. Record that coordinate and the SHA-256 of the exact
candidate file after building and testing it. Before a direct upload, query the
registry for that exact coordinate under **any** label. If occupied, do not upload,
replace or use `--force`, even when the existing digest matches. A changed build
needs a new build number or public version, producing a new filename. An identical
existing file may be verified or, when it is the tested staged file, promoted;
its bytes are never replaced. A label changes visibility of the same registry
file, not its identity.

Distinguish four steps in release evidence: build the candidate file, upload a
previously unoccupied coordinate if needed, promote a tested staged file by adding
the public label to that **same digest** if staging is used, and independently
verify the public registry poststate. Promotion checks the exact source coordinate,
source label and digest before adding the target label; it does not rebuild or
upload a second file at the same coordinate. A direct single-package publisher
does not need staging. MolSysSuite owns eligibility for staging, paired-package
promotion order and member rollout.

After upload or promotion, use a read-only registry query that can run again
without repeating the mutation. Match the public label, exact coordinate and
SHA-256 against the tested candidate. Record the query result and artifact identity
in the release receipt; an action's success status or mutation receipt alone is
insufficient. Use bounded retries for registry/index propagation, then leave the
gate unresolved if the exact public record cannot be observed. Check a clean
solver/install route separately before advertising user availability where the
distribution and CI policies require it. A red poststate verifier is diagnosed
with read-only queries, not another upload or promotion just to obtain a green run.

If an upload or label operation returns an uncertain response, inspect the
registry first. The expected public coordinate and digest may be accepted only
after read-only verification. A matching staged file without the public label may
be promoted again only after its source identity is rechecked; a direct upload may
be retried only after bounded observation still finds the coordinate unoccupied
and a fresh preflight confirms that state. A conflicting digest, occupied
coordinate, missing source identity, or unresolved registry state fails closed.
An HTTP 409 never authorizes `--force` or a rebuild at the same filename.

Keep a negative conformance check that rejects an occupied coordinate even under
another label and rejects changed bytes at the expected public coordinate. The
[reference evaluator](../../devtools/scripts/conda_publication_evidence.py) and
[fixtures](../../tests/test_conda_publication_evidence.py) illustrate those
decisions using registry snapshots; they do not perform registry I/O. Direct
components record their publishing route, evidence and bounded exceptions in
their `python_distribution_review` issue or a linked issue. This platform rule is
tracked by [MOLI #25](https://github.com/uibcdf/moli/issues/25); the provider's
[exact-file promotion primitive](https://github.com/uibcdf/action-build-and-upload-conda-packages/issues/43)
and MolSysSuite's [coordinated release](https://github.com/uibcdf/molsyssuite/issues/27)
and [poststate-verifier](https://github.com/uibcdf/molsyssuite/issues/48)
issues retain their own implementation ownership.

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
Credential access follows the contract below, accepted through
[MolI #8](https://github.com/uibcdf/moli/issues/8).

## Conda publication credential access

Diego Prada (`dprada`) administers and rotates the UIBCDF Anaconda publication
credential. Its canonical GitHub Actions name is `ANACONDA_UIBCDF_TOKEN`, stored
as an **organization secret available to selected repositories**. Diego
confirmed this administrative model on 2026-10-22 UTC in #8. The collaborator
preparing a package does not need to obtain or supply a personal upload token.

For a direct component that needs access, open or update an issue in the
component repository and link #8. Identify the repository, responsible release
maintainer, intended `uibcdf` package, reviewed publication workflow and its
trusted events/environments. Request repository access from Diego; he records
the grant or refusal there without disclosing the credential. Use the same
route for unavailable/revoked access or a suspected expired token. Diego owns
rotation and repository selection; record changed access and recheck affected
publication routes after rotation. No rotation interval is invented here.

The repository owner records who may invoke publication and the trusted
release/manual route, candidate checks and any environment approval it uses.
An organization-secret grant does not authorize a release. Ordinary tests and
fork/PR code must not publish or run with the upload credential. Build/test
work remains possible without it. Pass the canonical secret only to the
trusted publisher's documented input/environment; do not introduce a new
personal-token fallback or silently shadow the organization secret with a
same-name repository/environment secret. Existing aliases require owner review
when the route is next changed; this rule neither rotates credentials nor
rewrites historical releases.

### Readiness and evidence

Before an authorized publication, verify availability in the actual trusted
workflow context with a presence-only check, early enough to avoid an expensive
build doomed by missing access. An equivalent early check in the selected
publisher is acceptable. For example, inside that trusted job:

```yaml
- name: Check publication credential availability
  shell: bash
  env:
    MOLI_CONDA_TOKEN: ${{ secrets.ANACONDA_UIBCDF_TOKEN }}
  run: |
    set +x
    if [[ -z "${MOLI_CONDA_TOKEN:-}" ]]; then
      echo '::error::ANACONDA_UIBCDF_TOKEN unavailable; request repository access from Diego Prada through the owning issue.'
      exit 1
    fi
    echo 'Publication credential available (presence only).'
```

Keep the token out of command arguments, traces, artifacts and diagnostic
payloads. Retain only the repository, exact workflow/source/run, availability
result and administrator's issue disposition. An empty value establishes
unavailability in that context, not whether the cause is a missing grant,
event restriction or another configuration problem. Escalate that result to
Diego through the owning issue.

Availability does not prove validity or write access to `uibcdf`. The next
authorized real release must retain the successful exact-file upload/promotion
and independently verified target-channel poststate under the existing
immutable-coordinate rules. Do not manufacture a package/upload to test a token.
A past successful upload proves that recorded transaction, not future access.
Unknown grant, failed check, failed upload and unverified public poststate stay
visible as distinct readiness states; do not mark a repository ready from a
workflow reference, repository admin role or successful build alone.

[GitHub's secret usage documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
describes selected-repository organization access, empty unavailable secret
expressions and reusable-workflow forwarding. Its
[precedence reference](https://docs.github.com/en/actions/reference/security/secrets)
explains same-name environment/repository overrides. These technical details
do not decide MolI's release authority or prove an actual repository grant.

MolSysSuite owns equivalent member guidance, workflow adoption and receiving
evidence through [suite #45](https://github.com/uibcdf/molsyssuite/issues/45).
Requests involving its members retain that governance route and the same
credential administrator; MolI does not edit member workflows or grant access.
The existing canonical guide already links this distribution policy. Component
onboarding and release checklists link this section rather than copying the
administrative contract. Per-repository execution/adoption is recorded in #8
and the owning distribution/release issues; the policy alone is not deployment.

## Onboarding and adoption

Direct Python components register a `python_distribution_review` issue and state in
`moli.toml`. States are `pending`, `partial`, `adopted` and `excepted`. The issue records
the intended user channels, dependency closure, environment/recipe paths, CI route,
release readiness and any bounded exception. `adopted` requires evidence for the
routes the component actually claims; it does not assert that an incubating package
has already published a release. The registry validator prevents a new direct Python
component from entering without this review. Delegated governance tracks member
adoption in its own registry and may impose stricter domain requirements.
