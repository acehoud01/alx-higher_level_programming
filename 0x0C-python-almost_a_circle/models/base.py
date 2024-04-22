#!/usr/bin/python3
'''
Module for base class
'''

class Base:
    """Base class for managing id attribute and object count."""

    __nb_objects = 0  # Private class attribute for object count

    def __init__(self, id=None):
        """
        Initializes the Base class instance.

        Args:
            id (int, optional): An optional integer ID for the object.
                If not provided, a new unique ID is assigned. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
