"""Check byte-identical MOLI guides in directly governed components."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import tomllib

from check_repository import check as check_repository

ROOT = Path(__file__).resolve().parents[2]


def vendored_components(registry: dict[str, object]) -> list[str]:
    """Return repositories whose declared delivery mode requires a local guide."""
    return sorted(
        str(component["repository"])
        for component in registry["components"].values()
        if component["guide_delivery"] == "vendored"
    )


def check(workspace: Path, registry: dict[str, object]) -> list[str]:
    """Return guide-delivery and direct Python classification findings."""
    guide = str(registry["policies"]["component_guide"]["filename"])
    source = workspace / "moli" / guide
    if not source.is_file():
        return [f"{source}: canonical guide is missing"]
    findings: list[str] = []
    for repository in vendored_components(registry):
        root = workspace / repository.rsplit("/", 1)[-1]
        findings.extend(
            f"{repository}: {error}"
            for error in check_repository(root, source, require_direct_guide=True)
        )
        pyproject = root / "pyproject.toml"
        if pyproject.is_file():
            try:
                project = tomllib.loads(pyproject.read_text(encoding="utf-8")).get("project", {})
            except tomllib.TOMLDecodeError:
                findings.append(f"{pyproject}: invalid TOML")
                continue
            component = next(
                item for item in registry["components"].values() if item["repository"] == repository
            )
            if project.get("name") and "python-package" not in component.get("capabilities", []):
                findings.append(
                    f"{repository}: declared Python project needs python-package capability in moli.toml"
                )
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
