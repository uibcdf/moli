# MOLI repository badge policy

Badges make bounded claims and must link to authoritative, current evidence.

## Baseline and order

A MOLI repository README should identify its MOLI role or governance relationship,
applicable Python support when relevant, and license. A policy workflow badge may
appear only when the named workflow exists and its link targets that repository.
Delegated governance may define additional role badges for its members.

After the baseline, display only maintained capabilities, in this order: continuous
tests, coverage, deployed documentation, public release, DOI, and distribution.
Omit a category whose evidence is unavailable. Workflow names must match their
actual function; a policy-only check is not a test badge, and a documentation build
is not a deployed-site badge. A static green badge cannot replace live evidence.

## Coverage percentage

For a repository with meaningful tested executable code, maintain a coverage
producer in its actual CI and display Codecov's **live percentage** in its main
README when a recent complete default-branch report has been accepted. Put the
badge between tests and documentation, link it to that repository's Codecov
project, and use its actual default branch. Never type a percentage into README,
use a static image, expose a token, silently restrict the badge to a favorable
flag, or point to another repository. A coverage percentage describes only the
instrumented code and test selection; it is not a scientific correctness score,
a full-platform certification or a coverage minimum.

Review every directly governed component and MOLI itself. Incubating repositories
without meaningful executable code may record non-applicability with the condition
that triggers reassessment. A missing upload, an `unknown` SVG, an HTTP failure,
or a configured workflow is not evidence of non-applicability or of a percentage.
The direct Python-component registry carries an owner-local `coverage_review`;
MolSysSuite decides member adoption under its own badge policy.

For every advertised percentage, record the measured source commit, report scope,
cadence, accepted Codecov report and last observed upload time. A weekly report
may lag a later push, so name its cadence and never describe it as coverage of
the current commit unless it is. Keep an absent or stalled badge withheld and
track the producer defect with the owner. Offline README checks can validate
the badge's own repository, branch and shape; current percentage and upload
recency require separate network evidence.

The release badge requires a public release. A DOI badge requires the independently
verified public record and resolving DOI described in the
[Zenodo policy](zenodo_policy.md); use the concept DOI for a persistent project badge
when the badge claims the evolving project. A distribution badge requires a
published, verified package on the linked channel under the
[distribution policy](python_distribution_policy.md). A Git tag or release workflow
alone proves neither archival nor package availability.

Review badges after releases and service changes. Remove or correct a claim that no
longer matches its linked evidence.
