#!/usr/bin/python3
""" This defines a square class """


class Square:
    """ This is the init function """
    def __init__(self, size=0) -> None:
        """ Args:
            size: size of square
            Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
        """ This is the getter method"""
    @property
    def size(self):
        """
        Returns: size
        """
        return self.__size
        """ This is the setter method """
    @size.setter
    def size(self, value=0):
        """
        Args:
            value: set size to value
            Raises:
            TypeError: if value is not an integer
            ValueError: if size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0:")
        else:
            self.__size = value
    """this is the area method """
    def area(self):
        """
        Returns:
            area of the square
        """
        return self.__size ** 2

    """ this my_print method prints a square """

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
