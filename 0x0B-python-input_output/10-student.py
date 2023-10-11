#!/usr/bin/python3
"""The module: '9-student'"""


class Student:
    """A class that defines a student by:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method"""
    def to_json(self, attrs=None):
        d = {}
        if type(attrs) is list:
            for i in attrs:
                if i == "first_name":
                    d["first_name"] = self.first_name
                if i == "last_name":
                    d["last_name"] = self.last_name
                if i == "age":
                    d["age"] = self.age
            return d
        return self.__dict__
