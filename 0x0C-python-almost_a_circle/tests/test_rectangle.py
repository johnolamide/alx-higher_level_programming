#!/usr/bin/python3
""" Module contains the test class for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Test Class for the Rectangle class
    """
    def setUp(self):
        """
            Rectangle instance setup
        """
        self.r = Rectangle(10, 20, 5, 5, 99)

    def tearDown(self):
        """
            Rectangle instance tear down
        """
        del self.r

    def test_init(self):
        """
            Test case for the __init__ function
        """
        self.assertEqual(self.r.width, 10)
        self.assertEqual(self.r.height, 20)
        self.assertEqual(self.r.x, 5)
        self.assertEqual(self.r.y, 5)
        self.assertEqual(self.r.id, 99)

    def test_setters(self):
        """
            Test case for the setters
        """
        self.r.width = 15
        self.r.height = 25
        self.r.x = 5
        self.r.y = 10
        self.assertEqual(self.r.width, 15)
        self.assertEqual(self.r.height, 25)
        self.assertEqual(self.r.x, 5)
        self.assertEqual(self.r.y, 10)


if __name__ == "__main__":
    unittest.main()
