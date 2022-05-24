#!/usr/bin/python3
"""task 4"""


def print_square(size):
    """print square"""
    if size is None:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != size:
            print("")
