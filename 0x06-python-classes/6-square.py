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
        self.size = size
        self.position = position

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
        errorMessage = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple
           or len(value) != 2
           or type(value[0]) != int
           or type(value[1]) != int
           or value[0] < 0
           or value[1] < 0):
            raise TypeError(errorMessage)
        self.__position = value

    def area(self):
        """ Calculates the area for the square
            Returns:
                area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints square"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)


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
