#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(2)
if str(s) != "[Square] (1) 0/0 - 2":
    print("__str__ is not correctly overloaded: {}".format(s))
    exit(1)
