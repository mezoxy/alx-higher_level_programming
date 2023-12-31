#!/usr/bin/python3
"""The module: test_base"""


import unittest
import os
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
    
    def test_id_att(self):
        s1 = Square(5)
        s1.id = -4
        s3 = Square(5, 2, 4)
        self.assertEqual(s3.id, 2)

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

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass
    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))


if __name__ == "__main__":
    unittest.main()
