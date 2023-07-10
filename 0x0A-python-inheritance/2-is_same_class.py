#!/usr/bin/python3
"""checking object"""
def is_same_class(obj, a_class):
    """checking if exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
