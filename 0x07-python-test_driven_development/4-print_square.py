#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """Print a square with the # character.
     Args:
        size (int)
    """
    if (type(size) is not int) or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="" if j < size - 1 else "\n")
