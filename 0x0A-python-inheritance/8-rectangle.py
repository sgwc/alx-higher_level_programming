#!/usr/bin/python3

"""Write an class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the subclass
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
