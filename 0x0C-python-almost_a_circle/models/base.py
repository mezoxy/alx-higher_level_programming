#!/usr/bin/python3
"""The module: base"""


json import dumps, dump, loads, load


class Base:
    """A Base class: First class"""
    __nb_objects = 0
    """The Constructor"""
    def __init__(self, id=None):
        """The constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
