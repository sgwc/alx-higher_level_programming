#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
