#!/usr/bin/python3
"""Base Class"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Test class Begins"""

    def test_pep8(self):
        """test for pep8"""

        pep = pep8.StyleGuide(quit=True)
        chk = pep.check_files(["models/base.py"])
        self.assertEqual(chk.total_errors, 0, "Found code style errors (and warnings).")

    def test_positive_number(self):
        """test for positive no."""

        base = Base(8)
        self.assertEqual(base.id, 8)

    def test_doctest(self):
        """doc testing"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_negative(self):
        """tesing negetive number"""

        a = Base(-4)
        self.assertEqual(a.id, -4)

    def test_no_value(self):
        """test with no value"""

        b = Base()
        self.assertEqual(b.id, 1)
