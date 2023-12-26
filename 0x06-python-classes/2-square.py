#!/usr/bin/python3
''' Create a square class based on 1-square.py '''


class Square:
    ''' Square class
    Args:
        size: private instanse attribute, must be int and greater than 0
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
