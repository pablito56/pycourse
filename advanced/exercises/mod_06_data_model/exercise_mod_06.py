#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 06 (data model & customisation) exercise: customise CustomOrderedDict, AttrDict and Fraction
"""
#===============================================================================
# EXERCISE: advanced/exercises/mod_06_data_model/exercise_mod_06.py
#
# - Implement slicing and + and - operators in CustomOrderedDict
#    - __getslice__ is deprecated by __getitem__ passing an slice object
# - Modify AttrDict to access the dictionary ONLY if key already exists,
#    otherwise act as with normal attributes
# - Implement all required methods of Fraction to customise:
#    - Full rich comparisson with Fractions and other numbers
#    - + and * operator with Fractions and other numbers
#    - Index access to numerator and denominator (0 and 1)
#    - Key access to numerator and denominator ("num" and "den")
#    - Length (always 2)
# - http://docs.python.org/2.7/reference/datamodel.html
#
# - Run the tests in 'tests_mod_06.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_06.py'
#===============================================================================


from collections import OrderedDict


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        return OrderedDict.__getitem__(self, key)


class AttrDict(dict):
    def __getattr__(self, name):
        '''Called when an attribute lookup has not found the attribute in the usual places
        '''
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        '''Called when an attribute assignment is attempted
        '''
        self[name] = value

    def __delattr__(self, name):
        '''Called when an attribute deletion is attempted
        '''
        del self[name]


class Fraction(object):
    def __init__(self, numerator, denominator):
        self._num = int(numerator)
        self._den = int(denominator)

    def value(self):
        return float(self._num) / self._den
