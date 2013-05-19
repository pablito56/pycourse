#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD: Logging
"""


import logging


# Simplest example
logging.basicConfig(level=logging.INFO)
# Log traces using root logger
logging.debug("This is a DEBUG log trace which shouldn't be printed")
logging.info("This is an INFO log trace with standard config")


# You can log variables using old string interpolation format
logging.debug("This is a %s log trace. Times: %d", "DEBUG", 1)
logging.info("This is a %s log trace. Times: %d", "INFO", 2)


# logging module will execute the interpolation if required


# logging.basicConfig can take additional arguments:
logging.basicConfig(filename='app1.log', level=logging.INFO,
                    format="[%(process)d][%(levelname)s] %(asctime)s | %(module)s | %(message)s")


#===============================================================================
# - logging.basicConfig only has effect once (if no handlers are attached).
# - Logging setup applies to all modules. You don't have to call it from each module.
#    - This way you can modify logging setup of a 3rd party library
#===============================================================================


# However, to work with several modules you should use loggers with specific configurations


logger1 = logging.getLogger("root.module1")  # Typically: logger = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)
logger1.info("This is an INFO log trace of module %d", 1)


logger2 = logging.getLogger("root.module2")
logger2.setLevel(logging.WARNING)
logger2.info("This is an INFO log trace of module %d which shouldn't be printed", 2)


logger3 = logging.getLogger("root.module2.module3")
logger3.setLevel(logging.DEBUG)
logger3.info("This is an INFO log trace of module %d", 3)
logger3.debug("This is a DEBUG log trace of module %d", 3)


# You can setup different handlers


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console1 = logging.StreamHandler()  # Console handler
console1.setLevel(logging.DEBUG)
fmtr1 = logging.Formatter("[%(process)d][%(levelname)s] %(asctime)s | %(module)s | %(message)s")
console1.setFormatter(fmtr1)

logger.addHandler(console1)

console2 = logging.StreamHandler()  # Another console handler
console2.setLevel(logging.INFO)
fmtr2 = logging.Formatter("%(levelname)s @ %(asctime)s --> %(message)s")
console2.setFormatter(fmtr2)

logger.addHandler(console2)


fh = logging.FileHandler(filename="mod_logging.log", mode="a")  # Let's log to a file
fh.setLevel(logging.WARNING)
fmtr3 = logging.Formatter("[%(levelname)s][%(asctime)s] %(message)s")
fh.setFormatter(fmtr3)

logger.addHandler(fh)


# Let's try it


logger.debug("THIS IS A DEBUG TRACE")


logger.info("THIS IS AN INFO TRACE")


logger.warning("THIS IS A WARNING TRACE")


#===============================================================================
# - Check logging.config to comnfigure your logs:
#    - logging.config.fileConfig to load setup from a file
#        http://docs.python.org/2/howto/logging.html#configuring-logging
#    - logging.config.dictConfig to load setup from a Python dictionary
#        http://docs.python.org/2/howto/logging-cookbook.html#an-example-dictionary-based-configuration
#===============================================================================


#===========================================================================
# EXERCISE:
# - Execute the file 'exercises/mod_logging/timeit_logging.py':
#    $ python exercises/mod_logging/timeit_logging.py
#
# - Modify functions 'manual_formatting' and 'logging_interpolating' to let
#    the assertions succeed
#===========================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/logging.html
#  - http://pymotw.com/2/logging/
#===============================================================================
