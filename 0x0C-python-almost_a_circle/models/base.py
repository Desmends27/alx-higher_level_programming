#!/usr/bin/python3
""" Base Class """
import json


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

    @staticmethod
    def validator(attribute, name):
        """Validator and height and width"""
        if not isinstance(attribute, int):
            raise TypeError(f"{name} must be an integer")
        if attribute <= 0:
            raise TypeError(f"{name} must be > 0")

    @staticmethod
    def validator2(attribute, name):
        """Validate x and y"""
        if not isinstance(attribute, int):
            raise TypeError(f"{name} must be an integer")
        if attribute < 0:
            raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the json representation of list_objs to a file """
        if list_objs is None:
            return []
        else:
            filename = cls.__name__+".json"
            with open(filename, mode="w", encoding="utf-8") as file:
                json_list = [obj.to_dictionary() for obj in list_objs]
                json.dump(json_list, file)

    @staticmethod
    def from_json_string(json_string):
        """ Retunrs the list of json representation """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Retunrs an instance with all attributes already set """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        name = cls.__name__ + ".json"
        try:
            with open(name) as f:
                j = cls.from_json_string(f.read())
                return [cls.create(**x) for x in j]
        except FileNotFoundError:
            return []
