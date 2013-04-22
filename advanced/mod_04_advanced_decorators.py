#-*- coding: utf-8 -*-
u"""
MOD 04: advanced decorators
"""
import functools


# Actually, we can execute our own code in the at @ statement


def logger_decorator_factory(wrong_result):  # Decorator arguments are provided here
    """Factory to pass arguments to the decorator
    """
    print "Called logger_decorator_factory with", wrong_result

    def logger_decorator(func_to_decorate):
        print "Called logger_decorator"

        @functools.wraps(func_to_decorate)
        def logging_wrapper(*args, **kwargs):
            """Wrapper to print a log trace in case function returned a wrong result
            """
            res = func_to_decorate(*args, **kwargs)
            if res is wrong_result:  # Arguments are accessed inside the decorator
                print "Call '{}(*{}, **{})' failed with return value {}".format(func_to_decorate.__name__,
                                                                                args, kwargs, res)
            return res
        return logging_wrapper
    return logger_decorator


@logger_decorator_factory(-1)
def dummy_function_1(*args, **kwargs):
    print "\tCalled dummy_function_1", args, kwargs
    return args[0]


@logger_decorator_factory(7)
def dummy_function_2(*args, **kwargs):
    print "\tCalled dummy_function_2", args, kwargs
    return args[0]

dummy_function_1(7)

dummy_function_1(-1, 1, two=2)

dummy_function_2(7)

dummy_function_2(-1, 1, two=2)


#===============================================================================
# - Use a decorator factory to pass arguments to the decorator
#    - Remember to call the factory when decorating
#===============================================================================


# We said that a decorator is a callable, so...


class CounterDecorator(object):
    def __init__(self, func_to_decorate):
        print "Instantiated", self.__class__.__name__
        self.func = func_to_decorate
        self.raised = self.succeeded = self.failed = 0  # We can store decorator state

    def __call__(self, *args, **kwargs):  # Let me introduce the callables protocol!
        print "Called", self.__class__.__name__, "instance"
        try:
            res = self.func(*args, **kwargs)
            if res:
                self.succeeded += 1  # Decorator state can be accessed anywhere
            else:
                self.failed += 1
            return res
        except Exception, e:
            self.raised += 1
            raise


#===============================================================================
# - __call__ method is called when the instance is "called" as a function
#    - If this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
#    - More about this in module 06 (objects Data Model)
#===============================================================================


@CounterDecorator
def dummy_function_3(*args, **kwargs):
    print "\tCalled dummy_function_3", args, kwargs
    if isinstance(args[0], Exception):
        raise args[0]
    return args[0]


# What is right now 'dummy_function_3'?

print dummy_function_3


dummy_function_3(None)

dummy_function_3(1, 2, 3)

dummy_function_3("a")

dummy_function_3(TypeError())


# Ok but... where are the accumulated values?


# They are instance attributes, of course
print "SUCCEEDED", dummy_function_3.succeeded
print "FAILED", dummy_function_3.failed
print "RAISED", dummy_function_3.raised


#===============================================================================
# - Use a callable class (with __call__ method) to store the state of the decorator
#    - It is not possible to use functools.wraps
#===============================================================================


# And there is still more


class RetryDecoratorFactory(object):  # Decorator arguments are provided here
    def __init__(self, times):
        print "Instantiated", self.__class__.__name__, "with", times
        self.times = times  # We can store decorator state

    def __call__(self, func_to_decorate):
        print "Called", self.__class__.__name__, "instance"

        @functools.wraps(func_to_decorate)
        def logging_wrapper(*args, **kwargs):
            """Wrapper to print a log trace in case function returned a wrong result
            """
            for i in xrange(self.times):
                res = func_to_decorate(*args, **kwargs)
                if res:
                    return res
                print "Call '{}(*{}, **{})' failed with return value {}. Retrying".format(func_to_decorate.__name__,
                                                                                          args, kwargs, res)
        return logging_wrapper


@RetryDecoratorFactory(3)
def dummy_function_4(x, y):
    print "\tCalled dummy_function_4", x, y
    from random import seed, randint
    seed()
    return randint(x, y) % 2


# What is right now 'dummy_function_4'?

print dummy_function_4


dummy_function_4(0, 9)

dummy_function_4(0, 9)


#===============================================================================
# - Instantiate a callable class (with __call__ method) to pass arguments to decorator
#   and also store its internal state (not accessible from outside though)
#    - Remember to instantiate the class when decorating
#===============================================================================


#==============================================================================
# - There are still other options...
#    - Decorator class with mutable class attributes
#    - Decorate classes!!
#==============================================================================


# It's time for a bit of practice


#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_04_advanced_decorators/exercise_mod_04
#
# - Use memoization to speed up factorial and fibonacci computation
#     - Take care to not share the same cache for both
#     - Ideally it should be possible to specify different cache setup for each decorated function
#
# - Run the tests in 'tests_mod_04.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_04.py'
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://stackoverflow.com/a/1594484
#  - http://wiki.python.org/moin/PythonDecoratorLibrary
#  - http://docs.python.org/2/reference/datamodel.html#object.__call__
#===============================================================================
