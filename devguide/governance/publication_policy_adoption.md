# Publication policies: central delivery and owner adoption

## Scope and status — 2026-11-04

The principal maintainer selected central work on [#75](https://github.com/uibcdf/moli/issues/75)
and [#80](https://github.com/uibcdf/moli/issues/80), explicitly leaving component
implementation to each development team. MolI now supplies the normative
[external-publication authority](external_publication_authority.md),
[release/publication notice rule](release_publication_notices.md), registry,
canonical guide, root action, onboarding and starter/template changes.

**Central source delivery is distinct from adoption.** Both issues remain
partial until their outstanding owner delivery criteria have evidence. No
component or suite/member source is edited by this central task. The
[prepared owner requests](../pending_proposals/publication_policy_owner_drafts.json)
are local/internal drafts, not published issues or proof of delivery. Automatic
approval review rejected the first attempted Sabueso issue creation, requiring
explicit destination/content permission; no owner issue was created. Publication
of those concrete drafts awaits human authorization. Internal MolI policy work
and reporting continue.

## Component-owned work

For each component, its team receives the exact published canonical guide,
preserves existing root instructions while adding both actions, updates its
applicable release-closeout route and returns immutable source, checked guide
equality and executed native governance evidence. Scaffolds adopt contributor
instructions without inventing a publisher or runtime. The registered delivery
checker is `devtools/scripts/check_component_guides.py`; an owner can also use
`check_repository.py <checkout> --canonical-guide MOLI_GUIDE.md` from MolI.
The checker verifies copies/routes, not the meaning or future compliance of an
instruction. Keep that owner review explicit.

| Component | Inspected source | Instruction/guide adoption |
| --- | --- | --- |
| Sabueso | `129020182555787d3cab58cc110e7a707fc5e553` | Pending team delivery; draft request prepared |
| Praxis | `17e1856fa45a50b26097b19be28accb7ab88f689` | Pending team delivery; draft request prepared |
| Nextia | `32d12e20fae26f00a523d0ed4812e46def8a64e9` | Pending team delivery; runtime remains deferred |
| Moli | `08d0e2b809e7e5c46add5ee554ae9528831f7454` | Pending team delivery; draft request prepared |
| Recorda | `ff52fa5d8628d796f413b833c8abe73907990cf9` | Pending team delivery; draft request prepared |

All five inspected copies have the former canonical SHA-256
`12104363c7fd0cc4ca99e4a3d3b77fe85e9a44e3ab49e88936900df3efac2a3c`.
The new canonical guide SHA-256 is
`618f79bff3d519e6949d5373aec4cf3bfaebeb1cbf7a8dba31f12cfd36665cf2`.
Local inspection reports exactly five copy differences. The hosted guide audit
remains active and may report these pending copies; do not suppress, skip or
relabel that result. The final native run evidence belongs in #75/#80's delivery
comments. Central governance/administrative tests and component-copy adoption
have separate results.

## MolSysSuite delegation

[Suite #129](https://github.com/uibcdf/molsyssuite/issues/129) owns the separate
release-notice member rule and delivery. [Suite #159](https://github.com/uibcdf/molsyssuite/issues/159)
owns member external-publication instructions. Their reported deliveries are
not evidence for the five direct copies above. The prepared return comments
identify central delivery and its limits; their publication awaits the same
specific human authorization as the owner requests. Suite/member sources and
their policy-release identities remain unchanged by this task.

## Separate developer-tool review

[MolI #79](https://github.com/uibcdf/moli/issues/79) reviews GH Run Receptor
1.4.0 independently. The [source-bound inventory](../evidence/gh_run_receptor_79_20261104.json)
records the inspected inputs and dispositions. No maintained executable or
operator-installation version pin was identified in the five component snapshots;
generic inspection commands and historical tool-version receipts remain intact.
The central task uses the published 1.4.0 wheel in isolated scratch without
changing operator environments. This is not provider requalification, an installed
upgrade of other users, scientific acceptance or a new platform minimum.
