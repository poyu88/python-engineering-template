"""Minimal demonstrative module for installable package smoke tests."""


def greet(name: str) -> str:
    """Return a Traditional Chinese greeting for ``name``.

    Args:
        name: Display name. Empty or whitespace-only values are rejected.

    Returns:
        Greeting string including the trimmed name.

    Raises:
        ValueError: If ``name`` is empty after stripping.
    """
    cleaned = name.strip()
    if not cleaned:
        msg = "名稱不可為空"
        raise ValueError(msg)
    return f"你好，{cleaned}"
