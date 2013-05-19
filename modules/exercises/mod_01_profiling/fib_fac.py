#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 01: Timing and profiling
"""


def factorial(n):
    """Return the factorial of n"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_fac(x=30, y=900):
    fib = fibonacci(x)
    fac = factorial(y)
    print "fibonacci({}):".format(x), fib
    print "factorial({}):".format(y), fac


if __name__ == "__main__":
    fib_fac()
