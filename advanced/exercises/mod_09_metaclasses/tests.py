#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 09 (cooperative super call pattern) exercise: apply cooperative super call pattern
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_09_metaclasses/exercise_mod_09
#
# - Combine a metaclass with a decorator:
#    - We want to measure the execution time of all class methods (excluding __* methods)
#    - Implement a decorator as a function to measure the execution time of a function
#    - Add the execution time to the decorated function as an attribute
#    - Instead of decorating the class, we decorate in metaclass __new__ method every function
#    - We can decide which methods to decorate and which not
#    - Add a function or attributes to show last_execution_time of every method
#    - We can store the execution time in the decorator as an attribute...
#    - We can use metaclass to add methods and attributes
#
# - Run the tests in 'tests.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution.py'
#===============================================================================


import unittest
from inspect import ismethod
import exercise as src
# import solution as src


class TestNewMethod(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True

    def test_new_method_is_added_with_metaclas(self):
        """Check that a method called 'show_execution_time' is added
        """
        my_obj = src.SomeClass()
        self.assertTrue(hasattr(my_obj, 'show_execution_time'))
        self.assertTrue(ismethod(my_obj.show_execution_time))

    def test_method_called_has_exec_time_available(self):
        """Check how execution time is measured
        """
        my_obj = src.SomeClass()
        my_obj.get_fruits()
        self.assertTrue(hasattr(my_obj, '_time_get_fruits'))
        time_internal = getattr(my_obj, '_time_get_fruits')
        time_in_method = my_obj.get_fruits.last_time()
        self.assertEquals(time_internal, time_in_method, 'last time not availble')

    def test_different_objects_has_different_times(self):
        """Check that two different instances do not share measured execution time
        """
        my_obj = src.SomeClass()
        my_obj.get_fruits()
        another_obj = src.SomeClass()
        another_obj.get_fruits()
        self.assertNotEquals(getattr(my_obj, '_time_get_fruits', 0),
                             getattr(another_obj, '_time_get_fruits', 0),
                             'Two instances are sharing times')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
