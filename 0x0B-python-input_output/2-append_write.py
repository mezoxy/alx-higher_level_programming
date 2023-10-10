#!/usr/bin/python3
"""The module: 2-append_write"""


def append_write(filename="", text=""):
    """append_write:
    A unction that appends a string at the end of a text file 

    Args:
        filename: The path name or name of the file
        text: A string to add at the end

    Return:
        The number of characters added
    """
    with open(filename, 'a') as fl:
        fl.write(text)
        return len(text)
