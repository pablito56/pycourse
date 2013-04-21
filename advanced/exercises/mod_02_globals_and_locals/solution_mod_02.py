#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 02 (globals and locals) exercise: add a clear method

>>> import exercise_mod_02 as cache_mod

>>> cache_mod.set_key("my_key", "my_value")

>>> print cache_mod.CACHE["my_key"]
(1366544507.87305, 'my_value')  # (expiration time, value)

>>> print cache_mod.get_key("my_key")
my_value

>>> print cache_mod.clear()

>>> print cache_mod.get_key("my_key")
None
"""
#===============================================================================
# EXERCISE:
#
# - Modify our simple in-memory cache:
#     - Add a method to clear the cache content
#
# - Check the documentation
#
# - Run the tests in 'tests_mod_02.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_02.py'
#===============================================================================


import time
from collections import OrderedDict


CACHE = OrderedDict()
CACHE_SIZE = 5
CACHE_TTL = 1  # Maybe this should be increased in slow machines to run the tests


def set_key(key, value, ttl=None):
    """Set a key value in the cache with its expiration time.
    If no ttl (in seconds) is provided CACHE_TTL is taken by default.
    If cache length exceeds CACHE_SIZE when adding a key, the oldest (first inserted) key is removed (FIFO)
    """
    CACHE[key] = (time.time() + (ttl or CACHE_TTL), value)
    if len(CACHE) > CACHE_SIZE:
        CACHE.popitem(last=False)


def get_key(key):
    """Retrieve a key value from the cache.
    Returns None if does not exist or the key expired.
    If the key expired it is removed from the cache.
    """
    content = CACHE.get(key, None)  # content = (expiration_time, value)
    if content:
        if content[0] > time.time():
            return content[1]
        else:
            del CACHE[key]
    return None


def clear_keys():
    """Remove all cache keys content
    """
    # http://docs.python.org/2/reference/simple_stmts.html#global
    global CACHE
    CACHE = OrderedDict()
