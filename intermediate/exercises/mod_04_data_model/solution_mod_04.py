#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Module 06 (data model & customisation) exercise: solution
"""
#===============================================================================
# EXERCISE: advanced/exercises/mod_04_data_model/exercise_mod_04.py
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
# - Run the tests in 'tests_mod_04.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_04.py'
#===============================================================================


from collections import OrderedDict


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        """Item access or slicing, returns new instance
        """
        if isinstance(key, slice):
            return self.__class__(self.items()[key])
        return OrderedDict.__getitem__(self, key)

    def __add__(self, other):
        """Overloading of + operator, in place modification returning itself
        """
        res = self.__class__(self)
        res.update(other)
        return res

    def __sub__(self, other):
        """Overloading of - operator, in place modification returning itself
        """
        res = self.__class__(self)
        [res.pop(k, None) for k in other]
        return res


class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        else:
            # self.__dict__[name] = value  # Perform action instead of delegating
            dict.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            # del self.__dict__[name]  # Perform action instead of delegating
            dict.__delattr__(self, name)


class Fraction(object):
    def __init__(self, numerator, denominator):
        self._num = int(numerator)
        self._den = int(denominator)

    def value(self):
        return float(self._num) / self._den

    def __lt__(self, other):
        '''Called to implement evaluation of self < other
        '''
        try:
            return self.value() < other.value()
        except AttributeError:
            return self.value() < other

    def __le__(self, other):
        '''Called to implement evaluation of self <= other
        '''
        try:
            return self.value() <= other.value()
        except AttributeError:
            return self.value() <= other

    def __eq__(self, other):
        '''Called to implement evaluation of self == other
        '''
        try:
            return self.value() == other.value()
        except AttributeError:
            return self.value() == other

    def __ne__(self, other):
        '''Called to implement evaluation of self != other
        '''
        try:
            return self.value() != other.value()
        except AttributeError:
            return self.value() != other

    def __gt__(self, other):
        '''Called to implement evaluation of self > other
        '''
        try:
            return self.value() > other.value()
        except AttributeError:
            return self.value() > other

    def __ge__(self, other):
        '''Called to implement evaluation of self >= other
        '''
        try:
            return self.value() >= other.value()
        except AttributeError:
            return self.value() >= other

    def __str__(self):
        '''Called by the str() and print to compute the “informal” string representation
        '''
        return "{0}/{1}".format(self._num, self._den)

    def __len__(self):
        '''Called to implement the built-in function len()
        '''
        return 2

    def __getitem__(self, key):
        '''Called to implement evaluation of self[key]
        '''
        if key == 0 or key == 'num':
            return self._num
        elif key == 1 or key == 'den':
            return self._den
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        '''Called to implement assignment of self[key] = value
        '''
        if key == 0 or key == 'num':
            self._num = value
        elif key == 1 or key == 'den':
            self._den = value
        else:
            raise KeyError(key)

    def __add__(self, other):
        '''Called to implement the binary arithmetic operation self + other
        '''
        try:
            if self._den == other._den:
                return Fraction(self._num + other._num, self._den)
            else:
                return Fraction(self._num * other._den + other._num * self._den, self._den * other._den)
        except AttributeError:
            return Fraction(self._num + other * self._den, self._den)

    __radd__ = __add__

    def __mul__(self, other):
        '''Called to implement the binary arithmetic operation self * other
        '''
        try:
            return Fraction(self._num * other._num, self._den * other._den)
        except AttributeError:
            return Fraction(self._num * other, self._den)

    __rmul__ = __mul__
