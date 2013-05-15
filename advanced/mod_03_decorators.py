#-*- coding: utf-8 -*-
u"""
MOD 03: decorators fundamentals
"""


# Time to practice again


#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_03_decorators/exercise_mod_03
#
# - Use memoization to speed up factorial computation
#     - http://en.wikipedia.org/wiki/Memoization
#     - Use our simple in-memory cache to store and retrieve calls results
#
# - Run the tests in 'tests_mod_03.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_03.py'
#===============================================================================


import time
from exercises import simcache


def factorial(x):
    time.sleep(0.1)  # This sleep can not be removed!!
    if x < 2:
        return 1
    res = simcache.get_key(x - 1)
    if not res:
        res = factorial(x - 1)
        simcache.set_key(x - 1, res)
    return x * res


# Another example


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


t1_start = time.time()
print fibonacci(30)
t1_elapsed = time.time() - t1_start
print t1_elapsed

t1_start = time.time()
print fibonacci(33)
t1_elapsed = time.time() - t1_start
print t1_elapsed


# Slower than factorial. We should memoize


#===============================================================================
# - Remember DRY: Don't Repeat Yourself!
#    - Let's try to apply memoization in a generic way to not modified functions
#===============================================================================


# Let's do a bit of magic to apply memoization easily


# Let's create a new method with memoization
real_fibonacci = fibonacci
def fibonacci(n):
    res = simcache.get_key(n)
    if not res:
        res = real_fibonacci(n)
        simcache.set_key(n, res)
    return res

# Let's try it
t1_start = time.time()
print fibonacci(33)
t1_elapsed = time.time() - t1_start
print t1_elapsed

# Let's try something harder
t1_start = time.time()
print fibonacci(100)
t1_elapsed = time.time() - t1_start
print t1_elapsed


# Ok. Let's explain the trick in slow motion

simcache.clear_keys()  # Let's clean the cache

# Let's define the real fibonacci computation function
def fibonacci(n):
    if n < 2:
        return n
    print "Real fibonacci func, calling recursively to", fibonacci, n
    # Once the trick is done globals will contain a different function binded to 'fibonacci'
    return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci

print fibonacci(5)

#===============================================================================
# Call graph of fibonacci for n=5
#
#        __ 4 ---- 3 ----------- 2 ---- 1
#   5 __/      \__ 2 ---- 1  \__ 1  \__ 0
#      |              \__ 0
#       \__ 3 ---- 2 ---- 1
#              \__ 1  \__ 0
#
#===============================================================================

# Let's save a reference to the real function
real_fibonacci = fibonacci

print real_fibonacci  # Points to real fibonacci calculation function


# Let's create a new method which will use memoization
def memoized_fibonacci(n):
    # Try to retrieve value from cache
    res = simcache.get_key(n)
    if not res:
        # If failed, call real fibonacci func
        print "Memoized fibonacci func, proceeding to call real func", real_fibonacci, n
        res = real_fibonacci(n)
        # Store real result
        simcache.set_key(n, res)
    return res

print memoized_fibonacci  # This is the new function with memoization

# Let's replace the real function by the memoized version in module globals
fibonacci = memoized_fibonacci


print fibonacci(5)  # Let's see what happens now

print fibonacci(5)  # Let's try again

print fibonacci(10)  # Let's try with a bigger number


#===============================================================================
# - Congratulations! We have applied our first hand-crafted decorator
#===============================================================================


#===============================================================================
# - How would you memoize any function, not just fibonacci?
#===============================================================================


# Do you remember functions are first class objects? They can be used as arguments or return values...
# Do you remember we can declare functions inside other functions?

# Let's apply these concepts to find a generic method to use memoization

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def memoize_any_function(func_to_memoize):
    """Function to return a wrapped version of input function using memoization
    """
    print "Called memoize_any_function"

    def memoized_version_of_func(n):
        """Wrapper using memoization
        """
        res = simcache.get_key(n)
        if not res:
            res = func_to_memoize(n)  # Call the real function
            simcache.set_key(n, res)
        return res
    return memoized_version_of_func

fibonacci = memoize_any_function(fibonacci)


print fibonacci(35)


# Why not apply it directly?


@memoize_any_function  # This is the simplest decorator syntax
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(150)


#===============================================================================
# Python decorators:
#     - A callable which receives a funtion as only argument and returns another
#       function. Typically the resulting function wrapps the first function
#       executing some code before and/or after the first is called.
#
#     - New in Python 2.4, they are the pythonic implementation of Decorator Pattern
#
#    - Used with the at @ symbol before a function or method
#        - Don't forget to deal with 'self' as first argument of methods
#
#    - The decoration is done at import / evaluation time
#===============================================================================


# More about decorators


def timing_decorator(decorated_func):
    print "Called timing_decorator"

    def wrapper(*args):  # Use variable arguments to be compatible with any function
        """Wrapper for time executions
        """
        start = time.time()
        res = decorated_func(*args)  # Call the real function
        elapsed = time.time() - start
        print "Execution of '{0}{1}' took {2} seconds".format(decorated_func.__name__, args, elapsed)
        return res
    return wrapper


@timing_decorator
@memoize_any_function  # We can accumulate decorators
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


simcache.clear_keys()
print fibonacci(5)


#===============================================================================
# - It is possible to accumulate decorators
# - Order matters, they are run in strict top - down order
#===============================================================================


# Why 'memoized_version_of_f' appears as the function name? Let's change it


import functools
def memoize_any_function(decorated_func):
    """Function to return a wrapped version of input function using memoization
    """
    @functools.wraps(decorated_func)  # Use functools.wraps to smooth the decoration
    def memoized_version_of_f(*args):
        """Wrapper using memoization
        """
        res = simcache.get_key(args)
        if not res:
            res = decorated_func(*args)  # Call the real function
            simcache.set_key(args, res)
        return res
    return memoized_version_of_f


def timing_decorator(decorated_func):
    @functools.wraps(decorated_func)
    def wrapper(*args):  # Use variable arguments to be compatible with any function
        """Wrapper for time executions
        """
        start = time.time()
        res = decorated_func(*args)  # Call the real function
        elapsed = time.time() - start
        print "Execution of '{0}{1}' took {2} seconds".format(decorated_func.__name__, args, elapsed)
        return res
    return wrapper


#===============================================================================
# - functools.wraps copies name, module and docstring of wrapped function to its wrapper
#
# - Use variable number of positional and keyword arguments for higher compatibility
#===============================================================================


@timing_decorator
@memoize_any_function  # We can accumulate decorators, and they are run in strict top-down order
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


simcache.clear_keys()
print fibonacci(5)


#===============================================================================
# - Decorators are executed each time the decorated function is called
#    - Potential performance loss
#===============================================================================


@memoize_any_function
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timing_decorator
def call_fibonacci(n):
    return fibonacci(n)


simcache.clear_keys()
print call_fibonacci(30)


#===============================================================================
# Python decorators:
#
#     - A callable which receives a funtion as only argument and returns another
#       function. Typically the resulting function wrapps the first function
#       executing some code before and/or after the first is called.
#
#     - New in Python 2.4, they are the pythonic implementation of Decorator Pattern
#
#    - Used with the at @ symbol before a function or method
#        - Don't forget to deal with 'self' as first argument of methods
#
#    - The decoration is done at import / evaluation time
#
#    - It is possible to accumulate decorators
#        - Order matters, they are run in strict top - down order
#
#    - functools.wraps copies name, module and docstring of wrapped function to its wrapper
#
#    - Use variable number of positional and keyword arguments for higher compatibility
#
#    - Decorators are executed each time the decorated function is called
#        - Potential performance loss
#
#    - Typical uses:
#        - Memoization
#        - Timing, profiling, logging, stats...
#        - Overriding arguments, pre / post conditions
#        - Retries
#        - Exception handling
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://en.wikipedia.org/wiki/Decorator_pattern
#  - http://stackoverflow.com/a/1594484
#===============================================================================
