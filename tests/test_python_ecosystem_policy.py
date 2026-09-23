"""The registry must make direct Python component adoption visible."""

from __future__ import annotations

import unittest

from devtools.scripts.validate_governance import validate_python_ecosystem_reviews

POLICIES = {
    "python_support_libraries": {
        "status": "accepted",
        "applies_to": ["capability:python-package"],
        "libraries": ["argdigest", "depdigest", "smonitor", "pyunitwizard"],
        "review_field": "python_ecosystem_review",
        "normative": "devguide/policies/python_support_libraries_policy.md",
    },
    "python_developer_tools": {
        "status": "accepted",
        "applies_to": ["capability:python-package"],
        "tools": ["pytest-receptor", "gh-run-receptor"],
        "review_field": "python_ecosystem_review",
        "normative": "devguide/policies/python_developer_tools_policy.md",
    },
}


class PythonEcosystemPolicyTests(unittest.TestCase):
    def test_future_direct_python_package_needs_review(self):
        components = {
            "future": {
                "repository": "uibcdf/future",
                "capabilities": ["python-package"],
            }
        }
        self.assertIn(
            "moli.toml: component future needs a Python ecosystem review",
            validate_python_ecosystem_reviews(components, POLICIES),
        )
        components["future"]["python_ecosystem_review"] = {
            "issue": "uibcdf/future#2",
            "state": "pending",
        }
        self.assertEqual(validate_python_ecosystem_reviews(components, POLICIES), [])

    def test_review_must_belong_to_component_repository(self):
        components = {
            "future": {
                "repository": "uibcdf/future",
                "capabilities": ["python-package"],
                "python_ecosystem_review": {
                    "issue": "uibcdf/other#2",
                    "state": "pending",
                },
            }
        }
        self.assertIn(
            "moli.toml: component future has an invalid review issue",
            validate_python_ecosystem_reviews(components, POLICIES),
        )


if __name__ == "__main__":
    unittest.main()
