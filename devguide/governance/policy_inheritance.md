# MOLI policy boundary and delegated governance

MOLI governs the components directly registered in `moli.toml`. Its engineering
policies apply to those components according to their declared capabilities.
They do **not** pass automatically through a component with delegated internal
governance to that component's members.

MolSysSuite is a directly registered MOLI component and remains accountable to
MOLI for platform contracts: cross-component interfaces, scientific quantity
integrity, issue feedback, and applicable support-infrastructure cooperation.
`uibcdf/molsyssuite` is the normative owner of policies for its registered
members, including Python support, CI, Ruff, runtime support libraries,
developer tools, distribution, release versions, badges, and archival rules.
Its `suite.toml`, policy documents, release tags and conformance machinery
define the effective member rules and their rollout. MOLI neither registers
member adoption state nor directly validates those member policies.

MolSysSuite may choose a rule compatible with a MOLI policy, refer to a MOLI
document for context, or deliberately revise its own member rule. Such a choice
is a MolSysSuite governance decision; a new MOLI revision does not silently
change member obligations. A change that affects MolSysSuite's obligations as a
MOLI component or an interface with another MOLI component requires a MOLI
decision as well. A suite policy cannot waive a platform contract by changing
its member wording.

UIBCDF-owned developer tools and publication actions are separately cataloged
as [support infrastructure](support_infrastructure.md). Their provider
repositories own implementation and defects. MolSysSuite decides how its
members use them while observing any platform-facing contract that applies to
the suite itself.

## Reproducible sources

Direct components use the MOLI registry and canonical guide. MolSysSuite
records any MOLI revision it uses to verify its own platform obligations, but
that reference is not a source of member engineering values. Member conformance
uses a versioned MolSysSuite policy release. Historical results name the exact
suite release; moving branch links are for discovery.

## Guide delivery

`components.<name>.guide_delivery` records how a directly registered component
receives MOLI guidance. `vendored` means a byte-identical root `MOLI_GUIDE.md`.
`reference` means a delegated governance repository routes readers to MOLI
without copying that guide. This choice does not give MOLI authority over the
delegated members.

Direct components with `vendored` delivery keep a root `AGENTS.md` pointing to
the guide. `devtools/scripts/check_component_guides.py` checks those copies.
