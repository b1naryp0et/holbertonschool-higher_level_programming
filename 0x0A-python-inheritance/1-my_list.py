#!/usr/bin/python3
"""Create a MyList class"""


class MyList(list):
    """MyList class inherits from a list"""

    def print_sorted(self):
        """Prints the list, sorted"""
        print(sorted(self))
