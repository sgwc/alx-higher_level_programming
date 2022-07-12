#!/usr/bin/python3
"""
Class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """instance initialization method

        args:
            size: size of the squares side
            x: x position
            y: y position
            id: object id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print method """
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """width getter method
        return:
            size of width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        """ width and height setter method
        args:
            value: size value
        return:
            na
        """
        self.width = value
        self.height = value
