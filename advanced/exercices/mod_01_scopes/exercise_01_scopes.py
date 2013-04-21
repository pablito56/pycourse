#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 01 (scopes) exercise: implement a simple cache

>>> import exercise_01_1 as cache_mod

>>> cache_mod.set_key("my_key", "my_value")

>>> print cache_mod.CACHE["my_key"]
(1366544507.87305, 'my_value')  # (expiration time, value)

>>> print cache_mod.get_key("my_key")
my_value

>>> print cache_mod.get_key("not_found_key")
None
"""
#===============================================================================
# EXERCISE 1:
#
# - Implement a simple in-memory cache
#     - Set and get a value associated to a key
#     - Manage cache size to avoid taking too much memory (FIFO)
#     - Manage key's ttl (with default value) to let values expire
#
# - Check the imports documentation
#
# - Run the tests in 'tests_01_scopes.py' executing 'nosetests -v' inside this folder
#
# - Check the solution in module 'solution_01_scopes.py'
#===============================================================================


# http://docs.python.org/2/library/time.html#time.time
# current_unix_time = time.time()
import time
# http://docs.python.org/2/library/collections.html#ordereddict-objects
from collections import OrderedDict


CACHE = {}
CACHE_SIZE = 5
CACHE_TTL = 1  # Maybe this should be increased in slow machines to run the tests


def set_key(key, value, ttl=None):
    """Set a key value in the cache with its expiration time.
    If no ttl is provided CACHE_TTL is taken by default.
    If cache length exceeds CACHE_SIZE when adding a key, the oldest (first inserted) key is removed (FIFO)
    """
    raise NotImplementedError


def get_key(key):
    """Retrieve a key value from the cache.
    Returns None if key does not exist or the key expired.
    If the key expired it is removed from the cache.
    """
    raise NotImplementedError
