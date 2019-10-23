#!/usr/bin/python3
"""Square tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class squareTests(unittest.TestCase):
    """Class for testing Square"""

    def sq_area(self):
        """Area test"""

        e = Square(5)
        self.assertEqual(e.area(), 25)

