"""
Test Module for Square Class in the Shapes Module

This module contains test cases for the 'Square' class in the 'shapes' module.
The tests use pytest and parametrize decorator to cover multiple cases for calculating the area and perimeter of a square.

Test Functions:
- test_multiple_square_areas(side_length, expected_area): Test case for the 'area' method of the 'Square' class.
- test_multiple_square_perimeters(side_length, expected_perimeter): Test case for the 'perimeter' method of the 'Square' class.

Example Usage:

Run the tests using pytest:
$ pytest test_square.py

Note: This module assumes the availability of the 'shapes' module and uses pytest for testing.
"""
import pytest

from getting_started_pytest import shapes

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
    """
    Test case for the 'area' method of the 'Square' class.

    Parameters:
    - side_length: int
                  The length of each side of the square.
    - expected_area: int
                     The expected area of the square.
    """
    square = shapes.Square(side_length)
    result_area = square.area()

    assert result_area == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", SQUARE_PERIMETERS)
def test_multiple_square_perimtters(side_length, expected_perimeter):
    """
    Test case for the 'perimeter' method of the 'Square' class.

    Parameters:
    - side_length: int
                  The length of each side of the square.
    - expected_perimeter: int
                         The expected perimeter of the square.
    """
    square = shapes.Square(side_length)
    result_perimeter = square.perimeter()

    assert result_perimeter == expected_perimeter