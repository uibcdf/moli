"""Tests for direct component guide delivery."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from devtools.scripts.check_component_guides import check, vendored_components

REGISTRY = {
    "policies": {"component_guide": {"filename": "MOLI_GUIDE.md"}},
    "components": {
        "sabueso": {"repository": "uibcdf/sabueso", "guide_delivery": "vendored"},
        "molsyssuite": {
            "repository": "uibcdf/molsyssuite",
            "guide_delivery": "reference",
        },
    },
}


class ComponentGuideTests(unittest.TestCase):
    def test_only_vendored_components_need_a_copy(self):
        self.assertEqual(vendored_components(REGISTRY), ["uibcdf/sabueso"])

    def test_exact_copy_and_agents_route_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "moli/MOLI_GUIDE.md"
            source.parent.mkdir()
            source.write_text("canonical\n", encoding="utf-8")
            component = workspace / "sabueso"
            component.mkdir()
            (component / "MOLI_GUIDE.md").write_bytes(source.read_bytes())
            (component / "AGENTS.md").write_text(
                "Read MOLI_GUIDE.md\n", encoding="utf-8"
            )
            self.assertEqual(check(workspace, REGISTRY), [])

    def test_drift_and_missing_route_are_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "moli/MOLI_GUIDE.md"
            source.parent.mkdir()
            source.write_text("canonical\n", encoding="utf-8")
            component = workspace / "sabueso"
            component.mkdir()
            (component / "MOLI_GUIDE.md").write_text("changed\n", encoding="utf-8")
            findings = check(workspace, REGISTRY)
            self.assertEqual(len(findings), 2)
            self.assertTrue(any("differs from MOLI" in item for item in findings))
            self.assertTrue(any("must reference" in item for item in findings))

    def test_python_project_requires_registered_capability(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "moli/MOLI_GUIDE.md"
            source.parent.mkdir()
            source.write_text("canonical\n", encoding="utf-8")
            component = workspace / "sabueso"
            component.mkdir()
            (component / "MOLI_GUIDE.md").write_bytes(source.read_bytes())
            (component / "AGENTS.md").write_text("Read MOLI_GUIDE.md\n", encoding="utf-8")
            (component / "pyproject.toml").write_text(
                '[project]\nname = "sabueso"\n', encoding="utf-8"
            )
            findings = check(workspace, REGISTRY)
            self.assertTrue(any("needs python-package capability" in item for item in findings))

            REGISTRY["components"]["sabueso"]["capabilities"] = ["python-package"]
            try:
                self.assertEqual(check(workspace, REGISTRY), [])
            finally:
                del REGISTRY["components"]["sabueso"]["capabilities"]


if __name__ == "__main__":
    unittest.main()
