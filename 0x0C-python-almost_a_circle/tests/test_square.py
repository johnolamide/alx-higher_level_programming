#!/usr/bin/python3
""" Module contains the Test cases for the Square Class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        TestSquare: test for the Square Class
    """

    def setUp(self):
        """
            Setup a Square Instance
        """
        self.s1 = Square(5)

    def tearDown(self):
        """
            TearDown a Square Instance
        """
        del self.s1

    def test_init(self):
        """
            Test case for the __init__ method
        """
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.area(), 25)


if __name__ == '__main__':
    unittest.main()
