#-*- coding: utf-8 -*-
u'''
MOD: arguments and config
'''


import argparse


#===============================================================================
# - 'argparse' was introduced in 2.7 to replace 'optparse'
# - It provides additional features, like better positional args
#===============================================================================


# Let's create a command line arguments parser
parser = argparse.ArgumentParser(description='pycourse example app')

# Let's add some arguments to be parsed

# Boolean switch, False unless it is provided
parser.add_argument("-v", action="store_true", default=False)

print parser.parse_args(["-v"])
print parser.parse_args([])


# Let's customise the attribute where it is stored
parser = argparse.ArgumentParser(description='pycourse example app')
parser.add_argument("-v", action="store_true", default=False, dest="verbose")

args = parser.parse_args(["-v"])
print args.verbose


# Let's add a long argument key
parser = argparse.ArgumentParser(description='pycourse example app')
parser.add_argument("-v", "--verbose", action="store_true", default=False, dest="verbose")

args = parser.parse_args(["-v"])
print args.verbose


# Let's check the help message
try:
    print parser.parse_args(["-h"])  # It calls sys.exit, which raises SystemExit
except SystemExit:
    print "\nCatched SystemExit"


# Let's customise program name
parser = argparse.ArgumentParser(prog="example_app", description='pycourse example app')

#===============================================================================
# It is possible to change program name, description, usage message, help epilog,
#    prefix chatacters of the arguments (instead of '-' and '--'), customise how
#    conflicts are handled
#===============================================================================

# Let's customise -v help message
parser.add_argument("-v", "--verbose", action="store_true", default=False, dest="verbose",
                    help="Enable verbose behaviour, the app outputs more traces")

# Let's try it
parser.print_help()


# Let's add other type of arguments

# Int with default value (optional argument)
parser.add_argument("-n", "--num", action="store", type=int, default=0)


# String (default type), action="store" is also the default behaviour
parser.add_argument("--long_arg", dest="la", help="This string must be provided", metavar="LONG_VALUE")


# Positional command line argument (note that no str positional argument was provided to 'add_argument')
parser.add_argument(dest="pos_arg", type=int, help="This is a positional mandatory arg")

# Let's check the help message
parser.print_help()

# Let's use our new arguments
print parser.parse_args(["--verbose", "-n", "5", "--long_arg", "Hello", "12345"])

print parser.parse_args(["--verbose", "--long_arg", "Hello", "12345"])


# Let's make it fail
try:
    print parser.parse_args(["-v", "-n", "5"])  # It calls sys.exit, which raises SystemExit
except SystemExit:
    print "\nCatched SystemExit"


# Let's make it fail again
try:
    print parser.parse_args(["--verbose", "--long_arg", "Hello", "--new_arg", "12345"])
except SystemExit:
    print "\nCatched SystemExit"

#===============================================================================
# Old 'optparse' did not fail with missing or unrecognized arguments (you had to check them manually)
#===============================================================================


# Let's play a bit with actions


parser = argparse.ArgumentParser(description='pycourse example app')
parser.add_argument("-v", "--verbose", action="count", dest="verbose")
parser.add_argument("--val", action="append", dest="vals_lst", type=int)
parser.add_argument("--A", action="store_const", const="a")
parser.add_argument("--one", action="append_const", dest="nums_lst", const=1)
parser.add_argument("--two", action="append_const", dest="nums_lst", const=2)
parser.add_argument("--three", action="append_const", dest="nums_lst", const=3)


parser.print_help()


print parser.parse_args(["-vvv", "--val", "1", "--val", "12345", "--A", "--one", "--two", "--three"])


# Let's play a bit with nargs


parser = argparse.ArgumentParser(description='pycourse example app')
parser.add_argument("--values", dest="values", type=int, nargs=2)
parser.add_argument("--names", dest="names", type=str, nargs="*")
parser.add_argument("--planets", dest="planets", type=str, nargs="+")

parser.print_help()


print parser.parse_args(["--values", "12345", "6789", "--planets", "Venus", "Mars", "Earth"])


# Let's make it fail
try:
    print parser.parse_args(["--values", "12345"])
except SystemExit:
    print "\nCatched SystemExit"


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/argparse.html
#  - http://pymotw.com/2/argparse/
#===============================================================================
