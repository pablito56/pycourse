#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 04 (advanced decorators) exercise: tests
"""
import unittest
import time
from exercise_mod_04 import factorial, fibonacci
# from solution_mod_04 import factorial, fibonacci


class TestClearCache(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Increase output detail in case of errors
        """
        cls.maxDiff = None
        cls.longMessage = True

    def test_second_is_faster(self):
        expected_factorial = 10333147966386144929666651337523200000000L
        expected_fibonacci = 9227465
        x = 35
        # First factorial call
        start_fact_1 = time.time()
        res_fact_1 = factorial(x)
        elapsed_fact_1 = time.time() - start_fact_1
        self.assertEqual(res_fact_1, expected_factorial)
        # Second factorial call
        start_fact_2 = time.time()
        res_fact_2 = factorial(x)
        elapsed_fact_2 = time.time() - start_fact_2
        self.assertEqual(res_fact_2, expected_factorial)
        # Test factorial elapsed times
        print "factorial", elapsed_fact_1, "vs.", elapsed_fact_2
        self.assertTrue(elapsed_fact_1 > elapsed_fact_2 + 1)
        # First fibonacci call
        start_fib_1 = time.time()
        res_fib_1 = fibonacci(x)
        elapsed_fib_1 = time.time() - start_fib_1
        self.assertEqual(res_fib_1, expected_fibonacci)
        # Second fibonacci call
        start_fib_2 = time.time()
        res_fib_2 = fibonacci(x)
        elapsed_fib_2 = time.time() - start_fib_2
        self.assertEqual(res_fib_2, expected_fibonacci)
        # Test fibonacci elapsed times
        print "fibonacci", elapsed_fib_1, "vs.", elapsed_fib_2
        self.assertTrue(elapsed_fib_1 > elapsed_fib_2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
