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
  dimensional validation. A component owns its persisted schema and migration, and
  follows the [platform quantity integrity policy](quantity_integrity_policy.md)
  whenever quantities cross a boundary. PyUnitWizard owns the shared serialization
  design and codec; follow its [canonical guide](https://github.com/uibcdf/pyunitwizard/blob/main/standards/PYUNITWIZARD_GUIDE.md#storing-and-exchanging-quantities-provisional)
  and read the [design record](https://github.com/uibcdf/pyunitwizard/issues/83)
  before proposing a format or alternative. Runtime use alone does not silently
  establish that a persisted schema conforms.

## PyUnitWizard configuration authority

PyUnitWizard has one active unit policy per Python process. A component must not
replace its process-wide standard units, default quantity form, or default string
parser on import or first use. In particular, importing components in a different
order must not override a policy already chosen by the application or user.

Configuration authority follows this order, strongest first:

1. An explicit target unit, form, or parser supplied to the API call.
2. An explicitly activated local context, within PyUnitWizard's documented
   context and concurrency limits.
3. The application or interactive session's selected policy.
4. PyUnitWizard's factory defaults.

When no policy is active, a governed ecosystem may initialize its *shared*
baseline once. Its governance owns the baseline's content and adoption; this
bootstrap must not replace an active application policy or introduce a different
implicit default for each member. [MolSysSuite #18](https://github.com/uibcdf/molsyssuite/issues/18)
tracks that ecosystem's baseline and migration. Components outside such an
explicitly governed baseline consume the active policy without setting global
defaults themselves.

A component's scientific API and persisted schema still own their documented
unit contracts. Request a required unit explicitly at the operation boundary;
do not let an ambient display or standard-unit preference change a persisted
unit or a fixed-unit scientific result. An API intended to follow the session
policy must say so. Adoption evidence should cover application configuration
before component import, import and first-use order, and fixed-unit behavior
under a non-default policy. The [platform issue](https://github.com/uibcdf/moli/issues/11)
tracks this cross-component authority rule.

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
