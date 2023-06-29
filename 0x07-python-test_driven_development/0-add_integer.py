#!/usr/bin/python3
"""
    Module contains: function to add two integers
"""


def add_integer(a=None, b=98):
    """ Function that adds two integers

    Args:
        a (integer or float): first variable
        b (integer or float): second variable (default 98)

    Returns:
        the addition of a and b

    Raises:
        TypeError: if type is neither an integer or float
        ValueError: if no arguments are passed
    """
    if a is None:
        raise ValueError("at least one argument must be provided")
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
