#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 06 (cooperative super call pattern) exercise: apply cooperative super call pattern
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_06_super/exercise_mod_06
#
# - Implement all needed changes to let the tests pass. In particular, implement AmazingDict:
#    - Access keys as attributes only if they already exist
#    - Lower attributes and key names for query or modification
#    - Convert attributes or keys datetime values to strings when they are modified
#    - Print all attributes and keys accesses for query or modification
# - Check: http://docs.python.org/2/reference/datamodel.html?highlight=__contains__#object.__contains__
#
# - Run the tests in 'tests_mod_06.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_06.py'
#===============================================================================


from datetime import datetime


class Lower(object):
    '''Lower attributes and key names for query or modification
    '''
    def __getattribute__(self, name):
        return super(Lower, self).__getattribute__(name.lower())

    def __getitem__(self, key):
        return super(Lower, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setitem__(key.lower(), value)

    def __getattr__(self, name):
        return super(Lower, self).__getattr__(name.lower())

    def __setattr__(self, name, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setattr__(name.lower(), value)


class Attr(object):
    '''Access keys as attributes only if they already exist
    '''
    def __getattr__(self, name):
        try:
            return super(Attr, self).__getitem__(name)
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            super(Attr, self).__setitem__(name, value)
        else:
            super(Attr, self).__setattr__(name, value)


class Verbose():
    '''Print all attributes and keys accesses for query or modification
    '''
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(Verbose, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(Verbose, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(Verbose, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(Verbose, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(Verbose, self).__setattr__(name, value)


class DateStr(object):
    '''Convert attributes or keys datetime values to strings when they are modified
    '''
    def __setitem__(self, key, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setitem__(key, value)

    def __setattr__(self, name, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setattr__(name, value)


class AmazingDict(DateStr, Lower, dict):
    '''Dictionary with amazing enhanced behaviour:
    - Access keys as attributes only if they already exist
    - Lower attributes and key names for query or modification
    - Convert attributes or keys datetime values to strings when they are modified
    - Print all attributes and keys accesses for query or modification
    '''
    pass
