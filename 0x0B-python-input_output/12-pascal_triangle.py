#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows in the Pascal's triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        new_row = [1]
        for j in range(1, i):
            new_value = triangle[i-1][j-1] + triangle[i-1][j]
            new_row.append(new_value)
        new_row.append(1)
        triangle.append(new_row)

    return triangle
