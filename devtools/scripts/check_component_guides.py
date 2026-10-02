"""Check byte-identical MOLI guides in directly governed components."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import tomllib

if __package__:
    from .check_repository import check as check_repository
else:
    from check_repository import check as check_repository

ROOT = Path(__file__).resolve().parents[2]
MACOS_WORDING = (
    "macOS support is currently limited to Apple Silicon (arm64). "
    "Intel-based macOS (x86_64) is not part of the supported platform matrix. "
    "Support may be reconsidered if there is demonstrated user demand."
)
BADGE = re.compile(r"\[!\[[^\]]*\]\(([^)]+)\)\]\(([^)]+)\)")


def check_public_claims(
    root: Path, repository: str, component: dict[str, object]
) -> list[str]:
    """Validate local claim shape; service freshness remains a networked review."""
    errors: list[str] = []
    readme = root / "README.md"
    if not readme.is_file():
        return ["README.md: missing"]
    content = readme.read_text(encoding="utf-8")
    if "macos" in component.get("supported_os", []):
        if MACOS_WORDING not in " ".join(content.split()):
            errors.append("README.md: missing Apple Silicon support boundary")
        for workflow in (root / ".github/workflows").glob("*.y*ml"):
            source = workflow.read_text(encoding="utf-8")
            if re.search(r"macos-[0-9]+-intel\b", source) or re.search(
                r"platform_osx-64:\s*true\b", source
            ):
                errors.append(
                    f"{workflow.relative_to(root)}: active Intel macOS target"
                )
    codecov_badges = [
        (image, target)
        for image, target in BADGE.findall(content)
        if "codecov.io" in image or "codecov.io" in target
    ]
    review = component.get("coverage_review", {})
    if (
        isinstance(review, dict)
        and review.get("state") == "adopted"
        and not codecov_badges
    ):
        errors.append(
            "README.md: adopted coverage review needs a Codecov percentage badge"
        )
    expected_image = f"https://codecov.io/gh/{repository}/branch/main/graph/badge.svg"
    expected_target = f"https://app.codecov.io/gh/{repository}"
    for image, target in codecov_badges:
        if image != expected_image or target != expected_target:
            errors.append(
                "README.md: Codecov badge must target this repository's main branch"
            )
    return errors


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
        component = next(
            item
            for item in registry["components"].values()
            if item["repository"] == repository
        )
        findings.extend(
            f"{repository}: {error}"
            for error in check_public_claims(root, repository, component)
        )
        pyproject = root / "pyproject.toml"
        if pyproject.is_file():
            try:
                project = tomllib.loads(pyproject.read_text(encoding="utf-8")).get(
                    "project", {}
                )
            except tomllib.TOMLDecodeError:
                findings.append(f"{pyproject}: invalid TOML")
                continue
            if project.get("name") and "python-package" not in component.get(
                "capabilities", []
            ):
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
