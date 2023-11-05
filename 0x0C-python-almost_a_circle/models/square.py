#!/usr/bin/python3
"""The module square"""
from json import dumps, dump, loads, load
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val_s):
        if type(val_s) is not int:
            raise TypeError("width must be an integer")
        elif val_s <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = val_s
            self.height = val_s

    def __str__(self):
        """
            Magic method will return:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
