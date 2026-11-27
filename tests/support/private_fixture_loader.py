"""Private fixture loader pattern: missing file is unavailable, not PASS."""

from __future__ import annotations

from pathlib import Path


class PrivateFixtureUnavailableError(FileNotFoundError):
    """Raised when a private fixture path does not exist."""


def load_private_text(path: Path) -> str:
    """Load a private fixture file as text.

    Args:
        path: Absolute or relative path to the fixture.

    Returns:
        File contents decoded as UTF-8.

    Raises:
        PrivateFixtureUnavailableError: If the file is missing (skip≠PASS).
        OSError: If the file exists but cannot be read.
    """
    if not path.is_file():
        msg = f"PRIVATE_FIXTURE_UNAVAILABLE: {path}"
        raise PrivateFixtureUnavailableError(msg)
    return path.read_text(encoding="utf-8")
