#!/usr/bin/python3
"""File to test"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Id(unittest.TestCase):
    """Test Cases: """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id_rect(self):
        """Test_id: To test the id of instance according
            to id if it None or not
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

        r3 = Rectangle(10, 2)
        r3.id = -222
        self.assertEqual(r3.id, -222)

        r4 = Rectangle(10, 4, 1, 2, -98)
        self.assertEqual(r4.id, -98)

    def test_id_non_int(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
