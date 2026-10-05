"""Tests for the MOLI Development Observatory."""

from __future__ import annotations

import unittest

from devtools.scripts.development_observatory import dashboard_html, discover_scope, metrics

MOLI = {
    "components": {
        "sabueso": {"repository": "uibcdf/sabueso", "role": "knowledge"},
        "molsyssuite": {"repository": "uibcdf/molsyssuite", "role": "modeling-ecosystem"},
    },
    "support_infrastructure": {
        "resources": [
            {"repository": "uibcdf/pytest-receptor", "kind": "developer-receptor"},
            {"repository": "uibcdf/external-action", "kind": "github-action"},
        ]
    },
}
SUITE = {
    "members": [
        {"repository": "uibcdf/molsysmt", "role": "scientific-component"},
        {"repository": "uibcdf/pytest-receptor", "role": "developer-tool"},
    ]
}


class ObservatoryTests(unittest.TestCase):
    def test_scope_is_registry_driven_and_deduplicated(self):
        scope = discover_scope(MOLI, SUITE)
        indexed = {item["repository"]: item for item in scope}
        self.assertEqual(indexed["uibcdf/moli"]["layer"], "MOLI")
        self.assertEqual(indexed["uibcdf/molsyssuite"]["layer"], "MolSysSuite")
        self.assertEqual(indexed["uibcdf/molsysmt"]["layer"], "Scientific components")
        self.assertEqual(indexed["uibcdf/pytest-receptor"]["layer"], "Infrastructure")
        self.assertEqual(len(indexed), len(scope))

    def test_metrics_capture_flow_layers_and_age(self):
        dataset = {
            "generated_at": "2026-10-05T12:00:00Z",
            "scope": [
                {"repository": "uibcdf/moli", "layer": "MOLI"},
                {"repository": "uibcdf/molsysmt", "layer": "Scientific components"},
            ],
            "issues": [
                {"repository": "uibcdf/moli", "state": "closed", "created_at": "2026-10-01T10:00:00Z", "closed_at": "2026-10-03T10:00:00Z"},
                {"repository": "uibcdf/molsysmt", "state": "open", "created_at": "2026-10-02T10:00:00Z", "closed_at": None},
                {"repository": "uibcdf/molsysmt", "state": "closed", "created_at": "2026-10-02T11:00:00Z", "closed_at": "2026-10-04T10:00:00Z"},
            ],
            "provenance": {"issue_lifecycle_model": "snapshot-v1"},
        }
        result = metrics(dataset, days=5, timezone_name="UTC")
        self.assertEqual(result["summary"]["opened"], 3)
        self.assertEqual(result["summary"]["closed"], 2)
        self.assertEqual(result["summary"]["net_change"], 1)
        self.assertEqual(result["summary"]["current_open"], 1)
        self.assertEqual(result["daily"][-1]["cumulative_net_change"], 1)
        science = next(item for item in result["layers"] if item["layer"] == "Scientific components")
        self.assertEqual(science["opened"], 2)
        self.assertEqual(science["closed"], 1)
        self.assertEqual(sum(item["count"] for item in result["issue_age"]), 1)

    def test_html_consumes_json_and_documents_portability(self):
        html = dashboard_html()
        self.assertIn("fetch('metrics.json')", html)
        self.assertIn("issues.json", html)
        self.assertIn("Grafana", html)
        self.assertIn("MOLI Development Observatory", html)


if __name__ == "__main__":
    unittest.main()
