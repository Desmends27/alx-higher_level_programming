#!/usr/bin/python3
""" Rectangle class that inherits form the Base class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    attrs:
    __width: width of rectangle, private instance attribute
    __height: height or rectangle, private instance attribute
    __x: x attribute of rectangle, private instance attribute
    __y: y attribute of rectangle, private instance attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}\
                - {self.__width}/{self.__height}'

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        super().validator(value, 'width')
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        super().validator(value, 'height')
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        super().validator2(value, 'x')
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        super().validator2(value, 'y')
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the rectacle"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def to_dictionary(self):
        """ Returns the dictionary representatin of a rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def update(self, *args, **kwargs):
        """ Upate the rectangle attributes """
        attributes = ["id", "width", "height", "x", "y"]
        i = 0
        if args:
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
