#!/usr/bin/python3
"""The module"""


def class_to_json(obj):
    """class_to_json: returns the dictionary description"""
    return obj.__dict__
