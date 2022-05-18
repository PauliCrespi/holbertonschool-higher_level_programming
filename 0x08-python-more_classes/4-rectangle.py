#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area func"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter func"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """func print"""
        arr = ""
        if (self.__height == 0) or (self.__width == 0):
            return arr
        for h in range(self.__height):
            for w in range(self.__width):
                arr = arr + "#"
            if h != (self.__height - 1):
                arr = arr + "\n"
        return arr

    def __repr__(self):
        """repr func"""
        return("Rectangle(" + str(self.__width) + "\
, " + str(self.__height) + ")")
