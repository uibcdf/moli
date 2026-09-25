"""Keep platform claims explicit when registering direct Python components."""

from __future__ import annotations

import unittest

from devtools.scripts.validate_governance import validate_os_support

POLICIES = {
    "python_ci": {
        "baseline_os": ["linux", "macos"],
        "optional_os": ["windows"],
        "claimed_non_linux_frequency": "weekly",
        "release_installed_matrix": "all-claimed-os-and-python-minors",
    }
}


class OsSupportPolicyTests(unittest.TestCase):
    def test_new_direct_python_component_needs_platform_claim_and_owner_review(self):
        component = {"repository": "uibcdf/future", "capabilities": ["python-package"]}
        errors = validate_os_support({"future": component}, POLICIES)
        self.assertTrue(any("supported_os" in error for error in errors))

        component["supported_os"] = []
        component["os_support_review"] = {"issue": "uibcdf/future#2", "state": "pending"}
        self.assertEqual(validate_os_support({"future": component}, POLICIES), [])

        component["supported_os"] = ["linux", "macos"]
        component["os_support_review"]["state"] = "adopted"
        self.assertEqual(validate_os_support({"future": component}, POLICIES), [])

    def test_windows_is_optional_and_macos_needs_a_tracked_exception(self):
        component = {
            "repository": "uibcdf/future",
            "capabilities": ["python-package"],
            "supported_os": ["linux"],
            "os_support_review": {"issue": "uibcdf/future#2", "state": "adopted"},
        }
        errors = validate_os_support({"future": component}, POLICIES)
        self.assertTrue(any("macOS" in error for error in errors))

        component["macos_exception_issue"] = "uibcdf/future#3"
        component["os_support_review"]["state"] = "excepted"
        self.assertEqual(validate_os_support({"future": component}, POLICIES), [])

        component["supported_os"] = ["linux", "macos", "windows"]
        del component["macos_exception_issue"]
        component["os_support_review"]["state"] = "adopted"
        self.assertEqual(validate_os_support({"future": component}, POLICIES), [])

    def test_delegated_member_rows_are_not_registered_in_moli(self):
        component = {
            "repository": "uibcdf/molsyssuite",
            "capabilities": ["python-package"],
            "internal_governance": "delegated",
        }
        self.assertEqual(validate_os_support({"suite": component}, POLICIES), [])


if __name__ == "__main__":
    unittest.main()
