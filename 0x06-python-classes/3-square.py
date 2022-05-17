#!/usr/bin/python3
"""task 3"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """size init"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area func"""
        a = self.__size * self.__size
        return a
