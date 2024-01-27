#!/usr/bin/python3
""" A student class """


class Student:
    def __init__(self, first_name, last_name, age):
        """ first_name: first name of student
            last_name: last name of student
            age: age of sudent
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retuns the dictionary representation """
        return self.__dict__
