#!/usr/bin/python3
""" Module contains the class definition of BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry: defines a geometry class
        Args:

        Methods:
            __init__: initialize the class
            area: calculates the area
            integer_validator(name, value): validates value

    """
    def __init__(self):
        """ Initializes the BaseGeometry Class
        """
        pass

    def area(self):
        """ calculates the area of the geometry

            Raises:
                Exception: not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value

            Args:
                name(str): name
                value(int): integer value

            Raises:
                TypeError: if value is not an integer
                ValueError: if value is less than or equal to 0
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
