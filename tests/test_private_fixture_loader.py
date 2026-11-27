"""Tests for private fixture unavailable semantics."""

from __future__ import annotations

from pathlib import Path

import pytest
from tests.support.private_fixture_loader import (
    PrivateFixtureUnavailableError,
    load_private_text,
)


def test_missing_private_fixture_is_unavailable_not_pass(tmp_path: Path) -> None:
    missing = tmp_path / "absent.txt"
    with pytest.raises(PrivateFixtureUnavailableError, match="PRIVATE_FIXTURE_UNAVAILABLE"):
        load_private_text(missing)


def test_existing_private_fixture_loads(tmp_path: Path) -> None:
    path = tmp_path / "fixture.txt"
    path.write_text("ok", encoding="utf-8")
    assert load_private_text(path) == "ok"
