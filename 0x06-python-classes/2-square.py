#!/usr/bin/python3
"""Creat a square class"""


class Square:

    """The __int__ function for initialisation"""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
