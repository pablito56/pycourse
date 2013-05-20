#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 03: network
"""


#===============================================================================
# Standard library provides some modules for network operation:
#
#    - socket: provides access to the low-level C BSD socket interface, includes
#        a 'socket' class and some useful functions
#
#    - urllib2: a library to perform HTTP requests (get, post, multipart...)
#
#    - httplib: client side libraries of HTTP and HTTPS protocols, used by urllib2
#
#    - urlparse: library with functions to parse URLs
#
#    - Note that in Py3k urlparse, urllib and urllib2 have been merged in pacakge urllib
#===============================================================================


import socket


# In addition to typical socket class, some useful functions are provided
print socket.gethostname()
print socket.getfqdn()
print socket.gethostbyname(socket.getfqdn())


# Let's see how to perform HTTP requests


import requests  # Requests is much better than any other standard library alternative


location = "41.41,2.22"
key = "5nrhptjvus6gdnf9e6x75as9"
num_days = 3
url_pattern = "http://api.worldweatheronline.com/free/v1/weather.ashx?q={loc}&format=json&num_of_days={days}&key={key}"
r = requests.get(url=url_pattern.format(loc=location, days=num_days, key=key),
                 headers={'content-type': 'application/json'})  # It supports all HTTP methods, auth, proxies, post multipart...

# Let's check the response
print r.status_code
print r.encoding
print r.text

# And of course it parses the JSON
print type(r.json())  # Uses simplejson or std lib json

from pprint import pprint
pprint(r.json()["data"]["current_condition"][0])


# compare it with using urllib2
# https://gist.github.com/kennethreitz/973705


#===============================================================================
# - For low level socket operations use 'socket'
# - Use 'requests' always if possible for HTTP operation
# - Use 'urllib2' or 'httplib' as a fallback for special behaviour
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/socket.html
#  - http://pymotw.com/2/socket/
#  - http://docs.python.org/2/library/urllib2.html
#  - http://pymotw.com/2/urllib2/
#  - http://docs.python.org/2/library/httplib.html
#  - http://docs.python-requests.org/en/latest/
#===============================================================================
