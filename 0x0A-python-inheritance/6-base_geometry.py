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


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
