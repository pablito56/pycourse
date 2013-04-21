#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 03 (descriptors) exercise: tests

>>> import time
>>> from solution_mod_03 import factorial

>>> t1_start = time.time()
>>> res1 = factorial(200)
>>> t1_elapsed = time.time() - t1_start

>>> t2_start = time.time()
>>> res2 = factorial(200)
>>> t2_elapsed = time.time() - t2_start

>>> print "TIMES:", t1_elapsed, "vs.", t2_elapsed
TIMES: 20.1713969707 vs. 0.102944135666
"""
import unittest
import time
from .. import simcache
from exercise_mod_03 import factorial
# from solution_mod_03 import factorial


class TestMemoization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Increase output detail in case of errors
        """
        cls.maxDiff = None
        cls.longMessage = True

    def setUp(self):
        """Setup: ensure cache is empty before each test
        """
        simcache.clear_keys()

    def tearDown(self):
        pass

    def test_memoization_speedup(self):
        """Test that second call to factorial runs faster
        """
        x = 30
        # First call
        t1_start = time.time()
        res1 = factorial(x)
        t1_elapsed = time.time() - t1_start
        # Second call
        t2_start = time.time()
        res2 = factorial(x)
        t2_elapsed = time.time() - t2_start
        print t1_elapsed, "vs.", t2_elapsed
        # Assert second time was faster
        self.assertEqual(res1, res2, "Factorial results differ")
        self.assertTrue(t1_elapsed > t2_elapsed + 1, "Second execution did not run faster")
        self.assertTrue(simcache.get_key(x - 1))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
