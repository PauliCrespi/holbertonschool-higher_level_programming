#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """pascale"""
    new = []
    lst = []
    if n <= 0:
        return new
    for x in range(n):
        new = [1]
        if x > 0:
            for i in range(x):
                new.append(sum(lst[-1][i:i+2]))
        lst.append(new)
    return (lst)
