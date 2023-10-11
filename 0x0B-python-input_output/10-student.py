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
                if hasattr(self, i):
                    d[i] = getattr(self, i)
            return d
        return self.__dict__
