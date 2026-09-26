"""An occupied coordinate and a changed public digest must fail closed."""

from __future__ import annotations

import unittest

from devtools.scripts.conda_publication_evidence import (
    CondaCoordinate,
    RegistryFile,
    public_poststate_reasons,
    upload_preflight_reasons,
)

COORDINATE = CondaCoordinate(
    "uibcdf", "example", "1.2.3", "noarch", "example-1.2.3-py_0.conda"
)
EXPECTED_SHA256 = "a" * 64
CHANGED_SHA256 = "b" * 64


class CondaPublicationEvidenceTests(unittest.TestCase):
    def test_unoccupied_coordinate_can_be_uploaded(self):
        self.assertEqual(upload_preflight_reasons(COORDINATE, []), [])

    def test_staged_coordinate_blocks_upload_even_with_identical_digest(self):
        staged = RegistryFile(COORDINATE, EXPECTED_SHA256, frozenset({"staging"}))

        self.assertEqual(
            upload_preflight_reasons(COORDINATE, [staged]),
            ["coordinate already occupied; upload would replace an existing file"],
        )

    def test_public_coordinate_blocks_overwrite_of_changed_digest(self):
        public = RegistryFile(COORDINATE, CHANGED_SHA256, frozenset({"main"}))

        self.assertEqual(
            upload_preflight_reasons(COORDINATE, [public]),
            ["coordinate already occupied; upload would replace an existing file"],
        )

    def test_exact_promoted_file_passes_independent_poststate_check(self):
        public = RegistryFile(
            COORDINATE, EXPECTED_SHA256, frozenset({"staging", "main"})
        )

        self.assertEqual(
            public_poststate_reasons(COORDINATE, EXPECTED_SHA256, [public]), []
        )

    def test_changed_public_digest_fails_even_if_mutation_reported_success(self):
        public = RegistryFile(COORDINATE, CHANGED_SHA256, frozenset({"main"}))

        self.assertEqual(
            public_poststate_reasons(COORDINATE, EXPECTED_SHA256, [public]),
            [f"public file SHA-256 changed: {CHANGED_SHA256} != {EXPECTED_SHA256}"],
        )

    def test_staged_file_without_public_label_does_not_prove_publication(self):
        staged = RegistryFile(COORDINATE, EXPECTED_SHA256, frozenset({"staging"}))

        self.assertEqual(
            public_poststate_reasons(COORDINATE, EXPECTED_SHA256, [staged]),
            ["public label 'main' absent"],
        )

    def test_other_subdir_does_not_prove_exact_public_coordinate(self):
        other = RegistryFile(
            CondaCoordinate(
                "uibcdf", "example", "1.2.3", "linux-64", COORDINATE.filename
            ),
            EXPECTED_SHA256,
            frozenset({"main"}),
        )

        self.assertEqual(
            public_poststate_reasons(COORDINATE, EXPECTED_SHA256, [other]),
            ["exact coordinate absent from registry"],
        )


if __name__ == "__main__":
    unittest.main()
