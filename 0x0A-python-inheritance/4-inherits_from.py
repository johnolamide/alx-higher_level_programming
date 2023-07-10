#!/usr/bin/python3
""" Module contains the function definition of inherits_from
"""


def inherits_from(obj, a_class):
    """ checks if the object is an instance of a class that inherited
    directly or indirectly from the specified class

        Args:
            obj: object to check
            a_class: class to check

        Returns:
            True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
