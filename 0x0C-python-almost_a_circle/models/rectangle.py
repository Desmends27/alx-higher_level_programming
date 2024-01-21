#!/usr/bin/python3
""" This is the rectangle class, inherits from the base class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    Attributes:
    width(int): width of rectangle
    height(int): height of recangle
    x(int): x component
    y(int): y component
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id,
                                                            self.x, self.y,
                                                            self.width,
                                                            self.height)

    def to_dictionary(self):
        """ Print dictinory representation """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def area(self):
        """ Calcuates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Print to stdout """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Update the data """
        attributes = ["id", "width", "height", "x", "y"]
        i = 0
        if args:
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        super().integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        super().integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        super().integer_validator2("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        super().integer_validator2("y", y)
        self.__y = y
