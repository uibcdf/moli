"""Candidate evidence must expire with its actual inputs, not a green label."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from devtools.scripts.release_evidence import (
    GateReceipt,
    capture_candidate,
    stale_reasons,
)

INPUTS = {
    "release_version",
    "artifact_coordinate",
    "dependency_metadata",
    "resolved_closure",
    "recipe",
    "generated_runtime",
    "artifact",
}
SCOPE = {"os": "linux", "python": "3.13"}


class ReleaseEvidencePolicyTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name in ("molsysmt", "molsysviewer"):
            component = self.root / name
            component.mkdir()
            (component / "pyproject.toml").write_text(
                "dependencies = ['argdigest>=0.13']\n"
            )
            (component / "closure.lock").write_text("argdigest==0.13.0\n")
            (component / "recipe.yaml").write_text("- argdigest >=0.13\n")
            (component / "runtime.js").write_bytes(b"runtime 1.0")
            (component / "candidate.conda").write_bytes(b"artifact 1.0")

    def identity(self, name: str, commit: str) -> dict[str, str]:
        component = self.root / name
        return capture_candidate(
            commit=commit,
            facts={
                "release_version": "1.0.0",
                "artifact_coordinate": f"uibcdf/{name}/1.0.0/noarch/{name}-1.0.0-py_0.conda",
            },
            files={
                "dependency_metadata": component / "pyproject.toml",
                "resolved_closure": component / "closure.lock",
                "recipe": component / "recipe.yaml",
                "generated_runtime": component / "runtime.js",
                "artifact": component / "candidate.conda",
            },
        )

    def reasons(
        self, receipt: GateReceipt, current: dict[str, dict[str, str]]
    ) -> list[str]:
        return stale_reasons(
            receipt,
            gate=receipt.gate,
            scope=SCOPE,
            current=current,
            required_inputs={subject: INPUTS for subject in receipt.participants},
        )

    def test_unchanged_component_evidence_survives_other_component_rebuild(self):
        molsysmt = self.identity("molsysmt", "a" * 40)
        viewer = self.identity("molsysviewer", "b" * 40)
        component_gate = GateReceipt(
            "artifact-install", "passed", SCOPE, {"molsysmt": molsysmt}
        )
        pair_gate = GateReceipt(
            "installed-pair",
            "passed",
            SCOPE,
            {"molsysmt": molsysmt, "molsysviewer": viewer},
        )

        (self.root / "molsysviewer/runtime.js").write_bytes(b"runtime 1.0 corrected")
        current = {
            "molsysmt": self.identity("molsysmt", "a" * 40),
            "molsysviewer": self.identity("molsysviewer", "c" * 40),
        }

        self.assertEqual(self.reasons(component_gate, current), [])
        self.assertIn(
            "molsysviewer.generated_runtime: changed", self.reasons(pair_gate, current)
        )

    def test_changed_commit_cannot_inherit_a_pass(self):
        old = self.identity("molsysmt", "a" * 40)
        receipt = GateReceipt("source", "passed", SCOPE, {"molsysmt": old})
        current = {"molsysmt": self.identity("molsysmt", "c" * 40)}

        self.assertIn("molsysmt.source_commit: changed", self.reasons(receipt, current))

    def test_changed_dependency_metadata_cannot_inherit_a_pass(self):
        old = self.identity("molsysmt", "a" * 40)
        receipt = GateReceipt("installed", "passed", SCOPE, {"molsysmt": old})
        (self.root / "molsysmt/pyproject.toml").write_text(
            "dependencies = ['argdigest>=0.14']\n"
        )
        current = {"molsysmt": self.identity("molsysmt", "a" * 40)}

        self.assertIn(
            "molsysmt.dependency_metadata: changed", self.reasons(receipt, current)
        )

    def test_changed_generated_runtime_cannot_inherit_a_pass(self):
        old = self.identity("molsysviewer", "b" * 40)
        receipt = GateReceipt(
            "artifact-install", "passed", SCOPE, {"molsysviewer": old}
        )
        (self.root / "molsysviewer/runtime.js").write_bytes(b"runtime 1.0 corrected")
        current = {"molsysviewer": self.identity("molsysviewer", "b" * 40)}

        self.assertIn(
            "molsysviewer.generated_runtime: changed", self.reasons(receipt, current)
        )

    def test_changed_recipe_cannot_inherit_a_pass(self):
        old = self.identity("molsysmt", "a" * 40)
        receipt = GateReceipt("installed", "passed", SCOPE, {"molsysmt": old})
        (self.root / "molsysmt/recipe.yaml").write_text("- argdigest >=0.14\n")
        current = {"molsysmt": self.identity("molsysmt", "a" * 40)}

        self.assertIn("molsysmt.recipe: changed", self.reasons(receipt, current))

    def test_missing_observed_input_fails_closed(self):
        old = self.identity("molsysmt", "a" * 40)
        del old["recipe"]
        receipt = GateReceipt("source", "passed", SCOPE, {"molsysmt": old})
        current = {"molsysmt": self.identity("molsysmt", "a" * 40)}

        self.assertIn(
            "molsysmt.recipe: absent from receipt", self.reasons(receipt, current)
        )

    def test_required_participant_missing_from_receipt_fails_closed(self):
        molsysmt = self.identity("molsysmt", "a" * 40)
        viewer = self.identity("molsysviewer", "b" * 40)
        receipt = GateReceipt("installed-pair", "passed", SCOPE, {"molsysmt": molsysmt})

        reasons = stale_reasons(
            receipt,
            gate="installed-pair",
            scope=SCOPE,
            current={"molsysmt": molsysmt, "molsysviewer": viewer},
            required_inputs={"molsysmt": INPUTS, "molsysviewer": INPUTS},
        )
        self.assertIn("molsysviewer: absent from receipt", reasons)


if __name__ == "__main__":
    unittest.main()
