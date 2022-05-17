#!/usr/bin/python3
"""task 4"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """size init"""
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area func"""
        a = self.__size * self.__size
        return a
