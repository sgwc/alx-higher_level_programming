#!/usr/bin/python3
"""
Class REctangle
"""


from models.base import Base


class Rectangle(Base):
    """ clase Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance initialization method

        args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args):
        """ update attributes """
        listme = ['id', 'width', 'height', 'x', 'y']
        i = 0
        for arg in args:
            setattr(self, listme[i], arg)
            i += 1

    def area(self):
        """ computes area of the rectangle """
        return self.width * self.height

    def display(self):
        """ prints the rectangle """
        for y in range(self.y):
            print()
        for col in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print method"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    @property
    def width(self):
        """width getter methond"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height setter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        self.integer_validator('highet', value)
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.integer_validator2('y', value)
        self.__y = value