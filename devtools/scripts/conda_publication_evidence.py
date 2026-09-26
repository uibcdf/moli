"""Illustrative pre-upload and public-poststate checks for Conda file coordinates.

Callers must obtain an independent, current registry snapshot and compute the
candidate file's SHA-256. This module performs no network or registry mutation.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class CondaCoordinate:
    owner: str
    package: str
    version: str
    subdir: str
    filename: str


@dataclass(frozen=True)
class RegistryFile:
    coordinate: CondaCoordinate
    sha256: str
    labels: frozenset[str]


def upload_preflight_reasons(
    coordinate: CondaCoordinate, records: Iterable[RegistryFile]
) -> list[str]:
    """An occupied file coordinate blocks upload regardless of label or digest."""
    if any(record.coordinate == coordinate for record in records):
        return ["coordinate already occupied; upload would replace an existing file"]
    return []


def public_poststate_reasons(
    coordinate: CondaCoordinate,
    expected_sha256: str,
    records: Iterable[RegistryFile],
    *,
    public_label: str = "main",
) -> list[str]:
    """Verify the exact file and public label from a read-only registry snapshot."""
    matches = [record for record in records if record.coordinate == coordinate]
    if not matches:
        return ["exact coordinate absent from registry"]
    if len(matches) != 1:
        return ["exact coordinate has ambiguous registry records"]

    record = matches[0]
    reasons: list[str] = []
    if public_label not in record.labels:
        reasons.append(f"public label {public_label!r} absent")
    if record.sha256 != expected_sha256:
        reasons.append(
            f"public file SHA-256 changed: {record.sha256} != {expected_sha256}"
        )
    return reasons
