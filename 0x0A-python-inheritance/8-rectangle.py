#!/usr/bin/python3
"""task 8"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class"""

class Rectangle(BaseGeometry):
    """Class"""

    def __init__(self, width, height):
        """f"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
