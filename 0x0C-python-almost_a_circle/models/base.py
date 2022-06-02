#!/usr/bin/python3
"""Class Base"""


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inisialization"""
        if id is not None:
            self.id = id
        else:
            Base__nb_objects += 1
            self.id = Base.__nb_objects

