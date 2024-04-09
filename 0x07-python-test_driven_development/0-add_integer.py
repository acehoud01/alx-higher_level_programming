#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    a (int or float): The first number to add. Must be an integer or float.
    b (int or float, optional): The second number to add.
    Must be an integer or float. Defaults to 98.

    Returns:
    int: The sum of a and b, after casting them to integers if they are floats.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
