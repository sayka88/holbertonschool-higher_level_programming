#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
"""


class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes the square with a specific size.
        The size is a private attribute.
        """
        self.__size = size
