#!/usr/bin/python3
""" Module contains the test for the Base Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
        Test cases for the Base Class
    """

    def setUp(self):
        """
            Setup the Base Instances
        """
        self.b1 = Base()

    def tearDown(self):
        """
            Tear Down the Base Instance
        """
        del self.b1

    def test_init(self):
        """
            Test the __init__ method
        """
        pass
       # self.assertEqual(self.b1.id, 2)

    def test_to_json_string(self):
        """
            Test case for the to_json_string method
        """
        self.assertEqual(Base.to_json_string([]), "[]")
        
        # Test None
        self.assertEqual(Base.to_json_string(None), "[]")
        
        # Test list of dictionaries
        list_dictionaries = [{'x': 1, 'y': 2}, {'width': 3, 'height': 4}]
        expected = '[{"x": 1, "y": 2}, {"width": 3, "height": 4}]'
        self.assertEqual(Base.to_json_string(list_dictionaries), expected)

    def test_from_json_string(self):
        """
            Test case for the from_json_string method
        """
        # Test empty string
        self.assertEqual(Base.from_json_string(""), [])
        
        # Test None
        self.assertEqual(Base.from_json_string(None), [])
        
        # Test JSON string
        json_string = '[{"x": 1, "y": 2}, {"width": 3, "height": 4}]'
        expected = [{'x': 1, 'y': 2}, {'width': 3, 'height': 4}]
        self.assertEqual(Base.from_json_string(json_string), expected)

    def test_create(self):
        """
            Test case for the create method
        """
        # Test create with Rectangle
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        
        # Test create with Square
        s1 = Square(5, 1, 2, 99)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
