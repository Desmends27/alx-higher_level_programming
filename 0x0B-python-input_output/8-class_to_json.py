#!/usr/bin/python3
""" Returns a dictionart description witg a simple data structure"""


def class_to_json(obj):
    """ Returns a dictionary representation """
    return obj.__dict__
