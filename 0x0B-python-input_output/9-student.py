#!/usr/bin/python3
"""Module create class student
"""


class Student():
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """initalitation method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary
        representation of a Student instance
        """
        return vars(self)
