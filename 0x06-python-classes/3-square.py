#!/usr/bin/python3
"""A class od square"""


class Square:
    """The __init__ """
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """An  instance method that returns he current square area"""
    def area(self):
        return self.__size * self.__size
