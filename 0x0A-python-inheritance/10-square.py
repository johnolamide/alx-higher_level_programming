#!/usr/bin/python3
""" Module contains class definition for Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square: defines a square

        Args:
            size: size of the square

        Methods:
            __init__: initializes the size class
            area: calculates the size area
    """

    def __init__(self, size):
        """ Initializes the size class

            Args:
                size: size
        """
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculates the area of the square

            Returns:
                area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
