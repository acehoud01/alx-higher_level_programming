#!/usr/bin/python3
"""BaseGeometry.
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """
        Raises an exception with the message "area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the given value as int"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
