#!/usr/bin/python3
"""
define a classe with private attribute
"""


class Square:
    """a classe def for a sqr"""
    def __init__(self, size):
        """initialization size: int and it's the unit length of the square
        """
        self.__size = size
