#!/usr/bin/python3
"""task 7"""


class BaseGeometry:
    """Class"""
    pass

    def area(self):
        """area func"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """func"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
