#!/usr/bin/python3
""" This defines a ssquare class"""


class Square:
    """ This is the init method"""
    def __init__(self, size=0, position=(0,0)):
        """
        Args:
            size : size of square (private)
            position: x, y
        """
        self.size = size
        self.position = position

    """This is the getter method"""
    @property
    def size(self):
        """Returns:
            the size """
        return self.__size

    """ This is the setter method"""
    @size.setter
    def size(self, value):
        """
            Args:
                value: sets the size to value
            Raises:
            TypeError: if value is not an int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value
    """This is the position attribute"""
    @property
    def position(self):
        """Returns:
            position attribute
        """
        return self.__position
    """This is the property setter"""
    @position.setter
    def position(self, value):
        """
        Args:
            value: checks the value of the tuple
        Raises:
            TypeError: if len(tuple) is not 2 and value not a tuple"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) and val > 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """ This is the area property"""
    def area(self):
        """
        Returns:
            area of size
        """
        return self.__size ** 2
    def my_print(self):
        """Prints the # and space """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                        print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
