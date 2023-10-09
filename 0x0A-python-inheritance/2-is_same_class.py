#!/usr/bin/python3
"""The module: 2-is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class: A unction that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    Args:
        obj: The obect to check
        a_class: The class
    Return: True if the object is exactly an instance else False
    """
    if isinstance(obj, a_class):
        return True
    False
