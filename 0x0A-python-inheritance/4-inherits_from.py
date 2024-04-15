#!/usr/bin/python3
'''
4-inherits_from.py
'''


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class; otherwise, returns False.
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
