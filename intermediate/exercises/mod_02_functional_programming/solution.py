#-*- coding: utf-8 -*-
u'''
MOD 02: Functional programming and iterables tools solution
'''

from operator import itemgetter
from exercise import ENDPOINTS, RESOLUTION, load_json_file


def validate_external_endpoints(endpoints=ENDPOINTS):
    """Validate that all region 2 endpoints have been shared in external_endpoints
    #1 In report.json, you can find an external_endpoints sections which determines external endpoints that have
        been shared to a particular region. Find it.
    #2 We provide the metadata of several endpoint on global name ENDPOINTS
    #3 Implement a test that checks that both endpoints from region 2 have been shared
    :returns: True if all region 2 endpoints have been shared, False otherwise
    """
    data = load_json_file()
    externals_ips = map(itemgetter("ip"), data["external_endpoints"])
    region_2_eps = filter(lambda ep: ep["region"] == 2, endpoints)
    are_shared = map(lambda ep: ep["ipv6"][0] in externals_ips or ep["ipv4"][0] in externals_ips, region_2_eps)
    return all(are_shared)


def validate_endpoint_resolution(endpoints=ENDPOINTS, resolution=RESOLUTION):
    """
    #1 RESOLUTION global contains a resolution of endpoints, so each IP is a valid EP
    #2 ENDPOINTS global contains the metadata info of several Endpoints
    #3 Implement a test that checks that wowzas endpoints from region #1 have been resolved
    :returns: True if all region 1 wowzas have been resolved
    """
    resolved = resolution.split("\n")
    region_1_eps = filter(lambda ep: ep["region"] == 1, endpoints)
    region_1_wowzas = map(itemgetter("wowza"), region_1_eps)
    are_resolved = map(lambda w: w["ipv6"][0] in resolved or w["ipv4"][0] in resolved, region_1_wowzas)
    return all(are_resolved)


def validate_not_enabled_buckest():
    """
    #1 In report.json you can find a relation of buckets. Check it.
    #2 Implement a test that certifies that the not enabled buckets are 2,3 and 5
    :returns: list with the id of not enabled buckets
    """
    data = load_json_file()
    buckets = data["buckets"]
    buckets_id_not_enabled = map(lambda b: None if b["enabled"] else b["id"], buckets)
    buckets_not_enabled = filter(None, buckets_id_not_enabled)
    return buckets_not_enabled


def flatten_nested_lists(l):
    """Flatten nested lists into one single list

    >>> flatten_nested_lists([1, 2, [3, 4, [[5, 6], 7], 8, 9, 10], 11, 12])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    :param l: list to flatten
    :returns: new flattened list
    """
    res = []

    def flatten_reducer(accum_l, val):
        if isinstance(val, list):
            reduce(flatten_reducer, val, accum_l)
        else:
            accum_l.append(val)
        return accum_l
    return reduce(flatten_reducer, l, res)
