#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list containing the attributes and methods of the input object.
    """
    return dir(obj)
