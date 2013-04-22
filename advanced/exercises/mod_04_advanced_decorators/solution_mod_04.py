#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 04 (advanced decorators) exercise: solution
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


class SIMCache(object):
    def __init__(self, size, ttl):
        self.cache = OrderedDict()
        self.size = size
        self.ttl = ttl

    def set_key(self, key, value, ttl=None):
        """Set a key value in the cache with its expiration time.
        If no ttl (in seconds) is provided self.ttl is taken by default.
        If cache length exceeds CACHE_SIZE when adding a key, the oldest (first inserted) key is removed (FIFO)
        """
        self.cache[key] = (time.time() + (ttl or self.ttl), value)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

    def get_key(self, key):
        """Retrieve a key value from the cache.
        Returns None if does not exist or the key expired.
        If the key expired it is removed from the cache.
        """
        content = self.cache.get(key, None)
        if content:
            if content[0] > time.time():
                return content[1]
            else:
                del self.cache[key]
        return None

    def clear_keys(self, ):
        """Remove all cache keys content
        """
        self.cache = OrderedDict()


class MemoizationDecoratorFactory(object):
    def __init__(self, size=300, ttl=3600):
        # TODO: Merge both classes in a single class
        self.simcache = SIMCache(size, ttl)

    def __call__(self, func_to_memoize):
        @functools.wraps(func_to_memoize)
        def logging_wrapper(*args):
            """Wrapper to print a log trace in case function returned a wrong result
            """
            res = self.simcache.get_key(args)
            if not res:
                res = func_to_memoize(*args)  # Call the real function
                self.simcache.set_key(args, res)
            return res
        return logging_wrapper


@MemoizationDecoratorFactory()
def factorial(n):
    """Return n!"""
    time.sleep(0.1)  # Do not remove it
    if n < 2:
        return 1
    return n * factorial(n - 1)


@MemoizationDecoratorFactory()
def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
