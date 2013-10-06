#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module XY (cooperative super call pattern) exercise: apply cooperative super call pattern
"""
import unittest
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
        my_obj = src.SomeClass()
        self.assertTrue(hasattr(my_obj, 'show_execution_time'))

    def test_method_called_has_exec_time_available(self):
        my_obj = src.SomeClass()
        my_obj.get_fruits()
        self.assertTrue(hasattr(my_obj, '__time_get_fruits'))
        time_internal = getattr(my_obj, '__time_get_fruits')
        time_in_method = my_obj.get_fruits.last_time()
        self.assertEquals(time_internal, time_in_method, 'last time not availble')

    def test_different_objects_has_different_times(self):
        my_obj = src.SomeClass()
        my_obj.get_fruits()
        another_obj = src.SomeClass()
        another_obj.get_fruits()
        self.assertNotEquals(getattr(my_obj, '__time_get_fruits', 0),
                             getattr(another_obj, '__time_get_fruits', 0),
                             'Two instances are sharing times')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
