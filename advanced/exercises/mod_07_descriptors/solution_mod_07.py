#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 07 (descriptors) exercise: solution
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


import time


class CachedAttribute(object):
    def __init__(self, name, func, seconds):
        self.name = name
        self.func = func
        self.delta = seconds
        # self.expiration = None  # We need expiration for each instance!

    def __get__(self, inst, cls):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        # We have to store a different expiration for each instance!
        expiration = inst.__dict__.get("_cache_expiration", None)
        if expiration:
            print expiration, 'VS.', time.time()
        if expiration is None or expiration <= time.time():
            # Let's add the result to the INSTANCE and current time
            inst.__dict__[self.name] = self.func(inst)
            now = time.time()
            expiration = now + self.delta
            inst.__dict__["_cache_expiration"] = expiration
            print "Cached at", now, "until", expiration, "with value", inst.__dict__[self.name]
        return inst.__dict__[self.name]


class CachedAttrClass(object):
    def expensive_operation(self):
        from time import sleep
        from random import seed, random
        sleep(2)
        seed()
        return random()
    cached_attr = CachedAttribute('_cached_attr', expensive_operation, 3)
