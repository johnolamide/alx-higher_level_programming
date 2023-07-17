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
        self.s1 = Square(5, 2, 1)

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
        self.assertEqual(self.s1.size, 5)
        self.s1.size = 10
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s1.area(), 100)

    def test_raises(self):
        """
            Test case for raising exception
        """
        self.assertRaises(TypeError, lambda: setattr(self.s1, 'size', "size"))
        self.assertRaises(ValueError, lambda: setattr(self.s1, 'size', -10))

    def test_update(self):
        """
            Test case for the update method
        """
        self.s1.update(size=7, id=89, y=1)
        self.assertEqual(self.s1.size, 7)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.y, 1)

    def test_to_dictionary(self):
        """
            Tests case for the to_dictionary method
        """
        self.s1.id = 99
        expected = {'id': 99, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(self.s1.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
