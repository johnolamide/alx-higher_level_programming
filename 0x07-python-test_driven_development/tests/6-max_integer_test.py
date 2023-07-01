#!/usr/bin/python3
"""
    This script tests he max_iteger function from
    6-max_integer module.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        This class defines test cases for the max_integer function
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([7]), 7)


if __name__ == "__main__":
    unittest.main()
