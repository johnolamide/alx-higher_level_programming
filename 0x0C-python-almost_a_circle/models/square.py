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


if __name__ == '__main__':
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
