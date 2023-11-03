#!/usr/bin/python3
"""The module square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The subclasse of Rectabgle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
