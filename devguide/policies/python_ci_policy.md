# MOLI Python CI Policy

Normative for MOLI components carrying the `python-package` capability.

## Routine gate

Every push and pull request has a gating Linux test lane on the routine development Python version (currently 3.13).

## Operating-system support

Linux and macOS are the platform baseline for public MOLI Python packages. A
component is expected to support both. Linux is mandatory; a component that cannot
yet support macOS records a bounded exception with its reason, owning issue and exit
condition, and states the limitation in its README. Windows is optional: its absence
does not block a release or count as a policy exception. A component may add Windows
when it can maintain the evidence below.

The `supported_os` list in `moli.toml` records the operating systems a directly
governed Python component currently claims. Its `os_support_review` points to a
component-owned issue and has a `pending`, `partial`, `adopted` or `excepted` state.
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
Python minor (currently 3.11, 3.12, 3.13). On macOS, at least the routine Python
minor runs the required tests weekly; the same applies to Windows if claimed.
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

## Local freedom

Repositories choose workflow structure, environment solver, additional architecture
and specialized tests according to their risks. The shared contract concerns
observable support, not identical YAML. If a claimed platform's required evidence
fails, the component fixes the failure or narrows its public claim before release.
