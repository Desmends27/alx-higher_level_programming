#!/usr/bin/python3
""" This functions returns the list of availbe attributes
    and methods an object has"""


def lookup(obj):
    """
    Returns:
        avaialbe attributes and methods of obj
    """
    return dir(obj)
