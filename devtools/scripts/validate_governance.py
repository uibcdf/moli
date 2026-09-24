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
PYTHON_ECOSYSTEM_STATES = {"pending", "partial", "adopted", "excepted"}


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


def validate_python_ecosystem_reviews(
    components: dict[str, dict], policies: dict[str, dict]
) -> list[str]:
    """Require an adoption review for each directly governed Python package."""
    errors: list[str] = []
    expected = {
        "python_support_libraries": ["argdigest", "depdigest", "smonitor", "pyunitwizard"],
        "python_developer_tools": ["pytest-receptor", "gh-run-receptor"],
    }
    for name, packages in expected.items():
        policy = policies.get(name, {})
        if policy.get("status") != "accepted":
            errors.append(f"moli.toml: policy {name} is not accepted")
        if policy.get("applies_to") != ["capability:python-package"]:
            errors.append(f"moli.toml: policy {name} must apply to Python packages")
        key = "libraries" if name == "python_support_libraries" else "tools"
        if policy.get(key) != packages:
            errors.append(f"moli.toml: policy {name} has unexpected {key}")
        if policy.get("review_field") != "python_ecosystem_review":
            errors.append(f"moli.toml: policy {name} must require a review")
        if not policy.get("normative"):
            errors.append(f"moli.toml: policy {name} has no normative document")
    for name, component in components.items():
        if "python-package" not in component.get("capabilities", []):
            continue
        if component.get("internal_governance") == "delegated":
            continue
        review = component.get("python_ecosystem_review")
        if not isinstance(review, dict):
            errors.append(f"moli.toml: component {name} needs a Python ecosystem review")
            continue
        repository = component.get("repository", "")
        issue = review.get("issue", "")
        if not isinstance(issue, str) or not ISSUE.fullmatch(issue) or not issue.startswith(
            f"{repository}#"
        ):
            errors.append(f"moli.toml: component {name} has an invalid review issue")
        if review.get("state") not in PYTHON_ECOSYSTEM_STATES:
            errors.append(f"moli.toml: component {name} has an invalid review state")
    return errors


def validate_python_distribution_reviews(
    components: dict[str, dict], policies: dict[str, dict]
) -> list[str]:
    """Keep distribution decisions visible for every direct Python component."""
    errors: list[str] = []
    policy = policies.get("python_distribution", {})
    expected = {
        "status": "accepted",
        "applies_to": ["capability:python-package"],
        "primary_public_channel": "uibcdf",
        "third_party_channel": "conda-forge",
        "pypi_route": "optional-verified",
        "review_field": "python_distribution_review",
        "normative": "devguide/policies/python_distribution_policy.md",
    }
    for key, value in expected.items():
        if policy.get(key) != value:
            errors.append(f"moli.toml: Python distribution policy has invalid {key}")
    for name, component in components.items():
        if "python-package" not in component.get("capabilities", []):
            continue
        if component.get("internal_governance") == "delegated":
            continue
        review = component.get("python_distribution_review")
        if not isinstance(review, dict):
            errors.append(f"moli.toml: component {name} needs a Python distribution review")
            continue
        repository = component.get("repository", "")
        issue = review.get("issue", "")
        if not isinstance(issue, str) or not ISSUE.fullmatch(issue) or not issue.startswith(
            f"{repository}#"
        ):
            errors.append(f"moli.toml: component {name} has an invalid distribution review issue")
        if review.get("state") not in PYTHON_ECOSYSTEM_STATES:
            errors.append(f"moli.toml: component {name} has an invalid distribution review state")
    return errors


def validate_registry(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "moli.toml"
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        return [f"moli.toml: {error}"]
    if data.get("schema_version") != "0.3":
        errors.append("moli.toml: unsupported schema_version")
    governance = data.get("governance", {})
    if governance.get("policy_inheritance") != "transitive-by-capability":
        errors.append("moli.toml: policy inheritance must be transitive by capability")
    census = governance.get("infrastructure_census")
    if not isinstance(census, str) or not (root / census).is_file():
        errors.append("moli.toml: infrastructure census is missing")
    inheritance_contract = governance.get("policy_inheritance_contract")
    if not isinstance(inheritance_contract, str) or not (root / inheritance_contract).is_file():
        errors.append("moli.toml: policy inheritance contract is missing")
    required = {"sabueso", "praxis", "nextia", "molsyssuite", "moli-agent"}
    registered = data.get("components", {})
    components = set(registered)
    missing = sorted(required - components)
    if missing:
        errors.append("moli.toml: missing components: " + ", ".join(missing))
    for name, component in registered.items():
        delivery = component.get("guide_delivery")
        if delivery not in {"vendored", "reference"}:
            errors.append(f"moli.toml: component {name} has invalid guide delivery")
        if delivery == "reference" and component.get("internal_governance") != "delegated":
            errors.append(f"moli.toml: component {name} needs delegated governance to reference the guide")
        if component.get("internal_governance") == "delegated" and not component.get("internal_governance_repository"):
            errors.append(f"moli.toml: component {name} has no internal governance repository")
    policies = data.get("policies", {})
    errors.extend(validate_python_ecosystem_reviews(registered, policies))
    errors.extend(validate_python_distribution_reviews(registered, policies))
    for name in (
        "reporting_lifecycle",
        "cross_component_feedback",
        "component_guide",
        "python",
        "python_ci",
        "python_quality",
        "release_version",
        "repository_badges",
        "zenodo_archival",
    ):
        if policies.get(name, {}).get("status") != "accepted":
            errors.append(f"moli.toml: policy {name} is not accepted")
    for name, policy in policies.items():
        normative = policy.get("normative")
        if normative is not None and (not isinstance(normative, str) or not (root / normative).is_file()):
            errors.append(f"moli.toml: policy {name} has no existing normative document")
    guide = policies.get("component_guide", {})
    if guide.get("applies_to") != ["guide-delivery:vendored"]:
        errors.append("moli.toml: component guide must select vendored delivery")
    if not (root / str(guide.get("filename", ""))).is_file():
        errors.append("moli.toml: canonical component guide is missing")
    if guide.get("validator") != "devtools/scripts/check_component_guides.py":
        errors.append("moli.toml: component guide validator is not registered")
    elif not (root / guide["validator"]).is_file():
        errors.append("moli.toml: component guide validator is missing")
    python = policies.get("python", {})
    python_ci = policies.get("python_ci", {})
    if python_ci.get("routine_python") not in python.get("ci_versions", []):
        errors.append("moli.toml: routine Python must be in supported CI versions")
    if python_ci.get("routine_events") != ["push", "pull_request"]:
        errors.append("moli.toml: routine CI must cover pushes and pull requests")
    if python_ci.get("routine_os") != "linux" or "linux" not in python_ci.get("full_matrix_os", []):
        errors.append("moli.toml: Python CI must include Linux")
    if policies.get("python_quality", {}).get("target_version") != "py311":
        errors.append("moli.toml: Ruff must target the oldest supported Python")
    release = policies.get("release_version", {})
    pattern = release.get("pattern")
    if not isinstance(pattern, str):
        errors.append("moli.toml: release-version pattern is missing")
    else:
        try:
            if re.fullmatch(pattern, "1.2.3") is None or re.fullmatch(pattern, "01.2.3") is not None:
                errors.append("moli.toml: release-version pattern is not canonical X.Y.Z")
        except re.error:
            errors.append("moli.toml: release-version pattern is invalid")
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
