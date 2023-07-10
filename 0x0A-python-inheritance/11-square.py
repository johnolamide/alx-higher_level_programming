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
            __str__: string representation of the object
            area: calculates the size area
    """

    def __init__(self, size):
        """ Initializes the size class

            Args:
                size: size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ String representation of the object

            Returns:
                str: string representation
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

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
