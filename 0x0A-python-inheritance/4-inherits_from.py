#!/usr/bin/python3
"""The module: 4-inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from: A function that returns True if the object is
    an instance of a class that inherited
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
