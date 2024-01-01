"""
Test Module for Shapes - Circle

This module contains test cases for the 'Circle' class in the 'shapes' module.
Test cases include verifying the calculation of the area and perimeter of a circle.

Test Class:
- TestCircle: Test cases for the 'Circle' class.

Example Usage:

Run the tests using pytest:
$ pytest test_shapes.py

Note: This module assumes the availability of the 'shapes' module and uses pytest for testing.
"""

import math

from getting_started_pytest import shapes


class TestCircle:
    """
    Test cases for the 'Circle' class in the 'shapes' module.

    Test Methods:
    - setup_method(method): Set up method executed before each test method.
    - teardown_method(method): Teardown method executed after each test method.
    - test_area(): Test case for verifying the calculation of the area of a circle.
    - test_perimeter(): Test case for verifying the calculation of the perimeter of a circle.
    """

    def setup_method(self, method):
        """
        Set up method executed before each test method.

        Parameters:
        - method: str
                  The name of the test method being set up.
        """
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """
        Teardown method executed after each test method.

        Parameters:
        - method: str
                  The name of the test method being torn down.
        """
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        """
        Test case for verifying the calculation of the area of a circle.
        """
        result = self.circle.area()
        expected_result = math.pi * self.circle.radius ** 2
        assert result == expected_result

    def test_perimeter(self):
        """
        Test case for verifying the calculation of the perimeter of a circle.
        """
        result = self.circle.perimeter()
        expected_result = 2 * math.pi * self.circle.radius
        assert result == expected_result
