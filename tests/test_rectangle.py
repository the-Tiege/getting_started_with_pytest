"""
Test Module for Rectangle Class

This module contains test cases for the 'Rectangle' class in the 'shapes' module.
The tests cover the calculation of area, perimeter, and equality comparison of 'Rectangle' instances.

Test Functions:
- test_area(rectangle): Test case for verifying the calculation of the area of a 'Rectangle'.
- test_perimeter(rectangle): Test case for verifying the calculation of the perimeter of a 'Rectangle'.
- test_equality(rectangle, other_rectangle): Test case for comparing the equality of two 'Rectangle' instances.

Example Usage:

Run the tests using pytest:
$ pytest test_rectangle.py

Note: This module assumes the availability of the 'shapes' module and uses pytest for testing.
"""
from getting_started_pytest import shapes


def test_area(rectangle: shapes.Rectangle):
    """
    Test case for verifying the calculation of the area of a 'Rectangle'.

    Parameters:
    - rectangle: shapes.Rectangle
                 A 'Rectangle' instance for testing purposes.
    """

    result = rectangle.area()
    expected_result = 10 * 20

    assert result == expected_result


def test_perimeter(rectangle: shapes.Rectangle):
    """
    Test case for verifying the calculation of the perimeter of a 'Rectangle'.

    Parameters:
    - rectangle: shapes.Rectangle
                 A 'Rectangle' instance for testing purposes.
    """

    result = rectangle.perimeter()
    expected_result = (10 * 2) + (20 * 2)

    assert result == expected_result == expected_result


def test_equality(rectangle: shapes.Rectangle, other_rectangle: shapes.Rectangle):
    """
    Test case for comparing the equality of two 'Rectangle' instances.

    Parameters:
    - rectangle: shapes.Rectangle
                 A 'Rectangle' instance for testing purposes.
    - other_rectangle: shapes.Rectangle
                       Another 'Rectangle' instance for testing purposes.
    """
    assert rectangle != other_rectangle
