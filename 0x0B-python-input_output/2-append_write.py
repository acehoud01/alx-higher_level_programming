#!/usr/bin/python3
'''
2-append_write.py
'''


def append_write(filename="", text=""):
    """
    Appends the end to a text file (UTF-8 encoded)
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
