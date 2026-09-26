"""Archive fixtures show that one route cannot certify another route's bytes."""

from __future__ import annotations

import io
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path

from devtools.scripts.distribution_artifact_evidence import (
    ArtifactClaim,
    ResourceClaim,
    inspect_route_artifacts,
)

VERSION_PATTERN = rb'RELEASE_VERSION = "(?P<version>[^"]+)"'
WHEEL_RESOURCE = ResourceClaim("example/runtime.js", VERSION_PATTERN)
NPM_RESOURCE = ResourceClaim("package/dist/runtime.js", VERSION_PATTERN)


class DistributionArtifactEvidenceTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        self.wheel = root / "example-1.2.3-py3-none-any.whl"
        self.npm = root / "example-1.2.3.tgz"
        self.write_wheel(b'RELEASE_VERSION = "1.2.3"')
        self.write_npm(b'RELEASE_VERSION = "1.2.3"')

    def write_wheel(self, content: bytes, *, path: str = WHEEL_RESOURCE.path):
        with zipfile.ZipFile(self.wheel, "w") as archive:
            archive.writestr(path, content)

    def write_npm(self, content: bytes):
        with tarfile.open(self.npm, "w:gz") as archive:
            info = tarfile.TarInfo(NPM_RESOURCE.path)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))

    def reasons(self, *, routes: set[str] | None = None) -> list[str]:
        return inspect_route_artifacts(
            version="1.2.3",
            required_routes={"wheel", "npm"} if routes is None else routes,
            claims={
                "wheel": ArtifactClaim(self.wheel, "zip", (WHEEL_RESOURCE,)),
                "npm": ArtifactClaim(self.npm, "tar", (NPM_RESOURCE,)),
            },
        )

    def test_both_claimed_archives_contain_current_runtime(self):
        self.assertEqual(self.reasons(), [])

    def test_stale_wheel_fails_even_when_npm_regenerates_current_runtime(self):
        self.write_wheel(b'RELEASE_VERSION = "1.2.0"')

        self.assertEqual(
            self.reasons(),
            ["wheel: 'example/runtime.js' embeds '1.2.0', expected '1.2.3'"],
        )

    def test_missing_wheel_resource_fails_even_when_npm_passes(self):
        self.write_wheel(b'RELEASE_VERSION = "1.2.3"', path="example/other.js")

        self.assertEqual(
            self.reasons(),
            ["wheel: required resource 'example/runtime.js' missing or ambiguous"],
        )

    def test_missing_version_marker_fails(self):
        self.write_npm(b"runtime without a release version")

        self.assertEqual(
            self.reasons(),
            ["npm: 'package/dist/runtime.js' has no readable embedded version"],
        )

    def test_claimed_route_without_inspection_fails(self):
        self.assertEqual(
            self.reasons(routes={"wheel", "npm", "conda"}),
            ["conda: no artifact inspection"],
        )


if __name__ == "__main__":
    unittest.main()
