import pytest

import getting_started_pytest.shapes as shapes


def test_area(rectangle):

    result = rectangle.area()
    expected_result = 10 * 20

    assert result == expected_result


def test_perimeter(rectangle):

    result = rectangle.perimeter()
    expected_result = (10 * 2) + (20 * 2)

    assert result == expected_result == expected_result


def test_equality(rectangle, other_rectangle):
    assert rectangle != other_rectangle
