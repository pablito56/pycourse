#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 2: More useful descriptor example
'''
from datetime import datetime, timedelta

# Let's create a caching descriptor
class CachedAttribute(object):
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def __get__(self, inst, cls):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        # Let's add the result to the INSTANCE
        inst.__dict__[self.name] = self.func(inst)
        return inst.__dict__[self.name]
    def __set__(self, inst, val):
        print "Calling __set__ on instance of {0}".format(self.__class__.__name__)
        inst.__dict__[self.name] += val


# Let's use it
class MyCacheClass(object):
    def expensive_operation(self):
        from time import sleep
        sleep(5)
        return 12345
    # Note that the class and instance attribute have the same name
    attr = CachedAttribute('attr', expensive_operation)

# Let's instantiate the class
inst = MyCacheClass()
print inst.__dict__

# Let's recover the cached attribute
print inst.attr
print inst.__dict__

# Let's do it again
print inst.attr
print inst.__dict__


# Let's create a different caching descriptor
class CachedAttributeBis(object):
    def __init__(self, name, func, seconds):
        self.name = name
        self.func = func
        self.delta = timedelta(seconds=seconds)
        self.set_time = None
    def __get__(self, inst, cls):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        # Let's add the result to the INSTANCE
        if self.set_time:
            print self.set_time + self.delta, 'VS.', datetime.now()
        if self.set_time is None or self.set_time + self.delta < datetime.now():
            inst.__dict__[self.name] = self.func(inst)
            self.set_time = datetime.now()
            print "Cached at", self.set_time.isoformat()
        return inst.__dict__[self.name]

# Let's use it
class MyCacheClassBis(object):
    def expensive_operation(self):
        from time import sleep
        sleep(5)
        return 12345
    # Note that the class and instance attribute have the same name
    attr = CachedAttributeBis('attr_bis', expensive_operation, 30)

# Let's instantiate the class
inst = MyCacheClassBis()
print inst.__dict__

# Let's recover the cached attribute
print inst.attr
print inst.__dict__

# Let's do it again
print inst.attr
print inst.__dict__

# And again
print inst.attr
print inst.__dict__
