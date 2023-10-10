#!/usr/bin/python3
"""The module: 1-write_file"""


def write_file(filename="", text=""):
    """write_file: A function that writes a string to a text file
    Args:
        filename: The full path
        text: The string to write
        Return: The number of characters written
    """
    with open(filename, 'w') as fl:
        fl.write(text)
        return len(text)
