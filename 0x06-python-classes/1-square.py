#!/bin/python3
""" Create a python class with size attribute """


class Square:
    """ Create a square class
        Args:
            size: length of the one side of the square
    """
    def __init__(self, size):
        self.__size = size
