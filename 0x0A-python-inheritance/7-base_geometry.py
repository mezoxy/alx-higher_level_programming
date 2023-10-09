#!/usr/bin/python3
"""The module: 6-base_geometry"""


class BaseGeometry(list):
    """An instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public method that validate value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
