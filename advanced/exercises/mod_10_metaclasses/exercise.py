#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 3, 2013

@author: ealogar

@license: MIT

@contact: ealogar@gmail.com

Module 10 (metaclasses) exercise: apply decorators with metaclasses and generate new functionality
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_10_metaclasses/exercise_mod_10
#
# - Combine a metaclass with a decorator:
#    - We want to measure the execution time of all class methods (excluding _* methods)
#    - Implement a decorator as a function to measure the execution time of a function
#    - Add the execution time to the decorated function as an attribute
#    - Instead of decorating the class, we decorate in metaclass __new__ method every function
#    - We can decide with methods to decorate and which not
#    - Add a function or attributes to show last_execution_time of every method
#    - We can store the execution time in the decorator as an attribute...
#    - We can use metaclass to add methods and attributes
# - Check: Learning python fourth edition (chapters 38 and 39)
#
# - It's common to generate code with metaclasses based on simple classes (e.g. django)
#
# - Check the solution in module 'solution.py'
#===============================================================================

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
        # TODO: get time here

        # TODO: call the function being decorated: f

        # TODO: get ellapsed time here

        # TODO: make ellapsed_time available in object as an attribute __time_<method_name>
        time_internal_var = '__time_{0}'.format(f.__name__)
        setattr()  # Hint: args[0] is the object (self)

        def ellapsed_time(obj):
            return getattr(obj, time_internal_var, 'na')

        # TODO: Change None
        # update wrapper and bind ellapsed_time as a method
        # Hint: use MethodType to bind functions to instances
        wrapper.last_time = None

        # TODO: Here you must provide code to return the result of decorated function
        return
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
            # TODO: Decorate class methods not beginning with __
            # @decorator
            # function
            # is same that decorator(function)
            # hint use isfunction ...
            pass

        # TODO: bind show_execution_time provide to the class to show all measure times
        # you can add key, value to classdict (all class methods)

        return type.__new__(meta, classname, supers, classdict)


class SomeClass(object):

    # TODO: make SomeClass created with metaclass MeasureMetaclass

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
