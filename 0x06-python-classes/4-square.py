#!/usr/bin/python3
""" Module contains: square class definition"""


class Square:
    """
        Square: defines a square class
        Args:
            size: size of the square
        Methods:
            __init__: initialize the square class
            size: getter for size attribute
            size(value): setter for size attribute
            area: calculates the area of the square
    """
    def __init__(self, size=0):
        """ Initialize the Square class
            Args:
                size: size of the Square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter for size attribute
            Returns:
                value of size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size attribute
            Args:
                value: value for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area for the square
            Returns:
                area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
