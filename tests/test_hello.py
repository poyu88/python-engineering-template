"""Tests for the demonstrative hello module."""

from __future__ import annotations

import pytest

from app.hello import greet


def test_greet_returns_chinese_greeting() -> None:
    assert greet("Ada") == "你好，Ada"


def test_greet_strips_whitespace() -> None:
    assert greet("  Bob  ") == "你好，Bob"


def test_greet_rejects_empty() -> None:
    with pytest.raises(ValueError, match="名稱不可為空"):
        greet("   ")
