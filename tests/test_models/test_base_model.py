#!/usr/bin/python3
"""Base Class"""
import unittest
import pep8
import os
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """Test class Begins"""

    def test_pep8(self):
        """test for pep8"""

        pep = pep8.StyleGuide(quit=True)
        chk = pep.check_files(["models/base_model.py"])
        self.assertEqual(chk.total_errors, 0, "Found code style errors (and warnings).")

    def test_doctest(self):
        """doc testing"""

        self.assertTrue(len(Base.__doc__) >= 1)
