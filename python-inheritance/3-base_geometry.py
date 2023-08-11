#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class BaseGeometry:
    ''' 
    Class: BaseGeometry
    '''

    pass

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
