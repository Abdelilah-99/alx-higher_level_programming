#!/usr/bin/python3
"""function that writes
 an Object to a text file,
using a JSON representation"""
import json


def class_to_json(obj):
    """class to json"""
    return json.dumps(obj.__dict__)
