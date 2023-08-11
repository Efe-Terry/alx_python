#!/usr/bin/python3

"""@BaseGeometry class imported"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):

    """Represent a rectangle using BaseGeometry."""

    def __dir__(cls):

        '''
        This is to exclude an attribute from printing
        '''

        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def __init__(self, width, height):

        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
