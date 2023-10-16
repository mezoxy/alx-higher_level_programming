#!/usr/bin/python3
""" The module: rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle: A class That inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """The Area Method"""
    def area(self):
        return self.__height * self.__width

    """Public Method: Display"""
    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("".join("#" for j in range(self.__width)))

    """The magic method __str__"""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                    self.__x, self.__y, self.__width, self.__height)

    """Public method that assigns an argument to each attribute"""
    def update(self, *args, **kwargs):
        lis = ["id", "width", "height", "x", "y"]
        if args:
            i = 0
            while i < min(len(args), len(lis)):
                setattr(self, lis[i], int(args[i]))
                i += 1
        else:
            for key in kwargs:
                if key in lis:
                    setattr(self, key, kwargs[key])

    """Public Method"""
    def to_dictionary(self):
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
