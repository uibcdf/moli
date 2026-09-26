"""Keep MolSysSuite member policy outside MOLI's direct-component scope."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from devtools.scripts.validate_governance import validate_registry

ROOT = Path(__file__).resolve().parents[1]


class DelegatedPolicyBoundaryTests(unittest.TestCase):
    def test_transitive_inheritance_and_foreign_member_owner_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("devguide", "devtools", "MOLI_GUIDE.md"):
                (root / name).symlink_to(ROOT / name)
            text = (ROOT / "moli.toml").read_text(encoding="utf-8")
            (root / "moli.toml").write_text(
                text.replace(
                    'policy_inheritance = "direct-components-with-delegated-boundaries"',
                    'policy_inheritance = "transitive-by-capability"',
                ).replace(
                    'member_policy_owner = "uibcdf/molsyssuite"',
                    'member_policy_owner = "uibcdf/moli"',
                ),
                encoding="utf-8",
            )
            errors = validate_registry(root)
        self.assertIn(
            "moli.toml: policy inheritance must respect delegated boundaries", errors
        )
        self.assertIn(
            "moli.toml: component molsyssuite must own its member policy", errors
        )


if __name__ == "__main__":
    unittest.main()
