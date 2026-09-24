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

The release badge requires a public release. A DOI badge requires the independently
verified public record and resolving DOI described in the
[Zenodo policy](zenodo_policy.md); use the concept DOI for a persistent project badge
when the badge claims the evolving project. A distribution badge requires a
published, verified package on the linked channel under the
[distribution policy](python_distribution_policy.md). A Git tag or release workflow
alone proves neither archival nor package availability.

Review badges after releases and service changes. Remove or correct a claim that no
longer matches its linked evidence.
