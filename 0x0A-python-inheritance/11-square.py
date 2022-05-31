#!/usr/bin/python3
"""task 8"""

Rectangle = __import__('9-rectangle').Rectangle
"""import class"""


class Square(Rectangle):
    """Class"""

    def __init__(self, size):
        """f"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size

    def __str__(self):
        """str func"""
        return (f"[Square] {self.__size}/{self.__size}")
