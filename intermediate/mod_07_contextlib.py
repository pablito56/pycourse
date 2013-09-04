#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod 07: contextlibs module 
'''


#===============================================================================
# From Generator to Context Manager:
#
# - Alternative to create a context manager to defining __enter__() and __exit__() 
#       methods, is not difficult. 
# - Less overhead by using a decorator -> contextmanager()
# - The generator should initialize the context, yield exactly one time, then clean
#       up the context. 
# - The value yielded, if any, is bound to the variable in the as clause of the 
#       with statement. 
# - Exceptions from within the with block are re-raised inside the generator, 
#       so you can handle them there.
#===============================================================================

import contextlib

@contextlib.contextmanager
def make_context():
    print '  entering'
    try:
        yield {}
    except RuntimeError, err:
        print '  ERROR:', err
    finally:
        print '  exiting'


print 'Normal:'
with make_context() as value:
    print '  inside with statement:', value


print 'Handled error:'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')


print 'Unhandled error:'
with make_context() as value:
    raise ValueError('this exception is not handled')

#===============================================================================
# - At times it is necessary to manage multiple contexts simultaneously (such as 
# when copying data between input and output file handles, for example). 
# - It is possible to nest with statements one inside another. 
# - by using contextlibs.nested, we spare useless identation levels
#===============================================================================


@contextlib.contextmanager
def make_context(name):
    print 'entering:', name
    yield name
    print 'exiting :', name

with contextlib.nested(make_context('A'), make_context('B'), make_context('C')) as (A, B, C):
    print 'inside with statement:', A, B, C



#===============================================================================
# SOURCES:
#  - http://doughellmann.com/2008/05/pymotw-contextlib.html
#  - http://docs.python.org/2/library/contextlib.html
#===============================================================================
