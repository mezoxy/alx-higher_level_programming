#!/usr/bin/python3
"""A class Rectangle"""


class Rectangle:
    """Class name : Rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    """Special method __str__"""
    def __str__(self):
        obj = ""
        if self.__width == 0 or self.__height == 0:
            return obj
        for i in range(self.__height):
            for j in range(self.__width):
                obj += "#"
            if i == self.__height - 1:
                obj += ""
            else:
                obj += "\n"
        return obj

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
