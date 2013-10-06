#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 3, 2013

@author: ealogar

@license: MIT

@contact: ealogar@gmail.com

Module 10 (metaclasses) exercise: apply decorators with metaclasses and generate new functionality
"""
from time import sleep, time
from random import randint
from functools import wraps
from re import search
from inspect import isfunction, getmembers, ismethod
from copy import copy
from types import MethodType


def measure(f):
    """Simple decorator to measure the execution time of a member function
    It will add the last time as an attribute of the object.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time()
        try:
            res = f(*args, **kwargs)
        except Exception as e:
            res = None
        t1 = time()
        ellapsed_time = t1 - t0
        # make ellapsed_time available in object as an attribute __time_<method_name>
        time_internal_var = '__time_{0}'.format(f.__name__)
        setattr(args[0], time_internal_var, ellapsed_time)
        # bind a function to return ellapsed time of a method

        def ellapsed_time(obj):
            return getattr(obj, time_internal_var, 'na')

        wrapper.last_time = MethodType(ellapsed_time, args[0])
        if res:
            return res
        else:
            raise e
    return wrapper


def show_execution_time(obj):
    """print by console the attribute last_time of every
    methods of obj who has it available
    """
    for method in getmembers(obj, ismethod):
        if not search(r'^__*', method[0]):
            print 'Method {0} - last execution time {1}'.format(method[0],
                                    getattr(obj, '__time_{0}'.format(method[0]), 'Na'))


class MeasureMetaclass(type):
    """Metaclass to add measures to every method of a class using measure
    decorator.
    It makes available show_execution_time
    e.g:
    >>my_class = SomeClass()
    >>my_class.get_fruits()
    >>my_class.get_dries_fruits()
    >>my_class.show_execution_time()

    """

    def __new__(meta, classname, supers, classdict):  # @NoSelf
        for attr, attrval in classdict.items():
            if isfunction(attrval) and not search(r'^__*', attr):
                classdict[attr] = measure(attrval)
        # bind a function to the class to show all measure times
        classdict['show_execution_time'] = show_execution_time
        return type.__new__(meta, classname, supers, classdict)


class SomeClass(object):

    __metaclass__ = MeasureMetaclass

    def __init__(self):
        self.fruits = ['apple', 'peach', 'banana', 'strawberry']
        self.dried_fruits = ['peanut', 'nouse', 'almond']

    def get_fruits(self):
        sleep(0.01)  # getting is quick ...
        return copy(self.fruits)

    def add_fruit(self, fruit):
        if fruit not in self.get_fruits():
            sleep(0.1)  # inserting is expensive
            self.fruits.append(fruit)

    def delete_fruit(self, fruit):
        if fruit in self.get_fruits():
            sleep(0.2)
            del self.fruits[fruit]

    def get_dries_fruits(self):
        sleep(randint(0, 100) / 100)
        return copy(self.dried_fruits)
