#!/usr/bin/python3
"""This is sum function
"""

def add_integer(a, b=98):
    """function that adds 2 integers."""

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
