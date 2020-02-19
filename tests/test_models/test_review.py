#!/usr/bin/python3
""" Unit tests for Review class """

import unittest
from models.review import Review
from models.base_models import BaseModel
import pep8


class Test_Review(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        self.assertTrue(hasattr(Review, "Place.id"))
        self.assertTrue(hasattr(Review, "User.id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_type_review(self):
        """ Test the type of the attribute """
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.text), str)

    def test_instance(self):
        """ Test if is instance """
        self.assertIsInstance(Review, Review)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(Review.__doc__)
