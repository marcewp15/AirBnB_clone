#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models.user import User
from models.base_models import BaseModel
import pep8


class Test_Base(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
