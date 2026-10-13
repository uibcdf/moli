"""Actual public artifact consumption and failed/unavailable historical delivery."""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import recorda

SCRIPT = Path(__file__).resolve().parents[1] / "handoff.py"
spec = importlib.util.spec_from_file_location("handoff_example", SCRIPT)
handoff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handoff)
SABUESO = Path(os.environ["SABUESO_CHECKOUT"]).resolve()


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    directory = tmp_path_factory.mktemp("public-producer") / "bundle"
    result = subprocess.run(
        [
            sys.executable,
            str(SABUESO / "examples/user_journeys/comparative_support.py"),
            "produce",
            "--output",
            str(directory),
            "--fixtures",
            str(SABUESO / "temp_data"),
        ],
        capture_output=True,
        check=False,
        text=True,
        timeout=120,
        cwd=directory.parent,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return directory


@pytest.fixture
def received(bundle, tmp_path):
    output = tmp_path / "receiver"
    handoff.receive(bundle, output, sabueso_checkout=SABUESO)
    return output


def test_consumption_retains_original_results_credit_pins_and_parent_correlation(
    bundle, received
):
    native = handoff.read_json(bundle / "original.runtime.json")
    result = handoff.inspect_handoff(received)
    assert result["artifact_handoff_status"] == "complete"
    assert result["execution_status"] == "succeeded"
    assert result["original_producer"] == native["producer"]
    assert result["project_interpretation"] == "not_performed"
    assert result["authorization"] == "not_decided"
    parent, *uses = result["operations"]
    assert len(uses) == 3 and all(use["parent_id"] == parent["id"] for use in uses)
    for name in handoff.MEMBERS:
        assert (received / "bundle" / name).read_bytes() == (bundle / name).read_bytes()
    references = result["reference_checks"]["references"]
    assert all(
        row["status"] == "matched" for row in references if row["reference"]["digest"]
    )
    assert all(
        row["status"] == "unresolved"
        for row in references
        if not row["reference"]["digest"]
    )
    csl = json.loads((received / "original.references.csl.json").read_text())
    assert {row["id"] for row in csl} == {
        row["id"] for row in native["workflow"]["items"]
    }


def test_receiving_exercises_compact_credit_with_retained_original_input_scope(
    bundle, received
):
    native = handoff.read_json(bundle / "original.runtime.json")
    retained = handoff.read_json(received / "bundle/original.runtime.json")
    assert retained == native
    assert len(native["operations"]) == 3
    for operation in retained["operations"]:
        assert operation["format"] == "sabueso.comparative_operation@2"
        assert operation["inputs"]
        uses = operation["provider"]["attribution"]["uses"]
        assert uses
        for use in uses:
            context = use["context"]
            assert "inputs" not in context
            reference = context["input_scope"]
            assert reference["rule"] == "comparative_input_scope_reference@1"
            assert reference["operation_ref"] == operation["execution_id"]
            assert reference["field"] == "inputs"
            assert reference["sha256"].startswith("sha256:")
    assert handoff.inspect_handoff(received)["artifact_handoff_status"] == "complete"


@pytest.mark.parametrize("damage", ["missing", "changed", "export_missing"])
def test_unavailable_bytes_do_not_rewrite_successful_execution_history(
    received, damage
):
    target = received / (
        "original.references.bib"
        if damage == "export_missing"
        else "bundle/original.report.json"
    )
    if damage == "changed":
        target.write_bytes(target.read_bytes() + b" ")
    else:
        target.unlink()
    result = handoff.inspect_handoff(received)
    assert result["execution_status"] == "succeeded"
    assert result["artifact_handoff_status"] == "incomplete_or_unavailable"
    assert result["project_interpretation"] == "not_performed"
    if damage != "export_missing":
        expected = "mismatched" if damage == "changed" else "missing"
        assert any(
            row["status"] == expected
            for row in result["reference_checks"]["references"]
        )


@pytest.mark.parametrize(
    "damage",
    ["index", "producer", "pins", "journal", "interpretation", "authorization"],
)
def test_changed_bindings_are_refused(received, damage):
    path = received / "handoff.json"
    index = handoff.read_json(path)
    if damage == "index":
        index["references"][0]["path"] = "../outside"
    elif damage == "producer":
        index["original_producer"]["sabueso"] = "999.reader"
    elif damage == "pins":
        index["original_cards"]["human"] = "another entity"
    elif damage == "interpretation":
        index["project_interpretation"] = "approved"
    elif damage == "authorization":
        index["authorization"] = "granted"
    else:
        with (received / "record.jsonl").open("ab") as stream:
            stream.write(b"\n")
    path.write_text(json.dumps(index))
    with pytest.raises(ValueError):
        handoff.inspect_handoff(received)


def test_invalid_original_runtime_remains_a_failed_consumer_attempt(bundle, tmp_path):
    source = tmp_path / "invalid"
    shutil.copytree(bundle, source)
    runtime = handoff.read_json(source / "original.runtime.json")
    runtime["report_sha256"] = "0" * 64
    (source / "original.runtime.json").write_text(json.dumps(runtime))
    before = {name: handoff.digest(source / name) for name in handoff.MEMBERS}
    output = tmp_path / "failed"
    with pytest.raises(ValueError):
        handoff.receive(source, output, sabueso_checkout=SABUESO)
    assert recorda.inspect(output / "record.jsonl").status == "failed"
    assert (
        handoff.inspect_handoff(output)["artifact_handoff_status"]
        == "incomplete_or_unavailable"
    )
    assert {name: handoff.digest(source / name) for name in handoff.MEMBERS} == before


def test_existing_destination_is_never_overwritten(bundle, received):
    before = handoff.digest(received / "record.jsonl")
    with pytest.raises(FileExistsError):
        handoff.receive(bundle, received, sabueso_checkout=SABUESO)
    assert handoff.digest(received / "record.jsonl") == before


def test_owner_prepared_scoped_store_keeps_full_snapshots_and_native_pins(
    bundle, tmp_path
):
    import sabueso

    source = tmp_path / "scoped"
    source.mkdir()
    for name in handoff.MEMBERS[1:]:
        shutil.copyfile(bundle / name, source / name)
    manifest = handoff.read_json(source / "original.manifest.json")
    original = sabueso.KnowledgeStore(bundle / "knowledge.db")
    scoped = sabueso.KnowledgeStore(source / "knowledge.db")
    for pin in manifest["cards"].values():
        card = original.load(pin)
        assert scoped.save(card) == pin
        assert scoped.load(pin).to_dict() == card.to_dict()
    result = handoff.receive(
        source, tmp_path / "received-scoped", sabueso_checkout=SABUESO
    )
    assert result["artifact_handoff_status"] == "complete"
    assert (
        handoff.read_json(tmp_path / "received-scoped/handoff.json")["original_cards"]
        == manifest["cards"]
    )


def test_explicit_file_budget_and_later_inspection_budget_remain_separate(
    bundle, tmp_path
):
    failed = tmp_path / "too-small"
    with pytest.raises(ValueError, match="file limit"):
        handoff.receive(bundle, failed, sabueso_checkout=SABUESO, file_limit=1)
    assert recorda.inspect(failed / "record.jsonl").status == "failed"
    accepted = tmp_path / "explicit-budget"
    result = handoff.receive(
        bundle, accepted, sabueso_checkout=SABUESO, file_limit=handoff.MAX_BYTES * 2
    )
    assert result["artifact_handoff_status"] == "complete"
    later = handoff.inspect_handoff(accepted, file_limit=1)
    assert later["execution_status"] == "succeeded"
    assert later["artifact_handoff_status"] == "incomplete_or_unavailable"
    assert any(
        row["status"] == "too_large" for row in later["reference_checks"]["references"]
    )


def test_receive_cli_applies_the_requested_file_budget(bundle, tmp_path):
    output = tmp_path / "cli-limit"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "receive",
            "--bundle",
            str(bundle),
            "--output",
            str(output),
            "--sabueso-checkout",
            str(SABUESO),
            "--file-limit",
            "1",
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert result.returncode != 0
    assert recorda.inspect(output / "record.jsonl").status == "failed"


def test_failed_completion_marker_does_not_claim_a_complete_delivery(
    bundle, tmp_path, monkeypatch
):
    error = OSError("marker unavailable")

    def unavailable(*args, **kwargs):
        raise error

    monkeypatch.setattr(handoff, "write_json", unavailable)
    output = tmp_path / "uncommitted"
    with pytest.raises(OSError) as caught:
        handoff.receive(bundle, output, sabueso_checkout=SABUESO)
    assert caught.value is error
    result = handoff.inspect_handoff(output)
    assert result["execution_status"] == "succeeded"
    assert result["artifact_handoff_status"] == "incomplete_or_unavailable"


def test_inspection_needs_no_sabueso_ackredit_or_scientific_producer(received):
    code = """
import builtins,json,runpy,sys
original=builtins.__import__
def guarded(name,*args,**kwargs):
    if name.split('.')[0] in {'sabueso','ackredit','pyunitwizard'}:
        raise AssertionError('Independent inspection cannot import scientific producers')
    return original(name,*args,**kwargs)
builtins.__import__=guarded
module=runpy.run_path(sys.argv[1])
print(json.dumps(module['inspect_handoff'](sys.argv[2])))
"""
    result = subprocess.run(
        [sys.executable, "-c", code, str(SCRIPT), str(received)],
        capture_output=True,
        check=False,
        text=True,
        timeout=60,
        cwd=received,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(result.stdout)
    assert report["artifact_handoff_status"] == "complete"
    assert report["knowledge_pin_resolution"] == "not_performed_without_Sabueso"


def test_receive_is_inert_and_keeps_original_producer_under_a_different_reader(
    bundle, tmp_path, monkeypatch
):
    import ackredit
    import sabueso
    from sabueso.core import (
        attribution,
        attribution_bibliography,
        comparative_bibliography,
    )
    from sabueso.core.card import Card

    def forbidden(*args, **kwargs):
        raise AssertionError(
            "Receiving cannot acquire, derive, enrich metadata or create credit"
        )

    for module, names in (
        (ackredit, ("register_item", "track_item")),
        (sabueso, ("resolve", "refresh_card")),
        (
            Card,
            (
                "sequence_differences",
                "variant_tissue_usage",
                "isoform_tissue_usage",
                "explain_sequence_differences",
                "explain_variant_tissue_usage",
                "explain_isoform_tissue_usage",
            ),
        ),
        (attribution, ("_load_backend",)),
        (attribution_bibliography, ("descriptions",)),
        (comparative_bibliography, ("resource_descriptions", "method_descriptions")),
    ):
        for name in names:
            monkeypatch.setattr(module, name, forbidden)
    monkeypatch.setattr(sabueso, "__version__", "999.reader")
    with ackredit.session("inert hand-off"), sabueso.attribution() as run:
        before = ackredit.get_attribution().to_dict()
        result = handoff.receive(bundle, tmp_path / "inert", sabueso_checkout=SABUESO)
        assert ackredit.get_attribution().to_dict() == before
    assert (
        not run.operations
        and not run.acquisitions
        and not run.records
        and not run.literature
    )
    assert (
        result["original_producer"]
        == handoff.read_json(bundle / "original.runtime.json")["producer"]
    )
    assert result["original_producer"]["sabueso"] != "999.reader"
