#-*- coding: utf-8 -*-
u'''
MOD 08: Flow control
'''

# Let's start with the conditional execution

spam = [1, 2, 3]  # True
eggs = ""         # False

if spam:
    print "spam is True"
else:
    print "spam is False"

print "outside the conditional"  # Notice that there's is no closing fi statement


if spam:
    print "spam is True"
else:
    print "spam is False"

    print "still inside the conditional"


#==============================================================================
# REMEMBER:
# - Indentation is Python's way of grouping statements!!
#    - Typically four spaces per indentation level
#    - No curly brackets { } or semicolons ; used anywhere
#    - This enforces a more readable code
#==============================================================================


if eggs:
    print "eggs is True"
elif spam:
    print "eggs is False and spam is True"
else:
    print "eggs and spam are False"


if eggs:
    print "eggs is True"
elif max(spam) > 5:
    print "eggs is False and second condition is True"
elif len(spam) == 3 and not eggs is None:
    print "thirs condition is true"
else:
    print "everything is False"


# Let's see the ternary operator


spam = [1, 2, 3]  # True
eggs = ""         # False

print "first option" if spam else "second option"

print "first option" if eggs else "second option"

print "first option" if eggs else "second option" if spam else "last option"  # We can even concatenate them

print "first option" if eggs else ("second option" if spam else "last option")


# Time for the while loop


spam = [1, 2, 3]
while len(spam) > 0:
    print spam.pop(0)

spam = [1, 2, 3]
idx = 0
while idx < len(spam):
    print spam[idx]
    idx += 1


# What about the for loop?


spam = [1, 2, 3]
for item in spam:        # The for loop only iterates over the items of a sequence
    print item

spam = [1, 2, 3]
for item in spam[::-1]:  # As we saw, slicing may be slow. Keep it in mind
    print item


eggs = "eggs"
for letter in eggs:      # It can loop over characters of a string
    print letter


spam = {"one": 1,
        "two": 2,
        "three": 3}
for key in spam:         # Or even it can iterate through a dictionary
    print spam[key]      # Note that it iterates over the keys of the dictionary


# Let's see how to interact with loops iterations

spam = [1, 2, 3]
for item in spam:
    if item == 2:
        break
    print item


#===============================================================================
# - break statement halts a loop execution (inside while or for)
# - Only affects the closer inner (or smallest enclosing) loop
#===============================================================================


# A bit more complicated example
spam = ["one", "two", "three"]
for item in spam:                 # This loop is never broken
    for letter in item:
        if letter in "wh":        # Check if letter is either 'w' or 'h'
            break                 # Break only the immediate inner loop
        print letter
    print                         # It prints a break line (empty line)

# A bit different example
spam = ["one", "two", "three"]
for item in spam:
    for letter in item:
        if letter in "whe":       # Check if letter is either 'w', 'h' or 'e'
            continue              # Halt only current iteration, but continue the loop
        print letter
    print


#===============================================================================
# - continue statement halts current iteration (inside while or for)
# - loops continue its normal execution
#===============================================================================


spam = [1, 2, 3, 4, 5, 6, 7, 8]
eggs = 5
while len(spam) > 0:
    value = spam.pop()
    if value == eggs:
        print "Value found:", value
        break
else:                                      # Note that else has the same indentation than while
    print "The right value was not found"


spam = [1, 2, 3, 4, 6, 7, 8]
eggs = 5
while len(spam) > 0:
    value = spam.pop()
    if value == eggs:
        print "Value found:", value
        break
else:
    print "The right value was not found"

#===============================================================================
# - else clause after a loop is executed if all iterations were run without break statement called
#===============================================================================


spam = [1, 2, 3]
for item in spam:
    pass

#===============================================================================
# - pass statement is Python's noop (does nothing)
#===============================================================================


# Let's check exception handling

spam = [1, 2, 3]
try:
    print spam[5]
except:             # Use try and except to capture exceptions
    print "Failed"


spam = {"one": 1, "two": 2, "three": 3}
try:
    print spam[5]
except IndexError, e:      # Inside the except clause 'e' will contain the exception instance
    print "IndexError", e
except KeyError, e:        # Use several except clauses for different types of exceptions
    print "KeyError", e


try:
    print 65 + "spam"
except (IndexError, KeyError), e:  # Or even group exception types
    print "Index or Key Error", e
except TypeError, e:
    print "TypeError", e

try:
    print 65 + 2
except (IndexError, KeyError), e:
    print "Index or Key Error", e
except TypeError, e:
    print "TypeError", e
else:
    print "No exception"           # Use else clause to run code in case no exception was raised

try:
    print 65 + "spam"
    raise AttributeError           # Use 'raise' to launch yourself exceptions
except (IndexError, KeyError), e:
    print "Index or Key Error", e
except TypeError, e:
    print "TypeError", e
else:
    print "No exception"
finally:
    print "Finally we clean up"    # Use finally clause to ALWAYS execute clean up code

try:
    print 65 + 2
except (IndexError, KeyError), e:
    print "Index or Key Error", e
    raise                          # Use 'raise' without arguments to relaunch the exception
except TypeError, e:
    print "TypeError", e
else:
    print "No exception"
finally:
    print "Finally we clean up"    # Use finally clause to ALWAYS execute clean up code


# Let's see another construction

try:
    f = open("tmp_file.txt", "a")
except:
    pass  # Do something
else:
    try:
        f.write("I'm writing to a file...\n")
    except:
        pass  # Do something
    finally:
        f.close()


# Not pythonic, too much code for only three real lines

try:
    with open("tmp_file.txt", "a") as f:
        f.write("I'm writing to a file...\n")
except:
    pass  # Do something

# Where is the file closed? What happens if an exception is raised?


#===============================================================================
# Python context managers
#  - Encapsulate common patterns used wrapping code blocks where real runs the program logic
#     -  Usually try/except/finally patterns
#  - Several uses:
#     - Automatic cleanup, closing files or network or DB connections when exiting the context block
#     - Set temporary environment, like enable/disable logging, timing, profiling...
#  - Use the 'with' and optionally the 'as' statements to open a context manager
#     - It is automatically closed when code execution goes outside the block
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/controlflow.html#if-statements
#  - http://docs.python.org/2/reference/compound_stmts.html
#  - http://docs.python.org/2/reference/expressions.html#conditional-expressions
#  - http://docs.python.org/2/reference/simple_stmts.html
#  - http://www.python.org/dev/peps/pep-0343/
#  - http://docs.python.org/2/reference/compound_stmts.html#the-with-statement
#===============================================================================
