#!/usr/bin/python3
"""checking object"""


def inherits_from(obj, a_class):
    """checking  if the object is an instance of
    a class that inherited
    (directly or indirectly) from the specified class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
