#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod: gevent module
'''

#==========================================================================================
#
#  gevent is a Python networking library that uses greenlet to provide a synchronous
#       API on top of libevent event loop.
#
#
#==========================================================================================



#==========================================================================================
#
#  greenlets
#
#   A greenlet is a small independent pseudo-thread.
#       Think about it as a small stack of frames; the outermost (bottom) frame is the initial function you called,
#       and the innermost frame is the one in which the greenlet is currently paused.
#
#   You work with greenlets by creating a number of such stacks and jumping execution between them.
#   Jumps are never implicit: a greenlet must choose to jump to another greenlet,
#   which will cause the former to suspend and the latter to resume where it was suspended.
#   Jumping between greenlets is called switching
#
#==========================================================================================



from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)


gr1.switch()


# Note that 78 is never printed


#==========================================================================================
#
#  Gevent: a python networking library with
#   - fast event loop based on libevent (for 1.0 will be libev)
#   - using greenlet for lightweight execution units
#   - cooperative socket and ssl modules
#
#==========================================================================================


import gevent
import gevent.socket

urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(gevent.socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)
[job.value for job in jobs]


# gevent.spawn
# The greenlets are spawned by creating a Greenlet instance and calling its start method.
# (The spawn() function is a shortcut that does exactly that).
gevent.spawn(lambda: 1 / 0)


# The start method schedules an event that will switch to the greenlet created,
# as soon as the current greenlet gives up control.
# If there is more than one active event, they will be executed one by one,
# in an undefined order.

gevent.sleep(1)


#==========================================================================================
#
#  let's work with http requests
#
#==========================================================================================


import time
import urllib2
import socket  # important because it might have been patched by gevent.socket
import requests
import gevent

urls = ['http://www.heroku.com',
        'http://python-tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com',
        'http://www.gevent.org',
        'http://www.python.org']


def by_requests():
    jobs = [requests.get(x) for x in urls]


def by_urllib2():
    jobs = [gevent.spawn(urllib2.urlopen, u) for u in urls]
    gevent.joinall(jobs)


from timeit import Timer
t_by_requests = Timer(stmt=by_requests)
t_by_urllib2 = Timer(stmt=by_urllib2)
print 'by requests: {} seconds'.format(t_by_requests.timeit(number=3))
print 'by urllib2: {} seconds'.format(t_by_urllib2.timeit(number=3))


from gevent import monkey; monkey.patch_all()
print 'by requests: {} seconds'.format(t_by_requests.timeit(number=3))
print 'by urllib2: {} seconds'.format(t_by_urllib2.timeit(number=3))


#==========================================================================================
#
#  Gevent: a python networking library with
#   - fast event loop based on libevent (for 1.0 will be libev)
#   - using greenlet for lightweight execution units
#   - cooperative socket and ssl modules
#   - Ability to use standard library and 3rd party modules
#       written for standard blocking sockets (gevent.monkey).
#
# - There is an initiative to create a standard asynchronous I/O library
#    integrated in the core for Python 3.4, with its lightweight event loop
#        - Tulip: http://www.python.org/dev/peps/pep-3156/
#
#==========================================================================================


# requests it is not what we expected
import grequests


def by_grequests():
    jobs = (grequests.get(x) for x in urls)
    grequests.map(jobs)

t_by_grequests = Timer(stmt=by_grequests)
print 'by requests: %s seconds' % t_by_grequests.timeit(number=3)


#===============================================================================
# SOURCES:
#  - http://www.gevent.org
#  - https://github.com/kennethreitz/grequests
#  - http://greenlet.readthedocs.org/en/latest/
#===============================================================================
