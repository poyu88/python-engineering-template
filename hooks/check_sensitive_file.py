"""Cursor beforeReadFile hook: block reads of sensitive paths (auxiliary only).

Fail-open on unexpected errors is intentional for Cursor UX, but that outcome
must never be interpreted as a security PASS. See docs/AGENT_INTEGRITY.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import PurePath, PurePosixPath, PureWindowsPath
from typing import Any

SENSITIVE_FILE_NAMES: frozenset[str] = frozenset(
    {
        ".env",
        ".env.local",
        ".env.production",
        ".env.development",
        "config.json",
        "secrets.json",
        "credentials.json",
        "api_keys.json",
        "private_key.pem",
        "id_rsa",
        "id_rsa.pub",
        "password.txt",
        "passwords.txt",
        "secret.txt",
        "secrets.txt",
        "database.yml",
        "db_config.json",
        "private.key",
        "secret.key",
        "token.txt",
        "credentials",
        "config",
    }
)

SENSITIVE_DIR_NAMES: frozenset[str] = frozenset(
    {
        ".ssh",
        ".aws",
        ".gnupg",
        "secrets",
        "private_keys",
    }
)


def normalize_path_text(file_path: str) -> str:
    """Normalize separators and strip surrounding quotes/whitespace.

    Args:
        file_path: Raw path from hook JSON.

    Returns:
        Normalized path text using forward slashes where possible.
    """
    text = file_path.strip().strip('"').strip("'")
    return text.replace("\\", "/")


def path_parts(file_path: str) -> tuple[str, ...]:
    """Split a path into comparable parts for Windows and POSIX inputs.

    Args:
        file_path: Absolute or relative path string.

    Returns:
        Tuple of non-empty path parts (drive letters kept as parts).

    Raises:
        ValueError: If ``file_path`` is empty after normalization.
    """
    normalized = normalize_path_text(file_path)
    if not normalized:
        msg = "file_path 不可為空"
        raise ValueError(msg)

    pure: PurePath
    windows_like = (len(normalized) >= 2 and normalized[1] == ":") or normalized.startswith(
        ("//", "\\\\")
    )
    if windows_like:
        pure = PureWindowsPath(normalized.replace("/", "\\"))
    else:
        pure = PurePosixPath(normalized)

    parts = tuple(part for part in pure.parts if part not in {"/", "\\"})
    if not parts:
        msg = f"無法解析路徑: {file_path!r}"
        raise ValueError(msg)
    return parts


def is_sensitive_path(file_path: str) -> bool:
    """Return whether a path refers to a sensitive file or directory entry.

    Matching uses normalized parts (not basename-only), covering nested
    directories such as ``.aws/credentials`` and ``.ssh/id_rsa``.

    Args:
        file_path: Absolute or relative path.

    Returns:
        ``True`` if the path should be denied for auxiliary hook purposes.
    """
    parts = path_parts(file_path)
    lowered = tuple(part.lower() for part in parts)
    sensitive_names = {name.lower() for name in SENSITIVE_FILE_NAMES}
    sensitive_dirs = {name.lower() for name in SENSITIVE_DIR_NAMES}

    if lowered[-1] in sensitive_names:
        return True

    return any(part in sensitive_dirs for part in lowered)


def evaluate_file_hook(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate hook payload and return Cursor permission JSON fields.

    Args:
        payload: Decoded stdin JSON object.

    Returns:
        Dict containing ``permission`` and optional ``user_message`` /
        ``detection_status``.
    """
    file_path = payload.get("file_path", "")
    if not isinstance(file_path, str) or not file_path.strip():
        return {
            "permission": "allow",
            "detection_status": "NOT_APPLICABLE",
            "user_message": "缺少 file_path；輔助 hook 不阻擋",
        }

    try:
        sensitive = is_sensitive_path(file_path)
    except ValueError as exc:
        return {
            "permission": "allow",
            "detection_status": "BLOCKED",
            "user_message": (
                f"路徑無法解析（{exc}）。輔助 hook fail-open；"
                "此結果不是安全 PASS，正式驗收不得依賴本 hook。"
            ),
        }

    if sensitive:
        return {
            "permission": "deny",
            "detection_status": "PASS",
            "user_message": (
                f"無法讀取敏感路徑：{normalize_path_text(file_path)}。"
                "此為輔助防護，非正式安全邊界的唯一機制。"
            ),
        }

    return {
        "permission": "allow",
        "detection_status": "PASS",
    }


def main() -> None:
    """Read JSON from stdin, evaluate sensitivity, write JSON to stdout."""
    try:
        raw = sys.stdin.buffer.read().decode("utf-8")
        try:
            data: dict[str, Any] = json.loads(raw)
        except json.JSONDecodeError as exc:
            result = {
                "permission": "allow",
                "detection_status": "BLOCKED",
                "user_message": (
                    f"JSON 解析錯誤: {exc}。輔助 hook fail-open；不得將此結果視為安全通過。"
                ),
            }
            _emit(result)
            return

        if not isinstance(data, dict):
            result = {
                "permission": "allow",
                "detection_status": "BLOCKED",
                "user_message": "輸入必須為 JSON object；fail-open，非正式安全 PASS。",
            }
            _emit(result)
            return

        _emit(evaluate_file_hook(data))
    except Exception as exc:
        # Documented fail-open for Cursor UX; detection_status=BLOCKED ≠ security PASS.
        result = {
            "permission": "allow",
            "detection_status": "BLOCKED",
            "user_message": (
                f"檢查過程發生錯誤: {exc}。輔助 hook fail-open；不得將此結果視為安全通過。"
            ),
        }
        _emit(result)


def _emit(result: dict[str, Any]) -> None:
    """Write UTF-8 JSON to stdout."""
    output = json.dumps(result, ensure_ascii=False)
    sys.stdout.buffer.write(output.encode("utf-8"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
