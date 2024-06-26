#!/usr/bin/python3
""" Magic class """
import math


class MagicClass:
    """ Magic """
    def __init__(self, radius=0):
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ circumference """
        return (2 * math.pi * self.__radius)
