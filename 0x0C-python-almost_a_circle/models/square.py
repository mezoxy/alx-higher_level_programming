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

    def update(self, *args, **kwargs):
        """update: a public method that assigns attributes
            attributes:
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    3rd argument should be the x attribute
                    4th argument should be the y attribute
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(min(len(args), 4)):
                setattr(self, attributes[i], args[i])
        else:
            for key in kwargs:
                if key in attributes:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
            to_dictionary:
                    A public method that returns
                    the dictionary representation of a Square
            The dictionary contain:
                            id, size, x and y
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
