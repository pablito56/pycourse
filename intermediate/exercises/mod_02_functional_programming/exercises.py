#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: exercises involving functional functions
'''
ENDPOINTS = ["ipv4" : ["10.95.150.121"], "ipv6" : ["fd88:3be1:fee4:8c5c::2a"], "port" : null, "region" : 1, 
             "wowza" : {"ipv4" : ["10.95.150.81"], "ipv6" : ["fd88:3be1:fee4:8c5c::2b"]}}, 
            {"ipv4" : ["10.95.150.84"], "ipv6" : ["fd88:3be1:fee4:8c5f::30"], "port" : null, "region" : 1, 
             "wowza" : {"ipv4" : ["10.95.151.60"], "ipv6" : ["fd88:3be1:fee4:8c5d::63"]}},
            {"ipv4" : ["10.95.150.122"], "ipv6" : ["fd88:3be1:fee4:8c5d::2d"], "port" : null, "region" : 2, 
             "wowza" : {"ipv4" : ["10.95.150.82"], "ipv6" : ["fd88:3be1:fee4:8c5d::2c"]}},
            {"ipv4" : ["10.95.150.123"], "ipv6" : ["fd88:3be1:fee4:8c5d::2e"], "port" : null, "region" : 2, 
             "wowza" : {"ipv4" : ["10.95.150.83"], "ipv6" : ["fd88:3be1:fee4:8c5d::2f"]}}]


class FunctionalTest(unittest.Test):

    def test_external_endpoints(self):
        """ 
        #1 In report.json, you can find an external_endpoints sections which determines external endpoints that have
            been shared to a particular region. Find it.
        #2 We provide the metadata of endpoint on global name ENDPOINTS
        #3 Implement a test that checks that both endpoints from region 2 have been shared
        """
        pass

    def test_endpoint_resolution(self):
        """
        #1 below there is a resolution of endpoints, each IP is a valid EP
        #2 Above there is the metadata info of Endpoints with on global name ENDPOINTS
        #3 Implement a test that checks that wowzas endpoints from region #1 have been resolved
        """
        resolution = """10.95.150.84\n10.95.151.60\n10.95.150.81\nfd88:3be1:fee4:8c5d::63\nfd88:3be1:fee4:8c5c::2b"""
        pass

    def test_not_enabled_buckest(self):
        """
        #1 In report.json you can find a relation of buckets. Check it.
        #2 Implement a test that certifies that the not enabled buckets are 2,3 and 5
        """
        pass

