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
