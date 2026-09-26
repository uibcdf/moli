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


@dataclass(frozen=True)
class GateException:
    release_version: str
    observed_gate: GateReceipt
    evidence_ref: str
    observed_failure: str
    compensating_evidence: str
    decision_owner: str
    decided_at: str
    decision_ref: str
    remediation_issue: str
    release_limitation: str
    expiry_condition: str


def release_decision_reasons(
    observed: GateReceipt,
    *,
    reported_result: str,
    release_version: str,
    exception_allowed: bool,
    exception: GateException | None,
) -> list[str]:
    """Keep a gate's result separate from a candidate-specific release decision."""
    reasons: list[str] = []
    if reported_result != observed.result:
        reasons.append("reported gate result differs from observed result")
    if observed.result == "passed":
        if exception is not None:
            reasons.append("passing gate does not need an exception")
        return reasons
    if not exception_allowed:
        reasons.append("gate is not exception-eligible")
    if exception is None:
        reasons.append("unmet gate has no release exception")
        return reasons
    if exception.release_version != release_version:
        reasons.append("exception belongs to another release version")
    if exception.observed_gate != observed:
        reasons.append("exception belongs to another gate or candidate")
    for field in (
        "evidence_ref",
        "observed_failure",
        "compensating_evidence",
        "decision_owner",
        "decided_at",
        "decision_ref",
        "remediation_issue",
        "release_limitation",
        "expiry_condition",
    ):
        if not getattr(exception, field).strip():
            reasons.append(f"exception lacks {field}")
    return reasons


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
