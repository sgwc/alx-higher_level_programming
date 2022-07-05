#!/usr/bin/python3

"""Write an class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle but makes a square
    """

    def __init__(self, size):
        """Initializes a square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Prints a designated output to define square
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
