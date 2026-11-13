# Development and production environment names

Platform convention under [MolI #94](https://github.com/uibcdf/moli/issues/94).
The suffix names the **actual Python major.minor**; naming does not expand Python
support or qualify a dependency closure.

| Purpose | MolI | MolSysSuite |
| --- | --- | --- |
| Source development | `moli_dev@<python>` | `molsyssuite_dev@<python>` |
| Future production runtime | `moli@<python>` | `molsyssuite@<python>` |

For current Python 3.14 development the names are `moli_dev@3.14` and
`molsyssuite_dev@3.14`. The corresponding production names are `moli@3.14` and
`molsyssuite@3.14`; they describe future separately designed profiles, not existing
qualified environments or renamed packages. No environment is created by this
convention. MolSysSuite owns its recipes, member instructions and migration in
[suite #175](https://github.com/uibcdf/molsyssuite/issues/175) and its paused
workspace work in [#82](https://github.com/uibcdf/molsyssuite/issues/82).

## Development contents and evidence

An owner-selected development profile supplies the selected components' runtime,
editable/native build, test and documentation tools. Install each eligible local
Python checkout with `python -m pip install --no-deps --editable .` after solving
its dependencies; inspect interpreter/distribution/import origins and clean
closure. Repositories without a Python package need no invented editable install.
The shared name does not prove all components can coexist or that native builds,
notebooks, scientific APIs or public packages work.

For documentation that loads `sphinxcontrib.plantuml`, provide the Python
`sphinxcontrib-plantuml` extension and separately the renderer/Java prerequisites
and any Graphviz dependency used by the chosen configuration. An import resolves
the extension boundary only. Verify the actual tools belong to the intended
prefix, and build a representative strict Sphinx UML page, inspecting the rendered
diagram. Do not claim rendering from an import or a zero exit without its output.
This is documentation tooling, not a universal package runtime dependency.

Suite source `e162210a0f5130ff9bd1f9380e7ba991623c91a4` and
[its owner return](https://github.com/uibcdf/moli/issues/94#issuecomment-6836931452)
report a fresh hosted Linux/Python 3.14.10 development profile with a real
Sphinx/PlantUML SVG. That scoped evidence does not migrate this machine or qualify
a MolI profile; the exact suite recipe and future production design stay there.

## Owned migration

The historical suite prefix `molsyssuite@uibcdf_3.14` is preserved in original
receipts. Do not silently rename, delete or relink a working prefix. Before a
migration, name the owner, selected checkouts, required engines/tools, platform,
Python minor, current prefix/kernel uses and useful retained evidence. Create a
replacement from the reviewed owner recipe, then verify:

- Interpreter, installed/editable origins, native libraries and dependency closure.
- Selected public entry points and representative integration/documentation paths.
- Activation guidance and notebook kernel identity; reconnect only with explicit
  ownership and preserve active sessions and rollback inputs.

Switch the owned uses only after receiving succeeds; retire the old prefix under
the temporary-resource rule after its last user and evidence obligation end.
Record partial migration rather than relabeling the old cohort as new evidence.
No prefix, notebook or caller environment is changed by this documentation task.

## Future production design

A production profile needs a concrete scientist/service use case and selected
capabilities before package/engine choices. State installed artifact and native
engine identities, OS/Python support, optional features, resource/privacy policy,
reproducible closure and recovery. Production uses its reviewed installed route;
mutable editable development evidence cannot certify it. Unavailable components
or engines remain explicit gaps.

MolI owns the future `moli@<python>` design and qualification under #94; MolSysSuite
owns its counterpart [design](https://github.com/uibcdf/molsyssuite/blob/e162210a0f5130ff9bd1f9380e7ba991623c91a4/devguide/production_environment_profiles.md).
No MolI recipe/runtime closure is selected here. Revisit when the first concrete
production use case or owner-reviewed development cohort is selected. #94 stays
partial for that profile/receiving work, separately from this delivered convention.
