#!/usr/bin/python3
""" Module contains the test for the Base Class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Test cases for the Base Class
    """

    def setUp(self):
        """
            Setup the Base Instances
        """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        """
            Tear Down the Base Instance
        """
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_init(self):
        """
            Test the __init__ method
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)


if __name__ == "__main__":
    unittest.main()
