#-*- coding: utf-8 -*-
u'''
MOD 09: Way of working: next steps
'''

#===============================================================================
# Install pip
#
#    - pip is used to list, search, install, upgrade and uninstall packages from
#      PyPi, GitHub, or other VCSs
#    - easy_install is a simple installer from PyPi. It comes with setuptools 
#    - setuptools has recently merged distribute, which was a fork of setuptools. 
#       this versions is Py3k compatible.
#      Both are a library to build, package and install Python projects.
#        - A new packaging system is being implemented integrated in the std lib
#
#    - If you don't have pip in your OS package system, the easiest way is:
#        - Install distribute or setuptools
#        - Install pip with easy_install:
#         $ sudo easy_install pip
#===============================================================================


#===============================================================================
# Install virtualenv
#
#     - virtualenv is used to isolate environments
#         - different projects, POCs and spikes, different Python versions
#     - When Python interpreter starts it loads os and site-packages using relative paths
#        regarding the binary location
#         - For virtualenv it is enough to copy all this relative paths together with the binary
#     - It comes with pip installed
#
#     - Install it with pip:
#         $ sudo pip install virtualenv
#===============================================================================


#===============================================================================
# Use virtualenv
#
#     - Create a new environment:
#         $ virtualenv venvs/pycourse
#
#     - Create a new environment with different Python version:
#         $ which python3.3
#            /usr/local/bin/python3.3
#         $ virtualenv venvs/pycourse3.3 -p /usr/local/bin/python3.3
#
#     - Enable the virtualenv:
#         $ echo $PATH
#            /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:...
#         $ source venvs/pycourse/bin/activate
#         $ echo $PATH
#            /Users/pev/venvs/pycourse/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:...
#
#     - Disable the virtualenv:
#         $ deactivate
#===============================================================================


#===============================================================================
# Use pip (inside virtualenvs)
#
#    - List installed packages:
#         $ pip freeze
#            wsgiref==0.1.2
#
#    - Install new packages:
#         $ pip search pep8
#            wsgiref==0.1.2
#            autopep8                  - A tool that automatically formats Python code...
#            pep8                      - Python style guide checker
#            ...
#         $ pip install pep8
#            Downloading/unpacking pep8
#              Downloading pep8-1.4.5.tar.gz (63kB): 63kB downloaded
#              Running setup.py egg_info for package pep8
#            ...
#            Successfully installed pep8
#            Cleaning up...
#         $ pip freeze
#            wsgiref==0.1.2
#            pep8==1.4.4
#
#    - Install your project's requirements:
#         $ pip install -r requirements.txt
#            ...
#
#    - Create your project's requirements file:
#         $ pip freeze > requirements.txt
#===============================================================================


#===============================================================================
# Use PEP8
#
#     - PEP8 is the style guide for Python code
#     - Most IDEs integrate it
#     - In TID we accept 120 charactes per line (instead of 80)
#
#     - You can run and check code style from console
#         $ pep8 --max-line-length=119 .
#            ./file1.py:7:1: E302 expected 2 blank lines, found 1
#            ./file1.py:9:5: E301 expected 1 blank line, found 0
#            ./file2.py:11:5: E301 expected 1 blank line, found 0
#            ./file2.py:13:1: W293 blank line contains whitespace
#            ...
#===============================================================================


def func(arg1, arg2=None):
    '''This is the docstring of the function, explaining what it does
    its arguments, its exceptions raised and its return value

    It may be multiline or just a single line
    '''
    pass


class MyClass(object):
    '''This is the docstring of the class, explaining what it does
    '''
    def method(self, arg1, arg2=None):
        '''This is the docstring of the method, explaining what it does
        '''
        pass


# This way your code is well documented, and IDEs can display it


print func.__doc__
print
print MyClass.__doc__
print
print MyClass.method.__doc__  # Even you can access docstring


# Actually, check the beginning of this file...


#===============================================================================
# Use docstrings
#
#     - PEP8 defines this code documentation 'protocol'
#     - It consists on a string block below modules, classes and functions declaration
#     - It is possible to insert reStructuredText or EpiDoc markup
#     - There are tools to extract, display, format and convert it:
#        - Sphinx, pydoc (released with the interpreter)
#===============================================================================


#===============================================================================
# SOURCES:
# - https://pypi.python.org/pypi/setuptools
# - https://pypi.python.org/pypi/distribute
# - http://docs.python.org/2/library/copy.html#copy.deepcopy
# - http://www.python.org/dev/peps/pep-0008/
# - http://sphinx-doc.org/
#===============================================================================
