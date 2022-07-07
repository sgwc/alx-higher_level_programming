#!/usr/bin/python3
"""Module write object with json
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a
    text file, using a JSON representation
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
