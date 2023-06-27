#!/usr/bin/python3
"""
define a classe with private attribute
"""


class Square:
    """a classe def for a sqr"""
    def __init__(self, size=0):
        """initialization size: int and it's the unit length of the square
        """
        self.__size = size

    @property
    def size(self):
        """we retrieving the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """protect the value from bad"""
        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
