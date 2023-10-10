#!/usr/bin/python3
"""The module: 3-to_json_string"""


import json


def to_json_string(my_obj):
    """to_json_string:
        A function that returns the JSON representation of an object
    Arg:
        my_obj: A string
    Return:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
