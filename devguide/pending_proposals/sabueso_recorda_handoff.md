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

Eighteen public integration regressions pass locally through pytest-receptor with
twelve workers, Python 3.14 and fatal SQLite/unraisable guards. Cases cover exact
original retention/credit, parent-child correlation, no acquisition/derivation/new
credit under a changed reader version, unavailable/changed files, misbound index/
producer/pins/journal, unauthorized interpretation claims, refused overwrite,
explicit file budgets including CLI propagation, incomplete final publication,
native scoped-store copying and a producer-free subprocess reader. The existing
MOLI governance suite passes all 41 cases; governance and Ruff pass.

Local participants are editable checkouts of Sabueso, Recorda 0.3.0, Ackredit and
their compatible support providers in the existing shared development environment.
The source integration also revealed repeated full input scopes in comparative
credit; the separate compact `@2` correction remains Sabueso #108/#112 work.
Its source gates and publication are not inferred from this receiving exercise.

A separately declared Linux/Python 3.14 workflow receives pinned public Sabueso
`25f6163b306a1a863e7ceb5b8e660bdbd2cef432` with installed public Recorda 0.3.0 and
Ackredit 0.9.0. That baseline is source-qualified in its own repository. Hosted
execution of this new receiving workflow, broader OS/minor and installed-artifact
acceptance remain separate from these local source checks.

No private pilot data, results or new aggregates enter this contribution. Existing
private workflows may be assessed read-only through a separate ignored receiving
harness; that does not modify their notebooks or close scientist acceptance.

Keep #36/#18 open for project/campaign context, retention/availability policy,
EventLedger routing/correlation, CPU/GPU/resource accounting and consequential
commit policy. Nextia's owner must separately perform explicit interpretation;
this example creates neither Evidence nor permission. General self-contained
archives/replay, transactional durability and multi-process/distributed guarantees
remain outside its declared coverage.
