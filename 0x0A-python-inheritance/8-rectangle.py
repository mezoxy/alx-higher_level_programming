#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""The module: 8-rectangle"""


class Rectangle(BaseGeometry):
    """New class Rectangle  that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__("width", width)
        super().integer_validator("name", width)
        super().integer_validator("name", height)
        self.__width = width
        self.__height = height
