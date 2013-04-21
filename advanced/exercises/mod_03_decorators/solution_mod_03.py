#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 03 (descriptors) exercise: solution

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
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_03_decorators/exercise_mod_03
#
# - Use memoization to speed up factorial computation
#     - http://en.wikipedia.org/wiki/Memoization
#     - Use our simple in-memory cache to store calls results
#
# - Run the tests in 'tests_mod_03.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_03.py'
#===============================================================================


from time import sleep
from .. import simcache


def factorial(x):
    sleep(0.1)  # This sleep can not be removed!!
    if x < 2:
        return 1
    res = simcache.get_key(x - 1)
    if not res:
        res = factorial(x - 1)
        simcache.set_key(x - 1, res)
    return x * res
