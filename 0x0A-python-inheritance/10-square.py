#!/usr/bin/python3
"""making square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """prv attr"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
