#!/usr/bin/python3
""" Unit tests for Amenity class """

import unittest
from models.user import User
from models.base_models import BaseModel
import pep8


class Test_User(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        self.assertTrue(hasattr(User, "id"))
        self.assertTrue(hasattr(User, "create_at"))
        self.assertTrue(hasattr(User, "update_at"))
        self.assertTrue(hasattr(User, "__init__"))

    def test_type_user(self):
        """ Test the type of the attribute """
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)

    def test_instance(self):
        """ Test if is instance """
        self.assertIsInstance(User, User)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(User.__doc__)
