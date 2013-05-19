#!/usr/bin/env python
#-*- coding: utf-8 -*-
u'''
MOD: Logging solution: enhance performance using str.format or delegating interpolation to logging

Results in MacBook Pro 13" 2.4Ghz i5 8Gb:
$ python solution_timeit_logging.py
TIMING MANUAL INTERPOLATION LOGGING (1000000 times): 64.22650
TIMING MANUAL FORMATTING LOGGING (1000000 times): 62.92731
TIMING LOGGING INTERPOLATING LOGGING (1000000 times): 60.29762

Results without the logger.warning trace:
$ python solution_timeit_logging.py
TIMING MANUAL INTERPOLATION LOGGING (1000000 times): 6.57392
TIMING MANUAL FORMATTING LOGGING (1000000 times): 5.95113
TIMING LOGGING INTERPOLATING LOGGING (1000000 times): 3.67876
'''

import logging
import timeit


logging.basicConfig(filename='/tmp/test_logging.log', level=logging.DEBUG,
                    format="[%(process)d][%(levelname)s] %(asctime)s | %(module)s | %(message)s")
logger = logging.getLogger("timeit_logging")
logger.setLevel(logging.WARNING)


MIN_DIFFERENCE = 0.5


def manual_interpolation():
    """Execute string interpolation manually
    """
    logger.debug("This is a test. Func %s, level %s, num %d" % ("logging_interpolating", "DEBUG", 1234567))
    logger.debug("This is a test. Func %s, level %s, num %d" % ("logging_interpolating", "DEBUG", 1234567 * 2))
    logger.info("This is a test. Func %s, level %s, num %d" % ("logging_interpolating", "INFO", 7654321))
#     logger.warning("This is a test. Func %s, level %s, num %d" % ("logging_interpolating", "WARNING", 1000000))


def manual_formatting():
    """Execute string formatting (str.format) manually
    """
    logger.debug("This is a test. Func {}, level {}, num {}".format("logging_interpolating", "DEBUG", 1234567))
    logger.debug("This is a test. Func {}, level {}, num {}".format("logging_interpolating", "DEBUG", 1234567 * 2))
    logger.info("This is a test. Func {}, level {}, num {}".format("logging_interpolating", "INFO", 7654321))
#     logger.warning("This is a test. Func {}, level {}, num {}".format("logging_interpolating", "WARNING", 1000000))


def logging_interpolating():
    """Delegate string interpolation to logging module
    """
    logger.debug("This is a test. Func %s, level %s, num %d", "logging_interpolating", "DEBUG", 1234567)
    logger.debug("This is a test. Func %s, level %s, num %d", "logging_interpolating", "DEBUG", 1234567 * 2)
    logger.info("This is a test. Func %s, level %s, num %d", "logging_interpolating", "INFO", 7654321)
#     logger.warning("This is a test. Func %s, level %s, num %d", "logging_interpolating", "WARNING", 1000000)


def timeit_logging():
    num_times = 1000000

    t_manual_int = timeit.timeit(manual_interpolation, number=num_times)
    print "TIMING MANUAL INTERPOLATION LOGGING ({} times): {:.5f}".format(num_times, t_manual_int)

    t_manual_form = timeit.timeit(manual_formatting, number=num_times)
    print "TIMING MANUAL FORMATTING LOGGING ({} times): {:.5f}".format(num_times, t_manual_form)

    t_logging_int = timeit.timeit(logging_interpolating, number=num_times)
    print "TIMING LOGGING INTERPOLATING LOGGING ({} times): {:.5f}".format(num_times, t_logging_int)

    assert t_manual_int > t_manual_form + MIN_DIFFERENCE
    assert t_manual_form > t_logging_int + MIN_DIFFERENCE


if __name__ == '__main__':
    timeit_logging()
