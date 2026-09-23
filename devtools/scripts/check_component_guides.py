"""Check byte-identical MOLI guides in directly governed components."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import tomllib

ROOT = Path(__file__).resolve().parents[2]


def vendored_components(registry: dict[str, object]) -> list[str]:
    """Return repositories whose declared delivery mode requires a local guide."""
    return sorted(
        str(component["repository"])
        for component in registry["components"].values()
        if component["guide_delivery"] == "vendored"
    )


def check(workspace: Path, registry: dict[str, object]) -> list[str]:
    """Return missing, changed, or unreferenced guide findings."""
    guide = str(registry["policies"]["component_guide"]["filename"])
    source = workspace / "moli" / guide
    if not source.is_file():
        return [f"{source}: canonical guide is missing"]
    expected = source.read_bytes()
    findings: list[str] = []
    for repository in vendored_components(registry):
        root = workspace / repository.rsplit("/", 1)[-1]
        target = root / guide
        if not target.is_file():
            findings.append(f"{target}: guide is missing")
        elif target.read_bytes() != expected:
            findings.append(f"{target}: guide differs from MOLI")
        agents = root / "AGENTS.md"
        if not agents.is_file() or guide not in agents.read_text(encoding="utf-8"):
            findings.append(f"{agents}: must reference {guide}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=ROOT.parent)
    parser.add_argument("--list-repositories", action="store_true")
    args = parser.parse_args()
    registry = tomllib.loads((ROOT / "moli.toml").read_text(encoding="utf-8"))
    if args.list_repositories:
        for repository in vendored_components(registry):
            print(repository)
        return 0
    findings = check(args.workspace.resolve(), registry)
    for finding in findings:
        print(finding, file=sys.stderr)
    if not findings:
        print("All directly governed MOLI guides match their canonical source.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
