pycourse
========
 

Python course structured in 4 big blocks: basic, intermediate, advanced and utilities.

It starts from the very beginning, explaining what is Python and its basic data types and structures, and ends explaining advanced language features such as descriptors or metaclasses. As a bonus, the last block covers the most useful Python's standard library or 3rd party modules and utilities (logging, profiling, DBs drivers, Json parsing, etc).

Each block contains explanations, examples and exercises and is designed to be taught in about 8 hours (including time to solve the exercises). However, all the contents are fully documented and it is possible to follow them on your own.


# Course contents


## BASIC BLOCK:

* 00: What is Python?
* 01: Python history and versions
* 02: Tools and environment
* 03: Numbers
* 04: Strings
* 05: Collections
* 06: Dictionaries
* 07: Booleans
* 08: Flow control
* 09: List and dict comprehension
* 10: Functions
* 11: Classes
* 12: Modules and packages


## INTERMEDIATE BLOCK:
* 01: Mutables vs. immutables
* 02: Functional programming and iterables tools
* 03: Attributes look up
* 04: Objects data model customisation
* 05: Iterators and generators
* 06: Advanced generators, yield and itertools
* 07: Context managers and contextlib
* 08: Duck typing
* 09: Way of working


## ADVANCED BLOCK:
* 01: Namespaces and scopes
* 02: Globals and locals
* 03: Decorators
* 04: Advanced decorators
* 05: Functools module
* 06: Cooperative super call pattern (MRO and super)
* 07: Descriptors protocol
* 08: Slots and properties
* 09: Constructors and metaclasses
* 10: Common Java developers errors


## MODULES BLOCK:

* 01: Profiling and timing: profile, cprofile, timeit, plop
* 02: Standatd library: most useful modules
  * 02.1: time and datetime
  * 02.2: System and filesystem access: sys, os, shutil, subprocess and atexit
  * 02.3: Json handling: json, simplejson and ujson
  * 02.4: logging
  * 02.5: Command line arguments parsing: argparse
  * 02.5: Configuration files parsing: configparser
* 03: Network utilities: socket, urllib2, httplib, urlparse and requests
* 04: MySQL official driver
* 05: MongoDB official driver
* 06: Threading and GIL
* 07: Multiprocessing
* 08: Gevent
* 09: Django and Django Rest Framework
* 08: Debugging: pdb and ipdb
* 11: Testing
* 12: Remote access: fabric and paramiko
* 13: Packaging and distribution: distribute


> **DISCLAIMER:** Initially the course was planned in 3 blocks and it was imparted 3 times. However, based on the feedback of the attendees, it was split into 4 sessions of around 8 hours each. This way, some modules content was enlarged, more exercises were added and more time to solve the exercises was allocated.
> 
> You can find the old 3-sessions version in this tag: https://github.com/pablito56/pycourse/tree/v1.0_FirstRound


# Usage

All the course content is written down in Python scripts and designed to be executed with [pydemo](https://github.com/pablito56/pydemo "pydemo GitHub repository") interactive interpreter:
```shell
me@my_laptop:~/workspace/pycourse $ cd basic/
me@my_laptop:~/workspace/pycourse/basic $ pydemo mod_00_what_is_Python.py
Loaded 1 files, 7 code blocks
Python 2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(DemoHistoryConsole)
>>>
#-*- coding: utf-8 -*-
'''
MOD 00: What is Python?
'''

'\nMOD 00: What is Python?\n'
>>>
#===============================================================================
# EXERCISE: Execute the following command:
#     $ python -c "import this"
#===============================================================================

>>>
#===============================================================================
# From official website ( http://www.python.org/ ):
#
#     Python is a programming language that lets you work more quickly and integrate
#     your systems more effectively. You can learn to use Python and see almost
#     immediate gains in productivity and lower maintenance costs.
#
#===============================================================================

>>>
```

New explanations and examples will appear in the interpreter when pressing INTRO without introducing a command. It is also posible to manually execute other code to play around with the examples.
