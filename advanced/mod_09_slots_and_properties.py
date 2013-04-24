#-*- coding: utf-8 -*-
u'''
MOD 10: Slots and properties
'''


# Let's see more examples of solutions applying descriptors


# Let's create a class with slots
class SlottedClass(object):
    __slots__ = ['attr_x', 'attr_y']

    def __init__(self, x, y):
        self.attr_x = x
        self.attr_y = y

    def sum_content(self):
        return self.attr_x + self.attr_y

# Let's instantiate
inst = SlottedClass(12345, 67890)

print inst.attr_x
print inst.attr_y         # We can access its attributes
inst.attr_x = 54321       # We can modify its attributes
print inst.sum_content()  # We can call its methods


# Ok. Nothing strange so far...


inst.attr_xyz = 54321


# Let's check the instance __dict__

print inst.__dict__


#===============================================================================
# - There is no instance __dict__
#===============================================================================

# What about the class __dict__ ?

print SlottedClass.__dict__


# How it really works internally
print SlottedClass.__dict__['attr_x'].__get__(inst, SlottedClass)  # Slots are descriptors
SlottedClass.__dict__['attr_x'].__set__(inst, 100001)
print inst.attr_x


#===========================================================================
# Slots:
# - Light control of objects structure (can be bypassed though!)
# - Faster access
# - Smaller size
#     - Improve efficiency (storage and speed)
# - Really useful to handle huge amounts of objects
#
# - Slots are implemented with descriptors
#
# - Don't forget there is no instance __dict__ when using slots
#    - There are other restrictions. Chack the documentation!
#===========================================================================


# Let's see another solution using descriptors


# Let's define some temperature conversion methods (Celsius, Kelvin, Fahrenheit)
def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def k_to_c(k):
    return k - 273.15

def c_to_k(c):
    return c + 273.15


# Time to start thinking


#==============================================================================
# EXERCISE:
#
# - Given the previous methods, how would you define a class which could store
#    and return the temperature in different scales?
#
#     >>> temp = TempClass(0)
#     >>> temp.temp_celsius
#     0
#     >>> temp.temp_fahrenheit
#     32.0
#     >>> temp.temp_kelvin
#     273.15
#     >>> temp.temp_celsius = 28
#     >>> temp.temp_fahrenheit
#     82.4
#     >>> temp.temp_kelvin
#     301.15
#==============================================================================


# Let me introduce the properties
class TempClass(object):
    def __init__(self, temp_celsius=None, temp_fahrenheit=None, temp_kelvin=None):
        if temp_celsius is not None:
            self._temp = temp_celsius
        elif temp_fahrenheit is not None:
            self._temp = f_to_c(temp_fahrenheit)
        elif temp_kelvin is not None:
            self._temp = k_to_c(temp_kelvin)
        else:
            self._temp = 0

    def get_temp_celsius(self):
        return self._temp

    def set_temp_celsius(self, val):
        self._temp = val

    # This is a property declaration
    temp_celsius = property(get_temp_celsius, set_temp_celsius)

    def get_temp_fahrenheit(self):
        return c_to_f(self._temp)

    def set_temp_fahrenheit(self, val):
        self._temp = f_to_c(val)

    # This is another property
    temp_fahrenheit = property(get_temp_fahrenheit, set_temp_fahrenheit)

    def get_temp_kelvin(self):
        return c_to_k(self._temp)

    # And another property, WITHOUT setter!
    temp_kelvin = property(get_temp_kelvin)


# Let's try it
inst = TempClass(20)
print inst.temp_fahrenheit
print inst.temp_kelvin

inst.temp_fahrenheit = 32
print inst.temp_celsius

inst.temp_kelvin = 200  # There is no setter --> modification fails

# Let's see how it works
print inst.__dict__

print TempClass.__dict__

print TempClass.__dict__['temp_fahrenheit']
print TempClass.__dict__['temp_fahrenheit'].__get__(inst, TempClass)

TempClass.__dict__['temp_celsius'].__set__(inst, 100)
print inst.__dict__


# There are property decorators
class TempClass(object):
    def __init__(self, temp_celsius=None, temp_fahrenheit=None, temp_kelvin=None):
        if temp_celsius is not None:
            self._temp = temp_celsius
        elif temp_fahrenheit is not None:
            self._temp = f_to_c(temp_fahrenheit)
        elif temp_kelvin is not None:
            self._temp = k_to_c(temp_kelvin)
        else:
            self._temp = 0

    # tmp_celsius getter
    @property
    def temp_celsius(self):
        """Temp. in Celsius"""
        return self._temp

    # tmp_celsius setter
    @temp_celsius.setter
    def temp_celsius(self, val):
        self._temp = val

    @property
    def temp_fahrenheit(self):
        """Temp. in Fahrenheit"""
        return c_to_f(self._temp)

    @temp_fahrenheit.setter
    def temp_fahrenheit(self, val):
        self._temp = f_to_c(val)

    @property
    def temp_kelvin(self):
        """Temp. in Kelvin"""
        return c_to_k(self._temp)

    @temp_kelvin.setter
    def temp_kelvin(self, val):
        self._temp = k_to_c(val)


#===========================================================================
# - Properties are a specialized implementation of descriptors!
#    - Define getters, setters, deletters and even docstrings used instead
#        of direct attribute access
#    - Alternative declaration with decorators
#
# - Use them to keep retrocompatibility with direct attribute access
# - Use them when you need knowledge of class internals
# - Use descriptors for more generic logic or less coupled solutions
#===========================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/reference/datamodel.html#slots
#  - http://docs.python.org/2/library/functions.html#property
#===============================================================================
