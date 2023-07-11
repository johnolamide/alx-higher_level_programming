#!/usr/bin/python3
""" Module contains the function definition of class_to_json
"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.
        Args:
            obj: object
    """
    return obj.__dict__
