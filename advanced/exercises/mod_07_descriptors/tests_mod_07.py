#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 07 (advanced decorators) exercise: tests
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_07_descriptors/exercise_mod_07
#
# - Use descriptor protocol to cache during a certain TTL the return value of a function as an attribute
#
# - Run the tests in 'tests_mod_07.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_07.py'
#===============================================================================


import unittest
import time
from exercise_mod_07 import CachedAttrClass
# from solution_mod_07 import CachedAttrClass


class TestCachedAttribute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Increase output detail in case of errors
        """
        cls.maxDiff = None
        cls.longMessage = True

    def test_value_changes_after_ttl(self):
        """Test how cached attribute value is changed after it expired
        """
        instance = CachedAttrClass()
        res1 = instance.cached_attr
        time.sleep(3.1)
        res2 = instance.cached_attr
        self.assertNotEqual(res1, res2, "Calls after TTL expired must return a different value")

    def test_value_is_cached(self):
        """Test how cached attribute value does not change while not expired
        """
        instance = CachedAttrClass()
        res1 = instance.cached_attr
        res2 = instance.cached_attr
        self.assertEqual(res1, res2, "Calls before TTL expired must return the same value")

    def test_value_is_retrieved_fast(self):
        """Test how cached attribute value retrieval is fast while not expired
        """
        instance = CachedAttrClass()
        t_start_1 = time.time()
        res1 = instance.cached_attr
        t_elapsed_1 = time.time() - t_start_1
        self.assertTrue(t_elapsed_1 >= 2)
        t_start_2 = time.time()
        res2 = instance.cached_attr
        t_elapsed_2 = time.time() - t_start_2
        self.assertTrue(t_elapsed_1 > t_elapsed_2 + 1.5)
        self.assertEqual(res1, res2, "Calls before TTL expired must return the same value")
        time.sleep(3)
        t_start_3 = time.time()
        res3 = instance.cached_attr
        t_elapsed_3 = time.time() - t_start_3
        self.assertTrue(t_elapsed_2 < t_elapsed_3 + 1.5)
        self.assertNotEqual(res2, res3, "Calls after TTL expired must return different value")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
