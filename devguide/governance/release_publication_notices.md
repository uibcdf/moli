# Release and package-publication notices

Accepted by Diego in [MolI #75](https://github.com/uibcdf/moli/issues/75).
Every new component release, including a source-only release without a package,
and every new package publication receives an issue notice in its owning
governance domain:

| Event owner | Central notice destination |
| --- | --- |
| Direct MolI component outside MolSysSuite membership | `uibcdf/moli` |
| MolSysSuite member | `uibcdf/molsyssuite`, under its own member rule |

MolSysSuite owns member policy and rollout under
[suite #129](https://github.com/uibcdf/molsyssuite/issues/129). MolI does not
edit suite/member sources. Shared auxiliary providers use their governing
domain and retain the separate advance impact-notice obligation below.

## Trigger, owner and notice contents

The component's release/publication maintainer records the event as part of its
closeout. Open a release-specific central issue or use the existing issue for
that same release. Update that notice when a source-only release later gains
package files, another build or another publication route. Do not duplicate the
same event or treat a general policy issue as every release's notice.

Use the [notice template](../templates/release_publication_notice.md). Include:

- Component/repository, event type, exact version, responsible maintainer and
  owning implementation/release issue.
- Immutable source commit, tag/target and release URL where they exist. State
  source-only, unpublished or pending-package scope explicitly; an intended
  package coordinate is not an available package.
- For an actual package: channel/label or index, subdirectory/platform, exact
  filename, version/build and SHA-256; distinguish the producer identity from
  later documentary commits. Retain original files and qualification receipts.
- Actual producer, installed/public verification evidence and its limits,
  including unavailable or unexecuted gates. A source tag, successful build or
  upload alone does not establish a usable public dependency closure.
- Relevant ecosystem/provider versions and consumer pins, plausible compatibility
  effects, explicit unknowns and the owners/issues for receiving or other work.
  Availability is not consumer adoption or certification of future versions.

A release-specific example is [Recorda 0.3.3, #78](https://github.com/uibcdf/moli/issues/78):
its initial source-tag notice and later exact public-file evidence describe
different observed states in the same notice. The example is historical
evidence for that release, not a current package recommendation or a substitute
for reviewing the original receipts.

## Coordination boundaries

This is **post-event reporting**, not central pre-release permission, automatic
dependency/pin updates or a new requirement to run scientific suites. The
component still owns its release authority, candidate gates, compatibility and
scientific acceptance. Never move an immutable tag, rebuild an existing file or
claim an unavailable package to satisfy a notice.

For foreseeable effects of a shared provider change, give the existing
[advance impact notice](cross_component_feedback.md#changes-to-shared-auxiliary-providers)
before publication/consumer rollout. The post-event release notice does not
replace it. A single existing issue can carry both when it explicitly preserves
their distinct timing, scope and evidence.

Keep confidential/security material private. A reporting exception records its
owning issue, responsible owner, reason, interim controls and review/exit
condition in the governing domain; it does not erase the underlying event or
authorize disclosure. Internal notice authority does not authorize an external
issue or PR; follow the [external-publication rule](external_publication_authority.md).

## Delivery and future compliance

Root contributor instructions, the canonical guide, onboarding and templates
carry the reporting action. The [adoption record](publication_policy_adoption.md)
tracks component-owned instruction/guide commits and verification separately
from this central policy. Neither opening an adoption issue nor copying a
guide proves compliance of later release/publication events.
