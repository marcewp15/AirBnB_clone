#!/usr/bin/python3
""" Unit tests for Amenity class """

import unittest
from models.amenity import Amenity
from models.base_models import BaseModel
import pep8


class Test_Amenity(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        self.assertTrue(hasattr(Amenity, "name"))

    def test_type_amenity(self):
        """ Test the type of the attribute """
        self.assertEqual(type(Amenity.name), str)

    def test_instance(self):
        """ Test if is instance """
        self.assertIsInstance(Amenity, Amenity)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(Amenity.__doc__)
