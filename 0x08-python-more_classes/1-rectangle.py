#!/usr/bin/python3
""" reates a rectangle class """


class Rectangle:
    """ Create a rectangle class
    attrs:
    width: width of rectangle
    height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        """Special init method"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height retriver"""
        return self.__height

    @property
    def width(self):
        """width retriver"""
        return self.__width

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """" Setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
