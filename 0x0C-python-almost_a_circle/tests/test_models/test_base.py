#!/usr/bin/python3
"""The module: test_base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest1(unittest.TestCase):
    """BaseTest: A class to test the Base class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test_id: To test the id of instance according
            to id if it None or not
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(-44)
        self.assertEqual(b2.id, -44)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base(None)
        self.assertEqual(b4.id, 2)

        b5 = Base(123456)
        b5.id = 222222
        self.assertEqual(b5.id, 222222)

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

    def test_priv_atr(self):
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects

    def test_Tojs(self):
        js_rep = Base.to_json_string(None)
        self.assertEqual(js_rep, "[]")

        js_rep = Base.to_json_string([])
        self.assertEqual(js_rep, "[]")

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        js_rep = Base.to_json_string([dictionary])
        resu = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(js_rep, resu)

    def test_Tojs_noArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save_to_fl(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as fl:
            js_rep = fl.read()
            resu = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
            resu1 = '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(js_rep, resu + resu1)


if __name__ == "__main__":
    unittest.main()
