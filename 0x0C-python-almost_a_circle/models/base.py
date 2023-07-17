#!/usr/bin/python3
""" Module contains the class definition of Base
"""
import json


class Base:
    """
        Base: base model
        Attributes:
            __nb_objects: number of objects
            id (int): instance id
        Methods:
            __init__: initialize the class
            to_json_string(list_dictionaries): returns JSON representation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize the Base Class
            Args:
                id (int): instance id
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns JSON representation
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
