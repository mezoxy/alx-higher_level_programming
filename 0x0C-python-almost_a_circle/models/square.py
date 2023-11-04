#!/usr/bin/python3
"""The module : square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)
        self.size = size

    """Getter and Setter"""
    @property
    def size(self):
        """Getter"""
        return self.width

    """Set the width an height"""
    @size.setter
    def size(self, size):
        """Setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    """Public Method"""
    def update(self, *args, **kwargs):
        """update: Public Method
        Args:
            *args and kwargs
        """
        lis = ["id", "size", "x", "y"]

        if args:
            for i in range(min(len(lis), len(args))):
                setattr(self, lis[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    """Public method"""
    def to_dictionary(self):
        """to_dictionary"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}

    """The __str__ Method"""
    def __str__(self):
        """Magic Method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
