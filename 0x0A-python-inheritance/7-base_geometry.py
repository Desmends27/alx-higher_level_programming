#!/usr/bin/python3
""" Uses the base geometry class """


class BaseGeometry:
    """
    This the base geometry class
    Attributes:
    none
    """

    def area(self):
        """
        This is the area method
        Args:
        none
        Raises:
        Exception: message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator method
        Args:
        name(string): always a string
        value(integer): value to check
        Raises:
        TypeError: if message is not an integer
        ValueError: if message is not > 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
