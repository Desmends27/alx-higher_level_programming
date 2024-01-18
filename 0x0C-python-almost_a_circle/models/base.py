#!/usr/bin/python3
""" Base Class """


class Base:
    """ Base class for all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method 
        id: id cannot be none and will always be an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
