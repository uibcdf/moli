# MOLI Zenodo and DOI policy

This policy governs archival and citation claims for MOLI repositories when Zenodo
archival applies. A component owns its publication decision and exact-release evidence;
delegated governance may track member applicability and rollout separately.

## Metadata authority

Maintain `CITATION.cff` as the GitHub-facing citation record. Use it alone when it
expresses the needed metadata. Add `.zenodo.json` only for Zenodo-specific fields:
Zenodo uses that file in preference to `CITATION.cff` during GitHub release ingestion.
If both exist, validate their shared title, creators, identifiers, license and
repository relation before publication. A contradiction is a release blocker.
Zenodo documents the [citation-file precedence](https://help.zenodo.org/docs/github/describe-software/citation-file/)
and [Zenodo-specific metadata file](https://help.zenodo.org/docs/github/describe-software/zenodo-json/).

## Evidence and DOI meaning

A GitHub Release, citation file, reported integration toggle or webhook is not proof
that an archive exists. Record the observed state as `unknown`, `enabled_reported`,
`webhook_observed`, `release_published`, `ingestion_pending`, `verified`, `absent`,
`invalid`, `temporarily_unavailable` or `not_applicable`. Only `verified` authorizes
an archival claim. A bounded wait after publication is `ingestion_pending`, never
success; record the retry limit and observation date. `not_applicable` requires an
explicit, tracked applicability decision or exception.

The concept DOI identifies an evolving project or all its archived versions. Use it
for a stable project badge when that is the intended claim. A version DOI identifies
one archived release and is used for exact-version citation and reproducibility.
Neither DOI may be inferred from a tag, copied from another repository or announced
before its own public record is verified. Both DOI links must resolve through
`doi.org` to the expected public record before they appear in a README, badge,
citation instructions or release announcement. A newly registered DOI may need a
bounded propagation interval; a non-resolving DOI remains pending.
Zenodo explains [concept and version DOI use](https://zenodo.org/help/versioning);
DataCite notes [DOI resolution can lag registration](https://support.datacite.org/docs/mds-api-guide).

## Release verification

For each release intended for archival:

1. Validate citation metadata and any `.zenodo.json` agreement. Run the repository's
   complete release gates on the exact candidate commit.
2. Publish deliberately and record the exact GitHub tag, release and asset inventory.
3. Poll the anonymous public Zenodo record with a documented retry limit. If the
   service is unavailable, record `temporarily_unavailable`; if the limit expires
   without a matching record, record `absent`, not `verified`.
4. Independently match repository identity, software type, exact release version,
   public access, concept and version DOIs, and every archived file's name, size and
   checksum. A mismatch is `invalid`.
5. Resolve both DOI links through `doi.org` and confirm their destinations identify
   the expected project and version. Record `verified` only when the public archive
   and DOI resolution pass. Keep dated, sanitized evidence and periodically recheck
   claims exposed in public documentation.

State archive coverage exactly: a source snapshot does not prove that a wheel,
Conda package, checksum manifest or GitHub Release asset was deposited. Publication
to the `uibcdf` Conda channel has its own verification under the
[distribution policy](python_distribution_policy.md); neither surface proves the
other.

For a public release with archival intent, maintain a short **Current release
status** section in the README. Name the exact release version and state, link the
verified version DOI and concept DOI when available, and say which artifacts the
Zenodo record actually contains. While ingestion or DOI resolution is pending,
state that fact without displaying a DOI badge or claiming archival. Keep the section
in agreement with the public record and distribution state.

Credentials, hooks, tokens, cookies and signed URLs must never be stored in
repository evidence.

## Applicability

Archival requirements may depend on repository maturity and release intent.
Applicability and exceptions must be explicit rather than inferred from another
component. MolSysSuite owns its member inventory and any stricter member-specific
release gate.
