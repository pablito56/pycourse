#!/usr/bin/env python
#-*- coding: utf-8 -*-
u'''
MOD: Logging solution: enhance performance creating encoder / decoder instances or other json libraries

Results in MacBook Pro 13" 2.4Ghz i5 8Gb:
$ python exercises/mod_json/timeit_json.py
TIMING JSON NO INSTANCE (100000 times): 10.36147
TIMING JSON WITH INSTANCE (100000 times): 10.21998
TIMING SIMPLEJSON NO INSTANCE (100000 times): 10.13344
TIMING SIMPLEJSON WITH INSTANCE (100000 times): 9.25303
TIMING UJSON NO INSTANCE (100000 times): 2.53635
'''

import json
import simplejson
import ujson
import timeit


MIN_DIFFERENCE = 5


ENCODED = """{
    "lk_location": {
        "long": 2.2205954,
        "lat": 41.4121694
    },
    "timestamp": "2013-02-22T12:21:05",
    "screen": true,
    "inst_apps": [
        "la.droid.qr",
        "com.shazam.android",
        "com.evernote",
        "com.eurosport",
        "com.whatsapp",
        "com.linkedin.android"
    ],
    "run_apps": [
        "com.android.chrome",
        "com.google.android.apps.translate",
        "com.google.android.apps.maps",
        "com.eurosport"
    ]
}"""
DATA = {
    "lk_location": {
        "long": 2.2205954,
        "lat": 41.4121694
    },
    "timestamp": "2013-02-22T12:21:05",
    "screen": True,
    "inst_apps": [
        "la.droid.qr",
        "com.shazam.android",
        "com.evernote",
        "com.eurosport",
        "com.whatsapp",
        "com.linkedin.android"
    ],
    "run_apps": [
        "com.android.chrome",
        "com.google.android.apps.translate",
        "com.google.android.apps.maps",
        "com.eurosport"
    ]
}


json_encoder = None
json_decoder = None


simplejson_encoder = None
simplejson_decoder = None


def json_no_instance():
    """Execute 3 times encoding and decoding wih json (no instance created)
    """
    enc1 = json.loads(ENCODED)
    enc2 = json.loads(ENCODED)
    enc3 = json.loads(ENCODED)
    dec1 = json.dumps(DATA)
    dec2 = json.dumps(DATA)
    dec3 = json.dumps(DATA)


def json_w_instance():
    """Execute 3 times encoding and decoding wih json creating instances
    """
    enc1 = json.loads(ENCODED)
    enc2 = json.loads(ENCODED)
    enc3 = json.loads(ENCODED)
    dec1 = json.dumps(DATA)
    dec2 = json.dumps(DATA)
    dec3 = json.dumps(DATA)


def simplejson_no_instance():
    """Execute 3 times encoding and decoding wih simplejson (no instance created)
    """
    enc1 = json.loads(ENCODED)
    enc2 = json.loads(ENCODED)
    enc3 = json.loads(ENCODED)
    dec1 = json.dumps(DATA)
    dec2 = json.dumps(DATA)
    dec3 = json.dumps(DATA)


def simplejson_w_instance():
    """Execute 3 times encoding and decoding wih simplejson creating instances
    """
    enc1 = json.loads(ENCODED)
    enc2 = json.loads(ENCODED)
    enc3 = json.loads(ENCODED)
    dec1 = json.dumps(DATA)
    dec2 = json.dumps(DATA)
    dec3 = json.dumps(DATA)


def ujson_no_instance():
    """Execute 3 times encoding and decoding wih ujson
    """
    enc1 = json.loads(ENCODED)
    enc2 = json.loads(ENCODED)
    enc3 = json.loads(ENCODED)
    dec1 = json.dumps(DATA)
    dec2 = json.dumps(DATA)
    dec3 = json.dumps(DATA)


def timeit_json():
    num_times = 100000

    t_json_no_inst = timeit.timeit(json_no_instance, number=num_times)
    print "TIMING JSON NO INSTANCE ({} times): {:.5f}".format(num_times, t_json_no_inst)

    t_json_w_inst = timeit.timeit(json_w_instance, number=num_times)
    print "TIMING JSON WITH INSTANCE ({} times): {:.5f}".format(num_times, t_json_w_inst)

    t_simplejson_no_inst = timeit.timeit(simplejson_no_instance, number=num_times)
    print "TIMING SIMPLEJSON NO INSTANCE ({} times): {:.5f}".format(num_times, t_simplejson_no_inst)

    t_simplejson_w_inst = timeit.timeit(simplejson_w_instance, number=num_times)
    print "TIMING SIMPLEJSON WITH INSTANCE ({} times): {:.5f}".format(num_times, t_simplejson_w_inst)

    t_ujson_no_inst = timeit.timeit(ujson_no_instance, number=num_times)
    print "TIMING UJSON NO INSTANCE ({} times): {:.5f}".format(num_times, t_ujson_no_inst)

    assert t_json_no_inst > t_json_w_inst
    assert t_simplejson_no_inst > t_simplejson_w_inst
    assert t_json_w_inst > t_ujson_no_inst + MIN_DIFFERENCE
    assert t_simplejson_w_inst > t_ujson_no_inst + MIN_DIFFERENCE


if __name__ == '__main__':
    timeit_json()
