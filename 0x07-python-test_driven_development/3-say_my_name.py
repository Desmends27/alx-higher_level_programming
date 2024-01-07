#!/usr/bin/python3
"""This function say the name of an entity"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: first name of the person
        last_name: second name of the person
    Raises:
        TypeError: both args are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name != "" and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0:s} {1:s}".format(first_name, last_name))
