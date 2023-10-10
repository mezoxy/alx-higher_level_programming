#!/usr/bin/python3
"""The module: 5-save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: A function that writes an Object
        to a text file, using a JSON representation
    Args:
        my_obj: The object to be convert to JSON representation
        filename: The destination
    """
    with open(filename, 'w') as fl:
        fl.write(json.dumps(ny_obj))
