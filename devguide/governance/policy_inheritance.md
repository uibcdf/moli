# MOLI policy inheritance

MOLI is the sole normative owner of engineering rules that apply across its
components. `moli.toml` identifies each accepted policy, its applicability, and
its normative document. A component with delegated internal governance passes
applicable MOLI policies to its registered descendants according to their
capabilities. Delegation changes who coordinates adoption, not who owns a rule.

MolSysSuite therefore references MOLI policies for its members. Its registry
may record member classification, adoption state, evidence, bounded exceptions,
and explicit modeling-domain extensions. It must not independently redefine
MOLI-wide Python support, CI, quality tooling, release-version, badge, or DOI
rules. A stricter suite requirement identifies the inherited rule and states
only the additional requirement and its applicability.

## Policy snapshots and verification

Automated conformance uses an immutable MOLI Git commit or policy release as its
source of general policy values. The chosen reference is recorded alongside the
consumer's policy caller so a past result can be reproduced. A moving branch
is suitable for discovery, not for a required conformance gate.

Conformance checks evaluate the inherited baseline from that MOLI snapshot.
Delegated governance may run those checks, add checks for its own contracts,
and track adoption across its members.
An adoption inventory distinguishes the policy version a member has adopted
from the current MOLI baseline; publication of a new baseline does not imply
that every member has already adopted it.

## Guide delivery

`components.<name>.guide_delivery` records how a directly registered component
receives MOLI guidance. `vendored` means it keeps a byte-identical root
`MOLI_GUIDE.md`. `reference` means a delegated governance repository routes
readers to MOLI without copying that guide. This delivery choice does not
change policy inheritance or platform membership.
