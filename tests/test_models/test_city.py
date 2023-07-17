#!/usr/bin/python3
"""city test class"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """Test class Begins"""

    def test_pep8(self):
        """test for pep8"""

        pep = pep8.StyleGuide(quit=True)
        chk = pep.check_files(["models/city.py"])
        self.assertEqual(chk.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doctest(self):
        """doc testing"""

        self.assertTrue(len(City.__doc__) >= 1)
