#!/usr/bin/python3
""" This is the base class for all the files here """


import json


class Base:
    """
    Base class
    Attributes:
        __nb_objects(int): class attribute
        id(int): id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """ Integer validtor for width and height """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def integer_validator2(self, name, value):
        """ Integer validator for x and y """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return json representation of list dictionaries"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a json string to a file """
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = "[]"
        with open(cls.__name__ + ".json", mode='w') as f:
            f.write(j)

    @staticmethod
    def from_json_string(json_string):
        """ Return  a list representation json string """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance of all attributes """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Return list of instances """
        name = cls.__name__ + ".json"
        try:
            with open(name) as f:
                j = cls.from_json_string(f.read())
            return [cls.create(**x) for x in j]
        except FileNotFoundError:
            return []
