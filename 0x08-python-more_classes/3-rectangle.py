#!/usr/bin/python3
""" Module contains: recangle class definition
"""


class Rectangle:
    """
        Rectangle: defines a rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Methods:
            __init__: initialize the rectangle class
            width: getter for the width attribute
            width(value): setter for the width attribute
            height: getter for the height attribute
            height(value): setter for the height attribute
            perimeter: returns the perimeter of the rectangle
            area: returns the area of the rectangle
            __str__: A string representation of the object
            __repr__: A string representation of the object that
                     can be used to recreate it
    """
    def __init__(self, width=0, height=0):
        """ Initialize the rectangle class
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the width attribute
            Returns:
                the value of the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute
            Args:
                value (int): value of the width attribute
            Raises:
                TypeError: if width is not an integer
                ValueError: if width is less than 0
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute
            Returns:
                the value of the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute
            Args:
                value (int): value of the height attribute
            Raises:
                TypeError: if height is not an integer
                ValueError: if height is less than 0
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of the rectangle
            Returns:
                the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """ Calculates the perimeter of the rectangle
            Returns:
                the perimeter of the rectangle
        """
        if (self.height == 0 or self.width == 0):
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """ Returns a human-readable string representation of
        the object
            Returns:
                str: A string representation of the object
        """
        if (self.width == 0 or self.height == 0)
            return ""
        result = []
        for i in range(self.height):
            result.append("#" * self.width)
        return '\n'.join(result)

    def __repr__(self):
        """ Returns a string that can be used to recreate
        the object.
        Returns:
            str: A string representation of the object that can
            be used to recreate it
        """
        class_name = self.__class__.__name__
        object_id = hex(id(self))
        return "<3-rectangle.{} object at {}>".format(class_name, object_id)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}"
          .format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
