"""Demonstrative acceptance contract for teaching positive/negative tests.

This is intentionally a small domain-free validator. Projects must define their
own business contracts. In-repo contrasts with a local always-True callable are
**illustrative only** and are not a mutation-testing framework (see F-06).
"""

from __future__ import annotations


class ValidationError(ValueError):
    """Raised when demo validation rejects an input."""


def validate_non_negative_amount(amount: int) -> bool:
    """Validate that ``amount`` is a non-negative integer amount.

    Args:
        amount: Candidate amount. Must be an ``int`` and ``>= 0``.

    Returns:
        ``True`` when the amount is acceptable.

    Raises:
        ValidationError: If ``amount`` is not an ``int`` or is negative.
    """
    if not isinstance(amount, int) or isinstance(amount, bool):
        msg = "amount 必須為 int（不可為 bool）"
        raise ValidationError(msg)
    if amount < 0:
        msg = "amount 不可為負數"
        raise ValidationError(msg)
    return True
