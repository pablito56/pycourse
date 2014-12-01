#-*- coding: utf-8 -*-
u"""
MOD: Threading and GIL
"""


import threading


#===============================================================================
# - This module provides a high-level interface for working with threads.
# - It relies on low-level 'thread' module.
#===============================================================================


# Let's launch some threads


def job(num):
    """Threaded function
    """
    print "Job {}".format(num)

threads = []
for num in range(3):
    th = threading.Thread(target=job, args=(num,))  # args is optional
    threads.append(th)
    th.start()


# Let's see how to identify the threads


def job_name(num):
    """Threaded function
    """
    name = threading.current_thread().getName()
    print "Job {}, name {}".format(num, name)

th0 = threading.Thread(target=job_name, args=(0,), name="MY-THREAD-0")
th1 = threading.Thread(target=job_name, args=(1,))

th0.start()
th1.start()

name = threading.current_thread().getName()
print "Main pogram, name {}".format(name)


#===============================================================================
# - By default threads would prevent main program from exiting until they finished
# - To avoid this behaviour launch the threads as daemon
#===============================================================================

from time import sleep


def sleeper():
    """Threaded sleeper
    """
    print "Threaded sleeper"
    sleep(180)

t = threading.Thread(target=sleeper, name="sleeper")
t.setDaemon(True)
t.start()


# Although it is possible to wait for a daemonized thread

from time import sleep


def sleeper5():
    """Threaded sleeper of 5 seconds
    """
    print "Threaded sleeper of 5 seconds"
    sleep(5)

t = threading.Thread(target=sleeper5, name="sleeper5")
t.setDaemon(True)
t.start()

t.join(2)
print t.isAlive()
t.join()
print t.isAlive()


# It is possible to retrieve all existent threads
for t in threading.enumerate():
    print t.getName(), t.isAlive()


# We can use signaling between threads

def wait_for_event(event):
    """Thread which waits for an event
    """
    received = event.wait()
    name = threading.current_thread().getName()
    print "Waited, got {}, name {}".format(received, name)


def wait_for_event_timeout(event):
    """Thread which waits for an event 2 seconds
    """
    received = event.wait(2)
    name = threading.current_thread().getName()
    print "Waited with timeout, got {}, name {}".format(received, name)


event = threading.Event()
t1 = threading.Thread(target=wait_for_event, name="wait_for_event", args=(event,))
t1.start()
t2 = threading.Thread(target=wait_for_event_timeout, name="wait_for_event_timeout", args=(event,))
t2.start()

sleep(3)
event.set()


#===============================================================================
# - In a similar way, threading also provides 'Lock', 'Condition' and 'Semaphore'
#    to synchronize threads, control access to resources...
#===============================================================================


# Let's try to run fibonacci


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_30_25():
    fibonacci(30)
    fibonacci(25)


import timeit
print "Elapsed:", timeit.timeit(fib_30_25, number=10)


def fib_30_25_th():
    th1 = threading.Thread(target=fibonacci, args=(30,))
    th2 = threading.Thread(target=fibonacci, args=(25,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()


# What do you expect to be the time spent now?


print "Elapsed threaded:", timeit.timeit(fib_30_25_th, number=10)


# What? Let's try again


print "Elapsed threaded:", timeit.timeit(fib_30_25_th, number=10)


print "Elapsed threaded:", timeit.timeit(fib_30_25_th, number=10)


#===============================================================================
# Why the threaded version is slower? Any idea?
#===============================================================================


#===============================================================================
# Python's Global Interpreter Lock or GIL:
#
# - The Python interpreter is not fully thread-safe.
# - There's a global lock, called the global interpreter lock or GIL.
# - It must be held by a thread before it can safely access Python objects.
# - Without the lock, even the simplest operations could cause problems in
#     a multi-threaded program.
#
# - I/O releases the GIL
# - To emulate concurrency of execution, the interpreter regularly tries to
#     switch threads.
#
# - sys.setcheckinterval(interval=100): Set the interpreter's "check interval",
#     in number ticks (Python virtual insctructions aprox).
#     - Large value may increase performance of threads.
#     - Low value may increase responsiveness as well as overhead.
#===============================================================================


#===============================================================================
# - In Python 3.3 GIL was changed to enhance performance in context changes
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/threading.html
#  - http://docs.python.org/2/library/thread.html
#  - http://wiki.python.org/moin/GlobalInterpreterLock
#  - http://docs.python.org/2/library/sys.html#sys.setcheckinterval
#===============================================================================
