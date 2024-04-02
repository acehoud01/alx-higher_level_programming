#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        sys.stderr.write(f"Exception: {ex}\n")
        return None
