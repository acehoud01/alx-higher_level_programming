#!/usr/bin/python3
'''
4-from_json_string.py
'''


def from_json_string(my_str):
    """
    Returns a Python object decoded from a JSON string.
    """
    return json.loads(my_str)
