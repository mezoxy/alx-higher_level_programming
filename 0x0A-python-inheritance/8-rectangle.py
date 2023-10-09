#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""The module: 8-rectangle"""


class Rectangle(BaseGeometry):
    """New class Rectangle  that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        """somt"""
        super().__init__("height", height)
        super().integer_validator("height", height)
        self.__height = height
