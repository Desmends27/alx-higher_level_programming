#!/usr/bin/python3
""" Inherits from the Rectangle subclass """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Subclass of the Rectangle subclass representing a square
    Attributes:
        size: the width and height of the square
        x: the x-coordinate of the square
        y: the y-coordinate of the square
        id: the unique identifier of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class, uses the Rectangle constructor
        Args:
            size (int): the size of the square
            x (int): the x-coordinate of the square, default is 0
            y (int): the y-coordinate of the square, default is 0
            id (int): the unique identifier of the square, default is None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object
        Returns:
            str: a string representation of the Square object
        """
        return "[Square] ({0}) {1}/{2} - {3}".format(self.id, self.x,
                                                     self.y,
                                                     self.height)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object
        Returns:
            dict: a dictionary representation of the Square object
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def update(self, *args, **kwargs):
        """
        Updates the Square object with new values
        Args:
            *args: variable number of arguments, can be used to update id
                    , size, x, and y in order
            **kwargs: variable number of keyword arguments,
                can be used to update id, size, x,
                and y by specifying the attribute as a keyword
        """
        attributes = ["id", "size", "x", "y"]
        i = 0
        if args:
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """
        Gets the size of the Square object
        Returns:
            int: the size of the Square object
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets the size of the Square object
        Args:
            size (int): the size to set for the Square object
        """
        self.width = size
        self.height = size
