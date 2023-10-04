#!/usr/bin/python3
"""This module """


def matrix_divided(matrix, div):
    """matrix_divided a function that divides all elements of a matrix.
    Args: List of lists(matrix) and div
    Return: A new matrix (new)
    """
    big_matrix = []
    small_matrix = []
    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if matrix == [] or matrix == [[]]:
        raise TypeError(str1)
    for i in matrix:
        small_matrix = []
        if not isinstance(i, list):
            raise TypeError(str1)
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not type(j) in [int, float]:
                raise TypeError(str1)
            else:
                small_matrix.append(round(j / div, 2))
        big_matrix.append(small_matrix)
    return big_matrix
