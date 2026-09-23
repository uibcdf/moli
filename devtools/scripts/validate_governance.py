"""Validate the local MOLI governance registry and report records."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OPEN = {"open", "active", "blocked", "partial"}
CLOSED = {"resolved", "withdrawn", "superseded"}
VERIFICATION = {"reproduced", "measured", "inspected", "upstream", "asserted"}
ISSUE = re.compile(r"^uibcdf/[A-Za-z0-9_.-]+#[1-9][0-9]*$")


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML-like front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated front matter")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_reports(root: Path) -> list[str]:
    errors: list[str] = []
    for directory, archived in [
        (root / "devguide/pending_bugs", False),
        (root / "devguide/pending_proposals", False),
        (root / "devguide/archive", True),
    ]:
        if not directory.is_dir():
            errors.append(f"{directory.relative_to(root)}: missing")
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            try:
                data = front_matter(path)
            except ValueError as error:
                errors.append(f"{path.relative_to(root)}: {error}")
                continue
            for key in ("summary", "issue", "status", "opened", "verification"):
                if not data.get(key):
                    errors.append(f"{path.relative_to(root)}: missing {key}")
            if data.get("issue") and not ISSUE.fullmatch(data["issue"]):
                errors.append(f"{path.relative_to(root)}: invalid issue identity")
            status = data.get("status")
            if status and status not in OPEN | CLOSED:
                errors.append(f"{path.relative_to(root)}: invalid status {status!r}")
            if archived and status not in CLOSED:
                errors.append(f"{path.relative_to(root)}: archived report must be closed")
            if not archived and status in CLOSED:
                errors.append(f"{path.relative_to(root)}: closed report belongs in archive")
            verification = data.get("verification")
            if verification and verification not in VERIFICATION:
                errors.append(f"{path.relative_to(root)}: invalid verification {verification!r}")
    return errors


def validate_registry(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "moli.toml"
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        return [f"moli.toml: {error}"]
    required = {"sabueso", "praxis", "nextia", "molsyssuite", "moli-agent"}
    components = set(data.get("components", {}))
    missing = sorted(required - components)
    if missing:
        errors.append("moli.toml: missing components: " + ", ".join(missing))
    policies = data.get("policies", {})
    for name in ("reporting_lifecycle", "cross_component_feedback", "component_guide"):
        if policies.get(name, {}).get("status") != "accepted":
            errors.append(f"moli.toml: policy {name} is not accepted")
    return errors


def main() -> int:
    errors = validate_registry(ROOT) + validate_reports(ROOT)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("MOLI governance is locally valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
