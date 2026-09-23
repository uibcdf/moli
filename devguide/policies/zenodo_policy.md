# MOLI Zenodo and DOI Policy

This policy governs archival claims for MOLI repositories when Zenodo archival applies.

## Principle

A GitHub Release, metadata file, reported integration toggle, or webhook is not proof of archival. Only an independently verified public Zenodo record permits an archival claim.

## DOI semantics

Use the concept DOI for the evolving project and a version DOI for one immutable release.

## Metadata

`CITATION.cff` is the GitHub-facing citation record. If `.zenodo.json` is also used, shared metadata must agree before publication.

## Verification

For a release intended for archival:

1. validate metadata;
2. run repository release gates;
3. publish deliberately;
4. allow bounded ingestion time;
5. independently verify repository identity, version, DOI(s), access state, and archived files;
6. publish DOI claims only after verification.

Credentials, hooks, tokens, cookies, or signed URLs must never be stored in repository evidence.

## Applicability

Archival requirements may depend on repository maturity and release intent. Applicability and exceptions must be explicit rather than inferred from another component.
