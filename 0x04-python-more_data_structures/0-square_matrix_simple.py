#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        for col in row:
            return list(map(lambda col: col ** 2, new_matrix))
