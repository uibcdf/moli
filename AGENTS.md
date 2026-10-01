# MOLI repository instructions

Read `MOLI_GUIDE.md` before changing platform governance or a contract shared by
components. Use `moli.toml` to find accepted policies and their normative documents;
read the relevant decisions in `architecture_1.0/` for architectural work. Route
bugs and proposals to the owning GitHub issue as the guide requires.

When a development incident yields a reusable behavior rule, assess its scope
and record an accepted rule in the appropriate root or nested `AGENTS.md` in
the same change, or leave an owned issue for adoption. Follow
`devguide/governance/agent_instruction_lifecycle.md`; report a rule useful to
other components at the owning governance level. For work under `devguide/`,
also read `devguide/AGENTS.md`.

Validate this governance repository with
`python devtools/scripts/validate_governance.py`.
`devtools/scripts/check_repository.py` checks MOLI component repositories; it is
not the validator for this repository.
