#!/usr/bin/python3
"""test of amenity.py"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


def TestAmenity(unittest.TestCase):
    """amenity test case"""

    def SetUp(self):
       self.am = Amenity()

    def test_type(self):
        self.assertTrue(issubclass(Amenity(), BaseModel())
        self.assertTrue(issubclass(self.am, Amenity())

    def test_name(self):
        self.assertTrue(type(self.am.name), str)

if __name__ = "__main__"
    unittest.main()

