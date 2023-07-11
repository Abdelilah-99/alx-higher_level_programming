#!/usr/bin/python3
"""writes an Object to a text file
, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """dump"""
    with open(filename, "w") as a_file:
        return json.dump(my_obj, a_file)
