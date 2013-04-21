#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

SIMCACHE: Simple In-Memory Cache

>>> import simcache

>>> simcache.set_key("my_key", "my_value", ttl=600)

>>> print simcache.CACHE["my_key"]
(1366544507.87305, 'my_value')  # (expiration time, value)

>>> print simcache.get_key("my_key")
my_value

>>> print simcache.clear()

>>> print simcache.get_key("my_key")
None
"""
import time
from collections import OrderedDict


CACHE = OrderedDict()
CACHE_SIZE = 300
CACHE_TTL = 3600


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
    content = CACHE.get(key, None)
    if content:
        if content[0] > time.time():
            return content[1]
        else:
            del CACHE[key]
    return None


def clear_keys():
    """Remove all cache keys content
    """
    global CACHE
    CACHE = OrderedDict()
