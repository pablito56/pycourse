#-*- coding: utf-8 -*-
u'''
MOD 02: Functional programming and iterables tools exercise
'''

import json


ENDPOINTS = [{"ipv4": ["10.95.150.121"], "ipv6": ["fd88:3be1:fee4:8c5c::2a"], "port": None, "region": 1,
              "wowza": {"ipv4": ["10.95.150.81"], "ipv6": ["fd88:3be1:fee4:8c5c::2b"]}},
             {"ipv4": ["10.95.150.84"], "ipv6": ["fd88:3be1:fee4:8c5f::30"], "port": None, "region": 1,
              "wowza": {"ipv4": ["10.95.151.60"], "ipv6": ["fd88:3be1:fee4:8c5d::63"]}},
             {"ipv4": ["10.95.150.122"], "ipv6": ["fd88:3be1:fee4:8c5d::2c"], "port": None, "region": 2,
              "wowza": {"ipv4": ["10.95.150.82"], "ipv6": ["fd88:3be1:fee4:8c5d::2d"]}},
             {"ipv4": ["10.95.150.123"], "ipv6": ["fd88:3be1:fee4:8c5d::2e"], "port": None, "region": 2,
              "wowza": {"ipv4": ["10.95.150.83"], "ipv6": ["fd88:3be1:fee4:8c5d::2f"]}}]

RESOLUTION = """10.95.150.84\n10.95.151.60\n10.95.150.81\nfd88:3be1:fee4:8c5d::63\nfd88:3be1:fee4:8c5c::2b"""


def load_json_file(filename="report.json"):
    """Load JSON file and deserialize it
    :param filename: name of the JSON file to load
    :returns: dict with the JSON content
    """
    with open(filename, "r") as f:
        encoded_json = f.read()
        return json.loads(encoded_json)


def validate_external_endpoints(endpoints=ENDPOINTS):
    """Validate that all region 2 endpoints have been shared in external_endpoints
    #1 In report.json, you can find an external_endpoints sections which determines external endpoints that have
        been shared to a particular region. Find it.
    #2 We provide the metadata of several endpoint on global name ENDPOINTS
    #3 Implement a test that checks that both endpoints from region 2 have been shared
    :returns: True if all region 2 endpoints have been shared, False otherwise
    """
    return None


def validate_endpoint_resolution(endpoints=ENDPOINTS, resolution=RESOLUTION):
    """
    #1 RESOLUTION global contains a resolution of endpoints, so each IP is a valid EP
    #2 ENDPOINTS global contains the metadata info of several Endpoints
    #3 Implement a test that checks that wowzas endpoints from region #1 have been resolved
    """
    return None


def validate_not_enabled_buckest():
    """
    #1 In report.json you can find a relation of buckets. Check it.
    #2 Implement a test that certifies that the not enabled buckets are 2,3 and 5
    :returns: list with the id of not enabled buckets
    """
    return []


def flatten_nested_lists(l):
    """Flatten nested lists into one single list

    >>> flatten_nested_lists([1, 2, [3, 4, [[5, 6], 7], 8, 9, 10], 11, 12])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    :param l: list to flatten
    :returns: new flattened list
    """
    return []
