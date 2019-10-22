#!/usr/bin/python3
"""Module for Rectangle Class"""

from models.base import Base
"""import class Base"""


class Rectangle (Base):
    """Class: rectangle which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init/attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get rectangle width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets rectangle width"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get rectangle height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Raise Type and Value errors for height"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Raise errors for y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Rectangle made of #"""

        for q in range(self.__y):
            print()
        for q in range(self.__height):
            print(self.__x * ' ' + self.__width * "#")

    def __str__(self):
        """Returns the string of the class"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Arguments are assigned to attributes"""

        w = 0
        if args is not None and len(args) != 0:
            for g in args:
                w = w + 1
                if w == 1:
                    self.id = g
                if w == 2:
                    self.width = g
                if w == 3:
                    self.height = g
                if w == 4:
                    self.x = g
                if w == 5:
                    self.y = g
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary mapping"""

        diction = {'id': self.id, 'width': self.width, 'height': self.height,
                   'x': self.x, 'y': self.y}
        return diction
