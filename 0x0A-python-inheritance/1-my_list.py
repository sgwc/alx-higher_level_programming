#!/usr/bin/python3
"""class MyList that inherits from the list
"""


class MyList(list):
    """ class MyList inherits from the list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
