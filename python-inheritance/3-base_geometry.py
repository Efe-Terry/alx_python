#!/usr/bin/python3

"""
This is an empty BaseGeometry class.
"""

class BaseMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=BaseMetaClass):

    ''' 
    Class: BaseGeometry
    '''

    def __dir__(cls):
        '''
        This is to exclude an attribute from printing
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

