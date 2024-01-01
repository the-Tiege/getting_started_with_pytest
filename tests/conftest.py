
"""
Pytest Configuration Module for Shapes Testing

This module contains fixtures for testing the 'shapes' module.
Fixtures provide reusable setup code for tests, allowing the creation of instances
of the 'Rectangle' class for testing purposes.

Fixtures:
- rectangle: A fixture providing an instance of the 'Rectangle' class with dimensions 10x20.
- other_rectangle: A fixture providing another instance of the 'Rectangle' class with dimensions 15x40.

Example Usage:

In your test file, you can use the 'rectangle' and 'other_rectangle' fixtures like this:

def test_rectangle_area(rectangle):
assert rectangle.area() == 200

def test_rectangle_perimeter(other_rectangle):
assert other_rectangle.perimeter() == 110

Note: This module is specifically designed for testing the 'shapes' module and does not cover all possible test cases.
"""
import pytest

from getting_started_pytest import shapes


@pytest.fixture
def rectangle():
    """
    Fixture providing an instance of the 'Rectangle' class with dimensions 10x20.

    Returns:
    shapes.Rectangle: A 'Rectangle' instance for testing purposes.
    """
    return shapes.Rectangle(10, 20)


@pytest.fixture
def other_rectangle():
    """
    Fixture providing another instance of the 'Rectangle' class with dimensions 15x40.

    Returns:
    shapes.Rectangle: Another 'Rectangle' instance for testing purposes.
    """
    return shapes.Rectangle(15, 40)
