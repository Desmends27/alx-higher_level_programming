#!/usr/bin/python3
""" Based on the student class in 9 """


class Student:
    def __init__(self, first_name, last_name, age):
        """
            first_name: name of the student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation
        all if attrs is none, others based on the string in attrs
        """
        if attrs.len == 0:
            return self.__dict__
        if attrs:
            attrs_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attrs_dict[attr] = getattr(self, attr)
            return attrs_dict
        else:
            return self.__dict__
