# MOLI Development Observatory

The operational MOLI Development Observatory has moved to:

**[uibcdf/moli-dev-observatory](https://github.com/uibcdf/moli-dev-observatory)**

That repository is the owner of the collector, metric derivation, tests,
Overview → Layer → Repository static site, GitHub Actions schedule, and GitHub
Pages publication.

MOLI continues to own the authoritative platform registry in `moli.toml`.
MolSysSuite continues to own its member registry in `suite.toml`. The
Observatory consumes those sources without changing their governance meaning.

Historical design and migration evidence are preserved in:

- [MOLI issue #48](https://github.com/uibcdf/moli/issues/48);
- [archived Observatory proposal](archive/development_observatory.md);
- [standalone migration issue #1](https://github.com/uibcdf/moli-dev-observatory/issues/1);
- [standalone future roadmap #3](https://github.com/uibcdf/moli-dev-observatory/issues/3).

Do not add new Observatory runtime code or publication workflows to this
repository. Observatory implementation changes belong to
`uibcdf/moli-dev-observatory`.
