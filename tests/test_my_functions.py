"""
Test Module for my_functions

This module contains test cases for the functions in the 'my_functions' module.
The test cases demonstrate various capabilities of pytest, including basic function testing,
handling exceptions, marking slow tests, skipping tests, and handling expected failures.

Test Functions:
- test_add(): Test case for the 'add' function with integer arguments.
- test_add_strings(): Test case for the 'add' function with string arguments.
- test_divide(): Test case for the 'divide' function with valid arguments.
- test_divide_by_zero(): Test case for handling the 'ValueError' when dividing by zero.
- test_slow(): Slow test case marked with '@pytest.mark.slow' to demonstrate handling of slow tests.
- test_add_binary(): Skipped test case marked with '@pytest.mark.skip' due to a broken feature.
- test_divide_by_zero_broken(): Expected failure test case marked with '@pytest.mark.xfail'
  to handle the known issue of dividing by zero.

Example Usage:

Run the tests using pytest:
$ pytest test_my_functions.py

Note: This module assumes the availability of the 'my_functions' module and uses pytest for testing.
"""

import time

import pytest

from getting_started_pytest import my_functions


def test_add():
    """
    Test case for the 'add' function with integer arguments.
    """
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    """
    Test case for the 'add' function with string arguments.
    """
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"


def test_divide():
    """
    Test case for the 'divide' function with valid arguments.
    """
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    """
    Test case for handling the 'ValueError' when dividing by zero.
    """
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_slow():
    """
    Slow test case marked with '@pytest.mark.slow' to demonstrate handling of slow tests.
    """
    time.sleep(5)
    result = my_functions.divide(10, 5)
    expected_result = 2
    assert result == expected_result


@pytest.mark.skip(reason="This feature is currently broken")
def test_add_binary():
    """
    Skipped test case marked with '@pytest.mark.skip' due to a broken feature.
    """
    assert my_functions.add(10, 10) == 11


@pytest.mark.xfail(reason="We know we cannot devide by zero")
def test_divide_by_zero_broken():
    """
    Expected failure test case marked with '@pytest.mark.xfail' 
    to handle the known issue of dividing by zero.
    """
    my_functions.divide(4, 0)
