#!/usr/bin/python3
"""A documentation string"""


def inherits_from(obj, a_class):
    """a documentation string"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
