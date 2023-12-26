#!/usr/bin/python3
"""Creates a Class Square"""


class Square:
    """ This is the init method """

    def __init__(self, size=0):
        """
        Initalizes class attributes

        Args:
        size: defines the size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """This is the area method"""
    def area(self):
        """
        Defines the area attribute
        Returns:
            The area of the current square
        """
        return self.__size ** 2
