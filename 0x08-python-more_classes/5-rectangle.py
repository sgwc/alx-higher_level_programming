#!/usr/bin/python3
"""Write Rectangle that defines
    a rectangle by (based on 0-rectangle)"""


class Rectangle:
    """Class Rectangle 0-rectangle"""
    def __init__(self, width=0, height=0):
        '''Initializes the method'''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints in stdout the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle ...")
