#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """raising exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
