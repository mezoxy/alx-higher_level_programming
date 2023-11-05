#!/usr/bin/python3
"""The module: base"""


from json import dumps, dump, loads, load


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string:
                            A static method that returns the JSON string
                            representation of list_dictionaries
            Args:
                        A  list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)
