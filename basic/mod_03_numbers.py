#-*- coding: utf-8 -*-
'''
MOD 03: Numbers
'''


spam = 65              # an integer declaration. Yes, no semicolon ; at the end
print spam             # print is a reserved keyword / statement

print type(spam)       # this is a function call

#===============================================================================
# WARNING!
#    - 'type' is std lib function to retrieve the type of an object
#    - Never use 'type' in your code for type checking, only for demo or debugging purposes
#        - We will talk about it later in duck typing module
#===============================================================================

eggs = 2
print eggs
print type(eggs)

# Let's see the numeric operations

print spam + eggs      # sum

print spam - eggs      # difference

print spam * eggs      # product

print spam / eggs      # quotient

print spam // eggs     # floored quotient

print spam % eggs      # remainder or module

print pow(spam, eggs)  # power (yes, this is how a function is called)

print spam ** eggs     # power

fooo = -2              # negative value
print fooo
print type(fooo)

print -fooo            # negated

print +fooo            # unchanged

print abs(fooo)        # absolute value

print int(fooo)        # convert to integer

print long(fooo)       # convert to long integer

print float(fooo)      # convert to float

fooo += 1              # auto incremental (there is no ++)
print fooo

# More on the quotient

print spam / eggs          # quotient
print spam / float(eggs)   # quotient
print spam // float(eggs)  # floored quotient, aka. integer division

# More on the operations result type

print type(spam + eggs)
print type(long(spam) + eggs)
print type(float(spam) + eggs)
print type(float(spam) + long(eggs))

#===============================================================================
# - Python automatically infers the type of the result depending on operands type
#===============================================================================

# Let's try again the power

print eggs ** spam
print type(eggs ** spam)

from sys import maxint
print maxint

#===============================================================================
# - Python automatically converts integers into longs
#===============================================================================


# Let's instantiate other values

spam = 65L             # a long
print spam
print type(spam)

eggs = 2.0             # a float
print eggs
print type(eggs)

spam = 0101             # an integer in octet
print spam
print type(spam)

spam = 0x41            # an integer in hexadecimal
print spam
print type(spam)

# Let's do more complex operations

print round(spam + eggs / spam, 3)    # round to n digits, 0 by default
print round((spam + eggs) / spam, 3)  # round to n digits, 0 by default
print round(spam + (eggs / spam), 3)  # round to n digits, 0 by default


#===============================================================================
# - Use parentheses to alter operations order
#===============================================================================


#===============================================================================
# Python numeric types:
#  - int:
#     - Traditional integer
#     - Implemented using long in C, at least 32 bits precision
#     - Its values are [-sys.maxint - 1, sys.maxint]
#  - long:
#     - Long integer with unlimited precision
#     - Created automatically or when an L suffix is provided
#  - float:
#     - Floating point number
#     - Specified with a dot . as decimals separator
#     - Implemented using double in C
#     - Check sys.float_info for its internal representation
#
#  - Standard library also provides other built-in numeric formats:
#     - complex: using a float for real and imaginary part
#     - fractions: to hold rationals
#     - decimal: floating to hold user-defined precision
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
#===============================================================================
