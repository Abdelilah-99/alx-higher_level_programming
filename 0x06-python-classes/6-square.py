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

    @property
    def position(self):
        """we retrieving the value"""
        return self.__position

    @position.setter
    def position(self, value):
        """protect the value from bad"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
