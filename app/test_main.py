import pytest
from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_fifteen_and_twenty_four() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_advances_faster_than_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
