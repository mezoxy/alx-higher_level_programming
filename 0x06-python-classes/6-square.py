#!/usr/bin/python3
"""Creat a class of square"""


class Square:
    """The __init__"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position
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
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or\
                len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        a = self.__position[0]
        b = ""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size + a):
                if j in range(a):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
