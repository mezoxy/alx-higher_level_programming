#!/usr/bin/python3
"""The module: 3-to_json_string"""


import json


def from_json_string(my_str):
    """to_json_string:
        A function that returns the JSON representation of an object
    Arg:
        my_str: A string
    Return:
        An obect represented by JSON string
    """
    return json.loads(my_str)
