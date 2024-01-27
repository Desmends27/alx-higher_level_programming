#!/usr/bin/python3
""" Save a an obj to a file """
import json


def save_to_json_file(my_obj, filename):
    """ No exceptions are managed """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(fp=f,obj=my_obj)
