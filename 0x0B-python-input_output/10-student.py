#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method Retrieves a dictionary
        representation of a Student instance"""
        my_dict = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict
