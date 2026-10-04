# MOLI Python CI Policy

Normative for MOLI components carrying the `python-package` capability.

## Routine gate

Every ordinary push and pull request has a gating Linux test lane on the routine
development Python version (currently 3.14). A previously 3.13-only routine
lane moves to 3.14; do not silently remove required full-suite evidence for
older supported minors. The bounded direct-push deferral below does not turn a
skipped run into passing evidence or weaken a required pull-request gate.

## Validation during direct-push development

Match validation to the actual change and the repository's local instructions.
Before pushing, decide whether remote CI adds evidence at this point. Keep
short exploratory commits local and push a meaningful checkpoint when remote
visibility or backup is not needed for each increment. A commit or push alone
is not a validation checkpoint. For documentation, research notes or recorded
evidence that cannot change executable behavior, run the applicable local
document, governance and data checks. For changed numerical/public behavior,
run targeted regressions; broaden to affected platforms, dependencies,
packaging and integration boundaries when their risk warrants it. Reuse a
completed result only while the tested scope remains unchanged, and state the
scope of local tests, scientific comparisons and remote CI separately.

An authorized **direct push** may carry `[skip ci]` only when the repository's
owner permits it and the change does not need an immediate remote signal. This
can be a locally checked, non-executable documentation/evidence update with no
applicable required remote check, or an intermediate tested code checkpoint
under a documented recovery route that will run the required suite on the
resulting head. A repository that cannot reliably recover skipped code pushes
should batch commits locally and use an ordinary push. Prefer ending a code
development session with an unskipped checkpoint; inspect its required checks
on the actual head. If work stops on a skipped code head, record the validation
debt with an owner and trigger the repository's recovery or manual test route
before release, merge claims or closing the work. An older green run does not
certify subsequent skipped changes.

Do not use `[skip ci]` on a pull-request head with required checks, a release
candidate, publication, or a change needing immediate security, dependency,
packaging, migration or integration evidence. GitHub's
[skip behavior](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs)
suppresses workflows triggered by `push` and `pull_request`, not only an
expensive test job; required PR checks can remain pending. The marker is not a
substitute for a reviewed selective workflow. Follow stricter owner-local
gates until the repository owner changes them through its normal review route.

## Operating-system support

Linux and macOS are the platform baseline for public MOLI Python packages. A
component is expected to support both. Linux is mandatory; a component that cannot
yet support macOS records a bounded exception with its reason, owning issue and exit
condition, and states the limitation in its README. Windows is optional: its absence
does not block a release or count as a policy exception. A component may add Windows
when it can maintain the evidence below.

macOS support is currently limited to Apple Silicon (arm64). Intel-based macOS
(x86_64) is not part of the supported platform matrix. Support may be
reconsidered if there is demonstrated user demand. This is a prospective support
choice, not a claim that existing Intel installations have stopped working. Do
not remove historical artifacts or evidence. A component without verified arm64
evidence must state its actual limitation rather than implying arm64 support.

The `supported_os` list in `moli.toml` records the operating systems a directly
governed Python component currently claims. Its `os_support_review` points to a
component-owned issue and has a `pending`, `partial`, `adopted` or `excepted` state.
When `macos` is claimed, `supported_macos_architectures = ["arm64"]` records its
only eligible architecture. Omit that field when macOS is not claimed.
An incubating component may register with an empty supported list and a pending
review. The policy target remains Linux and macOS; an empty list makes no support
claim. `adopted` requires evidence for Linux
and macOS; `excepted` requires Linux evidence and a `macos_exception_issue` with an
exit condition. MolSysSuite records its members' claims and adoption in its own
registry; MOLI does not duplicate those
member rows. Each component states its current claim in its README. A platform
under test can be described as experimental, but it must not be included in the
supported list until its evidence passes. A `noarch: python` recipe alone does not
prove that its package or dependency closure works on every operating system.

## Required evidence

At least weekly, the complete required test suite runs on Linux for every supported
Python minor (currently 3.11, 3.12, 3.13, 3.14). On macOS, at least the routine Python
minor runs the required tests weekly; the same applies to Windows if claimed.
The macOS lane must demonstrate arm64 at runtime. A moving runner label alone
is insufficient; pin a documented arm64 runner or verify its architecture in
the job. No Intel-only job or `osx-64` publication target is a required gate.
Manual dispatch is available for candidate verification.

Before a public release, the exact candidate's installed package and required
dependency closure are tested on Linux and macOS across every Python minor the
component claims there. A component with a macOS exception tests the platforms it
actually claims and keeps the exception visible. A Windows claim requires the same
pre-release installed-package evidence on Windows. Representative runtime behavior,
not just import or solver success, is part of the check; package entry points are
exercised where the component provides them. The component may choose its workflow
shape, and a single noarch artifact may be installed on several platforms.

A skipped, cancelled, tolerated-failure, or merely configured lane is not passing evidence.
Before release, apply the [candidate evidence lifecycle](release_version_policy.md#candidate-evidence-lifecycle)
to each required installed-package lane. An earlier green matrix does not certify a
changed candidate or dependency closure.
If a repository permits a release with an unmet, specialized gate, record the separate
[bounded release-gate exception](release_version_policy.md#bounded-release-gate-exceptions)
while keeping that lane's actual status visible. The decision applies only to its
named candidate and scope; it does not waive an installed-package lane required
for a claimed operating system, add a support claim, or turn the lane into passing
evidence. The macOS support exception above remains a tracked limitation of the
component's supported-OS claim, with its own exit condition.

## Local freedom

Repositories choose workflow structure, environment solver, additional architecture
and specialized tests according to their risks. The shared contract concerns
observable support, not identical YAML. If a claimed platform's required evidence
fails, the component fixes the failure or narrows its public claim before release.
