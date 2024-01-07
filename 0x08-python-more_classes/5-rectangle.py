#!/usr/bin/python3
""" A rectangle class """


class Rectangle:
    """ Defines a rectangle class
    properties:
    width: width of rectangle
    height: height of rectangle
    methods:
    area: returns area of rectangle
    perimeter: returns perimeter of rectangle
    """
    def __init__(self, width=0, height=0):
        """ Init method
        width: width of rectangle(private)
        height: height of rectangle(private)
        """
        self.__height = height
        self.width = width

    def __str__(self):
        """ Print offiails string representation """
        shape = ''
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.width):
                shape += '#'
            if i < self.__height - 1:
                shape += '\n'
        return shape

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        """ Width retriver """
        return self.__width

    @property
    def height(self):
        """ Height retriver """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height """
        if not isinstance(value, int):
            raise TypeError('height must be a integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle
        if width or hieght is 0, perimeter is 0"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)
