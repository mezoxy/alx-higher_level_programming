!/usr/bin/python3
"""The module: test_base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest1(unittest.TestCase):
    """BaseTest: A class to test the Base class"""
    def setUp(self):
        Base._Base__nb_objects = 0
    
    def test_id_squa(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(5, 2, 4, 1)
        self.assertEqual(s2.id, 1)

        s3 = Square(5, 2, 4)
        self.assertEqual(s3.id, 2)

        s4 = Square(5, 2)
        s4.id = -15
        self.assertEqual(s4.id, -15)

        s5 = Square(5, 24)
        self.assertEqual(s5.id, 4)
