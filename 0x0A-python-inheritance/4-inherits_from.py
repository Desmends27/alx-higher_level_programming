#!/usr/bin/python3
""" Checks for subclass of objects """


def inherits_from(obj, a_class):
    """
    Args:
    obj(object) : object to check
    a_class(class) : object to test against
    Return:
    bool: True if it inherits form, false otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
