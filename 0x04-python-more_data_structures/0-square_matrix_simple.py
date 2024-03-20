#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    init_matrix = matrix.copy()
    for row in range(len(init_matrix)):
        init_matrix[row] = list(map(lambda x: x ** 2, init_matrix[row]))
    return init_matrix
