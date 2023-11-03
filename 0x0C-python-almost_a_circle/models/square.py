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

    """Getter"""
    @property
    def size(self):
        return self.width

    """Setter"""
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = size
            self.__height = size
