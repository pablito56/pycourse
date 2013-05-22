#-*- coding: utf-8 -*-
u"""
MOD: Distribute
"""


#===============================================================================
# - Distribute is a fork of the Setuptools project.
#     - Distribute is intended to replace Setuptools as the standard method for
#        working with Python module distributions.
#
# - Setuptools: download, build, install, upgrade, and uninstall Python packages -- easily!
#
# - The main feature is the setup.py scripts calling 'setuptools.setup' function
#
# - There is an initiative to create a standard packaging and distribution tool
#    integrated in the core in Python 3.4 ( http://www.python.org/dev/peps/pep-0426/ )
#
#===============================================================================


#===========================================================================
# EXERCISE:
# - Download and decompress pep8 and requests eggs:
#    $ mkdir -p tmp_eggs
#    $ pip install -d tmp_eggs requests
#    $ pip install -d tmp_eggs requests
#    $ cd tmp_eggs
#    $ tar -xzvf requests-1.2.1.tar.gz
#    $ tar -xzvf pep8-1.4.5.tar.gz
#
# - Check their setup.py and how it calls the setup function:
#    $ less pep8-1.4.5/setup.py  # less or your favourite editor
#    $ less pep8-1.4.5/setup.py
#
# - Check...
#    - All the '*_requires' arguments
#    - The 'entry_points' argument in pep8
#    - The auxiliary functions used
#
# - Create pep8 egg and RPM
#    $ cd pep8-1.4.5
#    $ python setup.py  bdist_egg
#    $ python setup.py  bdist_rpm  # Requires rpm-build
#
#===========================================================================


#===============================================================================
# SOURCES:
#  - https://pypi.python.org/pypi/distribute
#  - https://pypi.python.org/pypi/setuptools/0.6c11
#===============================================================================
