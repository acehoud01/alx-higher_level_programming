#!/usr/bin/python3
"""Base module."""

import json


class Base:
    """Base class for all models in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes set from the dictionary."""
        if cls.__name__ == 'Rectangle':
            if 'width' not in dictionary or 'height' not in dictionary:
                raise ValueError("width and height must " +
                                 "be provided for Rectangle")
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            if 'size' not in dictionary:
                raise ValueError("size must be provided for Square")
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class type")
        dummy.update(**dictionary)
        return dummy
