#-*- coding: utf-8 -*-
u"""
MOD: ConfigParser
"""


from ConfigParser import SafeConfigParser


#===============================================================================
# - ConfiParser module provides several classes
#   - RawConfigParser: The basic configuration parser object
#   - ConfigParser: Subclass of the previous, with interpolation and more options
#   - SafeConfigParser: Alternative of the previous, more "sane" and predictable
#===============================================================================


# Let's create a config file
filename = "basic.cfg"
cfg = """
[sectionA]
param1 = 5
param2 = hello
param3 = 0.5
param4 = false
param5 =
"""
with open(filename, "w") as f:
    f.write(cfg)


# Let's create the parser
parser = SafeConfigParser()
print parser.read(filename)  # Returns list of files parsed

# Let's use it
print repr(parser.get("sectionA", "param1"))  # By default strings are returned
print repr(parser.get("sectionA", "param2"))
print repr(parser.get("sectionA", "param3"))
print repr(parser.get("sectionA", "param4"))
print repr(parser.get("sectionA", "param5"))  # Empty string is read


# Let's retrieve other types
print repr(parser.getint("sectionA", "param1"))
print repr(parser.getfloat("sectionA", "param3"))
print repr(parser.getboolean("sectionA", "param4"))


# Let's check loaded files sections
print parser.sections()
print parser.has_section("sectionB")


# Let's check loaded files options
print parser.options("sectionA")
print parser.has_option("sectionA", "param1")
print parser.has_option("sectionA", "param5")  # Actually it exists, although is empty
print parser.has_option("sectionA", "param6")
print parser.items("sectionA")


# Let's work with more files and sections


# Let's create a new config file
filename2 = "advanced.ini"
cfg = """
[sectionA]
param1 = 11111
param2 = byebye
paramN = Nth param

[sectionB]
host = localhost
port = 80
url = https://%(host)s:%(port)s
"""
with open(filename2, "w") as f:
    f.write(cfg)


# Let's load three configuration files
print parser.read([filename, filename2, "does_not_exist.cfg"])  # Files not found are ignored


# Let's check the configuration available
print parser.items("sectionA")  # Order of files in read matters
print parser.items("sectionB")  # This is how interpolation works


# Let's check how options are found


filename = "conf.ini"
cfg = """
[DEFAULT]
paramC = param C section DEFAULT value

[sectionA]
paramB = param B section A value
"""
with open(filename, "w") as f:
    f.write(cfg)


# Let's read the new config file
defaults = {"paramD": "param D defaults value"}
parser = SafeConfigParser(defaults=defaults)
print parser.read(filename)


# Let's check the configuration available
vars = {"paramA": "param A vars value"}
print repr(parser.get("sectionA", "paramA", vars=vars))
print repr(parser.get("sectionA", "paramB", vars=vars))
print repr(parser.get("sectionA", "paramC", vars=vars))
print repr(parser.get("sectionA", "paramD", vars=vars))

print repr(parser.get("sectionA", "paramE", vars=vars))  # Note option names are not case sensitive
print repr(parser.get("sectionB", "paramE", vars=vars))


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/argparse.html
#  - http://pymotw.com/2/argparse/
#===============================================================================
