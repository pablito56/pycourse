#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 02: Functional programming and iterables tools tests
"""

import unittest
import exercise as source
# import solution as source


class TestFunctionalTools(unittest.TestCase):

    def test_validate_external_endpoints(self):
        """Test validate_external_endpoints(ENDPOINTS) returns True
        """
        self.assertTrue(source.validate_external_endpoints(source.ENDPOINTS))

    def test_validate_external_endpoints_wrong(self):
        """Test validate_external_endpoints(endpoints) returns False
        """
        endpoints = [{"ipv4": ["10.95.150.121"], "ipv6": ["fd88:3be1:fee4:8c5c::aa3"], "port": None, "region": 2,
                      "wowza": {"ipv4": ["10.95.150.81"], "ipv6": ["fd88:3be1:fee4:8c5c::2b"]}}]
        self.assertFalse(source.validate_external_endpoints(endpoints))

    def test_validate_endpoint_resolution(self):
        """Test validate_endpoint_resolution(ENDPOINTS, RESOLUTIONS) returns True
        """
        self.assertTrue(source.validate_endpoint_resolution(source.ENDPOINTS, source.RESOLUTION))

    def test_validate_endpoint_resolution_wrong(self):
        """Test validate_endpoint_resolution(ENDPOINTS, resolutions) returns False
        """
        resolution = """10.95.150.94\n10.95.151.60\n10.95.150.91\nfd88:3be1:fee4:8c5d::63\nfd88:3be1:fee4:8c5c::2c"""
        self.assertFalse(source.validate_endpoint_resolution(source.ENDPOINTS, resolution))

    def test_validate_not_enabled_buckest(self):
        """Test source.validate_not_enabled_buckest()
        """
        self.assertEqual(source.validate_not_enabled_buckest(), [2, 3, 5])

    def test_flatten_nested_lists(self):
        """Test source.flatten_nested_lists([1, 2, [3, 4, [[5, 6], 7], 8, 9, 10], 11, 12])
        """
        l = [1, 2, [3, 4, [[5, 6], 7], 8, 9, 10], 11, 12]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(source.flatten_nested_lists(l), expected)

    def test_flatten_nested_lists_plain(self):
        """Test source.flatten_nested_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        """
        l = expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(source.flatten_nested_lists(l), expected)


if __name__ == "__main__":
    #import sys;sys.argv = ["", "Test.testName"]
    unittest.main()
