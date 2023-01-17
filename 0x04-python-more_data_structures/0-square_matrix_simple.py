#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        return [list(map(lambda col: col ** 2, row))]
