#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """raising"""
    def area(self):
        """raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raising TypeError & ValueError"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
