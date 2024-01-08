#!/usr/bin/python3
""" This inherits from the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Attributes:
        width: width of rectangle
        height: height of rectangle
    Methods:
    just init
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates area of rectagnle
        Args:
        None
        """
        return self.__width * self.__height

    def __str__(self):
        """ Incase object is called with print """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
