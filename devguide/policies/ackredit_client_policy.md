# Ackredit contracts for direct MOLI consumers

Accepted under [MOLI #46](https://github.com/uibcdf/moli/issues/46) for
owner-selected use by direct components. Ackredit owns its APIs, schemas and
[canonical integration guide](https://github.com/uibcdf/ackredit/blob/main/standards/ACKREDIT_GUIDE.md).
MolSysSuite owns its independent
[member policy](https://github.com/uibcdf/molsyssuite/blob/ca96503f1049fcf7b16c8dd364510e8f1468a891/devguide/ackredit_client_policy.md)
and member adoption. Neither domain's acceptance certifies the other's consumers.

## Capability and public compatibility boundaries

| Chosen capability | Qualified public promise starts at |
| --- | --- |
| Detached portable attribution, `ackredit.attribution@1`, `Attribution`, `capture` and `get_attribution` | Ackredit 0.9.0 |
| `prepare_credit`, explicit `observe_calls`, and `ackredit.provider@1` interpretation | Ackredit 0.11.0 |
| Bounded `AttributionEvidence`, opt-in capture evidence and explicit integrated evidence reporting | Ackredit 0.12.0 |
| Standalone `validate_provider(module) -> dict` | Ackredit 0.12.0 |

These are capability floors, not a dependency specification or an instruction
to upgrade. Preserve the consumer's tested range, including upper bounds, and
qualify its actual provider and dependency closure before claiming released
compatibility. Required dependencies remain component product decisions;
accepting optional capabilities does not make a required dependency optional.
A portable-only consumer need not adopt observers, evidence or validation.

The provider promises reviewed meanings/signatures and versioned saved
interpretations across later patch/minor releases, including remaining pre-1.0
and 1.x for these bounded promises, under its own deprecation policy. Private
implementation and every presentation byte are not frozen.
Public 0.10.x retains provisional function-provider classification. Public
0.11.0 retains provisional recorder evidence and lacks standalone validation.
General public 1.x stability requires a separate qualified delivery. Original
artifacts retain their original promises. The
[decision inventory](../archive/review_ackredit_optional_contracts.md) identifies
immutable sources, public files, receiving evidence and direct-consumer limits.

## Responsibilities when a consumer chooses a capability

1. **Own bibliography and scientific meaning.** Keep declarations offline and
   check them against original works. Preserve original software/article
   identities, versions, use roles and scope. Installation or declaration is
   not observed use. The host decides when prepared credit is earned; observed
   entry alone does not establish successful scientific completion.
2. **Keep activation and sessions application-owned.** Libraries do not
   automatically enable observers, hooks, enrichment, journals or reminders.
   Contribute to the current session and captures rather than replacing them
   or subtracting deduplicated session IDs to infer a result's bibliography.
   Optional integrations defer provider loading to their requested boundary
   and preserve their documented absent-provider behavior. Required consumers
   retain their own dependency and initialization contract.
3. **Retain the observation limits.** Follow the canonical ownership/restoration
   contract for declared synchronous exports and executed awaited coroutines.
   Pre-activation aliases, generators, descriptors, native internals and
   subprocesses are not silently covered. Validation of a trusted imported
   module proves neither calls, registry compatibility, scientific correctness
   nor complete instrumentation; producer lazy-loader effects remain local.
4. **Preserve detached original records.** Each result retains reused references
   even when another result already used them. Keep owner-issued result links,
   original versions, observed bibliography, roles and explicit gaps alongside
   the scientific payload. Saved readers add no credit, science, enrichment or
   replacement by current metadata. Provider payloads do not define a universal
   host sidecar or project schema.
5. **Keep evidence opt-in and bounded.** Preserve original occurrence association,
   including repeated names, and the separate metadata-source, selected/
   unobserved-boundary and diagnosed-gap planes. `null` and `[]` retain different
   meanings. Automatic collection concerns active overlapping observers/captures
   in the same session; other recorder origins remain unknown. Saved reading
   emits no stored diagnostic again. Integrated evidence reporting is explicit
   and preserves the default report contract.
6. **Expose failure under the host's policy.** Distinguish scientific failure,
   recording failure, unavailable attribution and partial records. Preserve
   scientific exceptions and actual warning-as-error behavior. Optional
   provider failure preserves completed science and host-owned provenance while
   diagnosing incomplete tracking; a project may impose a stricter explicit
   commit policy. Required consumers document and test their failure rule.
   A scientific result alone does not establish complete attribution.

Source support, terms, disclosure permission, execution history and project
Evidence retain their owners under Architecture 1.0. A citation or attribution
record establishes none of those other decisions. `AttributionEvidence` describes
attribution recording; it is not Nextia Evidence.
[MOLI #36](https://github.com/uibcdf/moli/issues/36) retains shared exchange and
project integration.

## Receiving and owner-local adoption

Record chosen capabilities, exact host/provider versions, activation/failure
policy, supported paths and limits in the consumer's owning issue. Use real
receiving evidence appropriate to that choice: two results reusing a reference
and an enclosing workflow; observed versus untaken paths; evaluated-empty and
failed science; detached ownership; fresh readers preserving original versions
without new credit; and relevant provider faults, cleanup and warning filters.
Optional integrations also demonstrate genuine absence and deferred loading.
Evidence users test partial recording, occurrence association and explicit
reporting. Exercise any claimed older-provider fallback with that released
provider.

An installed flag, mock, declaration check, provider matrix or guide copy alone
does not qualify a current consumer. Retain tested source, artifact identity
and supported environments before release claims. Existing bounded receiving
keeps its original scope; later capabilities do not invalidate a completed
older pilot or require reopening it.

This review requires no universal dependency, version bump, consumer code or
guide-copy rollout, new recorder integration or deferred Nextia implementation.
Owners adopt when a concrete use case calls for it. Report provider defects
there and cross-link consumer work under the
[feedback policy](../governance/cross_component_feedback.md).
