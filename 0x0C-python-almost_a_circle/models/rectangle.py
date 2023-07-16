#!/usr/bin/python3
""" Module contains the class definition of the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle: Rectangle class
        Attributes:
            __width (int): width
            __height (int): height
            __x (int): x position
            __y (int0: y position
        Methods:
            __init__: initialize the Rectangle class
            width: getter for the width attribute
            width(value): setter for the width attribute
            height: getter for the height attribute
            height(value): setter for the height attribute
            x: getter for the x attribute
            x(value): setter for the x attribute
            y: getter for the y attribute
            y(value): setter for the y attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize the Rectangle class
            Args:
                width (int): the width of the rectangle
                height (int): the height of the rectangle
                x (int): the x position of the rectangle
                y (int): the y position of the rectangle
                id: instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter for the width attribute
            Returns:
                the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for the width attribute
            Args:
                value (int): width value
        """
        self.__width = value

    @property
    def height(self):
        """
            Getter for the height attribute
            Returns:
                the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter for the height attribute
            Args:
                value (int): height value
        """
        self.__height = value

    @property
    def x(self):
        """
            Getter for the x attribute
            Returns:
                the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter for the x attribute
            Args:
                value (int): x value
        """
        self.__x = value

    @property
    def y(self):
        """
            Getter for the y attribute
            Returns:
                the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter for the y attribute
            Args:
                value (int): y value
        """
        self.__y = value


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
