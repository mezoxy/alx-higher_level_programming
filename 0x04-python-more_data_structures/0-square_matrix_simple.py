#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        x = list(map(lambda v: v ** 2, i))
        new.append(x)
    return new
