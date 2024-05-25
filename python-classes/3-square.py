#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size and
a public instance method to calculate area.
"""


class Square:
    """
    This class defines a square by its size and can calculate its area.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a specific size.
        The size is a private attribute.
        Args:
            size (int): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
