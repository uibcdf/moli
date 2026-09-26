"""Small reference evaluator for release-candidate evidence fixtures.

Gate owners choose their own receipt format and declare the inputs each gate
consumes. This module demonstrates comparison of recorded identities; it does
not discover package routes or replace their installed-artifact tests.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GateReceipt:
    gate: str
    result: str
    scope: Mapping[str, str]
    participants: Mapping[str, Mapping[str, str]]


def capture_candidate(
    *, commit: str, facts: Mapping[str, str], files: Mapping[str, Path]
) -> dict[str, str]:
    """Capture a component's exact commit, declared facts and file digests."""
    if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        raise ValueError("candidate needs a full lowercase commit SHA")
    if "source_commit" in facts or "source_commit" in files or set(facts) & set(files):
        raise ValueError("candidate input names must be unique")
    identity = {"source_commit": commit}
    for name, value in facts.items():
        if not name or not isinstance(value, str) or not value:
            raise ValueError(f"candidate fact {name!r} is empty")
        identity[name] = value
    for name, path in files.items():
        if not name:
            raise ValueError("candidate file input has no name")
        with path.open("rb") as stream:
            identity[name] = hashlib.file_digest(stream, "sha256").hexdigest()
    return identity


def stale_reasons(
    receipt: GateReceipt,
    *,
    gate: str,
    scope: Mapping[str, str],
    current: Mapping[str, Mapping[str, str]],
    required_inputs: Mapping[str, set[str]],
) -> list[str]:
    """Explain why a gate receipt cannot certify the current candidates."""
    reasons: list[str] = []
    if receipt.gate != gate:
        reasons.append("gate changed")
    if receipt.result != "passed":
        reasons.append("gate did not pass")
    if dict(receipt.scope) != dict(scope):
        reasons.append("tested scope changed")
    if not required_inputs:
        reasons.append("gate has no declared participants")

    for subject in sorted(set(receipt.participants) | set(required_inputs)):
        recorded = receipt.participants.get(subject)
        observed = current.get(subject)
        if recorded is None:
            reasons.append(f"{subject}: absent from receipt")
            continue
        if observed is None:
            reasons.append(f"{subject}: no current identity")
            continue
        fields = (
            {"source_commit"} | set(required_inputs.get(subject, set())) | set(recorded)
        )
        for field in sorted(fields):
            if field not in recorded:
                reasons.append(f"{subject}.{field}: absent from receipt")
            elif field not in observed:
                reasons.append(f"{subject}.{field}: no current identity")
            elif recorded[field] != observed[field]:
                reasons.append(f"{subject}.{field}: changed")
    return reasons
