"""Archive preservation must not become package-publication evidence."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from devtools.scripts.check_archive_tags import (
    COMMAND,
    check,
    is_archive_tag,
    preservation_reasons,
    public_version_reasons,
    read_workflow,
    workflow_reasons,
)
from devtools.scripts.validate_governance import validate_registry

ROOT = Path(__file__).resolve().parents[1]


class ArchiveTagPolicyTests(unittest.TestCase):
    def workflow(self):
        return {
            "on": {"push": {"branches": ["main"], "tags": ["**"]}},
            "jobs": {"governance": {"steps": [{"run": COMMAND}]}},
        }

    def reasons(self, document):
        return workflow_reasons(document, "governance", command=COMMAND)

    def git(self, root, *args):
        return subprocess.check_output(
            ["git", "-C", str(root), *args], text=True, stderr=subprocess.PIPE
        ).strip()

    def repository(self, root):
        self.git(root, "init", "--initial-branch=main")
        (root / "content").write_text("historical fixture\n")
        workflow = root / ".github/workflows/validate_governance.yml"
        workflow.parent.mkdir(parents=True)
        # JSON is valid YAML and preserves the exact native event/step shapes.
        workflow.write_text(json.dumps(self.workflow()))
        script = root / "devtools/scripts/check_archive_tags.py"
        script.parent.mkdir(parents=True)
        script.write_bytes(
            (ROOT / "devtools/scripts/check_archive_tags.py").read_bytes()
        )
        self.git(root, "add", ".")
        self.git(
            root,
            "-c",
            "user.name=Archive fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-m",
            "Preserved experiment",
        )

    def annotated_tag(
        self, root, message="Owner: fixture\nPurpose: preserve experiment"
    ):
        self.git(
            root,
            "-c",
            "user.name=Archive fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "tag",
            "-a",
            "archive/experiment/nested",
            "-m",
            message,
        )

    def test_git_namespace_and_public_version_remain_separate(self):
        for name in (
            "archive/experiment",
            "archive/experiment/nested",
            "archive/1.2.3",
        ):
            with self.subTest(name=name):
                self.assertTrue(is_archive_tag(name))
                self.assertTrue(public_version_reasons(name))
        for name in (
            "archive/",
            "archive",
            "archive/has space",
            "archive/x..y",
            "v1.2.3",
            "other/x",
        ):
            with self.subTest(name=name):
                self.assertFalse(is_archive_tag(name))
                self.assertTrue(public_version_reasons(name))
        for name in ("0.0.0", "1.2.3", "100.20.0"):
            self.assertEqual(public_version_reasons(name), [])
        for name in ("01.2.3", "1.2.3rc1", "1.2.3+local", "1.2.3\n"):
            self.assertTrue(public_version_reasons(name))

    def test_all_tag_configuration_and_inert_path_filters(self):
        self.assertEqual(self.reasons(self.workflow()), [])
        for events in ("push", ["push", "pull_request"], {"push": None}, {"push": {}}):
            document = self.workflow()
            document["on"] = events
            self.assertEqual(self.reasons(document), [])
        document = self.workflow()
        document["on"]["push"]["paths"] = ["src/**"]
        self.assertEqual(self.reasons(document), [])  # GitHub ignores this for tags.

    def test_branch_only_wildcard_and_exclusion_filters_fail(self):
        for push in (
            {"branches": ["main"]},
            {"branches-ignore": ["retired"]},
            {"tags": ["*"]},
            {"tags": ["**", "!archive/**"]},
            {"tags": ["**"], "tags-ignore": ["archive/**"]},
            {"tags": "**"},
            {"tags": ["archive/**"]},
        ):
            document = self.workflow()
            document["on"]["push"] = push
            with self.subTest(push=push):
                self.assertTrue(self.reasons(document))
        self.assertTrue(self.reasons({"on": {"pull_request": None}}))

    def test_conditional_or_tolerated_gates_cannot_claim_capability(self):
        for field, value in (
            ("if", "always()"),
            ("needs", ["optional"]),
            ("continue-on-error", "true"),
        ):
            document = self.workflow()
            document["jobs"]["governance"][field] = value
            self.assertTrue(self.reasons(document))
        for field, value in (
            ("if", "startsWith(github.ref, 'refs/heads/')"),
            ("continue-on-error", "true"),
        ):
            document = self.workflow()
            document["jobs"]["governance"]["steps"][0][field] = value
            self.assertTrue(self.reasons(document))
        for command in ("# " + COMMAND, COMMAND + " || true", "echo '" + COMMAND + "'"):
            document = self.workflow()
            document["jobs"]["governance"]["steps"][0]["run"] = command
            self.assertTrue(self.reasons(document))

    def test_reusable_gate_requires_the_reviewed_immutable_capable_caller(self):
        caller = "uibcdf/example/.github/workflows/policy.yml@" + "a" * 40
        document = self.workflow()
        document["jobs"]["governance"] = {"uses": caller}
        self.assertEqual(workflow_reasons(document, "governance", caller=caller), [])
        for observed in (
            caller.replace("a" * 40, "main"),
            caller.replace("a" * 40, "b" * 40),
        ):
            document["jobs"]["governance"]["uses"] = observed
            self.assertTrue(workflow_reasons(document, "governance", caller=caller))
        self.assertTrue(
            workflow_reasons(
                document, "governance", caller=observed.replace("b" * 40, "main")
            )
        )
        with self.assertRaises(ValueError):
            workflow_reasons(document, "governance")

    def test_yaml_event_key_is_not_boolean_and_duplicates_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "workflow.yml"
            path.write_text("on:\n  push:\n    tags: ['**']\njobs: {}\n")
            self.assertIn("on", read_workflow(path))
            for source in (
                "on: push\non: pull_request\n",
                "on: push\njobs:\n  gate: {}\n  gate: {}\n",
                "on: [",
            ):
                path.write_text(source)
                with self.assertRaises(ValueError):
                    read_workflow(path)

    def test_real_annotated_tag_survives_read_only_conformance(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.repository(root)
            self.annotated_tag(root)
            before = self.git(root, "show-ref", "--tags")
            commit = self.git(root, "rev-parse", "archive/experiment/nested^{commit}")
            self.assertEqual(check(root), [])
            self.assertEqual(self.git(root, "show-ref", "--tags"), before)
            self.assertEqual(self.git(root, "rev-parse", "HEAD"), commit)
            (root / "pyproject.toml").write_text(
                '[project]\nversion = "archive/experiment/nested"\n'
            )
            self.assertTrue(any("package version" in reason for reason in check(root)))
            self.assertEqual(self.git(root, "show-ref", "--tags"), before)

    def test_lightweight_or_historical_annotation_can_use_pinned_issue_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.repository(root)
            self.git(root, "tag", "archive/experiment")
            self.assertTrue(preservation_reasons(root))
            commit = self.git(root, "rev-parse", "HEAD")
            record = root / "devguide/archive_tags.toml"
            record.parent.mkdir()
            content = (
                '[tags."archive/experiment"]\nowner = "fixture"\npurpose = "history"\n'
                f'issue = "uibcdf/moli#47"\ncommit = "{commit}"\ntag_object = "{commit}"\n'
            )
            record.write_text(content)
            self.assertEqual(preservation_reasons(root), [])
            record.write_text(
                content.replace(
                    f'tag_object = "{commit}"', 'tag_object = "' + "f" * 40 + '"'
                )
            )
            self.assertTrue(preservation_reasons(root))

    def test_missing_owner_or_noncommit_target_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.repository(root)
            self.annotated_tag(root, "Owner:\nPurpose: fixture")
            self.assertTrue(preservation_reasons(root))
            blob = self.git(root, "hash-object", "-w", "content")
            self.git(root, "tag", "archive/not-a-commit", blob)
            self.assertTrue(
                any(
                    "preserve a commit" in reason
                    for reason in preservation_reasons(root)
                )
            )

    def test_updating_main_cannot_retrofit_an_old_targets_gate(self):
        for absent_script in (False, True):
            with (
                self.subTest(absent_script=absent_script),
                tempfile.TemporaryDirectory() as temporary,
            ):
                root = Path(temporary)
                self.repository(root)
                workflow = root / ".github/workflows/validate_governance.yml"
                script = root / "devtools/scripts/check_archive_tags.py"
                if absent_script:
                    script.unlink()
                else:
                    old = self.workflow()
                    old["on"]["push"]["tags"] = ["*"]
                    workflow.write_text(json.dumps(old))
                self.git(root, "add", ".")
                self.git(
                    root,
                    "-c",
                    "user.name=Fixture",
                    "-c",
                    "user.email=fixture@example.invalid",
                    "commit",
                    "-m",
                    "Old gate",
                )
                self.annotated_tag(root)
                before = self.git(root, "show-ref", "--tags")
                workflow.write_text(json.dumps(self.workflow()))
                script.write_bytes(
                    (ROOT / "devtools/scripts/check_archive_tags.py").read_bytes()
                )
                self.assertTrue(
                    any("target workflow" in reason for reason in check(root))
                )
                self.assertEqual(self.git(root, "show-ref", "--tags"), before)

    def test_moli_gate_configuration_is_checked_by_the_real_reader(self):
        self.assertEqual(
            workflow_reasons(
                read_workflow(ROOT / ".github/workflows/validate_governance.yml"),
                "governance",
                command=COMMAND,
            ),
            [],
        )

    def test_cli_rejects_archive_candidate_before_reading_a_repository(self):
        for version, expected in (("archive/experiment", 1), ("1.2.3", 0)):
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "devtools/scripts/check_archive_tags.py"),
                    "/nonexistent/archive-policy-fixture",
                    "--release-version",
                    version,
                ],
                capture_output=True,
                check=False,
                text=True,
            )
            self.assertEqual(result.returncode, expected, result.stderr)

    def test_registry_cannot_silently_drop_archive_policy_boundary(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("devguide", "devtools", "MOLI_GUIDE.md"):
                (root / name).symlink_to(ROOT / name)
            source = (ROOT / "moli.toml").read_text()
            (root / "moli.toml").write_text(
                source.replace('namespace = "archive/"', 'namespace = "experimental/"')
            )
            self.assertTrue(
                any("archive" in reason for reason in validate_registry(root))
            )


if __name__ == "__main__":
    unittest.main()
