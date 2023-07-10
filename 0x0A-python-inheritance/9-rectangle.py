#!/usr/bin/python3
""" Module contains class definition for Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle: defines a rectangle

        Args:
            width: width
            height: height

        Methods:
            __init__: initializes the rectangle class
            __str__: string representation of the object
            area: calculates the rectangle area
    """

    def __init__(self, width, height):
        """ Initializes the rectangle class

            Args:
                width: width
                height: height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ string representation of the object

            Returns:
                str: string reresentation of the object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Calculates the area of the rectangle

            Returns:
                area of the rectangle
        """
        return self.__height * self.__width


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
