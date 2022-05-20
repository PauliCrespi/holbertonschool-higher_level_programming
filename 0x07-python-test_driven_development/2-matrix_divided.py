#!/usr/bin/python3
"""task 2"""


def matrix_divided(matrix, div):
    """matrix division"""
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix) is not tuple and type(matrix) is not set:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div <= 0:
        raise ZeroDivisionError("division by zero")

