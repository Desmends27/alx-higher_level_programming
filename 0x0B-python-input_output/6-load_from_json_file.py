#!/usr/bin/python3
""" Load data from a json file """
import json


def load_from_json_file(filename):
    """ file is the file with the obj data"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(fp=f)
