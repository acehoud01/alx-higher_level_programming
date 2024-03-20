#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, gld in sorted(a_dictionary.items()):
        if gld == value:
            del a_dictionary[key]
    return a_dictionary
