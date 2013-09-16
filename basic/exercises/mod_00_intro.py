#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: introductory exercises from pythonmonk.com
'''


def minimum(a, b):
    """Computes minimum of given 2 numbers.
    
        >>> minimum(2, 3)
        2
        >>> minimum(8, 5)
        5
        """
    min(a, b)
    # your code here


def maximum3(a, b, c):
    """Computes maximum of given three numbers.
    
    	>>> maximum3(2, 3, 5)
        5
    	>>> maximum3(12, 3, 5)
        12
    	>>> maximum3(2, 13, 5)
        13
    """
    max(a,b,c)
    # your code here


def istrcmp(s1, s2):
    """Compare given two strings for equality, ignoring the case.
    
    	>>> istrcmp("python", "Python")
        True
    	>>> istrcmp("latex", "LaTeX")
        True
    	>>> istrcmp("foo", "Bar")
        False
    """
    return s1.lower() == s2.lower()

    # your code here


def unique(values):
    """Finds all unique elements of a list.

        >>> unique([])
        []
        >>> unique([1, 2, 1])
        [1, 2]
        >>> unique([1, 2, 1, 3, 4, 2])
        [1, 2, 3, 4]
    """
    list(set(values))


def isort(names):
    """Sorts a list of strings ignoring the case.
    
        >>> isort(['BOB', 'ALICE', 'dave', 'charlie'])
        ['ALICE', 'BOB', 'charlie', 'dave']
    """
    names.sort(key=lambda x: x[1])

