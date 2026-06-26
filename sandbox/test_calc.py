"""Tests for the calculator. Run them with:  pytest

Each test reads like a sentence: "calculate this, expect that."
"""

import pytest

from calc import calculate


def test_addition():
    assert calculate("1 + 2") == 3


def test_multiply_before_add():
    # multiplication happens before addition
    assert calculate("1 + 2 * 3") == 7


def test_subtraction_and_division():
    assert calculate("10 / 2 - 1") == 4


def test_decimals():
    assert calculate("1.5 + 2.5") == 4


def test_division_gives_decimal():
    assert calculate("7 / 2") == 3.5


def test_divide_by_zero_is_a_clear_error():
    with pytest.raises(ZeroDivisionError):
        calculate("1 / 0")
