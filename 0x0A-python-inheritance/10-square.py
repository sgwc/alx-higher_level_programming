#!/usr/bin/python3

"""Write an class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """initial """
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)
