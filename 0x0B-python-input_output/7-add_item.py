#!/usr/bin/python3
""" Uses all 3 previous modules """
from sys import argv
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    temp = load_from_json_file("add_item.json")
except Exception:
    temp = []

temp.extend(argv[1:])
save_to_json_file(temp, "add_item.json")
