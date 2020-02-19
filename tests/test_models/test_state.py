#!/usr/bin/python3
""" Unit tests for State class """

import unittest
from models.state import State
from models.base_models import BaseModel
import pep8


class Test_State(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        pass

    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_hasattr(self):
        """ Test if an object has an attribute """
        self.assertTrue(hasattr(State, "name"))

    def test_type_state(self):
        """ Test the type of the attribute """
        self.assertEqual(type(State.name), str)

    def test_instance(self):
        """ Test if is instance """
        self.assertIsInstance(State, State)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(State.__doc__)
