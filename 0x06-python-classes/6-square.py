#!/usr/bin/python3
"""
define a classe with private attribute
"""


class Square:
    """a classe def for a sqr"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization size: int and it's the unit length of the square
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """we retrieving the value"""
        return self.__position

    @position.setter
    def position(self, value):
        """protect the value from bad"""
        if not isinstance(value, tuple) or len(value) != 2 or any(type(x) is not int for x in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
