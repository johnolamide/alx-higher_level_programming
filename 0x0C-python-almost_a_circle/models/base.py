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
            from_json_string(json_string): returns the list ofdictionaries
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

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of dictionaries from a JSON string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)
