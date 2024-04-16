#!/usr/bin/python3
'''
0-read_file.py
'''

def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
