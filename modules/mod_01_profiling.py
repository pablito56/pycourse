#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 01: Timing and profiling
"""

#===========================================================================
# EXERCISE:
#  - Execute the following command:
#     $ python -m timeit '"-".join([str(n) for n in range(100)])'
#
#  - Now execute the following:
#    $ python -m timeit '"-".join(map(str, range(100)))'
#
#  - Now execute:
#    $ python -m timeit --setup 'func = lambda n: "-".join(map(str, range(n)))' 'func(100)'
#
#  - And finally:
#    $ python -m timeit --setup 'func = lambda n: "-".join(map(str, xrange(n)))' 'func(100)'
#===========================================================================


#===============================================================================
# - timeit module:
#    - Provides a simple way to time the execution of Python statements.
#    - Provides both command line and programatic interfaces.
#===============================================================================


import timeit
print timeit.timeit(stmt='func(100)', setup='func = lambda n: "-".join(map(str, xrange(n)))', number=10000)


# It is possible to provide a callable statement


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_15():
    return fibonacci(15)


print timeit.timeit(stmt=fib_15, number=100)


# Actually, a Timer class is provided inside timeit module

t = timeit.Timer(stmt=fib_15)
print t.repeat(repeat=3, number=100)


#===============================================================================
# - timeit module:
#    - Provides a simple way to time the execution of Python statements.
#    - Provides both command line and programatic interfaces.
#        - Provides timeit.Timer class
#
#    - Useful to compare performance of different implementations.
#    - Remember that it may be affected by other processes in the machine.
#===============================================================================

#===========================================================================
# EXERCISE:
#  - Execute the following command:
#    $ python -m cProfile exercises/mod_01_profiling/fib_fac.py
#
#  - Now execute the following:
#    $ python -m cProfile -s time exercises/mod_01_profiling/fib_fac.py
#
#  - Now execute:
#    $ python -m cProfile -s cumulative exercises/mod_01_profiling/fib_fac.py
#
#  - And finally:
#    $ python -m cProfile -s calls exercises/mod_01_profiling/fib_fac.py
#===========================================================================


#===============================================================================
# - cProfile:
#    - Deterministic profiling of Python programs.
#    - C extension with reasonable overhead.
#    - Provides both command line and programatic interfaces.
#
#    - There is a pure Python alternative module with the same interface: profile
#===============================================================================

import cProfile
import pstats


filename = "cprofile_fib_fac.log"
max_num_lines = 3


# Note that in normal execution the import is not needed inside the statement string (incompatibility with pydemo)
cProfile.run(statement="from exercises.mod_01_profiling.fib_fac import fib_fac; fib_fac()", filename=filename)


stats = pstats.Stats(filename)
stats.strip_dirs().sort_stats('time').print_stats(max_num_lines)
stats.strip_dirs().sort_stats('cumulative').print_stats(max_num_lines)
stats.strip_dirs().sort_stats('calls').print_stats(max_num_lines)


#===============================================================================
# - cProfile:
#    - Deterministic profiling of Python programs.
#    - C extension with reasonable overhead.
#    - Provides both command line and programatic interfaces.
#    - Use pstats.Stats to parse and print cProfile output
#    - You can sort the records:
#        - time: single execution time of a function
#        - cumulative: accumulated execution time of a function
#        - calls: number of times a function was called
#        - Others: http://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats
#
#    - There is a pure Python alternative module with the same interface: profile
#===============================================================================


#===============================================================================
# - Use cProfile to identify slowest parts of your code
# - Use timeit to comparte alternative implementations
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/timeit.html
#  - http://pymotw.com/2/timeit/
#  - http://docs.python.org/2/library/profile.html
#  - http://pymotw.com/2/profile/
#===============================================================================
