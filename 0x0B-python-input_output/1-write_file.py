#!/usr/bin/python3
"""Module write a string to a text file
"""


def write_file(filename="", text=""):
    """function that writes a text file (UTF-8)
    """
    with open(filename, 'w', encoding="utf-8") as f:
        characters = f.write(text)
        return(characters)
