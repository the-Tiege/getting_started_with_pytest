"""
Geometric Shapes Module

This module defines a set of classes representing geometric shapes, including a base class Shape,
and its subclasses Circle, Rectangle, and Square. The classes are designed to calculate the area
and perimeter of the respective shapes.

Classes:
- Shape: A base class representing a generic geometric shape with methods for area and perimeter.
- Circle: A class representing a circle, inheriting from Shape, with methods to calculate area
          and perimeter.
- Rectangle: A class representing a rectangle, inheriting from Shape, with methods to calculate
             area and perimeter. It includes a custom equality comparison method (__eq__).
- Square: A class representing a square, inheriting from Rectangle, with methods inherited from
          Shape and Rectangle.

Example Usage:

circle_instance = Circle(radius=5.0)
circle_area = circle_instance.area()
circle_perimeter = circle_instance.perimeter()

rectangle_instance = Rectangle(length=4.0, width=6.0)
rectangle_area = rectangle_instance.area()
rectangle_perimeter = rectangle_instance.perimeter()

square_instance = Square(side_length=3.0)
square_area = square_instance.area()
square_perimeter = square_instance.perimeter()

Note: This module is intended for educational purposes and may not cover all edge cases.
"""


import math


class Shape:
    """
    A base class representing a generic geometric shape.

    Methods:
    - area(): Calculates and returns the area of the shape.
    - perimeter(): Calculates and returns the perimeter of the shape. 
    """

    def area(self) -> float:
        """
        Calculate the area of the shape.

        Returns: 
        float: The calculated area.
        """

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the shape.

        Returns:
        float: The calculated perimeter.
        """


class Circle(Shape):
    """
    A class representing a circle, inheriting from the Shape class.

    Attributes:
    - radius: float
              The radius of the circle

    Methods:
    - area(): Overides the area method to calculate the area of a circle.
    - perimeter(): Overides the perimeter method to calculate the circumference of the circle.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialises a Circle instance with a given radius.

        Parameters:
        - radius: float
                  The radius of the circle.  
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculates the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape class.

    Attributes:
    - length: float
              The length of the rectangle.
    - width: float
             The width of the rectangle.

    Methods:
    - __eq__(other): Compares if two rectangles are equal.
    - area(): Overides the area method to calculate the area of a rectangle.
    - perimeter(): Overides the perimeter method to calculate the perimeter of a rectangle.

    """

    def __init__(self, length: float, width: float) -> None:
        """
        Initialise a Rectangle instance with a given length and width.

        Parameters:
        - length: float
                  The length of the rectangle.
        - width: float
                 The width of the rectangle.
        """
        self.length = length
        self.width = width

    def __eq__(self, other: Shape) -> bool:
        """
        Compares if two rectangles are equal.

        Parameters:
        - other: Shape
                 The other shape to compare to.

        Returns:
        bool: True if the rectangles are equal, False otherwise.
        """
        if not isinstance(other, Rectangle):
            return False

        return self.width == other.width and self.length == other.length

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        Returns:
        float: The perimeter of the rectangle.
        """
        return (self.length * 2) + (self.width * 2)


class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.

    Attributes:
    - side_length: float
                   The length of each side of the square.
    """

    def __init__(self, side_length: float) -> None:
        """
        Initialize a Square instance with a given side length.

        Parameters:
        - side_length: float
                       The length of each side of the square.
        """
        super().__init__(side_length, side_length)
