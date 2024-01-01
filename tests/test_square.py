import pytest

import getting_started_pytest.shapes as shapes


SQUARE_AREAS = [
    (2, 4),
    (4, 16),
    (5, 25),
    (9, 81)
]

SQUARE_PERIMETERS = [
    (2, 8),
    (1, 4),
    (3, 12),
    (10, 40)
]


@pytest.mark.parametrize("side_length, expected_area", SQUARE_AREAS)
def test_multiple_square_areas(side_length, expected_area):
    square = shapes.Square(side_length)
    result_area = square.area()

    assert result_area == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", SQUARE_PERIMETERS)
def test_multiple_square_perimtters(side_length, expected_perimeter):
    square = shapes.Square(side_length)
    result_perimeter = square.perimeter()

    assert result_perimeter == expected_perimeter