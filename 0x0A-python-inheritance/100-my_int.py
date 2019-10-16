#!/usr/bin/python3
"""A documentation string"""


class MyInt(int):
    """a dcoumentation string"""

    def __eq__(self, other):
        """a documentation string"""
        return super().__ne__(other)

    def __ne__(self, other):
        """a documentation string"""
        return super().__eq__(other)
