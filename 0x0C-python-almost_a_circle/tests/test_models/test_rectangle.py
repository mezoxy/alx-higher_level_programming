#!/usr/bin/python3
"""File to test"""


import unittest
import os
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

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 4,"2")

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 4, 3, "2")

        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r1 = Rectangle(11, -2)

        with self.assertRaises(TypeError):
            r1 = Rectangle(0.5, 2)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 4, -3)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 4, 3, -9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 4, 3.4)

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 4, 3, 4.7)

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
