"""Check the universal MOLI governance surface of one component checkout."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "MOLI_GUIDE.md",
    "devguide/AGENTS.md",
    "devguide/pending_bugs/README.md",
    "devguide/pending_proposals/README.md",
    "devguide/archive/README.md",
    "devguide/templates/report.md",
]


def check(root: Path, canonical_guide: Path | None = None, require_direct_guide: bool = True) -> list[str]:
    errors: list[str] = []
    required = REQUIRED if require_direct_guide else [
        item for item in REQUIRED if item not in {"MOLI_GUIDE.md", "devguide/AGENTS.md"}
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"{relative}: missing")
    agents = root / "AGENTS.md"
    if require_direct_guide and agents.is_file():
        content = agents.read_text(encoding="utf-8")
        if "MOLI_GUIDE.md" not in content:
            errors.append("AGENTS.md: must reference MOLI_GUIDE.md")
        if "MOLI_GUIDE.md#durable-instructions-for-development-agents" not in content:
            errors.append("AGENTS.md: must link to the agent-instruction lifecycle")
        if "devguide/AGENTS.md" not in content:
            errors.append("AGENTS.md: must route developer-guide work to devguide/AGENTS.md")
    nested = root / "devguide/AGENTS.md"
    if require_direct_guide and nested.is_file():
        content = nested.read_text(encoding="utf-8")
        for reference in (
            "../AGENTS.md",
            "MOLI_GUIDE.md#reporting-bugs-and-proposals",
            "pending_bugs/",
            "pending_proposals/",
            "archive/",
        ):
            if reference not in content:
                errors.append(f"devguide/AGENTS.md: must reference {reference}")
    if canonical_guide is not None and (root / "MOLI_GUIDE.md").is_file():
        if (root / "MOLI_GUIDE.md").read_bytes() != canonical_guide.read_bytes():
            errors.append("MOLI_GUIDE.md: differs from canonical guide")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--canonical-guide", type=Path)
    parser.add_argument("--delegated", action="store_true", help="Check a MOLI component with delegated internal governance; do not require a vendored MOLI_GUIDE.md.")
    args = parser.parse_args()
    errors = check(args.target.resolve(), args.canonical_guide.resolve() if args.canonical_guide else None, require_direct_guide=not args.delegated)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"{args.target}: conforms to MOLI governance core.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
