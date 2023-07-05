#!/usr/bin/python3
"""returning sum of two int"""


def add_integer(a, b=98):
    """check if the value are not int or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    return a + b
