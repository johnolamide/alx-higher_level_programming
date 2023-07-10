#!/usr/bin/python3
""" Module contains the function definition for 0-lookup
"""


def lookup(obj):
    """ Returns the list attrubutes and methods of an object
        Args:
            obj: object

        Returns:
            a list of attributes and methods
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
