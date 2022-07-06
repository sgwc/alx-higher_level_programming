#!/usr/bin/python3
"""Module that append a string to a text file
"""


def append_write(filename="", text=""):
    """function that writes a text file (UTF-8)
    """
    with open(filename, 'a', encoding="utf-8") as f:
        characters = f.write(text)
        return(characters)
