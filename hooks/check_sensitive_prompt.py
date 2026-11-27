"""Cursor beforeSubmitPrompt hook: detect secrets in prompts (auxiliary only).

Fail-open on unexpected errors is intentional for Cursor UX and must not be
treated as a security PASS. See docs/AGENT_INTEGRITY.md.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


def detect_api_key(text: str) -> bool:
    """Return True when common API key patterns appear in ``text``."""
    patterns = [
        r'[Aa][Pp][Ii][_-]?[Kk][Ee][Yy]\s*[:=]\s*["\']?([A-Za-z0-9_\-]{20,})["\']?',
        r"[Aa][Pp][Ii][_-]?[Kk][Ee][Yy]\s+([A-Za-z0-9_\-]{20,})",
        r"sk-[A-Za-z0-9]{32,}",
        r"AIza[0-9A-Za-z_-]{35}",
        r"AKIA[0-9A-Z]{16}",
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def detect_password(text: str) -> bool:
    """Return True when password assignment patterns appear in ``text``."""
    patterns = [
        r'[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]\s*[:=]\s*["\']?([^\s"\']{6,})["\']?',
        r'[Pp][Ww][Dd]\s*[:=]\s*["\']?([^\s"\']{6,})["\']?',
        r'密碼\s*[:=]\s*["\']?([^\s"\']{6,})["\']?',
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def detect_secret_key(text: str) -> bool:
    """Return True when secret/token assignment patterns appear in ``text``."""
    patterns = [
        r'[Ss][Ee][Cc][Rr][Ee][Tt]\s*[:=]\s*["\']?([A-Za-z0-9_\-]{16,})["\']?',
        r'[Ss][Ee][Cc][Rr][Ee][Tt][_-]?[Kk][Ee][Yy]\s*[:=]\s*["\']?([A-Za-z0-9_\-]{16,})["\']?',
        r'[Tt][Oo][Kk][Ee][Nn]\s*[:=]\s*["\']?([A-Za-z0-9_\-]{20,})["\']?',
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def detect_credentials(text: str) -> bool:
    """Return True when username/password combos appear in ``text``."""
    patterns = [
        r"[Uu][Ss][Ee][Rr][Nn][Aa][Mm][Ee]\s*[:=].*[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]\s*[:=]",
        r"登入\s*[:=].*密碼\s*[:=]",
    ]
    return any(re.search(pattern, text, re.DOTALL) for pattern in patterns)


def check_sensitive_info(prompt: str) -> tuple[bool, str]:
    """Check prompt text for sensitive patterns.

    Args:
        prompt: User prompt content.

    Returns:
        Tuple of ``(has_sensitive, warning_message)``.
    """
    checks = [
        (detect_api_key, "檢測到 API Key，請勿在提示中包含敏感資訊"),
        (detect_password, "檢測到密碼資訊，請勿在提示中包含密碼"),
        (detect_secret_key, "檢測到 Secret／Token，請勿在提示中包含此類資訊"),
        (detect_credentials, "檢測到帳號密碼組合，請勿在提示中包含帳密"),
    ]
    for check_func, warning in checks:
        if check_func(prompt):
            return True, warning
    return False, ""


def evaluate_prompt_hook(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate prompt hook payload.

    Args:
        payload: Decoded stdin JSON object.

    Returns:
        Dict with ``continue``, optional message and ``detection_status``.
    """
    prompt = payload.get("prompt", "")
    if not isinstance(prompt, str) or prompt == "":
        return {
            "continue": True,
            "detection_status": "NOT_APPLICABLE",
            "user_message": "缺少 prompt；輔助 hook 不阻擋",
        }

    has_sensitive, warning = check_sensitive_info(prompt)
    if has_sensitive:
        return {
            "continue": False,
            "detection_status": "PASS",
            "user_message": f"{warning}（輔助防護，非正式安全邊界唯一機制）",
        }
    return {"continue": True, "detection_status": "PASS"}


def main() -> None:
    """Read JSON from stdin, evaluate prompt, write JSON to stdout."""
    try:
        raw = sys.stdin.buffer.read().decode("utf-8")
        try:
            data: dict[str, Any] = json.loads(raw)
        except json.JSONDecodeError as exc:
            result = {
                "continue": True,
                "detection_status": "BLOCKED",
                "user_message": (f"JSON 解析錯誤: {exc}。輔助 hook fail-open；不得視為安全通過。"),
            }
            _emit(result)
            return

        if not isinstance(data, dict):
            result = {
                "continue": True,
                "detection_status": "BLOCKED",
                "user_message": "輸入必須為 JSON object；fail-open，非正式安全 PASS。",
            }
            _emit(result)
            return

        _emit(evaluate_prompt_hook(data))
    except Exception as exc:
        # Documented fail-open for Cursor UX; detection_status=BLOCKED ≠ security PASS.
        result = {
            "continue": True,
            "detection_status": "BLOCKED",
            "user_message": (f"檢查過程發生錯誤: {exc}。輔助 hook fail-open；不得視為安全通過。"),
        }
        _emit(result)


def _emit(result: dict[str, Any]) -> None:
    """Write UTF-8 JSON to stdout."""
    output = json.dumps(result, ensure_ascii=False)
    sys.stdout.buffer.write(output.encode("utf-8"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
