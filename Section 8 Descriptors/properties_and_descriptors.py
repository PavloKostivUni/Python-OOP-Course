from numbers import Integral

'''
class Person:
    def get_age(self):
        return getattr(self, '_age', None)
    
    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value
    
    age = property(fget=get_age, fset=set_age)

p = Person()

try:
    p.age = -10
except ValueError as ex:
    print(ex)

p.age = 10

print(p.__dict__)
'''


class TimeUTC:
    @property
    def current_time(self):
        return 'current time'

t = TimeUTC()
try:
    t.current_time = 'hello'
except AttributeError as ex:
    print(ex)
print(hasattr(TimeUTC.current_time, '__set__'))


class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
    
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
    
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable')
        return self.fget(instance)
    
    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable')
        self.fset(instance, value)
    
    def setter(self, fset):
        self.fset = fset
        return self

class Person:
    def get_name(self):
        print('get_name called...')
        return getattr(self, '_name', None)
    
    def set_name(self, value):
        print('set_name called...')
        self._name = value
    
    name = MakeProperty(fget=get_name, fset=set_name)

    @MakeProperty
    def age(self):
        return getattr(self, '_age', None)
    
    @age.setter
    def age(self, value):
        self._age = value
    

p = Person()
p.name = 'Guido'
print(p.name)
p.age = 20
print(p.age)
print(p.__dict__)