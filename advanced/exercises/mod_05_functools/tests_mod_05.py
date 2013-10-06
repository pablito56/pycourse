#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 5, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 05 functools exercise

>>> it = power_of(2)

>>> it.next()
1

>>> it.next()
2

>>> it.next()
4

>>> it.next()
8

>>> it.next()
16

>>> it = power_of(3)

>>> it.next()
1

>>> it.next()
3

>>> it.next()
9
"""

import unittest
from exercise_mod_05 import power_of
# from solution_mod_05 import power_of


class TestPowerOf(unittest.TestCase):

    def test_power_of_2(self):
        """Test power_of(2) until 100
        """
        x = 2
        it = power_of(x)
        for index in xrange(101):
            self.assertEqual(it.next(), pow(x, index))

    def test_power_of_3(self):
        """Test power_of(3) until 1000
        """
        x = 3
        it = power_of(x)
        for index in xrange(1001):
            self.assertEqual(it.next(), pow(x, index))

    def test_power_of_7(self):
        """Test power_of(7) until 10000
        """
        x = 7
        it = power_of(x)
        for index in xrange(10001):
            self.assertEqual(it.next(), pow(x, index))


if __name__ == "__main__":
    #import sys;sys.argv = ["", "Test.testName"]
    unittest.main()
