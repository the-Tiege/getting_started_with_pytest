"""
Basic Math Operations Module

This module contains simple functions for performing basic mathematical operations,
including addition and division. The functions are designed to work with floating-point
numbers and include appropriate type annotations.

Functions:
- add(number_1: float, number_2: float) -> float: Adds two floating-point numbers.
- divide(number_1: float, number_2: float) -> float: Divides the first number by the second,
  raising a ValueError if the denominator is zero.

Example Usage:
result = add(3.5, 2.0)
print(result) # Output: 5.5

result = divide(8.0, 4.0)
print(result) # Output: 2.0
Note: This module is intended for educational purposes and may not cover all edge cases.
"""

def add(number_1: float, number_2: float) -> float:
    """
    Add two numbers and returns the result

    Parameters:
    - number_1: float 
                The first number.
    - number_2: float
                The second number.

    Returns:
    float: The sum of number_1 and number_2.
    """
    return number_1 + number_2


def divide(number_1: float, number_2: float) -> float:
    """
    Divides the first number by the second number and returns the result.

    Parameters:
    - number_1: float
                The first number.
    - number_2: float
                The second number.

    Returns:
    float: number_1 divided by number_2

    Raises:
    ValueError: If number_2 is 0, raises a ValueError.

    """
    if number_2 == 0:
        raise ValueError
    return number_1 / number_2
