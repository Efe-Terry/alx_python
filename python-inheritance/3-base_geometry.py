#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class NoInitSubclassMeta(type):
    def __init__(cls, name, bases, attrs):
        if '__init_subclass__' in attrs:
            del attrs['__init_subclass__']
        super().__init__(name, bases, attrs)

class BaseGeometry(metaclass=NoInitSubclassMeta):
    ''' 
    Class: BaseGeometry
    '''

    pass
