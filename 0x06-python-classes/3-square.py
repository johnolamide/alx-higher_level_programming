#!/usr/bin/python3
""" Module contains: definition for a Square class"""


class Square:
    """
        Square: defines a square class
        Args:
            size: size of the square
        Methods:
            __init__: initializes the square class
            area: calculate the area of the square
    """
    def __init__(self, size=0):
        """ Initialize the square class
            Args:
                size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area of the square
            Returns:
                size raised to power 2
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
