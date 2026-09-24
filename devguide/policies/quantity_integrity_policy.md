# Physical quantity integrity across MOLI

This policy applies to every MOLI component and UIBCDF support tool that produces,
transforms, stores, or communicates physical quantities. MolSysSuite inherits the
platform contract and records adoption and exceptions for its members. A component
owns its scientific meaning, input vocabulary, persisted schema, and migration.

## Required guarantees

1. A quantity crossing a public API or persistence, process, or component boundary
   must retain its value, unit, and scientific meaning. An unlabelled number, a unit
   inferred from a field name or session setting, and a separately documented unit
   are insufficient at a serialized boundary. The negotiated unit belongs inside
   the same serialized object as the values, including for arrays or columns.
2. Writers use PyUnitWizard's quantity conversion and serialization facilities
   where the relevant format is supported. Readers verify the serialized record
   and explicitly declare the expected field and unit or dimensionality. There is
   no implicit default unit, silent reinterpretation, or fallback after verification
   fails. The codec and its format are owned by PyUnitWizard; components must not
   create private competing codecs. See the [design record](https://github.com/uibcdf/pyunitwizard/issues/83)
   and [implementation](https://github.com/uibcdf/pyunitwizard/issues/82).
3. An in-process API that promises a physical quantity returns a quantity, unless
   the caller explicitly requests a numeric value in a named unit. Conversion at
   an external boundary names the target unit explicitly; it must not depend on
   the session's standard-unit policy. Check dimensions and, where dimensions
   alone are ambiguous, the quantity kind.
4. A source's original value, unit spelling, stated precision, and provenance
   remain available when normalization is performed. Translate source-specific
   unit vocabularies explicitly; case folding or passing unknown source strings
   straight to a unit parser can change their meaning.
5. Version a persisted schema when its quantity representation changes. Readers
   reject missing, ambiguous, unsupported, or inconsistent unit metadata instead
   of guessing. For a storage format not yet supported by PyUnitWizard's verified
   codec, track the migration and document a bounded, tested compatibility route;
   do not claim that the format is verified by the codec.

## Evidence for adoption

Each component that handles quantities inventories quantity-bearing paths and
their units, including frontend messages and stored columns. Test representative
scalar and array round trips, wrong units and dimensions, missing metadata,
modified values or units, and a non-default session policy. Include a cross-component
canary for scale errors such as 3 nanomolar being read as 3 picomolar. A digest or
record check cannot detect a source or writer that is wrong but internally
consistent; add domain-specific plausibility or cross-source checks where evidence
supports them.

The [platform tracking issue](https://github.com/uibcdf/moli/issues/12) records
the shared acceptance criteria. [Sabueso #32](https://github.com/uibcdf/sabueso/issues/32)
is the first consumer. [MolSysSuite #46](https://github.com/uibcdf/molsyssuite/issues/46)
tracks member adoption, including [MolSysMT #240](https://github.com/uibcdf/molsysmt/issues/240)
and [MolSysViewer #96](https://github.com/uibcdf/molsysviewer/issues/96).
PyUnitWizard 0.27.0 publishes a provisional QuantityRecord API for supported
encodings; support for additional container formats and release stability remain
tracked by its implementation issue. Follow its published API and compatibility
status before migrating an existing persisted format.
