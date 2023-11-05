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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file:
                        A class method  that writes the JSON string
                        representation of list_objs to a file
        Args:
            cls:        A class
            list_objs:   A list of instances
        """
        flname = str(cls.__name__) + ".json"
        array = []
        string = ""
        with open(flname, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    array.append(obj.to_dictionary())
                string = cls.to_json_string(array)
                f.write(string)
