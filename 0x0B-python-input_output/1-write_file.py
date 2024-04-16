#!/usr/bin/python3
'''
1-write_file.py
'''


def write_file(filename="", text=""):
    """
    Writes the given string to a text file (UTF-8 encoded)
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)
