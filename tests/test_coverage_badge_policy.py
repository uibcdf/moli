"""Require a tracked coverage decision for directly governed Python components."""

from __future__ import annotations

import unittest

from devtools.scripts.validate_governance import validate_coverage_reviews

POLICIES = {
    "repository_badges": {
        "coverage_review_field": "coverage_review",
        "coverage_image": "codecov-live-percentage",
    }
}


class CoverageReviewTests(unittest.TestCase):
    def test_direct_python_component_needs_owned_review(self):
        component = {"repository": "uibcdf/example", "capabilities": ["python-package"]}
        self.assertTrue(validate_coverage_reviews({"example": component}, POLICIES))
        component["coverage_review"] = {"issue": "uibcdf/example#1", "state": "pending"}
        self.assertEqual(
            validate_coverage_reviews({"example": component}, POLICIES), []
        )

    def test_delegated_members_remain_suite_owned(self):
        component = {
            "repository": "uibcdf/molsyssuite",
            "capabilities": ["python-package"],
            "internal_governance": "delegated",
        }
        self.assertEqual(validate_coverage_reviews({"suite": component}, POLICIES), [])


if __name__ == "__main__":
    unittest.main()
