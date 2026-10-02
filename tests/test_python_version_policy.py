"""Guard the accepted Python 3.14 development baseline."""

from __future__ import annotations

import unittest

from devtools.scripts.validate_governance import validate_python_versions


class PythonVersionPolicyTests(unittest.TestCase):
    def test_old_routine_and_range_are_rejected(self):
        policies = {
            "python": {
                "requires_python": ">=3.11,<3.15",
                "development_version": "3.14",
                "ci_versions": ["3.11", "3.12", "3.13", "3.14"],
            },
            "python_ci": {"routine_python": "3.14"},
        }
        self.assertEqual(validate_python_versions(policies), [])
        policies["python"]["requires_python"] = ">=3.11,<3.14"
        policies["python_ci"]["routine_python"] = "3.13"
        errors = validate_python_versions(policies)
        self.assertIn("moli.toml: Python policy has invalid requires_python", errors)
        self.assertIn("moli.toml: routine Python CI must use 3.14", errors)


if __name__ == "__main__":
    unittest.main()
