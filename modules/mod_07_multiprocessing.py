#-*- coding: utf-8 -*-
u"""
MOD: Multiprocessing
"""

import multiprocessing


#===============================================================================
# This module provides features to spawn processes with an API similar to threading
#    module. The processes avoid GIL related performance issues by using subprocesses
#    instead of threads.
#===============================================================================


import requests
from pprint import pprint


def get_weather(num):
    location = "41.41,2.22"
    key = "5nrhptjvus6gdnf9e6x75as9"
    num_days = 3
    url_pattern = "http://api.worldweatheronline.com/free/v1/weather.ashx?q={loc}&format=json&num_of_days={days}&key={key}"
    r = requests.get(url=url_pattern.format(loc=location, days=num_days, key=key),
                     headers={'content-type': 'application/json'})
    print "GET WEATHER", num
    pprint(r.json()["data"]["current_condition"][0])


def get_weather_3x_mp():
    p = multiprocessing.Pool(3)
    p.map(get_weather, range(3))


#===============================================================================
# WARNING: Multiprocessing requires that the __main__ module be importable by the
#    children, so it's not possible to use inside any kind of interpreter.
#===============================================================================


#===========================================================================
# EXERCISE:
# - Execute the script 'mod_multiprocessing/mod_mp_requests.py':
#    $ python mod_multiprocessing/mod_mp_requests.py
#
# - Execute the script 'mod_multiprocessing/mod_mp_fibonacci.py':
#    $ python mod_multiprocessing/mod_mp_fibonacci.py
#
# - Compare the results
#===========================================================================


#===============================================================================
# - In CPU-bounded operations multiprocessing really beats threading or any other
#    asynchronous alternative
#
# - The module also provides a 'Process' class, similar to 'threading.Thread'
#
# - It also provides inter-processes communications mechanisms, even to exchange
#    objects, but they can reduce the performance dramatically
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/multiprocessing.html
#  - http://pymotw.com/2/multiprocessing/index.html
#===============================================================================
