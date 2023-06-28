#!/usr/bin/python3
""" Module contains: square class definition"""


class Square:
    """
        Square: defines a square class
        Args:
            size: size of the square
            position: position of the square
        Methods:
            __init__: initialize the square class
            size: getter for size attribute
            size(value): setter for size attribute
            position: getter for position attribute
            position(value): setter for position attribute
            area: calculates the area of the square
            my_print: prints square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the Square class
            Args:
                size: size of the Square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Getter for position attribute
            Returns:
                value of position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for position attribute
            Args:
                value: value for position
        """
        for v in value:
            if v < 0:
                raise TypeError("position must be a tuple"
                                "of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area for the square
            Returns:
                area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
