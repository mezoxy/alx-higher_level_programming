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
                len(value) != 2 or type(value[0]) or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.__size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.__size)
