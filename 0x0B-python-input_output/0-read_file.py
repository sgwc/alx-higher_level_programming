#!/usr/bin/python3
"""Module read a file
"""


def read_file(filename=""):
    """function that reads a text file (UTF-8)
    and prints it to the stdout
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
