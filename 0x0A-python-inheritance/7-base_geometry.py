#!/usr/bin/python3
"""The module: 6-base_geometry"""


class BaseGeometry(list):
    """A basic class"""
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    """An instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public method that validate value"""
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

bg = BaseGeometry()
bg.integer_validator(12)
