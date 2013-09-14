#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod 07: context managers and contextlib
'''


# Let's go back to objects data model to implement a custom context manager


class TriFile(object):
    """Context manager to handle three files opened at the same time
    """
    def __init__(self, file1, file2, file3):
        print "CALLED __init__", file1, file2, file3
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3

    def __enter__(self):
        """Enter the runtime context related to this object
        """
        print "CALLED __enter__"
        self.f1 = open(self.file1, "a")
        self.f2 = open(self.file2, "a")
        self.f3 = open(self.file3, "a")
        return self.f1, self.f2, self.f3

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object
        Parameters describe the exception that caused the
        context to be exited (or None).
        """
        print "CALLED __exit__", exc_type, exc_val, exc_tb
        self.f1.close()
        self.f2.close()
        self.f3.close()
        return True      # If we return True the exceptions are not propagated


# Let's try our context manager


with TriFile("test_file1.txt", "test_file2.txt", "test_file3.txt") as tri_file_tuple:
    print "INSIDE THE CONTEXT MANAGER"
    f1, f2, f3 = tri_file_tuple
    f1.write("Hello f1!\n")
    f2.write("Hello f2!\n")
    f3.write("Hello f3!\n")


# Let's try it again


# We create the context manager instance before the with statement
ctxt_manager = TriFile("test_file1.txt", "test_file2.txt", "test_file3.txt")


# Later we use the context manager instance
with ctxt_manager as tri_file_tuple:
    print "INSIDE THE CONTEXT MANAGER"
    f1, f2, f3 = tri_file_tuple
    f1.write("Hello f1!\n")
    f2.write("Hello f2!\n")
    f3.write("Hello f3!\n")


# Let's raise an exception inside the context manager


with TriFile("test_file1.txt", "test_file2.txt", "test_file3.txt") as tri_file_tuple:
    f1, f2, f3 = tri_file_tuple
    f1.write("Bye bye f1!\n")
    f2.write("Bye bye f2!\n")
    f3.write("Bye bye f3!\n")

    raise TypeError(str)  # Let's make it raise an exception on purpose


# Let's raise an exception when entering the context manager

from os.path import sep
with TriFile("test_file1.txt", "test_file2.txt",
             sep.join(("", "file", "does", "not", "exist.txt"))) as tri_file_tuple:
    print "INSIDE THE CONTEXT MANAGER"
    f1, f2, f3 = tri_file_tuple
    f1.write("Won't be printed f1!\n")
    f2.write("Won't be printed f2!\n")
    f3.write("Won't be printed f3!\n")


#===============================================================================
# More info on context managers:
# - http://docs.python.org/2.7/reference/datamodel.html#with-statement-context-managers
# - http://docs.python.org/2.7/library/stdtypes.html#typecontextmanager
#===============================================================================


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
