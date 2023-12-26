#!/usr/bin/python3
"""Square class again but with a defined square
    The size of the square is checked and errors are raised
    based on input
"""


class Square:
    """This is a the built in init function """

    def __init__(self, size=0):
        """
        Args:
            size: private instance value of the square
        Raises:
            TypeError: if size argument is not integer
            ValueError: if the size of the argument is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
