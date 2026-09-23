# MOLI Python support libraries policy

Normative for MOLI components carrying the `python-package` capability. MOLI owns the
cross-component applicability rule. MolSysSuite governs its member libraries and its own
adoption inventory; its members inherit this baseline through the suite.

## Applicability

Review each boundary in a Python component and use the corresponding UIBCDF library when
that boundary exists:

- **ArgDigest:** nontrivial constraints, normalization, or validation of arguments at a
  public API boundary. Ordinary Python type errors alone do not create a dependency.
- **DepDigest:** optional, heavy, or backend-specific dependencies whose availability and
  loading need to be managed and explained to users.
- **SMonitor:** diagnostics that users need to see, including recoverable failures and
  incomplete operations. Scientific outcomes and provenance remain component data;
  SMonitor does not replace them.
- **PyUnitWizard:** physical quantities that require unit parsing, conversion, or
  dimensional validation. A component owns its persisted schema: using PyUnitWizard at
  runtime does not require serializing its Python objects or changing existing card
  values. A shared schema change follows the normal MOLI contract process.

Do not add an unused library solely to satisfy this policy. A component's review issue
records each applicable use, non-applicability with a reason, and any replacement of
hand-built code. A temporary exception records its reason, owner, tracking issue, and
exit condition. A component admitted to a Python-version transition verifies that its
chosen published library releases support every Python minor it claims.

## Adoption evidence

Direct Python components register a `python_ecosystem_review` issue and state in
`moli.toml`. Allowed states are `pending`, `partial`, `adopted`, and `excepted`.
`adopted` means the applicability review is complete and every applicable use has
implementation and test evidence; it does not mean all four libraries are dependencies.
`excepted` requires the recorded bounded exception. A registry state is a pointer to
evidence, not proof that imports or behavior conform.

New direct components cannot enter the registry as Python packages without this review.
The central guide audit also detects a declared Python project that lacks the
`python-package` capability. Delegated governance records member-level rollout and
exceptions in its own inventory.
