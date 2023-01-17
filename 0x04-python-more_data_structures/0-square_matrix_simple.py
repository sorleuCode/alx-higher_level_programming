#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        for col in row:
            new_matrx = list(map(lambda col: col ** 2, row))
    return new_matrx
