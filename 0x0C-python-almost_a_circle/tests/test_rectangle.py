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

#    def test_str(self):
#        """
#            Test case for the __str__ function
#        """
#        self.assertEqual(print(self.r), "[Rectangle] (99) 5/5 - 10/20")

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

    def test_valueerror(self):
        """
            Test case for raising ValueError
        """
        self.assertRaises(ValueError, lambda: setattr(self.r, 'width', -7))
        self.assertRaises(ValueError, lambda: setattr(self.r, 'height', 0))
        self.assertRaises(ValueError, lambda: setattr(self.r, 'x', -2))
        self.assertRaises(ValueError, lambda: setattr(self.r, 'y', -2))

    def test_typeerror(self):
        """
            Test case for raising TypeError
        """
        self.assertRaises(TypeError, lambda: setattr(self.r, 'width', "width"))
        self.assertRaises(TypeError, lambda: setattr(self.r, 'height', "height"))
        self.assertRaises(TypeError, lambda: setattr(self.r, 'x', "x"))
        self.assertRaises(TypeError, lambda: setattr(self.r, 'y', "y"))

    def test_area(self):
        """
            Test case for area method
        """
        self.assertEqual(self.r.area(), 200)

    def test_update(self):
        """
            Test case for the update method
        """
        self.r.update(10, 10, 10, 10)
        self.assertEqual(self.r.id, 10)
        self.assertEqual(self.r.height, 10)
        self.r.update(89, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.y, 3)

    def test_to_dictionary(self):
        """
            Test case for the to_dictionary method
        """
        expected = {'id': 99, 'width': 10, 'height': 20,
                    'x': 5, 'y': 5}
        self.assertEqual(self.r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
