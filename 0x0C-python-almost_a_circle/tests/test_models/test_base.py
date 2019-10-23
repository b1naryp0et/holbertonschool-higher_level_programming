#!/usr/bin/python3
"""Base tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class baseTest(unittest.TestCase):
    """Base class tests"""

    def testId(self):
        """Tests first id assignment"""

        u = Base()
        self.assertEqual(u.id, 8)
