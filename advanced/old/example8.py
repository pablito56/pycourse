#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 8: The properties, another useful implementation of descriptors
'''

# Some temperature conversion methods (Celsius, Kelvin, Fahrenheit)
def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0
def k_to_c(k):
    return k - 273.15
def c_to_k(c):
    return c + 273.15

# Let's declare a class to hold temperature measure
class MyTempClass(object):
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
    temp_celsius = property(get_temp_celsius, set_temp_celsius)
    def get_temp_fahrenheit(self):
        return c_to_f(self._temp)
    def set_temp_fahrenheit(self, val):
        self._temp = f_to_c(val)
    temp_fahrenheit = property(get_temp_fahrenheit, set_temp_fahrenheit)
    def get_temp_kelvin(self):
        return c_to_k(self._temp)
    def set_temp_kelvin(self, val):
        self._temp = k_to_c(val)
    temp_kelvin = property(get_temp_kelvin, set_temp_kelvin)
    
# Let's instantiate it
inst = MyTempClass(20)
print inst.temp_fahrenheit
print inst.temp_kelvin
inst.temp_fahrenheit = 32
print inst.temp_celsius

# Let's inspect the object
print inst.__dict__
print MyTempClass.__dict__
print MyTempClass.__dict__['temp_fahrenheit']
print MyTempClass.__dict__['temp_fahrenheit'].__get__(inst, MyTempClass)

MyTempClass.__dict__['temp_kelvin'].__set__(inst, 300)
print inst.__dict__

#===========================================================================
# - Properties are a specialized implementation of descriptors!
# - Use them when you need knowledge of class internals
# - Use descriptors for more generic logic / less coupled
#===========================================================================

#===============================================================================
# More info about descriptors:
# - Descriptors HowTo: http://docs.python.org/2/howto/descriptor.html
# - Data Model: http://docs.python.org/2/reference/datamodel.html
#
# THE END! Thanks for coming
#===============================================================================
