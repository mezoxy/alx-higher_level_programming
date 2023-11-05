#!/usr/bin/python3
"""The module : base"""
from json import dumps, loads, load, dump


class Base:
    """The Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    """Static Method for JSON representation"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    """Class method save to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        name_of_file = "{}.json".format(cls.__name__)
        list_dict = []
        with open(name_of_file, "w") as fl:
            if list_objs is None:
                fl.write("[]")
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsn_string = cls.to_json_string(list_dict)
                fl.write(jsn_string)

    """Static Method for"""
    @staticmethod
    def from_json_string(json_string):
        list_rep_json = []
        if json_string is None or len(json_string) == 0:
            return list_rep_json
        else:
            for dic in loads(json_string):
                list_rep_json.append(dumps(dic))
            return list_rep_json

    """Class method creat"""
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(2)
            dummy.update(**dictionary)
        return dummy

    """Class method"""
    @classmethod
    def load_from_file(cls):
        flname = "{}.json".format(cls.__name__)
        new = []
        try:
            with open(flname, "r") as fl:

                return new
        except Exception as e:
            return []
