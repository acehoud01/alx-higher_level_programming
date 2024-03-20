#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    init_dictionary = a_dictionary.copy()
    for key, value in list(init_dictionary.items()):
        init_dictionary[key] = value * 2
    return init_dictionary
