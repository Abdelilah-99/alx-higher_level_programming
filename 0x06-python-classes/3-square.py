#!/usr/bin/python3
"""
define a classe with private attribute
"""


class Square:
    """a classe def for a sqr"""
    def __init__(self, size=0):
        """initialization size: int and it's the unit length of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
