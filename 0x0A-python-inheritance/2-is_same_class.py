#!/usr/bin/python3
""" This function checks the instance of an object """


def is_same_class(obj, a_class):
    """
    Args:
        obj(object) : the object to check
        a_class: the class to check against
    Returns:
        bool: True if isinstance else false
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
