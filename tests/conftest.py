import pytest

import getting_started_pytest.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(15, 40)
