#!/usr/bin/python3
""" Unit tests for City class """

import unittest
from models.city import City
from models.base_models import BaseModel
import pep8


class Test_City(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "State.id"))

    def test_type_city(self):
        """ Test the type of the attribute """
        self.assertEqual(type(City.name), str)
        self.assertEqual(type(City.state_id), str)

    def test_instance(self):
        """ Test if is instance """
        self.assertIsInstance(City, City)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(City.__doc__)
