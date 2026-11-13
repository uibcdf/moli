"""A newly registered direct Python component needs a distribution decision."""

from __future__ import annotations

import unittest

from devtools.scripts.validate_governance import validate_python_distribution_reviews

POLICIES = {
    "python_distribution": {
        "status": "accepted",
        "applies_to": ["capability:python-package"],
        "primary_public_channel": "uibcdf",
        "third_party_channel": "conda-forge",
        "pypi_route": "reviewed-exception-only",
        "current_pypi_exceptions": ["pytest-receptor"],
        "current_route_issue": "uibcdf/moli#81",
        "review_field": "python_distribution_review",
        "normative": "devguide/policies/python_distribution_policy.md",
    }
}


class PythonDistributionPolicyTests(unittest.TestCase):
    def test_unreviewed_public_pypi_routes_are_rejected(self):
        for changes in (
            {"pypi_route": "optional-verified"},
            {"current_pypi_exceptions": []},
            {"current_pypi_exceptions": ["pytest-receptor", "future"]},
        ):
            with self.subTest(changes=changes):
                policy = {**POLICIES["python_distribution"], **changes}
                errors = validate_python_distribution_reviews(
                    {}, {"python_distribution": policy}
                )
                self.assertTrue(errors)
        self.assertEqual(validate_python_distribution_reviews({}, POLICIES), [])

    def test_future_direct_python_package_needs_own_review(self):
        components = {
            "future": {
                "repository": "uibcdf/future",
                "capabilities": ["python-package"],
            }
        }
        self.assertIn(
            "moli.toml: component future needs a Python distribution review",
            validate_python_distribution_reviews(components, POLICIES),
        )
        components["future"]["python_distribution_review"] = {
            "issue": "uibcdf/other#2",
            "state": "pending",
        }
        self.assertIn(
            "moli.toml: component future has an invalid distribution review issue",
            validate_python_distribution_reviews(components, POLICIES),
        )
        components["future"]["python_distribution_review"]["issue"] = "uibcdf/future#2"
        self.assertEqual(validate_python_distribution_reviews(components, POLICIES), [])


if __name__ == "__main__":
    unittest.main()
