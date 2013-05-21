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
# SOURCES:
#  - http://docs.python.org/2/library/unittest.html
#  - http://pymotw.com/2/unittest/index.html
#===============================================================================
