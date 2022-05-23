#!/usr/bin/python3
"""task 2"""


def matrix_divided(matrix, div):
    """matrix division"""
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    if type(matrix) is set or type(matrix) is tuple:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    for ch in matrix:
        if len(ch) == 0:
            raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        if type(ch) == set or type(ch) == tuple:
            raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    leng = len(matrix[0])
    for hh in range(len(matrix)):
        if len(matrix[hh]) != leng:
            raise TypeError("Each row of the matrix must have the same size")
        for kk in range(len(matrix[hh])):
            if type(matrix[hh][kk]) != int and type(matrix[hh][kk]) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for nn in matrix:
        new.append(list(map(lambda x: round(x / div, 2), nn)))
    return new
