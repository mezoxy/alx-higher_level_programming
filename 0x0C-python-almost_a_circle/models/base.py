#!/usr/bin/python3
"""The module: base"""


import json


class Base:
    """A Base class: First class"""

    __nb_objects = 0
    """The Constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """Static Methood"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """A method that returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    """Class Method"""
    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w") as fl:
            rep_json = []
            for obj in list_objs:
                rep_json.append(obj.to_dictionary())
            fl.write(cls.to_json_string(rep_json))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)
        return dummy.update(**dictionary)
