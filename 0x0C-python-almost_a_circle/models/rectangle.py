#!/usr/bin/python3
"""Rectangle class module"""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object with width,
        height, x-coordinate, y-coordinate, and an optional id."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
