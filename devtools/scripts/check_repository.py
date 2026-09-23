"""Check the universal MOLI governance surface of one component checkout."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "MOLI_GUIDE.md",
    "devguide/pending_bugs/README.md",
    "devguide/pending_proposals/README.md",
    "devguide/archive/README.md",
    "devguide/templates/report.md",
]


def check(root: Path, canonical_guide: Path | None = None) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"{relative}: missing")
    agents = root / "AGENTS.md"
    if agents.is_file() and "MOLI_GUIDE.md" not in agents.read_text(encoding="utf-8"):
        errors.append("AGENTS.md: must reference MOLI_GUIDE.md")
    if canonical_guide is not None and (root / "MOLI_GUIDE.md").is_file():
        if (root / "MOLI_GUIDE.md").read_bytes() != canonical_guide.read_bytes():
            errors.append("MOLI_GUIDE.md: differs from canonical guide")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--canonical-guide", type=Path)
    args = parser.parse_args()
    errors = check(args.target.resolve(), args.canonical_guide.resolve() if args.canonical_guide else None)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"{args.target}: conforms to MOLI governance core.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
