#!/usr/bin/python3
"""Test for BaseModel class"""

import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime
import inspect
import json

class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ Tests The base model functions """
    def test_Attributes(self):
        """Test all the attributes"""
        bmodel_1 = BaseModel()
        bmodel_2 = BaseModel()
