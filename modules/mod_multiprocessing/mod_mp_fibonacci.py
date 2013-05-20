#-*- coding: utf-8 -*-
u"""
MOD: Multiprocessing with requests
"""

import multiprocessing
import requests
import threading


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_fibonacci(num):
    fib = fibonacci(30 + num)
    print "GET FIBONACCI", num, fib


def get_fibonacci_3x_mp():
    p = multiprocessing.Pool(3)
    p.map(get_fibonacci, range(3))


def get_fibonacci_3x_th():
    threads = []
    for i in range(3):
        t = threading.Thread(target=get_fibonacci, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    import time
    start_th = time.time()
    get_fibonacci_3x_th()
    end_th = time.time()
    start_mp = time.time()
    p = multiprocessing.Pool(3)
    p.map(get_fibonacci, range(3))
    end_mp = time.time()
    print "ELAPSED THREADING: {:.5f} seconds".format(end_th - start_th)
    print "ELAPSED MULTIPROCESSING: {:.5f} seconds".format(end_mp - start_mp)
