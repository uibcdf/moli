"""Reference checks for derived resources delivered in ZIP or TAR artifacts.

Callers supply the route inventory and the archives built from the candidate.
Conda's nested .conda payload needs a repository-specific archive reader; this
example does not build, install or exercise a distribution.
"""

from __future__ import annotations

import re
import tarfile
import zipfile
from collections.abc import Mapping
from collections.abc import Set as AbstractSet
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class ResourceClaim:
    path: str
    version_pattern: bytes | None = None  # Named `version` capture, if applicable.


@dataclass(frozen=True)
class ArtifactClaim:
    archive: Path
    kind: Literal["zip", "tar"]
    resources: tuple[ResourceClaim, ...]


def inspect_route_artifacts(
    *,
    version: str,
    required_routes: AbstractSet[str],
    claims: Mapping[str, ArtifactClaim],
) -> list[str]:
    """Return route-specific failures for resources inside claimed archives."""
    reasons: list[str] = []
    for route in sorted(required_routes):
        claim = claims.get(route)
        if claim is None:
            reasons.append(f"{route}: no artifact inspection")
            continue
        if not claim.resources:
            reasons.append(f"{route}: no resources inventoried")
            continue
        try:
            if claim.kind == "zip":
                with zipfile.ZipFile(claim.archive) as archive:
                    reasons.extend(
                        _inspect_zip(route, version, archive, claim.resources)
                    )
            elif claim.kind == "tar":
                with tarfile.open(claim.archive, "r:*") as archive:
                    reasons.extend(
                        _inspect_tar(route, version, archive, claim.resources)
                    )
            else:
                reasons.append(f"{route}: unsupported archive kind {claim.kind!r}")
        except (OSError, tarfile.TarError, zipfile.BadZipFile) as exc:
            reasons.append(f"{route}: cannot read archive: {exc}")
    return reasons


def _inspect_zip(
    route: str,
    version: str,
    archive: zipfile.ZipFile,
    resources: tuple[ResourceClaim, ...],
) -> list[str]:
    entries = archive.infolist()
    reasons: list[str] = []
    for resource in resources:
        matches = [entry for entry in entries if entry.filename == resource.path]
        if len(matches) != 1 or matches[0].is_dir():
            reasons.append(
                f"{route}: required resource {resource.path!r} missing or ambiguous"
            )
            continue
        with archive.open(matches[0]) as stream:
            reasons.extend(_check_version(route, version, resource, stream.read()))
    return reasons


def _inspect_tar(
    route: str,
    version: str,
    archive: tarfile.TarFile,
    resources: tuple[ResourceClaim, ...],
) -> list[str]:
    entries = archive.getmembers()
    reasons: list[str] = []
    for resource in resources:
        matches = [entry for entry in entries if entry.name == resource.path]
        if len(matches) != 1 or not matches[0].isfile():
            reasons.append(
                f"{route}: required resource {resource.path!r} missing or ambiguous"
            )
            continue
        stream = archive.extractfile(matches[0])
        if stream is None:
            reasons.append(f"{route}: required resource {resource.path!r} unreadable")
            continue
        with stream:
            reasons.extend(_check_version(route, version, resource, stream.read()))
    return reasons


def _check_version(
    route: str, version: str, resource: ResourceClaim, data: bytes
) -> list[str]:
    if resource.version_pattern is None:
        return []
    match = re.search(resource.version_pattern, data)
    if match is None or "version" not in match.groupdict():
        return [f"{route}: {resource.path!r} has no readable embedded version"]
    try:
        found = match.group("version").decode("ascii")
    except UnicodeDecodeError:
        return [f"{route}: {resource.path!r} has no readable embedded version"]
    if found != version:
        return [f"{route}: {resource.path!r} embeds {found!r}, expected {version!r}"]
    return []
