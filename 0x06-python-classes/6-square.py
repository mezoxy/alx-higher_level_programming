#!/usr/bin/python3
"""Creat a class of square"""


class Square:
    """The __init__"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        return sefl.__position

    @position.setter
    def position(self, value):
        if len(value) == 2 and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        a = self.__position[0]
        b = ""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size + a):
                if self.__position[1] > 0:
                    b = "#"
                else:
                    b = " "
                print(b, end="")
            print()
