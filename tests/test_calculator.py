"""Tests for the calculator module.

These tests are intentionally simple — the goal is to learn CI/CD, not pytest.
"""

import pytest
from app.calculator import add, subtract, multiply, divide


# ─── Addition ────────────────────────────────────────────────────────

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


# ─── Subtraction ─────────────────────────────────────────────────────

def test_subtract_positive():
    assert subtract(10, 3) == 7


def test_subtract_negative_result():
    assert subtract(3, 10) == -7


# ─── Multiplication ──────────────────────────────────────────────────

def test_multiply_positive():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(100, 0) == 0


# ─── Division ────────────────────────────────────────────────────────

def test_divide_clean():
    assert divide(10, 2) == 5.0


def test_divide_decimal_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
