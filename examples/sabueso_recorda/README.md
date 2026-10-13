# Sabueso artifact consumption with Recorda (#36)

This review-only application receives Sabueso's existing observed comparative
example, keeps its scientific and runtime files byte-identical, and records the
application's actual consumption with Recorda 0.3. It is a bounded first receiving
exercise for [MOLI #36](https://github.com/uibcdf/moli/issues/36), with lifecycle
context relevant to [#18](https://github.com/uibcdf/moli/issues/18).

It does not implement ProjectContext, EventLedger routing, a ProjectStore, a shared
ProjectRecord schema, Nextia interpretation, authorization or a transactional
multi-file commit. `moli.sabueso_recorda_handoff_example@1` names this example's
index, not an accepted platform exchange format. The passive
`knowledge_consumption` label is not a Recorda routing profile implementation.

## Source-development exercise

Use the existing shared Python 3.14 development environment. Install participating
Sabueso, Recorda and Ackredit checkouts editable and verify their import paths.
Sabueso's published 0.14.0 artifact predates this example: use development source
`792bd0da45245ad0fca08e4b431e5e49e4d76ae8` or its documented source-equivalent head.
This is source integration, not qualification of a new distributed artifact.
CI selects that published compact `sabueso.comparative_operation@2` producer;
source qualification stays in Sabueso. A receiving regression checks that the
new format actually crosses this boundary with complete original inputs and
hash-bound scope references. The receiver delegates both new and historical
`@1` operation records to the explicitly supplied owner reader. Existing
historical records are never compacted or rewritten during reception.

From the MOLI checkout, with the Sabueso checkout at `../sabueso`:

```bash
python ../sabueso/examples/user_journeys/comparative_support.py produce \
  --fixtures ../sabueso/temp_data --output /tmp/public-comparative-bundle
python examples/sabueso_recorda/handoff.py receive \
  --bundle /tmp/public-comparative-bundle --output /tmp/public-handoff \
  --sabueso-checkout ../sabueso
python examples/sabueso_recorda/handoff.py inspect /tmp/public-handoff
SABUESO_CHECKOUT="$(realpath ../sabueso)" \
  python -m pytest -n 12 --receptor=llm examples/sabueso_recorda/tests
```

The producer uses declared public fixtures, never live providers. Reception
supports the original `sabueso.comparative_support_example@3` stage only, under
its owner-issued reader. Historical `@1`/`@2` readers remain with Sabueso; their
absent operation records are never reconstructed. This is a public bounded
example, not a generic entity exporter or a new Sabueso API.

## What is retained

The receiving directory contains:

- `bundle/knowledge.db` and the original manifest, scientific report and runtime
  sidecar, copied byte-identically from a closed source store;
- `record.jsonl`, containing a parent receiving operation and three child
  consumption operations with exact original result/execution identifiers,
  named rules, producer versions and knowledge pins;
- original CSL-JSON/BibTeX credit exported from the saved workflow without
  acquiring sources, deriving results, enriching metadata or registering uses;
- `handoff.json`, the example's final index binding the journal hash, retained
  files, original producer/pins and exports.

The application chooses its destination; scientific components do not select
project storage. Existing destinations are refused. Ordinary files have a 64 MiB
default limit each; the caller can explicitly choose a different local byte
budget with `--file-limit` on reception and inspection. Later inspection does not
silently inherit a larger budget from an artifact. Symlinked members and live
SQLite WAL states are refused. This is
not a self-contained archive of native source responses or a portable replay.

The caller should supply only the knowledge needed by the declared result.
A source-preparation step may use Sabueso's native `KnowledgeStore.load(pin)`
and `save(card)` to retain the full required snapshots in a fresh closed store,
checking identical pins and `to_dict()` states. Its container is a new artifact;
the original store remains intact. The report, manifest and runtime need not
change. This example does not silently project a project store or discard any
assertions within a retained Card. General self-contained export policy remains
with Sabueso/MOLI's historical-reference review.

## Read and failure semantics

Sabueso's owner reader verifies copied knowledge pins, selected assertions,
original rules/results and credit during reception. Recorda separately observes
this new consumption. Neither event is a rerun of the historical scientific
operation or a new source acquisition. Exceptions propagate; a rejected bundle
retains its failed receiving attempt without modifying the original input.

`inspect` requires Recorda and its support dependencies, but no Sabueso, Ackredit
or scientific producer. It verifies recorded file references through an explicit
local index and checks original version/execution bindings against the retained
runtime. Native Card pins remain explicitly unresolved in this producer-free
inspection; hash-matching store bytes alone do not resolve their scientific meaning.
Original bibliography remains in the saved runtime and exports, without new credit.

Execution history and current artifact availability are separate. A later missing
or changed file makes the hand-off unavailable while retaining the successful
recorded consumption. A failed final index publication leaves the hand-off
incomplete even when the recording session succeeded. This phase is declared
outside the recording boundary; multi-file atomicity/durability is unqualified.
Inspection does not alter original timestamps, versions or native sidecars.
Hashes bind local records and detect changed bytes; they do not authenticate
publishers, grant permission or establish scientific validity.

## Remaining owner acceptance

MOLI owns project/campaign context, historical-reference retention policy,
ProjectRecord/EventLedger correlation and routing, and consequential commit policy.
Nextia owns the explicit interpretation that could create project Evidence.
Recorda owns the recording substrate; Sabueso owns scientific support and native
result/source semantics. Keep #36/#18 open for these separate acceptance steps.
Private pilot files and results must stay outside this public example and CI.
