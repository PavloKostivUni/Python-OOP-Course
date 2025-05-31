import sys
import types


def add(a,b):
    return a + b

print(hasattr(add, '__get__'))

me = sys.modules['__main__']

f = add.__get__(None, me)
print(f)

"""
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Alex')

def say_hello(self):
    return f'{self.name} says hello'

m = types.MethodType(say_hello, p)
print(m)
"""

class MyFunc:
    def __init__(self, func):
        self._func = func
        
    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
            return self._func
        else:
            print('__get__ called from instance')
            return types.MethodType(self._func, instance)

def hello(self):
    print(f'{self.name} says hello')

class Person:
    def __init__(self, name):
        self.name = name
    
    say_hello = MyFunc(hello)

p = Person('Alex')

print(Person.say_hello)
print(p.say_hello)
