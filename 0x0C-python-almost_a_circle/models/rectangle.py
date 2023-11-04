#!/usr/bin/python3
"""The module rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """hi"""
    @property
    def x(self):
        return self.__x

    """hi"""
    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

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
        self.__y = val_y

    @width.setter
    def width(self, val_wi):
        if type(val_wi) is not int:
            raise TypeError("width must be an integer")
        elif val_wi <= 0:
            raise ValueError("width must be > 0")
        self.__width = val_wi

    @height.setter
    def height(self, val_h):
        if type(val_h) is not int:
            raise TypeError("height must be an integer")
        elif val_h <= 0:
            raise ValueError("height must be > 0")
        self.__height = val_h

    """A public Method Area"""
    def area(self):
        return self.__width * self.__height

    """A public method Display"""
    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    """The magic method __str__"""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    """A public method Update"""
    def update(self, *args, **kwargs):
        """update"""
        att = [
                "id",
                "width",
                "height",
                "x",
                "y"
                ]
        if args:
            for i in range(min(len(att), len(args))):
                setattr(self, att[i], int(args[i]))
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    """A public method to_dictionary"""
    def to_dictionary(self):
        """to_dictionary"""
        return {'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width}
