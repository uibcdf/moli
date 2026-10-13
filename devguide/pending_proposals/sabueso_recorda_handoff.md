---
summary: Receive original Sabueso artifacts with separately recorded consumption.
issue: uibcdf/moli#36
status: active
opened: 2026-10-13
closed:
verification: inspected
area: [knowledge-attribution, interoperability]
blocked_by: []
supersedes: []
---

# Sabueso receiving exercise with Recorda

The [public application example](../../examples/sabueso_recorda/README.md) retains
the original observed Sabueso comparative bundle and records actual application
consumption through Recorda's existing explicit-operation API. This is a ready
review contribution to #36, not acceptance of a ProjectRecord wire schema or
implementation of the broad routing/context specification in [RECORDA.md](../RECORDA.md).

The owner-issued manifest, scientific report, runtime credit and closed store are
copied byte-identically. Sabueso's own reader verifies original pins/support,
rules/results and credit. A separate Recorda parent and three child operations
retain original result/execution identities and producer versions; CSL-JSON/BibTeX
exports use the original saved workflow. Receiver/software versions never replace
the original producer. A caller may prepare a scoped closed store using native
exact-pin load/save with full-snapshot equality, without rewriting the original
store or discarding assertions within a retained Card.

Independent inspection uses Recorda without importing Sabueso, Ackredit or its
scientific producers. It checks exact local file occurrences and links the
consumer record back to the original runtime. Card pins remain explicitly
unresolved without their owner; matching store bytes do not resolve scientific
meaning. Execution success, current availability, authorization and interpretation
are separate. Missing/changed files retain successful historical execution with
unavailable hand-off status. Invalid bundles retain failed attempts; failure to
publish the final index remains an incomplete hand-off even if recording succeeded.

Nineteen public integration regressions pass locally through pytest-receptor with
twelve workers, Python 3.14 and fatal SQLite/unraisable guards. Cases cover exact
original retention/credit, parent-child correlation, no acquisition/derivation/new
credit under a changed reader version, unavailable/changed files, misbound index/
producer/pins/journal, unauthorized interpretation claims, refused overwrite,
explicit file budgets including CLI propagation, incomplete final publication,
native scoped-store copying, a producer-free subprocess reader and actual
reception of compact operation `@2` with retained original input scopes. The existing
MOLI governance suite passes all 41 cases; governance and Ruff pass.

Local participants are editable checkouts of Sabueso, Recorda 0.3.0, Ackredit and
their compatible support providers in the existing shared development environment.
The source integration also revealed repeated full input scopes in comparative
credit; the separate compact `@2` correction remains Sabueso #108/#112 work.
Its source gates and publication are not inferred from this receiving exercise.

A separately declared Linux/Python 3.14 workflow receives pinned public Sabueso
`792bd0da45245ad0fca08e4b431e5e49e4d76ae8` with installed public Recorda 0.3.0 and
Ackredit 0.9.0. Its exact-source [CI passes 15/15](https://github.com/uibcdf/sabueso/actions/runs/38456975623)
and [governance passes 1/1](https://github.com/uibcdf/sabueso/actions/runs/38456975421)
in Sabueso, verified from complete receptor captures. The earlier PR source
`fc110e882f3b5887d64fedcc60fca46250c062eb` passes
[18 hosted receiving cases](https://github.com/uibcdf/moli/actions/runs/38454271829)
and [applicable governance](https://github.com/uibcdf/moli/actions/runs/38454272358)
using prior qualified Sabueso `25f6163`. That receipt remains historical and does
not qualify this updated source pin or new case. Complete exact-head receiving
and governance checks remain required for this revision. Broader OS/minor and
installed-artifact acceptance remain separate from local source checks.

No private pilot data, results or new aggregates enter this contribution. Existing
private workflows may be assessed read-only through a separate ignored receiving
harness; that does not modify their notebooks or close scientist acceptance.

Keep #36/#18 open for project/campaign context, retention/availability policy,
EventLedger routing/correlation, CPU/GPU/resource accounting and consequential
commit policy. Nextia's owner must separately perform explicit interpretation;
this example creates neither Evidence nor permission. General self-contained
archives/replay, transactional durability and multi-process/distributed guarantees
remain outside its declared coverage.
