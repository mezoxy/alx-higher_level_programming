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
        self.__width = val_w

    @height.setter
    def height(self, val_h):
        self.__height = val_h

    @x.setter
    def x(self, val_x):
        self.__x = val_x

    @y.setter
    def y(self, val_y):
        self.__y = val_y
