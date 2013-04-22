#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 04 (advanced decorators) exercise: apply memoization to factorial and fibonacci
"""
#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_04_advanced_decorators/exercise_mod_04
#
# - Use memoization to speed up factorial and fibonacci computation
#     - Take care to not share the same cache for both
#     - Ideally it should be possible to specify different cache setup for each decorated function
#
# - Run the tests in 'tests_mod_04.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_04.py'
#===============================================================================


import functools
import time
from collections import OrderedDict


def factorial(n):
    """Return n!"""
    time.sleep(0.1)  # Do not remove it
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
