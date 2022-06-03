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

    def update(self, *args, **kwargs):
        """update func"""
        if (args is not None and len(args) > 0):
            count = 0
            for i in args:
                if count == 0:
                    self.id = i
                if count == 1:
                    self.size = i
                if count == 2:
                    self.x = i
                if count == 3:
                    self.y = i
                count += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """to dic"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
