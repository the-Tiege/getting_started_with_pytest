import pytest
import math

import getting_started_pytest.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        result = self.circle.area()
        expected_result = math.pi * self.circle.radius ** 2
        assert result == expected_result

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected_result = 2 * math.pi * self.circle.radius
        assert result == expected_result
