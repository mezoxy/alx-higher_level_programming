#!/usr/bin/python3
"""The module: 6-base_geometry"""


class BaseGeometry:
    """An instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public method that validate value"""
    def integer_validator(self, name, value):
        """integer_validator: That validate the value"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
