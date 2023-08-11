#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class BaseGeometry:
    ''' 
    Class: BaseGeometry
    '''

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item is "__init__subclass__"]
        return new_attribute_list
