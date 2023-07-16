#!/usr/bin/python3
""" Module contains the Class definition of the Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square: defines a Square
        Attributes:
            size: size of the square
            x: x position
            y: y position
            id: id of the square instance
        Methods:
            __init__: initializes the Square class
            __str__: string representation of the Square instance
            size: getter for the size attribute
            size(value): setter for the size attribute
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the Square class
            Args:
                size (int): size of the Square instance
                x (int): x position of the instance
                y (int): y position of the instance
                id (int): id of the instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            String representation of the Square instance
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """
            Getter for the size attribute
            Returns:
                value for the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Setter for the size attribute
            Args:
                value: size value
        """
        self.width = value
        self.height = value


if __name__ == '__main__':
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
