#!/usr/bin/python3
"""The module: 6-load_from_json_file"""


import json


def load_from_json_file(filename):
    """load_from_json_file:
            A function that creates an Object from a “JSON file”
        Arg:
            filename: The source
    """
    with open(filename, 'r') as fl:
        return json.load(fl)
