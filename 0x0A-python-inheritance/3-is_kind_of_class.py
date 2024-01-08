#!/usr/bin/python3
""" Contains the is kind of object class """


def is_kind_of_class(obj, a_class):
    """
    Args:
    obj(object) : object to be checkd
    a_class: class to be checked agains
    Returns:
    bool: True if isinstance, False otherwise
    """
    return isinstance(obj, a_class)
