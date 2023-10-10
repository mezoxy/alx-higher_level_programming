#!/usr/bin/python3
"""The module: 0-read_file"""


def read_file(filename=""):
    """A function that reads a text file"""
    with open(filename, 'r') as fl:
        print(fl.read(), end="")
