#!/usr/bin/python3
"""Square class mod"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init Square"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for square size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for square size"""

        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string"""

        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Square"""

        k = 0
        if args is not None and len(args) != 0:
            for s in args:
                k = k + 1
                if k == 1:
                    self.id = s
                if k == 2:
                    self.size = s
                if k == 3:
                    self.x = s
                if k == 4:
                    self.y = s
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary of a square"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
