#!/usr/bin/python3
"""Base module."""

import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dict_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries represented by JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
