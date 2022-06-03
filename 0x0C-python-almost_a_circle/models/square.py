#!/usr/bin/python3
"""Class Sqaure"""
from .rectangle import Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """str func"""
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width))
