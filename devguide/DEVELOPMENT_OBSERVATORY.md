# MOLI Development Observatory

The MOLI Development Observatory provides reproducible development-health metrics for the MOLI platform without making a particular dashboard technology part of the platform contract.

Tracked by [uibcdf/moli#48](https://github.com/uibcdf/moli/issues/48).

## Architecture

```text
moli.toml + MolSysSuite suite.toml + GitHub
                    ↓
                 collector
                    ↓
          normalized issue snapshot
               (issues.json)
                    ↓
                 analytics
                    ↓
             derived metrics
              (metrics.json)
                    ↓
      ┌─────────────┼─────────────┐
      ↓             ↓             ↓
 static HTML     reports/CLI   future backends
                               (for example Grafana)
```

The JSON records are the portable interface of the first implementation. The HTML dashboard is a consumer of those records and does not query GitHub directly.

## Scope discovery

Repository scope is derived from governance registries:

- `uibcdf/moli` itself;
- direct components registered in `moli.toml`;
- MolSysSuite members registered in `uibcdf/molsyssuite:suite.toml`;
- MOLI support infrastructure registered in `moli.toml` when it is not already represented as a MolSysSuite member.

The dashboard groups repositories into four presentation layers:

- **MOLI** — the platform repository and directly governed components other than MolSysSuite;
- **MolSysSuite** — the delegated ecosystem governance repository;
- **Scientific components** — MolSysSuite members whose role is `scientific-component`;
- **Infrastructure** — other registered MolSysSuite members and MOLI support infrastructure.

This grouping is observational only. It does not change ownership or delegated governance.

## V1 data model

`issues.json` records normalized issue snapshots and provenance. It intentionally excludes pull requests returned by GitHub's issues endpoint. The first schema contains repository, GitHub issue identity, state, timestamps, labels and URL.

V1 is a **snapshot model**. GitHub's current `closed_at` field does not preserve the complete sequence of close/reopen cycles. A future event model may add explicit lifecycle events without changing the dashboard's role as a derived consumer.

`metrics.json` derives:

- issues opened and closed per day;
- 7-day moving averages;
- cumulative net backlog change over the selected window;
- opened/closed/current-open counts by platform layer and repository;
- closure ratio;
- current open-issue age buckets.

The default display window is 90 days and UTC. Both are command-line parameters.

## Local build

```bash
python devtools/scripts/development_observatory.py \
  --output build/development-observatory \
  --days 90 \
  --timezone UTC

python -m http.server --directory build/development-observatory 8000
```

Then open `http://localhost:8000/`.

For a higher GitHub API rate limit, set `MOLI_OBSERVATORY_GITHUB_TOKEN` to a token that can read the repositories in scope. V1 is intended for public development data. Do not grant a broader token merely to make private or confidential repositories visible to the public dashboard.

Registry membership and effective collection scope are deliberately distinct. If GitHub returns 403 or 404 for an individual registered repository (for example, a private MolSysSuite member during an unauthenticated public-data run), collection continues for the remaining repositories. The inaccessible entry is omitted from effective `scope`, recorded in `excluded_scope` with its registry metadata and HTTP status, and counted in dashboard metadata. Other API failures remain fatal so collector regressions are not silently hidden.

## GitHub Actions and publication

`.github/workflows/development_observatory.yml` refreshes the observatory daily and on manual dispatch. Every run uploads the generated site and JSON as a workflow artifact.

GitHub Pages deployment is opt-in. Set the repository variable:

```text
MOLI_OBSERVATORY_PUBLISH_PAGES=true
```

and configure Pages to use GitHub Actions before expecting the deployment job to publish the site.

A private repository must not be assumed to imply a private Pages site. If development metrics later include private repositories, internal infrastructure, costs, client work, or other restricted information, use an authenticated publication route.

## Future backends

The collector and analytics model must remain independent of the initial static renderer. Possible future consumers include:

- Grafana backed by PostgreSQL or a time-series database;
- authenticated static hosting;
- notebooks and reports;
- CLI summaries;
- monitoring/alerting systems.

A move to Grafana should ingest the normalized observatory records (or a versioned compatible schema), not require rewriting repository discovery or GitHub collection semantics.

Likely future metrics include PR lead time and merge throughput, CI success/runtime, release cadence, coverage history, and issue lifecycle events including reopen cycles.
