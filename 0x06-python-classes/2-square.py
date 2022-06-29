#!/usr/bin/python3
"""Square class based 0-square"""


class Square:
    """define Square class"""
    def __init__(self, size=0):
        """initialize Square size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
