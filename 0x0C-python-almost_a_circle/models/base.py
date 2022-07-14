#!/usr/bin/python3
"""
Class base Module
"""

import json


class Base:
    """ base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validator2(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dict"""
        return json.dumps(list_dictionaries or [])
