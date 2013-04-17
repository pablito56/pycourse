pycourse
========

Python course structured in 3 big bocks: basic, advanced and utilities


# Course content


## BASIC BLOCK (6 - 8h)

* 00: What is Python?
* 01: Python history and versions
* 02: Tools and environment
* 03: Numbers
* 04: Strings
* 05: Collections
* 06: Dictionaries
* 07: Booleans
* 08: Flow control
* 09: Functions
* 10: Iterators, comprehension and generators
* 11: Functional programming and iterables tools
* 12: Classes
* 13: Modules and packages
* 14: Duck typing
* 15: Mutables vs. immutables
* 16: Way of working


## ADVANCED BLOCK (6 – 8h)

* 01: Namespaces, scope, closures, global (nonglobal)
    * Revisit custom power function 
* 02: Decorators
    * Logging, trace, timing, retry...
* 02.5: Decorator classes, decorate classes
    * Memoization
* 03: Objects are dicts, `__dict__`, getattr / hasattr / setattr
* 04: Objects data model and customization (str, repr)
  * 05: Rich comparisson
  * 06: Numeric operations & coercion
  * 07: Attribute access
  * 08: Containers (key or index access, slicing, copy)
  * 09: Iterators / generators (yield) + patterns
  * 10: Context managers
* 11: Cooperative super call pattern: MRO and super
* 12: Descriptors protocol
* 13: Properties
* 14: Slots
* 15: Constructor and "destructor": `__new__` and `__del__`
* 16: Metaclasses
* 17: Common Java developers errors (getters and setters, abuse of staticmethod and classmethod, single class per module, fear to multiple inheritance, importing...)
* 18: Threads and GIL


## UTILITIES BLOCK (6 - 8h)

* Standatd library: useful functions: map, reduce, zip, globals, locals, all, filter…
* Standatd library: most useful modules
  * collections
  * ABC?
  * itertools
  * functools
  * contextlibs
  * datetime + tz
  * sys
  * os
  * json
  * inspect
  * cmd
  * logging
  * Files access: os.path, shutil
  * Commands execution: 
  * Paralelism: thread, multiprocessing, GIL
  * …
* Unit testing, mocking (dependency injection vs. mocking abuse)
* Debugging and profiling: ipdb, timeit, profile & cprofile, plop
* Packaging and distribution: setuptools and distutils, buildout
* Rremote access: fabric and paramiko
* 3rd parties:
  * virtualenv
  * Web development: Django, Django rest fwk, Tastypie
  * Asynch processing: gevent and Twisted
  * HTTP requests: requests
  * DB access: pymongo, python-mysql
  * …
