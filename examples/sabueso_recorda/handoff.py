"""Review-only consumer of Sabueso's observed public example, using Recorda 0.3.

This application retains component-owned artifacts; it defines no ProjectRecord
schema and performs no scientific interpretation or source acquisition.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import shutil
import sys
from dataclasses import asdict
from pathlib import Path

FORMAT = "moli.sabueso_recorda_handoff_example@1"
OWNER_FORMAT = "sabueso.comparative_support_example@3"
MEMBERS = (
    "knowledge.db",
    "original.manifest.json",
    "original.report.json",
    "original.runtime.json",
)
MAX_BYTES = 64 * 1024 * 1024
GAPS = [
    "Only this application-owned consumption boundary is recorded",
    "Original source and comparative executions remain in Sabueso artifacts",
    "Native knowledge references require their Sabueso owner to resolve",
    "No ProjectContext, EventLedger routing or transactional multi-file commit",
    "No CPU/GPU accounting, source authorization or Nextia interpretation",
    "The final index publication is outside the completed recording session",
]


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    with Path(path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, allow_nan=False, indent=2)
        stream.write("\n")


def owner_reader(checkout):
    """Use the explicitly supplied owner's reader, never invent an exchange API."""
    checkout = Path(checkout).resolve(strict=True)
    helper = checkout / "examples/user_journeys/comparative_support.py"
    sys.path.insert(0, str(helper.parent))
    module = importlib.import_module("comparative_support")
    import sabueso

    if Path(module.__file__).resolve() != helper or not Path(
        sabueso.__file__
    ).resolve().is_relative_to(checkout):
        raise ValueError("Sabueso and its reader must use the supplied local checkout")
    return module


def artifact_reference(name, hash_value):
    import recorda

    return recorda.Reference(
        owner="sabueso",
        identifier=f"example-artifact:{name}:sha256:{hash_value}",
        digest=hash_value,
    )


def copy_member(source, target, file_limit):
    if source.is_symlink() or not source.is_file():
        raise ValueError("The declared artifact must be an ordinary local file")
    before = source.stat()
    if before.st_size > file_limit:
        raise ValueError("Artifact exceeds this bounded example's file limit")
    before_hash = digest(source)
    with source.open("rb") as src, target.open("xb") as dst:
        shutil.copyfileobj(src, dst)
    after = source.stat()
    if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (
        after.st_size,
        after.st_mtime_ns,
        after.st_ctime_ns,
    ) or digest(target) != before_hash:
        raise ValueError("Artifact changed while receiving it")
    return before_hash


def receive(source, destination, *, sabueso_checkout, file_limit=MAX_BYTES):
    """Retain original artifacts and record their actual consumption, not a rerun."""
    import ackredit
    import recorda
    import sabueso

    if type(file_limit) is not int or file_limit < 1:
        raise ValueError("File limit must be a positive byte count")
    source = Path(source).resolve(strict=True)
    destination = Path(destination)
    destination.mkdir(mode=0o700, parents=True, exist_ok=False)
    copied = destination / "bundle"
    copied.mkdir(mode=0o700)
    reader = owner_reader(sabueso_checkout)
    references = {}
    with (
        recorda.session(
            "Sabueso artifact consumption", path=destination / "record.jsonl", gaps=GAPS
        ) as session,
        session.operation(
            "moli.receive_sabueso_example",
            profile="knowledge_consumption",
            parameters={"requested_format": OWNER_FORMAT},
            implementation={
                "receiver_sha256": digest(__file__),
                "recorda_version": recorda.__version__,
                "sabueso_reader_version": sabueso.__version__,
            },
        ) as parent,
    ):
        wal = source / "knowledge.db-wal"
        if wal.exists() and wal.stat().st_size:
            raise ValueError("Receive a closed SQLite store, not a live WAL state")
        for name in MEMBERS:
            references[name] = artifact_reference(
                name, copy_member(source / name, copied / name, file_limit)
            )
        declaration = read_json(copied / "original.manifest.json")
        if (
            declaration.get("format") != OWNER_FORMAT
            or declaration.get("stage") != "original"
        ):
            raise ValueError("Only original observed @3 bundles are supported")
        # Owner-issued pins, assertions, rules, result hashes and original
        # workflow credit are verified without source access or derivation.
        manifest, report, runtime = reader.read_stage(copied, "original")
        for name in MEMBERS:
            parent.output(name, references[name])
        for key, original in zip(reader.OPERATIONS, runtime["operations"], strict=True):
            inputs = {
                "original_report": references["original.report.json"],
                "original_runtime": references["original.runtime.json"],
            }
            for index, scope in enumerate(original["inputs"]):
                inputs[f"knowledge_{index}"] = recorda.Reference(
                    owner="sabueso", identifier=scope["card_ref"]
                )
            with session.operation(
                "moli.consume_sabueso_result",
                profile="knowledge_consumption",
                inputs=inputs,
                parameters={
                    "result": key,
                    "source_execution_id": original["execution_id"],
                    "source_result_id": original["result_id"],
                    "source_producer": runtime["producer"]["sabueso"],
                    "source_rule": original["rule"]["rule"],
                },
            ) as consumption:
                # Meaningful use here is acceptance and persistence of this
                # verified result. No project Evidence or decision follows.
                if report["views"][key] != report[key]["view"]:
                    raise ValueError("The retained result differs from its explanation")
                consumption.output(
                    "accepted_report", references["original.report.json"]
                )
        # Export from the original saved credit; do not register or track uses.
        credit = ackredit.Attribution.from_dict(runtime["workflow"])
        for fmt, suffix in (("csl-json", "csl.json"), ("bibtex", "bib")):
            (destination / f"original.references.{suffix}").write_text(
                credit.report(format=fmt), encoding="utf-8"
            )
    # Completion is declared last. A failure here leaves the journal intact and
    # the hand-off incomplete; no atomic or distributed commit is claimed.
    write_json(
        destination / "handoff.json",
        {
            "format": FORMAT,
            "journal_sha256": digest(destination / "record.jsonl"),
            "references": [
                {"reference": asdict(reference), "path": f"bundle/{name}"}
                for name, reference in references.items()
            ],
            "exports": {
                f"original.references.{suffix}": digest(
                    destination / f"original.references.{suffix}"
                )
                for suffix in ("csl.json", "bib")
            },
            "original_producer": runtime["producer"],
            "original_cards": manifest["cards"],
            "project_interpretation": "not_performed",
            "authorization": "not_decided",
        },
    )
    return inspect_handoff(destination, file_limit=file_limit)


def inspect_handoff(directory, *, file_limit=MAX_BYTES):
    """Inspect recorded execution and file availability with Recorda alone."""
    import recorda

    if type(file_limit) is not int or file_limit < 1:
        raise ValueError("File limit must be a positive byte count")
    directory = Path(directory)
    recorded = recorda.inspect(directory / "record.jsonl")
    resolver = None
    declaration = None
    index = directory / "handoff.json"
    if index.exists():
        declaration = read_json(index)
        if declaration["format"] != FORMAT or declaration["journal_sha256"] != digest(
            directory / "record.jsonl"
        ):
            raise ValueError("Recorded journal or hand-off format differs")
        if (
            declaration["project_interpretation"] != "not_performed"
            or declaration["authorization"] != "not_decided"
        ):
            raise ValueError(
                "Project interpretation or authorization is outside this example"
            )
        entries = {}
        for row in declaration["references"]:
            reference = recorda.Reference(**row["reference"])
            path = row["path"]
            if path not in {f"bundle/{name}" for name in MEMBERS}:
                raise ValueError("Unknown artifact in the local reference index")
            name = Path(path).name
            if (
                reference != artifact_reference(name, reference.digest)
                or reference in entries
            ):
                raise ValueError("Changed or duplicate reference declaration")
            entries[reference] = path
        if len(entries) != len(MEMBERS) or set(entries.values()) != {
            f"bundle/{name}" for name in MEMBERS
        }:
            raise ValueError("Incomplete local reference index")
        declared = {json.dumps(asdict(r), sort_keys=True) for r in entries}
        retained = {
            json.dumps({k: v for k, v in value.items() if k != "kind"}, sort_keys=True)
            for operation in recorded.operations
            for values in (operation["inputs"], operation["outputs"])
            for value in values.values()
            if isinstance(value, dict)
            and value.get("kind") == "reference"
            and value.get("digest") is not None
        }
        if declared != retained:
            raise ValueError("Reference index differs from the recorded occurrences")
        if set(declaration["exports"]) != {
            "original.references.csl.json",
            "original.references.bib",
        }:
            raise ValueError("Unknown citation export in the hand-off")
        resolver = recorda.LocalFileResolver(
            directory, entries, digest_algorithm="sha256"
        )
    checks = recorda.check_references(recorded, resolver=resolver, max_bytes=file_limit)
    files = [
        row for row in checks["references"] if (row["reference"] or {}).get("digest")
    ]
    exports = (
        {}
        if declaration is None
        else {
            name: "matched"
            if (directory / name).is_file() and digest(directory / name) == expected
            else "missing_or_changed"
            for name, expected in declaration["exports"].items()
        }
    )
    available = (
        declaration is not None
        and files
        and all(row["status"] == "matched" for row in files)
        and all(status == "matched" for status in exports.values())
    )
    if available:
        native = read_json(directory / "bundle/original.runtime.json")
        if (
            declaration["original_producer"] != native["producer"]
            or declaration["original_cards"] != native["cards"]
        ):
            raise ValueError("Original producer or knowledge pins differ")
        parent, *uses = recorded.operations
        if parent["name"] != "moli.receive_sabueso_example" or len(uses) != len(
            native["operations"]
        ):
            raise ValueError("Consumer boundaries differ from the declared hand-off")
        for use, original in zip(uses, native["operations"], strict=True):
            parameters = use["parameters"]
            if (
                use["name"] != "moli.consume_sabueso_result"
                or use["parent_id"] != parent["id"]
                or parameters["source_execution_id"] != original["execution_id"]
                or parameters["source_result_id"] != original["result_id"]
                or parameters["source_producer"] != native["producer"]["sabueso"]
                or parameters["source_rule"] != original["rule"]["rule"]
            ):
                raise ValueError(
                    "Consumer occurrence is misbound to the original execution"
                )
            retained_pins = [
                value["identifier"]
                for name, value in use["inputs"].items()
                if name.startswith("knowledge_")
            ]
            if retained_pins != [scope["card_ref"] for scope in original["inputs"]]:
                raise ValueError(
                    "Consumer input pins differ from the original execution"
                )
    return {
        "execution_status": recorded.status,
        "artifact_handoff_status": "complete"
        if available and recorded.status == "succeeded"
        else "incomplete_or_unavailable",
        "coverage": recorded.coverage,
        "operations": recorded.operations,
        "reference_checks": checks,
        "export_checks": exports,
        "knowledge_pin_resolution": "not_performed_without_Sabueso",
        "original_producer": None
        if declaration is None
        else declaration["original_producer"],
        "original_producer_basis": "bound_to_retained_runtime"
        if available
        else "declaration_not_currently_verified",
        "project_interpretation": "not_performed",
        "authorization": "not_decided",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    receive_parser = sub.add_parser("receive")
    receive_parser.add_argument("--bundle", type=Path, required=True)
    receive_parser.add_argument("--output", type=Path, required=True)
    receive_parser.add_argument("--sabueso-checkout", type=Path, required=True)
    inspect_parser = sub.add_parser("inspect")
    inspect_parser.add_argument("directory", type=Path)
    receive_parser.add_argument(
        "--file-limit",
        type=int,
        default=MAX_BYTES,
        help="Maximum individual file length in bytes",
    )
    inspect_parser.add_argument(
        "--file-limit",
        type=int,
        default=MAX_BYTES,
        help="Maximum individual file length in bytes",
    )
    args = parser.parse_args()
    result = (
        receive(
            args.bundle,
            args.output,
            sabueso_checkout=args.sabueso_checkout,
            file_limit=args.file_limit,
        )
        if args.action == "receive"
        else inspect_handoff(args.directory, file_limit=args.file_limit)
    )
    print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2))
    return 0 if result["artifact_handoff_status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
