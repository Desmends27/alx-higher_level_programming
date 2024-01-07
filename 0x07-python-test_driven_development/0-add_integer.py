#!/usr/bin/python3
"""
    This is my add module
"""


def add_integer(a, b=98):
    """
    Args:
    a: first number
    b: second nmber
    Raises:
        TypeError: if a or b is not a float or an int
    Return:
    sum of a and b
    """
    if a is None:
        raise ValueError("a must be a number")
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        b = int(b)
    elif b == 98:
        raise ValueError("two numbers must be provided")
    try:
        return a + b
    except ValueError:
        raise ValueError("Cannot convert Nan to integer")
