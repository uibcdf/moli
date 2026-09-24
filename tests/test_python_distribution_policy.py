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
        "pypi_route": "optional-verified",
        "review_field": "python_distribution_review",
        "normative": "devguide/policies/python_distribution_policy.md",
    }
}


class PythonDistributionPolicyTests(unittest.TestCase):
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
