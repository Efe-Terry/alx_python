#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""

class BaseMetaClass(type):
    
    '''
    Class: 
    '''
    
    def __dir__(cls):
        
        '''
        This is to exclude an attribute from printing
        '''

        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseMetaClass):   
"""Reprsent base geometry."""

    def __dir__(cls):

        '''
        This is to exclude an attribute from printing
        '''

        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
