# MolI and Moli naming convention

Accepted by Diego on 2026-10-21 under
[#73](https://github.com/uibcdf/moli/issues/73).

## Conceptual basis

The names distinguish three related concepts:

| Term | Meaning |
| --- | --- |
| **Molecular Intelligence** | The capability of the complete scientific system, combining Scientific Context, Molecular Modeling and Scientific Reasoning, as defined in [Architecture 1.0](../../architecture_1.0/MOLECULAR_INTELLIGENCE.md). |
| **MolI** | The platform that brings together the components, shared contracts and infrastructure supporting that capability. The name combines **Mol** from **Molecular** and **I** from **Intelligence**. |
| **Moli** | The proper name of MolI's scientific agent, its optional reasoning and agency component. It names the agent rather than the platform or the capability as a whole. |

The related names express that Moli belongs to MolI. Their different meanings
are the reason for the convention; capitalization makes that distinction
visible. MolI can be used directly by people and other systems. Scientific
Reasoning may be entirely human or augmented by Moli; Molecular Intelligence
does not depend on the presence of this agent or an LLM.

Use this concise formulation when introducing the relationship:

> **MolI is the Molecular Intelligence platform. Moli is its scientific agent.**

In Spanish:

> **MolI es la plataforma de Molecular Intelligence. Moli es su agente científico.**

When both names first appear together, write **the MolI platform** and
**the agent Moli** (Spanish: **la plataforma MolI** and **el agente Moli**) if
needed for clarity. Moli's proper name does not merge the agent with the
platform or assign it ownership of other components' scientific objects.

## Standard spelling

| Name | Meaning | Capitalization |
| --- | --- | --- |
| **MolI** | The platform as a whole: its components, shared architecture, contracts and governance. | Uppercase **M** and final uppercase **I**; lowercase **o** and **l**. |
| **Moli** | The platform's optional scientific reasoning and agency component: the agent. | Initial uppercase **M**; lowercase **oli**, including the final **i**. |

Use these spellings in new or revised human-facing prose, including
documentation, issues, discussions, reports, presentations and conversations.
The rule applies in Spanish and English, including headings and sentence starts.
When both appear, make the relationship explicit: **Moli is an agent within
MolI**. Do not use the platform name as a shorthand for the agent.

Examples:

- Spanish: "MolI integra Sabueso, Praxis, Nextia y MolSysSuite."
- Spanish: "Moli puede ayudar al científico a trabajar con MolI."
- English: "MolI is the platform; Moli is its optional scientific agent."

## Existing names and technical references

Earlier documents use **MOLI** for the platform and **MOLI Agent** for the agent.
The current prose spellings are **MolI** and **Moli**, respectively. This
editorial convention names the same architectural concepts; it does not change
component responsibilities, scientific authority or the agent's optional role.
Moli remains distinct from MolSys-AI and its specialist agent.

Keep actual technical identifiers and destinations exact: for example,
`uibcdf/moli`, `uibcdf/moli-agent`, `moli.toml`, `MOLI_GUIDE.md` and
`architecture_1.0/MOLI_AGENT.md`. The naming convention does not rename a
repository, file, package, import, API, schema or persistent identifier.

Preserve exact quotations, immutable evidence and historical decision records.
When explaining them in current prose, identify the older spelling if needed:
"Moli (called MOLI Agent in Architecture 1.0)". Apply the current convention
when authoring or substantively revising maintained prose; a global rewrite of
historical architecture and archives is not required.

## Ownership and future use

This is the shared display-name convention for MolI and its directly governed
components. The accepted policy is registered in `moli.toml`; root contributor
instructions link here so future work does not depend on chat memory.
MolSysSuite's team owns adoption in its documentation and members through
[its governance issue](https://github.com/uibcdf/molsyssuite/issues/121).
Local technical identifiers and other component names retain their own contracts.
