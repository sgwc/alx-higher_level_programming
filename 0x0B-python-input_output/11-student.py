#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method to retrieve a dictionary representation
            of a student instance
        """
        if attrs is not None:
            dict_student = {}
            for k in self.__dict__:
                if k in attrs:
                    dict_student[k] = self.__dict__[k]
            return dict_student
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): instance dictionary
        """
        if json:
            self.__dict__ = json
