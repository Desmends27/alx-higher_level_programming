#!/usr/bin/python3
""" Sqare class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class the supper class
        with id, x , y, width, height
        width and height will be assigned the same value
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initalze a square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overwrite inherited str method """
        return f"[Square] - ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Upade the square class by adding a public method """
        attributes = ['id', 'width', 'x', 'y']
        if args:
            i = 0
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a square """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """ returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """ Set the value of a setter """
        self.validator(value, 'width')
        self.width = value
        self.height = value
