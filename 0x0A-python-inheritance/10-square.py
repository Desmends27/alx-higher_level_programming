#!/usr/bin/python3
""" This inherits from the rectagle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Squre class
    Attributes:
    size: size of square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ calculates the area """
        return self.__size ** 2
