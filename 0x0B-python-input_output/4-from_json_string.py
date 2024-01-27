#!/usr/bin/python3
""" Returns an object represent by a son string """
import json


def from_json_string(my_str):
    """ No execeptions are managed """
    return json.loads(my_str)
