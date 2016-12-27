#!/usr/bin/env python
#coding=utf-8

"""This is python lesson"""

def start_func(arg):
    """This is a function."""
    pass

class Myclass(object):
    """This is my class."""
    
    def my_method(self, arg):
        """This is my methond"""
        pass
        
print __doc__
print start_func.__doc__
print Myclass.__doc__
print Myclass.my_method.__doc__
