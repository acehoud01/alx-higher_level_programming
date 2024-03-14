#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")
