#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class BaseGeometryMeta(type):
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=BaseGeometryMeta):
    ''' 
    Class: BaseGeometry
    '''

    pass
