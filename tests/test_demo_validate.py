"""Positive/negative/boundary tests for the demo acceptance contract."""

from __future__ import annotations

import pytest

from app.demo_validate import ValidationError, validate_non_negative_amount


def test_validate_accepts_zero_and_positive() -> None:
    assert validate_non_negative_amount(0) is True
    assert validate_non_negative_amount(100) is True


def test_validate_rejects_negative() -> None:
    with pytest.raises(ValidationError, match="不可為負數"):
        validate_non_negative_amount(-1)


def test_validate_rejects_bool_and_non_int() -> None:
    with pytest.raises(ValidationError, match="必須為 int"):
        validate_non_negative_amount(True)  # type: ignore[arg-type]
    with pytest.raises(ValidationError, match="必須為 int"):
        validate_non_negative_amount(1.5)  # type: ignore[arg-type]


def test_illustrative_fixed_true_is_not_a_mutation_framework() -> None:
    """Illustrative contrast only — NOT production mutation testing.

    Shows that a local always-True callable would accept invalid inputs, while
    the real ``validate_non_negative_amount`` rejects them. This does **not**
    mutate installed production code and is **not** a mutation-testing framework
    (see Phase 3 F-06 / ENGINEERING_BACKLOG ENG-006).
    """

    def always_true(_amount: int) -> bool:
        return True

    with pytest.raises(ValidationError):
        validate_non_negative_amount(-5)
    with pytest.raises(ValidationError):
        validate_non_negative_amount(False)  # type: ignore[arg-type]

    assert always_true(-5) is True
    assert always_true(False) is True  # type: ignore[arg-type]
