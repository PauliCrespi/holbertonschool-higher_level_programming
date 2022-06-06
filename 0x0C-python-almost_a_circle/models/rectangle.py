#!/usr/bin/python3
"""Class Rectangle"""


from .base import Base


class Rectangle(Base):
    """class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height muste be > 0")
        self.__height = value

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area func"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        for m in range(0, self.y):
            print("")
        for i in range(self.height):
            for k in range(0, self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """str func"""
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width) + "/" + str(self.height))

    def update(self, *args, **kwargs):
        """update func"""
        if (args is not None and len(args) > 0):
            count = 0
            for i in args:
                if count == 0:
                    self.id = i
                if count == 1:
                    self.width = i
                if count == 2:
                    self.height = i
                if count == 3:
                    self.x = i
                if count == 4:
                    self.y = i
                count += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """to dic"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
