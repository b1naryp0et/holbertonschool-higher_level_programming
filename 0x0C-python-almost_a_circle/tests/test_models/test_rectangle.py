#!/usr/bin/python3
"""Rectangle tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class rectangleTest(unittest.TestCase):
    """Rectangle class tests"""

    def rectArea(self):
        """Tests area"""

        e = Rectangle(5, 6)
        self.assertEqual(e.area(), 30)
