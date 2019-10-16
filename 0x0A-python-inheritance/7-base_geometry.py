#!/usr/bin/python3
"""A documentation string"""


class BaseGeometry:
    """a documentation string"""

    def area(self):
        """a documentation string"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """a documentation string"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
