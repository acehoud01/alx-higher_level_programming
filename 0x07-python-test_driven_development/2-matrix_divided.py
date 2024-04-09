#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by the given divisor.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The divisor (cannot be 0).

    Returns:
        list of lists: A new matrix with elements divided by div
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
