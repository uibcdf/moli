# Reporting Protocol

## Stable identity

GitHub issues are the stable identity for bugs, proposals, and coordination work.

## Where to report

- one-component bug/proposal → owning component repository;
- provider limitation discovered by another component → provider repository, with consumer context;
- shared contract affecting two or more directly governed MOLI components → `uibcdf/moli`;
- MolSysSuite-internal concern → follow MolSysSuite governance;
- concern crossing Scientific Context/MOLI Agent and MolSysSuite → `uibcdf/moli`, with linked implementation issues where required.

## Durable analysis

Use an owning repository's `devguide/` when an issue needs durable alternatives, evidence, rationale, migration notes, or acceptance criteria. The issue remains the stable public identity.

MOLI does not yet require the full MolSysSuite report/archive machinery. Introduce additional lifecycle automation only when real governance load justifies it.

## Confidentiality

Never move confidential scientific content into a public issue merely to satisfy reporting. Use sanitized evidence and reference the existence of controlled/private material where appropriate.

## Closure

A shared-contract issue should close only when the normative decision is recorded and affected implementation work is either complete or explicitly tracked elsewhere.
