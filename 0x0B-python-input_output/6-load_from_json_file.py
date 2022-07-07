#!/usr/bin/python3
"""Module create obj from json
"""
import json


def load_from_json_file(filename):
    """function that creates an object
    from a "JSON file"
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            new = json.loads(line)
    return new
