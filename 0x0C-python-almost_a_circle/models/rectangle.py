#!/usr/bin/python3
"""the module ractangle"""
from json import dumps, dump, loads, load
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
        private instance width height x and y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """Getter and stter for each attributtes except id"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """Set the value to each attributes"""
    @width.setter
    def width(self, val_w):
        if type(val_w) is not int:
            raise TypeError("width must be an integer")
        elif val_w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val_w

    @height.setter
    def height(self, val_h):
        if type(val_h) is not int:
            raise TypeError("height must be an integer")
        elif val_h <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val_h

    @x.setter
    def x(self, val_x):
        if type(val_x) is not int:
            raise TypeError("x must be an integer")
        elif val_x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val_x

    @y.setter
    def y(self, val_y):
        if type(val_y) is not int:
            raise TypeError("y must be an integer")
        elif val_y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val_y
