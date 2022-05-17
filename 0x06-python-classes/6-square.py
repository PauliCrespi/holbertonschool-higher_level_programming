#!/usr/bin/python3
"""task 6"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """self"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return(self.__position)

    @size.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int) or (value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[1]) != int) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area func"""
        a = self.__size * self.__size
        return a

    def my_print(self):
        """print func"""
        if self.__size == 0:
            print("")
        for p in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for n in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
