#!/usr/bin/python3
"""A documentation string"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a documentation string"""

    def __init__(self, width, height):
        """a documentation string"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)("height", height)
        self.__width = width
        self.__height = height
