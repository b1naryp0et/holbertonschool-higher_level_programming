#!/usr/bin/python3
"""Square tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pep8


class TestRectangle(unittest.TestCase):
    """ Class rectangle tests """
    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
