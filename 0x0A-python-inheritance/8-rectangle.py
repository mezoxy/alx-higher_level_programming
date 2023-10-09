#!/usr/bin/python3
"""The module: 8-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """New class Rectangle  that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__("width", width)
        super().integer_validator("width", width)
        super().__init__("height", height)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
