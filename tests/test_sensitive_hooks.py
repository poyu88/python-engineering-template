"""Tests for generalized sensitive path/prompt hooks."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from hooks.check_sensitive_file import (
    evaluate_file_hook,
    is_sensitive_path,
    normalize_path_text,
    path_parts,
)
from hooks.check_sensitive_prompt import check_sensitive_info, evaluate_prompt_hook

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (r"C:\Users\me\.env", True),
        ("/home/me/.env", True),
        (r"C:\project\.aws\credentials", True),
        ("/home/me/.aws/credentials", True),
        (r"C:\project\.ssh\id_rsa", True),
        ("secrets/api_keys.json", True),
        ("src/app/hello.py", False),
        ("README.md", False),
        ("docs/AGENT_INTEGRITY.md", False),
        ("./tests/fixtures/sample.txt", False),
        ("C:/project/not_secrets/readme.txt", False),
    ],
)
def test_is_sensitive_path_windows_and_posix(path: str, expected: bool) -> None:
    assert is_sensitive_path(path) is expected


def test_normalize_and_parts_handle_mixed_separators() -> None:
    assert normalize_path_text(r"C:\a\b\.env") == "C:/a/b/.env"
    parts = path_parts(r"C:\a\b\.env")
    assert parts[-1] == ".env"


def test_empty_and_invalid_paths_raise() -> None:
    with pytest.raises(ValueError):
        path_parts("   ")


def test_evaluate_file_hook_deny_and_fail_open_semantics() -> None:
    denied = evaluate_file_hook({"file_path": r"C:\tmp\.env"})
    assert denied["permission"] == "deny"
    assert denied["detection_status"] == "PASS"

    blocked = evaluate_file_hook({"file_path": ""})
    assert blocked["permission"] == "allow"
    assert blocked["detection_status"] == "NOT_APPLICABLE"
    assert "安全" not in blocked.get("user_message", "") or "PASS" not in blocked.get(
        "user_message", ""
    )


def test_fail_open_is_not_security_pass_on_bad_json(tmp_path: Path) -> None:
    script = REPO_ROOT / "hooks" / "check_sensitive_file.py"
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=b"not-json",
        capture_output=True,
        check=False,
        cwd=REPO_ROOT,
    )
    payload = json.loads(proc.stdout.decode("utf-8"))
    assert payload["permission"] == "allow"
    assert payload["detection_status"] == "BLOCKED"
    message = payload["user_message"]
    assert ("不得" in message) or ("安全通過" in message)


def test_prompt_hook_blocks_password_and_allows_clean() -> None:
    blocked = evaluate_prompt_hook({"prompt": "password: hunter2xyz"})
    assert blocked["continue"] is False
    assert blocked["detection_status"] == "PASS"

    clean = evaluate_prompt_hook({"prompt": "請說明 quality gate 如何 fail-closed"})
    assert clean["continue"] is True
    assert clean["detection_status"] == "PASS"


def test_check_sensitive_info_detects_token() -> None:
    found, _msg = check_sensitive_info("token: abcdefghijklmnopqrstuvwxyz12")
    assert found is True
