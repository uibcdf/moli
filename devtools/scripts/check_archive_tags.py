"""Read-only checks for the opt-in archive-tag capability (MOLI #47).

This is MOLI's executable gate and a reference for owner-local integrations.
It does not qualify a publisher or grant permission to publish. YAML inspection
requires PyYAML; the ordinary component governance checker remains independent.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tomllib
from pathlib import Path

PUBLIC_VERSION = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")
ISSUE = re.compile(r"uibcdf/[A-Za-z0-9_.-]+#[1-9][0-9]*\Z")
CALLER = re.compile(
    r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/\.github/workflows/"
    r"[A-Za-z0-9_.-]+\.ya?ml@[0-9a-f]{40}\Z"
)
COMMAND = "python devtools/scripts/check_archive_tags.py ."


def public_version_reasons(version: str) -> list[str]:
    """Reject archive names before a caller acquires publication authority."""
    return (
        []
        if PUBLIC_VERSION.fullmatch(version)
        else ["public version must be canonical X.Y.Z"]
    )


def is_archive_tag(name: str) -> bool:
    """Use Git's own ref grammar, with a nonempty reserved suffix."""
    if not name.startswith("archive/") or not name.removeprefix("archive/"):
        return False
    return (
        subprocess.run(
            ["git", "check-ref-format", f"refs/tags/{name}"],
            capture_output=True,
            check=False,
        ).returncode
        == 0
    )


def read_workflow(path: Path) -> dict:
    """Keep event names as strings and refuse ambiguous duplicate YAML keys."""
    import yaml

    class WorkflowLoader(yaml.BaseLoader):
        pass

    def mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            if not isinstance(key, str) or key in result:
                raise ValueError("workflow has a non-string or duplicate mapping key")
            result[key] = loader.construct_object(value_node)
        return result

    WorkflowLoader.add_constructor("tag:yaml.org,2002:map", mapping)
    try:
        result = yaml.load(path.read_text(encoding="utf-8"), Loader=WorkflowLoader)
    except yaml.YAMLError as error:
        raise ValueError("workflow YAML is invalid") from error
    if not isinstance(result, dict):
        raise ValueError("workflow must be a mapping")
    return result


def workflow_reasons(
    document: dict,
    job_id: str,
    *,
    command: str | None = None,
    caller: str | None = None,
) -> list[str]:
    """Check a deliberately narrow, unconditional all-tag gate configuration.

    A reusable caller must equal the owner's reviewed immutable capable revision.
    Configuration checks do not prove that its implementation or publisher works.
    """
    if (command is None) == (caller is None):
        raise ValueError("name exactly one reviewed command or reusable caller")
    errors = []
    events = document.get("on")
    if isinstance(events, str):
        push = {} if events == "push" else None
    elif isinstance(events, list):
        push = {} if "push" in events else None
    elif isinstance(events, dict) and "push" in events:
        push = events["push"]
        if push is None or push == "":
            push = {}
    else:
        push = None
    if not isinstance(push, dict):
        errors.append("archive gate must run on tag pushes")
    elif (
        "tags-ignore" in push
        or ("tags" in push and push["tags"] != ["**"])
        or (
            "tags" not in push
            and any(key in push for key in ("branches", "branches-ignore"))
        )
    ):
        errors.append(
            'archive gate needs all-tag coverage; use tags: ["**"] without exclusions'
        )
    # GitHub does not evaluate paths/paths-ignore for tag pushes.
    jobs = document.get("jobs", {})
    job = jobs.get(job_id) if isinstance(jobs, dict) else None
    if not isinstance(job, dict):
        return errors + ["archive gate job is missing"]
    if (
        "if" in job
        or "needs" in job
        or job.get("continue-on-error", "false") not in (False, "false")
    ):
        errors.append("archive gate job must be unconditional and failure-gating")
    if caller is not None:
        if not CALLER.fullmatch(caller) or job.get("uses") != caller:
            errors.append(
                "archive caller must match the reviewed capable full-commit revision"
            )
    else:
        steps = job.get("steps", [])
        matching = (
            [
                step
                for step in steps
                if isinstance(step, dict)
                and isinstance(step.get("run"), str)
                and step["run"].strip() == command
            ]
            if isinstance(steps, list)
            else []
        )
        if not any(
            "if" not in step
            and step.get("continue-on-error", "false") in (False, "false")
            for step in matching
        ):
            errors.append(
                "reviewed archive command needs an unconditional failure-gating step"
            )
    return errors


def _git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def preservation_reasons(root: Path) -> list[str]:
    """Inspect archive refs without writing them; retain owner metadata and pins."""
    manifest = root / "devguide/archive_tags.toml"
    records = (
        tomllib.loads(manifest.read_text(encoding="utf-8")).get("tags", {})
        if manifest.is_file()
        else {}
    )
    if not isinstance(records, dict):
        return ["archive tag records must be a mapping"]
    errors = []
    for name in _git(root, "tag", "--list", "archive/*").splitlines():
        ref = f"refs/tags/{name}"
        if not is_archive_tag(name):
            errors.append(f"{name}: invalid reserved tag name")
            continue
        try:
            commit = _git(root, "rev-parse", "--verify", f"{ref}^{{commit}}")
        except subprocess.CalledProcessError:
            errors.append(f"{name}: archive tag must preserve a commit")
            continue
        record = records.get(name)
        if record is not None:
            if not isinstance(record, dict) or not all(
                isinstance(record.get(key), str) and record[key].strip()
                for key in ("owner", "purpose", "issue", "commit", "tag_object")
            ):
                errors.append(f"{name}: incomplete owner preservation record")
            elif (
                not ISSUE.fullmatch(record["issue"])
                or record["commit"] != commit
                or record["tag_object"] != _git(root, "rev-parse", "--verify", ref)
            ):
                errors.append(f"{name}: preservation identity or owning issue differs")
        else:
            annotation = _git(root, "for-each-ref", "--format=%(contents)", ref)
            if _git(root, "cat-file", "-t", ref) != "tag" or not all(
                re.search(rf"^{field}:[ \t]*\S[^\r\n]*$", annotation, re.MULTILINE)
                for field in ("Owner", "Purpose")
            ):
                errors.append(
                    f"{name}: needs Owner/Purpose annotation or pinned owning-issue record"
                )
    return errors


def check(root: Path) -> list[str]:
    document = read_workflow(root / ".github/workflows/validate_governance.yml")
    errors = workflow_reasons(document, "governance", command=COMMAND)
    errors.extend(preservation_reasons(root))
    project = root / "pyproject.toml"
    if project.is_file():
        version = (
            tomllib.loads(project.read_text(encoding="utf-8"))
            .get("project", {})
            .get("version", "")
        )
        if isinstance(version, str) and version.startswith("archive/"):
            errors.append("archive name cannot be a project/package version")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument(
        "--release-version",
        help="Only check canonical public-version shape; never authorizes publishing",
    )
    args = parser.parse_args()
    try:
        errors = (
            public_version_reasons(args.release_version)
            if args.release_version is not None
            else check(args.root.resolve())
        )
    except (OSError, ValueError, subprocess.CalledProcessError, ImportError) as error:
        print(f"archive check unavailable: {error}", file=sys.stderr)
        return 1
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print("Archive-tag policy checks pass; publication qualification is separate.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
