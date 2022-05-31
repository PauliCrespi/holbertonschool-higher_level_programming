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


class Rectangle(BaseGeometry):
        """Class"""

    def __init__(self, width, height):
        """f"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
