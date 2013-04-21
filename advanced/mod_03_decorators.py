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
#     - Use our simple in-memory cache to store calls results
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
    "Return the nth fibonacci number"
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


# It's still worse than factorial. We should memoize


#===============================================================================
# - Remember DRY: Don't Repeat Yourself!
#===============================================================================


# Let's do a bit of magic to apply memoization easily


real_fibonacci = fibonacci


# Let's create a new method with memoization
def fibonacci(n):
    res = simcache.get_key(n)
    if not res:
        res = real_fibonacci(n)
        simcache.set_key(n, res)
    return res


# Let's run for first time
t1_start = time.time()
print fibonacci(30)
t1_elapsed = time.time() - t1_start
print t1_elapsed

# Let's try again
t1_start = time.time()
print fibonacci(33)
t1_elapsed = time.time() - t1_start
print t1_elapsed

# Let's try something harder
t1_start = time.time()
print fibonacci(100)
t1_elapsed = time.time() - t1_start
print t1_elapsed


# Let's explain the trick in slow motion

simcache.clear_keys()  # Let's clean the cache

# Let's define the real fibonacci computation function
def fibonacci(n):
    "Return the nth fibonacci number"
    if n < 2:
        return n
    print "Real fibonacci func, calling recursively to", fibonacci, n
    # Once the trick is done globals will contain a different function binded to 'fibonacci'
    return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci

print fibonacci(5)

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

# Do you remember functions are first class objects? They can be used as arguments or return values...

# Do you remember we can declare functions inside other functions?

def memoize_any_function(f):
    def memoized_version_of_f(n):
        res = simcache.get_key(n)
        if not res:
            res = f(n)
            simcache.set_key(n, res)
        return res
    return memoized_version_of_f

fibonacci = memoize_any_function(real_fibonacci)


print fibonacci(15)
