#!/usr/bin/python3
"""
    Module contains: Square Class definition with size attribute
"""


class Square:
    """
        Square: defines a square
        Attributes:
            size: size of the square
        Method:
            __init__: initialize the Square class
    """

    def __init__(self, size):
        """ Initialize the Square class
            Args:
                size: size of the square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
