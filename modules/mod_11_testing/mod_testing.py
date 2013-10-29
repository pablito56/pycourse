#!/usr/bin/env python
#-*- coding: utf-8 -*-
u'''
MOD: Testing
'''


#===========================================================================
# EXERCISE:
# - Execute nosetests in this folder:
#    $ nosetests -sv
#
# - You can specify certain packages, modules, classes or tests. From parent folder:
#    $ nosetests -sv mod_11_testing
#    $ nosetests -sv mod_11_testing.mod_testing
#    $ nosetests -sv mod_11_testing.mod_testing:TestMyMathLib
#    $ nosetests -sv mod_11_testing.mod_testing:TestMyMathLib.test_sum
#===========================================================================


import unittest
import lib_to_test


# Some nosetests versions require 'test' to appear in the class name
class TestCaseExample(unittest.TestCase):
    """This is a tests class, grouping a bunch of tests
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass is executed BEFORE all class tests and setUps
        """
        print "SET_UP_CLASS"
        super(TestCaseExample, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        """tearDownClass is executed AFTER all class tests and tearDowns
        """
        print "TEAR_DOWN_CLASS"
        super(TestCaseExample, cls).tearDownClass()

    def setUp(self):
        """setUp is executed BEFORE each test
        """
        print "SET_UP"

    def tearDown(self):
        """tearDown is executed AFTER each test
        """
        print "TEAR_DOWN"

    # Some nosetests versions require 'test' to appear in the function name
    def test_sum(self):
        """This is an actual empty test
        """
        print "TESTING"


class TestMyMathLib(unittest.TestCase):
    """This is another tests class
    """

    def setUp(self):
        """setUp is executed BEFORE each test
        """
        self.x = 7
        self.y = 2

    # Some nosetests versions require 'test' to appear in the function name
    def test_sum(self):
        """This is an actual test
        """
        expected = 9
        # unittest.TestCase provides several assertion methods
        self.assertEqual(expected, lib_to_test.sum(self.x, self.y),
                         "Sum results differ")
        self.assertTrue(expected == lib_to_test.sum(self.x, self.y))  # Message is optional
        self.assertGreaterEqual(lib_to_test.sum(self.x, self.y), self.x)
        self.assertFalse(lib_to_test.sum(0, 0))
        self.assertIsNotNone(lib_to_test.sum(0, 0))

    # We can add as tests methods and classes as desired
    def test_subs(self):
        """Second test
        """
        x = [10, 20, 30]
        y = [1, 2, 3]
        expected = [9, 18, 27]
        expected_unordered = [9, 27, 18]
        # We can compare collections or sequences
        self.assertEqual(expected, map(lib_to_test.subs, x, y))
        self.assertItemsEqual(expected_unordered, map(lib_to_test.subs, x, y))

    # Classes and its tests are not executed in strict order
    def test_errors_raised(self):
        """Another test
        """
        # Check an exception is raised
        self.assertRaises(ZeroDivisionError, lib_to_test.div, self.x, 0)
        # Check an exception is raised and check exception content
        with self.assertRaises(ValueError) as exc_ctxt_mgr:
            lib_to_test.fail(self.x, self.y)
        self.assertEqual((self.x, self.y), exc_ctxt_mgr.exception.args)

    def test_which_fails(self):
        """This test will fail
        """
        self.assertTrue(False)

    def test_which_crashes(self):
        """This test will crash
        """
        self.assertTrue(lib_to_test.sum())


def setUpModule():
    """setUpModule is executed BEFORE all test classes
    """
    # Typically open connections, change settings
    print "SET_UP_MODULE"


def tearDownModule():
    """tearDownModule is executed AFTER all test classes
    """
    print "TEAR_DOWN_MODULE"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


#===============================================================================
# - Regarding mocking, in Python monkey patching classes is trivial. It is really
#    easy to replace instances methods or modules functions with your own stuff.
# - To use real full-featured mocks use the 'mock' library:
#    - http://www.voidspace.org.uk/python/mock/
#    - It was added to Python standard library in 3.3 as 'unittest.mock'
#        - http://docs.python.org/3/library/unittest.mock.html
#===============================================================================

#===============================================================================
# - mock library allows to replace parts of our code in a safe and easy way with 
#     - mock objects. You can assert how they are called too.
# - Base class is Mock although is advisable to use MagicMock subclass
#     - MagicMock has all "magic" methods already pre-created
# - patch utility allow to monkey patching at module and class level within the 
#     scope of test
# - Let's see a quick example 
#===============================================================================

from mock import MagicMock
from lib_to_test import ProductionClass
prod = ProductionClass()
prod.prod_method = MagicMock(return_value=3)
print prod.prod_method(40, 3)
prod.prod_method.assert_called_once_with(40, 3)

# with side_effect we can return several values and raise exceptions too
prod.prod_method = MagicMock(side_effect=ValueError("not number"))
prod.prod_method("my_string")


prod.prod_method = MagicMock(side_effect=[2, 3, 4])
prod.prod_method(34, 2)
prod.prod_method(34, 2)
prod.prod_method(34, 2)

# But we are modifying our source code, we better use patch
from mock import patch

# patch as decorator, provides MagicMock in function decorated
@patch('lib_to_test.ProductionClass')
def test(mockClass):
    lib_to_test.ProductionClass()  # Already imported in module..
    print 'ProductionClass {}'.format(lib_to_test.ProductionClass)
    assert mockClass is lib_to_test.ProductionClass
    print mockClass.called

test()

print lib_to_test.ProductionClass

# We can also use patch for system libraries...
import sys

# patch as context manager
with patch('sys.exit') as exitMock:
    try:
        sys.exit()
    except SystemExit:
        print "exiting programm"
    exitMock.assert_called_once_with()

try:
    sys.exit()
except SystemExit:
    print "exiting programm"

# we can patch some object, dict, open and magic methods....

my_patch = patch.object(prod, 'prod_method')
method_mock = my_patch.start()
method_mock.return_value = 5000
print prod.prod_method(30, 3)

# we stop the patch now ...
my_patch.stop()
print prod.prod_method(30, 3)

# WTF ??, yes before we change ProductionClass inside the module....
prod = ProductionClass()
my_patch = patch.object(prod, 'prod_method')
method_mock = my_patch.start()
method_mock.return_value = 5000
print prod.prod_method(30, 3)
my_patch.stop()
print prod.prod_method(30, 3)

# magic methods
mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
str(mock)
mock.__str__.assert_called_with()

# dictionary
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    print "dict foo is now: {}".format(foo)
    assert foo == {'newkey': 'newvalue'}

print "dict foo is {}".format(foo)
assert foo == original

# open function can be patched tooo....
from mock import mock_open

# write
with patch('__builtin__.open', mock_open()) as m:
    with open('foo.txt', 'w') as f:
        f.write('something')
    m.mock_calls

import os
os.path.exists('foo.txt')

# read
with patch('__builtin__.open', mock_open( read_data='foo')) as m:
    with open('foo.txt') as f:
        file = f.read()
    print file

#===============================================================================
# To measure coverage run the nose collector in ../exercises folder with the options:
#    nosetests -s -v --with-cover --cover-package=mod_11_testing--cover-branches
#===============================================================================

#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/unittest.html
#  - http://pymotw.com/2/unittest/index.html
#  - http://www.voidspace.org.uk/python/mock/
#===============================================================================
