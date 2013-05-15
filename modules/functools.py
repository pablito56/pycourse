#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod: functools module 
'''


#===============================================================================
# functools - High-order functions and operators on callables
#
#   - High-order functions: functions that act on or return other functions
#   - any callable object can be treated as a function for the purpose of this module
#
#===============================================================================


# partial objects 
#    - created by functools.partial function
#    - they are like functions in that they are callable but have some minor diffs
#

# functools.partial(func[, *args][, **keywords])
#
#      returns a new 'partial' object which when called will behave like func called
#      with the positional arguments 'args' and keyword arguments 'keywords'.

import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)

def show_details(name, f, is_partial=False):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    if not is_partial:
        print '\t__name__:', f.__name__
        print '\t__doc__', repr(f.__doc__)
    if is_partial:
        print '\tfunc:', f.func
        print '\targs:', f.args
        print '\tkeywords:', f.keywords

show_details('myfunc', myfunc)
myfunc('a', 3)


p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)
p1('default a')
p1('override b', b=5)


p2 = functools.partial(myfunc, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')


print 'Insufficient arguments:'
p1()


# partial functions does not have a __name__ or __doc__ attributes by default.
# functools.update_wrapper solves this purpose


def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:', 
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
        print '\t__doc__', repr(f.__doc__)


show_details('myfunc', myfunc)


p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)


print 'Updating wrapper:'
print '\tassign:', functools.WRAPPER_ASSIGNMENTS
print '\tupdate:', functools.WRAPPER_UPDATES


functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)


# functools.wraps(wrapped[,assigned][,updated])
#   a convenience function for invoking partial(update_wrapper, wrapped=wrapped,
#                                               assigned=assigned, updated=updated)


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print '\tdecorated:', (a, b)
        print '\t',
        f(a, b=b)
    return decorated


show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)


wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to decorated', 4)


#===============================================================================
# SOURCES:
#  - http://doughellmann.com/2008/04/pymotw-functools.html
#  - http://docs.python.org/2/library/functools.html
#===============================================================================
