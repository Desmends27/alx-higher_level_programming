#!/usr/bin/python3
"""Create a class Square with the properties of a square"""


class Square:
    """This is the init function"""
    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        self.__size = size

    """This is the getter method"""
    @property
    def size(self):
        """
        Returns:
            the size attribute
        """
        return self.__size

    """This is the setter method"""
    @size.setter
    def size(self, value):
        """
        Args:
            value: value to set the size to
        Raises:
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """This is the area method"""
    def area(self):
        """
        Return: area of square
        """
        return self.__size ** 2
