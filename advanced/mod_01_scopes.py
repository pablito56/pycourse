#-*- coding: utf-8 -*-
u"""
MOD 01: Namespaces and scopes
"""


# Let's start with a bit of practice


#===============================================================================
# EXERCISE 1: pycourse/advanced/exercices/mod_01_scopes/exercise_01_scopes.py
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


import time
from collections import OrderedDict


CACHE = OrderedDict()
CACHE_SIZE = 5
CACHE_TTL = 600


def set_key(key, value, ttl=None):
    """Set a key value in the cache with its expiration time.
    If no ttl is provided CACHE_TTL is taken by default.
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


set_key("my_key", "my_value")
print CACHE
print CACHE["my_key"]  # (expiration time, value)
print get_key("my_key")


print get_key("not_found_key")


set_key("short_living_key", "short_living_value", 0.1)
print get_key("short_living_key")
time.sleep(0.1)
print get_key("short_living_key")


#===============================================================================
# LESSONS LEARNT:
# - It is possible to access global names in a module (module attributes) from
#   within its functions and classes
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - It is possible to access global names in a module (module attributes) from
#   within its functions and classes
#    - The same happens with imported names!
#===============================================================================


# Let's continue playing a bit with these ideas
from os import path
print path

from sys import path
print path


#===============================================================================
# - Two modules can define the same name for different things
#===============================================================================


# Remember to avoid collisions when importing
from os import path as ospath
from sys import path as syspath
print ospath
print syspath


# Why both modules can define the same name?


#==============================================================================
# - Python namespaces
#    - A namespace is a mapping from names to objects
#        - Currently implemented as Python dictionaries (may change in the future)
#    - Examples:
#        - The set of built-in names (functions and exceptions): map, xrange, abs... (__builtin__)
#        - Global names in a module
#        - Local names in a function invocation
#        - Names defined in top-level invocation of the interpreter (__main__)
#
#    - There is no relation between names in different namespaces
#        - Two modules or functions may define the same name without confusion
#
#    - Namespaces are created at different moments and have different lifetimes
#        - Local namespace of a function invocation is created each time it is called
#==============================================================================


def get_power_func(y):
    print "Preparing to raise to power of {} func".format(y)

    def power_func(x):
        print "Executing computation of {} raised to power of {}".format(x, y)

        def my_custom_power_func():  # No arguments provided?!?!
            print "Actual computation of {} raised to power of {}".format(x, y)
            x = x ** y
            return x
        return my_custom_power_func()
    return power_func

raise_to_3 = get_power_func(3)
raise_to_4 = get_power_func(4)

two = 2
three = 3
print raise_to_4(two)
print raise_to_3(three)
print two, three


# Did you realize 'my_custom_power_func' takes no argument? What kind of sorcery is this?


#==============================================================================
# - Python scopes
#    - Textual region of a Python program where a namespace is directly accessible
#    - Although scopes are determined statically, they are used dynamically
#
#    - At any time during execution, there are at least three nested scopes
#      whose namespaces are directly accessible:
#        - The innermost scope, which is searched first, contains the local names
#
#        - The scopes of any enclosing functions, which are searched starting with
#          the nearest enclosing scope, contains non-local, but also non-global names
#
#        - The next-to-last scope contains the current module’s global names
#
#        - The outermost scope (searched last) is the namespace containing built-in names
#
#    - Only local scope and global namespaces can be modified
#==============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces
#===============================================================================
