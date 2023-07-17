#!/usr/bin/python3
""" Module contains the class definition of Base
"""
import os
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
            save_to_file(cls, list_objs): writes JSON to a file
            from_json_string(json_string): returns the list ofdictionaries
            create(cls, **dicionary): creates a new instance
            load_from_file(cls): returns a list of instances from a file
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
            Args:
                list_dictionaries: dictionary of attributes
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save JSON to file
            Args:
                cls: class
                list_objs: list object
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of dictionaries from a JSON string
            Args:
                json_string: JSON string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Creates a new Base instance
            Args:
                cls: class
                dictionary: dictionary of attributes
        """
        dummy = cls(1, 1)

        # update the dummy instance with the dictionary values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances from a file
            Args:
                cls: class
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            list_dictionaries = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dictionaries]
