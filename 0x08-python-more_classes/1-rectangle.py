#!/usr/bin/python3
""" reates a rectangle class """


class Rectangle:
    """ Create a rectangle class 
    attrs:
    width: width of rectangle
    height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('width must be an integer')
        elif height < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = height
