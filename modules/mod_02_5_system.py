#-*- coding: utf-8 -*-
u"""
MOD: system, filesystem and commands access
"""


import sys


#===============================================================================
# - Module 'sys' provides access tools to interact with the interpreter
#===============================================================================


# Some examples


# Retrieve command line arguments
print sys.argv


# Exit from Python (raises SystemExit exception)
try:
    sys.exit(-1)
except SystemExit:
    print "Catched SystemExit exception"


# Get floats codification details
print sys.float_info


# Default system encoding
print sys.getdefaultencoding()


# Get the PYTHONPATH
print sys.path


# Get current platform
print sys.platform


# Get current Python and C API versions
print sys.version
print sys.api_version
print sys.version_info


# Time for another module


import os


#===============================================================================
# - Module 'os' provides a portable way of using operating system dependent functionality.
#===============================================================================


# Examples


# Get current environment variables
print os.environ
print os.getenv("PATH")
os.putenv("NEW_ENV_VAR", "hello")
print os.getenv("NEW_ENV_VAR")


# Operate with current working directory
os.chdir("exercises")
print os.getcwd()
os.chdir("..")
print os.getcwd()


# Get current user and group
print os.getgid()
print os.getuid()


# Operate with folders
os.mkdir("test_folder")
os.chmod("test_folder", 777)
print os.listdir(".")
print os.listdir("test_folder")
os.rmdir("test_folder")


#===============================================================================
# - File management tools are also in 'os' module
#    - 'os.remove', 'os.chown'...
#    - Actully 'open' function maps to 'os.open'
#===============================================================================


# Interact with paths (os.path)
print os.path.abspath(".")
print os.path.split(os.__file__)
print os.path.isdir(os.path.dirname(os.__file__))


# Time for another module


import shutil


#===============================================================================
# - Module 'shutil' provides high-level operations on files
#    - 'shutil.copy2', 'shutil.copytree', 'shutil.rmtree'...
#===============================================================================


import subprocess


#===============================================================================
# - 'subprocess' module allows you to spawn new processes, connect to their
#    input/output/error pipes, and obtain their return codes.
#    - In other words, launch other commands (locally)
#===============================================================================


# Execute a command and get its return code
ret = subprocess.call(["ls", "-lAhtr"], shell=True)
print ret

# Only check command execution
subprocess.check_call(["ls", "does_not_exist"])

# Execute a command and get its output
out = subprocess.check_output(["ls", "-lAhtr"])
print out


# Time for next module


import atexit


#===============================================================================
# - 'atexit' module provides a single function to register cleanup functions.
# - Cleanup functions are automatically executed upon normal interpreter termination.
# - The order in which the functions are called is not defined;
#===============================================================================


def say_bye_bye():
    print "Closing. Bye bye!!"

atexit.register(say_bye_bye)



#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/sys.html
#  - http://pymotw.com/2/sys/
#  - http://docs.python.org/2/library/os.html
#  - http://pymotw.com/2/os/
#  - http://docs.python.org/2/library/shutil.html
#  - http://pymotw.com/2/shutil/
#  - http://docs.python.org/2/library/subprocess.html
#  - http://pymotw.com/2/subprocess/
#  - http://docs.python.org/2/library/atexit.html
#  - http://pymotw.com/2/atexit/
#===============================================================================
