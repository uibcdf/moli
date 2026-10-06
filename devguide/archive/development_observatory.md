---
summary: Build portable development observability for MOLI and its registered ecosystem.
issue: uibcdf/moli#48
status: resolved
opened: 2026-10-05
closed: 2026-10-06
verification: measured
area: [development, observability]
blocked_by: []
supersedes: []
---

# MOLI Development Observatory

## What

Create a reproducible development-observability pipeline owned by MOLI. The first consumer is a static HTML dashboard, while normalized issue data and derived metrics remain independent of the rendering layer.

## How / evidence

The initial use case was a platform-wide analysis of issue creation and resolution rates. The useful views were daily opened/closed counts, seven-day moving averages, net backlog growth, layer/repository attribution, and issue age.

`moli.toml` already provides the authoritative direct-component and support-infrastructure registry. MolSysSuite is registered as a delegated ecosystem and its `suite.toml` provides the authoritative member inventory and roles. Therefore repository discovery can be registry-driven without creating a second hard-coded platform inventory.

The proposed V1 uses a normalized issue snapshot (`issues.json`), derived metrics (`metrics.json`), and a static HTML consumer. GitHub Actions can refresh the data and always retain a run artifact; Pages publication is opt-in.

## Why

Development activity is currently large enough that manual inspection of issue counts is insufficient to distinguish healthy discovery/stabilization from accumulating unresolved work. A durable observatory makes those trends reproducible and gives MOLI a path toward broader development observability without prematurely choosing a server, database, or monitoring vendor.

The separation between normalized data and rendering also keeps a future Grafana, database, authenticated dashboard, notebook, or report consumer possible.

## Alternatives

- HTML that queries GitHub directly: rejected because it couples credentials, acquisition, analysis, and presentation.
- Daily aggregate CSV as the canonical source: rejected because it loses issue-level information needed for later metrics.
- Streamlit/Dash/Panel: deferred because they require an application service.
- Grafana now: deferred because it would force an operational backend before the metric model is established.
- MyST-first presentation: possible later if MOLI develops a broader documentation portal.

## Acceptance criteria

- Registry-driven repository discovery from MOLI and MolSysSuite governance sources.
- Canonical normalized issue data separated from derived metrics and HTML.
- Tested local collector/analytics path.
- Static dashboard for issue flow, moving averages, net backlog, layers, and issue age.
- Scheduled/manual GitHub Actions refresh with generated artifacts.
- Explicit publication/privacy guidance.
- Maintained design statement preserving future Grafana/alternative-backend compatibility.
- Repository governance validation and relevant tests pass on the implementation head.

## Resolution

Implemented V1 and V1.1 in `uibcdf/moli`, then migrated operational ownership on
2026-10-06 to the dedicated
[`uibcdf/moli-dev-observatory`](https://github.com/uibcdf/moli-dev-observatory)
repository.

The standalone repository owns collection, analytics, tests, static
Overview → Layer → Repository rendering, scheduled publication, and future
Observatory development. MOLI and MolSysSuite remain authoritative for the
registries used to discover the observed scope.

Production validation in the new repository collected **1218 issues from 24 of
25 registered repositories** using public GitHub access; the private
`uibcdf/opencastp` repository was correctly excluded. The generated site
artifact was retained successfully. GitHub Pages publication requires the
one-time repository setting selecting GitHub Actions as the Pages source.

Historical platform work remains traceable through `uibcdf/moli#48`; the
standalone migration is tracked by `uibcdf/moli-dev-observatory#1`, and the
future roadmap moved to `uibcdf/moli-dev-observatory#3`.
