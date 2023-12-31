#!/usr/bin/python3
"""Creat a class of square"""


class Square:
    """The __init__"""
    def __init__(self, size=0):
        self.__size = size
    """Property"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
